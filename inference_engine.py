# =========================
# Inference Engine
# =========================
# Generic forward-chaining engine.

from working_memory import facts, fired, trace, assert_fact, has_fact

rules = []


def defrule(name, if_patterns, then_asserts):
    """Register a rule into the knowledge base."""
    rules.append({
        "name": name,
        "if":   if_patterns,
        "then": then_asserts,
    })


def run_engine():
    """
    Forward chaining: keeps looping through all rules repeatedly
    until a full pass produces zero new facts (match-resolve-act cycle).
    """
    changed = True
    while changed:
        changed = False
        for r in rules:
            if r["name"] in fired:
                continue

            # Check all conditions against working memory
            ok = all(has_fact(slot, value) for (slot, value) in r["if"])

            if ok:
                fired.add(r["name"])
                new_facts = []
                for (slot, value) in r["then"]:
                    if assert_fact(slot, value):
                        changed = True
                        new_facts.append(f"({slot}: {value})")

                if new_facts:
                    conditions = ", ".join(f"({s}: {v})" for (s, v) in r["if"])
                    trace.append(
                        f"Rule '{r['name']}' fired.\n"
                        f"  Conditions matched : {conditions}\n"
                        f"  New facts asserted : {', '.join(new_facts)}"
                    )

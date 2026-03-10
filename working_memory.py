# =========================
# Working Memory
# =========================
# Holds everything currently known to be true during a session.
# Grows as the user answers questions and as rules fire.

facts = set()   # stores tuples like ("goal", "Stay healthy")
fired = set()   # rule names that already fired
trace = []      # explanation trace: list of strings describing what fired and why


def reset():
    """Reset all global state so main() can be safely called multiple times."""
    facts.clear()
    fired.clear()
    trace.clear()


def assert_fact(slot, value):
    """Assert a fact like (slot, value). Return True if newly added."""
    f = (slot, value)
    if f in facts:
        return False
    facts.add(f)
    return True


def has_fact(slot, value):
    return (slot, value) in facts


def get_fact_value(slot):
    """Get the first value for a slot (if any)."""
    for (s, v) in facts:
        if s == slot:
            return v
    return None


def get_all_values(slot):
    """Get all values for a given slot."""
    return [v for (s, v) in facts if s == slot]

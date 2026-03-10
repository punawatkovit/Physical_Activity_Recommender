# =========================
# Main
# =========================
# Entry point. Handles all user interaction and output.

import knowledge_base as kb
from working_memory import reset, assert_fact, has_fact, get_all_values
from inference_engine import run_engine


# =========================
# I/O helpers
# =========================

def ask_yes_no(prompt):
    while True:
        ans = input(f"{prompt} (yes/no): ").strip().lower()
        if ans.startswith("y"):
            return "yes"
        if ans.startswith("n"):
            return "no"
        print("  Please type yes or no.")


def ask_choice(prompt, choices):
    print(f"\n{prompt}")
    for i, c in enumerate(choices, 1):
        print(f"  {i}) {c}")
    while True:
        raw = input("Choose a number: ").strip()
        try:
            idx = int(raw)
            if 1 <= idx <= len(choices):
                return choices[idx - 1]
        except ValueError:
            pass
        print(f"  Please enter a number between 1 and {len(choices)}.")


# =========================
# Output helpers
# =========================

def print_header():
    print("\n" + "=" * 55)
    print("    🏃  Physical Activity Expert System")
    print("=" * 55)


def print_section(title):
    print(f"\n{'—' * 55}")
    print(f"  {title}")
    print(f"{'—' * 55}")


def print_summary(mode, goal, env, time):
    print_section("Your Preferences")
    print(f"  Mode        : {mode}")
    print(f"  Goal        : {goal}")
    print(f"  Environment : {env}")
    print(f"  Time        : {time}")


def print_stop_result():
    print_section("⚠️  Health Screening Result")
    print(f"\n  {kb.STOP_MESSAGE}\n")


def print_recommendations(recs):
    print_section("✅  Recommended Activities")
    if not recs:
        print(
            "\n  No recommendation could be matched for your inputs.\n"
            "  Please review your answers or consult a fitness professional."
        )
        return
    for i, r in enumerate(recs, 1):
        desc = kb.ACTIVITY_DESC.get(r, "No description available.")
        print(f"\n  {i}. {r}")
        print(f"     {desc}")


def print_explanation():
    from working_memory import trace
    print_section("🔍  Explanation (Rules That Fired)")
    if not trace:
        print("\n  No rules fired.")
        return
    for i, entry in enumerate(trace, 1):
        print(f"\n  [{i}] {entry}")


# =========================
# Main
# =========================

def main():
    reset()
    print_header()

    # --- APSS Screening ---
    print_section("APSS Health Screening (answer yes or no)")
    for slot, question in kb.APSS_QUESTIONS:
        answer = ask_yes_no(f"  Q: {question}")
        assert_fact(slot, answer)

    # Run engine early to check for stop
    run_engine()

    if has_fact("stop", "true"):
        print_stop_result()
        print_explanation()
        return

    # --- Preferences ---
    print_section("Your Activity Preferences")
    mode = ask_choice("How do you prefer to exercise?", ["On my own", "Group-based"])
    goal = ask_choice("What is your main goal?",        ["Stay healthy", "Lose weight/fat", "Gain strength"])
    env  = ask_choice("Preferred environment?",         ["Indoor", "Outdoor", "Either"])
    time = ask_choice("How much time do you have?",     ["<75 minutes", ">=75 minutes"])

    # Normalise time label to match rule patterns (<75 / >=75)
    time_key = "<75" if time.startswith("<") else ">=75"

    assert_fact("mode", mode)
    assert_fact("goal", goal)
    assert_fact("env",  env)
    assert_fact("time", time_key)

    # Run engine again with preferences asserted
    run_engine()

    # --- Output ---
    print_summary(mode, goal, env, time)

    recs = get_all_values("recommend")
    # Deduplicate while preserving order
    seen = set()
    ordered_recs = []
    for r in recs:
        if r not in seen:
            seen.add(r)
            ordered_recs.append(r)

    print_recommendations(ordered_recs)

    # Ask if user wants to see the explanation trace
    print()
    show = ask_yes_no("Would you like to see which rules fired (explanation)?")
    if show == "yes":
        print_explanation()

    print(f"\n{'=' * 55}\n")


if __name__ == "__main__":
    main()

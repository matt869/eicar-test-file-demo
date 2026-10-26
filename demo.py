#!/usr/bin/env python3
"""Print a harmless, console-only security incident simulation."""


def main() -> None:
    print("=== SECURITY DEMO: SIMULATED INCIDENT ===")
    print("This is a fictional walkthrough; no system changes are made.")
    print()

    events = (
        "A suspicious attachment is reported by a user.",
        "The security team records the report for triage.",
        "The affected device is marked for investigation (simulation only).",
        "The team reviews the alert and documents next steps.",
        "The exercise ends; no files or settings were changed.",
    )

    for number, event in enumerate(events, start=1):
        print(f"[{number}/{len(events)}] {event}")

    print()
    print("=== DEMO COMPLETE ===")


if __name__ == "__main__":
    main()

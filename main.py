#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

The line: my houseplants died of neglect, so I replaced them with
plastic ones. The plastic ones are thriving. I am not sure what that
says about me — the joke lands on the turn from dead plants to the
speaker's own self-assessment.
"""
import os

LINE = "My plants died of neglect, so I bought plastic ones. They are thriving — and honestly, I am not sure what that says about me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()

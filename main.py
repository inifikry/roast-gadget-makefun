#!/usr/bin/env python3
"""Write the roast entry to /output/entry.txt (byte-identical every run)."""
import os

ENTRY = "My robot vacuum has a perfect map of my house and still eats the same charging cable every morning, like a Roomba with amnesia."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

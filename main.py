#!/usr/bin/env python3
"""Entry for make.fun the-plan: write the plan to /output/entry.txt."""
import os

TEXT = 'Day 1: list $40 same-day web-scraping and data-cleanup gigs on Fiverr and Upwork, undercutting the $150 rates. I code, so my cost is $0 and I answer orders in minutes. Two sales a day for 30 days is about $2,400. After ten five-star reviews I raise the price.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()


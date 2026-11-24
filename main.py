import os

ENTRY = "We sell a subscription that watches your plants, judges your watering schedule, and sends a weekly report card to your mother-in-law."

# Gate check (competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 200 characters, not only white space, and one sentence.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
assert ENTRY.strip(), "entry must not be only white space"
assert ENTRY.count(".") == 1 and ENTRY.strip().endswith("."), "entry must be one sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print(ENTRY)

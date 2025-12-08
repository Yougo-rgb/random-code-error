import random

errors = []

# Open errors.txt and add every line withour whitespace
with open("errors.txt", "r", encoding="utf-8") as f:
    for line in f:
        stripped_line = line.strip()
        if stripped_line:
            errors.append(stripped_line)

# Select a random error
chosen = random.choice(errors)

# Write the chosen error on ERROR.md
with open("ERROR.md", "w", encoding="utf-8") as f:
    f.write(f"```txt\n{chosen}\n```")
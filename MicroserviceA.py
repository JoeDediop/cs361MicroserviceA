import random
import string
import os
import time

# Expanded syllable chunks for fantasy name generation
syllables_start = [
    "Thal", "Vor", "Mal", "Zor", "Ela", "Kel", "Shi", "Lyr", "Dur", "Gal", "Fen", "Rav", "Tor", "Bryn",
    "Sar", "Mor", "Taz", "Nel", "Xal", "Yr", "Dav", "Bel", "Kra", "Nor", "Sol", "Zen", "Val", "Nar",
    "Ith", "Eld", "Or", "Gar", "Drak", "Sul", "Jor", "Xer", "Lor", "Quil", "Pal", "Yen", "Bra", "Cal"
]

syllables_end = [
    "nor", "dris", "gor", "an", "reth", "da", "ion", "lyn", "ara", "orn", "las", "thas", "dor", "vin",
    "grim", "rok", "mar", "don", "ren", "vor", "kin", "zan", "gal", "sol", "rad", "tur", "tash", "myr",
    "fal", "rix", "dul", "bar", "za", "ash", "dom", "var", "rek", "rian", "lor", "vir", "kan", "tar"
]

def add_fantasy_element(name):
    """Adds fantasy elements (e.g., apostrophes, suffixes) to a name with a 10% probability."""
    if random.random() < 0.1:
        if random.choice([True, False]):
            # Insert an apostrophe in a random position
            pos = random.randint(1, len(name) - 1)
            name = name[:pos] + "'" + name[pos:]
        else:
            # Append a random fantasy suffix
            suffix = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
            name += suffix
    return name

def generate_fantasy_name():
    """Generates a fantasy-style name from syllable chunks."""
    first_name = random.choice(syllables_start) + random.choice(syllables_end)
    last_name = random.choice(syllables_start) + random.choice(syllables_end)

    # Add fantasy elements to first or last name randomly
    first_name = add_fantasy_element(first_name)
    last_name = add_fantasy_element(last_name)

    return f"{last_name}, {first_name}"

def generate_names(amount=1):
    """Generates a list of fantasy names based on the specified amount."""
    return [generate_fantasy_name() for _ in range(amount)]

def process_request(file_path):
    """Processes the request in the text file by generating names."""
    with open(file_path, "r") as file:
        content = file.read().strip()

    # Check for the request command and amount
    if content.startswith("run"):
        try:
            amount = int(content.split("amount=")[-1])
            names = [generate_fantasy_name() for _ in range(amount)]
            output = "; ".join(names)

            # Write the generated names back to the file
            with open(file_path, "w") as file:
                file.write(output)

            print("Generated names written to the file.")
        except ValueError:
            print("Invalid amount specified in the request.")
    else:
        print("No valid 'run' command found in the file.")

def watch_file(file_path):
    """Continuously watches the file for new requests."""
    last_modified_time = os.path.getmtime(file_path)

    while True:
        try:
            # Check if the file has been modified
            current_modified_time = os.path.getmtime(file_path)
            if current_modified_time != last_modified_time:
                print("Change detected, processing request...")
                process_request(file_path)
                last_modified_time = current_modified_time

            # Check every second for changes
            time.sleep(1)

        except KeyboardInterrupt:
            print("Microservice stopped.")
            break

        except FileNotFoundError:
            print("Request file not found. Waiting for it to be created...")
            time.sleep(1)

# Specify the path to the request file
file_path = "request.txt"
watch_file(file_path)

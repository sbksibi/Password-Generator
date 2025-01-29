import itertools
import re
from datetime import datetime

def generate_company_passwords(company_name, min_length=8):
    if not company_name.strip():
        return []

    current_year = datetime.now().year
    next_year = current_year + 1
    current_month = datetime.now().month
    seasons = ["Winter", "Spring", "Summer", "Fall"]
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December",
              "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    common_suffixes = ["123", "1234", "!", "@123", "#", "$", "2024", str(current_year), str(next_year), "999"]
    special_chars = ["!", "@", "#", "$", "%", "&", "*", "_", "-", ".", "+", "="]
    common_prefixes = ["Welcome", "Admin", "Secure", "Pass", "Login", "Root", "User", "Staff", "System"]
    number_sequences = ["123", "1234", "12345", "123456", "999", "000", "007", "101", "777", "666"]
    corporate_suffixes = ["Inc", "LLC", "Ltd", "Corp", "Co", "Group"]
    department_names = ["HR", "IT", "Finance", "Admin", "Sales", "Support", "Tech", "Service"]
    keyboard_walks = ["1qaz2wsx", "1q2w3e4r", "qwerTY123", "1qaz@WSX", "zaq1@WSX",
                      "!QAZ2wsx", "1qazxsw2", "1qazXSW@", "2wsx3edc", "3edc4rfv"]

    # Generate company base words with variations
    company_parts = re.findall(r'\w+', company_name)
    base_words = []
    separators = ['', '-', '_', '.', '@', '$', '!', '%']

    # Generate combined terms with separators and case variations
    for sep in separators:
        combined = sep.join(company_parts)
        if combined:
            base_words.append(combined.lower())
            base_words.append(combined.upper())
            base_words.append(combined.capitalize())
            if len(company_parts) > 1:
                camel_case = ''.join([part.capitalize() for part in company_parts])
                base_words.append(camel_case)

    # Add corporate suffixes and departments
    for suffix in corporate_suffixes + department_names:
        base_words.extend([suffix.lower(), suffix.upper(), suffix.capitalize()])

    # Leet speak conversion
    def leet_speak(text):
        leet_map = {
            'a': '@', 'A': '@', 'e': '3', 'E': '3',
            'i': '1', 'I': '1', 'o': '0', 'O': '0',
            's': '$', 'S': '$', 't': '7', 'T': '7',
            'g': '9', 'G': '9', 'b': '8', 'B': '8'
        }
        return ''.join(leet_map.get(c, c) for c in text)

    leet_words = [leet_speak(word) for word in base_words]
    base_words += leet_words

    # Generate passwords using itertools.product for efficiency
    passwords = set()

    # Combine with suffixes/prefixes
    for prefix, word, suffix, char in itertools.product(common_prefixes, base_words, common_suffixes, special_chars):
        passwords.update({
            f"{prefix}{char}{word}",
            f"{word}{char}{suffix}",
            f"{prefix}{word}{suffix}",
            f"{word}{suffix}{char}"
        })

    # Date and month combinations
    date_formats = [
        f"{current_month:02d}{current_year}",
        f"{current_month:02d}{next_year}",
        f"{current_year}",
        f"{next_year}",
        datetime.now().strftime("%m%d%Y"),
        datetime.now().strftime("%d%m%Y")
    ]
    for word, date_str in itertools.product(base_words, date_formats):
        passwords.add(f"{word}{date_str}")
        passwords.add(f"{word}@{date_str}")

    # Seasonal and month-based passwords
    for season, month in itertools.product(seasons, months[:12]):
        passwords.update({
            f"{season}{current_year}",
            f"{month}{next_year}",
            f"{season}@{current_year}",
            f"{month}@{next_year}"
        })

    # Corporate and department combinations
    for corp, dept in itertools.product(corporate_suffixes, department_names):
        passwords.update({
            f"{corp}{dept}{current_year}",
            f"{dept}{corp}{next_year}",
            f"{corp}@{dept}",
            f"{dept}#{corp}"
        })

    # Add keyboard walks and common passwords
    passwords.update(keyboard_walks)
    passwords.update([
        "admin", "administrator", "admin@123", "password", "password1",
        "123456", "123456789", "qwerty", "abc123", "letmein", "welcome",
        "monkey", "1234", "12345", "12345678", "football", "iloveyou",
        "123123", "baseball", "sunshine", "ashley", "bailey", "dragon",
        "superman", "master", "hello", "freedom", "whatever", "qazwsx",
        "trustno1", "Password123", "Admin123!"
    ])

    # Filter by minimum length if specified
    if min_length > 0:
        passwords = {pwd for pwd in passwords if len(pwd) >= min_length}

    return sorted(passwords)

def save_passwords(passwords, filename="passwords.txt"):
    with open(filename, "w") as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Generated {len(passwords)} passwords. Saved to {filename}")

if __name__ == "__main__":
    company = input("Enter company name: ").strip()
    if not company:
        print("Company name cannot be empty!")
    else:
        passwords = generate_company_passwords(company)
        save_passwords(passwords)
import itertools
import re
from datetime import datetime

def generate_company_passwords(company_name, min_length=8):
    if not company_name.strip():
        return []

    # Temporal configurations
    current_year = datetime.now().year
    short_year = str(current_year)[-2:]
    next_year = current_year + 1
    current_month = datetime.now().month
    
    # Pattern components
    components = {
        'seasons': ["Winter", "Spring", "Summer", "Fall"],
        'months': ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December",
                  "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        'special_chars': ["!", "@", "#", "$", "%", "&", "*", "_", "-", ".", "+", "="],
        'tech_terms': ["Server", "Cloud", "Data", "Network", "Tech", "IT", "Dev", "Prod", "Test", "Web", "App"],
        'number_patterns': ["1", "0", "123", "007", "2024", "2023", "100", "200", "99", "66", "1234", "888"],
        'corporate_terms': ["Inc", "LLC", "Ltd", "Corp", "Co", "Group", "Global", "Solutions"],
        'departments': ["HR", "IT", "Finance", "Sales", "Support", "Service", "Ops", "Dev"],
        'keyboard_walks': ["1qaz2wsx", "1q2w3e4r", "qwerTY123", "1qaz@WSX", "zaq1@WSX"],
        'common_passwords': ["Admin123!", "Password1", "Welcome123", "Secure@2024", "Summer2024"]
    }

    # Company name processing
    processed_name = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', company_name)
    company_parts = re.findall(r'\w+', processed_name)
    
    # Base word generation
    base_words = set()
    separators = ['', '-', '_', '.', '@', '$', '!', '%', '&', '*']
    
    # Generate base variations
    for sep in separators:
        combined = sep.join(company_parts)
        if combined:
            # Case variations
            variations = {
                combined.lower(),
                combined.upper(),
                combined.capitalize(),
                combined.swapcase(),
                combined[:1].upper() + combined[1:].lower()
            }
            base_words.update(variations)
            
            # Number inserted variations
            for num in components['number_patterns']:
                base_words.add(f"{combined}{num}")
                base_words.add(f"{num}{combined}")
                base_words.add(f"{combined[:2]}{num}{combined[2:]}")
    
    # Acronym generation
    def generate_acronyms(parts):
        acronym = "".join(p[0] for p in parts)
        return {
            acronym.lower(),
            acronym.upper(),
            f"{acronym.lower()}{short_year}",
            f"{acronym.upper()}{current_year}",
            f"{acronym}@{current_year}",
            f"{acronym}#{next_year}"
        }
    
    acronyms = generate_acronyms(company_parts) if len(company_parts) > 1 else set()
    base_words.update(acronyms)
    
    # Leet speak transformations
    def leet_transform(text):
        substitutions = {
            'a': ['@', '4'], 'e': ['3'], 'i': ['1', '!'],
            'o': ['0'], 's': ['$', '5'], 't': ['7'],
            'g': ['9'], 'b': ['8'], 'z': ['2'],
            'l': ['1'], 'k': ['|<'], 'm': ['^^']
        }
        transformed = [text]
        for char, replacements in substitutions.items():
            for r in replacements:
                transformed.append(text.lower().replace(char, r))
                transformed.append(text.upper().replace(char.upper(), r))
        return transformed
    
    leet_words = set()
    for word in base_words:
        leet_words.update(leet_transform(word))
    base_words.update(leet_words)
    
    # Password pattern generation
    passwords = set()
    
    # Core pattern generator
    def generate_core_patterns():
        # Acronym-based patterns
        for acronym, term, year, sep in itertools.product(
            acronyms,
            components['tech_terms'] + components['departments'],
            [str(current_year), str(next_year), short_year],
            components['special_chars']
        ):
            passwords.update({
                f"{acronym}{term}{sep}{year}",  
                f"{term}{sep}{acronym}{year}",  
                f"{acronym}{sep}{year}{term}",  
                f"{term}{year}{sep}{acronym}"   
            })
        
        # Mirrored patterns
        for base, num, sep in itertools.product(
            base_words,
            components['number_patterns'],
            components['special_chars']
        ):
            passwords.add(f"{base}{sep}{num}{sep}{base}".lower())  
            passwords.add(f"{num}{sep}{base}{sep}{num}")           
        
        # Department-tech patterns
        for dept, tech, sep in itertools.product(
            components['departments'],
            components['tech_terms'],
            components['special_chars']
        ):
            passwords.add(f"{dept}{sep}{tech}{current_year}")  # IT@Server2024
            passwords.add(f"{tech}{sep}{dept}{next_year}")     # Server@IT2025
        
        # Date-based patterns
        date_formats = [
            f"{current_month:02d}{current_year}",
            f"{current_month:02d}{next_year}",
            datetime.now().strftime("%m%y"),
            datetime.now().strftime("%d%m%y")
        ]
        for word, date, sep in itertools.product(base_words, date_formats, components['special_chars']):
            passwords.add(f"{word}{sep}{date}")  
            passwords.add(f"{date}{sep}{word}")  
    
    generate_core_patterns()
    
    # Add additional components
    passwords.update(components['keyboard_walks'])
    passwords.update(components['common_passwords'])
    
    # Length filtering
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
        print("Error: Company name cannot be empty!")
    else:
        try:
            passwords = generate_company_passwords(company)
            save_passwords(passwords)
        except Exception as e:
            print(f"Error generating passwords: {str(e)}")
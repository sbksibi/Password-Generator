# Company Password Generator 🔐

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive password generation tool for security professionals to test organizational password strength. Generates potential passwords based on company names, common patterns, and corporate terminology.

**Use Case**: Ethical penetration testing, security audits, and password policy validation.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Advanced Customization](#advanced-customization)
- [Output Format](#output-format)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Ethical Notice](#ethical-notice)

## Features 🚀
- **Smart Pattern Generation**:
  - Company name variations (camelCase, UPPERCASE, lowercase)
  - Leet speak transformations (e.g., `TechCorp` → `T3chC0rp`)
  - Corporate suffixes (Inc, LLC) and departments (HR, IT)
- **Temporal Patterns**:
  - Current year/next year combinations
  - Seasonal passwords (Winter2024, Spring2025)
  - Month-based patterns (January2024, Feb@2025)
- **Security Awareness**:
  - Common weak passwords (`qwerty`, `password1`)
  - Keyboard walk patterns (`1qaz2wsx`, `!QAZ@WSX`)
- **Customization**:
  - Minimum password length filtering
  - Configurable special characters and prefixes

## Installation 💻

### Prerequisites
- Python 3.7 or later
- Git (optional)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/company-password-generator.git
   cd company-password-generator
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Run the script:
   ```bash
   python password_generator.py
   ```

## Usage 🛠️

### Basic Usage
```bash
$ python password_generator.py
Enter company name: CyberShield

Generated 2487 passwords. Saved to passwords.txt
```

### Advanced Customization
Modify these variables in the code for different results:
```python
# In generate_company_passwords() function:
min_length = 10  # Change minimum password length

# Add/remove special characters:
special_chars = ["!", "@", "#", "$", "%", "&", "*", "?"]

# Extend corporate terms:
department_names = ["HR", "IT", "Security", "DevOps"]
```

## Output Format 📄
Example output for `company_name = "CyberShield"`:
```
CyberShield2024!
Cyb3rSh13ld#123
Admin@CyberShield
Winter2024
HR%CyberShield
1qaz2wsx
...
```

File structure in `passwords.txt`:
```
[Company Name Variations][Special Character][Year/Sequence]
[Common Prefixes][Department][Seasonal Patterns]
[Keyboard Walks][Leet Speak][Weak Passwords]
```

## How It Works ⚙️

### Input Processing:
- Splits company names using regex (e.g., "CyberShield LLC" → `["CyberShield", "LLC"]`)
- Generates case variations and abbreviations

### Pattern Generation:
- Combines base words with:
  - Temporal patterns (years/months)
  - Corporate terminology
  - Special character separators

### Security Patterns:
- Leet speak transformations
- Common weak password list
- Keyboard adjacency patterns

### Filtering:
- Removes duplicates with `set()`
- Sorts alphabetically
- Applies minimum length filter

## Contributing 🤝
1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-patterns
   ```
3. Add your improvements:
   - New password patterns
   - Enhanced company name parsing
   - Additional test cases
4. Submit a pull request with a description

## License 📜
MIT License - See [LICENSE](LICENSE) for details.

## Ethical Notice ⚠️
### Legal Compliance:
❗ Use only on systems you own or have explicit written permission to test.
❗ Comply with local laws (Computer Fraud and Abuse Act, GDPR, etc.).

### Responsible Disclosure:
If you find vulnerabilities in third-party systems:
- Notify the organization privately
- Allow reasonable time for remediation
- Never expose sensitive data publicly

**Disclaimer**: This tool is for educational and authorized security testing only. Developers assume no liability for misuse.

## Repository Structure 🌳
```
company-password-generator/
├── password_generator.py   # Main generator script
├── passwords.txt           # Generated password list
├── README.md               # This documentation
├── LICENSE                 # MIT License text
└── .gitignore              # Standard Python gitignore
```

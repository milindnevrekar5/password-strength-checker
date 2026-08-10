# Google-Guidelines Password Strength Tester

A Python-based cybersecurity tool that evaluates password strength based on Google's official account security guidelines. Instead of a generic point system, this script analyzes passwords for length, uniqueness, character complexity, and predictability to categorize them as Weak, Medium, or Strong.

## 🚀 Features

* **Strict Guideline Adherence:** Evaluates passwords based on real-world security standards (e.g., requiring 12+ characters for a "Strong" rating).
* **Vulnerability Scanning:** Actively detects highly predictable sequential keyboard patterns (like `qwerty` or `1234`) and basic dictionary words.
* **Regex Character Analysis:** Utilizes Python's Regular Expressions (`re`) to verify the presence of uppercase letters, lowercase letters, numbers, and special symbols.
* **Shoulder-Surfing Protection:** Uses Python's built-in `getpass` module to securely hide user input in the terminal, ensuring the password is not displayed on the screen as it is typed.
* **Zero Dependencies:** Built entirely using Python's standard library. No external installations required.

## 📋 Prerequisites

* Python 3.6 or higher installed on your system.

## 🛠️ Installation

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/milindnevrekar5/google-password-tester.git](https://github.com/milindnevrekar5/google-password-tester.git)
Navigate to the project directory:
cd google-password-tester
💻 Usage
Run the script directly from your terminal. When prompted, type the password you want to test and press Enter. Note: Your keystrokes will not be visible on the screen for security reasons.
python google_password_tester.py
📊 Example Output
Example 1: A Strong Password
Google-Guidelines Password Evaluator
------------------------------------
Enter a password to test (input will be hidden): 

----------------------------------------
Password Strength Results
----------------------------------------
Strength: 🟢 STRONG
Analysis: Excellent work! This password effectively blocks both human guessing and automated cyberattacks.
Reason: It is at least 12 characters long and uses a complex combination of uppercase, lowercase, numbers, and symbols.
Tip: Creating long passphrases made from quotes or lyrics is a great way to keep this memorable!
Example 2: A Weak Password
Google-Guidelines Password Evaluator
------------------------------------
Enter a password to test (input will be hidden): 

----------------------------------------
Password Strength Results
----------------------------------------
Strength: 🔴 WEAK
Analysis: Your password is highly vulnerable to hacking.
Reason: It relies on basic dictionary words, sequential keyboard patterns (like 'qwerty' or '1234'), or is under 8 characters.
Tip: Avoid easily guessable personal information such as birthdates or nicknames.
⚠️ Disclaimer
Educational Purposes Only. This tool is designed to teach fundamental cybersecurity concepts, input validation, and password hygiene. Do not enter your actual, sensitive passwords (like your banking or primary email passwords) into third-party scripts.

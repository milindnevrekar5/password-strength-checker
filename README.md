Password Strength Checker

A beginner-friendly Python command-line project that provides a basic estimate of password strength using length and character-pattern checks.

«This is an educational heuristic, not Google's official password checker or a security audit. Never enter a real or reused password into this demonstration.»

Features

- Checks password length.
- Detects a small set of common weak patterns.
- Checks uppercase, lowercase, numbers, and symbols.
- Hides terminal input using Python's "getpass".
- Uses Python's standard library.

Requirements

- Python 3.6 or newer.

Installation

git clone https://github.com/milindnevrekar5/google-password-tester.git
cd google-password-tester
python google_password_tester.py

Use a made-up sample password for demonstrations.

How It Works

The "evaluate_password()" function checks basic password characteristics and prints a Weak, Medium, or Strong label. These labels are only a learning aid.

Limitations

- The common-pattern list is limited.
- Character variety alone cannot reliably measure password strength.
- It does not check breached-password databases.
- It does not guarantee protection against attacks.

Learning Outcomes

Python functions, regular expressions, conditional logic, and secure terminal input.

Disclaimer

Educational use only. Never submit real passwords or sensitive credentials to this program.
import re
import getpass

def evaluate_password(password: str):
    """Evaluates password strength based on Google's security guidelines."""
    
    # 1. Define known weak patterns (dictionary words, sequential keyboard patterns)
    weak_patterns = ["password", "qwerty", "1234", "asdf", "1111"]
    
    # Check if any weak pattern is inside the password (case-insensitive)
    has_weak_pattern = any(pattern in password.lower() for pattern in weak_patterns)
    
    # 2. Analyze the character types used in the password
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))
    
    length = len(password)
    
    print("\n" + "-" * 40)
    print("Password Strength Results")
    print("-" * 40)
    
    # CATEGORY: WEAK
    # Highly vulnerable because it relies on basic dictionary words, sequential patterns, or is too short.
    if length < 8 or has_weak_pattern:
        print("Strength: 🔴 WEAK")
        print("Analysis: Your password is highly vulnerable to hacking.")
        print("Reason: It relies on basic dictionary words, sequential keyboard patterns (like 'qwerty' or '1234'), or is under 8 characters.")
        print("Tip: Avoid easily guessable personal information such as birthdates or nicknames.")
        
    # CATEGORY: STRONG
    # At least 12 characters long, complex combination of upper, lower, numbers, and symbols.
    elif length >= 12 and has_uppercase and has_lowercase and has_number and has_symbol:
        print("Strength: 🟢 STRONG")
        print("Analysis: Excellent work! This password effectively blocks both human guessing and automated cyberattacks.")
        print("Reason: It is at least 12 characters long and uses a complex combination of uppercase, lowercase, numbers, and symbols.")
        print("Tip: Creating long passphrases made from quotes or lyrics is a great way to keep this memorable!")
        
    # CATEGORY: MEDIUM
    # Meets the bare minimum (8+ characters, basic mix of letters and numbers) but lacks full complexity or length.
    else:
        print("Strength: 🟡 MEDIUM")
        print("Analysis: This password meets the bare minimum technical requirements, but could be better.")
        print("Reason: It is at least 8 characters long with a basic mix of characters, but it remains susceptible to advanced cracking tools.")
        print("Fix: Upgrade to a strong password by making it at least 12 characters long and ensuring it includes symbols.")

def main():
    print("Google-Guidelines Password Evaluator")
    print("------------------------------------")
    # getpass securely hides the password input in the terminal
    user_password = getpass.getpass("Enter a password to test (input will be hidden): ")
    
    evaluate_password(user_password)

if __name__ == "__main__":
    main()

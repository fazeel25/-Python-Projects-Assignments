from hashlib import sha256

def hash_password(password):
    """Returns the SHA-256 hash of the given password."""
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, check_password):
    """Verifies if the email and password combination is correct."""
    if email not in stored_logins:
        print(f"❌ Login failed: Email '{email}' not found.")
        return False

    hashed_input = hash_password(check_password)
    if stored_logins[email] == hashed_input:
        print(f"✅ Login successful for '{email}'!")
        return True
    else:
        print(f"❌ Login failed: Incorrect password for '{email}'.")
        return False

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }

    print("\n🔒 Testing login attempts:\n")

    login("example@gmail.com", stored_logins, "word")
    login("example@gmail.com", stored_logins, "password")
    login("code_in_placer@cip.org", stored_logins, "Karel")
    login("code_in_placer@cip.org", stored_logins, "karel")
    login("student@stanford.edu", stored_logins, "password")
    login("student@stanford.edu", stored_logins, "123!456?789")
    login("wrong_user@example.com", stored_logins, "anything")  # Example to show email not found

if __name__ == "__main__":
    main()

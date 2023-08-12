def calculate_key_value(key):
    key_value = sum(ord(char) for char in key)
    return key_value

def encrypt(text, key):
    key_value = calculate_key_value(key)
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key_value) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    key_value = calculate_key_value(key)
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - shift - key_value) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    key = input("Enter the key: ")
    choice = input("Encrypt or Decrypt? (E/D): ")

    if choice.upper() == 'E':
        text = input("Enter the text to encrypt: ")
        encrypted_text = encrypt(text, key)
        print("Encrypted text:", encrypted_text)
    elif choice.upper() == 'D':
        encrypted_text = input("Enter the text to decrypt: ")
        decrypted_text = decrypt(encrypted_text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

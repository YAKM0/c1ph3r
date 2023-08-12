# Simple Caesar Cipher Encryption and Decryption

This is a Python script that implements a simple Caesar cipher for encrypting and decrypting text. The Caesar cipher is a basic form of substitution cipher where each letter in the plaintext is shifted a fixed number of positions down or up the alphabet.

## Usage

1. Run the script using a Python interpreter.
2. The script will display a banner at the beginning.
3. You will be prompted to enter a key. The key is used for shifting the characters during encryption and decryption.
4. Choose whether to encrypt or decrypt the text by typing 'E' for encryption or 'D' for decryption.
5. Enter the text to encrypt or decrypt as prompted.
6. The script will output the encrypted or decrypted text.

## Functions

### `calculate_key_value(key)`

Calculates the sum of ASCII values of characters in the provided key.

### `encrypt(text, key)`

Encrypts the provided text using the Caesar cipher with the given key.

### `decrypt(encrypted_text, key)`

Decrypts the encrypted text using the Caesar cipher with the given key.

### `main()`

Handles user input and interaction:
- Prompts for the key.
- Prompts for encryption or decryption choice.
- Accepts input text.
- Displays the result.

## Note

This script is meant for educational purposes and to demonstrate a basic concept of encryption and decryption. The Caesar cipher is not secure for real-world encryption needs. Use it responsibly and do not rely on it for sensitive information.

## License

This project is licensed under the [MIT License](LICENSE).

# Secret Language in Python

This Python script allows two people to communicate using a unique secret language. It encrypts messages using a custom-generated cipher and decrypts them back to readable text.

## Features
- Generates a unique cipher every time the script runs.
- Encrypts and decrypts messages.
- Simple text-based user interaction.

## How It Works
1. The script creates a randomized letter substitution cipher.
2. Users can choose to encrypt or decrypt messages.
3. Encrypted messages can only be understood by the person with the same cipher.

## Usage
1. Run the script:

2. Choose an option:
   - `e` to encrypt a message.
   - `d` to decrypt a message.
   - `q` to quit.
3. Enter the message and receive the transformed text.

## Example
```
Do you want to encrypt or decrypt? (e/d/q to quit): e
Enter message to encrypt: Hello World
Encrypted message: Xyzzy Abcde

Do you want to encrypt or decrypt? (e/d/q to quit): d
Enter message to decrypt: Xyzzy Abcde
Decrypted message: Hello World
```

## Notes
- Each run generates a new cipher, so encrypted messages must be decrypted using the same instance.
- Modify the script to store and reuse the cipher for long-term communication.


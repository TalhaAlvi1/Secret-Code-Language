import random

def generate_cipher():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled = list(letters)
    random.shuffle(shuffled)
    cipher_dict = {letters[i]: shuffled[i] for i in range(len(letters))}
    reverse_cipher = {v: k for k, v in cipher_dict.items()}
    return cipher_dict, reverse_cipher

def encrypt_message(message, cipher_dict):
    return "".join(cipher_dict.get(char, char) for char in message)

def decrypt_message(message, reverse_cipher):
    return "".join(reverse_cipher.get(char, char) for char in message)

if __name__ == "__main__":
    cipher_dict, reverse_cipher = generate_cipher()
    
    print("Welcome to the secret language!")
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d/q to quit): ")
        if choice == 'q':
            break
        elif choice == 'e':
            msg = input("Enter message to encrypt: ")
            encrypted = encrypt_message(msg, cipher_dict)
            print(f"Encrypted message: {encrypted}")
        elif choice == 'd':
            msg = input("Enter message to decrypt: ")
            decrypted = decrypt_message(msg, reverse_cipher)
            print(f"Decrypted message: {decrypted}")
        else:
            print("Invalid option. Please choose again.")

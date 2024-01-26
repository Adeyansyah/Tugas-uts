def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            elif char.isupper():
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

# Contoh penggunaan
ciphertext = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
shift_value = 13  # Nilai pergeseran (bisa diubah sesuai kebutuhan)
decrypted_message = caesar_decrypt(ciphertext, shift_value)

print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)

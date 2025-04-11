class VigenereCipher:
    def __init__(self, key: str):
        self.key = self.format_key(key)

    def format_key(self, key: str):
        return ''.join(filter(str.isalpha, key.upper()))

    def repeat_key(self, text: str):
        return (self.key * (len(text) // len(self.key) + 1))[:len(text)]

    def encrypt(self, plaintext: str) -> str:
        plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
        key = self.repeat_key(plaintext)
        ciphertext = []

        for p, k in zip(plaintext, key):
            shift = (ord(p) + ord(k) - 2 * ord('A')) % 26
            ciphertext.append(chr(shift + ord('A')))

        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
        key = self.repeat_key(ciphertext)
        plaintext = []

        for c, k in zip(ciphertext, key):
            shift = (ord(c) - ord(k) + 26) % 26
            plaintext.append(chr(shift + ord('A')))

        return ''.join(plaintext)

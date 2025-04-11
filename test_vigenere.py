import unittest
from vigenere import VigenereCipher

class TestVigenereCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = VigenereCipher("LEMON")

    def test_encrypt(self):
        encrypted = self.cipher.encrypt("ATTACKATDAWN")
        self.assertEqual(encrypted, "LXFOPVEFRNHR")

    def test_decrypt(self):
        decrypted = self.cipher.decrypt("LXFOPVEFRNHR")
        self.assertEqual(decrypted, "ATTACKATDAWN")

    def test_non_alpha_input(self):
        encrypted = self.cipher.encrypt("Attack at dawn!")
        self.assertEqual(encrypted, "LXFOPVEFRNHR")

    def test_decrypt_non_alpha(self):
        decrypted = self.cipher.decrypt("LXFOPVEFRNHR")
        self.assertEqual(decrypted, "ATTACKATDAWN")

if __name__ == "__main__":
    unittest.main()

# Шифр Виженера 

## Установка
- Клонировать репозиторий
```bash
git clone https://github.com/dariavolnova/vigenere_cipher
cd vigenere_cipher
```
- Использование программы
``` python
from vigenere import VigenereCipher

cipher = VigenereCipher("LEMON")
cipher.encrypt("ATTACKATDAWN") 
cipher.decrypt("LXFOPVEFRNHR")  
```
- Запустить тесты
``` python
python -m unittest test_vigenere.py
```


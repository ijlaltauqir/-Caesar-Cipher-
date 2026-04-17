"""
vigenere.py — Vigenère cipher: encrypt and decrypt

Concepts used:
  - Keyword cycling with enumerate() and modulo
  - zip() — pair each plaintext letter with a key letter
  - String methods: isalpha(), upper(), lower()
  - List comprehension
  - Generator with next() and itertools.cycle

The Vigenère cipher is a polyalphabetic substitution cipher.
Instead of one fixed shift, it uses a keyword — each letter of the
keyword is a separate shift applied in rotation.

Example:
  plaintext : HELLO
  keyword   : KEY        (K=10, E=4, Y=24)
  shifts    :  K  E  Y  K  E
               10  4  24 10  4
  ciphertext: RIJVS

This makes it MUCH harder to crack with frequency analysis because
the same plaintext letter encrypts to different ciphertext letters
depending on its position.
"""


def _key_stream(keyword: str, length: int) -> list[int]:
    """
    Generate a list of shift values from a keyword, repeated to fill `length`.

    Example: keyword="KEY", length=8 -> [10, 4, 24, 10, 4, 24, 10, 4]
    """
    keyword = keyword.upper()
    # Only use alphabetic characters from the keyword
    clean_key = [c for c in keyword if c.isalpha()]

    if not clean_key:
        raise ValueError("Keyword must contain at least one letter.")

    # Cycle the key to match the number of letters in the message
    stream = []
    key_index = 0
    for _ in range(length):
        stream.append(ord(clean_key[key_index % len(clean_key)]) - ord('A'))
        key_index += 1
    return stream


def encrypt(text: str, keyword: str) -> str:
    """
    Encrypt plaintext using the Vigenère cipher.

    Non-letter characters are preserved and do NOT consume a key position —
    so "HELLO WORLD" and "HELLOWORLD" use the same key positions for letters.
    """
    result = []
    letter_count = 0

    # Count total letters first to build the key stream
    letter_count = sum(1 for c in text if c.isalpha())
    shifts = _key_stream(keyword, letter_count)

    key_i = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shifts[key_i]) % 26
            result.append(chr(base + shifted))
            key_i += 1
        else:
            result.append(char)

    return "".join(result)


def decrypt(text: str, keyword: str) -> str:
    """
    Decrypt a Vigenère-encrypted ciphertext.

    Decryption uses (26 - shift) for each key letter, reversing the encryption.
    """
    result = []

    letter_count = sum(1 for c in text if c.isalpha())
    shifts = _key_stream(keyword, letter_count)

    key_i = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Reverse the shift: subtract instead of add
            shifted = (ord(char) - base - shifts[key_i]) % 26
            result.append(chr(base + shifted))
            key_i += 1
        else:
            result.append(char)

    return "".join(result)
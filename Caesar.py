"""
caesar.py — Caesar cipher: encrypt, decrypt, and brute-force cracker

Concepts used:
  - ord() / chr()        : convert characters <-> ASCII numbers
  - Modular arithmetic   : % operator wraps Z back to A
  - String methods       : isalpha(), isupper(), upper()
  - List comprehension   : build result character by character
  - Dictionary           : store letter frequency counts
  - sorted()             : rank frequencies for cracking
"""

# English letter frequencies (most common first) — used by the cracker
ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def encrypt(text: str, shift: int) -> str:
    """
    Encrypt plaintext using Caesar cipher.

    Each letter is shifted forward by `shift` positions in the alphabet.
    Non-letter characters (spaces, punctuation, numbers) are left unchanged.

    How it works:
      - ord('A') = 65, ord('Z') = 90
      - Subtract 65 to get position 0-25
      - Add shift, wrap with % 26
      - Add 65 back to get ASCII

    Example:
      encrypt("HELLO", 3) -> "KHOOR"
      H(7) + 3 = K(10), E(4) + 3 = H(7), etc.
    """
    shift = shift % 26  # normalise — shift of 27 is same as shift of 1
    result = []

    for char in text:
        if char.isalpha():
            # Preserve original case (upper or lower)
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)  # keep spaces, punctuation as-is

    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """
    Decrypt a Caesar-encrypted ciphertext.

    Decryption is just encryption with a negative shift.
    encrypt("KHOOR", 3) -> "HELLO"  (shift forward 3)
    decrypt("KHOOR", 3) -> "HELLO"  (shift backward 3, same as forward 23)

    We reuse encrypt() by passing (26 - shift) which reverses the shift.
    """
    return encrypt(text, 26 - (shift % 26))


def crack(ciphertext: str) -> tuple[str, int]:
    """
    Break a Caesar cipher using frequency analysis.

    How frequency analysis works:
      - In English, 'E' is the most common letter (~12.7%)
      - In a Caesar ciphertext, the most frequent letter is likely 'E' shifted
      - We count letter frequencies in the ciphertext
      - The most frequent ciphertext letter probably maps to 'E'
      - key = (position_of_most_frequent - position_of_E) % 26

    This is a statistical attack — it works best on longer texts.
    Returns: (decrypted_text, discovered_key)
    """
    # Count how often each letter appears in the ciphertext
    freq = {}
    for char in ciphertext.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    if not freq:
        return ciphertext, 0

    # Find the most frequent letter in the ciphertext
    most_common = max(freq, key=freq.get)

    # Assume most_common maps to 'E' (most frequent in English)
    # key = (cipher_letter_pos - plain_letter_pos) % 26
    guessed_key = (ord(most_common) - ord('E')) % 26

    return decrypt(ciphertext, guessed_key), guessed_key


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    """
    Try all 25 possible Caesar shifts and return all results.

    Useful when the ciphertext is too short for frequency analysis.
    Returns a list of (shift, decrypted_text) tuples for all 25 shifts.
    """
    results = []
    for shift in range(1, 26):
        results.append((shift, decrypt(ciphertext, shift)))
    return results
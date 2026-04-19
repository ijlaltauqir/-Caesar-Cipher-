"""
cipher.py — Main CLI entry point for the Caesar/Vigenère cipher tool

Concepts used:
  - argparse    : build professional command-line interfaces
  - sys.exit()  : exit with error codes (0 = success, 1 = error)
  - File I/O    : open(), read(), write(), the 'with' statement
  - Imports     : importing from your own modules (caesar.py, vigenere.py)
  - __name__ == '__main__' : only run CLI code when script is executed directly

Usage examples:
  python cipher.py -e "Hello World" -k 3
  python cipher.py -d "Khoor Zruog" -k 3
  python cipher.py --crack "Khoor Zruog"
  python cipher.py --brute "Khoor Zruog"
  python cipher.py -e "Hello" --vigenere --keyword SECRET
  python cipher.py -e "Hello" -k 3 --file input.txt --output encrypted.txt
"""

import argparse
import sys
import os

import Caesar
import Vigenere


# ─────────────────────────────────────────────
# File helpers
# ─────────────────────────────────────────────

def read_file(path: str) -> str:
    """Read a text file and return its contents as a string."""
    if not os.path.exists(path):
        print(f"[ERROR] File not found: {path}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    """Write a string to a text file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Output saved to: {path}")


# ─────────────────────────────────────────────
# CLI setup with argparse
# ─────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    """
    Build and return the argument parser.

    argparse concepts:
      - add_argument()          : define a CLI flag
      - type=int                : auto-convert string input to integer
      - required=False          : optional arguments
      - mutually_exclusive_group: only one of -e / -d / --crack can be used
      - help=""                 : shown when user runs `python cipher.py -h`
    """
    parser = argparse.ArgumentParser(
        prog="cipher",
        description="Caesar & Vigenère cipher tool with frequency analysis cracker",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
examples:
  python cipher.py -e "Attack at dawn" -k 13
  python cipher.py -d "Nggnpx ng qnja" -k 13
  python cipher.py --crack "Nggnpx ng qnja"
  python cipher.py --brute "KHOOR"
  python cipher.py -e "Secret" --vigenere --keyword LEMON
  python cipher.py -e "" -k 3 --file message.txt --output out.txt
        """
    )

    # ── Mode: encrypt / decrypt / crack / brute (pick one) ──
    mode_group = parser.add_mutually_exclusive_group(required=True)

    mode_group.add_argument(
        "-e", "--encrypt",
        metavar="TEXT",
        help="Encrypt the given text"
    )
    mode_group.add_argument(
        "-d", "--decrypt",
        metavar="TEXT",
        help="Decrypt the given text"
    )
    mode_group.add_argument(
        "--crack",
        metavar="TEXT",
        help="Auto-crack Caesar cipher using frequency analysis"
    )
    mode_group.add_argument(
        "--brute",
        metavar="TEXT",
        help="Brute-force all 25 Caesar shifts and print all results"
    )

    # ── Cipher options ──
    parser.add_argument(
        "-k", "--key",
        type=int,
        default=3,
        help="Caesar shift key (integer, default: 3)"
    )
    parser.add_argument(
        "--vigenere",
        action="store_true",
        help="Use Vigenère cipher instead of Caesar"
    )
    parser.add_argument(
        "--keyword",
        metavar="WORD",
        default="KEY",
        help="Keyword for Vigenère cipher (default: KEY)"
    )

    # ── File I/O ──
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Read input text from a file instead of command line"
    )
    parser.add_argument(
        "--output",
        metavar="PATH",
        help="Save output to a file"
    )

    return parser


# ─────────────────────────────────────────────
# Main logic
# ─────────────────────────────────────────────

def run(args) -> None:
    """Execute the selected cipher operation based on parsed arguments."""

    # ── Determine input text ──
    # If --file is given, read from file. Otherwise use the inline text.
    if args.file:
        # Get the text from whatever mode flag has the filename placeholder
        input_text = read_file(args.file)
        print(f"[+] Read {len(input_text)} characters from {args.file}")
    else:
        # Pull from whichever mode was selected
        input_text = args.encrypt or args.decrypt or args.crack or args.brute

    # ── Execute selected mode ──

    if args.encrypt is not None or (args.file and args.encrypt is not None):
        # ENCRYPT
        if args.Vigenere:
            result = Vigenere.encrypt(input_text, args.keyword)
            print(f"\n[Vigenère ENCRYPT] keyword={args.keyword}")
        else:
            result = Caesar.encrypt(input_text, args.key)
            print(f"\n[Caesar ENCRYPT] shift={args.key}")

        print(f"  Plaintext : {input_text}")
        print(f"  Ciphertext: {result}\n")

    elif args.decrypt is not None or (args.file and args.decrypt is not None):
        # DECRYPT
        if args.Vigenere:
            result = Vigenere.decrypt(input_text, args.keyword)
            print(f"\n[Vigenère DECRYPT] keyword={args.keyword}")
        else:
            result = Caesar.decrypt(input_text, args.key)
            print(f"\n[Caesar DECRYPT] shift={args.key}")

        print(f"  Ciphertext: {input_text}")
        print(f"  Plaintext : {result}\n")

    elif args.crack:
        # CRACK with frequency analysis
        result, found_key = Caesar.crack(input_text)
        print(f"\n[CRACK] Frequency analysis result:")
        print(f"  Ciphertext    : {input_text}")
        print(f"  Discovered key: {found_key}")
        print(f"  Plaintext     : {result}\n")

    elif args.brute:
        # BRUTE FORCE all shifts
        results = Caesar.brute_force(input_text)
        print(f"\n[BRUTE FORCE] All 25 shifts for: {input_text}")
        print(f"  {'Shift':<8} {'Decrypted'}")
        print(f"  {'─'*6}   {'─'*40}")
        for shift, text in results:
            print(f"  {shift:<8} {text}")
        print()
        result = results[0][1]  # use shift=1 as file output fallback

    # ── Save to file if requested ──
    if args.output and 'result' in locals():
        write_file(args.output, result)


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

def main():
    """
    __name__ == '__main__' check:
    This block only runs when you execute the script directly:
        python cipher.py ...
    It does NOT run when another script imports this file.
    This is a Python best practice for all CLI scripts.
    """
    parser = build_parser()

    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
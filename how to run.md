================================================================
  HOW TO RUN THE CAESAR & VIGENÈRE CIPHER PROJECT
  Complete step-by-step guide for beginners
================================================================


----------------------------------------------------------------
STEP 1 — MAKE SURE PYTHON IS INSTALLED
----------------------------------------------------------------

1. Open your terminal (or Command Prompt on Windows)
2. Type this and press Enter:

     python --version

   You should see something like: Python 3.11.0
   If you get an error, download Python from: https://www.python.org/downloads/
   During installation on Windows — CHECK the box that says "Add Python to PATH"


----------------------------------------------------------------
STEP 2 — SET UP YOUR PROJECT FOLDER
----------------------------------------------------------------

Create ONE folder on your computer called:
  caesar-vigenere-cipher

Put ALL of these files inside that folder:
  - cipher.py
  - caesar.py
  - vigenere.py
  - plaintext.txt     (rename your sample file to this, no subfolder)

Your folder should look exactly like this:

  caesar-vigenere-cipher/
  ├── cipher.py
  ├── caesar.py
  ├── vigenere.py
  └── plaintext.txt

IMPORTANT: All .py files must be in the SAME folder.
           cipher.py imports caesar.py and vigenere.py —
           they must be next to each other or it will crash.


----------------------------------------------------------------
STEP 3 — OPEN THE FOLDER IN YOUR TERMINAL
----------------------------------------------------------------

  ON WINDOWS:
  1. Open the folder in File Explorer
  2. Click the address bar at the top (where the path is shown)
  3. Type:  cmd
  4. Press Enter — a black Command Prompt window opens
     already inside your folder

  ON MAC:
  1. Open Terminal (search for it in Spotlight)
  2. Type:  cd  (with a space after it, do NOT press Enter yet)
  3. Drag your project folder into the Terminal window
  4. Now press Enter

  ON LINUX:
  1. Open Terminal
  2. Type: cd /path/to/caesar-vigenere-cipher
  3. Press Enter

  To confirm you are in the right folder, type:
     dir        (Windows)
     ls         (Mac / Linux)

  You should see cipher.py, caesar.py, vigenere.py listed.


----------------------------------------------------------------
STEP 4 — RUN YOUR FIRST COMMAND (TEST IT WORKS)
----------------------------------------------------------------

Type this exactly and press Enter:

  python cipher.py -e "Hello World" -k 3

You should see:

  [Caesar ENCRYPT] shift=3
    Plaintext : Hello World
    Ciphertext: Khoor Zruog

If you see this — everything is working perfectly!


----------------------------------------------------------------
STEP 5 — ALL AVAILABLE COMMANDS (copy and paste these)
----------------------------------------------------------------

--- ENCRYPT text ---
python cipher.py -e "Hello World" -k 3
python cipher.py -e "Attack at dawn" -k 13
python cipher.py -e "Your secret message here" -k 7

--- DECRYPT text (use the SAME key you used to encrypt) ---
python cipher.py -d "Khoor Zruog" -k 3
python cipher.py -d "Nggnpx ng qnja" -k 13

--- AUTO-CRACK (no key needed — tool figures it out) ---
python cipher.py --crack "Khoor Zruog"
python cipher.py --crack "Nggnpx ng qnja"

--- BRUTE FORCE (shows all 25 possible decryptions) ---
python cipher.py --brute "KHOOR"

--- VIGENERE CIPHER (uses a keyword instead of a number) ---
python cipher.py -e "Hello World" --vigenere --keyword SECRET
python cipher.py -d "Zincs Pgvnu" --vigenere --keyword SECRET

--- ENCRYPT AN ENTIRE FILE ---
python cipher.py -e "" -k 7 --file plaintext.txt --output encrypted.txt

  This reads plaintext.txt, encrypts it with shift 7,
  and saves the result to a new file called encrypted.txt
  in the same folder.

--- DECRYPT A FILE ---
python cipher.py -d "" -k 7 --file encrypted.txt --output decrypted.txt

--- SEE THE HELP MENU ---
python cipher.py -h


----------------------------------------------------------------
STEP 6 — RUNNING IN VISUAL STUDIO CODE (VS CODE)
----------------------------------------------------------------

VS Code is a free code editor. Download from: https://code.visualstudio.com

  HOW TO OPEN YOUR PROJECT IN VS CODE:
  1. Open VS Code
  2. Click: File > Open Folder
  3. Select your caesar-vigenere-cipher folder
  4. Click "Select Folder" (Windows) or "Open" (Mac)

  You will see all your files listed on the left side panel.

  HOW TO RUN COMMANDS IN VS CODE:
  1. Open the built-in terminal:
       Menu bar > Terminal > New Terminal
       OR press:  Ctrl + ` (backtick key, top-left of keyboard)
  2. A terminal panel opens at the BOTTOM of VS Code
  3. It is already inside your project folder automatically
  4. Type your commands here exactly as shown in Step 5

  HOW TO READ/EDIT THE CODE IN VS CODE:
  1. Click any .py file in the left panel to open it
  2. You can read, edit, and save the code
  3. After saving, run your command again in the terminal

  OPTIONAL — INSTALL THE PYTHON EXTENSION IN VS CODE:
  1. Click the Extensions icon on the left sidebar (looks like 4 squares)
  2. Search for: Python
  3. Install the one by Microsoft
  4. This gives you syntax highlighting and error underlines


----------------------------------------------------------------
STEP 7 — COMMON ERRORS AND HOW TO FIX THEM
----------------------------------------------------------------

ERROR: "python is not recognized as a command"
FIX:   Python is not installed or not added to PATH.
       Reinstall Python from python.org and check "Add to PATH"

ERROR: "ModuleNotFoundError: No module named 'caesar'"
FIX:   You are running cipher.py from the wrong folder.
       Make sure caesar.py is in the SAME folder as cipher.py.
       Use cd to navigate to the correct folder first.

ERROR: "No such file or directory: plaintext.txt"
FIX:   The file plaintext.txt must be in the SAME folder
       as cipher.py. Do not put it in a subfolder.

ERROR: "SyntaxError" or strange output
FIX:   Make sure you copied the full .py files without
       any missing characters. Re-download and try again.

ERROR: Nothing happens / blank output
FIX:   Run: python cipher.py -h
       If the help menu shows, the tool is working.
       Check your command for typos.


----------------------------------------------------------------
QUICK REFERENCE — ALL FLAGS EXPLAINED
----------------------------------------------------------------

  -e "text"          Encrypt the text in quotes
  -d "text"          Decrypt the text in quotes
  --crack "text"     Auto-find the key and decrypt
  --brute "text"     Try all 25 possible keys
  -k 3               The shift key (any number 1-25)
  --vigenere         Use Vigenere mode instead of Caesar
  --keyword WORD     The keyword for Vigenere mode
  --file name.txt    Read input from a file
  --output name.txt  Save output to a file
  -h                 Show help menu


================================================================
  You are ready. Good luck with your cybersecurity journey!
================================================================
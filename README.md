# CRYPTIX - Password Strength Analyzer & Wordlist Generator

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3-green)](https://flask.palletsprojects.com/)

**Author:** Priyanshi Sharma    

## Project Overview

CRYPTIX is a **Password Strength Analyzer and Custom Wordlist Generator**.  
It helps users evaluate the strength of passwords and create targeted wordlists for educational and security purposes.  
The project offers both a **GUI** (via Flask) and a **CLI interface**.

## Tools & Technologies Used
- **Python** – core programming language.
- **Flask** – for GUI/web interface.
- **HTML, CSS** – for interface design.
- **Regex (re)** – for password strength validation.
- **itertools & os** – for wordlist generation and file handling.

## Features

- **Password Strength Checker**
  - Evaluates password length, uppercase/lowercase, digits, and special characters.
  - Detects repeated characters.
  - Provides score out of 100 and strength label (WEAK, MEDIUM, STRONG).
  - Gives actionable suggestions for improvement.
  - Eye toggle in GUI to show/hide password input.

- **Custom Wordlist Generator**
  - Generate wordlists based on Name, Year, and optional extra keywords.
  - Includes leetspeak variations, common suffixes (123, 007, etc.), and year appending (2000–2025).
  - Preview first 20 lines in GUI, full wordlist saved in `reports/custom_wordlist.txt`.
  - You can also download the full wordlist using 'Download Wordlist' option.

- **Dual Interfaces**
  - GUI for web usage.
  - CLI for terminal-based usage.

## CLI Interface

- Run CLI:

python main.py


**Follow menu:**
1. Check password strength
2. Generate custom wordlist
3. Exit

**Example for Password Strength:**
Enter choice (1/2/3): 1
Enter password to analyze: s@@nv167_348

Score: 95/100
Strength Level: STRONG
Suggestions:
- Add more special characters

**Example for Wordlist Generation:**
Enter choice (1/2/3): 2
Enter name / keyword: Priyanshi
Enter year: 2006
Extra word (optional): Psharma

Wordlist saved at: reports/custom_wordlist.txt

**Exit CLI:**
Enter choice (1/2/3): 3
Exiting tool.

## Screenshots Attached
- CRYPTIX GUI Interface
- Wordlist Generator
- Password Strength Checker
- Exit
## Credits
- Developed by Priyanshi Sharma
- Educational project focused on password security awareness
- Wordlists generated for testing & learning purposes only
## Notes
- GUI preview displays first 20 lines only; full wordlist is saved in reports/custom_wordlist.txt.
- Always use strong passwords and handle wordlists responsibly.
- Both GUI and CLI provide user-friendly interfaces for flexible usage.

**Try it out, have fun, and keep your passwords strong with CRYPTIX!**

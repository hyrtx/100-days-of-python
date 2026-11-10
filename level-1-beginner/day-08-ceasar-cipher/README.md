# Day 08 Project: Ceasar Cipher

A command-line text encryption and decryption tool based on the ancient Caesar Cipher, featuring modular architecture, ASCII art integration, and input validation.

## Objective

Apply and expand core programming concepts from **Day 08** of the course, focusing on:
* **Functions with Inputs:** Understanding parameters and arguments.
* **Data Manipulation:** Indexing, modular arithmetic, and list operations.
* **Control Flow & Error Handling:** Managing continuous loops (`while`) and input validation (`try/except`).

## Program Rules & Logic Flow

1. **Mode Selection:** The user chooses whether to `encode` (encrypt) or `decode` (decrypt) a message.
2. **Message & Shift Input:** The user inputs the target text and an integer shift number (safely handled using modulo arithmetic to stay within the 26-letter alphabet range).
3. **Cipher Processing:** The program iterates through each character, shifting its position forward or backward in a duplicated alphabet list while preserving spaces and special characters.
4. **Continuation:** The user can choose to run the cipher again or terminate the program.

## How to Run the Code
```bash
python main.py
```
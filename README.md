# Comment Moderation Classifier

A simple Python program that checks a user comment and labels it as SAFE or OFFENSIVE. It also shows which words were flagged.

## Features
- Detects offensive words in English and Hinglish (Hindi written in Roman letters)
- Catches spelling tricks such as idi0t (numbers instead of letters) and idiiiot (repeated letters)
- Shows the exact flagged words for each comment
- Runs in the terminal, no extra libraries needed

## How it works
1. The comment is converted to lowercase.
2. Look-alike characters (0, 1, 3, 4, 5, @, $) are turned back into letters.
3. Repeated letters are removed.
4. The cleaned comment is matched against a list of offensive words.

## How to run
1. Install Python 3.
2. Download classifier.py.
3. Open a terminal in the same folder and run:

python classifier.py
4. Type a comment and press Enter. Type exit to stop.

## Example
Enter a comment: you are an idi0t
Result: OFFENSIVE
Flagged words: ['idiot']
## Limitations and future work
- It is rule-based, so it only catches words from its list.
- It does not understand context or sarcasm.
- Planned: Devanagari Hindi words, a test file to measure accuracy, and a machine learning version.

## Author
Anshul Trivedi

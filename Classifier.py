# Comment Moderation Classifier v3 (English + Hinglish words, spelling tricks)
# Author: Anshul Trivedi

# Step 1: English offensive words
english_words = ["idiot", "stupid", "hate", "scam", "fake", "loser"]

# Step 2 (new): common Hinglish words, written in English letters
hinglish_words = ["pagal", "bewakoof", "gadha", "nalayak", "chor", "dhokha", "bakwas", "ghatiya"]

bad_words = english_words + hinglish_words

# turn number/symbol tricks back into letters, "idi0t" -> "idiot"
look_alike = {"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "@": "a", "$": "s"}

def clean_text(comment):
    text = comment.lower()
    for fake_char, real_char in look_alike.items():
        text = text.replace(fake_char, real_char)
    return text

# remove repeated letters, "idiiiot" -> "idiot"
def remove_repeats(text):
    result = ""
    for ch in text:
        if len(result) < 1 or ch != result[-1]:
            result += ch
    return result

def classify_comment(comment):
    text = remove_repeats(clean_text(comment))
    found = []
    for word in bad_words:
        if remove_repeats(word) in text:
            found.append(word)
    if found:
        return "OFFENSIVE", found
    return "SAFE", []

print("Comment Moderation Classifier v3. Type 'exit' to stop.")
while True:
    user_comment = input("Enter a comment: ")
    if user_comment.lower() == "exit":
        break
    label, words = classify_comment(user_comment)
    print("Result:", label)
    if words:
        print("Flagged words:", words)
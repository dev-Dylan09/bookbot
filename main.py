from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    unique_char_count = count_unique_letter(text)
    print(text)
    print(f"\n{word_count} words found in the document")
    print(f"\nUnique letters:")
    for char, count in unique_char_count.items():
        print(f"{char}: {count}")
    print(generate_report(book_path, word_count, unique_char_count))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_unique_letter(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    return Counter(cleaned_text)

def generate_report(book_path, word_count, unique_char_count):
    report_lines = []
    report_lines.append(f"\nReport for '{book_path}':")
    report_lines.append(f"\nTotal word count: {word_count}")
    report_lines.append("\nCharacter Occurrences:")
    sorted_char = sorted(unique_char_count.items(), key=lambda x: (-x[1]))

    for char, count in sorted_char:
        report_lines.append(f"This letter {char} was found: {count} times")

    return "\n".join(report_lines)

main()
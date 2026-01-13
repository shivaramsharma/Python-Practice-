import string

def count_word_freq(filename):
    word_counts = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        text = text.lower()
        text = text.translate(str.maketrans('','',string.punctuation))
        words = text.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}
    return word_counts

if __name__ == "__main__":
    try:
        with open('sample.txt', 'w', encoding='utf-8') as f:
            f.write("This is a sample text file. "
                    "This file has sample text, and the text has words. "
                    "Words, words, words.")
        print("Created 'sample.txt' for testing.")
    except IOError as e:
        print(f"Could not create sample file: {e}")
        exit()
    file_to_process = 'sample.txt'
    counts = count_word_freq(file_to_process)

  
    if counts:
        print(f"\nWord frequencies in '{file_to_process}':")
        for word, count in sorted(counts.items()):
            print(f"'{word}': {count}")


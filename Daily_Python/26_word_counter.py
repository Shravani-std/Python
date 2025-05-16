def count_words(text):
    return len(text.split())

def count_characters(text,include_spaces):
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))


def count_sentence(text):

    sentence_ending = [".","?","!","and"]
    count = 0

    for char in text:
        if char in sentence_ending:
            count +=1
    if count == 0 and text.strip():
        count = 1

    return count

def analyze_text(text):
    word_count = count_words(text)
    char_count_with_spaces = count_characters(text,True)
    char_count_without_spaces = count_characters(text,False)
    sentence_count = count_sentence(text)

    if sentence_count > 0:
        words_per_sentence = word_count / sentence_count
    else:
        words_per_sentence = 0
    
    if word_count > 0:
        chars_per_word = char_count_with_spaces / word_count
    else:
        chars_per_word = 0
    
    print("\n===== 📊 Text Analysis Results 📊 =====")
    print(f"• 📝 Words: {word_count}")
    print(f"• 🔤 Characters (with spaces): {char_count_with_spaces}")
    print(f"• 🔡 Characters (without spaces): {char_count_without_spaces}")
    print(f"• 📃 Sentences: {sentence_count}")
    print(f"• 📏 Average words per sentence: {words_per_sentence:.1f}")
    print(f"• 📐 Average characters per word: {chars_per_word:.1f}")


def main():
    print("\n==== 📝 Word Counter 📝 ====")
    print("Count words, characters, and sentences in your text ✨")

    while True:
        print("\nChoose an option: ")
        print("1. 📄 Enter text to analyze")
        print("2. 🚪 Exit")

        choice = input("\nYour choice (1/2): ")

        if choice == "1":
            print("\n Enter or paste your text below (press Enter twice to finish): ")
            lines = []

            while True:
                line = input()
                if not line and not lines[-1]:
                    break

                lines.append(line)

            text = "\n".join(lines)

            if not text.strip():
                print(" No text provided. Please try again")
                continue

            analyze_text(text)

        elif choice == "2":
            print("Goodbye 👋")
            break
        else:
            print(" Invalid choice. Please enter 1 or 2.")

main()
input_text = input("enter your text:\n")

spilted_text = input_text.lower().split()

word_count = dict()
print(len(spilted_text))
i=0
for word in spilted_text:
    word_count[word] = word_count.get(word,0) +1

sorted_word_count = sorted(word_count.items() , key=lambda x: x[1], reverse=True)

print("Word frequencies (using dictionary):")
for word, count in sorted_word_count:
    print(f"'{word}': {count}")

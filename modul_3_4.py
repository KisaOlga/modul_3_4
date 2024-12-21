
def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)

    for i in range(len(words)):
        if root_word.lower() in words[i].lower() or words[i].lower() in root_word.lower():
            same_words.append(words[i])
        return (same_words)

result_1 = single_root_words('book', 'Bookshelf', 'bookstore', 'cheers', 'bookmark')
result_2 = single_root_words('glasses', 'Glass', 'apple', 'Disable', 'Bag')
print(result_1)
print(result_2)

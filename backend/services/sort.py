def sort(words, order):
    reverse = order == "desc"
    words.sort(reverse=reverse)
    return words

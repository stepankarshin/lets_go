def reverse_text(text):
    new_text[len(text)] = []
    for i in text:
        new_text[-i-1] = text[i]
    return new_text

def reverse_text(text):
    ---функция переворота текста---
    new_text[len(text)] = []
    for i in text:
        new_text[-i-1] = text[i]
    return new_text

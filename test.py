def capitalize_words(some_str):
    new_list = list(some_str.split())
    second_new_list = []
    for word in new_list:
        new_word = word[0].upper() + word[1:]
        second_new_list.append(new_word)
    return ' '.join(second_new_list)

result = capitalize_words("hello, world!")
print(result)




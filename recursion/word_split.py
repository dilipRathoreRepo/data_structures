
# word_split('themanran',['the','ran','man'])


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            word_split(phrase[len(word):], list_of_words, output)
    return output


phrase = 'themanran'
list_of_words = ['the', 'ran', 'man']

print(word_split(phrase, list_of_words))

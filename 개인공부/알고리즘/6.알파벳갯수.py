word = 'aaabbbalphabetpass'


def count_word(word):
    result = {}
    for i in word:
        result[i] = result.get(i, 0) + 1
    return result


print(count_word(word))

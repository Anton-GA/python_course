# Подсчет частоты входящих символов
def get_symbol_count_dict(word: str):
    result = {}
    for symbol in word:
        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1

    return result

# Подсчет всех слов в тексте
def count_word(text: str):
    return len(text.split(' '))

# Подсчет предложений в тексте
def count_sentences(sentences):
    return len(sentences.split('. '))

function = input("""
1: freq symb
2: number of words
3: number of sentences
""")

if function == '1':
    print(get_symbol_count_dict('Nice to meet you!'))

if function == '2':
    text = ('One. Two. Three. Four. Five')
    print(f'Number of words in text: {count_word(text)}')

if function == '3':
    sentences = ('Hello. The weather is fine today. Goodbye.')
    print(f'Number of sentences in text: {count_sentences(sentences)}')
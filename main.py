from pprint import pprint
from random import choice


def filter_exact_match(words: list, suggested_word: str, answer: str) -> list:
    for letter_index, status in enumerate(answer):
        if status != '2':
            continue

        filtered_words = []
        for word in words:
            if word[letter_index] == suggested_word[letter_index]:
                filtered_words.append(word)

        words = filtered_words.copy()
        filtered_words.clear()

    return words


def filter_mismatch(words: list, suggested_word: str, answer: str) -> list:
    the_right_words = [True] * len(words)
    for letter, status in zip(suggested_word, answer):
        if status != '0':
            continue

        letter_count = 0
        for letter_1, status_1 in zip(suggested_word, answer):
            if letter_1 == letter and status_1 != '0':
                letter_count += 1

        for word_index, word in enumerate(words):
            if letter_count < word.count(letter):
                the_right_words[word_index] = False

    filtered_words = []
    for status, word in zip(the_right_words, words):
        if status:
            filtered_words.append(word)

    return filtered_words.copy()


def filter_overlap(words: list, suggested_word: str, answer: str) -> list:
    for letter_index, status in enumerate(answer):
        if status != '1':
            continue

        filtered_words = []
        for word in words:
            if word[letter_index] != suggested_word[letter_index]:
                filtered_words.append(word)

        words = filtered_words.copy()
        filtered_words.clear()

    the_right_words = [True] * len(words)
    for letter, status in zip(suggested_word, answer):
        if status != '1':
            continue

        for word_index, word in enumerate(words):
            if letter not in word:
                the_right_words[word_index] = False

    filtered_words = []
    for status, word in zip(the_right_words, words):
        if status:
            filtered_words.append(word)

    return filtered_words.copy()


def filter_words(words: list, suggested_word: str, answer: str) -> list:
    words = filter_exact_match(words, suggested_word, answer)
    words = filter_mismatch(words, suggested_word, answer)
    words = filter_overlap(words, suggested_word, answer)
    return words


def main() -> None:
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = file.read().split()
        while words:
            print('Choose one of the words and enter it into guesser and a game:')
            print(*words)
            suggested_word = input()
            answer = input()
            if answer == '22222':
                print(f'Congratulations you won')
                break
            words = filter_words(words, suggested_word, answer)


if __name__ == '__main__':
    main()

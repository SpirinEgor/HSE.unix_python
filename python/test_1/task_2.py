import re
from typing import Tuple, List

INPUT_FILE = "lorem_ipsum.txt"


def collect_statistic_from_file(path_to_file: str) -> Tuple[List[Tuple[str, int]], int]:
    word2count = {}
    n_sentences = 0
    with open(path_to_file, "r") as input_file:
        for line in input_file:
            sentences = re.split(r"[\.\!\?]", line)
            n_sentences += len(sentences)
            for sentence in sentences:
                sentence = re.sub(r"[\.\,\-\:]", "", sentence)
                words = sentence.split(" ")
                for word in words:
                    word = word.strip()
                    if len(word) == 0:
                        continue
                    if word not in word2count:
                        word2count[word] = 0
                    word2count[word] += 1

    sorted_words = list(sorted([(_w, _c) for _w, _c in word2count.items()], key=lambda _t: _t[1], reverse=True))
    return sorted_words, n_sentences


def get_next_words(sorted_words: List[Tuple[str, int]], word: str, next_k: int):
    word_pos = -1
    for i, (cur_word, cnt) in enumerate(sorted_words):
        if cur_word == word:
            word_pos = i
            break
    if word_pos == -1:
        raise TypeError(f"Can't find {word} in given statistic")
    n_words = sum([_c for _, _c in sorted_words])
    for i in range(word_pos + 1, min(len(sorted_words), word_pos + 1 + next_k)):
        word, cnt = sorted_words[i]
        print(f"{word}: {cnt / n_words}")


if __name__ == '__main__':
    _sorted_words, _n_sentence = collect_statistic_from_file(INPUT_FILE)
    print("top 10 words in file:")
    print("\n".join(map(lambda _t: f"{_t[0]}: {_t[1]}", _sorted_words[:10])))
    print(f"number of sentences: {_n_sentence}")
    _word = "Lorem"
    print(f"next top 3 words after {_word}:")
    get_next_words(_sorted_words, _word, 3)

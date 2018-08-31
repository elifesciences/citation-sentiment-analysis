import os

from ..utils.download import download_if_not_exists
from ..utils.string import lower_all, strip_all


words_en_download_url = 'http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt'

data_path = 'data'
words_en_txt = os.path.join(data_path, 'wordlist/wordsEn.txt')


def download_and_read_english_words():
    download_if_not_exists(words_en_download_url, words_en_txt)
    with open(words_en_txt, 'r') as word_file:
        return set(lower_all(strip_all(word_file)))

import random
from webbrowser import get

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
def draw_letters():
    letters = []
    letter_pool_dict = LETTER_POOL.copy()
    
    # generates list of letters for each letter amount in values
    letter_list = [key for key, value in letter_pool_dict.items() for value in range(value)]
    print(letter_list)

    while len(letters) < 10:
        # get one random letter in the letter list
        letter = random.choice(letter_list)
        # adds random letter to letters
        letters.append(letter)
        # removes letter from letter_list
        letter_list.remove(letter)

    return letters

draw_letters()
def uses_available_letters(word, letter_bank):
    word_list = list(word.upper())
    letter_bank_copy = letter_bank.copy()
    return_list = []
    # checks every letter in user's word
    for letter in word_list:
        if letter in letter_bank_copy:
            # if letters in letter bank, add letters to return_list
            return_list.append(letter)
            # remove the letters from letter bank 
            letter_bank_copy.remove(letter)
    # return True of False
    return word_list == return_list

def score_word(word):
    score_dict = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        ('K'): 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }

    word_upper = word.upper()
    score = 0
    for letter in word_upper:
        for key in score_dict:
            if letter in key:
                score += score_dict[key]
    if len(word) >= 7 and len(word) <= 10:
        score += 8
    return score

def get_highest_word_score(word_list):
    # create a dict which has word as key and its socre as value
    word_score_dict = {}
    for word in word_list:
        score = score_word(word)
        word_score_dict[word] = score
    
    highest_score = max(word_score_dict.values())
    # put all the same highest score words in a dict
    highest_dict = {word: word_score_dict[word] for word, value in word_score_dict.items() if value == highest_score}
    # get a word has the min len in highest dict
    min_len_word = min(list(highest_dict.keys()), key=len)
    # check every word in dict and return ten letters word
    for k, v in highest_dict.items():
        if len(k) == 10:
            return k, v
    # check every word in dic and return the shortest word
    for k, v in highest_dict.items():
        if k == min_len_word:
            return k, v
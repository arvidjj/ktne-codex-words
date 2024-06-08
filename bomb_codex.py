'''
# used for testing purposes

slot1 = ["t", "s", "y", "g", "i", "n"]
slot2 = ["j", "v", "e", "w", "y", "f"]
slot3 = ["v", "c", "s", "k", "b", "j"]
slot4 = ["t", "c", "e", "l", "k", "q"]
slot5 = ["r", "k", "q", "g", "c", "b"] 
'''

word_list = [
    'about', 'after', 'again', 'below', 'could',
    'every', 'first', 'found', 'great', 'house',
    'large', 'learn', 'never', 'other', 'place',
    'plant', 'point', 'right', 'small', 'sound',
    'spell', 'still', 'study', 'their', 'there',
    'these', 'thing', 'think', 'three', 'water',
    'where', 'which', 'world', 'would', 'write'
]

'''
    I think it is already done by this point forwards, but I will keep the code here just in case
        |
        |
        v
'''

# (1) simple function to find all the words that have the letters the user has entered in the slot
def find_all_word_occurences_on_slot_letters(slot_index, letter_list):
    returned_words = []
    for word in word_list:
        for letter in letter_list:
            if word[slot_index] == letter:
                returned_words.append(word)
    return returned_words

# (2) check if the word appears in every slot
def check_single_word_in_slots(word, slots):
    selected_slots = []
    # we need to filter only the slots the user has entered a letter in
    for slot in slots:
        if len(slot) > 0:
            selected_slots.append(slot)
    # check for every slot, if the word appears on every slot, return true, if there is at least one without the word, return false
    for slot in selected_slots:
        if word in slot:
            continue
        else:
            return False
    return True

# (3) iterate over each word and check if it appears in every slot
# this is simply a "if this word appears on every slot, then it's a correct word"
def iterate_over_each_word(words):
    matches = []
    for word in words:
        for single_word in word:
            if check_single_word_in_slots(single_word, words):
                matches.append(single_word)
    return remove_duplicates_from_array(matches)

def remove_duplicates_from_array(array):
    return list(dict.fromkeys(array))

'''
basically we use the find_all_word_occurences_on_slot_letters function to find 
all the words that have the letters the user has entered in the slot
then we check if the word appears in every slot, if it does, we append it to the matches list
also check_single_word_in_slots already filters out the slots that have no letters entered for a more dynammic approach
'''
def main():
    words1 = (find_all_word_occurences_on_slot_letters(0, ["x", "n"]))
    words2 = (find_all_word_occurences_on_slot_letters(1, ["x", "e"]))
    words3 = (find_all_word_occurences_on_slot_letters(2, ["x", "v"]))
    words4 = (find_all_word_occurences_on_slot_letters(3, ["x", "e"]))
    words5 = (find_all_word_occurences_on_slot_letters(4, ["x", "r"]))

    words = [words1, words2, words3, words4, words5]
    print(remove_duplicates_from_array(iterate_over_each_word(words)))


if __name__ == "__main__":
    main()

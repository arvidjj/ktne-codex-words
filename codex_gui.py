import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from bomb_codex import *

class LetterInput(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.all_input_fields = []
        # need to store each slot into a list
        self.slot1_input_fields = []
        self.slot2_input_fields = []
        self.slot3_input_fields = []
        self.slot4_input_fields = []
        self.slot5_input_fields = []

        for slot_index in range(5):
            self.add_slot(slot_index)

        self.word_list = QListWidget()
        self.layout.addWidget(self.word_list)

        self.setLayout(self.layout)
    
    def add_slot(self, slot_index):
        slot_layout = QHBoxLayout()
        input_fields = []

        for field_index in range(5):
            line_edit = QLineEdit()
            line_edit.setMaxLength(1)  # only allow 1 character
            line_edit.setFixedSize(30, 30)

            line_edit.textChanged.connect(lambda text, si=slot_index, fi=field_index: self.handle_input_change(text, si, fi))
            slot_layout.addWidget(line_edit)
            input_fields.append(line_edit)


        self.all_input_fields.append(input_fields)
        if slot_index == 0:
            self.slot1_input_fields = input_fields
        elif slot_index == 1:
            self.slot2_input_fields = input_fields
        elif slot_index == 2:
            self.slot3_input_fields = input_fields
        elif slot_index == 3:
            self.slot4_input_fields = input_fields
        elif slot_index == 4:
            self.slot5_input_fields = input_fields

        self.layout.addLayout(slot_layout)
    
    '''
        Get all the letters from a slot
    '''
    def get_all_letters_from_slot(self, slot_index):
        letters = []
        if slot_index == 0:
            for field in self.slot1_input_fields:
                letters.append(field.text())
        elif slot_index == 1:
            for field in self.slot2_input_fields:
                letters.append(field.text())
        elif slot_index == 2:
            for field in self.slot3_input_fields:
                letters.append(field.text())
        elif slot_index == 3:
            for field in self.slot4_input_fields:
                letters.append(field.text())
        elif slot_index == 4:
            for field in self.slot5_input_fields:
                letters.append(field.text())
        return letters

    '''
        When the user enters a letter check for every possible word that can exist with the letters in the slots
        and then display it on the list
    '''
    def handle_input_change(self, text, slot_index, field_index):
        print(f"Slot {slot_index}, Field {field_index}, Text: {text}")

        # this is where the codex does his thing
        # get all letters from the slots
        # find all words that contain the letters in the slots
        words1 = (find_all_word_occurences_on_slot_letters(0, self.get_all_letters_from_slot(0)))
        words2 = (find_all_word_occurences_on_slot_letters(1, self.get_all_letters_from_slot(1)))
        words3 = (find_all_word_occurences_on_slot_letters(2, self.get_all_letters_from_slot(2)))
        words4 = (find_all_word_occurences_on_slot_letters(3, self.get_all_letters_from_slot(3)))
        words5 = (find_all_word_occurences_on_slot_letters(4, self.get_all_letters_from_slot(4)))
        words = [words1, words2, words3, words4, words5]

        # iterate over each word and check if it appears in every slot, if so return each word that was found
        # this is simply a "if this word appears on every slot, then it's a correct word"
        # because if it doesn't appear on every slot, then it's not possible to be correct
        found_words = iterate_over_each_word(words)
        # display it on the gui list
        self.append_all_words(found_words)

    def append_word(self, word):
        if word: 
            self.word_list.addItem(QListWidgetItem(word))
    '''
        Add all the words to the list, clearing first ofc
    '''
    def append_all_words(self, words):
        self.word_list.clear()
        for word in words:
            self.append_word(word)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LetterInput()
    window.setWindowTitle("Codex Defuser")
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec())


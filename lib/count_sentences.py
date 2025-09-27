#!/usr/bin/env python3


class MyString:
    def __init__(self, value=""):
        self.value = value  # runs through the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            

    def is_sentence(self):
        return self.value.endswith(".")
      
    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
      
    def count_sentences(self):
        count = 0
        for i in range(len(self.value)):
            if self.value[i] in ".?!" and (i == len (self.value) -1 or self.value[i+1] not in ".?!"):
               count += 1
        return count
        
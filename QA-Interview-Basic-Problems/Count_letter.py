# ============================================================
# Day 15 - Count Character Frequency
#
# Difficulty:
# Easy
#
# New Concept:
# Dictionary (dict)
#
# ------------------------------------------------------------
#
# Problem Statement
#
# Given a string,
# count how many times each character appears.
#
# Return the result as a dictionary.
#
# Spaces should also be counted.
#
# The comparison is case-sensitive.
#
# ------------------------------------------------------------
#
# Example 1
#
# Input:
#
# "banana"
#
# Output:
#
# {
#     'b':1,
#     'a':3,
#     'n':2
# }
#
# ------------------------------------------------------------
#
# Example 2
#
# Input
#
# "Hello"
#
# Output
#
# {
#     'H':1,
#     'e':1,
#     'l':2,
#     'o':1
# }
#
# ------------------------------------------------------------
#
# Create
#
# class CharacterCounter
#
# def count_frequency(self)
#
#
# ------------------------------------------------------------
#
# Required Test Cases
#
# ""
#
# "a"
#
# "aaaa"
#
# "banana"
#
# "Hello"
#
# "Hello World"
#
# "112233"
#
# "@@!!"
#
# "AaAa"
#
# "বাংলা"
#
# "😊😊😂"
#
# ------------------------------------------------------------
#
# Bonus 1
#
# Print the most frequent character.
#
#
# Bonus 2
#
# Ignore case.
#
# "AaAa"
#
# should become
#
# {
#     'a':4
# }
#
# ============================================================

# --- without class ------
def get_character_from_number(position):
    return chr(position + 65)

def count_letter(str):
    counter = [0]*26

    for chr in str:
        letter_number = (ord(chr.upper()) - 65) 
        counter[letter_number] += 1

    return counter


# --- using class object ---

class CharacterCounter:
    
    @staticmethod
    def character_counter(string):
        counter = {}
        for ch in string:
            key = ch.upper()
            if key not in counter:
                counter[key] = 1
            else:
                counter[key] += 1

        return counter 
        

if __name__=="__main__":
    result = count_letter("abccdeffg")
    position = 0
    for x in result:
        if x != 0:
            print(f"{get_character_from_number(position)}:{x}")
        position += 1

    print(CharacterCounter.character_counter("aAAbccdeffg"))
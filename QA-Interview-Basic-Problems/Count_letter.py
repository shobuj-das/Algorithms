def get_character_from_number(position):
    return chr(position + 65)

def count_letter(str):
    counter = [0]*26

    for chr in str:
        letter_number = (ord(chr.upper()) - 65) 
        counter[letter_number] += 1

    return counter
    
if __name__=="__main__":
    result = count_letter("abccdeffg")
    position = 0
    for x in result:
        if x != 0:
            print(f"{get_character_from_number(position)}:{x}")
        position += 1
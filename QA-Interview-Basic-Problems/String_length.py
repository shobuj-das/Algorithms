def string_length(text):
    counter = 0
    for x in text:
        if x != '\0':
            counter += 1

    return counter

def string_length_count_using_while_loop(text):
    counter = 0
    i = 0
    while True:
        try:
            if isinstance(text[i], str):
                counter += 1
                i += 1
        except IndexError:
            break

    return counter


if __name__=='__main__':
    print( string_length('abcddf'))
    print(string_length_count_using_while_loop("abcd"))
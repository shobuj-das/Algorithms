def reverseString(text):
    text_list = list(text)

    size = len(text)
    y = size - 1

    for x in range(size//2):
        text_list[x],text_list[y] = text_list[y], text_list[x]
        y -= 1

    rev_str = "".join(text_list)

    print(rev_str)

text = input("enter text: ")
reverseString(text)
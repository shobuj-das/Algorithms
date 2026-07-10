# Problem Statement

# Given a string containing only:

# ( ) { } [ ]

# Determine whether the string is valid.

# A string is valid if:

# Every opening bracket has a matching closing bracket.
# Brackets close in the correct order.


def is_valid_parentheses(text):
    track = []
    opening = "({["
    closing = ")}]"
    matcing = ["()", "{}", "[]"]
    # print(matcing)
    for x in text:
        if x in opening:
            # print(f'{x} -> oepning')
            track.append(x)
            # print(track)
        elif x in closing:
            if len(track) == 0:
                return False
            # print(f'{x} -> closing')
            temp = track[-1] + x
            # print(f'{temp} -> temp')
            if temp in matcing:
                track.pop()
                # print(track)
            else:
                return False
        
    # return True
    if len(track) == 0:
        return True
    else:
        return False


if __name__=="__main__":
    print(is_valid_parentheses(""))            # True
    print(is_valid_parentheses("()"))          # True
    print(is_valid_parentheses("()[]{}"))      # True
    print(is_valid_parentheses("(]"))          # False
    print(is_valid_parentheses("([)]"))        # False
    print(is_valid_parentheses("{[]}"))        # True
    print(is_valid_parentheses("((()))"))      # True
    print(is_valid_parentheses("((())"))       # False
    print(is_valid_parentheses(")))"))         # False
    print(is_valid_parentheses("{{{{}}}}"))    # True
    print(is_valid_parentheses("[[[[]]]]"))    # True
    print(is_valid_parentheses("{[(])}"))      # False
            

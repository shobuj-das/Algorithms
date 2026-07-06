# Problem Statement

# Given a string, return the first character that appears only once.

# If every character repeats, return None.

def finding_first_not_repeating_character(string):
    
    str_len = len(string)
    found_char = None

    for i in range(str_len):
        duplicateFound = False
        for j in range(str_len):
            if i != j:
                if string[i] == string[j]:
                    duplicateFound = True
                    break
        if not duplicateFound:
            # found_char =  string[i]
            # break
            return string[i]

    return found_char
        

if __name__=='__main__':
    # Empty string
    print(finding_first_not_repeating_character(""))

    # Single character
    print(finding_first_not_repeating_character("a"))

    # Two characters
    print(finding_first_not_repeating_character("ab"))
    print(finding_first_not_repeating_character("aa"))

    # All unique
    print(finding_first_not_repeating_character("abc"))
    print(finding_first_not_repeating_character("abcdef"))

    # All repeated
    print(finding_first_not_repeating_character("aabbcc"))
    print(finding_first_not_repeating_character("aabbccddeeff"))

    # First character is unique
    print(finding_first_not_repeating_character("abcdd"))
    print(finding_first_not_repeating_character("leetcode"))

    # Last character is unique
    print(finding_first_not_repeating_character("aabbccd"))
    print(finding_first_not_repeating_character("aabbccdde"))

    # Middle character is unique
    print(finding_first_not_repeating_character("abac"))
    print(finding_first_not_repeating_character("loveleetcode"))
    print(finding_first_not_repeating_character("automation"))

    # Unique character surrounded by duplicates
    print(finding_first_not_repeating_character("aabcc"))
    print(finding_first_not_repeating_character("bbacc"))

    # Multiple unique characters
    print(finding_first_not_repeating_character("abcd"))
    print(finding_first_not_repeating_character("xyzxyzab"))

    # Numbers
    print(finding_first_not_repeating_character("112233445"))
    print(finding_first_not_repeating_character("123451234"))
    print(finding_first_not_repeating_character("9999991"))

    # Special characters
    print(finding_first_not_repeating_character("@@##$$%"))
    print(finding_first_not_repeating_character("!!@@##"))
    print(finding_first_not_repeating_character("$$%%^^&&*"))

    # Spaces
    print(finding_first_not_repeating_character(" "))
    print(finding_first_not_repeating_character("a a"))
    print(finding_first_not_repeating_character("hello world"))

    # Mixed case (case-sensitive)
    print(finding_first_not_repeating_character("Aa"))
    print(finding_first_not_repeating_character("aA"))
    print(finding_first_not_repeating_character("AaBbAa"))

    # Long repeated string
    print(finding_first_not_repeating_character("aaaaaaaaaaaaaaaaaaaaaaaaab"))

    # Unicode
    print(finding_first_not_repeating_character("বাংলা"))
    print(finding_first_not_repeating_character("আআম"))
    print(finding_first_not_repeating_character("😊😊😂"))
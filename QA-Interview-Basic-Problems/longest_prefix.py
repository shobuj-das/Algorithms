# Problem Statement

# Given a list of strings, find the longest common prefix shared by all strings.

def longest_common_prefix(words):
    if len(words) == 0:
        return None
    
    first_word = words[0]
    flag = True
    prefix = []
    index = 0
    for ch in first_word:
        for word in words:
            if word[index] != ch:
                flag = False
        if flag:
            break
        prefix.append(ch)
    prefix = "".join(prefix)
    return prefix

if __name__=="__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))      # fl
    # print(longest_common_prefix(["dog", "racecar", "car"]))         # ""
    # print(longest_common_prefix(["interview", "internet", "internal"])) # inter
    # print(longest_common_prefix(["apple", "apple"]))                # apple
    # print(longest_common_prefix([""]))                              # ""
    # print(longest_common_prefix([]))                                # ""
    # print(longest_common_prefix(["a"]))                             # a
    # print(longest_common_prefix(["ab", "a"]))                       # a
    # print(longest_common_prefix(["abc", "abcd", "abcde"]))          # abc
    # print(longest_common_prefix(["prefix", "pre", "prevent"]))      # pre
    # print(longest_common_prefix(["same", "same", "same"]))          # same
    # print(longest_common_prefix(["abc", "xyz"]))                    # ""
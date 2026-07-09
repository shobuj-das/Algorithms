# Problem Statement

# Given a list of strings, find the longest common prefix shared by all strings.

def longest_common_prefix(words):
    if not words:
        return ""
    
    stop = False
    prefix = []
    first_word = words[0]
    for i in range(len(first_word)):
        for j in range(1,len(words)):
            word = words[j]
            if i >= len(word):
                stop = True
                break
            elif first_word[i] != word[i]:
                stop = True
                break
          
        if stop:
            break
        prefix.append(first_word[i])
        
    prefix = "".join(prefix)

    return prefix

if __name__=="__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))      # fl
    print(longest_common_prefix(["dog", "racecar", "car"]))         # ""
    print(longest_common_prefix(["interview", "internet", "internal"])) # inter
    print(longest_common_prefix(["apple", "apple"]))                # apple
    print(longest_common_prefix([""]))                              # ""
    print(longest_common_prefix([]))                                # ""
    print(longest_common_prefix(["a"]))                             # a
    print(longest_common_prefix(["ab", "a"]))                       # a
    print(longest_common_prefix(["abc", "abcd", "abcde"]))          # abc
    print(longest_common_prefix(["prefix", "pre", "prevent"]))      # pre
    print(longest_common_prefix(["same", "same", "same"]))          # same
    print(longest_common_prefix(["abc", "xyz"]))                    # ""
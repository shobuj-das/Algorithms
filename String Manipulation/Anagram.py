# def checkAnagram(str1, str2):
#
#     list1 = list(str1)
#     list2 = list(str2)
#
#     list1.sort()
#     list2.sort()
#
#     # str1 = ''.join(list1)
#     # str2 = ''.join(list2)
#     # if str1 == str2:
#     #     return True
#     # else:
#     #     return False
#
#     for x in range(len(list1)):
#         if list1[x] != list2[x]:
#             return False
#     return True
#
# print(checkAnagram("anagram", "nagaram"))


def checkAnagram(str1, str2):
    list1 = list(str1)
    list2 = list(str2)

    for x in list1:
        if x in list2:
            list2.remove(x)
        else:
            return False
    return True

print(checkAnagram("anagram", "nagaram"))

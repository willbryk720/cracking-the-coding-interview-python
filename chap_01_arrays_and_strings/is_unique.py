'''
Implement an algorithm to determine of a string has all unique characters.

A: Create hashtable of possible ascii characters. Run through characters and check if character has already been 
hashed.
'''

def is_unique(s):
    chars = [False] * 256
    for c in s:
        ascii_value = ord(c)
        if chars[ascii_value]:
            return False
        else:
            chars[ascii_value] = True
    return True


'''
Followup: What if you cannot use additional data structures?

A: We can sort the string and check for the same character next to each other. Note this assumes sort does not use 
Other data structures
'''

def is_unique2(s):
    list(s).sort()
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


solutions = [["", True],["h", True], ["hh", False], ["hellothere", False],  ["hellllothere", False],  ["ethr", True]]
for solution in solutions:
    print solution, is_unique(solution[0]), is_unique2(solution[0])
    assert is_unique(solution[0]) == solution[1]
    assert is_unique2(solution[0]) == solution[1]
    
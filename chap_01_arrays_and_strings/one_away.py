'''
Write function to check if one string is one away from another. 
Meaning, can delete one letter from one string to get to the other, or replace one letter

A: Handle two cases separately
'''

def one_away(s_tuple):
    s1, s2 = s_tuple
    s1_len, s2_len = len(s1), len(s2)
    if s1_len == s2_len:
        return check_replace(s1, s2)
    elif s1_len - s2_len == 1:
        return check_remove(s1, s2)
    elif s2_len - s1_len == 1:
        return check_remove(s2, s1)
    else:
        return False
    
def check_replace(s1, s2):
    one_diff_used = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if one_diff_used:
                return False
            else:
                one_diff_used = True
    return True

def check_remove(big_s, small_s):
    one_diff_used = False
    big_index = 0
    for small_index in range(len(small_s)):
        if big_s[big_index] != small_s[small_index]:
            if one_diff_used:
                return False
            else:
                big_index += 1
        big_index += 1
    return True
        
        
tests = [
{"input":  ("pale", "ple"), "answer": True},
{"input":  ("pales", "pale"), "answer": True}, 
{"input":  ("pale", "bale"), "answer": True},
{"input":  ("pale", "bake"), "answer": False}, 
]

for test in tests:
    q1, a1 = test["input"], one_away(test["input"])
    assert a1 == test["answer"]

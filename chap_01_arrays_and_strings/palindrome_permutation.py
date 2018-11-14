'''
Write function to check if a string has a permutation that is a palindrome. The palindrome 

A: Create bit vector that holds whether the number of that character 
with the ascii value at the index in the bit vector is even
'''

def palindrome_permutation(s):
    bitVectorOfEvens = [True] * 52
    numOdds = 0
    for c in s:
        ascii_value = ord(c)
        if ascii_value >= 65 and ascii_value <= 90:
            index = ascii_value - 39
        elif ascii_value >= 97 and ascii_value <= 122:
            index = ascii_value - 97
        
        isEven = bitVectorOfEvens[index]
        numOdds = numOdds + 1 if isEven else numOdds - 1

        bitVectorOfEvens[index] = not isEven
    
    return numOdds <= 1
        

tests = [
{"input":  "", "answer": True},
{"input":  "h", "answer": True}, 
{"input":  "hi", "answer": False},
{"input":  "hello", "answer": False}, 
{"input":  "heehll", "answer": True}, 
{"input":  "heehllo", "answer": True}
]

for test in tests:
    q1, a1 = test["input"], palindrome_permutation(test["input"])
    assert a1 == test["answer"]

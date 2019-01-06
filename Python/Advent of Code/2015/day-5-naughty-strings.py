# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

def vowelCount(string):
    vowelCounter = 0
    vowels = ["a","e","i","o","u"]
    for characters in string:
        if characters in vowels:
            vowelCounter += 1
            if vowelCounter == 3:
                return True
    return False

def doubleCharacterChecker(string):
    lastCheckedLetter = ''
    for character in string:
        if character == lastCheckedLetter:
            return True
        else:
            lastCheckedLetter = character
    return False

def naughtyStringEvaluator(string):
    naughtyStrings = ["ab", "cd", "pq", "xy"]
    for naughtyString in naughtyStrings:
        if naughtyString in string:
            return True
    return False



def main():
    niceCount = 0
    with open('day-5-naughty-strings.txt', 'r') as f:
        stringsList = f.read().splitlines()
        for string in stringsList:
            if vowelCount(string) == True:
                if doubleCharacterChecker(string) == True:
                    if naughtyStringEvaluator(string) == False:
                        niceCount += 1
    print(niceCount)    





if __name__ == "__main__":
    main()
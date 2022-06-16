from data import baseDict
import random

# WORDS TO CHOOSE FROM: bloom, doom, cat, zoom

enterWord = input("Enter a word: ")
numSynonym = int(input("Enter the number of synonyms you want: "))

def givenWord(inputWord, numSyn):
    if inputWord in baseDict:
        keyList = baseDict[str(inputWord)]
        randomValue = random.sample(keyList, numSyn)
        print("The synonym(s) of", inputWord, "is: ", randomValue)
    else:
        print("Based on my limited knowledge of words, I don't know the synonym of ", inputWord)

synonym = givenWord(enterWord, numSynonym)
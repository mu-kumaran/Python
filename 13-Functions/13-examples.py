# Count words in string using dictionary

def CountWords(args):
    sentence = []
    countDict = {}
    sentence = args.split(" ")
    for key in sentence:
        countDict[key] = sentence.count(key)
    print(countDict) 

if __name__ == "__main__":
    sentence = input("Enter the sentence: ")
    CountWords(sentence)
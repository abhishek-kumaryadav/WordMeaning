from WordMeaningClass import WordMeaningClass
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        meanings = WordMeaningClass(filename)
        meanings.generate_meanings()
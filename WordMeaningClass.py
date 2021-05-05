import sys
from PyDictionary import PyDictionary


class WordMeaningClass:
    def __init__(self, filename):
        self.filename = filename
        self.writename = filename[0:-9] + "meaning.txt"
        self.d = PyDictionary()

    def generate_meanings(self):
        with open(self.filename, "r") as f, open(self.writename, "a+") as w:
            for i, line in enumerate(f):
                if line.strip() != "":
                    word = (
                        line.strip()
                        .lstrip('"')
                        .rstrip('"')
                        .strip()
                        .replace("(", "")
                        .replace(")", "")
                        .replace(":", "")
                        .replace(",", "")
                        .replace(".", "")
                    )
                    # word = "perils"
                    # print(word)
                    # for mean in d.meaning(word, disable_errors=True):
                    #     print(mean)
                    # print(d.meaning(word, disable_errors=True))
                    out = "\n{}:\n{}\nSynonym:{}\nAntonym:{}\n".format(
                        word,
                        self.d.meaning(word, disable_errors=True),
                        self.d.synonym(word),
                        self.d.antonym(word),
                    )
                    w.write(out)
                    print(out)
        print("All word meanings saved to: {}".format(self.writename))
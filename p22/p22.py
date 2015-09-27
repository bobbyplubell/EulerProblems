import csv
import string

def alpha_to_digit(ch):
    return ord(string.lower(ch))-96

def scores(filename):
    i = 1
    total_score = 0
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar = '"')
        for row in reader:
            row.sort()
            for val in row:
                score = 0
                for ch in val:
                    score += alpha_to_digit(ch)
                score *= i
                total_score += score
                i += 1

    return total_score

if __name__ == "__main__":
    print(scores('names.txt'))

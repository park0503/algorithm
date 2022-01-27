import sys


def main():
    while True:
        sentence = sys.stdin.readline()
        if sentence == ".\n":
            break
        bracket = []
        skip = False
        for word in sentence:
            if word == "(" or word == "[":
                bracket.append(word)
                continue
            if word == ")":
                if bracket and bracket[-1] == "(":
                    bracket.pop()
                else:
                    print("no")
                    skip = True
                    break
            elif word == "]":
                if bracket and bracket[-1] == "[":
                    bracket.pop()
                else:
                    print("no")
                    skip = True
                    break
        if skip:
            continue
        elif bracket:
            print("no")
        else:
            print("yes")


main()

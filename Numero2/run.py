import sys

def countE(proposition):
    return proposition.count('e')

def countWords(proposition):
    return len(proposition.split())

def countConsecutive(proposition):
    return proposition.count(proposition[-1])


if len(sys.argv) != 1:
    print("Please put the proposition as the argument! i.e. ./start.sh \"Give me less import taxes.\"")
    exit(1)

proposition = sys.argv[0]

negotiate = countE(proposition)
refused = countWords(proposition)
accepted = countConsecutive(proposition)

if accepted < refused:
    if refused < accepted:
        print("Negotiate")
    else
        if refused < negotiate:
            print("Negotiate")
        else
            print("Refuse")
else
    if accepted < negotiated:
        if refused < accepted:
            print("Negotiate")
        else
            if refused < negotiate:
                print("Negotiate")
            else
                print("Refuse")
    else
        print("Accepted")



    













import keyword
from beautifultable import BeautifulTable


def is_keyword(item):
    if item in keyword.kwlist:
        return True
    else:
        # if the item is'nt keyword or String it is definitly identifier!
        return False


operators = ['+', '-', '*', '/', '<', '>', '=', '!', '&', '|']


def is_Operator(char):
    if char in operators:
        return True
    else:
        return False


delimiter = {'(', ')', '[', ']', '{', '}', ',', ':', '.', ';'}


def is_Delimiter(char):
    if char in delimiter:
        return True
    else:
        return False


workfile = input("Enter Python file (.py) address: ")

try:
    fin = open(workfile, 'r', encoding="utf8")
    file_lines = fin.readlines()
except:
    print("Input file does not exists: ", workfile)
    quit(0)

row = 0
float = 1.5
lst = ""
result = BeautifulTable()
result.columns.header = ["Token", "Token_Type", "Block_No", "Row", "Column"]

for item in file_lines:
    i = 0
    Block_No = 0
    first_of_line = True
    while i < len(item):
        char = item[i]
        column = i
        # To calculate Block_No.
        if first_of_line and char == " ":
            while char == " ":
                i += 1
                char = item[i]
            Block_No = int(i / 4)
        elif char == "#":
            break

        # Ignore strings in code.
        elif char == "\"":
            first_of_line = False
            i += 1
            char = item[i]
            previous_char = item[i - 1]
            while True:
                if char == "\"":
                    if previous_char != "\\":
                        break
                    else:
                        two_previous_char = item[i - 2]
                        if two_previous_char == "\\":
                            break
                i += 1
                char = item[i]
                previous_char = item[i - 1]

            i += 1


        elif char.isalpha() or char == "_":
            first_of_line = False
            word = ""
            column = i
            while char.isalpha() or char == "_":
                # Form words to determine if they are keywords or identifiers
                word = word + char
                i += 1
                char = item[i]
            if is_keyword(word):
                lst = [word, "keyword", Block_No, row + 1, column]
                result.rows.append(lst)
            else:
                lst = [word, "identifier", Block_No, row + 1, column]
                result.rows.append(lst)

        elif is_Operator(char):
            first_of_line = False
            # opt = ""
            # column = i
            # while is_Operator(char):
            #     opt = opt + str(char)
            #     i += 1
            #     char = item[i]
            lst = [char, "operator", Block_No, row + 1, column]

            result.rows.append(lst)
            i += 1


        elif is_Delimiter(char):
            first_of_line = False
            lst = [char, "delimiter", Block_No, row + 1, i]
            result.rows.append(lst)

            i += 1

        elif char.isnumeric():
            first_of_line = False
            digit = ""
            column = i
            while char.isnumeric():
                digit = digit + str(char)
                i += 1
                char = item[i]
            lst = [digit, "digit", Block_No, row + 1, column]

            result.rows.append(lst)

        else:
            first_of_line = False
            i += 1
    row += 1

print(result)

from sys import *

tokens = []  # list of tokens


def open_file(file):  # open file and return string or data
    data = open(file, "r").read()
    return data


def check_file(filecontents):  # Remove spaces a check if syntax is correct
    tok = ""
    filecontents = list(filecontents)
    for char in filecontents:  # cycle threw and add each char to the last
        tok += char   # add the previous char(s) to the current char
        if tok == " ":   # ignore spaces
            tok = ""
        elif tok == "T":
            tokens.append("T")
            tok = ""
        elif tok == "F":
            tokens.append("F")
            tok = ""
        elif tok == "~":
            tokens.append("~")
            tok = ""
        elif tok == "->":
            tokens.append("->")
            tok = ""
        elif tok == ".":
            tokens.append(".")
            tok = ""
        elif tok == "^":
            tokens.append("^")
            tok = ""
        elif tok == "v":
            tokens.append("v")
            tok = ""
        elif tok == "\n":
            tok = ""
        # TODO put in the case for "()"!!!!!!!!!!
        else:
            print("error")
            return "error"
    # print(tokens)
    return tokens


def Bool_def():  #Interpretation starts here
    if(Var_def(var) and Imply_term(s.pop())):
        return True
    else:
        return False


def Var_def(var):
    if(var == "#"):
        var == Imply_term;
    elif(Var_def(var):
        return True
    elif(var == ""):
        return True
    else:
        return False


def Imply_term(var):
    if(Connect_term(var) and Imply_tail(s.pop())):
        return True
    else:
        return False


def Imply_tail(var):
    if(var == "->" and Connect_term(s.pop()) and Imply_tail(s.pop())):
        return True
    elif(var == ""):
        return True
    else:
        return False


def Connect_term(var):
    if(Literal(var) and Connect_tail(var)):
        return True
    else:
        return False


def Connect_tail(var):
    if(var == "v" and Literal(s.pop()) and Connect_tail(s.pop())):
        return True
    elif(var == "^" and Literal(s.pop()) and Connect_tail(s.pop())):
    elif(var == ""):
        return True
    else:
        return False


def Literal(var):
    if(Atom(var)):
        return True
    elif(var == "~" and Literal(s.pop())):
        return True
    else:
        return False


def Atom(var):
    if(var == "T"):
        return True
    elif(var == "F"):
        return True
    elif(var == "("):
        if(Imply_term(s.pop())):
            if(s.pop() == ")"):
                True
            else:
                False
        else:
            False
    else:
        print("Error: Enter 'T', 'F', or '()'")
        return False




def load_stack(tokens):  # put tokens into stack
    for i in reversed(tokens):
        s.push(i)


class Stack:  # stack class with functions
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printstack(self):
        for items in reversed(self.items):
            print(items)


s = Stack()  # create the stack


def __run__():  # main
    file = input("File name: ")  # input the file to interpret
    data = open_file(file)  # gets data from file input
    toks = check_file(data)  # lexes data
    load_stack(toks)  # puts data on stack
    if(Bool_def):  # calls interpreter
        print("valid")
    else:
        print("invalid")


__run__()  
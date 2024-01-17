
class Stack:

    def __init__(self):
        self.Top = -1
        self.myStack = []

    def charPair(self, openChar, closeChar):
        if openChar == "(" and closeChar == ")":
            return True
        if openChar == "{" and closeChar == "}":
            return True
        if openChar == "[" and closeChar == "]":
            return True
        if self.myStack[self.Top] == "+*/":
            return False
        return False

    def Push(self, item):
        for char in item:  # "{())}":

            if char in "({[":
                self.Top += 1
                self.myStack.append(char)  # }
            elif char in ")}]":
                if (self.isEmpty()) or not myStack.charPair(self.getTop(), char):
                    return False
                else:
                    self.pop()
        if (item[len(item)-2] in "+-/*" and item[len(item)-1] in "({[]})") or item[len(item)-1] in "+-/*=":
            return False

        return self.isEmpty()

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty!")

        else:
            self.Top -= 1
            self.myStack.pop()

    def getTop(self):
        if self.isEmpty():
            raise Exception("Staack is empty!")
        else:
            return self.myStack[self.Top]

    def isEmpty(self):
        return (len(self.myStack) == 0)

    def __str__(self):
        return str(self.myStack)


while (True):
    try :
        myStack = Stack()
        item = input("Enter the experision : ")

        if (myStack.Push(item)):
            print(eval(item))
        else:
            print("Not Balanced")
    except : raise Exception("Please enter a valid input!")

class Stack:

    def __init__(self):
        # Initialize an empty stack and set the top index to -1
        self.Top = -1
        self.myStack = []

    def charPair(self, openChar, closeChar):
        # Check if the given open and close characters form a valid pair
        pairs = {"(": ")", "{": "}", "[": "]"}
        if openChar in pairs and pairs[openChar] == closeChar:
            return True
        # Additional check for operators
        if openChar == "+" and closeChar in "*/":
            return True
        return False

    def Push(self, item):
        # Iterate through each character in the input expression
        for char in item:
            if char in "({[":
                # Push opening brackets onto the stack
                self.Top += 1
                self.myStack.append(char)
            elif char in ")}]":
                # Check for matching closing brackets
                if self.isEmpty() or not self.charPair(self.getTop(), char):
                    return False
                else:
                    # Pop the matching opening bracket from the stack
                    self.pop()

        # Additional checks for invalid combinations
        if (item[-2] in "+-/*" and item[-1] in "({[]})") or item[-1] in "+-/*=":
            return False

        # Check if the stack is empty at the end (balanced expression)
        return self.isEmpty()

    def pop(self):
        # Pop the top element from the stack
        if self.isEmpty():
            raise Exception("Stack is empty!")
        else:
            self.Top -= 1
            self.myStack.pop()

    def getTop(self):
        # Return the top element of the stack
        if self.isEmpty():
            raise Exception("Stack is empty!")
        else:
            return self.myStack[self.Top]

    def isEmpty(self):
        # Check if the stack is empty
        return len(self.myStack) == 0

    def __str__(self):
        # Return a string representation of the stack
        return str(self.myStack)


while True:
    try:
        # Create a new instance of the Stack class for each iteration
        myStack = Stack()
        # Prompt the user to enter an expression
        item = input("Enter the expression: ")

        # Check if the expression is balanced and evaluate if so
        if myStack.Push(item):
            print(eval(item))
        else:
            print("Not Balanced")
    except:
        raise Exception("Please enter a valid input!")

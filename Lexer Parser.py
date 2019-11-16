class Lexer:
    def __init__(self, source):
        self.source = source
        self.cursor = 0
    def advance(self):
        self.cursor += 1
    def currentChar(self):
        if self.cursor >= len(self.source):
            return '\0'
        return self.source[self.cursor]
    def nextToken(self):
        # Skip through whitespace
        while self.currentChar() in [' ', '\t', '\n', '\r']:
            self.advance()
        # Check for end of file
        if self.currentChar() == '\0':
            return None
        # Check for symbols
        if self.currentChar() in ['(', ')', '+', '-', '*', '/']:
            c = self.currentChar()
            self.advance()
            return c
        # Check for number
        if self.currentChar().isdigit():
            digits = []
            while self.currentChar().isdigit():
                digits.append(self.currentChar())
                self.advance()
            n = int(''.join(digits))
            return n
        raise Exception("Unrecognized char {0}".format(self.currentChar()))

class Operation:
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self)
    def __str__(self): 
        return '({0} {1} {2})'.format(self.left, self.op, self.right)

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = lexer.nextToken()
    def advance(self):
        self.token = lexer.nextToken()
    def parseNumber(self):
        if type(self.token) == int:
            n = self.token
            self.advance()
            return n
        raise Exception("Expected a number")
    def parseParentheses(self):
        if self.token == '(':
            self.advance()
            expr = self.parseAddSubtract()
            if self.token != ')':
                raise Exception("Expected closing parentheses")
            self.advance()
            return expr
        return self.parseNumber()
    def parseMultiplyDivide(self):
        left = self.parseParentheses()
        while self.token in ['*', '/']:
            op = self.token
            self.advance()
            right = self.parseParentheses()
            left = Operation(op, left, right)
        return left
    def parseAddSubtract(self):
        left = self.parseMultiplyDivide()
        while self.token in ['+', '-']:
            op = self.token
            self.advance()
            right = self.parseMultiplyDivide()
            left = Operation(op, left, right)
        return left

def interpret(tree):
    if type(tree) == int:
        return tree
    elif tree.op == '+':
        return interpret(tree.left) + interpret(tree.right)
    elif tree.op == '-':
        return interpret(tree.left) - interpret(tree.right)
    elif tree.op == '*':
        return interpret(tree.left) * interpret(tree.right)
    elif tree.op == '/':
        return interpret(tree.left) / interpret(tree.right)

source = input()
lexer = Lexer(source)
parser = Parser(lexer)
print(interpret(parser.parseAddSubtract()))
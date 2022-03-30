import string 
import sys

# Token Classes
T_PLUS = "ADD"
T_MINUS = "MINUS"
T_MUL = "MUL"
T_DIV = "DIV"
T_IDENTIFIER = "IDENTIFIER"
T_PHPOPEN = "PHPOPENTAG"
T_PHPCLOSE = "PHPCLOSETAG"
T_CLASS = "CLASS"
T_FUNCTION = "FUNCTION"
T_CURLYOPEN = "CURLYOPEN"
T_CURLYCLOSE = "CURLYCLOSE"
T_LITERAL = "STRING-LITERAL"
T_VAR = "VAR"
T_NUMBER = "NUMBER"
T_BOPEN = "BRACKETOPEN"
T_BCLOSE = "BRACKETCLOSE"
T_ECHO = "PRINT-OUTPUT"
T_ASSIGN = "ASSIGN"
T_EOL = "SEMICOLON"
T_CONCATE = "CONCATE"


# IDENTIFIERS
IDENTIFIERS = ["class", "function", "echo"]

# file 
filename = "php.txt"
with open("php.txt") as file:
    data = file.read()

# helper function to keep track of the line NUMBER
def pos(s, index):
    if not len(s):
        return 1,1
    sp = s[:index+1].splitlines(keepends=True)
    return len(sp), len(sp[-1])


# Error class 
class Error():
    def __init__(self, filename, line, col, err_type, message):
        self.filename = filename 
        self.line = line 
        self.col = col
        self.err_type = err_type
        self.message = message

    def __repr__(self):
       return f'{self.filename}, {self.line}, {self.message}, {self.err_type}' 

# Token class for the lexer
class Token():
    def __init__(self, line, col, token_class, value=None):
        self.line = line 
        self.col = col
        self.token_class = token_class 
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.line}, {self.col}, {self.token_class}, {self.value}'
        return f'{self.line}, {self.col}, {self.token_class}'

class Lexer():
    def __init__(self, text):
        self.text = text 
        self.pos = -1
        self.current_char = None
        self.next()

    def next(self):
        self.pos += 1
        self.current_char = (self.text[self.pos] if self.pos < len(self.text) else None)
	
    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            line, col = pos(self.text, self.pos)[0], pos(self.text, self.pos)[1]
            if self.current_char == "+":
                tokens.append(Token(line, col, T_PLUS))
            elif self.current_char == "-":
                tokens.append(Token(line, col, T_MINUS))
            elif self.current_char == "*":
                tokens.append(Token(line, col, T_MUL))
            elif self.current_char == "/":
                tokens.append(Token(line, col, T_DIV))

            # php tags validation
            # open tag 
            elif self.current_char in "<":
                identifier = ""
                while str(self.current_char) in "<?php":
                    identifier += self.current_char
                    self.next()
                if identifier == "<?php":
                    tokens.append(Token(line, col, T_PHPOPEN))
                continue
            # close tag 
            elif self.current_char in "?":
                identifier = ""
                while str(self.current_char) in "?>":
                    identifier += self.current_char
                    self.next()
                if identifier == "?>":
                    tokens.append(Token(line, col, T_PHPCLOSE))


            # identifier and type validation
            elif self.current_char in string.ascii_letters:
                # create an identifier 
                identifier = ""

                # loop through the string, ensuring it's in the alphabet
                while str(self.current_char) in string.ascii_letters:
                    identifier += self.current_char
                    self.next()
                # check for identifiers 
                if identifier in IDENTIFIERS:
                    # check for class or function identifiers 
                    if identifier == IDENTIFIERS[0]: 
                        tokens.append(Token(line, col, T_CLASS))
                    elif identifier == IDENTIFIERS[1]:
                        tokens.append(Token(line, col, T_FUNCTION))
                    elif identifier == IDENTIFIERS[2]:
                        tokens.append(Token(line, col, T_ECHO))
                else:
                    tokens.append(Token(line, col, T_IDENTIFIER, identifier))
                continue 

            # curly validation
            elif self.current_char == "{":
                tokens.append(Token(line, col, T_CURLYOPEN))
            elif self.current_char == "}":
                tokens.append(Token(line, col, T_CURLYCLOSE))
            
            # regular bracket validation
            elif self.current_char == "(":
                tokens.append(Token(line, col, T_BOPEN))
            elif self.current_char == ")":
                tokens.append(Token(line, col, T_BCLOSE))


            # number validation
            elif self.current_char in "0123456789":
                num = ""
                decimal_count = 0 
                while str(self.current_char) in ".0123456789":
                    if str(self.current_char) in ".":
                        if decimal_count == 1:
                            return None
                        decimal_count += 1
                    num += self.current_char
                    self.next()
                tokens.append(Token(line, col, T_NUMBER, float(num)))
                continue           

            # assign operator validation
            elif self.current_char == "=":
                tokens.append(Token(line, col, T_ASSIGN))

            # EOL validation
            elif self.current_char == ";":
                tokens.append(Token(line, col, T_EOL))
            
            # variable addressing
            elif self.current_char == "$":
                tokens.append(Token(line, col, T_VAR))

            # string literal validation
            elif self.current_char == '"':
                identifier = '"'
                self.next()
                while str(self.current_char) != '"':  
                    identifier += self.current_char
                    self.next()
                    if self.current_char == " ":
                        self.current_char = "&nbsp"
                    elif self.current_char == "'":
                        self.current_char = "\\\'"
                    elif self.current_char == "\\":
                        self.current_char = "\\"
                identifier += '"'
                self.next()
                if identifier.startswith('"') and identifier.endswith('"'):
                    tokens.append(Token(line, col, T_LITERAL, identifier))
                else:
                    return Error(filename, line, col, "String Literal Not terminated".err_type, self.message)
                continue 

            # concatenate validation
            elif self.current_char == ".":
                tokens.append(Token(line, col, T_CONCATE))
           
            # whitespace addressing
            elif self.current_char == " ":
                pass

            self.next()
        return tokens


def main():
    tokens = Lexer(data).make_tokens()
    
    for i in range(0, len(tokens)):
        print(tokens[i])

main()

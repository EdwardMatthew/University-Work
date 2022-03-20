import re

tokens = []

source_code = 'int result'.split()
test1 = 'int result = 100;'.split()
test2 = 'int result = 100; a = a + 8;'.split()
test3 = 'int result = 100; a = a + 8;'.split()
test4 = 'int result = 100; a = a + 8; b = b + result;'.split()
test5 = 'b = b + result;'.split()
testcase = 'result;'

# loop through the source code
for word in testcase:

    # datatype validation
    if word in ['str', 'int', 'bool', 'float', 'double']:
        tokens.append(['DATATYPE', word])

    # identifier validation
    elif re.match('[a-z]', word) or re.match('[A-Z]', word):
        tokens.append(['IDENTIFIER', word])

    # operator validation
    elif word in ['=', '!', '+']:
        tokens.append(['OPERATOR', word])

    # integer validation
    elif re.match('[0-9]', word):
        tokens.append(['INTEGER', word])

    # end of statement validation
    elif re.match(';$', word):
        tokens.append(['END_STATEMENT', word])

# output
print(tokens)

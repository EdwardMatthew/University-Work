ast = { 'VariableDeclaration': [] }

tokens = [ ['DATATYPE', 'int'], ['IDENTIFIER', 'result'], ['OPERATOR', '='],  
           ['INTEGER', '100'], ['END_STATEMENT', ';'] ]

# loop for each token
for x in range(0, len(tokens)):

    token_type = tokens[x][0]
    token_value = tokens[x][1]

    # check for EOF
    if token_type == "END_STATEMENT": break

    # check token_type
    if token_type == "DATATYPE":
        ast["VariableDeclaration"].append({"type":token_value})
    if token_type == "IDENTIFIER":
        ast["VariableDeclaration"].append({"type":token_value})
    if token_type == "OPERATOR":
        pass
    if token_type == "INTEGER":
        ast["VariableDeclaration"].append({"type":token_value})
    if token_type == "END_STATEMENT":
        ast["VariableDeclaration"].append({"type":token_value})
        
print(ast)

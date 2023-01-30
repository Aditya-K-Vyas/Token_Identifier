import re

# open the file in read mode
file = open("input.txt", "r")
# read the contents of the file
data = file.read()

keywordList = ['break', 'case', 'char', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'if', 'int', 'long',
               'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
               'unsigned', 'void', 'volatile', 'while', 'include', "namespace"]

operatorList = ['+', '-', '*', '/', '%', '++', '--', '+=', '-=', '*=', '/=', '%=', '==', '!=', '>', '<', '>=', '<=',
                '&&', '||', '!', '&', '|', '^', '~', '<<', '>>', '>>=', '<<=', '&=', '^=', '|=']

specialSymbolList = ['(', ')', '{', '}', '[', ']', ';', ',', '.', '?', '/', '\\', '\'', '\"', '`', '~', '!', '@', '#',
                     '$', '%', '^', '&', '*', '_', '-', '+', '=', '|', '\\', ':', ';', '"', '<', '>', '?']

# regex for identifiers
identifierRegex = r'[a-zA-Z_][a-zA-Z0-9_]*'
# regex for numbers
numberRegex = r'[-+]?[0-9]*\.?[0-9]+'
myLiterals = []

# token generation from the data
myIdentifiers = re.findall(identifierRegex, data)

# print(myIdentifiers)
myNumbers = re.findall(numberRegex, data)

# get all the string literals

myOperators = []
mySpecialSymbols = []
myKeywords = []
for i in data:
    if i in operatorList:
        myOperators.append(i)
    elif i in specialSymbolList:
        mySpecialSymbols.append(i)

for i in myIdentifiers:
    if i in keywordList:
        myKeywords.append(i)
        myIdentifiers.remove(i)

literalsRegex = r'\"[^"]*\"'
myLiterals = re.findall(literalsRegex, data)

# identify string literals
# close the file
file.close()
print("Keywords: ", myKeywords)
print("Identifiers: ", myIdentifiers)
print("Numbers: ", myNumbers)
print("Operators: ", myOperators)
print("Special Symbols: ", mySpecialSymbols)
print("Literals: ", myLiterals)

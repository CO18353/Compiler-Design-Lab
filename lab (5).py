# WAP for a simple lexical analyzer
def buff(buffer):
    if buffer in list_keywords:
        kw.append(buffer)
    elif buffer.isnumeric():
        co.append(buffer)
    elif buffer.isalnum() or buffer.isalpha():
        ie.append(buffer)
    return ''

program_code = ''
op = int(input("Enter 1. To read program form a text file\nEnter 2. To enter the program through terminal\n"))
if(op == 1):
    filename = input("Enter the name of the file: ")
    with open(filename, "r") as f:
        program_code = f.read()
else:
    print("Enter the program, enter 'exitcode' to quit:\n")
    while(True):
        program_line = input()
        if(program_line == "exitcode"):
            break
        program_code += program_line+' '

buffer=''
list_keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "main","printf", "register", "return", "scanf", "short", "signed", "sizeof", "static", "struct",	"switch",	"typedef",	"union", "unsigned", "void", "volatile", "while"]
list_delimitters = ["(", ")", "{", "}", "[", "]", "<", ">","'", '"', ",",";"]
list_operators = ["+", "-", "*", "/", "%", "=", ".", "^"]
kw = list()
op = list()
ie = list()
dl = list()
co = list()
ch=0
while ch < len(program_code):
    if program_code[ch] in list_delimitters:
        dl.append(program_code[ch])
        if program_code[ch]=='"':
            ch+=1
            while(program_code[ch]!='"'):
                buffer += program_code[ch]
                ch+=1
            ch+=1
            co.append(buffer)
            buffer=''
        elif program_code[ch]=="'":
            ch+=1
            co.append(program_code[ch])
            ch+=1
        else:
            buffer = buff(buffer)

    elif program_code[ch] in list_operators:
        op.append(program_code[ch])
        buffer = buff(buffer)

    elif program_code[ch] == " " or program_code[ch] == "\t":
        buffer = buff(buffer)

    else:
        buffer+=program_code[ch]
    ch+=1    
if buffer!='':
    buffer = buff(buffer)
print("Identifiers present are: ", ie)
print("Keywords present are: ", kw)
print("Constants present are: ", co)
print("Delimiters present are: ", dl)
print("Operators present are: ", op)
print("Total tokens are: ", len(ie)+len(kw)+len(co)+len(dl)+len(op))
# int main()
# {
#   int a, b;
#   a = 10;
#  return 0;
# }
# exitcode

# int main()
# {
#   int a = 10, b = 20;
#   printf("sum is :%d",a+b);
#   return 0;
# }
# exitcode

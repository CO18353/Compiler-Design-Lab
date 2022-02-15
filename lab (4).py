# WAP to identify whether the given line is a comment and type of comment and the length and the number of comments.
def findComment(program_code):
    t=0 #Stores length of mlc
    flag=0 #For mlc
    lineNumber=0
    mlc=list()
    slc=list()
    program_code=program_code.split('\n')
    for line in program_code:
        lineNumber+=1
        if(flag==0):
            m=line.find("/*")
            s=line.find("//")
            if(m==-1):
                m=1000000000
            if(s==-1):
                s=1000000000
            if(m<s):
                m2=line.find("*/")
                if(m2!=-1):
                    mlc.append([lineNumber, lineNumber, len(line)-m-4])
                else:
                    flag=1
                    t+=len(line)-m-2
                    mlc.append([lineNumber])
            elif(s<m):
                slc.append([lineNumber,len(line)-s-2])
        else:
            m=line.find("*/")
            if(m!=-1):
                mlc[-1].append(lineNumber)
                mlc[-1].append(t+m)
                flag=0
                t=0
            else:
                t+=len(line)
    return {"mlc":mlc,"slc":slc}

program_code=''
op=int(input("Enter 1. To read program form a text file\nEnter 2. To enter the program through terminal\n"))
if(op==1):
    filename=input("Enter the name of the file: ")
    with open(filename,"r") as f:
        program_code=f.read()
else:
    print("Enter the program, enter 'exitcode' to quit:\n")
    while(True):
        program_line=input()
        if(program_line=="exitcode"):
            break
        program_code+=program_line+'\n'
ans=findComment(program_code)
print("Total Comments: ", len(ans["slc"])+len(ans["mlc"]))
print("Total Single Line Comments: ",len(ans["slc"]))
print("Total Multi Line Comments: ",len(ans["mlc"]))
print("Details about the single line comments present in the program are:")
for x in ans["slc"]:
    print("Line number "+str(x[0])+" contains a single line comment having "+str(x[1])+" characters.")
print("Details about the multiple line comments present in the program are:")
for x in ans["mlc"]:
    print("Line number "+str(x[0])+" to "+str(x[1])+" is a multi line comment having "+str(x[2])+" characters.")

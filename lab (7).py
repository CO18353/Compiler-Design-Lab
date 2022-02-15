stack="$"
stack_str=""
ip=""
grammar=["E->E*E","E->E+E","E->(E)","E->x"]
nop=len(grammar)
flag=0

print("The grammar is: ")
for pr in grammar:
    print(pr)

ip=input("Enter the string: ")
ip+="$"

stack=ip[0]+stack

i=1
top=1

print('{:>10}'.format("Stack"),end="")
print('{:>10}'.format("Input Buffer"), end="")
print('{:>10}'.format("Action"))

print('{:>10}'.format("$"), end="")
print('{:>10}'.format(ip), end="")
print('{:>10}'.format("Shift"))

while(ip[i]!="$" or stack!="E$"):
    #print("Stack: "+stack+" | Input Buffer: "+ip[i:])
    print('{:>10}'.format(stack), end="")
    print('{:>10}'.format(ip[i:]), end="")
    for k in range(top):
        stack_str=stack[:top-k]
        #print("Top of stack: "+stack_str)
        for j in range(nop):
            rhs=grammar[j][3:]
            # print("Rule "+str(j)+": "+rhs)
            if(stack_str[::-1] == rhs):
                #print("Match Found! ",end="")
                l=len(stack_str)
                stack=stack[l:]
                top=top-l
                # print("Stack after popping: ",stack)
                stack = grammar[j][0]+stack
                top+=1
                #print("Stack after reduce: ",stack)
                flag = 1
                print('{:>10}'.format("Reduce"))
                break
    if(flag==0):
        if(ip[i]!="$"):
            stack=ip[i]+stack
            top+=1
            #print("Stack after shift: ",stack)
            print('{:>10}'.format("Shift"))
            i+=1
        else:
            break
    flag=0

if(stack == "E$" and ip[i] == "$"):
    print('{:>10}'.format("E$"), end="")
    print('{:>10}'.format("$"), end="")
    print('{:>10}'.format("-"))
    print("Success!")
else:
    print("Invalid")
import json

production_rules=dict()
nonterminals=list()
terminals=list()
start='S'
temp=list()
ch=int(input("Enter 1. To read the CFG from JSON file\nEnter 2.To read from terminal\n"))
if(ch==2):
    file_name=input("Enter the filename: ")
    with open(file_name, 'r') as data:
        cfg = json.load(data)
        production_rules = cfg["production_rules"]
        nonterminals = cfg["nonterminals"]
        terminals = cfg["terminals"]
        start = cfg["start"]
else:
    terminals=input("Enter the terminal symbols: ").split(" ")
    nonterminals=input("Enter the nonterminal symbols: ").split(" ")
    start=input("Enter the start symbol: ")
    n=int(input("Enter the number of production rules: "))
    print("Enter the production rules:\n")
    for _ in range(n):
        pr=input().split(" ")
        production_rules[pr[0]]=pr[1]

print("The production rules entered are:\n")
for nt,pr in production_rules.items():
    print(nt+"->"+pr)

s = input("Enter the string to process: ")
l=len(s)
i=0
j=start
while(True):
    
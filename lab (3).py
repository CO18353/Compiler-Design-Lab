import json

class NFA:
    current_state=None
    def __init__(self,file_name):
        with open(file_name,'r') as data:
            dfa=json.load(data)
            self.states=dfa["states"]
            self.alphabets=dfa["alphabets"]
            self.initial=dfa["initial"]
            self.final=dfa["final"]
            self.transition=dfa["transition"]

if __name__=="__main__":
    nfa = NFA("nfa.json")

    null_transitions=dict()
    for s in nfa.states:
        null_transitions[s]={s}

    temp=[]
    
    for s in null_transitions:
        temp.append(s)
        while(len(temp)!=0):
            t=temp[0]
            for ns in nfa.transition[t]["^"]:
                null_transitions[s].add(ns)
                temp.append(ns)
            temp.pop(0)
    
    new_alphabets=[x for x in nfa.alphabets if x!="^"]

    temp=[{nfa.initial}]
    new_initial = frozenset({nfa.initial})
    new_states = {new_initial}
    new_transition=dict()
    while(len(temp)!=0):
        new_transition[frozenset(temp[0])]={}
        for a in new_alphabets:
            new_state = set()
            for d in temp[0]:
                for s in null_transitions[d]:
                    for b in nfa.transition[s][a]:
                        new_state.add(b)
                    new_substate=new_state
                    for c in new_substate:
                        for b in null_transitions[c]:
                            new_state.add(b)
            
            new_states.add(frozenset(new_state))
            new_transition[frozenset(temp[0])][a]=frozenset(new_state)
            if new_state not in temp:
                temp.append(new_state)
        temp.pop(0)
    
    new_final=[]
    for i in new_transition.keys():
        for j in nfa.final:
            if j in i:
                new_final.append(i)
    
    change_name=dict()
    count=0
    for i in new_states:
        change_name[i]="q"+str(count)
        count+=1
        
    changed_transitions=dict()
    for i in new_transition.keys():
        changed_transitions[change_name[i]]=dict()
        for j in new_transition[i].keys():
            changed_transitions[change_name[i]][j]=change_name[new_transition[i][j]]

    change_initial=change_name[new_initial]

    change_final=[]
    for i in new_final:
        change_final.append(change_name[i])

    print("\nState Transition table is:\n")
    print('{:>10}'.format("|"), end="")
    for j in new_alphabets:
        print('{:>10}'.format(j+" "+"|"), end="")
    print("\n----------------------------------")
    l = len(changed_transitions)
    for i in changed_transitions:
        if i in change_initial:
            print('{:>10}'.format("->"+str(i)+" |"), end="")
        elif i in change_final:
            print('{:>10}'.format("*"+str(i)+" |"), end="")
        else:
            print('{:>10}'.format(str(i)+" |"), end="")
        for j in changed_transitions[i]:
            print('{:>10}'.format(changed_transitions[i][j]+" "+"|"), end="")
        print()

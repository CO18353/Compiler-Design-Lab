import json

class DFA:
    current_state=None
    def __init__(self,file_name):
        with open(file_name,'r') as data:
            dfa=json.load(data)
            self.states=dfa["states"]
            self.alphabets=dfa["alphabets"]
            self.initial=dfa["initial"]
            self.final=dfa["final"]
            self.transition=dfa["transition"]
    
    def check_dfa(self):
        if(self.initial not in self.states):
            return False
        for state in self.final:
            if(state not in self.states):
                return False
        for alph in self.alphabets:
            if(alph not in self.transition):
                return False
            if(len(self.transition[alph])!=len(self.states)):
                return False
        return True

    def process_string(self,s):
        self.current_state=self.initial
        print("𝛿("+str(self.current_state)+",^)="+str(self.current_state))
        if(len(s)==0):
            if(self.current_state in self.final):
                return True
        else:
            for a in s:
                print("𝛿("+str(self.current_state)+","+a+")=", end='')
                self.current_state = self.transition[a][self.current_state]
                print(self.current_state)
            if(self.current_state in self.final):
                return True
            else:
                return False

if __name__=="__main__":
    ques = DFA("ending_with_aa.json")
    if(ques.check_dfa()==True):
        s=input("Enter the string to be processed: ")
        if(ques.process_string(s)==True):
            print("The string is accepted by the DFA!")
        else:
            print("The string is not accepted.")
    else:
        print("There is some error in your DFA.")

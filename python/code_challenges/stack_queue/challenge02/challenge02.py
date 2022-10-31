# Write here the code challenge solution
def brackets(string_bracket):#string_bracket="(){}[]"
    stack=[]
    open_braket=["(","[","{"]
    close_bracket=[")","]","}"]
    pair = {')' : '(' , ']' : '[' , '}' : '{'}
    for i in string_bracket:
        if i in open_braket: 
            stack.append(i)
        elif i in close_bracket:
        
            if stack.pop() != pair[i] :
                return False
            else :
                continue
        else :
            continue
    if stack ==[]:
        return True

if __name__=="__main__":
    seq="{([)]}"
    print(brackets(seq))


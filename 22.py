def checkbrackets(brackets):
    check = 0;
    if brackets == '[':
        check +=1;
    elif brackets == ']':
        check-=1;
    if check==0:
        return True;
    else :
        return False;
brackets='[[]]';
print(checkbrackets(brackets));

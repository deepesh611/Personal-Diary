
# IMPORTING LIBRARIES
import pickle
import time
import emoji
import pwinput
# import os



f = open('sign.dat','rb')
sign = pickle.load(f)
f.close()



# CHECKING AUTHENTICATION TO ACCESS THE FILE
def check():
    f = open('pwd.dat','rb')
    data = pickle.load(f)
    p = pwinput.pwinput(prompt ="Enter your password:\n", mask="*")
    print()
    if p == data:
        print('WELCOME !\n')
        time.sleep(1)
    else:
        print('INVALID PASSWORD !') 
        print('   ',(emoji.emojize(":pensive_face:"))*3)
        time.sleep(5)
        quit()



# FUNCTION TO CHANGE PASSWORD
def cng_pwd():
    o = pwinput.pwinput(prompt ="ENTER PREVIOUSLY SET PASSWORD :\n", mask="*")
    print()
    f = open('pwd.dat','rb')
    data = pickle.load(f)
    f.close()
    if o == data:
        f = open('pwd.dat','wb')
        p = pwinput.pwinput(prompt ="ENTER THE NEW PASSWORD :\n", mask="*")
        print()
        pickle.dump(p,f)
        print('Password was Successfully Changed.')
        print()
        f.close()
    else:
        print('INVALID PASSWORD !')
        print('   ',(emoji.emojize(":pensive_face:"))*3,'\n')
        pass
    time.sleep(1)



# FUNCTION TO TAKE MULTIPLE LINE INPUTS
def mlinput():
    lines = []
    
    print('Enter Today\'s Log :\n')
    while True:
        uin = input()
        if uin == '':
            break
        else:
            lines.append(uin+'\n')
        
    data = ''.join(lines)
    return data
    


# FUNCTION TO ADD A DAYS RECORD
def add_log():
    txt1 = time.ctime()
    new_str = txt1.center(50, ' ')
    print(new_str)
    data = '\n' + new_str + '\n\n' + mlinput() + '\n' + '\t'*13+'- '+ sign + '\n\n'
    f = open('data.dat','ab')
    pickle.dump(data,f)
    f.close()
    print('Log Updated.\n  \U0001f44d\U0001f44d\U0001f44d')
    time.sleep(1)
    
    

# FUNCTION TO DISPLAY ALL LOGS STORED IN THE DIARY
def display():
    try:
        with open('data.dat', 'rb') as f:
            data = pickle.load(f)
            print(data)
            f.close()
    except EOFError:
        print('The Diary is Empty.\n')

    time.sleep(1)
    input('Press Enter to Continue.')



# FUNCTION TO CLEAR THE DIARY
def clear():
    f = open('data.dat','wb')
    pickle.dump('',f)
    f.close()



# FUNCTION TO EXIT THE APPLICATION
def Exit():
    # A simple gesture of courtesy towards the user to enhance user experience
    print("*"*100)
    print("**                              YOUR LOGS WERE SUCCESSFULLY STORED                                **")
    print("*"*100,"\n")
    time.sleep(3)
    quit()



# CREATING A MENU
def menu():
        txt1 = 'MENU'
        print( txt1.center(50,'~'))
        print()
        print(' 1 : ADD A RECORD')
        print(' 2 : DISPLAY ALL RECORDS')
        print(' 3 : CLEAR THE DIARY')
        print(' 4 : TO CHANGE THE PASSWORD')
        print(' 5 : EXIT')
        print()
        chc=int(input("ENTER YOUR CHOICE (1-9):\n"))
        print()
        if chc==1:
            add_log()
        elif chc==2:
            display()
        elif chc==3:
            clear()
        elif chc==4:
            cng_pwd()
        elif chc==5:
            Exit()
        else:
            print("You have Given a Wrong Input.\n")
            time.sleep(1)
        print()



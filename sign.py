
# A FILE TO ADD A SIGNATURE

import pickle


def sign():
    sign = input('Enter Signature : \n')
    f = open('sign.dat','wb')
    pickle.dump(sign,f)
    f.close()
    print('\nSign Saved\n \U0001f44d\U0001f44d\U0001f44d')
    
sign()
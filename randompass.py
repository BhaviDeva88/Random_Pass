import random 
import array 
pass_len = 8
Number_Of_Pwd=5
DIG= [str(x) for x in range(0,10)]
print(DIG)
LOW_CASE = [chr(x) for x in range(ord('a'), ord('z') + 1)] 
UPPER=[chr(y) for y in range(ord('A'), ord('Z') + 1)] 
print(UPPER)
SPECIAL = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  '*', '(', ')'] 
consolidated_pwd = DIG + UPPER + LOW_CASE + SPECIAL 
print(consolidated_pwd)

for i in range(Number_Of_Pwd):
    # randomly select at least one character from each character set above 
    rdig = random.choice(DIG) 
    rupper = random.choice(UPPER) 
    rlowcase = random.choice(LOW_CASE) 
    rspecial = random.choice(SPECIAL) 
    
    temp_pass = rdig+rupper+rlowcase+rspecial
   
    for x in range(pass_len-4): 
        temp_pass = temp_pass + random.choice(consolidated_pwd) 
        # convert temporary password into array and shuffle to  
        # prevent it from having a consistent pattern 
        # where the beginning of the password is predictable 
        temp_pass_list = array.array('u',temp_pass) 
        random.shuffle(temp_pass_list) 

    password = "" 
    for x in temp_pass_list: 
            password = password + x 

    # print out password 

    print(password) 



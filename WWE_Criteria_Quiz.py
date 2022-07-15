import math
def game():
    criteriaList= ["Former WWE Champion", "Former Tag Team Champion", "Former World Heavyweight Champion", "Former Royal Rumble Winner", "Money in the Bank Winner", "King of the Ring Winner", "Former Intercontinental Champion"]
    superstarList_random= ["John Cena", "The Undertaker", "Edge", "Big Show", "AJ Styles", "Randy Savage", "Sheamus"]
    superstarList_key= ["Randy Savage", "AJ Styles", "Big Show", "The Undertaker", "John Cena", "Sheamus", "Edge"]
    Lost= False
    correctCount=0
    while len(superstarList_key)>0 and Lost==False:
        print(' ')
        print('Criteria:')
        for criteria in criteriaList:
            print("\n"+criteria)
        print(' ')
        print('Superstars:')
        for superstar in superstarList_random:
            print("\n"+superstar)
        user_guess= input("\n Type the superstar who matches all the above criteria: ")
        if user_guess in superstarList_key:
            if user_guess==superstarList_key[len(superstarList_key)-1]:
                correctCount+=1
                superstarList_random.remove(user_guess)
                superstarList_key.pop()
                criteriaList.pop()
            else:
                Lost=True
        else:
            print("Invalid input")
    print("You scored "+str(correctCount)+" out of 7!")
game()


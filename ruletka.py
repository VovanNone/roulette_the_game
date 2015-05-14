

import random, sys, time

symbols = ["$", "&", "@", "€", "£"]
stop = False
sample = []
cash = 1000
bet = 0
        ####### functions ######
def bet_check():
    global cash
    global bet
    global sample
    try:
        if int(bet) > cash:
            print("ва-банк?!")
            bet = cash
    except:
        if bet == "vovan":
            sample = ["@", "@", "@"]
            bet = cash
        else:
            print("ты ввёл who_knew_что. Ставка номинальная =1\n")
            bet = 1
        ##########
def user_comb():
    global sample
    if sample == []:
        k = 0
        while k < 3:
            k = k + 1
            j = random.choice(symbols)
            time.sleep(1)
            sys.stdout.write(j+" ")
            sys.stdout.flush()
            sample.append(j)
    else:
        pass
        
        ##########

def lucky_check():
    global sample
    global cash
    global bet
    h = 0
    if str(sample[0]) == str(sample[2]) == str(sample[1]) :
        print("\n win")
        cash = cash + int(bet)*6
        
    elif str(sample[0]) == str(sample[2]):
        print("\n half win")
        cash = cash + int(bet)*3
        
    elif str(sample[0]) == str(sample[1]) or str(sample[1]) == str(sample[2]):
        print("\n quarter win")
        cash = cash + int(bet)*2
        
    else:
        print("\n ты pro_a_ball")
        cash = cash - int(bet)
        
    
      ####### prog body ########
      
print("готов проиграть " + str(cash) + " ₽?")
while stop == False and cash > 0:
    answer = input("проверим пруху? <any key - да, n - нет> \n")
    if answer == "n":
        print("слабак!")
        print("таки унёс из казино " + str(cash) + " ₽")
        stop = True
    else:
        sample = []
        bet = input("твоя ставка ")
        bet_check()
        if sample == []:
            user_comb()
        else:
            print(sample)
        lucky_check()
        print("на кармане " + str(cash) + " ₽")
        if cash <= 0:
            print("какая жаль...ты проигрался в ноль")
        
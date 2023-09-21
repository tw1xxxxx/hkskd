import random   
NumberToGuess=random.randint(1,20)   
a=-1        
while a!=NumberToGuess:      
    a=int(input("Угадай число от 1 до 20 "))      
    if a > NumberToGuess:        
        print("Число должно быть меньше")      
    elif a < NumberToGuess:         
        print("Число должно быть больше")      
    else:         
        print("Вы угадали, это число = " + str(NumberToGuess))                    
        break
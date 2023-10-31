slovo1 = input(f'Введите слово на латинице  /n ')
slovo1_len = len(slovo1.strip())
idx = slovo1_len // 2

if slovo1_len % 2 == 0:
    print(slovo1[idx - 1:idx + 1] ) 
else:
    print(slovo1[idx])  
        
    
    
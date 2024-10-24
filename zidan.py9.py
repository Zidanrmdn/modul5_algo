# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:05:48 2024

@author: ASUS
"""

n = 0
money = 0
people = 0

while (n != ''):
    n = str(input("Masukkan umur : "))
    people += 1
    if (n == str('')):
        break;
    else:
        
        if (int(n) <= 2):
            print('Gratis')
            money += 0
            print("total payment : ", money)
        elif (3 <= int(n) <= 12):
            print("Harga $14.00")
            money += 14.00
            print("total payment : ", money)
        elif (150 >= int(n) >= 65):
            print('Harga $18.00')
            money += 18.00
            print("total payment : ", money)
        elif (13 <= int(n) <= 64):
            print('Harga $23.00')
            money += 23.00
            print("total payment : ", money)
        else:
            people -= 1
            print('INVALID')
            
if(people == 1):
    print(" ")
else:
    pay = float(input("Masukkan jumlah uang : "))
    chance = pay - money
    print('Running Kembalian : ', chance)
    
    
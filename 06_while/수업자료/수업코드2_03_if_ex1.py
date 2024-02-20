'''
letter=input("알파벳 한 글자를 입력하세요:")
if letter == "A":
    print("10진수 ==> 10")
elif letter == "B":
    print("10진수 ==> 11")
elif letter == "C":
    print("10진수 ==> 12")
elif letter is "D":
    print("10진수 ==> 13")
elif letter is "E":
    print("10진수 ==> 14")
elif letter is "F":
    print("10진수 ==> 15")
else:
    print("16진수가 아닙니다.")

hex = ['a', 'b' ,'c' ,'d', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

word = input('16진수 한 글자 입력 : ')
if word in hex: 
    print('10진수 ==>', int(word, 16))
elif len(word) >= 2:
    print('입력 가능한 글자 수를 초과하였습니다.')
else :
    print('16진수가 아닙니다.')


hnum_str=input('16진수 한글자 입력 :')
if len(hnum_str) == 1:
    if "A" <= hnum_str <= "F" or "a" <= hnum_str <= "f":
        hnum = int(hnum_str, 16)
        print('10진수 ==> ', hnum)
    else:
        print('입력하신 ',hnum_str,'은 16진수 글자가 아닙니다')

else:
    print('한글자를 초과하여 입력하셨습니다')
'''

num = input('16진수 한글자 입력 :')
if ('0' <= num <= '9') or ('a' <= num <= 'f') or ('A' <= num <= 'F'):
    print('10진수 ==>', int(num, 16))
else:
    print('16진수가 아닙니다')









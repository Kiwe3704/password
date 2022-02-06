#輸入密碼程式
# 
# #    password = input('請輸入密碼: ')
#    if password != 'a1234567':
#        print('密碼錯誤還有兩次機會')
#    elif password != 'a1234567':
#        print('密碼錯誤還有一次機會')
#    elif password == 'a1234567':
#        print('登入成功')
#        break

password = 'a1234567'
i = 3 #剩餘機會
while i > 0:
    pwd = input("請輸入密碼: ")
    if pwd == password:
        print('登入成功')
        break #逃出迴圈
    else:
        i = i - 1
        print('密碼錯誤! 還有', i, '次機會')
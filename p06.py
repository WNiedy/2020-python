#input();;
a=input("請輸入性別(M/F):")
'''

#1
if a == "M":
    print("男")
#2
if a == "M" or a== "m":
    print("男")
#3
if a in ["M" , "m"]:
    print("男")
else:
    print("女")
'''
#if elif
if a in ["M" , "m"]:
    print("男")
elif a in ["F" , "f"]:
    print("女")
else:
    print("輸入錯誤")
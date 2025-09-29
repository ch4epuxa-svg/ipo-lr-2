ss_8 = input ("Enter the number in octal ")
for i in ss_8:
    if int(i) >= 8 :
        print("The number contains invalid characters.The selected number system only accepts the following characters: 01234567")
        exit()
if len(ss_8) == 5:
    ss_10 = (int(ss_8[0]) * 8**4) + (int(ss_8[1]) * 8**3) + (int(ss_8[2]) * 8**2) + (int(ss_8[3]) * 8**1) + (int(ss_8[4]) * 8**0)
    print("ss_8 -> ss_10 : ",ss_10)
else:
    print("the number must be five digits")

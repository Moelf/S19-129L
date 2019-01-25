for i in range(100,401):
    digits = str(i)
    if int(digits[0])%2==0 and int(digits[1])%2==0 and int(digits[2])%2==0:
        print(i)

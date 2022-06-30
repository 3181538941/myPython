s = input("")
list = [i for i in range(1, 26)]
for i in list:
    print()
    for per in s:
        if "A" <= per <= "Z":
            temp = (ord(per) - ord("A") + i) % 26
            te2 = ord("A") + temp
            print(chr(te2), end='')
        elif "a" <= per <= "z":
            temp = (ord(per) - ord("a") + i) % 26
            te2 = ord('a') + temp
            print(chr(te2), end='')
        else:
            print(per, end='')
    print()

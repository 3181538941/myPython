s = input("input which code that should be translated: ")
for i in range(26):
    print("please 检查 : ")
    a = []
    for j in s:
        if 'A' <= j <= 'Z':
            # if "A" <= j <= "Z":
            temp = chr((ord(j) - ord("A") + i) % 26 + ord('A'))
            a.append(temp)
        # elif "a" <= j <= "z":
        elif 'a' <= j <= 'z':
            temp = chr((ord(j) - ord("a") + i) % 26 + ord('a'))
            a.append(temp)
        else:
            a.append(j)
    b = ''.join(a)
    print(b)

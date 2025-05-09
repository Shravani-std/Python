word = str(input("Enter a word: "))

def reverse(a):
    a = list(a) 
    s = 0
    e = len(a) - 1

    while s < e:
        a[s], a[e] = a[e], a[s]
        s += 1
        e -= 1

    return ''.join(a)

print("Your name is:", reverse(word))

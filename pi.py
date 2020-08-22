digits = list(map(int, open("pi.txt", "r").read().split(",")))

print("table of accurate approximations")
print("digit\tindex\tscore")
max = [(0, 0)]
for index, digit in enumerate(digits):
    score = digit / (index + 1)
    if digit >= max[-1][1]:
        print(digit, index, score, sep="\t")
        max.append((index, digit))

def cr(l, iter):
    num_tape = [1, l[0]]
    den_tape = [0, 1]
    for digit in l[1:iter]:
        num_tape.append(digit * num_tape[-1] + num_tape[-2])
        den_tape.append(digit * den_tape[-1] + den_tape[-2])
        num_tape.pop(0)
        den_tape.pop(0)        
        print("\r", (index + 2) / iter * 100, "%", " " * 16, end="")    
    print(f"\n\napprox: {num_tape[-1]} / {den_tape[-1]}")
    
print()
cr(digits, int(input("index: ")))



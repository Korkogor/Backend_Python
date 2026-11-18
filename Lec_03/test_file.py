number = '+79150123909'
N = 4
Z = 2

start = number[:N]
end = number[-Z:]
stealth = (len(number[N:-Z]) * '*')
print(start + stealth +end)

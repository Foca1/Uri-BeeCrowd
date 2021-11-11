soma = 1
b = 2

for i in range(3,40,2):
    soma+=i/b
    b*=2
print(f"{soma:.2f}")
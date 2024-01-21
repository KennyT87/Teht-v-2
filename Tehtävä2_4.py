luku1 = int(input("Anna 1. kokonaisluku: "))
luku2 = int(input("Anna 2. kokonaisluku: "))
luku3 = int(input("Anna 3. kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
avg = float((luku1 + luku2 + luku3)/3)

print(f"Lukujen summa on {summa}, niiden tulo on {tulo} ja keskiarvo on {avg:.2f}")
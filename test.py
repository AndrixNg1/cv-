def premier(n):
    if n <= 1:
        return False
    for x in range(2, int(n ** 0.5) + 1):  # Vérifier jusqu'à la racine carrée de n
        if n % x == 0:
            return False  # Si un diviseur est trouvé, n n'est pas premier
    return True  # Si on sort de la boucle, n est premier

# Test
n = int(input("Entrez un nombre : "))
if premier(n):
    print(f"{n} est un nombre premier.")
else:
    print(f"{n} n'est pas un nombre premier.")
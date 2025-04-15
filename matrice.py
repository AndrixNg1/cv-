import numpy as np

# Définition des matrices
A = np.array([[2, 3], [1, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition
somme = A + B

# Multiplication
produit = np.dot(A, B)

# Déterminant
det_A = np.linalg.det(A)

# Inverse (si déterminant non nul)
if det_A != 0:
    inverse_A = np.linalg.inv(A)
else:
    inverse_A = "Non inversible"

# Affichage des résultats
print("A + B =\n", somme)
print("A × B =\n", produit)
print("Déterminant de A =", det_A)
print("Inverse de A =\n", inverse_A)

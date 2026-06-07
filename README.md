# Transformée de Fourier Discrète (DFT/FFT) en Python pur

Projet éducatif réalisé sans aucune bibliothèque externe (pas de NumPy, pas de SciPy).

Implémentations 1D et 2D avec :
- Version **naïve** (O(N²) en 1D, O(M²N²) en 2D)
- Version **rapide** (FFT Cooley-Tukey radix-2 récursive)
- Transformées **inverses** incluses + normalisation correcte

## Fichiers

- `tfd1D_naif.py` → DFT 1D naïve + inverse
- `tfd1D_rapide.py` → FFT 1D rapide + inverse
- `tfd2D_naif.py` → DFT 2D naïve + inverse
- `tfd2D_rapide.py` → FFT 2D rapide (séparabilité) + inverse

Chaque fichier contient un exemple exécutable.

## Exemple (image 2×2 : [[1, 2], [3, 4]])

Coefficients 2D (naïve et rapide donnent le même résultat) :
[(10+0j), (-2+0j)] [(-4+0j), (0+0j)]

Reconstruction inverse (parties réelles) :
[[1.0, 2.0] [3.0, 4.0]]

## Notes
- Version rapide : taille doit être puissance de 2.
- Code 100% Python standard, idéal pour comprendre la FFT de l’intérieur.

## Utilisation
```bash
python tfd2D_rapide.py

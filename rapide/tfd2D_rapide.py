import cmath 
from tfd1D_rapide import tfd1D_rapide, itfd1D_rapide

def tfd2D_rapide(image):
    lignes_transformees = [tfd1D_rapide(ligne) for ligne in image]
    M = len(lignes_transformees)       
    N = len(lignes_transformees[0])    
    colonnes_transformees = []         
    for j in range(N):  
        colonne = [lignes_transformees[i][j] for i in range(M)]
        colonne_transformee = tfd1D_rapide(colonne)
        for i in range(M):
            if j == 0:
                colonnes_transformees.append([0]*N)  
            colonnes_transformees[i][j] = colonne_transformee[i]

    return colonnes_transformees  

def itfd2D_rapide(coefficients):
    M = len(coefficients)       
    N = len(coefficients[0])    
    colonnes_inverse = []      
    for j in range(N):          
        colonne = [coefficients[i][j] for i in range(M)]  
        colonne_inverse = itfd1D_rapide(colonne)           
        for i in range(M):
            if j == 0:
                colonnes_inverse.append([0]*N)  
            colonnes_inverse[i][j] = colonne_inverse[i]
    image_reconstruite = [itfd1D_rapide(ligne) for ligne in colonnes_inverse]

    return image_reconstruite 


image = [[1, 2], [3, 4]]                   
freq2D = tfd2D_rapide(image)              
reconstruit2D = itfd2D_rapide(freq2D)  
print("\ntfd2D_rapide :")
for ligne in freq2D:
    print(ligne)              
print("\nitfd2D_rapide :")
for ligne in reconstruit2D:
    print([round(x.real,5) for x in ligne])
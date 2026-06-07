import cmath  

def tfd2D_naif(image):
    M = len(image)           
    N = len(image[0])        
    coefficients = []       
    for u in range(M):
        ligne_freq = []      
        for v in range(N):
            s = 0            
            for m in range(M):        
                for n in range(N):    
                    angle = -2j * cmath.pi * ((u*m)/M + (v*n)/N)
                    s += image[m][n] * cmath.exp(angle)
            ligne_freq.append(s)
        coefficients.append(ligne_freq)

    return coefficients


def itfd2D_naif(coefficients):
    M = len(coefficients)    
    N = len(coefficients[0])
    image_reconstruite = [] 
    for m in range(M):
        ligne_image = []
        for n in range(N):
            s = 0              
            for u in range(M):
                for v in range(N):
                    angle = 2j * cmath.pi * ((u*m)/M + (v*n)/N)
                    s += coefficients[u][v] * cmath.exp(angle)
            ligne_image.append(s / (M*N))
        image_reconstruite.append(ligne_image)

    return image_reconstruite  


image = [[1, 2], [3, 4]] 
coefficients2D = tfd2D_naif(image)
print("tfd2D_naif :")
for ligne in coefficients2D:
    print(ligne) 
image_reconstruite = itfd2D_naif(coefficients2D)
print("\nitfd2D_naif :")
for ligne in image_reconstruite:
    print([round(x.real,5) for x in ligne])
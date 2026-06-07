import cmath 

def tfd1D_naif(signal):
    N = len(signal)          
    coefficients = []         
    for k in range(N):
        s = 0                 
        for n in range(N):
            angle = -2j * cmath.pi * k * n / N
            s += signal[n] * cmath.exp(angle)
        coefficients.append(s)

    return coefficients     

def itfd1D_naif(coefficients):
    N = len(coefficients)      
    signal_reconstruit = []    
    for n in range(N):
        s = 0                   
        for k in range(N):
            angle = 2j * cmath.pi * k * n / N
            s += coefficients[k] * cmath.exp(angle)
        signal_reconstruit.append(s / N)

    return signal_reconstruit   


signal_exemple = [1, 2, 3, 4] 
frequences = tfd1D_naif(signal_exemple)
print("tfd1D_naif :", frequences)  
signal_reconstruit = itfd1D_naif(frequences)
print("itfd1D_naif :", [round(x.real, 5) for x in signal_reconstruit])
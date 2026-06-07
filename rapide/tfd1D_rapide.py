import cmath  

def tfd1D_rapide(signal):
    N = len(signal)             
    if N <= 1:
        return signal           

    signal_pairs = tfd1D_rapide(signal[0::2])    
    signal_impairs = tfd1D_rapide(signal[1::2]) 

    coefficients = [0] * N
    for k in range(N // 2):
        facteur = cmath.exp(-2j * cmath.pi * k / N) * signal_impairs[k]
        coefficients[k] = signal_pairs[k] + facteur         
        coefficients[k + N//2] = signal_pairs[k] - facteur  

    return coefficients

def itfd1D_rapide(coefficients):
    N = len(coefficients)
    if N <= 1:
        return coefficients

    coeffs_pairs = itfd1D_rapide(coefficients[0::2])
    coeffs_impairs = itfd1D_rapide(coefficients[1::2])

    signal_reconstruit = [0] * N
    for k in range(N // 2):
        facteur = cmath.exp(2j * cmath.pi * k / N) * coeffs_impairs[k]
        signal_reconstruit[k] = coeffs_pairs[k] + facteur
        signal_reconstruit[k + N // 2] = coeffs_pairs[k] - facteur 

    return [val / 2 for val in signal_reconstruit]


signal_exemple = [1, 2, 3, 4,5,6] 
frequences = tfd1D_rapide(signal_exemple)    
print("tfd1D_rapide :", frequences)
signal_reconstruit = itfd1D_rapide(frequences)  
print("itfd1D_rapide :", [round(x.real, 5) for x in signal_reconstruit])

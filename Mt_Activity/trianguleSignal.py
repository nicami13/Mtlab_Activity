import numpy as np  
import matplotlib.pyplot as plt  
from scipy.signal import sawtooth, square  

# Parámetros  
fs = 5000  # Frecuencia de muestreo  
t = np.arange(0, 1.5, 1/fs)  # Vector de tiempo  

# Generar señales  
x1 = sawtooth(2 * np.pi * 50 * t)  # Onda de diente de sierra  
x2 = square(2 * np.pi * 50 * t)     # Onda cuadrada  

# Crear la figura y los ejes  
fig, axs = plt.subplots(2, 1, figsize=(10, 6))  

# Graficar la onda de diente de sierra  
axs[0].plot(t, x1)  
axs[0].set_xlim(0, 0.2)  
axs[0].set_ylim(-1.2, 1.2)  
axs[0].set_xlabel("Tiempo (seg)")  
axs[0].set_ylabel("Amplitud")  
axs[0].set_title("Onda Periodica De Diente De Sierra")  

# Graficar la onda cuadrada  
axs[1].plot(t, x2)  
axs[1].set_xlim(0, 0.2)  
axs[1].set_ylim(-1.2, 1.2)  
axs[1].set_xlabel("Tiempo (seg)")  
axs[1].set_ylabel("Amplitud")  
axs[1].set_title("Onda Periodica cuadrada")  

# Ajustar el espacio entre los gráficos  
plt.tight_layout()  
plt.show()  
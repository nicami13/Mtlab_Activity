import numpy as np  
import matplotlib.pyplot as plt  

  
fs = 10000  
wiht= 0.02
t = np.arange(-2, 2, 1/fs)  

def tripuls(t, ancho):

    return np.maximum(1 - np.abs(t / (ancho / 2)), 0) * (np.abs(t) <= (ancho / 2)) 

def rectpuls(t, ancho):  

    return np.where(np.abs(t) < (ancho / 2), 1, 0)  

 
x1 = tripuls(t, wiht)  
x2 = rectpuls(t,wiht)   


fig, axs = plt.subplots(2, 1, figsize=(8, 6))  

 
axs[0].plot(t, x1, label='Pulso Triangular', color='royalblue', linewidth=2)  
axs[0].set_xlim(-0.1, 0.1)  
axs[0].set_ylim(-0.2, 1.2)  
axs[0].set_xlabel("Tiempo (seg)", fontsize=12)  
axs[0].set_ylabel("Amplitud", fontsize=12)  
axs[0].set_title("Pulso Triangular", fontsize=14)  
axs[0].grid(True)  
axs[0].legend()  

 
axs[1].plot(t, x2, label='Pulso Rectangular', color='tomato', linewidth=2)  
axs[1].set_xlim(-0.1, 0.1) 
axs[1].set_ylim(-0.2, 1.2)  
axs[1].set_xlabel("Tiempo (seg)", fontsize=12)  
axs[1].set_ylabel("Amplitud", fontsize=12)  
axs[1].set_title("Pulso Rectangular", fontsize=14)  
axs[1].grid(True) 
axs[1].legend()  


plt.tight_layout()  
plt.show()  
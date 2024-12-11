import tkinter as tk
from tkinter import messagebox
import random

def reiniciar_juego():
    global numero_aleatorio, vidas
    numero_aleatorio = random.randint(1, 10)
    vidas = 3
    lbl_vidas.config(text=f"Vidas restantes: {vidas}")
    lbl_mensaje.config(text="Adivina el número entre 1 y 10")
    entrada_numero.delete(0, tk.END)

def verificar_numero():
    global vidas
    adivinanza = entrada_numero.get()

    if adivinanza.upper() == 'RESET':
        reiniciar_juego()
        return

    if adivinanza.upper() == 'QUIT':
        messagebox.showinfo("Juego terminado", f"Te has rendido. El número era {numero_aleatorio}.")
        root.destroy()
        return

    if not adivinanza.isdigit():
        lbl_mensaje.config(text="Por favor, ingresa un número válido.")
        return

    adivinanza = int(adivinanza)

    if adivinanza == numero_aleatorio:
        messagebox.showinfo("¡Felicidades!", "¡Acertaste el número!")
        reiniciar_juego()
    else:
        vidas -= 1
        if vidas > 0:
            if adivinanza < numero_aleatorio:
                lbl_mensaje.config(text="El número que buscas es mayor. Intenta de nuevo.")
            else:
                lbl_mensaje.config(text="El número que buscas es menor. Intenta de nuevo.")
            lbl_vidas.config(text=f"Vidas restantes: {vidas}")
        else:
            messagebox.showerror("Fin del juego", f"Te has quedado sin intentos. El número era {numero_aleatorio}.")
            reiniciar_juego()

# Configuración inicial
root = tk.Tk()
root.title("Adivina el Número")

numero_aleatorio = random.randint(1, 10)
vidas = 3

# Interfaz gráfica
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

lbl_instruccion = tk.Label(frame, text="Adivina el número entre 1 y 10", font=("Arial", 12))
lbl_instruccion.pack()

entrada_numero = tk.Entry(frame, font=("Arial", 12))
entrada_numero.pack(pady=5)

btn_verificar = tk.Button(frame, text="Verificar", font=("Arial", 12), command=verificar_numero)
btn_verificar.pack(pady=5)

btn_reiniciar = tk.Button(frame, text="Reiniciar", font=("Arial", 12), command=reiniciar_juego)
btn_reiniciar.pack(pady=5)

lbl_mensaje = tk.Label(frame, text="", font=("Arial", 12))
lbl_mensaje.pack(pady=5)

lbl_vidas = tk.Label(frame, text=f"Vidas restantes: {vidas}", font=("Arial", 12))
lbl_vidas.pack()

# Iniciar aplicación
root.mainloop()

# sudo apt-get install python3-tk
import tkinter as tk

def accion():
	print("Has pulsado el boton")
	
ventana = tk.Tk()  # METODO ESTATICO

tk.Button(ventana,text="Pulsame si te atreves",command=accion).pack(padx=10,pady=10)

etiqueta = tk.Label(text="¿Has pulsado el boton?")
etiqueta.pack(padx=10,pady=10)

ventana.mainloop()  # NO TE SALGAS


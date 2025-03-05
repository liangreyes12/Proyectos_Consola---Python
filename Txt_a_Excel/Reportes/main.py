import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk  # Interfaz moderna con ttkbootstrap

def procesar_archivos_txt(directorio, archivo_salida):
    columnas = [
        "Cedula", "Codigo", "Telefono", "Nombre", "Identificacion", "Direccion", "Fecha1",
        "Fecha2", "Cargo", "FechaIngreso", "Salario", "Email", "Genero", "FechaNacimiento",
        "EPS", "FondoPensiones", "Valor", "Categoria"
    ]
    
    dataframes = []
    
    archivos_txt = [f for f in os.listdir(directorio) if f.endswith(".txt")]
    
    if not archivos_txt:
        messagebox.showwarning("Advertencia", "No se encontraron archivos .txt en la carpeta seleccionada.")
        return
    
    try:
        for archivo in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo)
            with open(ruta_archivo, "r", encoding="ISO-8859-1") as f:
                lineas = f.readlines()
                datos = [line.strip().split("\t") for line in lineas]
                df = pd.DataFrame(datos, columns=columnas, dtype=str)
                dataframes.append(df)
        
        df_final = pd.concat(dataframes, ignore_index=True)
        df_final.to_excel(archivo_salida, index=False)
        messagebox.showinfo("Proceso Completado", f"Archivo Excel guardado como: {archivo_salida}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al procesar los archivos: {str(e)}")

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        carpeta_var.set(carpeta)

def convertir():
    directorio = carpeta_var.get()
    if not directorio:
        messagebox.showwarning("Error", "Por favor selecciona una carpeta primero.")
        return
    
    archivo_salida = os.path.join(directorio, "datos_completos.xlsx")
    procesar_archivos_txt(directorio, archivo_salida)

# Crear la ventana principal
root = ttk.Window(themename="cosmo")  # Tema moderno
root.title("Convertir TXT a Excel")
root.geometry("420x280")
root.resizable(False, False)

# Variable para mostrar la carpeta seleccionada
carpeta_var = tk.StringVar()

# Contenedor principal
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Etiqueta
ttk.Label(frame, text="Seleccione la carpeta con archivos TXT:", font=("Arial", 12)).pack(pady=10)

# Botón para seleccionar carpeta (centrado y redondeado)
btn_seleccionar = ttk.Button(
    frame, text="Seleccionar Carpeta", command=seleccionar_carpeta,
    bootstyle="primary-outline", padding=10
)
btn_seleccionar.pack(pady=5, fill="x")

# Label para mostrar la ruta seleccionada
ttk.Label(frame, textvariable=carpeta_var, wraplength=350, foreground="blue").pack(pady=5)

# Botón para convertir (centrado y redondeado)
btn_convertir = ttk.Button(
    frame, text="Convertir a Excel", command=convertir,
    bootstyle="success-outline", padding=10
)
btn_convertir.pack(pady=20, fill="x")

# Ejecutar la aplicación
root.mainloop()
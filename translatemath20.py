import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import messagebox

# Función para interpretar y graficar una expresión matemática
def interpretar_y_graficar(expr_str):
    try:
        x = sp.symbols('x')
        expr = sp.sympify(expr_str)
        expr_lambda = sp.lambdify(x, expr, "numpy")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = expr_lambda(x_vals)
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'y = {sp.pretty(expr)}')
        plt.title(f'Graph of y = {expr_str}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Could not interpret the expression: {e}")

# Función para graficar datos estadísticos
def graficar_estadistica(data, chart_type):
    try:
        if chart_type == "Bar Chart":
            plt.bar(data.keys(), data.values())
        elif chart_type == "Line Chart":
            plt.plot(list(data.keys()), list(data.values()))
        elif chart_type == "Pie Chart":
            plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
        plt.title(chart_type)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Could not generate the graph: {e}")

# Ventana para Lenguaje y Notación Matemática
def abrir_ventana_lenguaje():
    ventana_lenguaje = tk.Toplevel(root)
    ventana_lenguaje.title("Mathematical Language and Notation")
    
    label = tk.Label(ventana_lenguaje, text="Enter a mathematical expression:")
    label.pack(pady=10)
    
    entry = tk.Entry(ventana_lenguaje, width=40)
    entry.pack(pady=10)
    
    button = tk.Button(ventana_lenguaje, text="Graph", command=lambda: interpretar_y_graficar(entry.get()))
    button.pack(pady=10)

# Ventana para Estadística y Probabilidad
def abrir_ventana_estadistica():
    ventana_estadistica = tk.Toplevel(root)
    ventana_estadistica.title("Statistics and Probability")
    
    label = tk.Label(ventana_estadistica, text="Enter data (format: key1:value1, key2:value2):")
    label.pack(pady=10)
    
    entry = tk.Entry(ventana_estadistica, width=40)
    entry.pack(pady=10)
    
    chart_type = tk.StringVar(ventana_estadistica)
    chart_type.set("Bar Chart")
    
    option_menu = tk.OptionMenu(ventana_estadistica, chart_type, "Bar Chart", "Line Chart", "Pie Chart")
    option_menu.pack(pady=10)
    
    button = tk.Button(ventana_estadistica, text="Graph", command=lambda: graficar_estadistica(
        dict(item.split(":") for item in entry.get().split(", ")), chart_type.get()))
    button.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Mathematical Language and Statistics Tool")

label = tk.Label(root, text="Choose a section:")
label.pack(pady=20)

button_lenguaje = tk.Button(root, text="Mathematical Language and Notation", command=abrir_ventana_lenguaje)
button_lenguaje.pack(pady=10)

button_estadistica = tk.Button(root, text="Statistics and Probability", command=abrir_ventana_estadistica)
button_estadistica.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()

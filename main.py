import tkinter as tk

ventana = tk.Tk()

ventana.title("Tkinter_Lab")
ventana.geometry("500x500")
WIDTH = 500
HEIGHT = 500
#Función de análisis numérico.
def Analisis_num (num):
    if not isinstance (num, int):
        print("Error, ingrese un número entero.")
        return []
    return Analisis_num_aux(abs(num), 1)
def Analisis_num_aux (num, divisor):
    if divisor * divisor > num:
        return []
    if num % divisor == 0:
        par = (divisor, num // divisor)
        return [par] + Analisis_num_aux(num, divisor + 1)
    else:
        return Analisis_num_aux(num, divisor + 1)

def abrir_analisis_num ():
    window1 = tk.Toplevel()
    window1.title("Análisis númerico")
    window1.geometry("500x500")
    def cerrar_window1():
        window1.destroy()
    canva2 = tk.Canvas(window1, bg="#F028D2", width=WIDTH, height=HEIGHT)
    canva2.pack(fill="both", expand=True)
    tk.Label(canva2, text="Ingrese un número entero:").pack(pady=10)
    entrada_text = tk.Entry(canva2)
    entrada_text.pack(pady=5)
    label_result = tk.Label(canva2, text="Los pares son: ", fg="green", wraplength=350)
    label_result.pack(pady=20)
    def Analisis_connect ():
        user_text = entrada_text.get()
        if user_text.isdigit():
            valor = int(user_text)
            resultado = Analisis_num(valor)
            label_result.config(text=f"Los pares ordenados son: {resultado}")
        else:
            label_result.config(text="Error, ingrese solo números, y que sean enteros.", fg="red")
    botonw1 = tk.Button(canva2, text="Calcular pares ordenados", command=lambda: Analisis_connect())
    botonw1.pack(pady=5)
    botonw1_2 = tk.Button(canva2,text="Volver", command=lambda: cerrar_window1())
    botonw1_2.pack(pady=5)
    window1.mainloop()


        

canva1 = tk.Canvas(ventana, bg="#209ACA", width=WIDTH, height=HEIGHT)
canva1.pack()

labelV1 = tk.Label(ventana, text="Bienvenida a mi interfaz gráfica")
labelV1.place(x=160, y=25)

botonV1 = tk.Button(canva1, text="Analisis numérico",  command=lambda: abrir_analisis_num())
botonV1.place(x=5, y=5)
ventana.mainloop()
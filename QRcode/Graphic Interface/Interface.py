import qrcode
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox

def generar_qr():
    link = entry_link.get().strip()
    name = entry_nombre.get().strip()

    # Validar que se ingrese un enlace
    if not link:
        messagebox.showerror("Error", "El enlace no puede estar vacío.")
        return

    # Usar "ImagenQR" como nombre predeterminado si no se ingresa uno
    if not name:
        name = "ImagenQR"

    try:
        # Generar el código QR
        img = qrcode.make(link)
        archivo = filedialog.asksaveasfilename(
            defaultextension=".png",
            initialfile=name,
            filetypes=[("PNG files", "*.png")]
        )
        if archivo:
            img.save(archivo)
            messagebox.showinfo(
                "Éxito", f"Código QR generado y guardado como: {archivo}")
    except Exception as e:
        messagebox.showerror(
            "Error", f"Hubo un error al generar el QR: {str(e)}")


# Configuración de la interfaz gráfica
ventana = Tk()
ventana.title("Generador de Códigos QR")

# Etiquetas y entradas
Label(ventana, text="Ingrese un enlace:").grid(
    row=0, column=0, padx=10, pady=5, sticky="w")
entry_link = Entry(ventana, width=40)
entry_link.grid(row=0, column=1, padx=10, pady=5)

Label(ventana, text="Nombre del archivo (opcional):").grid(
    row=1, column=0, padx=10, pady=5, sticky="w")
entry_nombre = Entry(ventana, width=40)
entry_nombre.grid(row=1, column=1, padx=10, pady=5)

# Botón para generar el QR
Button(ventana, text="Generar QR", command=generar_qr).grid(
    row=2, column=0, columnspan=2, pady=10)

# Ejecutar la ventana
ventana.mainloop()

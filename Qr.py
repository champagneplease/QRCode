import qrcode

def generar_qr():
    link = input("Ingrese un link para generar un QR: ")
    name = input("Ingrese el nombre para guardar la imagen: ")

    img = qrcode.make(link)
    img.save(f'{name}.png')

    print(f"QR generado y guardado como {name}.png")

# Llamar función
generar_qr()

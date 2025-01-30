import qrcode

def generar_qr():
    link = input("Ingrese un link para generar un QR: ")
    name = input("Ingrese el nombre para guardar la imagen: ")
    if name == "":
        name = "ImagenQR"

    img = qrcode.make(link)
    img.save(f'{name}.png')

    print(f"QR generado y guardado como {name}.png")

generar_qr()

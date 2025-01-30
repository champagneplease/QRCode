import qrcode
import os

img = qrcode.make(input('Inrgese un link para generar un QR: '))
print(type(img))

img.save(input('Ingrese el nombre de la imagen: ')+'.png')

# Generador de Códigos QR

Este proyecto es un script en Python que permite generar códigos QR a partir de un enlace proporcionado por el usuario y guardarlos como imágenes PNG. Es una herramienta sencilla y fácil de usar.

## Requisitos previos

Antes de ejecutar el script, asegúrate de tener instalado lo siguiente:

- **Python3**  
- El módulo `qrcode`. Puedes instalarlo ejecutando el siguiente comando en tu terminal:

  ```bash
  pip install qrcode[pil]
  ```

## Instrucciones

1. **Ejecuta el script**:  
   Usa el siguiente comando en tu terminal, reemplazando `Qr.py` con el nombre del archivo del script:

   ```bash
   python3 Qr.py
   ```

2. **Sigue las instrucciones**:  
   - Ingresa un enlace para generar el código QR.  
   - Ingresa un nombre para guardar la imagen PNG.

3. **Resultado**:  
   El código QR generado se guardará en el mismo directorio donde se encuentra el script.

## Ejemplo de uso

Supongamos que el script se llama `Qr.py`. Al ejecutarlo con el siguiente comando:

```bash
python3 Qr.py
```

Aparecerá lo siguiente en la consola:

```
Ingrese un link para generar un QR: https://example.com
Ingrese el nombre para guardar la imagen (sin extensión): mi_codigo_qr
QR generado y guardado como mi_codigo_qr.png
```

El archivo `mi_codigo_qr.png` se guardará en el mismo directorio.
# :D
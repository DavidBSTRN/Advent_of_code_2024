from PIL import Image
import numpy as np
import os

# Funkce pro kontrolu čistoty tuby
def check_tube_cleanliness(image_path, threshold_value, dirty_pixel_limit):
    # Načtení obrázku
    tube_image = Image.open(image_path)

    # Převod obrázku na numpy pole
    tube_array = np.array(tube_image)

    # Prahování (thresholding) pro zvýraznění světlých míst
    bright_pixels = (tube_array > threshold_value).astype(np.uint8)

    # Spočítání jasných pixelů
    bright_pixel_count = np.sum(bright_pixels)

    # Vyhodnocení čistoty tuby
    print(f"Obrázek: {image_path}")
    print(f"Počet světlých pixelů: {bright_pixel_count}")

    if bright_pixel_count > dirty_pixel_limit:
        print("Tuba je špinavá.")
    else:
        print("Tuba je čistá.")

# Složka s obrázky
folder_path = 'OK'


# Procházení všech obrázků ve složce
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(folder_path, filename)
        check_tube_cleanliness(image_path, 200, 2000)


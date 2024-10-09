#Atividade
import cv2
import numpy as np
#import cv2_imshow # Import the cv2_imshow function
import matplotlib.pyplot as plt # Importa a biblioteca matplotlib e crie um alias para ela como plt

#Carrega a imagem da placa e coloca em tons de cinza
imagem = cv2.imread('C:/Users/user/Documents/GitHub/CGPI/Atividade Filtros/placa.png', cv2.IMREAD_GRAYSCALE)

#Aplicando Filtro Média (Suaviza)
filtro_media_7x7 = cv2.blur(imagem, (7, 7))
filtro_media_15x15 = cv2.blur(imagem, (5, 5))

#Aplicando Filtro Mediana (Suaviza)
filtro_gaussiano_mediana_7 = cv2.GaussianBlur(imagem, (7,7),0)
filtro_gaussiano_mediana_15 = cv2.GaussianBlur(imagem, (15,15),0)
#filtro_mediana_7 = cv2.medianBlur(imagem, 7)
#filtro_mediana_15 = cv2.medianBlur(imagem, 15)

#Aplicando Filtro Sobel (Destaca as bordas)
sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)
sobel_combinado = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)


# Exibir os Resultados:
plt.figure(figsize=(15, 10))

# Imagem Original
plt.subplot(3, 3, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')
plt.axis('off')

# Filtros de Média
plt.subplot(3, 3, 2)
plt.title('Filtro Média 7x7')
plt.imshow(filtro_media_7x7, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.title('Filtro Média 15x15')
plt.imshow(filtro_media_15x15, cmap='gray')
plt.axis('off')

# Filtros de Mediana
plt.subplot(3, 3, 5)
plt.title('Filtro Mediana 7')
plt.imshow(filtro_gaussiano_mediana_7, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.title('Filtro Mediana 15')
plt.imshow(filtro_gaussiano_mediana_15, cmap='gray')
plt.axis('off')

# Filtros Sobel
plt.subplot(3, 3, 4)
plt.title('Filtro Sobel X + Y')
plt.imshow(sobel_combinado, cmap='gray')
plt.axis('off')

plt.show()



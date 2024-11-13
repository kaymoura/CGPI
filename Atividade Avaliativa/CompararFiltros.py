import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_filtros(img):
    # Carregar a imagem
    img = cv2.imread('C:/Users/user/Documents/GitHub/CGPI/Atividade Avaliativa/fotoAntiga.jpg', 0)  # Carrega em escala de cinza

    # Aplicar os filtros
    blur = cv2.blur(img, (5, 5))
    median = cv2.medianBlur(img, 5)
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

    # Visualizar as imagens
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
    plt.subplot(2, 3, 2), plt.imshow(blur, cmap='gray'), plt.title('Média')
    plt.subplot(2, 3, 3), plt.imshow(median, cmap='gray'), plt.title('Mediana')
    plt.subplot(2, 3, 4), plt.imshow(gaussian, cmap='gray'), plt.title('Gaussiano')
    plt.subplot(2, 3, 5), plt.imshow(laplacian, cmap='gray'), plt.title('Laplaciano')
    plt.subplot(2, 3, 6), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
    plt.show()

# Chamar a função com o nome da sua imagem
aplicar_filtros('sua_imagem.jpg')
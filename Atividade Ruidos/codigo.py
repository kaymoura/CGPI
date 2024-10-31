import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem do coelho e coloca em tons de cinza
imagem = cv2.imread('C:/Users/user/Documents/GitHub/CGPI/Atividade Ruidos/coelho.jpg', cv2.IMREAD_GRAYSCALE)

# Função aplicando ruido gaussiano
def ruido_gaussiano(imagem, variancia):
    # Cria ruído gaussiano com média 0 e variância especificada
    ruido = np.random.normal(0, variancia**0.5, imagem.shape)
    imagem_ruido = np.clip(imagem + ruido, 0, 255)  # Garante que os valores fiquem entre 0 e 255
    return imagem_ruido.astype(np.uint8)

# Função aplicando ruido sal e pimenta
def ruido_sp(imagem, porcentagem):
    altura, largura = imagem.shape[:2]
    num_pixels = int(altura * largura * porcentagem)
    indices_pixels = np.random.randint(0, altura * largura, num_pixels)
    imagem = imagem.flatten()

    # Aplica "pimenta" (preto) e "sal" (branco)
    imagem[indices_pixels[:num_pixels // 2]] = 0  # Pimenta (preto)
    imagem[indices_pixels[num_pixels // 2:]] = 255  # Sal (branco)

    imagem = imagem.reshape((altura, largura))
    return imagem

# Gera imagens com ruído
imagem_gaussiana = ruido_gaussiano(imagem, variancia=25)
imagem_sal_pimenta = ruido_sp(imagem, porcentagem=0.05)

# Aplicando Filtro Gaussiano no ruido gaussiano
filtro_gaussiano_15 = cv2.GaussianBlur(imagem_gaussiana, (15, 15), 0)

# Aplicando Filtro Mediana no ruido gaussiano
filtro_mediana_15 = cv2.medianBlur(imagem_gaussiana, 15)

# Aplicando Filtro Bilateral no ruido gaussiano
filtro_bilateral_15 = cv2.bilateralFilter(imagem_gaussiana, d=15, sigmaColor=100, sigmaSpace=100)

# Aplicando Filtro Gaussiano no ruido sal e pimenta
filtro_gaussiano_sp = cv2.GaussianBlur(imagem_sal_pimenta, (15, 15), 0)

# Aplicando Filtro Mediana no ruido sal e pimenta
filtro_mediana_sp = cv2.medianBlur(imagem_sal_pimenta, 15)

# Aplicando Filtro Bilateral no ruido sal e pimenta
filtro_bilateral_sp = cv2.bilateralFilter(imagem_sal_pimenta, d=15, sigmaColor=100, sigmaSpace=100)

# Estrutura para mostrar as imagens
plt.figure(figsize=(12, 10))

# Exibe a imagem original
plt.subplot(3, 4, 1), plt.imshow(imagem, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])

# Exibe a imagem com ruido gaussiano
plt.subplot(3, 4, 5), plt.imshow(imagem_gaussiana, cmap='gray'), plt.title('Ruído Gaussiano')
plt.xticks([]), plt.yticks([])

# Filtros na Imagem com Ruído Gaussiano
plt.subplot(3, 4, 6), plt.imshow(filtro_gaussiano_15, cmap='gray'), plt.title('Filtro Gaussiano (Ruído Gaussiano)')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 4, 7), plt.imshow(filtro_mediana_15, cmap='gray'), plt.title('Filtro Mediana (Ruído Gaussiano)')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 4, 8), plt.imshow(filtro_bilateral_15, cmap='gray'), plt.title('Filtro Bilateral (Ruído Gaussiano)')
plt.xticks([]), plt.yticks([])

# Exibe a imagem com ruido sal e pimenta
plt.subplot(3, 4, 9), plt.imshow(imagem_sal_pimenta, cmap='gray'), plt.title('Ruído Sal e Pimenta')
plt.xticks([]), plt.yticks([])

# Filtros na Imagem com Ruído Sal e Pimenta
plt.subplot(3, 4, 10), plt.imshow(filtro_gaussiano_sp, cmap='gray'), plt.title('Filtro Gaussiano (Sal e Pimenta)')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 4, 11), plt.imshow(filtro_mediana_sp, cmap='gray'), plt.title('Filtro Mediana (Sal e Pimenta)')
plt.xticks([]), plt.yticks([])
plt.subplot(3, 4, 12), plt.imshow(filtro_bilateral_sp, cmap='gray'), plt.title('Filtro Bilateral (Sal e Pimenta)')
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
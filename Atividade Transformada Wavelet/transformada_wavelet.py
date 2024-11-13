# git + exhj + ex2 = 1500
# trabalho pra apresenta semana q vem = 4000
# Exercicio 2: Compreensão de imagem usando wallet
# objetivo: Utilizar a transformada Wavelet para realizar a compressão de uma imagem,
# removendo componentes de alta frequência (detalhes) e reconstruindo a imagem comprimida.
# no tratamento de ruidos aplicados a uma imagem
# Instruções: 1. Carregue uma imagem em escala de cinza.
# 2. Aplique a transformada Wavelet (usando 'haar') para decompor a imagem em componentes: (LL, LH, HL, HH)
# 3. Descarte os componentes de detalhes  (LH, HL, HH) e mantenha apenas o componente de baixa frequência (LL)
# 4. Realize a reconstrução inversa usando apenas o componente LL e visualize a imagem reconstruída.
# 5. Compare a imagem original com a imagem reconstruída. Avalie a qualidade da imagem comprimida.

import cv2
import numpy as np
import matplotlib.pyplot as plt
# Biblioteca para transformada wavelet
import pywt

# Carrega a imagem em tons de cinza
# imagem = cv2.imread('/content/drive/MyDrive/Colab Notebooks/coelho.jpg', cv2.IMREAD_GRAYSCALE)
imagem = cv2.imread('C:/Users/user/Documents/GitHub/CGPI/Atividade Ruidos/coelho.jpg', cv2.IMREAD_GRAYSCALE)

# Aplica a transformada Wavelet usando 'haar'
coeffs2 = pywt.dwt2(imagem, 'haar')
LL, (LH, HL, HH) = coeffs2  # LL = baixa frequência, LH, HL, HH = componentes de alta frequência

# Reconstrói a imagem apenas com LL (componente de baixa frequência)
imagem_comprimida = pywt.idwt2((LL, (None, None, None)), 'haar')

# Estrutura para mostrar as imagens
plt.figure(figsize=(10, 5))

# Exibe a imagem original
plt.subplot(1, 2, 1), plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.xticks([]), plt.yticks([])

# Exibe a imagem reconstruída com compressão
plt.subplot(1, 2, 2), plt.imshow(imagem_comprimida, cmap='gray')
plt.title('Imagem Comprimida (Apenas LL)')
plt.xticks([]), plt.yticks([])

plt.show()

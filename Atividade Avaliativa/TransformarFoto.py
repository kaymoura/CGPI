import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread('C:/Users/user/Documents/GitHub/CGPI/Atividade Avaliativa/joaquinzao.jpg', 0)

# Aplicar filtro de aguçamento (Unsharp Mask)
kernel_sharpen = np.array([[-1,-1,-1],
                           [-1, 9,-1],
                           [-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel_sharpen)

# Aplicar filtro Gaussiano para suavização
blurred = cv2.GaussianBlur(sharpened, (5,5), 0)

# Aplicar filtro de Laplace para detectar bordas
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
edges = np.uint8(np.absolute(laplacian))

# Combinar a imagem suavizada com as bordas
result = cv2.addWeighted(blurred, 0.8, edges, 0.2, 0)

# Mostrar as imagens
plt.figure(figsize=(20,6))

# Imagem original
plt.subplot(1,5,1),plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

# Imagem aguçada
plt.subplot(1,5,2),plt.imshow(sharpened, cmap='gray')
plt.title('Aguçada'), plt.xticks([]), plt.yticks([])

# Imagem suavizada
plt.subplot(1,5,3),plt.imshow(blurred, cmap='gray')
plt.title('Suavizada'), plt.xticks([]), plt.yticks([])

# Imagem com bordas (Laplaciano)
plt.subplot(1,5,4),plt.imshow(edges, cmap='gray')
plt.title('Bordas (Laplaciano)'), plt.xticks([]), plt.yticks([])

# Imagem final
plt.subplot(1,5,5),plt.imshow(result, cmap='gray')
plt.title('Resultado Final'), plt.xticks([]), plt.yticks([])

plt.tight_layout()  # Ajusta automaticamente o layout dos subplots
plt.show()
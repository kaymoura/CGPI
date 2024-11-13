import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from pywt import dwt2, idwt2

# Carregar a imagem
img = cv2.imread('C:/Users/user/Documents/GitHub/CGPI/Atividade Avaliativa/antiga.jpg', 0)  # Carregar em tons de cinza

# Transformada de Fourier
fft_img = fftpack.fft2(img)
fft_img_shift = np.fft.fftshift(fft_img)
magnitude_spectrum = 20*np.log(np.abs(fft_img_shift))

# Transformada Wavelet
coeffs = dwt2(img, 'haar')  # 'haar' é apenas um exemplo de wavelet
LL, (LH, HL, HH) = coeffs

# Reconstrução da imagem a partir da Transformada Wavelet
img_rec = idwt2(coeffs, 'haar')

# Visualização
fig, axes = plt.subplots(2, 3, figsize=(10, 5))
ax = axes.ravel()

ax[0].imshow(img, cmap='gray')
ax[0].set_title('Imagem Original')

ax[1].imshow(magnitude_spectrum, cmap='gray')
ax[1].set_title('Fourier')

ax[2].imshow(LL, cmap='gray')
ax[2].set_title('Aproximação (LL)')

ax[3].imshow(LH, cmap='gray')
ax[3].set_title('Detalhes (LH)')

ax[4].imshow(HL, cmap='gray')
ax[4].set_title('Detalhes (HL)')

ax[5].imshow(HH, cmap='gray')
ax[5].set_title('Detalhes (HH)')

plt.tight_layout()
plt.show()
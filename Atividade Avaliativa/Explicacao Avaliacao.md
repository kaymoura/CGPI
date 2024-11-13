# Atividade Avaliativa 

- Matéria de Computação Gráfica e Processamento de Imagens
- Professora Otilia

## Comparando Transformadas de Fourier e Wavelet em Python

### Introdução 

Comparar diretamente a imagem original com suas transformadas (Fourier e Wavelet) não é uma tarefa trivial. Cada transformada representa uma visão diferente dos dados, no domínio da frequência (Fourier) e em múltiplas resoluções (Wavelet). A "melhor" transformada dependerá fortemente da aplicação específica.

### Objetivo do Código 
- Carregar uma imagem: Utilizaremos a biblioteca OpenCV para carregar a imagem.
- Aplicar as transformadas: Calcularemos a Transformada de Fourier e a Transformada Wavelet discreta (DWT) usando as bibliotecas NumPy e SciPy.
- Visualizar os resultados: Utilizaremos a biblioteca Matplotlib para plotar as imagens originais e suas respectivas transformadas.
- Análise qualitativa: A escolha da melhor transformada será discutida com base nas visualizações, mas a decisão final dependerá do contexto da aplicação.

### Resultado

Está no arquivo Resultado_ComparandoTransformadas.png

## Comparando Filtros em Python

### Introdução

queremos comparar visualmente e possivelmente quantitativamente os efeitos de diferentes filtros em uma imagem. A "melhor" opção dependerá do resultado desejado, ou seja, do que se busca enfatizar ou atenuar na imagem.

### Objetivo do Código

### Resultado

Está no arquivo Resultado_CompararFiltros.png

## Aprimorando Imagem Antiga com Python.

### Introdução



### Ferramentas Usadas

* **Python:** Linguagem de programação.
* **OpenCV:** Biblioteca de visão computacional para processamento de imagens.
* **NumPy:** Biblioteca para operações numéricas em Python.
* **Matplotlib:** Biblioteca para visualização de dados, incluindo imagens.

### Código Python

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
img = cv2.imread('imagem_antiga.jpg', 0)  # Carrega em escala de cinza

# Aplicar filtro de aguçamento (Unsharp Mask)
kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])
sharpened = cv2.filter2D(img, -1, kernel)

# Aplicar filtro de Canny para detectar bordas
edges = cv2.Canny(sharpened, 100, 200)

# Combinar a imagem original com as bordas
result = cv2.addWeighted(sharpened, 0.8, edges, 0.2, 0)

# Mostrar a imagem original e a imagem processada
plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(result, cmap='gray')
plt.title('Imagem Processada'), plt.xticks([]), plt.yticks([])
plt.show()
```

### Explicação do Código

1. **Carregar a imagem:** Carrega a imagem em escala de cinza para simplificar o processamento.
2. **Filtro de aguçamento:** Aplica um kernel personalizado para aumentar o contraste nas bordas, tornando a imagem mais nítida.
3. **Detecção de bordas:** Utiliza o detector de bordas de Canny para encontrar as bordas na imagem aguçada.
4. **Combinação:** Combina a imagem aguçada com a imagem de bordas para realçar as características desejadas.
5. **Visualização:** Exibe a imagem original e a imagem processada lado a lado para comparação.

### Ajustando os Parâmetros

* **Kernel:** O kernel do filtro de aguçamento pode ser ajustado para obter diferentes níveis de nitidez.
* **Limiares de Canny:** Os valores dos limiares no detector de bordas de Canny controlam a sensibilidade à detecção de bordas.
* **Pesos da combinação:** Os pesos na função `cv2.addWeighted` controlam a contribuição da imagem aguçada e das bordas na imagem final.

### Considerações Adicionais

* **Ruído:** Aumentar a nitidez também pode amplificar o ruído presente na imagem. Para reduzir o ruído, considere aplicar filtros de suavização antes do aguçamento.
* **Outras técnicas:** Existem outras técnicas de processamento de imagens que podem ser utilizadas, como a restauração de imagens antigas e a remoção de arranhões.
* **Resultados:** Os resultados podem variar dependendo da qualidade da imagem original e dos parâmetros escolhidos.


### Resultado

Está no arquivo Resultado_TransformarFoto.png

# Atividade Avaliativa 

- Matéria de Computação Gráfica e Processamento de Imagens
- Professora Otilia

## 1. Comparando Transformadas de Fourier e Wavelet em Python

### Introdução 

Comparar diretamente a imagem original com suas transformadas (Fourier e Wavelet) não é uma tarefa trivial. Cada transformada representa uma visão diferente dos dados, no domínio da frequência (Fourier) e em múltiplas resoluções (Wavelet). A "melhor" transformada dependerá fortemente da aplicação específica.

### Objetivo do Código 
- Carregar uma imagem: Utilizaremos a biblioteca OpenCV para carregar a imagem.
- Aplicar as transformadas: Calcularemos a Transformada de Fourier e a Transformada Wavelet discreta (DWT) usando as bibliotecas NumPy e SciPy.
- Visualizar os resultados: Utilizaremos a biblioteca Matplotlib para plotar as imagens originais e suas respectivas transformadas.
- Análise qualitativa: A escolha da melhor transformada será discutida com base nas visualizações, mas a decisão final dependerá do contexto da aplicação.

### Análise e Considerações

#### Transformada de Fourier:

 - Captura as frequências presentes na imagem.
 - Útil para análise de padrões periódicos e filtragem de frequências.
 - A transformada de Fourier é global, ou seja, ela analisa a imagem inteira de uma só vez.
   
#### Transformada Wavelet:

 - Permite analisar a imagem em diferentes escalas (resoluções).
 - É útil para detectar características locais e bordas.
 - A decomposição wavelet oferece uma representação mais esparsa da imagem em muitos casos.

### Resultado
A escolha entre a Transformada de Fourier e a Transformada Wavelet depende da sua aplicação:

- Padrões periódicos: Fourier é mais adequada.
- Detalhes locais e bordas: Wavelet é mais adequada.
- Compressão de imagem: Wavelet é frequentemente usada devido à sua representação esparsa.
- Análise de textura: Ambas podem ser úteis, dependendo da natureza da textura.

Está no arquivo Resultado_ComparandoTransformadas.png

## 2. Comparando Filtros em Python

### Introdução

Comparar visualmente e possivelmente quantitativamente os efeitos de diferentes filtros em uma imagem. A "melhor" opção dependerá do resultado desejado, ou seja, do que se busca enfatizar ou atenuar na imagem. A escolha do melhor filtro depende da aplicação específica e dos objetivos da sua análise de imagem. A comparação visual é uma ferramenta poderosa, mas métricas quantitativas podem fornecer insights mais precisos.

### Objetivo do Código

- Carregamento da imagem: Carrega a imagem em escala de cinza para simplificar o processamento.
- Aplicação dos filtros: Cada filtro é aplicado à imagem original e o resultado é armazenado em uma variável.
- Visualização: As imagens original e filtradas são exibidas lado a lado para comparação visual.

### Resultado

#### Análise dos Resultados

- Filtros de suavização: Média, mediana e gaussiano reduzem o ruído e borram as bordas. A escolha entre eles depende do nível de suavização desejado.
- Filtro laplaciano: Detecta bordas e detalhes, destacando áreas de alta frequência.
- Filtro Sobel: Também detecta bordas, mas é mais sensível à direção das bordas.

Está no arquivo Resultado_CompararFiltros.png

## 3. Aprimorando Imagem Antiga com Python.

### Introdução

Considerando uso de uma Imagem antiga do Estádio do Joaquinzão em Taubaté, foi aplicado Filtro de aguçamento, filtro Gaussiano para suavização e filtro de Laplace para detectar bordas. Por fim a combinação deles. Com intuito de melhorar a imagem.

### Ferramentas Usadas

* **Python:** Linguagem de programação.
* **OpenCV:** Biblioteca de visão computacional para processamento de imagens.
* **NumPy:** Biblioteca para operações numéricas em Python.
* **Matplotlib:** Biblioteca para visualização de dados, incluindo imagens.

### Explicação do Código

1. **Carregar a imagem:** Carrega a imagem em escala de cinza para simplificar o processamento.
2. **Filtro de aguçamento:** Aplica um kernel personalizado para aumentar o contraste nas bordas, tornando a imagem mais nítida.
3. **Detecção de bordas:** Utiliza o detector de bordas de Canny para encontrar as bordas na imagem aguçada.
4. **Combinação:** Combina a imagem aguçada com a imagem de bordas para realçar as características desejadas.
5. **Visualização:** Exibe a imagem original e a imagem processada lado a lado para comparação.

### Resultado

Está no arquivo Resultado_TransformarFoto.png 

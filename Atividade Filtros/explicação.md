### Atividade Filtros

1 Carregar uma Imagem OK (Linha 08 do código)

2. Aplicar os Filtros:

   1. Observar as mudanças na imagem original após a aplicação dos filtros de média, mediana e Sobel.
      Média: O filtro de média suaviza a imagem, reduzindo o ruído e as bordas. Quanto maior o kernel (tamanho da matriz), maior o efeito de suavização.
      Mediana: A mediana também suaviza a imagem, mas é mais eficaz em remover ruído impulsivo (pimenta e sal). A mediana substitui o valor central de um pixel pela mediana dos valores dos pixels em sua vizinhança.
      Sobel: O filtro de Sobel destaca as bordas da imagem, detectando as variações de intensidade. O resultado é uma imagem que realça os contornos.

3. Analisar os Resultados:

   1. Responder às seguintes perguntas:
      a) Como a imagem original mudou após a aplicação de cada filtro?
      R\_ Média: A imagem se torna mais suave, perdendo detalhes finos e nitidez.
      Mediana: A imagem também se torna mais suave, mas preserva melhor os detalhes em comparação com a média. É especialmente eficaz em remover ruído impulsivo.
      Sobel: A imagem original é transformada em uma imagem que destaca as bordas, com os contornos dos objetos se tornando mais visíveis.

      b) Qual filtro foi mais eficaz para suavizar a imagem?
      R\_ Como não defini o tipo de ruído presente na imagem original, é difícil dizer qual filtro é o mais eficaz.

      c) E qual foi mais eficaz para destacar as bordas?
      R\_ O filtro Sobel é o mais eficaz para destacar as bordas, pois ele é projetado especificamente para detectar gradientes de intensidade.

      d) Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?
      R\_ Média: Redução de ruído gaussiano, preparação de imagens para segmentação, suavização de imagens antes da detecção de bordas.
      Mediana: Remoção de ruído impulsivo, preservação de detalhes em imagens com textura.
      Sobel: Detecção de bordas, extração de características, reconhecimento de padrões.

4. Experimentar:
   4.1. Experimentar diferentes tamanhos de kernel nos filtros de média e mediana (por exemplo, (3, 3), (5, 5), etc.) e observar como isso afeta a suavização da imagem.

   -> Experimento 1 - filtros de média (3,3)(6,6) e mediana (5,5)(10,10) - Resultado na figura 2

   Com essa tentativa notei que o kernel da mediana não executa pois ele necessariamente necessita ser um número impar para ter o centro da matriz. Então alterei o (10,10) para (11,11).

   -> Experimento 2 - filtros de média (4,4)(2,2) e mediana (9,9)(17,17) - Resultado na figura 3

   Os dois experimentos demonstraram que o tamanho do kernel influencia significativamente o resultado dos filtros. Kernels maiores tendem a produzir um efeito de suavização mais intenso, enquanto kernels menores preservam mais detalhes. É importante encontrar um equilíbrio entre suavização e preservação de detalhes para cada aplicação específica.

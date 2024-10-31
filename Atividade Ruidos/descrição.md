### Atividade Ruídos


Objetivo: avaliar a eficácia de diferentes filtros de suavização no tratamento de ruídos aplicados a uma imagem

Instruções:
1. Carregue uma imagem em escala de cinza. (Linha 06 do código)
2. Aplique dois tipos de ruídos à imagem: Ruído Gaussiano(Linha 09 do código) e Ruído Sal e Pimenta(Linha 16 do código)
3. Aplique os seguintes filtros à imagem ruidosa: filtro da média (gaussiano)(Linha 34 e 43 do código), filtro da mediana(Linha 37 e 46 do código), filtro bilateral(Linha 40 e 49 do código)
4. Para cada tipo de ruído, visualize e compare os resultados de cada filtro.(Linha 55 a 83 do código)
5. Desafio: Explique qual filtro se mostrou mais eficaz para cada tipo de ruído e por que:

	- O filtro gaussiano foi o mais eficaz para o ruído gaussiano, pois ele reduz as variações de intensidade de forma suave e homogênea, ideal para esse tipo de ruído que é distribuído de maneira contínua pela imagem. 
    - E o filtro da mediana foi o mais eficaz para o ruído sal e pimenta, pois ele é projetado para lidar com ruídos pontuais, removendo eficientemente os pixels de intensidade extrema sem prejudicar a nitidez da imagem.

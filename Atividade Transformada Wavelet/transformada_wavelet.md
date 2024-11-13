# Compressão de Imagem usando Transformada Wavelet

Este projeto explora o uso da Transformada Wavelet para compressão de imagem, removendo componentes de alta frequência (detalhes) e mantendo apenas o componente de baixa frequência para reconstruir uma versão comprimida da imagem. A qualidade da imagem comprimida é então comparada com a imagem original para avaliar a perda de detalhes.

## Descrição do Projeto
O objetivo deste projeto é realizar a compressão de uma imagem em tons de cinza, aplicando a Transformada Wavelet com o filtro 'haar'. A Transformada Wavelet decompõe a imagem em quatro componentes:

LL (Baixa Frequência): Contém a informação principal da imagem (padrão de baixa frequência).
LH, HL, HH (Alta Frequência): Contêm os detalhes e ruídos da imagem.
Para a compressão, apenas o componente LL é mantido, enquanto os componentes de alta frequência (LH, HL, HH) são descartados. A imagem é então reconstruída utilizando apenas o LL, resultando em uma versão menos detalhada e comprimida da imagem original.


## Conclusão
A Transformada Wavelet permite comprimir imagens removendo componentes de alta frequência, resultando em uma imagem de menor tamanho e com perda de detalhes. 

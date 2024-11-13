# Compressão de Imagem usando Transformada Wavelet

Este projeto explora o uso da Transformada Wavelet para compressão de imagem, removendo componentes de alta frequência (detalhes) e mantendo apenas o componente de baixa frequência para reconstruir uma versão comprimida da imagem. A qualidade da imagem comprimida é então comparada com a imagem original para avaliar a perda de detalhes.

## Descrição do Projeto
O objetivo deste projeto é realizar a compressão de uma imagem em tons de cinza, aplicando a Transformada Wavelet com o filtro 'haar'. A Transformada Wavelet decompõe a imagem em quatro componentes:

LL (Baixa Frequência): Contém a informação principal da imagem (padrão de baixa frequência).
LH, HL, HH (Alta Frequência): Contêm os detalhes e ruídos da imagem.
Para a compressão, apenas o componente LL é mantido, enquanto os componentes de alta frequência (LH, HL, HH) são descartados. A imagem é então reconstruída utilizando apenas o LL, resultando em uma versão menos detalhada e comprimida da imagem original.

### Instruções de Uso
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências:

bash
Copiar código
pip install opencv-python matplotlib pywavelets
Execute o script para carregar, comprimir e visualizar a imagem:

bash
Copiar código
python compressao_wavelet.py

### Avaliação da Qualidade da Imagem
Para avaliar a qualidade da imagem comprimida em relação à original, podem ser utilizadas métricas de similaridade de imagem como:

MSE (Erro Médio Quadrático): Calcula a média dos quadrados das diferenças de pixel entre as duas imagens. Valores menores indicam menor perda de qualidade.
PSNR (Pico de Sinal-Ruído): Mede a relação entre o valor máximo do sinal e o ruído, em decibéis (dB). Quanto maior o valor, melhor a qualidade da imagem reconstruída.
Cálculo do MSE e PSNR
python
Copiar código
import numpy as np

def calcula_mse(imagem_original, imagem_reconstruida):
    return np.mean((imagem_original - imagem_reconstruida) ** 2)

def calcula_psnr(mse, max_pixel=255.0):
    if mse == 0:
        return float('inf')
    return 20 * np.log10(max_pixel / np.sqrt(mse))

# Calcula o MSE e PSNR
mse = calcula_mse(imagem, imagem_comprimida)
psnr = calcula_psnr(mse)

print(f"MSE: {mse:.2f}")
print(f"PSNR: {psnr:.2f} dB")
Interpretação dos Resultados
MSE Baixo: Indica uma boa correspondência entre a imagem original e a reconstruída.
PSNR Alto (acima de 30 dB): Geralmente indica uma boa qualidade para a imagem reconstruída, mesmo após a perda de detalhes.
Resultados
Com base nos resultados do MSE e PSNR, podemos avaliar se a imagem comprimida preserva uma qualidade visual aceitável em comparação com a imagem original. Este método é particularmente útil em aplicações onde é necessária uma redução de dados, mas uma leve perda de qualidade visual é tolerável.

Conclusão
A Transformada Wavelet permite comprimir imagens removendo componentes de alta frequência, resultando em uma imagem de menor tamanho e com perda de detalhes. A comparação com a imagem original usando métricas como MSE e PSNR ajuda a quantificar a perda de qualidade, permitindo ajustar a compressão para obter um equilíbrio entre tamanho e qualidade.


# Importe a biblioteca numpy com o nome np
import numpy as np

# Imprima a versão do numpy e a configuração
print(np.__version__)

# ## Criação de arrays

# ### Crie um array numpy de tamanho 10, preenchido com zeros.
np.zeros(10)

# ### Crie um array numpy com valores variando de 10 a 49
np.arange(10, 50)

# ### Crie uma matriz numpy de inteiros 2x2, preenchida com uns.
np.ones([2, 2], dtype=np.int)

# ### Crie uma matriz numpy de números float 3x2, preenchida com uns.
np.ones([3, 2], dtype=np.float)

# ### Dado o array numpy X, crie um novo array numpy com o mesmo formato e tipo de X, preenchido com uns.
X = np.arange(4, dtype=np.int)
np.ones_like(X)

# ### Dada a matriz numpy X, crie uma nova matriz numpy com o mesmo formato e tipo de X, preenchida com zeros.
X = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int)
np.zeros_like(X)

# ### Crie uma matriz de inteiros 4x4 numpy, preenchida com cinco.
np.ones([4, 4], dtype=np.int) * 5

# ### Dada a matriz numpy X, crie uma nova matriz numpy com o mesmo formato e tipo de X, preenchida com sete.
X = np.array([[2, 3], [6, 2]], dtype=np.int)
np.ones_like(X) * 7

# ### Crie uma matriz de identidade numpy 3x3 com uns na diagonal e zeros em outros lugares.
np.identity(3)

# ### Crie um array numpy com 3 valores inteiros aleatórios entre 1 e 10.
np.random.randint(10, size=3)

# ### Crie uma matriz numpy 3x3x3, preenchida com valores float aleatórios.
np.random.randn(3, 3, 3)  # Floats de 0 a 1

# ### Dada a lista Python X, converta-a em um array numpy Y.
X = [1, 2, 3]
print(X, type(X))
Y = np.array(X)
print(Y, type(Y))  # Tipo diferente

# ### Dado o array numpy X, faça uma cópia e armazene-a em Y.
X = np.array([5, 2, 3], dtype=np.int)
print(X, id(X))
Y = np.copy(X)
print(Y, id(Y))  # IDs diferentes

# ### Crie um array numpy com números de 1 a 10.
np.arange(1, 11)

# ### Crie um array numpy com os números ímpares entre 1 e 10.
np.arange(1, 11, 2)

# ### Crie um array numpy com números de 1 a 10 em ordem decrescente.
np.arange(1, 11)[::-1]

# ### Crie uma matriz numpy 3x3 preenchida com valores de 0 a 8.
np.arange(9).reshape(3, 3)

# ### Mostre o tamanho da memória da matriz numpy Z dada.
Z = np.zeros((10, 10))
print("%d bytes" % (Z.size * Z.itemsize))

# ## Indexação de arrays

# ### Dado o array numpy X, mostre seu primeiro elemento.
X = np.array(['A', 'B', 'C', 'D', 'E'])
X[0]

# ### Dado o array numpy X, mostre seu último elemento.
X[-1]

# ### Dado o array numpy X, mostre seus três primeiros elementos.
X[0:3]  # Lembre-se! Os elementos começam no índice zero

# ### Dado o array numpy X, mostre todos os elementos do meio.
X[1:-1]

# ### Dado o array numpy X, mostre os elementos em posição ímpar.
X[::2]

# ### Dada a matriz numpy X, mostre os elementos da primeira linha.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X[0]

# ### Dada a matriz numpy X, mostre os elementos da última linha.
X[-1]

# ### Dada a matriz numpy X, mostre o primeiro elemento da primeira linha.
X[0, 0]

# ### Dada a matriz numpy X, mostre o último elemento da última linha.
X[-1, -1]

# ### Dada a matriz numpy X, mostre os elementos da linha do meio.
X[1:-1, 1:-1]

# ### Dada a matriz numpy X, mostre os dois primeiros elementos das duas primeiras linhas.
X[:2, :2]

# ### Dada a matriz numpy X, mostre os dois últimos elementos das duas últimas linhas.
X[2:, 2:]

# ### Converta o array numpy X dado em float.
X = [-5, -3, 0, 10, 40]
np.array(X, np.float)

# ### Inverta o array numpy X dado (o primeiro elemento se torna o último).
X[::-1]

# ### Ordene o array numpy X dado.
X = [0, 10, -5, 40, -3]
X.sort()
X

# ### Dado o array numpy X, defina o quinto elemento como 1.
X = np.zeros(10)
X[4] = 1
X

# ### Dado o array numpy X, mude o 50 para 40.
X = np.array([10, 20, 30, 50])
X[3] = 40
X

# ### Dada a matriz numpy X, mude a última linha para todos 1.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X[-1] = np.array([1, 1, 1, 1])
X

# ### Dada a matriz numpy X, mude o último item da última linha para 0.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X[-1, -1] = 0
X

# ### Dada a matriz numpy X, adicione 10 a cada elemento.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X + 10

# ### Dada a matriz numpy X, multiplique por 2 cada elemento.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X * 2

# ### Dada a matriz numpy X, divida por 2 cada elemento.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X / 2

# ### Dada a matriz numpy X, calcule a raiz quadrada de cada elemento.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
np.sqrt(X)

# ### Dada a matriz numpy X, calcule a média de todos os elementos.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
np.mean(X)

# ### Dada a matriz numpy X, calcule a média de cada linha.
np.mean(X, axis=1)

# ### Dada a matriz numpy X, calcule a média de cada coluna.
np.mean(X, axis=0)

# ### Dada a matriz numpy X, calcule a soma de todos os elementos.
np.sum(X)

# ### Dada a matriz numpy X, calcule a soma de cada linha.
np.sum(X, axis=1)

# ### Dada a matriz numpy X, calcule a soma de cada coluna.
np.sum(X, axis=0)

# ### Dado o array numpy X, adicione 5 a cada elemento menor que 10.
X = np.array([1, 6, 11, 15])
X[X < 10] += 5
X

# ### Dada a matriz numpy X, ajuste os valores menores que 10 para serem 10.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])
X[X < 10] = 10
X

# ### Dada a matriz numpy X, retorne os valores únicos.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
np.unique(X)

# ### Dada a matriz numpy X, obtenha os valores máximo e mínimo.
X = np.array([1, 3, 5, 7, 9])
np.max(X), np.min(X)

# ### Dada a matriz numpy X, obtenha os índices dos valores máximo e mínimo.
X = np.array([1, 3, 5, 7, 9])
np.argmax(X), np.argmin(X)

# ### Dada a matriz numpy X, calcule a média, mediana, desvio padrão e variância.
X = np.array([1, 2, 3, 4, 5, 6])
mean = np.mean(X)
median = np.median(X)
std_dev = np.std(X)
variance = np.var(X)
mean, median, std_dev, variance

# ### Dada a matriz numpy X, calcule a média das suas colunas.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
np.mean(X, axis=0)

# ### Dada a matriz numpy X, calcule a média das suas linhas.
X = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
np.mean(X, axis=1)

# ## Operações de Álgebra Linear

# ### Dados os arrays numpy A e B, multiplique-os.
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
np.dot(A, B)

# ### Dada a matriz numpy A, calcule a transposta.
A = np.array([[1, 2], [3, 4], [5, 6]])
A.T

# ### Dados os arrays numpy A e B, calcule o produto externo.
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
np.outer(A, B)

# ### Dados os arrays numpy A e B, calcule o produto interno.
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
np.inner(A, B)

# ### Dada a matriz numpy A, calcule o determinante.
A = np.array([[1, 2], [3, 4]])
np.linalg.det(A)

# ### Dada a matriz numpy A, calcule a inversa.
A = np.array([[1, 2], [3, 4]])
np.linalg.inv(A)

# ### Dada a matriz numpy A, calcule os autovalores e autovetores.
A = np.array([[1, 2], [3, 4]])
eigenvalues, eigenvectors = np.linalg.eig(A)
eigenvalues, eigenvectors

# ## Aprofundamento

# ### Crie um array numpy 10x10 com valores aleatórios e encontre os valores mínimo e máximo.
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
Zmin, Zmax

# ### Crie um vetor numpy de tamanho 30 e encontre o valor médio.
Z = np.random.random(30)
Zmean = Z.mean()
Zmean

# ### Crie uma matriz numpy 2D com 1s nos bordas e 0s dentro.
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0
Z

# ### Crie uma matriz numpy 8x8 e preencha-a com um padrão de tabuleiro de xadrez.
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
Z

# ### Normalize uma matriz numpy aleatória 5x5 (subtraia a média e divida pelo desvio padrão).
Z = np.random.random((5,5))
Z = (Z - np.mean(Z)) / np.std(Z)
Z

# ### Multiplique uma matriz numpy 5x3 por uma matriz 3x2.
A = np.random.random((5,3))
B = np.random.random((3,2))
np.dot(A, B)

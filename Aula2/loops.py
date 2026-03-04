# ===============================
# LOOPS EM PYTHON: FOR e WHILE
# ===============================

# Lista com vários tipos de dados
listas = [1, 3, 4, "Lista escola", 3.4, True]
# Índices:  0  1  2        3        4     5

# --------------------------------
# INFORMAÇÕES BÁSICAS DA LISTA
# --------------------------------

# len() retorna a quantidade de elementos da lista
print("Tamanho da lista:", len(listas))

# Acessando um elemento pelo índice (posição)
# Índices em Python começam em 0
print("Elemento da posição 0:", listas[0])


# =====================================
# LOOP FOR (usando índice com range)
# =====================================

# range(len(listas)) cria uma sequência de números
# de 0 até o tamanho da lista - 1
# Aqui estamos percorrendo a lista usando o índice
for i in range(len(listas)):
    print("Índice:", i, "| Valor:", listas[i])


# =====================================
# LOOP FOR estilo "foreach"
# =====================================

# Aqui não usamos índice
# A variável "lista" recebe diretamente cada valor da lista
for elemento in listas:
    print("Valor:", elemento)


# =====================================
# LOOP WHILE
# =====================================

# while executa enquanto a condição for verdadeira

# Guardamos o tamanho da lista
iend = len(listas)

# Criamos uma variável de controle começando em 0
i = 0

# Enquanto i for menor que o tamanho da lista
while i < iend:
    print("Índice:", i, "| Valor:", listas[i])
    
    # Incremento obrigatório para evitar loop infinito
    i += 1
import random
import time

# Lista com 10 mil elementos
minhaLista10k = [random.randint(1,10000) for _ in range(10000)]
minhaLista10k.sort()

# Lista com 100 mil elementos
minhaLista100k = [random.randint(1,100000) for _ in range(100000)]
minhaLista100k.sort()

# Lista com 1 milhão de elementos
minhaLista1M = [random.randint(1,1000000) for _ in range(1000000)]
minhaLista1M.sort()

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    etapas = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        etapas += 1

        if chute == item:
            return meio, etapas
        
        if chute > item:
            alto = meio - 1

        else:
            baixo = meio + 1

    return None, etapas

# Medindo o tempo de execução para a lista de 10 mil elementos
item_10k = random.randint(1, 10000)
inicio10k = time.time()
resultado_10k, etapas_10k = pesquisa_binaria(minhaLista10k, item_10k)
fim10k = time.time()

print("Lista com 10 mil elementos:")
print(f"Elemento buscado: {item_10k}")
print(f"Resultado da busca: {resultado_10k}")
print(f"Número de etapas: {etapas_10k}")
print(f"Tempo de execução: {fim10k - inicio10k} segundos")
print("\n")

# Medindo o tempo de execução para a lista de 100 mil elementos
item_100k = random.randint(1, 100000)
inicio100k = time.time()
resultado_100k, etapas_100k = pesquisa_binaria(minhaLista100k, item_100k)
fim100k = time.time()

print("Lista com 100 mil elementos:")
print(f"Elemento buscado: {item_100k}")
print(f"Resultado da busca: {resultado_100k}")
print(f"Número de etapas: {etapas_100k}")
print(f"Tempo de execução: {fim100k - inicio100k} segundos")
print("\n")

# Medindo o tempo de execução para a lista de 1 milhão de elementos
item_1M = random.randint(1, 1000000)
inicio1M = time.time()
resultado_1M, etapas_1M = pesquisa_binaria(minhaLista1M, item_1M)
fim1M = time.time()


print("Lista com 1 milhão de elementos:")
print(f"Elemento buscado: {item_1M}")
print(f"Resultado da busca: {resultado_1M}")
print(f"Número de etapas: {etapas_1M}")
print(f"Tempo de execução: {fim1M - inicio1M} segundos")
print("\n")
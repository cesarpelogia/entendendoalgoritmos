import random
import time

# Lista com 10 mil elementos
minhaLista10k = random.sample(range(1, 10001), 10000)
minhaLista10k.sort()

# Lista com 100 mil elementos
minhaLista100k = random.sample(range(1, 100001), 100000)
minhaLista100k.sort()

# Lista com 1 milhão de elementos
minhaLista1M = random.sample(range(1, 1000001), 1000000)
minhaLista1M.sort()

def pesquisa_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    etapas = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]
        etapas += 1

        if chute == item:
            return chute, etapas
        
        if chute > item:
            fim = meio - 1

        else:
            inicio = meio + 1

    return None, etapas

# Medindo o tempo de execução para a lista de 10 mil elementos
item_10k = random.randint(1, 10000)
inicio10k = time.perf_counter()
resultado_10k, etapas_10k = pesquisa_binaria(minhaLista10k, item_10k)
fim10k = time.perf_counter()
tempo10k = fim10k - inicio10k
tempo10k_microsegundos = tempo10k * 1_000_000

print("Lista com 10 mil elementos:")
print(f"Elemento buscado: {item_10k}")
print(f"Resultado da busca: {resultado_10k}")
print(f"Número de etapas: {etapas_10k}")
print(f"Tempo de execução: {tempo10k:.7f} segundos")
print("\n")

# Medindo o tempo de execução para a lista de 100 mil elementos
item_100k = random.randint(1, 100000)
inicio100k = time.perf_counter()
resultado_100k, etapas_100k = pesquisa_binaria(minhaLista100k, item_100k)
fim100k = time.perf_counter()
tempo100k = fim100k - inicio100k
tempo100k_microsegundos = tempo100k * 1_000_000

print("Lista com 100 mil elementos:")
print(f"Elemento buscado: {item_100k}")
print(f"Resultado da busca: {resultado_100k}")
print(f"Número de etapas: {etapas_100k}")
print(f"Tempo de execução: {tempo100k:.7f} segundos")
print("\n")

# Medindo o tempo de execução para a lista de 1 milhão de elementos
item_1M = random.randint(1, 1000000)
inicio1M = time.perf_counter()
resultado_1M, etapas_1M = pesquisa_binaria(minhaLista1M, item_1M)
fim1M = time.perf_counter()
tempo1M = fim1M - inicio1M
tempo1M_microsegundos = tempo1M * 1_000_000

print("Lista com 1 milhão de elementos:")
print(f"Elemento buscado: {item_1M}")
print(f"Resultado da busca: {resultado_1M}")
print(f"Número de etapas: {etapas_1M}")
print(f"Tempo de execução: {tempo1M:.7f} segundos")
print("\n")
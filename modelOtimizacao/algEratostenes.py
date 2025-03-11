import time
import psutil

def crivo_eratostenes(limite):
    # Medição inicial de recursos
    cpu_inicial = psutil.cpu_percent(interval=0.1)
    memoria_inicial = psutil.virtual_memory().percent
    disco_inicial = psutil.disk_usage('/').percent
    bytes_enviados_inicial = psutil.net_io_counters().bytes_sent
    bytes_recebidos_inicial = psutil.net_io_counters().bytes_recv
    
    inicio = time.time()

    eh_primo = [True for i in range(limite + 1)]
    eh_primo[0] = eh_primo[1] = False 
 
    p = 2
    
    while p * p <= limite:
        if eh_primo[p]:
            for i in range(p * p, limite + 1, p):
                eh_primo[i] = False
     
        p += 1
    
    primos = [p for p in range(2, limite + 1) if eh_primo[p]]
    fim = time.time()
    tempo = fim - inicio
    
    # Medição final de recursos
    cpu_final = psutil.cpu_percent(interval=0.1)
    memoria_final = psutil.virtual_memory().percent
    disco_final = psutil.disk_usage('/').percent
    bytes_enviados_final = psutil.net_io_counters().bytes_sent
    bytes_recebidos_final = psutil.net_io_counters().bytes_recv
    
    # Cálculo das diferenças
    uso_cpu = cpu_final
    uso_memoria = memoria_final
    uso_disco = disco_final
    dados_enviados = bytes_enviados_final - bytes_enviados_inicial
    dados_recebidos = bytes_recebidos_final - bytes_recebidos_inicial
    
    # Resultado com estatísticas de recursos
    recursos = {
        'uso_cpu': uso_cpu,
        'uso_memoria': uso_memoria,
        'uso_disco': uso_disco,
        'dados_enviados': dados_enviados,
        'dados_recebidos': dados_recebidos
    }
    
    return primos, tempo, recursos


if __name__ == "__main__":
    limite = 1000
    numeros_primos, tempo, recursos = crivo_eratostenes(limite)
    
    print(f"Números primos até {limite}:")
    print(numeros_primos)
    print(f"Tempo de execução: {tempo:.6f} segundos")
    
    # Exibindo estatísticas de recursos
    print("\nEstatísticas de uso de recursos:")
    print(f"CPU: {recursos['uso_cpu']:.2f}%")
    print(f"Memória: {recursos['uso_memoria']:.2f}%")
    print(f"Disco: {recursos['uso_disco']:.2f}%")
    print(f"Dados enviados: {recursos['dados_enviados']} bytes")
    print(f"Dados recebidos: {recursos['dados_recebidos']} bytes")
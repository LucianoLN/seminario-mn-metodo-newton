import math  # Importa a biblioteca math para usar o valor de pi

def volume_esfera(R):
    return (4 * math.pi * (R ** 3)) / 3

# Função f(h): representa a equação do volume da calota esférica menos o volume desejado
def f(h, R, V):
    return (math.pi * h**2 / 3) * (3*R - h) - V

# Função derivada f'(h): derivada da função f(h) em relação a h
def df(h, R):
    return math.pi * h * (2*R - h)

# Função que aplica o método de Newton-Raphson
def metodo_newton(h0, R, V, tolerancia, max_iter):
    h = h0  # Define h com o valor do chute inicial

    # Mostra o cabeçalho da tabela de iterações
    print(f"{'Iteração':<10} | {'Altura (h)':<15} | {'Erro (f(h))':<15}")
    print("-" * 45)

    # Laço que repete o processo até o número máximo de iterações
    for i in range(max_iter):
        f_h = f(h, R, V)   # Calcula o valor da função no ponto atual
        df_h = df(h, R)    # Calcula o valor da derivada no ponto atual

        # Verifica se a derivada é zero para evitar divisão por zero
        if df_h == 0:
            print("Derivada nula. O método falhou.")
            return None  # Encerra a função se não puder continuar

        # Fórmula do método de Newton-Raphson
        h_novo = h - f_h / df_h

        # Exibe os dados da iteração atual
        print(f"{i+1:<10} | {h:<15.6f} | {f_h:<15.6e}")

        # Verifica se a diferença entre o valor novo e o antigo é menor que a tolerância
        if abs(h_novo - h) < tolerancia:
            return h_novo  # Retorna o valor encontrado se o erro for pequeno

        h = h_novo  # Atualiza h para a próxima iteração

    # Se atingir o número máximo de iterações, retorna o último valor calculado
    return h

# =========================
# Programa principal
# =========================

R = 3              # Raio da esfera
V = 30           # Volume desejado
h0 = 3.0           # Chute inicial para a altura
tolerancia = 0.0001  # Erro máximo permitido
max_iter = 20      # Número máximo de iterações

# Verificação dos valores da esfera
if (V > volume_esfera(R)): 
    print("VOLUME INVÁLIDO")
    print(f"Volume máximo da esfera é de {volume_esfera(R):.2f}")
else:
    # Chama a função do método de Newton
    resultado = metodo_newton(h0, R, V, tolerancia, max_iter)
    
    # Verifica se encontrou um resultado válido
    if resultado:
        print("-" * 45)
        print(f"A altura necessária é: {resultado:.4f} metros")

import math

def f(h):
    # Função baseada no volume da calota esférica: (pi * h^2 / 3) * (3R - h) - V
    return (math.pi * h**2 / 3) * (9 - h) - 30

def df(h):
    # Derivada da função em relação a h: pi * h * (2R - h)
    return math.pi * h * (6 - h)

def metodo_newton(h0, tolerancia, max_iter):
    h = h0
    print(f"{'Iteração':<10} | {'Altura (h)':<15} | {'Erro (f(h))':<15}")
    print("-" * 45)
    
    for i in range(max_iter):
        f_h = f(h)
        df_h = df(h)
        
        # Evita divisão por zero
        if df_h == 0:
            print("Derivada nula. O método falhou.")
            return None
            
        # Fórmula de Newton-Raphson: h_novo = h - f(h)/f'(h)
        h_novo = h - f_h / df_h
        
        print(f"{i+1:<10} | {h:<15.6f} | {f_h:<15.6e}")
        
        # Critério de parada
        if abs(h_novo - h) < tolerancia:
            return h_novo
        
        h = h_novo
        
    return h

# Parâmetros Iniciais
raio = 3
volume_alvo = 30
chute_inicial = 3.0  # Começamos no meio do tanque (h = R)
erro_admitido = 0.0001


resultado = metodo_newton(chute_inicial, erro_admitido, 20)

if resultado:
    print("-" * 45)
    print(f"A altura necessária é: {resultado:.4f} metros")

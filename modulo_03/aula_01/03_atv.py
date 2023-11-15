
'''
Uma loja de informática recebeu componentes usados de um 
computador para avaliar se estão com defeito. As peças que 
não estiverem com defeito podem ser colocadas à venda. Como, 
então, podemos criar uma solução em Python para resolver 
esse problema?
'''

def create_report():
    componentes_verificados = set(['caixas de som', 'cooler', 'dissipador de calor', 'cpu', 'hd', 'estabilizador', 'gabinete', 'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem', 'monitor', 'mouse', 'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner', 'teclado', 'webcam'])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])
    componentes_ok = componentes_verificados.difference(componentes_com_defeito)

    print(componentes_ok)

    print(f"Componentes verificados = {len(componentes_verificados)}")
    print(f"Componentes defeituosos = {len(componentes_com_defeito)}")
    print(f"Componentes ok = {len(componentes_ok)}")    

    print("Os componentes que podem ser vendidos são:")
    for i in componentes_ok:
        print(i)
        
create_report()  
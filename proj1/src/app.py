class FirstQuestion:
    def __init__(self, valor_inicial, valor_final):
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final

    def imprimir_pares(self):
        i = self.valor_inicial
        
        while i <= self.valor_final:
            
            if i % 2 == 0:  
                print(i)
                
            i += 1

# Exemplo de uso:
questao = FirstQuestion(15, 200)
questao.imprimir_pares()

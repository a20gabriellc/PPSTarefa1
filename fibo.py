import unittest

#Función que genera la sucesión de Fibonacci
def fibonacci(n):
    fibo = [0, 1]
    
    while n > len(fibo):
        m = fibo[len(fibo) - 1] + fibo[len(fibo) - 2]
        fibo.append(m)
    
    return fibo

resultado = fibonacci(15)
print(resultado)

class test(unittest.TestCase):
    #El nombre debe empezar por "test", por algún motivo
    def test_hacer(self): 
        #pongo 4 porque recordemos que en los arrays las posiciones empiezan por 0
        #por tanto para la 5ª posición hay que poner 4
        self.assertEqual(resultado[4], 3)
        
if __name__ == '__main__': 
    unittest.main() 

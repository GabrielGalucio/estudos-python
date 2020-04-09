# PRINT vs RETURN
# print: does not affect the calculation of the output 
# return: does not visualize the output, it specifies what a certain function is supposed 
# to give back

def funcao_retorno(a):
    resultado = a + 10
    return resultado

print(funcao_retorno(2))

def funcao_testanto(b):
    resultado = b * 2
    print("Teste")
    return resultado

print(funcao_testanto(2))
# Uma das caracteristicas mais úteis em Python ( e para iniciantes
# pode paraecer um pouco confuso) são as expressões lambda. Expres
# soes lambda nos permitem criar funções "anônimas". Ista significa
# que podemos fazer rapidamente funções ad-hoc sem a necessidade de
# definir uma função usando a palavra reservado def.

# Objetos de função desenvolvidos executando expressões lambda funci
# onam exatamente da mesma forma como aqueles criados e atribuidos pe
# la palavra reservada def. Mas há algumas diferenças fundamentais que
# fazem lambda útil em funções especializadas

# 1- O corpo do lambda é uma única expressão. não um bloco de instruções
# 2- O corpo do lambda é semelhante a uma instrução de retorno do corpo def

# Expressões lambda realment são úteis quando usada em conjunto com as fun
# ções map(), filter() e reduce()

# Expressões lambda são usada para criar funções simples, são tambem chamadas
# funções in-line ou apenas de funções anonimas. SINTAXE:

# lambda parametro_entrada: retorno da função
# lambda x: x**2

# Diferenças do def e lambda

# def -> cria um objeto e atribui um nome a ele (nome da função)
# lambda -> cria um objeto, mas retorna como um resultado em tempo de execução
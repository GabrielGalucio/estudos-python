# Quando há erro porem é necessário continuação

#try:
#    print(5/0)
#except:
#    print("Ocorreu um erro")
#finally:
#    print("O usuario X realizou calculo no sistema")


# Quando há um erro e você continua o passando s
for buscar in range(10):
    try:
        print("Buscando informações")
        print(5/0)
    except:
        pass
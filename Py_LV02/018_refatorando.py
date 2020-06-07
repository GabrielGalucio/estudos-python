import logging 

logging.basicConfig(             # Para criar e adicionar informação de como vamos armazenar
    filename = "dados.log",      # Nome do arquivo do log
    level = logging.DEBUG,       # level serve -> somente info de nivle para cima (5 niveis)
    format = "%(levelname)s %(asctime)s: %(message)s",# Define qual formato vai ser armazenaod no arquivo txt
    datefmt = "%d/%m/%Y %H:%M:%S"        # Define o formato da data do arquivo txt
)

# Instanciando a classe StreamHandler (do import loggin)
logger = logging.StreamHandler()
logging.getLogger("").addHandler(logger)

try:
    ano_atual = int(input("Digite aqui o ano atual: "))
except ValueError:
    logging.warning("Você deve digitar um número valido crlh")

try:
    print(5/0)
except:
    logging.warning("Ocorreu um erro")
finally:
    logging.info("O usuario X realizou calculo no sistema")



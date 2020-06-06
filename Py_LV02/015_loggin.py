# Loggin mantem um historico do que está acontecendo no programa em txt
import logging 

logging.basicConfig(             # Para criar e adicionar informação de como vamos armazenar
    filename = "info.log",      # Nome do arquivo do log
    level = logging.DEBUG,       # level serve -> somente info de nivle para cima (5 niveis)
    format = "%(levelname)s %(asctime)s: %(message)s",# Define qual formato vai ser armazenaod no arquivo txt
    datefmt = "%d/%m/%Y %H:%M:%S"        # Define o formato da data do arquivo txt
)

# Instanciando a classe StreamHandler (do import loggin)
logger = logging.StreamHandler()
logging.getLogger("").addHandler(logger)


# Escrevendo um retorno
logging.debug("Isso é uma mensagem nivel debug")
logging.info("Isso é uma mensagem nivel info")
logging.warning("Isso é uma mensagem nivel warning")
logging.error("Isso é uma mensagem nivel error")
logging.critical("Isso é uma mensagem nivel critical")
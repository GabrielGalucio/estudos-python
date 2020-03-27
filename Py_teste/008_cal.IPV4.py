# Calculos de sub-rede IPV4 em python

# O usuário pode enviar o seu endreço IP de duas formas, como no exemplo:
# 192.168.0.1/24 -> Informar o IP com o prefixo da rede
# 192.168.0.1 255.255.255.0 -> Informar o IP com a máscar da subrede

# O programa deverá ser inteligente o suficiante para distinguir os doi tipos e extrair as infor
# mações necessárias para o usuario, que geralmente se concentra e 03 (três) sendo elas:
# 1- REDE
# 2- BROADCAST
# 3- N DE IP's

# Check list
# Incialmente uma classe irá ser criada e a mesma deverá receber parametros obrigadotiros já in-
# formados no texto acima, basicamente: ip ou ip/cidr -> prefixo(ou prefixo ou máscara), mascara
# (ou máscara ou prefixo) bem como as demais pontos do check lista enunciados abaixo::::::::::::
# 01- Checar se o IP foi enviado;
# 02- Checar se o IP tem prefixo -> extair prefixo;
# 03- Verificar se o IP é válido;
# 04- Checar se a máscara ou prefixo foram enviados;
# 05- Converter o IP decimal para IP binário;
# 06- Obter o prefixo da máscara;
# 07- Configurar o broadcast e a rede em binário;
# 08- Obter máscara de subrede em prefixo.

# Retorno final:
# Dicionário com IP, prefixo, mascara, rede, broadcast e n_IP's
# TUDO ISSO POR IR EM READ.ME***

import re       # Importando expressões regulares

class Ipv4NetworkCalculator():
    def __init__(self, ip='', prefixo='', mascara='', rede='', broadcast='', numero_ips=''):
        self.ip = ip
        self.prefixo = prefixo
        self.mascara = mascara
        self.rede = rede
        self.broadcast = broadcast
        self.numero_ips = numero_ips

        print("Teste")

        # Checando se o endereço IP foi enviado -> Naturalmente ira dar erro pois não há parametro
        if self.ip == '':
            raise ValueError("IP não enviado.")

    # Crias-e uma expressão regular para ver se o IP tem prefixo
    def ip_tem_prefixo(self):
        ip_prefixo_regexp = re.compile('')


if __name__ == '__main__':
    ipv4 = Ipv4NetworkCalculator(ip='192.169.0.1')

# PAROU EM 12:12







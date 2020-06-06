# Modulos

import tela as tl
import wifi as wf
from time import sleep

tl.controleBrilhoTela()
sleep(5)
tl.controleAplicativoCelular()

wf.criarWifi()
wf.alterarSenhaWifi()
wf.conectarWifi()

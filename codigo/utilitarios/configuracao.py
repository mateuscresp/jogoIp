import os


#Constantes de configuração
NOME_JOGO = "Neymar Time Attack - Copa do Mundo"
LARGURA_TELA = 800
ALTURA_TELA = 600

FPS = 60

COR_BRANCA = (255, 255, 255)
COR_PRETA = (0, 0, 0)
COR_VERDE = (34, 139, 34)

TEMPO_INICIAL = 30 #tempo concedido ao iniciar a partida
TEMPO_MAX = 60 #teto máximo acumulável

VELO_NEYMAR = 5 #px/frame
VELO_SPRINT = 8 #px/frame

STAMINA_MAX = 100 #máximo de pontos de stamina
CONSUMO_STAMINA = 20  #gasto ao sprinting (20 pontos por segundo)
REGEN_STAMINA = 10 #regenera 10 pontos por segundo


#Caminhos
DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA_RECURSOS = os.path.join(DIRETORIO_BASE, "recursos")

#Dicionário organizador de recursos
ASSETS = {
    "IMAGENS": {
        "NEYMAR": os.path.join(PASTA_RECURSOS, "imagens", "neymar.png"),
        "PAMONHA": os.path.join(PASTA_RECURSOS, "imagens", "pamonha.png"),
        "TACA": os.path.join(PASTA_RECURSOS, "imagens", "taca.png"),
        "BANDEIRA_INGLATERRA": os.path.join(PASTA_RECURSOS, "imagens", "bandeira_inglaterra.png"),
        "BANDEIRA_ALEMANHA": os.path.join(PASTA_RECURSOS, "imagens", "bandeira_alemanha.png"),
        "BANDEIRA_ARGENTINA": os.path.join(PASTA_RECURSOS, "imagens", "bandeira_argentina.png"),
        "BANDEIRA_ESPANHA": os.path.join(PASTA_RECURSOS, "imagens", "bandeira_espanha.png"),
        "BANDEIRA_FRANCA": os.path.join(PASTA_RECURSOS, "imagens", "bandeira_franca.png"),
    },

    "SONS": {
        "MUSICA_FUNDO": os.path.join(PASTA_RECURSOS, "sons", "musica_copa.mp3"),
        "COLETA_PAMONHA": os.path.join(PASTA_RECURSOS, "sons", "pamonha.wav"),
        "COLETA_BANDEIRA": os.path.join(PASTA_RECURSOS, "sons", "bandeira.wav"),
        "COLETA_TACA": os.path.join(PASTA_RECURSOS, "sons", "taca.wav"),
    },

    "FONTES": {
        "FONTE_PRINCIPAL": os.path.join(PASTA_RECURSOS, "fontes", "fonte_jogo.ttf"),
    }
}
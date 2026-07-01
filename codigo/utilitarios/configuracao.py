import os


#Constantes de configuração
NOME_JOGO = "Neymar Time Attack - Copa do Mundo"
LARGURA_TELA = 800
ALTURA_TELA = 600

FPS = 60

COR_BRANCA = (255, 255, 255)
COR_PRETA = (0, 0, 0)
COR_VERDE = (34, 139, 34)

TEMPO_INICIAL = 10 #Tempo concedido ao iniciar a partida
TEMPO_MAX = 20 #Teto máximo acumulável

VELO_NEYMAR = 5 #px/frame
VELO_SPRINT = 8 #px/frame

STAMINA_MAX = 100 #Máximo de pontos de stamina
CONSUMO_STAMINA = 20  #Gasto ao sprinting (20 pontos por segundo)
REGEN_STAMINA = 10 #Regenera 10 pontos por segundo


#Caminhos
DIRETORIO_BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PASTA_RECURSOS = os.path.join(DIRETORIO_BASE, "recursos")

#Dicionário organizador de recursos
ASSETS = {
    "IMAGENS": {
        #Sprites de Neymar
        "NEYMAR_PARADO": os.path.join(PASTA_RECURSOS, "imagens", "NEYPARADO.png"),
        "NEYMAR_ANDANDO1": os.path.join(PASTA_RECURSOS, "imagens", "NEYANDANDO1.png"),
        "NEYMAR_ANDANDO2": os.path.join(PASTA_RECURSOS, "imagens", "NEYANDANDO2.png"),
        "NEYMAR_CORRENDO1": os.path.join(PASTA_RECURSOS, "imagens", "NEYCORRENDO1.png"),
        "NEYMAR_CORRENDO2": os.path.join(PASTA_RECURSOS, "imagens", "NEYCORRENDO2.png"),
        
        #Colecionáveis principais
        "PAMONHA": os.path.join(PASTA_RECURSOS, "imagens", "PAMONHA.png"),
        "TACA": os.path.join(PASTA_RECURSOS, "imagens", "TACA.png"),
        
        #Bandeiras
        "BANDEIRA_INGLATERRA": os.path.join(PASTA_RECURSOS, "imagens", "INGLATERRA.png"),
        "BANDEIRA_ALEMANHA": os.path.join(PASTA_RECURSOS, "imagens", "ALEMANHA.png"),
        "BANDEIRA_ARGENTINA": os.path.join(PASTA_RECURSOS, "imagens", "ARGENTINA.png"),
        "BANDEIRA_ESPANHA": os.path.join(PASTA_RECURSOS, "imagens", "ESPANHA.png"),
        "BANDEIRA_FRANCA": os.path.join(PASTA_RECURSOS, "imagens", "FRANCA.png"),
    },


   "SONS": {
        #Trilhas e efeitos sonoros
        "MUSICA_FUNDO": os.path.join(PASTA_RECURSOS, "sons", "musica_copa.mp3"),
        "COLETA_PAMONHA": os.path.join(PASTA_RECURSOS, "sons", "pamonha.wav"),
        "SPAWN_BANDEIRA": os.path.join(PASTA_RECURSOS, "sons", "spawn_bandeira.wav"),
        "COLETA_TACA": os.path.join(PASTA_RECURSOS, "sons", "taca.wav"),
        "GAME_OVER": os.path.join(PASTA_RECURSOS, "sons", "game_over.wav"),
        "VITORIA": os.path.join(PASTA_RECURSOS, "sons", "vitoria.mp3"),
    },

    "FONTES": {
        "FONTE_PRINCIPAL": os.path.join(PASTA_RECURSOS, "fontes", "fonte_jogo.ttf"),
    }
}
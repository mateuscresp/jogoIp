# 🎮 Jogo da Disciplina de IP - CIn / UFPE

Projeto Final desenvolvido para a disciplina de Introdução à Programação.

---

## 👥 Integrantes do Grupo
* Mateus Crespim - GitHub: @mateuscresp
* Caio César - GitHub: @CaioC11
* [Nome do Integrante 3] - GitHub: @usuario3
* [Nome do Integrante 4] - GitHub: @usuario4

---

## 🚀 Tecnologias Utilizadas
* Python 3
* Pygame

---

## Estrutura do repositório
jogolp/
│
├── recursos/                 # 🎨 Tudo o que for mídia visual ou sonora do jogo (antigo 'assets')
│   ├── imagens/             # Sprites do personagem, itens e obstáculos (PNG)
│   ├── cenarios/            # Imagens de fundo das telas e fases
│   └── sons/                # Músicas de fundo e efeitos sonoros (SFX)
│
├── codigo/                  # 💻 Todo o código-fonte estruturado do jogo (antigo 'src')
│   ├── __init__.py          # Arquivo para o Python reconhecer a pasta como um pacote
│   │
│   ├── classes/             # 🧱 Onde o grupo vai aplicar POO obrigatoriamente
│   │   ├── __init__.py
│   │   ├── elemento_jogo.py # Classe base (mãe) para herança
│   │   ├── jogador.py       # Classe que controla o personagem (antigo 'player')
│   │   └── itens.py         # Classe com os 3 tipos de coletáveis distintos
│   │
│   └── utilitarios/         # ⚙️ Configurações e ferramentas de suporte (antigo 'utils')
│       ├── __init__.py
│       └── configuracao.py  # Cores, tamanho da tela, FPS, etc. (antigo 'config')
│
├── .gitignore               # 🧹 Ignorar arquivos temporários do sistema
├── README.md                # 📝 Relatório e documentação do projeto
└── principal.py             # 🚀 Onde roda o Game Loop (antigo 'main.py')
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

## 📂 Arquitetura do Projeto

A estrutura de diretórios do projeto foi organizada de forma modular para facilitar o desenvolvimento em grupo e a aplicação de Orientação a Objetos:

```text
jogolp/
│
├── recursos/                 # 🎨 Mídias visuais e sonoras do jogo
│   ├── imagens/             # Sprites do personagem, itens e obstáculos (PNG)
│   ├── cenarios/            # Imagens de fundo das telas e fases
│   └── sons/                # Músicas de fundo e efeitos sonoros (SFX)
│
├── codigo/                  # 💻 Código-fonte estruturado do projeto
│   ├── __init__.py          # Inicializador de pacote modular do Python
│   │
│   ├── classes/             # 🧱 Implementação dos conceitos de POO
│   │   ├── __init__.py
│   │   ├── elemento_jogo.py # Classe base (mãe) para herança de sprites
│   │   ├── jogador.py       # Classe que controla o personagem principal
│   │   └── itens.py         # Classes dos 3 tipos distintos de coletáveis
│   │
│   └── utilitarios/         # ⚙️ Configurações gerais e suporte
│       ├── __init__.py
│       └── configuracao.py  # Centralizador de variáveis globais (Cores, FPS, Janela)
│
├── .gitignore               # 🧹 Filtro para ignorar arquivos temporários do sistema
├── README.md                # 📝 Relatório e documentação principal do projeto
└── principal.py             # 🚀 Arquivo principal que executa o Game Loop
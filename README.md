# Discord Meme Bot

Bot feito em Python usando discord.py que reproduz áudios de memes
em canais de voz.

## Funcionalidades

- !comandos → Exibe todos os comandos disponíveis
- !sus → Bot responde **AMOGUS**
- !dado → Rola um dado de 6 lados
- !memes → lista os memes disponíveis
- !play (meme) → Reproduz áudio do meme escolhido
- !stop → Interrompe a reprodução do áudio
- !info → Exibe informações sobre o bot

## Tecnologias

- Python
- discord.py
- FFmpeg
- PyNaCl

## Como executar

### 1 - **É necessário Instalar as dependências!**

### Para instalar FFmpeg no Windows 10/11:
no terminal, digite...

```winget install ffmpeg```

```pip install -r requirements.txt```

---

### Instalar no Linux:
no terminal, digite...

```sudo apt install ffmpeg```

```pip install -r requirements.txt```

### Biblioteca libopus0

```sudo apt update```

```sudo apt install libopus0```

---

2 - Adicione seu token no bot.py

3 - Execute o bot:

```python bot.py```
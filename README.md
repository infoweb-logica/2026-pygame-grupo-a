# 2026-pygame-grupo-a

## Guias
- [guia do desenvolvedor](https://github.com/infoweb-logica/2026-pygame-grupo-a/wiki/dev)
---

## FIXME [título do jogo]

### Resumo do jogo

O jogo será baseado em uma mecânica de luta em turnos entre dois jogadores, semelhante àqueles de referência estudados pela equipe. O cenário do jogo representará espaços do IFRN, campus Natal-Central, e seus personagens, as principais Diretorias Acadêmicas. Cada um desses personagens possuirá poderes com diferentes mecânicas, sempre inspirados nos estereótipos dessas diretorias.

### O Que faz o jogador ganhar? O que faz Perder?

O Jogador vai ter um sistema de vida, o HP, assim como o inimigo, e quando esse HP zera, o inimigo, ou o player morre.

Exemplo:

```python
HP_PLAYER = 150
vivo = True
if HP_PLAYER <= 0:
   vivo = False
```

Tambem haverá um TIMER que definine a duração total da partida, e se esse timer acabar, haverá um desempate, ou seja:  
DESEMPATE!  
Inimigo = 120HP  
Player  = 126HP

Ambos vão começar a ganhar dano, até a vida de um chegar a zero, e quem chegar a zero primeiro, perde. Se ambos tiverem com a mesma quantia de vida, dá empate.

Exemplo de código:
```python

# SITUAÇÃO DE EMPATE
vida_player  = 120 # maximo de vida é 200
vida_inimigo = 120
vivo         = True
timer        = 5 # minutos, nesse exemplo
situacao_desempate = False

if timer <= 0:
   situacao_desempate = True

if situacao_desempate == True:
   for vida in range(200):
      vida_player  - 1
      vida_inimigo - 1

      if vida_player <= 0:
         vivo = False
         break
      
      if vida_inimigo <= 0:
         print("Parabens! voce ganhou!")
         break

```

### Referência de outros jogos
- Jogos de turno da franquia Pokémon
- Seleção de personagens e mapas como em jogos de luta (Street Fighter, Mortal Kombat, ...)

### Design do jogo

A mecânica principal do jogo é baseada em combate em turnos alternados, com ataques e habilidades únicas para cada personagem.
Durante o combate, o jogador terá três opções de ataque, incluindo uma habilidade especial, selecionáveis por botões na tela ou por ações do teclado personalizáveis.
Os personagens e cenários são escolhidos antes da luta pelos jogadores.

FIXME [Link para o figma] ou [Rascunhos das telas em papel]

FIXME [Elementos áudio visuais do jogo (sprites, fundos, etc) são autorais ou de terceiros? construídos ou baixados de qual lugar?]


Engine: pygame(https://pygame-zero.readthedocs.io/)

### Demo do jogo

FIXME [Vídeo do jogo]

FIXME [Como fazer para jogar?]

---
## Equipe
- [Davi Az.](https://github.com/Mazvedo) 
- [isadora](https://github.com/isadoralidynara)
- [João Gabriel](https://github.com/jvsziinn)
- [Kaun](https://github.com/kkauankauan19x)
- [Kristhyan](https://github.com/kristhyanlima-svg)
- [Leonardo Ataide Minora](https://github.com/leonardo-minora)
- [Lorena](https://github.com/Lores034)
- [Lucas Gabriel](https://github.com/Adicide)
- [Luiz Heytor](https://github.com/NoxHG)
- [Luyza](https://github.com/mari1aluyza)
- [Mateus "C?" Lemos](https://github.com/archangello)
- [Miguel Alexandre](https://github.com/M1guel_Alexandre)
- [Moisés](https://github.com/kjzeyss)
- [Ravi Rodrigues](https://github.com/raviaguiar)
- [Renan Azevedo](https://github.com/MrRBAzevedo)
- [Sara](https://github.com/hilflerty)
- [Vitor Carvalho](https://github.com/Vaert4201)
- [Vitor Emidio](https://github.com/VoiidHead)

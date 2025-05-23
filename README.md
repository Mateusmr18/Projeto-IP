# Jogo Old Beats
## Membros:
- Cairo Henrique Silva Thomaz de Aquino (chsta@cin.ufpe.br)
- Eduardo Gabriel de Souza Pedroza (egsp@cin.ufpe.br)
- Jadson José da Silva Lins (jjsl2@cin.ufpe.br)
- Mateus Rafael Correia de Melo (mrcm@cin.ufpe.br)
- Rodrigo Pereira Ferreira (rpf2@cin.ufpe.br)
- Ryann Andre Dias da Silva (rads@cin.ufpe.br)

## Descrição da Arquitetura do Projeto:
# Ideia geral:
- Interface: 2D - Com visões superior e horizontal.
- Jogabilidade: Movimentação varia entre lateral e livre conforme as fases.
- Fases: São 3 fases com chefes e mecânicas individuais:
  
Fase 1 (Pianista) - Movimentação lateral com mecânica de pulo, o objetivo é desviar dos projéteis lançados horizontalmente pelo pianista;

Fase 2 (Guitarrista) - Movimentação lateral, o objetivo é desviar dos projéteis lançados verticalmente pelo chefe, o personagem tem uma área especifica para acertar o chefe;

Fase 3 (Baterista) - Ataque do baterista se trata de projetéis que se expandem de forma aleatória pelo cenário, sendo o objetivo do jogador desviar desses ataques.

- Itens: Ao derrotar cada um dos chefes você receberá o instrumento usado por ele.
- Condição de vitória: Obter todos os instrumentos de cada chefe.
- Condição de derrota: Caso o protagonista recebe muito dano do chefe, ocorrerá um game over na fase em que estiver.
- Interação com objetos:
Ao derrotar um chefe ele dropará o instrumento que quando coletado ficará salvo no menu de seleção de fase.


## Capturas de Tela:
![Imagem 1](prints/selecao_fases.jpg) 
![Imagem 2](prints/fase_kurt.jpg)
![Imagem 3](prints/tela_guitarra.jpg)



## Bibliotecas e Ferramentas Utilizadas:
Biblioteca PyGame

Biblioteca random - Utilizada em situações como na aleatoriedade do tempo entre cada ataque do boss baterista e na aleatoriedade da ordem das imagens dos projetéis.

WhatsApp e Discord - Meios de comunicação
Piskel, LibreSprites, PhotoShop - Criação das pixel arts para as sprites


## Divisão de Trabalho:
- Cairo Henrique: Programação do protagonista, menu de seleção de fase e integração do timing do ritmo
- Eduardo Pedroza: Programação do Boss 3 (baterista)
- Jadson Lins: Design/criação das artes do personagem, bosses e ataques
- Mateus Rafael: Programação do Boss 1 (pianista)
- Rodrigo Ferreira: Programação do Boss 2 (guitarrista)
- Ryann: Criação dos cenários de cada fase
Além disso, a equipe se uniu em diferentes momentos para debater e apresentar soluções em conjunto.

## Conceitos da disciplina utilizados:
- Foram utilizados diversos conceitos essenciais, destacando estruturas condicionais, laços de repetição e lprints/selecao_fases.jpgistas. Além disso o código inteiro apresenta o uso de Programação Orientada a Objetos, com diferentes classes reutilizáveis.

## Desafios e Erros Enfrentados e Lições Aprendidas no Decorrer do Projeto:
Provavelmente o maior erro que cometemos foi a organização/comunicação precária, o que dificultou a unificação entre as funções dos membros do grupo. Tentamos resolver esse erro com reuniões, pessoalmente ou por call.
Ademais, o projeto foi desafiador no que se refere a conseguir pôr as ideias em prática no período curto de tempo, além de conciliar o projeto com outras atividades acadêmicas.
Aprendemos que a organização é essencial e deve ser o pilar para a extruturação de qualquer projeto.

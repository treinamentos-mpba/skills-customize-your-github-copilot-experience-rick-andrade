
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa um jogo da Forca em Python no qual o jogador adivinha uma palavra sorteada. Pratique listas, strings, entrada de dados, condicionais e loops.

## 📝 Tarefas

### 🛠️ Preparar a Palavra e o Estado do Jogo

#### Descrição
Complete a preparação do jogo para selecionar uma palavra secreta e inicializar as variáveis que acompanharão os palpites.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words`.
- Inicializar uma coleção para registrar as letras já adivinhadas.
- Definir e inicializar o limite de palpites incorretos.
- Preparar o estado necessário para exibir quais letras da palavra já foram descobertas.

### 🛠️ Conduzir uma Partida

#### Descrição
Implemente o loop principal para receber palpites, atualizar o estado do jogo e encerrar a partida quando houver vitória ou derrota.

#### Requisitos
O programa concluído deve:

- Exibir a palavra com letras não descobertas representadas por `_` e solicitar um palpite de letra.
- Revelar as posições correspondentes quando o palpite estiver na palavra.
- Contabilizar palpites incorretos e informar quantas tentativas restam.
- Encerrar quando todas as letras forem descobertas ou o limite de palpites incorretos for atingido.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.
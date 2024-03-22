# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Pisquinha")
define h = Character("Husk")
define k = Character("Kai")


# O jogo começa aqui.

label start:

    with fade

    scene cenario2

    "Dois irmãos lutam pela liderança do clã dos lobos"

    play music "/audio/musicadefundo.mp3"

    show pisquinha

    with dissolve

    p "Não quero brigar com você irmão"

    p "Essa luta não faz sentido pra mim"

    hide pisquinha

    show husk

    with dissolve

    h "Deixa de conversa mole Pisquinha"

    h "Isso pra mim tem outro nome"

    h "Covardia"

    hide husk

    "Pisquinha deve enfrentar o irmão Husk"

menu:

    "Sim.":
        jump game

    "Não.":
        jump book

label game:

    show pisquinha

    with dissolve

    p "Se não há outra escolha, eu estou pronto irmão"

    hide pisquinha

    show husk

    with dissolve

    h "Farei o que deve ser feito"

    hide husk

    jump marry

label book:

    show husk

    with dissolve

    h "Você não tem escolha, lembre-se a força vem do seu interior"

    hide husk

    show pisquinha

    with dissolve

    p "Eu não queria, mas é o unico jeito"

    hide pisquinha

    jump marry

label marry:

    "Os irmãos batalharam"

    stop music


    return

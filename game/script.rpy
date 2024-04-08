# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mina = Character("Mina")
define luna = Character("Luna")
define voce = Character("Você")

image bgPark = "backgrounds/bgpark.jpg"
image bgRuas = "backgrounds/bgruas.jpg"
image bgRuasNoite = "backgrounds/bgruasnoite.jpg"

image mina11 = "characters/mina/mina1-1.png"
image luna11 = "characters/luna/luna1-1.png"
image luna12 = "characters/luna/luna1-2.png"
image luna13 = "characters/luna/luna1-3.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgPark
    with pixellate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mina11

    # These display lines of dialogue.

    "Você está andando pelo parque..."
    "..."

    mina "Olá, quem é você?"
    voce "Eu sou o ..., e você?"
    mina "Eu sou a Mina"
    voce "O que você está fazendo por aqui?"
    mina "Acabei de me mudar pra cá"
    
    menu:
        "Chamar ela para conhecer o Bairro":
            jump conhecerBairro
        "Volte para sua casa e vá comer bolachas":
            jump comerBolachas

label conhecerBairro:

    voce "Quer conhecer o bairro comigo?"
    mina "Claro!!!"
    "..."
    mina "Então... Para onde vamos mesmo?"
    voce "Vários lugares!!!"

    scene bgRuas
    with pixellate

    "Então vocês andaram pelas ruas"
    "..."

    mina "Vai demorar muito?"

    # This ends the game.
    return

label comerBolachas:

    hide mina11

    "Então você a ignora e volta para sua casa sozinho..."
    "Voltando as horas passam e já é noite"

    jump gameOver

label gameOver:

    scene bgRuasNoite
    with pixellate

    "Agora na sua frente uma estranha garota aparece..."

    show luna11

    luna "Moço poderia me ajudar?"
    voce "Sim, qual o problema?"

    show luna12
    with dissolve

    luna "O PROBLEMA É APENAS VOCÊ!!!!"

    show luna13
    with dissolve

    "Então esse é o fim para você né?"
    "Mas não se preocupe existem outras chances"

    # This ends the game.
    return

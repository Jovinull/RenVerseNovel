# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mina = Character("Mina")
define luna = Character("Luna")
define voce = Character("Você")

image park = "backgrounds/park.jpg"
image ruas = "backgrounds/ruas.jpg"
image ruasNoite = "backgrounds/ruasnoite.jpg"
image cafe = "backgrounds/cafe.jpg"
image distritoComercial = "backgrounds/distritocomercial.png"
image praca = "backgrounds/praca.jpg"

image iconCopoCafe = "items/copocafe.png"

image mina11 = "characters/mina/mina1-1.png"
image mina12 = "characters/mina/mina1-2.png"
image mina21 = "characters/mina/mina2-1.png"
image mina22 = "characters/mina/mina2-2.png"

image luna11 = "characters/luna/luna1-1.png"
image luna12 = "characters/luna/luna1-2.png"
image luna13 = "characters/luna/luna1-3.png"

# The game starts here.

label start:

    $ foiProCafe = False
    $ quantidadeCafe = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene park
    with pixellate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mina11

    # These display lines of dialogue.

    "Você está andando pelo parque..."
    "..."

    hide mina11
    show mina22
    with dissolve

    mina "Olá, quem é você?"
    voce "Eu sou o ..., e você?"
    mina "Eu sou a Mina"

    hide mina22
    show mina21
    with dissolve

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

    scene ruas
    with pixellate

    hide mina21
    show mina22
    with dissolve

    mina "Então... Para onde vamos mesmo?"
    voce "Vários lugares!!!"

    "Então vocês andaram pelas ruas"
    "..."
    mina "Vai demorar muito?"
    voce "Já já chegaremos"
    
    scene distritoComercial
    with pixellate

    voce "É aqui que as lojas ficam!!"
    mina "Nossa é sério? Nem havia reparado"
    "Você sente a ironia"

    menu:
        "Convidar ela para tomar um café":
            voce "Então... Você quer ir tomar um café?"
            mina "Claro, andar está me deixando cansada"
            $ foiProCafe = True
            jump cafe
        "Continuar explorando a cidade":
            jump continuarPasseio

    # This ends the game.
    return

label comerBolachas:

    hide mina11

    "Então você a ignora e volta para sua casa sozinho..."
    "Voltando as horas passam e já é noite"

    jump gameOver

label cafe:

    scene cafe
    with pixellate

    hide mina22
    show mina11
    with dissolve

    "Vocês se sentam... Mas ficam um clima estranho"
    "Ambos olhando um para o outro não teria um resultado diferente, né?"
    "Então você toma uma atitude"
    voce "Que tal pegar café para nós dois? Eu pago"
    mina "Já que você quer ser tão cavalheiro, não posso negar"

    show iconCopoCafe at right
    with Dissolve(1)
    $ quantidadeCafe += 1

    "Vocês conversam enquanto tomar o café..."
    "As horas passam e vocês terminam..."
    "Mas será que ela gostaria de outro café?"

    menu:
        "Oferecer outro café":
            jump cafe
        "Sair e continuar o passeio":
            jump continuarPasseio

label continuarPasseio:

    scene praca

    voce "Essa aqui é a praça onde passei parte de minha infância brincando"

    hide mina11
    show mina22
    with dissolve

    mina "Bem legal, parece um ótimo lugar para deixar as crianças se desenvolverem né"
    voce "Claro que é!! Por isso sou um cara incrivel"
    "Você escuta ela dando algumas risadas divertidas"

    hide mina22
    show mina12
    with dissolve

    voce "Então posso assumir que gostou daqui?"
    mina "Muito!!"
    voce "Bom, acho melhor irmos embora, já está ficando tarde"

    hide mina12
    show mina11
    with dissolve

    mina "Concordo"

    menu:
        "Levar ela para sua casa":
            jump levarCasa
        "Voltar para casa":
            jump gameOver

label levarCasa:

    hide mina11

    scene ruasNoite

    "Vocês andam e nada realmente especial acontece, apenas andam por aí"
    
    show mina12
    with dissolve

    mina "Bom, aqui eu já estou bem perto de casa, Obrigada por hoje"
    voce "Não foi nada"

    hide mina12
    show mina22
    with dissolve

    mina "Obrigada mesmo por me mostrar a cidade hoje"

    if foiProCafe == True:
        mina "E também por me levar no café, foi divertido te conhecer melhor"

        hide mina22
        show mina21
        with dissolve

        voce "Bom, eu também gostei de te conhecer, então acho que estamos quites"

        hide mina21
        show mina22
        with dissolve

        mina "É mais você pagou %(quantidadeCafe)d cafés isso foi muito generoso da sua parte, eu gosto muito disso e de café"

        if quantidadeCafe >= 5:
            mina "Na verdade foram muitos cafés né... Eu estava distraida conversando com você e nem percebi"
            mina "Bom, eu PROMETO que depois irei te recompensar de alguma forma"

return

label gameOver:

    scene ruasNoite
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

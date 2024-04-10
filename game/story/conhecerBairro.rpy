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

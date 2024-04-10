label start:

    $ foiProCafe = False
    $ quantidadeCafe = 0

    play music "musics/awesomeness.mp3" fadein 1.5

    scene park
    with pixellate

    show mina11

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

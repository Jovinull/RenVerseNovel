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

    show parabens
    with dissolve

return
label continuarPasseio:

    scene praca

    voce "Essa aqui é a praça oSnde passei parte de minha infância brincando"

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
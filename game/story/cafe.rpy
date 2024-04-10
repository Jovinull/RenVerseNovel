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
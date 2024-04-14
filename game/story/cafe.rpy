label cafe:

    scene cafe
    with pixellate

    hide mina22
    show mina11
    with dissolve

    "Na atmosfera aconchegante do café, o aroma tentador do café fresco paira no ar, envolvendo você e Mina enquanto vocês se acomodam em uma mesa próxima à janela. A luz suave do entardecer filtra-se pelas cortinas, criando um ambiente acolhedor e tranquilo."
    "Enquanto vocês se sentam, uma leve tensão parece pairar entre vocês, como se ambos estivessem um pouco nervosos com a situação. No entanto, você decide quebrar o gelo e fazer algo para tornar o momento mais confortável."
    "Então você toma uma atitude"
    voce "Que tal pegar café para nós dois? Eu pago"
    "Você sugere, tentando amenizar o clima. Mina sorri suavemente, parecendo aliviada com a sua iniciativa."
    mina "Já que você quer ser tão cavalheiro, não posso negar"
    "Ela responde com um toque de brincadeira na voz."
    "Enquanto você se levanta para fazer o pedido no balcão, os sons suaves de conversas e o vapor da máquina de café preenchem o espaço ao redor. Você pede dois cafés, um expresso para você e um cappuccino para Mina, lembrando-se de suas preferências que ela mencionou anteriormente."

    show iconCopoCafe at right
    with Dissolve(1)
    $ quantidadeCafe += 1

    "Logo, os cafés são entregues à mesa, cada xícara emanando calor e promessa de conforto. Vocês dois envolvem as mãos ao redor das xícaras, apreciando o calor reconfortante enquanto começam a conversar."
    "As palavras fluem facilmente entre vocês, e o tempo parece desacelerar enquanto vocês compartilham histórias, risadas e pensamentos. O sabor rico do café complementa a atmosfera relaxante, criando um momento íntimo e especial entre vocês dois."
    "À medida que as horas passam, vocês terminam os cafés, mas a conexão entre vocês parece mais forte do que nunca. No entanto, você se pergunta se Mina gostaria de mais uma xícara."

    menu:
        "Oferecer outro café":
            "Decidindo prolongar o momento agradável, você sugere a Mina que peçam mais uma rodada de café. Ela aceita o convite com um sorriso, e vocês dois continuam desfrutando da companhia um do outro enquanto saboreiam mais uma xícara quente."
            jump cafe
        "Sair e continuar o passeio":
            "Percebendo que já passaram tempo suficiente no café, você propõe a Mina que continuem o passeio pela cidade. Ela concorda prontamente, e vocês se levantam da mesa, prontos para explorar mais lugares interessantes juntos."
            jump continuarPasseio
            
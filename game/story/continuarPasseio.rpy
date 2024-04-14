label continuarPasseio:

    scene praca

    "Depois de deixar o café, vocês dois continuam o passeio pela cidade, explorando os lugares interessantes que o bairro tem oferecer. Logo, vocês chegam a uma praça pitoresca, onde você costumava passar boa parte de sua infância brincando."
    voce "Essa aqui é a praça onde passei parte de minha infância brincando"
    "você compartilha com Mina, apontando para os diferentes pontos que trazem lembranças antigas à tona."
    "Mina olha ao redor, admirando a beleza tranquila da praça."
    hide mina11
    show mina22
    with dissolve
    mina "Bem legal, parece um ótimo lugar para deixar as crianças se desenvolverem, né?"
    "ela comenta, com um brilho de admiração nos olhos."
    "Você não pode deixar de sorrir para o comentário dela."
    voce "Claro que é! Por isso sou um cara incrível"
    "Você brinca, provocando algumas risadas divertidas dela."
    "Depois de aproveitarem um pouco mais o ambiente da praça, você percebe que o sol começa a se pôr no horizonte, pintando o céu com tons dourados e alaranjados."
    voce "Bom, acho melhor irmos embora, já está ficando tarde"
    "você sugere, olhando para Mina."
    "Ela concorda prontamente, mostrando-se compreensiva com a ideia de encerrar o passeio por hoje. ela responde, parecendo satisfeita com a experiência que tiveram juntos."
    mina "Concordo"
    hide mina22
    show mina12
    with dissolve
    "Com isso, vocês começam a se despedir da praça, prontos para seguir para o próximo destino. No entanto, surge uma escolha importante:"
    hide mina12
    show mina11
    with dissolve

    menu:
        "Levar ela para sua casa":
            "Você decide levar Mina para sua casa, oferecendo-lhe uma carona ou acompanhando-a até lá para garantir que chegue em segurança. Essa é uma oportunidade para prolongar o tempo juntos e continuar a conversa no conforto de um ambiente familiar."
            jump levarCasa
        "Voltar para casa":
            "Você opta por voltar para casa, desfrutando do tempo que passaram juntos e deixando Mina seguir seu caminho. Embora você tenha gostado muito da companhia dela, você sabe que é hora de cada um seguir sua própria jornada.""
            jump gameOver
label conhecerBairro:
    
    "Depois de convidar Mina para conhecer o bairro, ela aceita animadamente, e vocês dois partem juntos para explorar as ruas tranquilas e os cantos escondidos do local."

    scene ruas
    with pixellate

    hide mina21
    show mina22
    with dissolve

    "Mina parece genuinamente interessada em descobrir mais sobre a área, e você se sente feliz por poder mostrar a ela os encantos do bairro."
    "Enquanto caminham, você aponta os principais pontos de interesse, como parques, cafés aconchegantes e pequenas lojas locais."
    "Mina parece estar aproveitando cada momento, absorvendo as informações com entusiasmo, e você se diverte compartilhando suas histórias e curiosidades sobre o lugar."
    
    scene distritoComercial
    with pixellate

    "Depois de um tempo, vocês chegam ao distrito comercial do bairro. As ruas estão movimentadas, com pessoas indo e vindo, e as lojas exibem suas vitrines coloridas."
    "Você aponta para as diferentes lojas, explicando o que cada uma oferece, e Mina parece impressionada com a variedade de opções."
    "Mina olha ao redor, admirando a paisagem urbana, e você percebe um leve cansaço em seus olhos."
    "É compreensível, afinal, vocês caminharam bastante. Nesse momento, você se vira para ela, ponderando sobre o que fazer a seguir."
    
    menu:
        "Convidar ela para tomar um café":
            "Você sugere a Mina que vocês parem para tomar um café em um dos cafés charmosos que você passou no caminho. Mina parece gostar da ideia, e vocês entram juntos no café, sentindo o cheiro delicioso do café fresco."
            $ foiProCafe = True
            jump cafe
        "Continuar explorando a cidade":
            "Decidindo aproveitar ao máximo o tempo juntos, você propõe a Mina continuar explorando a cidade, mesmo que isso signifique mais caminhada. Mina concorda prontamente, mostrando-se animada para descobrir mais lugares interessantes ao seu lado."
            jump continuarPasseio

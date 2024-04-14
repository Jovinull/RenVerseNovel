label levarCasa:

    hide mina11

    scene ruasNoite

    "Enquanto vocês caminham pelas ruas à noite, o ambiente tranquilo e sereno parece envolvê-los, proporcionando um momento de calma após um dia cheio de descobertas. Vocês dois compartilham silêncios confortáveis enquanto seguem o caminho de volta para a casa de Mina."
    
    show mina12
    with dissolve

    mina "Bom, aqui eu já estou bem perto de casa. Obrigada por hoje"
    "Mina diz, parando em frente à sua residência e olhando para você com gratidão."
    voce "Não foi nada"
    "Você responde, sentindo-se satisfeito por ter passado o dia ao lado dela."
    "Mina sorri suavemente, os olhos brilhando com apreciação."
    hide mina12
    show mina22
    with dissolve
    mina "Obrigada mesmo por me mostrar a cidade hoje"
    "Ela expressa sinceramente."

    if foiProCafe == True:
        mina "E também por me levar no café, foi divertido te conhecer melhor."

        hide mina22
        show mina21
        with dissolve

        voce "Bom, eu também gostei de te conhecer, então acho que estamos quites."

        hide mina21
        show mina22
        with dissolve

        "Mina ri suavemente, parecendo genuinamente tocada pela gentileza que você demonstrou"
        mina "É, mas você pagou %(quantidadeCafe)d cafés, isso foi muito generoso da sua parte. Eu gosto muito disso e de café"

        if quantidadeCafe >= 5:
            mina "Na verdade, foram muitos cafés né... Eu estava distraída conversando com você e nem percebi. Bom, eu PROMETO que depois irei te recompensar de alguma forma."
            "Com isso, você se despede de Mina, vendo-a entrar em sua casa com um aceno gentil. Enquanto você retorna para o seu próprio lar, uma sensação de contentamento e gratidão preenche seu coração, lembrando-lhe do dia especial que passou ao lado dela."

    show parabens
    with dissolve

return
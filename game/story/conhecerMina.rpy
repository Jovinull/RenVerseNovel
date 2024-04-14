label conhecerMina:

    scene park
    with pixellate

    show mina11

    "Você está andando pelo parque, desfrutando da tranquilidade, quando avista uma garota aparentemente perdida."
    "Enquanto caminha pelo parque, você percebe uma jovem olhando em volta com uma expressão confusa."
    "Uma garota se aproxima, com um ar de preocupação"

    hide mina11
    show mina22
    with dissolve

    mina "Olá, desculpe incomodar, me chamo Mina, mas estou um pouco perdida. Você saberia me dizer como chegar à rua principal?"
    voce "Claro, eu posso te ajudar. Eu sou o %(nomeProtagonista)s." 
    mina "Acabei de me mudar para cá e estou tentando me familiarizar com a cidade."
    "Enquanto Mina olha ao redor, claramente desorientada, ela dá um passo em falso e tropeça em uma raiz exposta, caindo de forma desajeitada."
    mina "Ai, isso doeu..."
    "Você não entende como isso foi acontecer, mas com cuidado, você ajuda Mina a se sentar em um banco próximo, enquanto ela esfrega o tornozelo dolorido."
    "Ela da um sorriso forçado"
    mina "Desculpe, que situação vergonhosa. Eu não costumo ser tão desastrada..."
    "Você fala com um sorriso tranquilizador"
    voce "Não se preocupe, acidentes acontecem. Deixe-me ver se consigo encontrar algo para ajudar a aliviar a dor."
    "Com uma rápida busca, você encontra um pacote de gelo em um cooler abandonado por perto, improvisando um compressa para o tornozelo de Mina."
    "Enquanto conversam, você descobre que Mina é uma aspirante a artista, e ela revela que estava explorando o parque em busca de inspiração para suas pinturas."
    "Com o passar do tempo, a conversa flui naturalmente, e vocês compartilham histórias e risadas, transformando um momento desajeitado em um início de amizade inesperado."

    voce "Mina, eu posso te acompanhar até a rua principal, assim tenho certeza de que você chegará lá em segurança."
    "Mina olha para você, surpresa estampada em seu rosto."
    mina "Sério? Você faria isso por mim? Isso é muito gentil da sua parte."
    voce "Claro, não é problema. Além disso, seria uma ótima oportunidade para conhecer melhor a cidade."
    "Com um sorriso radiante, Mina aceita sua oferta e vocês começam a caminhar em direção à rua principal. Durante o trajeto, Mina compartilha mais sobre sua paixão pela arte e suas expectativas para a nova cidade."
    "Quando finalmente chegam à rua principal, Mina agradece calorosamente pela sua ajuda e se despede com um aceno, prometendo manter contato."

    hide mina22
    show mina21
    with dissolve
    
    menu:
        "Chamar ela para conhecer o Bairro":
            jump conhecerBairro
        "Volte para sua casa e vá comer bolachas":
            jump comerBolachas
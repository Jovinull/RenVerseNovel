label start:

    $ foiProCafe = False
    $ quantidadeCafe = 0
    $ nomeProtagonista = renpy.input("Então qual o seu nome?")
    if nomeProtagonista == "":
        $ nomeProtagonista = "Wander"

    play music "musics/awesomeness.mp3" fadein 1.5
    
    jump conhecerMina

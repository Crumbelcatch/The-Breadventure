
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(_("You"), color="#EAEAEA")
define h = Character(_("Tophat"), color="#EAEAEA")
define b = Character(_("Bow"), color="#EAEAEA")
define c = Character(_("Cone"), color="#EAEAEA")

define d = Character(_("Breadeamon"), color="#e50004")

define SPR_turnout = [("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")]



# The game starts here.
label start:

    scene bg lecturehall

    "test... TEST"

    $winsDeamon = 0
    $winsPlayer = 0

    m "Lets play scissors, paper, rock! I choose:"

    jump playSPR


label evalSPR:


    if (playerChoice, deamonChoice) in SPR_turnout:

        m "This Round goes to me!"

        $ winsPlayer = winsPlayer + 1

    elif (deamonChoice, playerChoice) in SPR_turnout:

        d "This one ges to me!"

        $ winsDeamon = winsDeamon + 1

    else:

        d "It's a tie!"

        m "Let's go again."


    if winsPlayer == 2:

        jump endingGood


    if winsDeamon == 2:

        jump endingBad

    jump playSPR



label playSPR:

    menu:

        m "I choose:"

        "Scissors":
            $ playerChoice = "Scissors"
        "Paper":
            $ playerChoice = "Paper"
        "Rock":
            $ playerChoice = "Rock"

    $ deamonChoice = renpy.random.choice(["Scissors", "Paper", "Rock"])

    d "I choose %(deamonChoice)s"

    jump evalSPR



label endingBad:

    scene bg_badEnding

    m "Aw hell naw..."

    "This is the bad ending."

    return


label endingGood:

    scene bg_goodEnding

    m "That was close..."

    "This is the good ending."

    return

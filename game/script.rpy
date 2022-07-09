
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character(_("You"), color="#EAEAEA")
define h = Character(_("Tophat"), color="#6f256a")
define b = Character(_("Bow"), color="#144694")
define c = Character(_("Cone"), color="#2cb700")
define f = Character(_("Cone's Friends"), color="#176000")

define d = Character(_("Breademon"), color="#e50004")

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


label endingRoomemate:

    scene bg_roommateEnding

    m "OMG, they were roommates"

    "This is the roommates ending."

    return


label endingNeutral:

    scene bg_neutralEnding

    m "¯\_(ツ)_/¯"

    "This is the neutral ending."

    return


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


# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    style.say_who_windowGray = Style ('say_who_window')
    style.say_who_windowGray.background = "#000000"


define m = Character(_("You"), color="#EAEAEA", what_color="#ffffff", window_background="gui/Custom__Name_Toast.png", window_ypos=0.5, window_xpos=0.5, window_bg_height=500, window_width=500)
define h = Character(_("Tophat"), color="#6f256a")
define b = Character(_("Bow"), color="#144694")
define c = Character(_("Cone"), color="#2cb700")
define f = Character(_("Cone's Friends"), color="#176000")

define r = Character(_("Everyone"), color="#6f256a")

define d = Character(_("Breademon"), color="#e50004")

define SPR_turnout = [("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")]



# The game starts here.
label start:


    jump endingDeamonWin


    scene bg lecturehall

    r "test... TEST"

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

        jump endingDeamonWin

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


label endingMcWin:

    scene bg_McWinEnding



    return


label endingDeamonWin:

    scene bg_badEnding

    show hugo nervoes at right

    c "Oh my gosh guys, I think they're coming back!"

    hide hugo

    show jerry neutral at right

    h "Quick, get them a glass of water!"

    show hugo neutral at right

    "Hugo storms off into the kitchen."

    b "Can you hear me??"

    m "Loud and clear!"

    c "Here you go, careful don't choke."

    m "Thanks, pal!"

    c "...Pal? You've never called me that before."

    m "Oh really? Why not...we're friends aren't we?"

    b "You've never said that to anyone..."

    h "Guys, I think we should let them rest, they look like they need it desperately. But good job everyone."

    m "Actually, I only need all the bread you currently have in this house."

    r "What?"

    return


label endingGood:

    scene bg_goodEnding

    m "That was close..."

    "This is the good ending."

    return

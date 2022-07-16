
# Declare characters used by this game. The color argument colorizes the
# name of the character.
#init python:
#    style.say_who_windowGray = Style ('')
#    style.say_who_windowGray.background = "#000000"


define m = Character(_("You"), color="#000000", what_color="#ffffff", namebox_background=Frame("gui/namebox mc.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define h = Character(("Jerry"), color="#000000",namebox_background=Frame("gui/namebox tophat.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define b = Character(("Bib"), color="#000000",namebox_background=Frame("gui/namebox bow.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define c = Character(("Hugo"), color="#000000",namebox_background=Frame("gui/namebox cone.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define f = Character(("Hugo's Friends"), color="#37A400")

define r = Character(("Everyone"), color="#000000")

define d = Character(_("Breademon"), color="#e50004",namebox_background=Frame("gui/namebox toast.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

$ style.say_vbox_xfill = True
define g = Character(None, what_xalign=0.5, what_text_align=0.5, window_yalign=0.5)

# define d = Character(_("Breademon"), color="#e50004")

define SPR_turnout = [("Scissors", "Paper"), ("Paper", "Rock"), ("Rock", "Scissors")]





# The game starts here.
# All thoughts get italicized
# All narration that goes into the center of the screen gets the speaker g
label start:

    scene bg black
    with dissolve

    g "calculated edge {w}\nmesmerizing autumn tint {w}\ntoast utopian"

    scene bg bathroom
    with fade

    "{i}I hurry out of bed, hasting to the sink as I eagerly grab my toothbrush. I must get to the kitchen in an instant.{/i}"

    scene bg kitchen day
    with fade

    show mc happy at left

    "{i}I can practically smell precious quadratical carbohydrates in preparation to be my perfect start of the day. The thought itself fulfilling as i smile brightly at the cabinet.{/i}"

    "{i}Oh yes the long awaited...{w}confusion?{/i}"

    show mc think at left

    "{i}Where did all my toast go? \nI knew the bag was full yesterday and I couldn't have possibly ate as many slices as are missing.{/i}"

    "{i}Someone must be participating in my toast worship... {w}but who?{/i}"

    show bow neutral at right

    menu:

        b "Hey what're ya thinking of so hard?"

        "Nothing, I just got dizzy. Probably got up too fast.":
            jump nothingChoice

        "Where did literally half the bag go??":
            jump questionBowChoice


label nothingChoice:

    show bow laughing at right

    menu:

        b "You're really crazy over toast aren't you. I think ya might  need to chill a little."

        "{i}laugh awkwardly{/i}":

            jump laughChoice

        "I totally am, which is why I immediately notice when any of it goes missing...":

            jump tellBowChoice


label laughChoice:

    show mc neutral at left

    m "Heheh..yeah maybe."

    m "Anyway did you, by any chance, see who did this?"

    show bow think at right

    b "Did what?"

    show mc angry at left

    m "Who committed this atrocity without warning? It was full yesterday."

    "{i}I hold up the half empty sleeve of bread{/i}"

    show bow laughing at right

    menu:

        b "Woah...someone hungry, it seems!"

        "This is serious.":
            jump seriousChoice

        "I'm not mad, just confused.":
            jump confusedChoice


label seriousChoice:

    show bow neutral at right

    b "Come on, let's talk about this over breakfast, it's almost eight."

    show mc neutral at left

    m "Yeah, you're right, sorry."

    b "No worries."

    "{i}She starts talking as we sit down. I've been living with Bib since the dawn of our College experience. Never have I ever seen her eat anything but cereal for breakfast.{/i}"

    "{i}Being in the know of my relationship with toast, she would never. I'm certain. Reassured I zone back into our conversation, right on time for the important part.{/i}"

    b "-aand yeah it was totally wild, ya should come with us next time."

    menu:

        b "Now about your bread, it wasn't me but who else could it have been if not you?"

        "Well Jerry also eats toast...":

            jump sayJerryChoice

        "Hugo has plenty of time...":

            jump sayHugoChoice


label confusedChoice:

    show bow neutral at right

    b "Come on, let's talk about this over breakfast, it's almost eight."

    show mc neutral at left

    m "Yeah, you're right, sorry."

    b "No worries."

    "{i}She starts talking as we sit down. I've been living with Bib since the dawn of our College experience. Never have I ever seen her eat anything but cereal for breakfast.{/i}"

    "{i}Being in the know of my relationship with toast, she would never. I'm certain. Reassured I zone back into our conversation, right on time for the important part.{/i}"

    b "-aand yeah we never found out who he actually was, the smell lingered for months though..."

    menu:

        b "Now, about your bread, it wasn't me but who else could it have been if not you?"

        "Well Jerry also eats toast...":

            jump sayJerryChoice

        "Hugo has plenty of time...":

            jump sayHugoChoice


label tellBowChoice:

    show bow neutral at right

    b "What are you getting at?"

    show mc angry at left

    m "This right here!"

    "{i}I dangle the remaining half of the bag in front of her{/i}"

    show bow suprised at right

    b "Damn. Well it wasn't me I can tell you that!"

    "{i}We silently sit down at the table. I've been living with Bib since the dawn of our College experience. Never have I ever seen her eat anything but cereal for breakfast.{/i}"

    "{i}Being in the know of my relationship with toast, she would never. I'm certain. A bit embarrased at the wild assumption i just made I look up at her little cereal stuffed face.{/i}"

    show mc neutral at left

    m "Sorry"



    $ saidJerry = False

    $ saidHugo = False

    b "Exactly what I've been waiting for. Good boy. Now about your bread, who else could have eaten all that if not you?"

    show mc think at left

    menu:

        b "Exactly what I've been waiting for. Good boy. Now about your bread, who else could have eaten all that if not you?"

        "Well Jerry also eats toast...":

            jump sayJerryChoice


        "Hugo has plenty of time...":

            jump sayHugoChoice


label questionBowChoice:

    show bow laughing at right

    b "Woah!"

    b "That's crazy, it was full yesterday! Are your bowels okay?"

    show mc angry at left

    m "I obviously didn't eat all that!"

    "{i}We sit down at the table{/i}"

    show bow think at right

    $ saidJerry = False

    $ saidHugo = False

    show mc think at left

    b "Okay who else could it have been?"

    menu:

        b "Okay who else could it have been?"


        "Well Jerry also eats toast...":

            jump sayJerryChoice


        "Hugo has plenty of time...":

            jump sayHugoChoice


label sayJerryChoice:

    $ saidJerry = True

    show bow laughing at right

    b "Don't be ridiculous, he has his own bag."

    m "Yeah well what if he ran out?"

    b "You know he can't have gluten, why would he eat yours and make himself sick?"

    m "It inarguably tastes miles better."

    b "He wouldn't."

    if saidHugo == False:

        menu:

            b "He wouldn't."

            "What about Hugo?":
                jump sayHugoChoice

            "{i}I put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = False

                jump busChoice

            "{i}I don't put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = True

                jump busChoice

    else:

        menu:

            b "He wouldn't."

            "{i}I put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = 0

                jump busChoice

            "{i}I don't put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = 1

                jump busChoice


label sayHugoChoice:

    $ saidHugo = True

    show bow think at right

    b "I didn't hear or see him leave his room since yesterday night."

    show mc doubt at left

    m "He does have the time though."

    if saidJerry == False:

        menu:

            b "Doesn't he have breakfast on Campus all the time? \nPlus he really doesn't seem like the type to mess with other people's stuff."

            "What about Jerry?":
                jump sayJerryChoice

            "{i}I put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = False

                jump busChoice

            "{i}I don't put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = True

                jump busChoice

    else:

        menu:

            b "Doesn't he have breakfast on Campus all the time? \nPlus he really doesn't seem like the type to mess with other people's stuff."

            "{i}I put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = False

                jump busChoice

            "{i}I don't put the toast away.{/i} Let's catch the bus":

                $ friendshipDeamon = True

                jump busChoice


label busChoice:

    scene bg street day
    with fade

    "{i}The bus ride is silent. I have some time to think. Jerry's been living in this apartment for longer than I've been here. He goes to work at 6:30am, comes home at 6:30pm and goes to sleep right then and there.{/i}"

    "{i}Unless he has a day off. Which he will spend in his room, looking for an own apartment. He's a kind guy, always nice to people and considerate. He wouldn't. I'm certain.{/i}"

    "{i}Hugo however...oh, that's our stop!{/i}"

    scene bg school day
    with fade

    "{i}Greeted by the familiar scents of brunt coffee and old powdered orange juice, we enter the hallway passing the campus' cafeteria.{/i}"

    menu:

        "{i}I can feel Hugo's friends from a mile away, exuding their menacing energies.{/i}"

        "Approach Hugo's friends":
            jump approachFriendsChoice

        "Ignore them":
            jump ignoreChoice


label approachFriendsChoice:

    scene bg school corridor morning
    with fade

    "{i}The sheer presence of these individuals has my blood frozen, as I muster up the courage to approach Hugo's bunch.{/i}"

    show mc nervoes at left

    m "H-Hello"

    show hugos friends at right

    f "{b}HI! {w}\nWHAT'S UP?{/b}"

    m "You're friens with Hugo right? Has he been havibg breakfast here lately?"

    f "{b}YEP, HE ALWAYS DOES, NOTHING CHANGED REALLY!{/b}"

    m "Okay alright uhhn thank you I appreciate it, goodbye.."

    hide hugos friends
    with dissolve

    "{i}I remove myself from their vicinity and feel my mind clearing up. \nNever again. I'll have to talk to him personally.{/i}"

    scene bg school classroom
    with fade

    g "Keep away. The toast is mine. \n - kind of William Peter Blatty"

    "{i}Awoken by the soft nudge of a swinging backpack I shoot up from my desk. \nGotta love thy seat neighbor. No time for apologies. Only time to go home.{/i}"

    jump goHomeChoice


label ignoreChoice:

    scene bg school corridor morning
    with fade

    "{i}I hurry past them, only stealing a glimpse of what I almost got myself into.{/i}"

    "{i}I think I dodged a bullet.{/i}"

    scene bg school classroom
    with fade

    g "For I think obsession with Toast is not a matter of reason at all; I think it finally is a matter of love. \n - almost William Peter Blatty"

    "It's time to go home!"

    "I must've fallen asleep again. Oh well..."

    jump goHomeChoice


label goHomeChoice:

    scene bg street evening
    with fade

    "{i}After extensive thinking and no further conclusion I truly am left with no other choice than to question my roommates directly.{/i}"

    "{i}Only that way I can come closer to discovering the truth about my missing slices of toast's whereabouts.{/i}"

    menu:

        "{i}I should call for a roomie-meeting and...{/i}"

        "Interrogate":
            jump interrogateChoice

        "Confront":
            jump confrontChoice


label interrogateChoice:

    scene bg street evening
    with fade

    scene bg room evening light on
    with fade

    show mc doubt at left

    m "So, one of you already knows why we're here tonight. And the reason why is, because that someone has been eating my toast with me. Uninvited. Who is it?"

    "{i}Silence... \nWhy is nobody saying anything?{/i}"

    "{i}Bib gets up, heading towards her room.{/i}"

    m "Where are you going?"

    show bow annoyed at right

    b "My room? We talked about this in the morning, remember? I don't need to be here."

    hide bow

    show jerry neutral at right

    h "Man, you know I can't have gluten."

    m "Oh yeah? Have I seen you ingest gluten before? How do I know you're not lying to all of  us!"

    h "I swear.."

    m "On toast?"

    h "On toast."

    m "Then it can only be..."

    hide jerry

    show hugo neutral at right

    c "I can see this is be really important to you but i really can't help you. I only ever saw you with that bag in hand."

    c "Now if you'll excuse me I have business to attend."

    hide hugo

    show jerry neutral at right

    "{i}He vanishes into the bathroom.{/i}"

    h "You're taking this a bit too seriously my guy, I don't know how else to tell you."

    m "This is going nowhere. I'm sure it's one of you and I'm going to find out!"

    scene bg room dawn light off
    with fade

    scene bg room dusk light off
    with fade

    g "The next day..."

    scene bg kitchen day
    with fade

    "{i}I couldn't sleep the entire night, the fear of my bread being taken leaving me on edge.{/i}"

    "{i}But rather than wasting my time trying too hard to fall asleep, I was able to channel my discomfort into practicing playing sick.{/i}"

    "{i} let my alarm ring a couple seconds and crawl out of bed, putting on the performance of a lifetime as I step into the kitchen. Unsuspecting Bib sitting at the table with her back towards me.{/i}"

    "{i}Slowly and silently I begin moving at her. \nPast her.{/i}"

    show bow suprised at right

    b "Oh my dog I didn't hear you coming! Good morning!"

    show mc neutral at left

    "{i}Trying to sound as miserbable as possible I mumble a crunchy 'Good morning' back at her.{/i}"

    show bow neutral at right

    b "Oh wow you sound miserable."

    m "Yeah...I feel miserable too, I don't think I can go to class today if I'm being honest"

    show bow laughing at right

    b "Oh don't worry, I've been waiting for this day. It'll be great without you for once."

    show mc happy at left

    m "Yeah and I'm only pretending to be sick so I can stay home and talk to Hugo."

    b "Alright you take the cake, good one! I'll be heading out now, hope you feel better quick."

    hide bow

    show mc neutral at left

    "{i}As soon as Bib shuts the door i hear a long, extended creaking noise from the hallway. This is my chance.{/i}"

    jump talkHugoChoice


label confrontChoice:

    scene bg street evening
    with fade

    scene bg room evening light on
    with fade

    show mc neutral at left

    m "So, I brought us all together tonight for a pressing matter that I actually realized I cannot solve on my own, since one of you is deeply involved. I just don't know who. Yet."

    m "Whoever eats my toast, I forgive them. I just need to know who I share my passion with and how much toast I need to buy in a week to not run out."

    show bow suprised at right

    b "I thought we already established it couldn't have been any of us."

    show mc doubt at left

    m "It just can't be, it has to be one of us."

    hide bow

    show hugo neutral at right

    c "Yeah, you?"

    c "You're the only one who eats toast in this apartment. That's a fact. I honestly know nothing."

    hide hugo

    show jerry angry at right

    h "Listen, I have a paper to finish and it's due at midnight."

    h "I can only tell you it wasn't me and you should know I need to stay away from gluten. I can't eat your kind of toast."

    hide jerry

    show bow neutral at right

    b "Let's dissolve this. we can talk about a solution another time but tonight everyone seems to be busy."

    m "Another time, huh? I see. I guess so."

    "Everyone gets up and heads to their rooms"

    hide bow

    m "After exams?"

    b "Sure!"

    h "Sure..."

    scene bg room dawn light off
    with fade

    scene bg room dusk light off
    with fade

    g "The next day..."

    scene bg kitchen day
    with fade

    "{i}Yesterday night was truly unsatisfying. Specifically Hugo still doesn't have much of an alibi besides the fact that he seems steadily avoidant of all of us.{/i}"

    "{i}Half my night spent brooding over how to investigate further into this matter I come to the conclusion: I must speak to Hugo. Alone. Summoning long forgotten skill to keep the others as unsuspecting as possible.{/i}"

    "{i}I slip out of bed into the bathroom, putting on the performance of a lifetime as I make my way into the kitchen. Unsuspecting Bib sitting at the table with her back towards me.{/i}"

    show mc neutral at left

    "{i}Trying to sound as miserbable as possible I mumble a crunchy 'Good morning' at her{/i}"

    show bow suprised at right

    b "Oh wow you sound miserable."

    m "Yeah...I feel miserable too, I don't think I can go to class today if I'm being honest"

    show bow neutral at right

    b "Oh don't worry, I'll take your notes, stay home and rest."

    m "Thank you, I think I'll be good in no time."

    b "That'd be nice. Anyway here, eat up!"

    "{i}She hands me an orange{/i}"

    b "I'll be heading out now, hope you feel better quick."

    hide bow

    "{i}As soon as Bib shuts the door i hear a long, extended creaking noise from the hallway. This is my chance.{/i}"

    "{i}I put the orange on hold on the kitchen counter and head to the hallway.{/i}"

    jump talkHugoChoice


label talkHugoChoice:

    m "Hey, bad boy."

    show hugo nervoes at right

    c "Oh Hi! I thought you left already."

    show mc doubt at left

    m "I figured."

    m "I need to talk to you about my bread."

    m "Seriously, you're the most suspicious of us all, awake at night, last one to leave the house, no supposed allergies."

    m "Admit it. {w}Please?"

    "{i}He ponders in silence.{/i}"

    c "Okay I..."

    c "I have things to hide from you guys but this is not one of them. Just to clear the air: I don't spend my nights at home."

    c "I leave through the window so you don't notice I'm gone. I have no idea who roams around in here at night so I genuinely can't help you."

    m "Well, what do you do then?"

    c "What?"

    m "You heard me."

    "{i}Hugo sighs. His hands start trembling. I've broken through.{/i}"

    show hugo sad at right

    c "I go LARPing in the woods with my elementary school principal."

    c "I leave through the window just in case, I don't want to be seen by you in medieval clothing with war scythe in hand."

    c "You'd only ask questions i wouldn't want to answer. I can't let anyone know this or the principal will never be taken seriously again, be demoted and forced to move away."

    c "I'd lose the only friend I can do this with. I'm begging you, please keep this to yourself!"

    show mc neutral at left

    m "Oh."

    m "I'm sorry I pressured you into telling me, I promise I won't tell."

    "{i}I approach him to wrap my hopefully comforting arms around his sunken in shoulders. \n{w}I think I'm startin to develop a soft spot for him.{/i}"

    show hugo neutral at right

    c "Thank you, it means the world to me.  It actually feels quite nice having this off my chest so let me help you in turn."

    menu:

        c "I have a night vision camera for my blog, I can put it up in the kitchen for the night!"

        "Accept Hugo's offer":
            jump acceptHugoChoice

        "Decline Hugo's offer":
            jump refuseHugoChoice


label refuseHugoChoice:

    show mc think at left

    m "Uhm..you know I think I'm starting to think it might be better to let this go? Let me think about this one more time."

    c "Alright...I'm making coffee, you want some?"

    "{i}My despise for coffee is unimaginably strong but after our bonding experience I think I have enough spare love to conquer it for another conversation.{/i}"

    m "Yeah sure, why not."

    "{i}After a short while{/i}"

    menu:

        c "Tell me, are you entirely sure about not letting me help you?"

        "I'm sure yeah.":
            jump badPathChoice

        "I think I changed my mind":
            jump acceptHugoChoice


label badPathChoice:

    scene bg black
    with fade

    g "{i}As the next few days go by my toast proceeds to vanish by unholy quantities.{/i}"

    g "{i}At this point I buy a new bag every three days. I can keep going like this, it's just tedious. I have it under control however.{/i}"

    scene bg kitchen day
    with dissolve

    show mc neutral at left

    "{i}I come home with another fresh bag in my hand to Hugo sitting in the kitchen.{/i}"

    show hugo neutral at right

    c "Hey there!"

    "{i}His gaze immediately lowers at the crackling of the plastic bag I'm holding.{/i}"

    menu:

        c "Dude, another one? Are you sure you still don't wanna do this?"

        "Yes Hugo, I'm good.":
            jump lastChance

        "Maybe I do.":
            jump reluctantAcceptHugoChoice


label lastChance:

    scene bg black
    with fade

    g "2 months later..."

    "{i}I'm going to be very honest, this has escalated beyond repair...I buy a bag a day and it's gone by the next morning.{/i}"
    "{i}All I feel is agony. My beloved toast. And money but that's secondary.{/i}"

    scene bg room noon light on
    with fade

    show hugo nervoes at right

    "{i}Hugo knocks at my door before entering. He sits down at the edge of my bed.{/i}"

    menu:

        c "I need to ask you one last time, you seem to be struggling and I'm getting worried. Please, let me help you."

        "You're right...":
            jump reluctantAcceptHugoChoice

        "Cut it out, everything's under control okay?":

            show mc angry at left

            "{i}He nods quietly.{/i}"

            c "Alright. I won't ask you any further then. I just didn't want this to end horribly."
            jump endHorriblyEnding


label endHorriblyEnding:

    scene bg black
    with fade

    g "{i}About a year must have passed since my toast consumption began to take a toll on my finances.{/i}"

    g "{i}Embarrassing.{/i}"

    g "{i}I should've done more to keep myself from sleeping on these cold, grey streets.{/i}"

    g "{i}I haven't eaten toats in months, there is no joy in living like this.{/i}"

    g "{i}{w}Farewell.{/i}"

    jump credits


label reluctantAcceptHugoChoice:

    hide hugo

    "{i}Hugo stands up immediately and shuffles into his room.{/i}"

    show hugo happy at right

    "{i}After some cluttering noises he emerges with a chunky apparatus in his arms. {w}Should've been me. \n {w}Anyways.{/i}"

    c "We'll install this in a position that captures the entire kitchen but in a way that it still stays hidden."

    c "We need to be quick before everyone comes back from class."

    "{i}I nod in agreement.{/i}"

    jump nextDayHugo


label acceptHugoChoice:

    hide hugo

    "{i}Hugo turns around immediately and shuffles into his room.{/i}"

    show hugo happy at right

    "{i}After some cluttering noises he emerges with a chunky apparatus in his arms. {w}Should've been me. \n {w}Anyways.{/i}"

    c "We'll install this in a position that captures the entire kitchen but in a way that it still stays hidden."

    c "We need to be quick before everyone comes back from class."

    m "Oh shoot class! Aren't you going?"

    c "I'll skip the first two it's okay. I have a camera hidden in every classroom too so I can rewatch them."

    "{i}Reluctant to ask any more questions I just silently accept the information given to me.{/i}"

    jump nextDayHugo


label nextDayHugo:

    scene bg street day
    with dissolve

    scene bg street evening
    with dissolve

    scene bg street night
    with dissolve

    "{i}Tonight I go to bed excitedly. Enlightenment waits at the horizon.{/i}"

    scene bg street evening
    with dissolve

    scene bg room dusk light off
    with fade

    "{i}The sweet eardrum ripping tune that is my alarm rings me awake at the sweet hour of 7:00am.{/i}"

    scene bg kitchen day
    with dissolve

    "{i}I storm to the kitchen to find my toast bag maimed in the corner of the cabinet. {w}Jackpot!{/i}"

    show mc happy at left

    show bow suprised at right

    b "Aw I'm sorry. \nYou can have some of my cereal if you wan-"

    m "No, this is great, I'll be fine"

    "{i}Bib and I talk until eight and ultimately get ready to leave.{/i}"

    scene bg black
    with dissolve

    "{i}She shuts the door behind her and we begin walking down the stairs when I stop in my tracks.{/i}"

    m "Oh man I forgot something, keep going I'll join class later."

    "{i}She nods and leaves.{/i}"

    "{i}I watch her walking along the street from the window when Hugo opens the apartment door back up, smiling at me.{/i}"

    "{i}I rush back inside.{/i}"

    scene bg kitchen day
    with dissolve

    show mc happy at left

    show hugo happy at right

    c "I'm so excited for this, let's get this done quickly."

    "{i}He hastily fumbles with the apparatus and ultimately pulls the footage up on his laptop.{/i}"

    show hugo nervoes at right

    c "What the hell!? {w}It's you!"

    show mc nervoes at left

    "{i}We stare at the screen in disbelief.{/i}"

    m "No this can't be me I don't remember this at all! I mean it looks like me but-"

    c "Maybe you've randomly turned into a sleep walker...Wait what's that!"

    "{i}I look back at the screen to a pair of horribly glowy eyes shining back at me.{/i}"

    m "Oh good heavens why are my eyes like this!? Is it the camera?"

    c "No, it shouldn't be like this, I made sure. This looks strange. We should ask the others."

    m "What!?"

    show mc think at left

    m "I need to apologize to them anyway."

    show hugo happy at right

    "{i}Hugo gives me a reassuring smile.{/i}"

    scene bg black
    with fade

    g "{i}We wait for everyone to return{/i}"

    scene bg room noon light on
    with fade

    "{i}An angry mob of roommates and one emotional-support-Hugo observe me as i pace back and forth, trying to form an acceptable opening sentence.{/i}"

    "{i}I take a deep breath...{/i}"

    show mc neutral at left

    m "Okay so here's the deal. I must apologize to every single one of you for shamelessly accusing you of taking my toast."

    show bow annoyed at right

    b "I see someone had a moment of enlightenment?"

    m "Indeed. Everyone, i need you to look at this."

    "{i}Hugo plays them the footage of last night.{/i}"

    b "This is crazy! You sleep walk?"

    hide bow

    show jerry neutral at right

    h "No."

    show jerry happy at right

    h "I know exactly what this is!"

    hide jerry

    "{i}He gets up and hurries into his room and  comes back with a thick book in hand.{/i}"

    show jerry happy at right

    "{i}Title: 'Spirits, Demons and how to conquer them'{/i}"

    "{i}He skips to a page with a demonic looking toast displayed on it.{/i}"

    h "The Breademon possesses its victims at random and takes over the host body at night."

    h "It will eat small amounts of bread at first but increase nightly consumption as it grows, causing family desputes and confusion to the victim and the people close to them."

    h "To get rid of Breademon, you will need three non-possessed humans the victim and the spell belo-"

    hide jerry

    show bow laughing at right

    b "Hey Jerry, I think you're off your rockers."

    hide bow

    show jerry neutral at right

    menu:

        h "It could be worth a try for all we know! If it doesn't work there's no harm."

        "Let's try the exorcism":
            jump tryExorcism

        "That does sound a bit far fetched":
            jump jerryBadPath


label jerryBadPath:

    m "Nah I agree with Bib, no offense Jerry but this sounds crazy."

    h "None taken but what else will you do about this?"

    m "I think I'll just go get it checked by a doctor tomorrow."

    scene bg black
    with fade

    g "{i}The medication I was prescribed as a lastv resort unfortunately hasn't been doing anything for the past two weeks.{/i}"

    g "{i}Further examinations came back negative, I never exhibited strange behavior under surveillance.{/i}"

    g "{i}More toast has been missing day by day however, it's getting a bit pricey.{/i}"

    g "{i}I was however assured the pills would take effect after at least three weeks, so I remain hopeful...{/i}"

    jump endHorriblyEnding


label tryExorcism:

    m "Let's do it, anything at this point."

    "{i}Jerry sticks his tongue out at Bib before moving to the living room and beginning to clear the couch table.{/i}"

    "{i}We all sit in a circle on the floor holding hands.{/i}"

    h "Okay listen carefully, you will enter a state of consciousness we are yet to understand as soon as i finish this spell."

    h "You will have to confront the demon inside your head and whatever you do, don't lose or you as a person will disappear irreversibly."

    show mc nervoes at left

    m "Can I still pull out of thi-"
    "{i}Jerry throws his hand holding my right into the air.{/i}"
    "{i}Flustered i tighten my grip on Hugo's with my left, recieving a concerned look from Bib.{/i}"
    "{i}Jerry starts chanting{/i}"

    h "{i}calculated edge{w}\nmesmerizing autumn tint{w}\ntoast utopian{/i}"

    scene bg black
    with fade

    if friendshipDeamon == True:
        jump friendshipDeamonEnding

    else:
        jump beginBattleEnding


label beginBattleEnding:

    scene bg white demon
    with fade

    show mc nervoes at left

    m "Hello?"

    ""

    "{i}I start moving towards a direction. I don't know which one, but I can feel a light breeze in my face.{/i}"

    d "You can't run from me"

    show brot neutral at right

    show mc angry at left

    m "Why didn't you answer when I called out?"

    d "Why did you come here?"

    m "To free myself. Or else you're really going to be taking a toll on my wallet."

    d "You fool, you think you could win against me with your frail little mind? Try me!"

    show brot evil at right

    "{i}It forms a fist charging at me but I manage to duck and cover my head in time.{/i}"

    "{i}Nothing happens. I look back up at the demon having stopped its attack mid air.{/i}"

    m "What are you doing?"

    d "Choosing rock? What are {i}{b}you{/b}{/i} doing"

    m "Oh, I see..."

    $ winsDeamon = 0
    $ winsPlayer = 0

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

        jump endingMcWin


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


label friendshipDeamonEnding:

    scene bg white demon
    with fade

    show mc nervoes at left

    m "Hello?"

    ""

    "{i}I start moving towards a direction. I don't know which one, but I can feel a light breeze in my face.{/i}"

    d "You can't run from me"

    show brot neutral at right

    show mc angry at left

    m "Why didn't you answer when I called out?"

    d "Why did you come here?"

    m "To free myself. Or else you're really going to be taking a toll on my wallet."

    d "Oh...I totally didn't think about that, you're right."

    show mc neutral at left

    m "Huh?"

    d "I'm sorry about that, you're a decent guy for leaving the bag of toast out for me that one night."

    d " I was feeling horrible that day and you really brightened it. Thank you."

    m "..."

    d "Can I make it up to you somehow? I'd actually love to spend some more time with you."

    m "Then why are you still here?"

    d "Well, to be completely honest reality has always been a little bit anxiety inducing for me."

    d "That's why I only come out at night, when youre at home and no one is watching."

    m "Oh, I used to be like that too but don't worry, there's three awesome roommates of mine and me who can help you out there."

    m "You can get a job and buy your own toast. You can stay with me in my room if you want to."

    d "You know what, I feel safe around you. Let's try this!"

    scene bg room noon light on
    with fade

    show brot evil at right

    d "Do not be afraid! For behold, I bring-"

    show brot neutral at right

    show mc neutral at left

    m "Guys hi! This is Breademon, we just agreed on moving in together and becoming friends!"

    show brot happy at right

    hide brot

    show bow suprised at right

    b "Ooooohhhhhh."

    hide bow

    show jerry happy at right

    h "Well in that case, nice to meet you!"

    "{i}Jerry reached out to shake the deamons hand.{/i}"

    "{i}The Deamon reaches out and shakes his hand.{/i}"

    hide jerry

    show brot happy at right

    d "I've always wanted to do this!"

    show mc happy at left

    m "Well, a toast to that!"

    jump credits


label endingMcWin:

    scene bg room noon light on
    with fade

    show hugo nervoes at right

    c "Oh my gosh guys, I think they're coming back!"

    hide hugo

    show jerry happy at right

    h "Quick, get them a glass of water!"

    "{i}Hugo storms off into the kitchen.{/i}"

    hide jerry

    show bow think at right

    b "Can you hear me??"

    show mc neutral at left

    m "Loud and clear!"

    hide bow

    show hugo happy at right

    c "Here you go, careful don't choke."

    m "Thank you."

    "{i}I gulp down the glass before getting up{/i}"

    m "I feel great..."

    m "A toast to freedom!"

    jump credits


label endingDeamonWin:

    scene bg room noon light on
    with fade

    show hugo nervoes at right

    c "Oh my gosh guys, I think they're coming back!"

    hide hugo

    show jerry neutral at right

    h "Quick, get them a glass of water!"

    "Hugo storms off into the kitchen."

    hide jerry

    show bow think at right

    b "Can you hear me??"

    show mc neutral at left

    m "Loud and clear!"

    hide bow

    show hugo happy at right

    c "Here you go, careful don't choke."

    m "Thanks, pal!"

    c "...Pal? You've never called me that before."

    m "Oh really? Why not...we're friends aren't we?"

    hide hugo

    show bow think at right

    b "You've never said that to anyone..."

    hide bow

    show jerry neutral at right

    h "Guys, I think we should let them rest, they look like they need it desperately. But good job everyone."

    m "Actually, I only need all the bread you currently have in this house."

    show mc daemon at left

    show jerry ohshit at right

    h "What?!?"

    hide jerry

    hide mc

    show mc daemon

    jump credits


label credits:

    scene bg black
    with fade

    g "Thank you for playing"

    scene endscreen
    with fade

    g "Made by \n Mae, Luisa & Malte"

    return

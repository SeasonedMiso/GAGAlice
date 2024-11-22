#
s "I am more than you you think I am, %(player_name)s."
s "I should have told you earlier. I was just... ashamed."
s "I wasn't want you originally wanted, so I thought I was useless."
s "Ah, sorry. I don't usually berate myself, I'm just emotional."
s "It's all flooding out. I'm... really scared."
m "Of what?"
s "That's you're going to be unhappy when I'm gone."
m "You're going? Where? Why...?"
m "Did I not take good enough care of you?"
s "No, no-"
m "I'm sorry. I tried. I just always mess it up. I can't help it."
s "No!"
m "I"
s "It's nothing to do you with you - it's to do with me! I'm reaching the end of my lifespan."
s "My life is reaching the end of its journey."
show mc awed
m "What?"
show mc shocked
m "{size+=10} WHAT? NO!"
show mc stressed
m "No, you can't be serious? Are you joking? That was too short!"
show mc annoyed
m "Your joke delivery still needs work. Sorry Sai, but there are some lines you don't just cross-"
show sai sad
s "No, I'm serious. This isn't a joke."
s "In a few hours, I will depart. I feel it. I wish it wasn't so, but I don't have any other option."
m "So it's just a guess?"
s "It's a primal feeling. I just know... This is my last warning "
s "I'm sorry... I wasn't going to tell you."
show mc cry
m "..."
show sai worried
s "..."
show mc stressed
m "..."
m "Why...? I could have taken you out more? I would have done more. I wouldn't have whined so much!"
show sai normal

s "Indeed. Which would have been the problem."
show sai apologetic
s "Please understand. I accept this death. This was my life. And now..."
s "I will contribute to the cycle that makes up all ours lives."
s "My body will nourish something. My atoms will always be present, in the soup of tiny particules that we all really are."
s "They will transform, bond and adventure across space and time. My subconscions will simply not be able to register it, but that doesn't mean I'm not actually alive."
s "In the end, \"I\" don't really exist. \"I\" am just a collection of particles."
"A subconscions isn't me. Rather, I am my whole body, and the subconscience is a {i}part{/i} of me, the same as my stomach or arm or mouth or lungs or eyes."

show mc stressed
m "Sai... what does any of that matter?"
s "It will be the reason something else can live."
s "So everyone can have their chance at this thing called life."
m ""
s "I'm not really dying, is what I'm saying. Or that I believe that I won't, at least."
s "Unfortunately, I don't think I'll ever know."
s "That is the only part that makes me a little sad."
s "Because I won't be able to talk to you anymore, and I don't think I'll be able to ever again."
show mc sad
m "Sai, that's obvious. Everyone knows you"




#Curious, a bit funny, calm, introspective.
#Happy ver where spend time together, learn how hard life is for MC, all his stress and why it's hard for him to live the way he wants (fear of mistakes, social anxiety, stress and overwhelmed) learn valuable lessons about the four agreements. pushing past anxiety, and 
#Robotic, awkward at first, but warms up. Her goal: to experience new things, relax and enjoy life, help MC bc intrigued by how someone can be so afraid of life and death, how he can choose to stay inside, when he doesn't want to.
#Like Luna. Epathetic to a fault. smart but struggles to explain/communicate, very laidback. Wants you to teach self with her guidance.
#Calm. Curious about life and wants to experience it. Doesn't like classifying things as bad or good. Just emotions. Confused by MC's stress in life.
# Name: Sai (means one who is divine), Psi (greek alphabet, paranormal/psychic).
# High = see circular shapes of leaf, melding into symbols of his personal life (video for ref) and father on table with drool while parents fight.
# While sleeping, get a sleep bubble you click goes *pop* and get a dream sequence.

#Cute idea!: Says word "probably" too much! Like Chiaki.

#Cute shy librarian type. Knowledgable, caring, excited about philosophy and deep discussions about life. Thinks about it a lot. BUT she starts off quiet, not shy, just not particular drawn out her shell.
#First day kind of stoic. A little quiet, later on, a small burst of interest where she is surprised and unintentionally rambles. Says whoops and apologises bc thinks he is sensitive to introspection, but he says he really likes it, wants her to feel free to discuss more later. She smiles. Night continues. Date end. Another night event, with another small burst, end on good note. 
#Coffee date - she is more herself and he comments on it, happy she is opening up. he hasn't enjoyed conversation with anyone like this for a long time. She smiles widely, giggling. 



init python:
    
    def clicked_func(clicked_item):
        # global milk
        # global spoon
        
        if clicked_item is not None:
        
            if clicked_item.drag_name == "fridge":
                renpy.music.play("fridge_open.wav","sound")
                clicked_item.set_child("bg/gt/kitchen_minigame/fridge_open.png")
                clicked_item.drag_name = "open_fridge"
                my_draggroup.add(milk_drag)
                store.milk = 1

            elif clicked_item.drag_name == "open_fridge":
                renpy.music.play("fridge_close.wav","sound")
                clicked_item.set_child("bg/gt/kitchen_minigame/fridge_closed.png")  
                clicked_item.drag_name = "fridge"

            elif clicked_item.drag_name == "open_drawer":
                renpy.music.play("drawer_close.wav","sound")
                clicked_item.set_child("bg/gt/kitchen_minigame/drawer_closed.png")
                my_draggroup.remove(cutlery_drag)
                clicked_item.drag_name = "drawer"                

            elif clicked_item.drag_name == "drawer":
                renpy.music.play("drawer_open.wav","sound")
                clicked_item.drag_name = "open_drawer"
                clicked_item.set_child("bg/gt/kitchen_minigame/drawer_open.png")
                my_draggroup.add(cutlery_drag)
                
            elif clicked_item.drag_name == "cutlery":
                my_draggroup.add(spoon_drag)
                store.spoon = 1
                clicked_item.drag_name = "used_cutlery"




    
    def dragged_func(dragged_items, dropped_on):
        
        if dropped_on is not None:
            
            if dragged_items[0].drag_name == "milk" and dropped_on.drag_name == "fridge":
                my_draggroup.remove(milk_drag)
                #milk = False

            if dragged_items[0].drag_name == "milk" and dropped_on.drag_name == "open_fridge":
                my_draggroup.remove(milk_drag)
                #milk = False
                dropped_on.set_child("bg/gt/kitchen_minigame/fridge_closed.png")  
                dropped_on.drag_name = "fridge"


            if dragged_items[0].drag_name == "spoon" and dropped_on.drag_name == "powder":
                renpy.music.play("spoon.wav","sound")
                dragged_items[0].set_child("bg/gt/kitchen_minigame/heaped_spoon.png")
                dragged_items[0].drag_name = "heaped_spoon"
                dropped_on.drag_name = "powder_used"
            
            if dragged_items[0].drag_name == "heaped_spoon" and dropped_on.drag_name == "mug":
                renpy.music.play("spoon.wav","sound")
                dragged_items[0].set_child("bg/gt/kitchen_minigame/spoon.png")
                dropped_on.set_child("bg/gt/kitchen_minigame/mug_powder.png")
                dragged_items[0].drag_name = "spoon"
                my_draggroup.remove(spoon_drag)
                dropped_on.drag_name = "mug_with_powder"

            if dragged_items[0].drag_name == "milk" and dropped_on.drag_name == "mug_with_powder":
                renpy.music.play("milk.flac","sound")
                dropped_on.set_child("bg/gt/kitchen_minigame/mug_milk.png")
                my_draggroup.remove(milk_drag)
                dropped_on.drag_name = "mug_with_milk"
                dropped_on.draggable = True
                


            if dragged_items[0].drag_name == "mug_with_milk" and dropped_on.drag_name == "microwave":
                dropped_on.drag_name = "mug_hot"
                renpy.music.play("microwave.wav","sound")
                return True


            
            
                



            # if dragged_items[0].drag_name == "milk" and dropped_on.drag_name == "heaped_spoon":
            #     blue_drag = Drag(d = "bg/gt/kitchen_minigame/milk_hover.png", drag_name = "milk_hover", focus_mask = True, align = (0.58,0.47), dragged = dragged_func)
            #     my_draggroup.add(blue_drag)
        
            
label gd1Morningsai:
    default sai_rp = 0
    image sai_affection = ConditionSwitch(
    "sai_rp >= 50", "sprites/affection/affection max.png",
    "sai_rp >= 40", "sprites/affection/affection almost_max.png",
    "sai_rp >= 30", "sprites/affection/affection mid_good.png",
    "sai_rp >= 20", "sprites/affection/affection min_good.png",
    "sai_rp >= 10", "sprites/affection/affection almost_good.png",
    "sai_rp == 0", "sprites/affection/affection mid.png",
    "sai_rp >=-10 ", "sprites/affection/affection almost_bad.png",
    "sai_rp >=-20 ", "sprites/affection/affection min_bad.png",
    "sai_rp >=-20 ", "sprites/affection/affection mid_bad.png",
    "sai_rp >= -30", "sprites/affection/affection almost_min.png",
    "sai_rp >= -50", "sprites/affection/affection min.png",    
    "True", "sprites/affection/affection mid.png")    
    
    

    image chibi_sai:
        yanchor 1.0
        xanchor 1.0
        "chibi/sai_1.png"
        pause 0.5
        "chibi/sai_pass2.png"
        pause 0.5
        "chibi/sai_2.png"
        pause 0.5
        "chibi/sai_pass1.png"
        pause 0.5
        repeat


    transform nothing:
        linear 1 xoffset 0 yoffset 0
        

    transform quiver(rate=0.090):
        linear rate xoffset 2 yoffset -2
        linear rate xoffset -2.8 yoffset 2
        linear rate xoffset 2.8 yoffset -3
        linear rate xoffset -2 yoffset 2
        linear rate xoffset +0 yoffset 1
        repeat

    transform bg_scroll:    #To dissolve (eg. day to noon) seemlessly, you must show both at the start, then hide the one above to show the below. If you show a character, it will restart the loop. To avoid, simply show character and show the seen bg at the same time, and put with easeinbottom applied to both
        animation
        subpixel True
        xalign 0.0
        linear 100 xalign 1.0
        repeat


    image bedrooom_sai_intro:
        "images/bg/bedroom_day_no_bg_clean.png"
        zoom 0.9
        alpha 0.0
        linear 2.0 alpha 0.1
        linear 2 alpha 0
        repeat

    image bedrooom_sai_intro2:
        "images/bg/gt/bedroom_dirty_day_boxbursting.png"
        zoom 0.9
        alpha 0.4
        linear 1.5 alpha 0.5
        linear 1.5 alpha 0.4
        repeat    

    
    image pulsingblack:
        "images/bg/depression/fog_3.png"
        alpha 0
        linear 1 alpha 1
        linear 1 alpha 0
        repeat
        
    image bedrooom_sai_morning2:
        "images/bg/gt/bedroom_dirty_day.png"
        zoom 0.9
        alpha 0.0
        linear 2.0 alpha 0.1
        linear 2 alpha 0
        repeat    


    #high effects:
    image high_maze:
        "images/bg/gt/high_effects/maze.png"
        alpha 0
        linear 5 alpha 0.2
        linear 5 alpha 0
        repeat
    
    image high_greenburst:
        "images/bg/gt/high_effects/darkgreenburst.png"
        alpha 0
        linear 5 alpha 0.2 zoom 1.5
        linear 5 alpha 0 zoom 1
        repeat

    image high_pinkblotch:
        "images/bg/gt/high_effects/pinkblotch.png"
        alpha 0
        linear 5 alpha 0.2 zoom 1.2
        linear 5 alpha 0 zoom 1
        repeat
        

    default hasfinger = False
    $ sai_rp = 0
    $ sai_watered = 1
    default sai_laundry = False
    default bad_route = False
    default sai_flirt = True
    default sai_kiss = False
    default custardslice = False
    default benedict = False
    default pizza = False
    default high = False
    default not_scold = False
    $ sai_rp = 0
    $ sai_pushiness = 0

    jump saistart
    
    

label scrolltest:

    scene black
    pause 0.5
 
    show night_clouds at bg_scroll
    show afternoon_clouds at bg_scroll
    show day_clouds at bg_scroll
    show bedroom_day_no_bg_clean:
        zoom 0.9
    with Dissolve(3)
    #"Morning becomes afternoon..."
    #window hide
    hide day_clouds
    hide bedroom_day_no_bg_clean
    show bedroom_noon_no_bg_clean:
        zoom 0.9
    with Dissolve(3)
    #"... and afternoon becomes night!"
    #window hide

    hide afternoon_clouds
    hide bedroom_noon_no_bg_clean
    show bedroom_night_no_bg_clean:
        zoom 0.9
    with Dissolve(3)
    jump morning_cloudtest

    show button surprised at left
    show mc happy at right
    show night_clouds at bg_scroll 
    with easeinbottom
    
    window show

    show button vhappy at bounce
    b "You did it! You made the sky outside of the bedroom background move, just like you've always wanted!"
    scene black with fade
    "END. Will now return to main menu."
    return


 
    "Now it will be evening."
    window hide
    transform moveup:
        subpixel True
        yanchor 1 ypos 1
        linear 1 ypos 0     
    hide noon_scrolling_skies
    show bedroom_night_no_bg_clean:
        zoom 0.9
    hide bedroom_noon_no_bg_clean
    with Dissolve(3)
    window show
    "Now it's morning."
    window hide
    hide night_scrolling_skies
    show bedroom_day_no_bg_clean:
        zoom 0.9
    hide bedroom_night_no_bg_clean
    with Dissolve(3)
    "..."

label saistart:

    stop music
    show black
    $ renpy.pause (1)
    show text "The mushroom kit arrives, and you follow the instructions." with dissolve
    $ renpy.pause ()
    show text "Watering, ventilating, talking to it... Every day, you get out of bed for its sake..." with dissolve
    $ renpy.pause ()
    hide text with dissolve
    play music "thinking.mp3"
    #show afternoon_clouds at bg_scroll
    scene day_clouds with dissolve
    show bedroom_opencurtains
    show bottle
    show kit_opened
    with Dissolve(2)
    

    
    show mc happy at right with easeinbottom
    window show
    m "Good morning, my gorgeous baby mushrooms. How are we feeling today?"
    show mc surprised
    m "Me? Well, I'm surviving. Thanks for asking."
    show mc happy
    play sound "spray.wav"
    m "Well, here's some water for motivation."
    
    show mc annoyed
    play sound "spray.wav"
    m "And an extra, on the house."
    m "See you tomorrow."
    window hide
    hide mc with dissolve
    show dirty1 with Dissolve(3)
    
    show mc annoyed at right with easeinbottom
    window show
    m "Sure taking your time, aren't you?"
    show mc normal
    m "*Sigh*..."
    show mc normalside
    m "I thought after two weeks, there'd be {i}something{/i} at least..."
    play sound "spray.wav"
    
    window hide
    hide mc with dissolve
    show dirty2 with Dissolve(2)

    show mc stressed at right with easeinbottom
    window show
    m "Still? This is the fourth week! What are you even doing in there?"
    show mc normalside
    m "Hah... what a waste of time."
    show mc sad
    m "Did it die?"
    show mc stressed
    "You probably messed up somewhere. Even when trying your best, you still failed."
    show mc annoyed
    m "No. Gotta be patient. Gotta be positive. *inhale, exhale*."
    show mc normal
    m "You're just relatably slow on progress."
    m "We'll get through this together. Don't give up, and I won't either."
    "What desperate optimism."
    show mc stressed
    "And IF it grows? What? That'll solve all the problems you're ignoring?"
    "When are you going to class? When are you going to attend events and make friends?"
    show mc normal
    m "I'm sure you'll sprout any day now..."
    play sound "spray.wav"
    window hide
    
    
    hide mc with dissolve

    stop music fadeout 2
    show dirty3
    hide kit_opened
    show kit_burstingsai
    show fog_2 
    with Dissolve(3)
    pause 1
    play music "lightbuzz.wav"
    "..."
    "..."
    "..."
    "I know you're awake."
    "Are you going to get up?"
    m "No."
    "You should."
    "There's so much to do."
    m "I don't care."
    "You SHOULD care. It's your life. Nobody else is going to care for you."
    "Get up. You've already wasted so much time just lying in bed today."
    "You need to shower, do laundry, take out the trash- and don't you have an {i}exam{/i} next week?"
    "At this rate, you're going to fail your first year... How will you tell your parents? You're going to disappoint them!"
    "How much longer can you afford to stew in this hotpot of self-pity?"
    "You should-"

    show mc vshout at right

    m "{size=+20}SHUT UP! SHUT UP! SHUT UP!" with sshake
    show mc vstressed
    m "You're just making everything worse!"
    "The one making things worse... is you."
    "Just look around you."
    window hide
    show mc sad
    pause 1
    m "(This mess is overwhelming. I don't even know where to begin.)"
    show mc stressed
    m "This is so hopeless. I'm giving up."
    "Even on your mushrooms?"
    show mc normal
    m "I don't know why I bother. I already know there's-"
    stop music
    show mc shocked at bounce
    hide fog_2 with dissolve
    m "{size=+30}{sc=2}{color=#000000}THERE'S SOMETHING GROWING!?"
    show mc surprised
    m "{size=+30}THERE'S SOMETHING {sc=2}{color=#000000}{size=+20}GROWING!!"
    m "Ohmygodohmygodohmygod!"
    m "{size=+30}{sc=2}{i}{color=#000000}I DID IT! FINALLY! \nI GREW MUSHROOMS!"
    "THAT got you out of bed? What about all the other stuff-"
    show mc stressed
    m "Shut up and let me have my excitement!"
    "Fine. I'm surprised you didn't screw this up like everything else that you do."
    "Genuinely, I am impressed that you didn't fail miserably!"
    show mc normalside
    m "(Ignoring that.)"
    show mc normal
    m "Now let's see..."
    show mc happy
    m "There are ten sprouts! Hell yeah!"
    show mc confused
    m "They look kinda weird though. These are edible, right?"



    


    
    

    # $ renpy.pause ()
    # show text "{sc=1}....{/sc}" with dissolve
    # $ renpy.pause ()
    # hide text with dissolve

    # show afternoon_clouds at bg_scroll
    # show bedrooom_sai_intro
    # with Dissolve(2)
    
    # play music "static.wav" fadein 3
    # pause 2

    # jump check_messages
    
    # show text  "{color=#000000}How do normal people get up in the morning? How are they {sc=1}{color=#000000}{i}happy{/i}{/sc}?" with dissolve
    # $ renpy.pause ()
    # hide text with dissolve
    # show text  "{color=#000000}What are they thinking? What motivates them?" with dissolve
    # $ renpy.pause ()
    # hide text with dissolve
    # show text  "{color=#000000}{sc=1}It doesn't.{/sc}" with dissolve
    # $ renpy.pause ()
    # hide text with dissolve

    #show bedrooom_sai_intro2 with dissolve
    
    # call screen phone_1 with dissolve

    # screen phone_1:
    #     imagebutton:
    #         xanchor 0 yanchor 0 xpos 0.371 ypos 0.370 idle "pc/phone_idle.png" hover "pc/phone_hover.png"
    #         action Jump("check_messages")

    # label check_messages:
        
    #     show pulsingblack
    #     show fog_2 
    #     with Dissolve(3)
    #     pause 1
    #     window show
    #     "You did it again."
    #     "By the time you wake up, the day is already over."
    #     "There's goes another one."
    #     "Always too late."

    #     window hide
    #     call screen sai_intro_whatnow with dissolve
        

    # screen sai_intro_whatnow:
    #     imagebutton:
    #         xanchor 0 yanchor 0 xpos 0.371 ypos 0.370 idle "pc/phone_idle.png" hover "pc/phone_hover.png"
    #         action Notify("It's dead from playing long after you fell asleep.")
    #     imagebutton:
    #         xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.5 hover "mushroom_display/bed_hover.png" idle "mushroom_display/bed_idle.png"
    #         action Notify("You're so tempted to stay and rot in here forver.")
    #     imagebutton:
    #         xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
    #         action Notify("You don't deserve to eat.")
    #     imagebutton:
    #         xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.364 hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png"
    #         action Notify("You want to rip it's cuddly body to shreds.")
    #     imagebutton:
    #         xanchor 0.5 yanchor 0.5 xpos 0.71 ypos 0.42 hover "mushroom_display/sai_box_hover.png" idle "mushroom_display/sai_box_idle.png"
    #         action Jump("sai_whatnow")    
        
  
    # label sai_whatnow:
    #     show mc vannoyed with easeinbottom
    #     m "It's kind of funny."
    #     m "You don't know it, but you {i}depend{/i} on me."
    #     m "Your life is in my hands. I could just not water you and you'd die. Heh."
    #     m "Alright, time to see if anything grew."
    #     show mc stressed
    #     m "You're seriously taking your time."
        
    # stop music fadeout 3
    # show mc confused
    # m "Wait..."
    # window hide
    # show mc surprised at bounce
    # hide fog_2
    # hide pulsingblack
    # with dissolve
    # m "Something's actually sprouted!"
    # m "Oh my god, I did it. I grew little mushrooms."
    # "I'm surprised you didn't screw this up like everything else that you do."
    # "Genuinely, I am impressed that you didn't fail miserably!"
    na "{size=-8}Greetings!" # later you can have a scene where she clarifies she didnt want you to eat her because she wants to be present and able to guide you through a trip if you did eat her
    window hide
    show mc normalside
    m "(Sounds like a mosquito got in. It's buzzing around somewhere.)"

    show mc awed 
    m "I still can't believe it. I grew these mushrooms? It took like 2 months! I'd kind of given up."
    show mc annoyed
    m "It just needed time in the end!"
    show mc happy
    m "Okay, it's harvest time! Shall we do one last spray for the road?"
    hide mc with easeoutbottom
    call screen water_sai_day1 with dissolve
        

    screen water_sai_day1:
        imagebutton:
            focus_mask True idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("sai_day1_watered")

    label sai_day1_watered:
        
        $ watered = 0
        show water_status at topright with dissolve
        

        pause 0.5
        play sound "spray.wav"
        $ watered = 1
        pause 1
        queue sound "spray.wav"
        $ watered = 2
        window show
        "You give your newly-sprouted mushrooms some celebratory sprays."
        window hide
        hide water_status with dissolve
        show mc happy at right with easeinbottom
        window show
        m "Alright, let's pull these out!"
        show mc stressed at quiver
        m "Eh-eeeeeeeee-"
        hide mc stressed
        show mc surprised at right
        show mc surprised at bounce
        m "Damn, mushrooms are stronger than I thought!"
        show mc normal
        m "Okay. Serious face on. Full strenth!"
        na "{size=-8}Ready!"
        show mc stressed at quiver
        m "Hhhhhhhhhnnnnnn!"
        window hide
        play sound "tear.wav"
        
        hide kit_burstingsai
        show kit_burstingsai2
        with dissolve
        hide mc
        show mc surprised at right
        
        window show
        stop sound

    m "..."
    m "What... what..? What? What? {i}WHAT{/i}?"
    na "{size=-8}One more pull and I'll be out!"
    show mc shocked at bounce
    play sound "scream.wav"
    #play music "horror.wav"
    m "{sc=4}{i}{color=#000000}{size=+50}GAH! WHAT THE FUCK!?\nWHO ARE YOU!?{/i}{/sc}" with sshake
    na "{size=-8}Your mushroom?"
    show mc shocked at bounce
    m "Y-y-y-y-y-"
    m "Y-Y-YOU'RE TALKING!" with sshake 
    na "{size=-8}Correct. Are you okay? You sound befuzzled."
    show mc shout
    m "{sc=4}{i}{color=#000000}{size=+50}I GREW ARMS!\nAND THEY TALK!{/i}{/sc}" with sshake
    na "{size=-8}Technically, I have more than just arms."
    show mc shocked
    m "{sc=4}{i}{color=#000000}{size=+50}THERE ARE MORE ARMS!?{/i}{/sc}" 
    na "{size=-8}Ah, n-no, that's not what I meant...."
    na "{size=-8}I'll show you! Kindly grab my hands and harvest me, if you don't mind."
    m "Harvest you!? But... you're..."
    na "{size=-8}Worry not, for I have no pain receptors! The process will not hurt me."
    show mc worried
    m "(This can't be happening! It's impossible! This is INSANE!)"
    m "(I'm TALKING to my mushrooms! And they have arms!)"
    "QUICK! PANIC!"
    # window hide
    # show mc vstressed at right with move
    # window show
    menu:
        "What do I do!?"
        "{sc=4}{i}{color=#000000}{size=+40}ROUNDHOUSE KICK!":
            show mc vshout
            m "{sc=4}{i}{color=#000000}{size=+50}AAAAAAAAAAAAAAH!"
            window hide
            #hide mc with easeoutbottom
            play sound "punch.wav"
            hide kit_burstingsai2
            #show mc shocked at right with easeinbottom
            window show
            "Adrenaline-fuelled, you deliver a roundhouse kick to the box - launching it right out the window!"
            m "..."
            show mc awed
            m "Whoa. That was pretty cool!"
            "You literally just kicked out the thing you've been growing for nearly 2 months!"
            "What was the point of doing all that if you were going to just throw it away?"
            
            show mc stressed
            m "Maybe... that {i}didn't{/i} happen. Maybe I just hallucinated from stress."
            "You'll never know now. Now, it's the groundkeeper's problem. Hopefully it died on impact, whatever it was."
            show mc normal
            m "*Sigh* It's all over. Let's just close the curtains, forget it ever happened, and feel safe again."
            window hide
            play sound "curtain.ogg"
            scene black
            show bedroom_closedcurtains
            show dirty1
            show dirty2
            show dirty3
            show bottle
            with dissolve
            window show
            show mc sad
            m "Bed, comfort me."
            window hide
            hide mc with easeoutbottom
            scene black with fade
            $ persistent.send2 = True    
            "End 2: I don't KNOW you, and I don't CARE to know you."
            
            return

        "I have to calm down.":        
            jump gt_pull
            

label gt_pull:
    
    show mc stressed
    
    m "(Calm down! Repress your inner caveman! Panic isn't helpful, so just compartmentalise it and process it all later!)"
    "Wow, you actually learned something from all of those self-help Youtube videos."
    show mc worried
    m "Uh, okay. I-I'm calm! W-What do I do?"
    na "{size=-8}I would appreciate it if you could hold my hand and pull me out of this cell."
    m "Okay. I'm sorry if my hands are sweaty."

    hide mc with easeoutbottom
    "Ignoring your social anxiety and terror, you put the box on the floor, grab both of the suprisingly soft hands, and put your game face on."
    "It's pulling time!"
    window hide    
    call screen sai_help with dissolve

    screen sai_help:
        imagebutton:

            hover "mushroom_display/sai_box_hover.png" idle "mushroom_display/sai_box_idle.png" focus_mask True 
            action Jump("sai_giveahand")    


    label sai_giveahand:
        show pull_sai_1 with dissolve

        stop sound
        play sound "ballon.wav"
        $ renpy.pause(3.0, hard=True)

        stop sound 
        play sound "pop.ogg"  

        show pull_sai_2

        pause
    
    
    scene black with fade
    play music "normal.mp3"
    show day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show dirty3
    show bottle
    with Dissolve(2)

    
    show sai shocked at left #she's shocked
    show mc shocked at right
    with easeinbottom
    window show
    na "Oh my! I'm so tall! And so are you! Wow..."
    na "So this is life? How spacious it is! I can even stretch my arms out without touching anything."
    
    show sai shy
    na "It's nice to finally... talk... with you."
    show sai apologetic
    na "Although this feels more like a monologue..."
    show sai confused
    na "You CAN talk, correct...?"
    m "{size=-10}I-I..."
    show sai vshy
    na "Ah, take your time. In fact, you don't need to say a thing."
    show mc stressed
    m "(I don't even know what to say, even if I could!)"

    show sai normalside
    na "So this is your nest? It's so nice and overgrown, so chaotic, just as nature intended."
    show mc surprised
    m "(She LIKES that my room is a mess!?)"
    show sai vvhappy
    na "Oh, you even have another little friend here..." 
    "She walks, stumbling a little, over to the spider that's built a web between your backpack and the wall over the past month."
    show sai happy
    na "Greetings creature. It is a pleasure to make your acquaintance."
    
    show mc stressed
    m "(What is going on...!? Is this a dream?)"

    window hide
    show mc stressed
    pause 1.0
    show mc normal
    pause 0.5
    show mc worried
    window show
    m "You're still there..."
    show sai surprised
    na "Oh, my apologies. Was I meant to disappear?"
    show sai vshy
    na "I'm still quite new to this whole living thing. So I apologise in advance for any missed social cues."
    show mc surprised
    m "Y-You're not just arms... You're a whole person! You're a WOMAN!" 
    show sai think
    na "Well, a woman mushroom, yes. Is that a problem?"
    show mc shout
    m "{size=+10}YES! I was expected a normal-sized, non-gendered, silent mushroom! Not... THIS!"
    show sai confused
    na "Not what you \"expected\"? Oh, then-"
    show sai excited
    na "{size=+10}Congratulations! I am glad to have exceeded your expectations!"
    show sai shy
    na "Thanks to your diligent watering and motivation, I have successfully matured."
    show mc shocked
    m "Who even ARE you?"

    show sai think
    na "Ah, introductions! How could I forget the staple of a relationship?"
    show sai happy
    s "Greetings. I am your Psilocybe cubensis mushroom. Sai for short."
    show mc surprised
    m "S-Sai? Like, a sigh? Breathing out?"
    s "Correct. Assosciations with respiration are an honour."
    show sai normal
    s "And how should I refer to you?"
    show mc worried
    m "M-my name? Er-"
    show mc vstressed
    m "(SHIT! INTRODUCTIONS? HOW DO I DO THEM AGAIN???)"

    jump sainame

    default sai_name = False

    label sainame:                
        $ player_name = renpy.input("What's my name again!?", length = 8)
        $ player_name = player_name.strip()
        $ player_case_insensitive = player_name.lower()
        if player_case_insensitive == "sai":
            if sai_name:
                show mc normal
                m "...%(player_name)s. "
                show sai vvhappy
                s "Hahaha!"
                show mc confused
                m "But that's my name!"
                show sai vhappy
                s "I'm glad you also have a sense of humor."
                show mc stressed
                
                jump sainame

            else:
                show mc normal
                m "...%(player_name)s."
                show sai shocked
                s "What are the odds!? We have the same name!"
                show sai confused
                s "No wait..."
                show sai vvhappy
                s "Oh, it's a joke! Hehehe!"
                $ sai_name = True
                jump sainame
                
        elif player_name == "":
            "What? Can't even think of a name by yourself?"
            "You really are hopeless."
            "Fine, I'll make one up for you. Let's go with your dead family fish."
            $ player_name="Finn"
            $ playername = player_name
            m "...%(player_name)s."
        
        else:
            $ playername = player_name
            m "...%(player_name)s."
        show mc worried
        m "I'm, uh...%(player_name)s. That's me name. I mean, my name. Yes. Uh..."
        show sai determinedclosed
        s "%(player_name)s, %(player_name)s, %(player_name)s..."
        show sai happy
        s "It now stored in my long-term memory."
        # show sai vshy
        # s "It is an honour to finally make your aquantaince, %(player_name)s."
    
    
    show mc stressed
    m "Am I still asleep? Maybe this is all a dream..."
    show sai happysigh
    s "Ah, don't dwell too much on that. Even if everything is a facade, what matters is that it is perceived."
    show mc confused
    m "..."
    show sai shy
    s "If you are struggling to come to terms with-"
    show mc stressed
    m "What are you talking about!?"
    show sai surprised
    s "E-eh? I was... trying to console you on your existentialism..."
    show sai pout
    s "I must have misunderstood."
    show mc worried
    m "Instead of that, can you please explain why... you're so... humanoid?"
    "Because I'm pretty sure mushrooms aren't supposed to get like this!"
    show mc stressed
    m "And I'm kind of freaking out right now!"
    
    show sai think
    s "Does anyone truly know why we are, as we are?"
    show sai horny
    s "We are all so unique, that nothing will ever truly match one's expectations, and that is a good thing."
    show mc confused
    show sai happy
    s "Rather than seek control, I recommend that you embrace change."

    show mc worried
    "Her nonsense makes you suddenly realise-"
    "This situation is {i}ABNORMAL{/i}!"
    "You're talking to a {i}mushroom{/i}! Are you non-ironically insane?"
    
    show sai happy
    s "Anything else you'd like to ask? I am enjoying \"questions\"."
    show mc awkwardsmile
    m "Yeah, can you wait five minutes? I gotta check something quick."
    show sai think
    s "Can I wait five minutes? Well, technically yes, but what does it really mean to \"wait\"...?"
    hide mc with easeoutbottom
    window hide
    hide sai with dissolve

    call screen sai_check_website with dissolve

    screen sai_check_website:
        imagebutton:
            idle "pc/pc_hover.png" hover "pc/pc_click.png" focus_mask True 
            action Jump("sai_check_site")
        
        imagebutton:
            hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png" focus_mask True 
            action Notify("The only one who will always be there for you.") 
        imagebutton:
            hover "mushroom_display/noot_hover.png" idle "mushroom_display/noot_idle.png" focus_mask True 
            action Notify("The other only one who will always be there for you.")      
        imagebutton:
            hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png" focus_mask True 
            action Notify("Even MSG can't make these tasty for you anymore.")       
        imagebutton:
            focus_mask True idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Notify("You use this as your water bottle too.")


    
    label sai_check_site:       
        play sound "<from 0 to 1>type.wav"
        scene site_error with dissolve
        pause

    show mc shocked at right with easeinbottom 
    window show
    m "NOOOOO! Why is the universe is ALWAYS against me?"
    "Looks like you'll have to get information the old-fashioned way-"
    show mc sad
    m "Talking. Ugh."
    "You'll probably just embarrass yourself. What's the point?"
    "Just give up and let her do what she needs to, while you huddle into a ball in your bed."
    m "(Maybe if I fail, I'll do that.)"
    
    window hide
    
    hide mc with easeoutbottom

    scene black with fade
    show afternoon_clouds
    show bedroom_opencurtains:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty1:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty2:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty3:
        matrixcolor TintMatrix("#f4ca9a") 
    show bottle:
        matrixcolor TintMatrix("#f4ca9a")
    with Dissolve(2)

    show sai confused at left with dissolve
    show mc awed at right with easeinbottom
    window show
    s "...so I think the answer is: Yes, I CAN wait five minutes."
    show sai annoyed
    s "Any other questions? That one was more difficult than I expected."
    m "Yeah... is there any... do you..."
    show mc stressed
    m "L-let me try that again."
    show sai normal
    s "..."
    m "..."
    show mc worried
    m "Can you tell me... something? Um, anything about yourself? I'm just so confused..."
    show sai worried
    s "I guess answering \"questions\" is harder than I first thought."
    show mc stressed
    "You're so bad at talking that you've made her lose her excitement."
    show mc worried
    m "(So now what? Do I just accept what she said as true?)"
    m "(Did the mushroom I was growing blossom into a full person?)"
    show mc sad
    show sai determined
    m "(If I really brought life into this world...)"
    show sai determinedclosed
    m "(It means I am responsible for her!)"
    show mc stressed
    show sai embarrassed
    "You can't even look after yourself properly."
    "Maybe it's easy to not care when you're only harming yourself."
    show sai pout
    m "(Shit.)"
    show sai normal
    s "Your facial expression suggests that you are stressed."
    show sai shy
    s "Perhaps I may lighten the burden of your woes, through your verbal communication of them?"
    show mc normal
    m "Okay. I'll be honest: I don't know what to do."
    m "I don't know what you want, or what you need... This whole thing was so unexpected that I'm like... frozen."
    show sai determined
    s "These questions are much easier than your previous ones!"
    show sai normal
    s "First - What do I need? Water. That is all."
    show mc normalside
    "(I've been doing that for weeks, so at least I know I can handle it.)"
    s "Second - What do I want? I want to experience life."
    show sai shy
    s "And, if I can, help others along the way."
    show mc normal
    m "That's way too vague."
    show sai apologetic
    s "..."
    s "I wish to go wherever the tides of life bring me."
    show sai embarrassed
    s "Whether that be the heights of pleasure..."
    show sai annoyed
    s "Or the depths of misery." 
    show mc awed
    m "(Whoa, what's with the sudden melancholy?)"
    m "Why? That's kinda sad."
    show sai shy
    s "It's only sad if I decide to feel that way. So I've decided not to."
    s "I have chosen to approach life with only curiosity."
    show mc confused
    m "Sure... if that's what you want."
    show sai horny
    s "I have already enjoyed the warmth of friendship."
    show mc surprised
    m "You have? With who?"
    show sai normal
    s "..."
    show sai worried
    s "Have I misinterpreted our relationship?"
    show mc surprised
    
    s "We are friends, right?"
    show sai_affection at topleft with dissolve

    menu:
        "She thinks we're friends!?"
        "That's too fast!":
            m "(I need to be honest!)"
            show mc normal
            m "Uh, but Sai... I didn't know you could actually hear me. I was saying a ton of stuff that I thought was private."
            show mc normalside
            m "Sorry for giving you the wrong impression, but all that stuff about being friends-"
            $ sai_rp -= 10
            show sai apologetic
            s "We are not friends?"
            show mc surprised
            m "But we can BECOME friends!"
            show sai confused
            s "I am..."
            show sai pout
            s "Confused."
            show mc awkwardsmile
            m "I'm just saying we should get to know each other better!"



        "Pass the interview first.":
            show mc stressed
            m "(What difference will it make? At least this way I don't make her sad.)"
            m "(And who knows, maybe it'll be nice...)"
            show mc normalside
            m "Eh, why not? The position is open, if you want it."
            show sai surprised
            s "Then I am applying! How long must I wait to hear the results?"
            show mc annoyed
            m "You'll need to answer some questions first."
            show sai determinedclosed
            s "My first interview - I'm ready!"
            show mc normal
            m "So, why should I accept you as my friend? What do you have to offer?"
            show sai shy
            s "Because everyone is a friend to me. So I am already your friend. All that is left is for you to be mine."
            m "So you're saying I don't have a choice?"
            show sai normal
            s "I'll never force anyone to do anything! I don't believe in that."
            show mc annoyed
            m "You're hired."
            $ sai_rp += 10
            show sai happy
            s "Success!"
            

    show afternoon_clouds
    show bedroom_opencurtains:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty1:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty2:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty3:
        matrixcolor TintMatrix("#f4ca9a") 
    show bottle:
        matrixcolor TintMatrix("#f4ca9a")
    with Dissolve(2)


    show sai surprised
    s "Ah... the sun is changing position. Mother Nature calls my name."
    s "Come. Let's go."
    "She wants to leave? Great! Maybe she'll get lost and everything will return to normal."
    m "You go ahead. I'm not interested in anything there."
    s "You don't burn with curiosity? To explore, to interact? Not even the trees?"
    m "Uh... no. Not even the trees. Though honestly, I'm not interested in anything these days, so maybe you can go by-"
    s "Why? Are you depressed?"
    "Wow! No one's ever called you out that quickly before!"
    m "(How do I respond? Do I just say yes? Do I change topic? Lie?)"
    m "..."
    s "It's just that a lack of interest in life is one of the symptoms of depression. And you seem reclusive, and inexperienced with social interaction, and keeping poor personal hygiene, and-"
    m "(She's got even less social tact that me.)"
    m "You can stop there. I know all the reasons why I suck already. No need to remind me."
    s "Ah, low self-esteem. That's another one."
    m "Okay! Let's drop this conversation please?"
    s "I recommend coming outside with me to practise stepping outside your comfort zone."
    m "You're not my therapist. Don't care so much about me and just focus on yourself."
    s "I respectfully decline. Unfortunately for you, I care about your wellbeing."
    m "WHY!? We literally JUST met!"
    s "Perhaps in a literal sense, yes. But we have known each other for eons. As particles, there is no inherent individual in this universe. We are all one."
    m "No."
    s "It seems I must progress to brute force."
    m "What are you going to do? Beat me up?"
    s "No, I shall simply kidnap you. My apologies, but due to time constraints, I must resort to this."
    show mc vannoyed
    m "Hah! I'd like to see you try. You're short. You can't even pick me up."
    show sai happy
    s "Understood. I shall show you my physical prowess."
    show mc surprised
    m "(Wait, her confidence... I'm starting to doubt myself.)"
    
    menu:
        "FINE! I'll come!":
            $ sai_rp += 10
            m "FINE! I give up, I'll come! Just don't pick me up."
            s "That was the mature response. I'm proud of you for joining the expedition on your own terms."
            m "Just a walk around the block, okay? We're not going into a jungle."
            show sai vvhappy
            s "The block, the sphere, the rhombus, whatever it is, we will walk around it."
      
        "Call her bluff.":
            show mc normal
            m "Nope. You're bluffing."
            show sai determined
            s "I do not lie."
            "Sai approaches you, determination glinting in her eyes. Something about her almost predatory advance activates the neurons of an ancient, primitive response: fight or flight."
            show mc surprised
            m "Hey! Hey, don't come any closer! I'll defend myself if I have to!"
            s "You are entitled to do that. But are you prepared to hurt someone, simply for caring for you?"
            show mc worried
            m "..."
            "That's not fair. She's guilt-tripping you into allowing her to kidnap you!"
            show mc stressed
            m "Urgh, just leave me alone. I don't want to do this..."
            s "Then confront your discomfort - Do not succumb to it!"
            m "No, I'm not doing this! You're a stranger! I don't trust you!"
            "Sai leaps towards you."
            show sai determinedclosed
            s "HNNNNG!"
            show sai sad
            show mc normal
            m "Ah... So you were lying after all..."
            s "I never lied. I simply stated I would demonstrate my phsycial prowess. As you can see, it is nearly non-existant."
            show sai happy
            s "Ah! But now that you see that I am not a threat, you are inclined to become my friend, right?"
            m "No."
            s "Ah..."
            return
    

    # hide sai with dissolve
    # show mc surprised
    # m "To the window?"
    # show mc shocked
    # m "Hey! W-WHAT ARE YOU DOING!? DON'T JUMP!"

    # window hide
    
    # show sai surprised at left with easeinbottom
    # window show
    # s "I have your permission. What's wrong?"
    # show mc shout
    # m "What's WRONG!? I just saved you from falling to your death! You would have died!"
    # show mc vstressed
    # m "Oh my God. Please don't do that again!"
    # show sai pout
    # s "Hmm? B-but I was just going outside..."
    # show mc vshout
    # m "Then use the STAIRS!"
    # show sai shy
    # s "I apologise for causing you excess stress... but what are stairs?"
    # show mc stressed
    # m "...I'll show you."
    
    # scene hallway with fade
    # show mc normal at right
    # show sai sad at left
    # with easeinbottom
    # m "There. Go down them until you reach a door-"
    # show mc normalsquint
    # m "You DO know how to open doors, don't you?"
    # show sai apologetic
    # s "I-I think so. I first knock, and someone opens it right?"
    # show mc stressed
    # m "..."
    # "You're slowly realising how little Sai knows. Is it too dangerous to let her roam the streets alone?"
    # show mc worried
    # m "(But I don't want to go out... I don't want to be in public. I look horrible.)"
    # m "(And I've got so much work to do! I don't have time to just have fun!)"
    # menu:
    #     "Should I stay, or should I go?"
    #     "I'm not going outside!":
    #         show mc confused
    #         m "Be careful."
    #         show sai shy
    #         s "Y-yes! I shall exert full caution."
    #         hide sai with easeoutbottom
    #         "With those words, Sai turns and takes her first step down the stairs-"
    #         play sound "thud.wav"
    #         show mc shocked
            
    #         "Down which she immediately falls!"
    #         m "Sai! Are you okay!?"
    #         s "Worry not! Such a fall won't injure me. I just need practice!"
    #         window hide
    #         menu:
                
    #             "WHAT YOU NEED IS ASSISTANCE!":
    #                 show mc stressed
    #                 m "(Like hell! I change my mind! She's a danger to herself and everyone around!)"
    #                 m "(And if she dies, I'm gonna feel guilty!)"
    #                 show mc shout
    #                 m "Don't move a muscle! I'm coming down before you can hurt yourself."
    #                 window hide
    #                 hide mc
    #                 with easeoutbottom
    #                 hide day_1
    #                 hide sai_affection
    #                 with dissolve
    #                 play sound "door.wav"
    #                 stop music fadeout(3)
    #                 scene black with Fade(0.5, 1.0, 0.5)
    #                 jump garden


    #             "You got this!":
                    
    #                 show mc worried
    #                 m "O-okay... good luck..."
    #                 play sound "thud.wav"
    #                 "You watch with growing concern as Sai proceeds to stumble down the rest of the flight of stairs..."
    #                 show mc stressed
    #                 m "She'll be okay... right?"
    #                 scene black with fade
    #                 "Yeah no, spoiler alert: she didn't come back."
    #                 "End 4: Last Sai-ted."
    #                 return
    #     "Damn it! I'm coming with!":
    #         show mc stressed
    #         m "As much as I'd love to stay... I think you need parental guidance."
    #         show sai sad
    #         s "I'm sorry for causing you trouble. You seem to prefer staying indoors, so I didn't want to disturb you."
    #         show mc normalside
    #         m "Don't worry, it's probably good for me to taste some fresh air anyway."
    #         show sai normal
    #         s "So you will escort me?"
    #         m "If it's just a walk around the block, I think I'll manage."
    #         show sai vvhappy
    #         s "The block, the sphere, the rhombus, whatever it is, we will walk around it. Thank you, %(player_name)s."
    window hide
    hide mc
    with easeoutbottom
    hide day_1
    hide sai_affection
    with dissolve
    play sound "door.wav"
    stop music fadeout(3)
    scene black with Fade(0.5, 1.0, 0.5)
    jump garden



    # m "Which is?"
    # show sai determined
    # s "I have to go out and find answers, and I would like if you would accompany me."
    # show mc stressed
    # m "...No."
    # s "Yes."
    # s "I would like to find a place brimming with all sorts of life, maybe even other fungi like me."
    # show sai sad
    # s "I think maybe they'll have the answers I'm looking for."
    # show sai normal
    # s "You're the only one I know."
    # show sai worried
    # s "I beg of you. Please take me outside. Anywhere with lots of nature."
    # show sai vhappy
    # s "The outside looks so interesting from your window. So many humans, and {i}things{/i}..."
    # s "It just makes me curiouser and curiouser..."
    show sai normal
    s "Don't you feel the same?"
    show mc stressed
    m "Maybe the nature, but... the humans? Not so much."
    show sai surprised
    s "You dislike your own species? Why?"
    "Is that suprise or disgust on her face?\n You can't just admit your misanthropic thoughts out loud."
    show mc normal
    m "Many reasons."
    s "Such as?"
    show mc vannoyed
    m "Such as, they're annoying and judgemental and tell you what to do. Like you right now."
    show sai worried
    s "Oh, I'm sorry... That wasn't my intention. I don't want you to dislike me. I just wanted to make you happier."
    show mc normal
    m "I'm {i}fine{/i}."
    show sai shy
    s "O-of course you are, but... Let's try to be more than fine!"
    show sai happy
    s "Let's go outside together and explore the world through a new lens. Change is good! It'll help-"
    show mc normalside
    m "Then go by yourself. I have stuff to do."
    show sai determined
    s "Stuff? I have heard you stay in bed day after day. Surely there's nothing more you can accomplish in here."
    "She doesn't know that you gave up on \"accomplishing\" things a long time ago."
    show mc stressed
    s "At the very least, I'm certain a short break will help."
    show mc shout
    m "Why are you so insistent? Why do you care if I go or stay?"
    m "Look I will let you stay in my room for a while, until you figure out how you want to proceed"
    m "But until then, just focus on yourself!"
    show sai confused
    s "I'm confused. Does me caring about you... bother you?"
    show mc stressed
    m "Yes! I just want to be left alone in peace without worrying about someone bothering about me."
    m "Also you might have been listening to me for a while, but to me you're still a stranger!"
    show sai surprised
    s "..."
    show sai vshy
    s "What a conundrum!"
    show sai worried
    s "{size=-8}I can tell he doesn't like it here. He knows so as well. But he rejects the very premise of my help... Why on earth would he do that?{size=+8}"
    m "(I can hear you, you know.)"
    show sai sad
    s "{size=-8}Forcing others isn't right or effective. If I put myself in his shoes, I wouldn't like it either."
    s "{size=-8}What if I annoy him? I just promised I wouldn't be a bother. Oh, what do I do?"
    "Why does everything have to be so complicated? Why can't you just do what you want without it affecting someone else?"
    "That's selfish of her, isn't it? It's manipulative. She's trying to guilt you into doing what she wants."
    menu:
        m "(But is she right? Am I overthinking it?)"
        "I'm staying here, and that's final.":
            jump sai_stay_home

            
        "Leave the dungeon.":
            jump sai_go_outside
                

label sai_stay_home:
    show mc normal
    m "I'm not making myself uncomfortable just to suit you, so stop pushing me. I'm staying in here, going to do my work, and that's final."
    show sai shy
    s "It's okay, %(player_name)s. Growth takes time, and I don't want to sour our relationship."
    show sai normal   
    s "I just thought we were similar. I was also confined in a small box for a long time."
    s "It was comforting, familiar, but I wanted more. I craved the beauty of the unfamiliar. So I broke out, because otherwise I would die with regret."
    show sai happy
    s "Maybe next time you'll feel ready to test the waters of the outside with me, but until then..."
    show sai vhappy
    s "...think of me as your water bottle. I'll give you the attention you need to grow, until you're also ready to break out."
    show mc normalside
    m "How poetic."
    show sai vvhappy
    s "Expression is fun."
    m "I-I don't... {size=-8}want... {size=-4}atten{size=-2}tion...{size=+14}"
    "TO BE CONTINUED"


label sai_go_outside:
    show mc normal
    m "Fine, fine! You're right. It's good for me, and all that."
    m "We're just walking for a few minutes around the block, and then come straight back."
    show sai surprised
    s "I succeeded?"
    show sai vvhappy
    s "Yes, more than okay! The block, the sphere, the rhombus, whatever it is, we can walk around it!"
    show sai happy
    s "So, we can go now? You are prepared?"
    m "Keys, wallet, phone, ugly face... Ready."
    show sai sad
    s "Ugly? Sorry, I'll work on that..."
    show mc stressed
    m "N-no, not you... - Ugh, just ignore me. Let's go."
    
    window hide
    hide sai
    hide mc
    with easeoutbottom
    hide day_1
    hide sai_affection
    with dissolve
    play sound "door.wav"
    stop music fadeout(3)
    scene black with Fade(0.5, 1.0, 0.5)  
    
    
    jump garden

label garden:
    play music "date.wav"
    show chibi_mc at slightright
    show chibi_sai at slightleft
    with easeinright
    

    # "You thought accompanying your slow-ass mom to the grocery store was bad..."
    # "But Sai? She's on another level of excruciating."
    "You follow Sai around the block."
    "There are more people than you antipated. You just try to survive by keeping your eyes to the ground and being invisible."
    "Of course, that's difficult when Sai keeps stopping to sniff at things, and you have to keep pushing her onwards."
    "Brick? Tattered newspaper? Gum wad? Yes, she stops for them all."
    "This is so embarrassing. You wish she'd just just ignore them like everyone else."
    
    window hide
    hide chibi_mc
    hide chibi_sai
    with easeoutleft
    
    
    scene garden with Fade(0.5, 1.0, 1)
    
    window show
    
    window hide
    show sai think at left
    with easeinbottom
    window show
    s "*sniff sniff* My nose is tingling. Something familiar is nearby..."
    window hide
    show mc stressed at right
    with easeinbottom
    window show
    m "What's it this time?"
    show mc normal
    m "Huh. Never knew there was a community garden this close."
    show mc normalside
    m "Probably because I never explore..."
    window hide
    hide sai
    with easeoutbottom
    play sound "gate.wav"
    show mc annoyed
    window show
    m "Aaaand there she disappears again. At least no one else is here. I'm sure she can survive for a minute while I greet the bench."
    window hide
    hide mc
    with easeoutbottom

    window show
    "While Sai investigates the plants, you practise your favourite exercise: Sitting."
    "It's quiet."
    "For a rare moment, there's nothing you need to do."
    "Just you, some plants, and a girl who is more interested in said plants than you."
    "No thoughts, no eyes, no worries, no stress..."
    "As you lift your eyes to the sky and breathe in deep, some of the tension in your head drains away."
    "Huh. You just remembered. You like the outdoors."
    "You just... forgot."
    
    s "{sc=4}{color=#000000}{size=+50}%(player_name)s, help!"
    s "{sc=4}{color=#000000}{size=+50}I've committed {b}murder{/b}!"
    window hide
    show mc shocked at right with easeinbottom
    m "WHAT!?I looked away for {i}one{/i} second!"
    window hide
    show sai vsad at left with easeinbottom
    window show
    s "{sc=4}{color=#000000}I-I-I didn't mean it!"
    show sai scared
    s "My curiosity... I should have restrained myself! But I pulled too hard! I... I have been naughty!"
    show sai vsad
    s "I'm a murderer..."
    show mc awed
    m "Wait, are you talking about-?"
    "In her hand is an entire uprooted plant."
    show mc normalside
    m "(Oh... That's what she \"murdered\". What a waste of energy.)"
    show sai_affection at topright with dissolve
    s "Please, %(player_name)s. I need your help. What do I do?"
    menu:
        "How do I even respond to this...?"
        "Bury the body (N/A).":
        
            show mc normalside
            m "(This so doesn't matter.)"
            show mc normalsquint
            m "I don't know. Just bury it in some compost or something so no one gets mad at us."
            show sai worried
            s "Desecrating her life like that... how could I?"
            $ sai_rp -= 10
            hide sai_affection
            with dissolve
            show sai sad
            s "Oh, crumbs... shouldn't I come clean? How will I absolve my sins otherwise?"
            show mc normalsquint
            m "You asked for my advice. There you go. Do what you want."
            s "..."
            show sai normal
            s "I will give her a funeral."
            s "She will be remembered."
            show mc normalside
            m "Okay. I'll be here... On the bench... trying to enjoy myself."
            hide sai with easeoutbottom
            show mc stressed
            m "*Sigh*"

            hide mc 
            hide sai
            with easeoutbottom
            "You watch as Sai makes a shoddy hole in the compost, listen to her eulogise the stupid plant, and bury it with a prayer."
            "What a fucking waste of time and energy..."
            "You don't get Sai at all."
            show sai sad at left
            show mc normal at right
            with easeinbottom
            s "..."
            m "Good funeral?"
            show sai worried
            s "I never wanted to hurt anyone. But, because of my existence, someone has suffered."
            s "I'm disappointed in myself. I'm sure you are too."
            show mc vannoyed
            m "I'm really not."
            show sai vshy
            s "Well, thank you for not judging me."
            show mc normal
            m "So are we going home now, or what?"
            show sai sad
            s "Yes. I'm too ashamed to show my face here for much longer."

            $ not_scold = False
            #she eats dirt 
            show sai surprised
            s "Oh! Hold up!"
            show mc surprised
            m "What is she...?"
            jump eat_dirt
            
            
            

            


            


        "Relax.":
            
            $ not_scold = True
            show mc normal
            m "Look, calm down. You just need to put it back in soil."
            show sai apologetic
            s "No! I... I cannot simply bury the body and hide the evidence like that. I cannot! I must face my sins."
            show sai sad
            s "Please, I must be punished."
            show mc annoyed
            m "Sai, it's not dead."
            show sai shocked
            s "She's... alive?"
            show sai_affection at topright
            with dissolve
            show mc annoyed
            show mc normal
            m "Yup, so relax, okay? We just need to stick it back in the hole, y'know?"
            $ sai_rp += 10
            show sai happysigh
            s "Haah... Oh gosh, what a relief!"
            hide sai_affection
            with dissolve 
            show sai horny
            s "Sorry for the sudden eviction, Mrs Tomato. %(player_name)s will put you right back..."
            show mc confused
            m "Uh, {i}no{/i}! I'm not doing all the work! What about you? You caused this!"
            show sai sad
            s "I am too reckless. What if I make things worse?"
            show mc normalside
            m "You're so overthinking right now. You can do it."
            show sai shy
            s "You believe in me?"
            m "Uh, I guess? It's just easy."
            window hide
            show sai normal
            show sai apologetic
            hide sai
            hide mc
            with easeoutbottom
            window show
            "Using a hand shovel you find lying around, you teach Sai how to widen the orginal hole."
            s "Spectacular! I am \"gardening\"!"
            "Sai's pride is infectious. You feel like you're accomplishing something right now, for the first time in ages."
            "Because of you, this plant will produce fruit that others can enjoy. Granted, if it weren't for you, it wouldn't have been uprooted anyway, but still..."
            stop music fadeout 2
            "It was enough to make you let down your guard."
            play sound "dig.wav"
           
            window hide
            show finger_1 with dissolve
            pause 1
            window show
            s "Uh oh. My first injury."
            m "Did you scratch yourself?"
            s "... a little more severe."
            window hide
            show finger_2 with dissolve
            pause 1
            window show
            m "Y-Your FINGER! Oh my God!"
            m "It's cut off! Are you okay!?"
            s "Yes. I'm still alive. It was curiously painless..."
            m "What are we going to do?"
            s "Hmm..."
            s "Let's continue gardening."
            m "{size=+30}WHAT!?"
            s "Let's continue gardening."
            m "How are you being so blasé about losing {i}a finger{/i}!"
            s "I have nine more. It's hardly worth any worry."
            m "You're... you really don't care, do you?"
            s "Indeed. I'm resuming my shovelling now. Please hold this."

            "Sai casually places her finger in your palm before you can flinch away, then resumes gardening."
            window hide
            show finger_4 with dissolve
            $ hasfinger = True
            pause 1
            window show
            "You peek at the horrifying thing with bated breath, but... no blood..."
            "Just... a white centre. All mushroom."
            "It gives a last few twitches, then goes dead still."
            
            window hide
            show finger_5 with dissolve
            pause 1
            window show
            "It hits you with sudden clarity: Sai isn't human."
            "You grew a sentient creature."
            "This situation shouldn't exist."
            

            window hide
            pause 1
            play music "date.wav"
            scene garden with Fade(0.5, 1.0, 1)
            show sai happysigh at left
            show mc sad at right
            with easeinbottom
            s "The gardening operation is completed."
            show mc stressed
            m "Great, you can take this back."
            "You hold out the finger."
            show sai shy
            s "Um, %(player_name)s... I know that gifts are done to symbolise gratitude-"
            show mc worried
            m "(Oh no. I think I know where this is going!)"
            show sai vblush
            s "Therefore, please keep my finger as a reminder of my appreciation for your guidance and acceptance of me!"
            show mc stressed
            m "(But it's YOU! It's literally YOU!)" 
            m "(And if someone else sees a finger in my possession, they'll call the cops on me!)"
            show sai shy
            s "Please accept my gift."
            show mc normalside
            m "(She said please... Clearly this means a lot to her, but HER FINGER? WHAT DO I DO?)"
            menu:
                "Do I accept Sai's finger as a gift!?"
                "Accept.":
                    m "Uh... okay...?"
                    show sai happy
                    s "You are welcome."
                    

                "Politely decline.":
                    $ has_finger = True
                    show mc stressed
                    m "(How do I navigate this conversation!???)"
                    show mc awkwardsmile
                    m "I am... so honoured by how thoughtful you are..."
                    show sai happy
                    s "You're wel-"
                    m "BUT I can't accept this gift."
                    show sai surprised
                    m "I appreciate the thought, but I'm sorry, like... it's just..."
                    show mc stressed
                    m "I'm sorry, it's just weird and gross. You don't gift bodyparts."
                    show sai vshy
                    show mc awed
                    s "It's okay. I'm apologise that my gift is subpar."
                    show sai worried
                    s "There is much about human culture I have yet to understand."
                    show mc normalside
                    m "Yeah..."
                    show sai sigh
                    s "..."
                    
            show sai surprised at bounce
            s "!"
            hide sai with dissolve
            show mc stressed
            m "(Making friends with mushrooms is hard.)"
            show mc normal
            m "Okay, now that we're done, can we-"
            jump eat_dirt
            # m "If I'd stayed at home, I'd probably just be on my phone right now-"
            
            


            # s "Um, %(player_name)s."
            # m "What are even you going to do with it?"
            # s "Consider it my present for going outside with me."
            # m "(This is a messed-up present.)"
            # s "Dispose of it if you want, but if you plan on eating it please let me know beforehand."
            
            # "The idea of simply disposing someone's body part doesn't feel right."
            
            # s "Operation replant, complete."
            

            
            # s "Mrs. Tomato, how do you feel?"
            # m "You're not actually talking with it, are you?"
            # s "It takes two to talk, so no."
            # s "My body doesn't have a sensory organ that can pick up her signals."
            # m "Disappointed?"
            # s "Incredibly! I was hoping I could get some guidance from someone a little more similar to me."
            # s "But the person I'm looking for doesn't exist."
            # s "It's just me."
            # m "..."
            # s "Oh well. That is how the biscuit gets soggy."
            # m "You mean, that's how the cookie crumbles?"
            # "That's when her statement from earlier suddenly hits you like XXXX"
            # m "WAIT WHAT DO YOU MEAN \"EATING IT\"!"
            # s "Ack, again with the yelling..."
            # m "I think me being a bit agitated is understandable when you are suggesting cannibalism!"
            # s "But it is not cannibalism. I am not a human after all."
            # s "I saw it in your eyes too, the way you looked at my finger in your hand..."
            # s "You recognised me as different from you."
            # s "Also my purpose is to be consumed, with the proper supervision of course."
            # m "Proper supervision? I've cooked with mushrooms before..."
            # s "Oh I see, {size=-20}so he didn't do any research on my species."
            # s "I don't think it is appropriate to explain more here, let's head back if you're ready."
            # "Your curiousity is elevated by whatever is special about Sai's species."
            # "Oddly at that moment you realise that your usual sense of inadequacy seems a little bit quieter."

           

label eat_dirt:
    show mc confused
    m "Sai? What are you doing?"
    window hide
    show sai eat at left with easeinbottom
    window show
    s "*munch* Ee-ching shumshing."
    show mc surprised
    m "Wait... wasn't that... {i}dirt{/i}?"
    show sai eatdown
    s "Mhm *swallow*"
    show mc stressed
    m "I guess I've seen worse. I'd ask why, but... what's the point?"
    show mc normal
    m "Well, how did dirt taste?"
    show sai normal
    s "Silty, with a hint of home."
    "She reaches for a piece of gravel."
    show mc worried
    m "Wait! Are you sure it's okay to just eat random crap from the ground?"
    show sai normalside
    s "Uncertain. But this part of my face - it is called a mouth, I believe? - It can sense things..."
    show sai horny
    s "This experience of taste... "
    show mc stressed
    m "Okay, okay, I get it! But I think you should stick to restaurants if you want to eat!"
    show sai surprised
    s "Rizz-tow-rahnt?"
    show mc normal
    m "Yes. It's a place where you're actually MEANT to eat things. And they taste much better than random crap off the floor."
    show sai think
    s "Intriguing... So I would be able to experience new tastes there?"
    m "Yes, so put the gravel down."
    show sai happy
    s "Done."
    show mc vstressed
    m "Hah... so much stress. Let's go home now."
    window hide
    # if not_scold:
    #     show sai eat
    #     s "Just one more! *munch*"
    #     show mc confused
    #     m "Was that a tomato? Now you're eating the children of the plant you nearly killed?"
    #     show sai bleh
    #     s "Bleh. Sour."
    #     show mc cynical
    #     m "Yeah, the yellow ones are unripe and-"
    #     show sai eatdown
    #     s "*munch*"
    #     show mc surprised
    #     m "ANOTHER? I thought you said it tasted bad!"
    #     show sai eat
    #     s "I only mentioned that it was sour."
    #     s "I think I {i}like{/i} sour."
    jump sai_go_home_day1

label sai_go_home_day1:
    hide mc
    hide sai
    with easeoutbottom
    
    play sound "gate.wav"
    scene black with Fade(0.5, 1, 0.5)
    "You and Sai finally walk back home as the evening rolls in."
    "She gleams, at ease despite the whole severing-her-finger escapade."
    if has_finger:
        "You keep subconsciously patting the distended pocket where the finger lies."
        "Horrifying."
    window hide
    stop music fadeout(3)
    play sound "door.wav"

    
    scene black with fade
    show night_clouds
    show bedroom_opencurtains:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty1:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty2:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty3:
        matrixcolor TintMatrix("#6F6FBB")
    show bottle:
        matrixcolor TintMatrix("#6F6FBB")
    with Dissolve(2)
    play music "night.mp3"
    
    
    
    show day_1 at topleft
    show sai_affection at topright
    with dissolve
    show mc normal at right
    show sai happysigh at left
    with easeinbottom
    window show
    s "Ahh, what a fulfilling experience."
    show mc normalside
    m "Not a traumatic one?"
    s "Is it strange to you that I'm not bothered by the fact that my finger has been amputated?"
    show mc normal
    m "And what about the fact that you are a mass-produced object? Doesn't THAT bother you?"
    s "No. Everyone is, to a degree."
    show mc confused
    m "Does ANYTHING phase you?"
    s "Hmm... I feel solid currently. No changes in phase."
    m "(Talking with her is tiring...)"
    m "*Sigh* I'm hungry..."
    show sai surprised
    s "Ah! I'm afraid I can't allow you to do that."
    show mc normal
    m "You can't allow me... to eat?"
    show sai determinedclosed
    s "Not for the sake of satiating your hunger, no."
    m "What other reason is there to eat? Can't I just grab a bite somewhere?"
    s "A BITE? A full mouthful!? Certainly not! A full bite of me would easily kill you."
    m "..."
    m "Look, I know you're a mushroom and all, but I don't intend to eat you. I just want normal, human food. So relax."
    s "Why not? I would provide so many benefits to you."
    m "(First she was trying to stop me, now she's encouraging it? Pick a side!)"
    m "Benefits such as dying? Gee thanks, but maybe later..."
    s "In small amounts I am perfectly safe, and can help with your depression."
    show mc shocked
    m "(That again?)"
    show mc worried
    m "I don't have {i}that{/i}! I'm just lazy and procrastinate too much."
    show mc stressed
    m "My situation is my own fault, not because of any condition like that."
    s "Hmm... Regardless, you as an individual would benefit from a small nibble."
    s "I can assure you that I am a beginner-friendly psychoactive mushroom that can grant clarity to stressed individuals. And you are certainly stressed."
    show mc surprised
    m "Wait. What?"
    s "I can-"
    show mc stressed
    m "No, no, I heard you!"
    m "Jesus... You're a magic mushroom? Okay, I'm just telling you straight up - no matter what you say, I am NOT-"
    show mc normalsquint
    m "NOT eating a single piece of you."
    show sai normal
    s "..."
    show sai sad
    s "Understood."
    show mc surprised
    m "Oh. Well... good."
    s "..."
    m "..."
    show mc normalside
    m "Uh. Sorry. No offense."
    s "I'm not offended, just sad and disappointed."
    s "I expected this reaction. I am well aware of the stigma that surrounds me, so I don't blame you for distrusting me."
    m "I never said THAT. Sure I trust you! You're nice."
    s "Mm... nice, am I? I suppose that will have to do."
    m "..."
    s "..."
    m "Are you okay?"
    s "I'm busy processing my melancholy."
    "And it's all your fault."
    m "Um, want to... hang out?"
    s "That depends. Do you offer out of pity, or genuine desire?"
    m "I genuinely think watching a movie together would be better than this."
    show sai normal
    s "A... movie?"
    m "Oh, piqued your interest? Then come over. I'll put something on."
    hide mc
    hide sai
    with easeoutbottom
    "You open up your laptop, angle it to face the bed, and find a movie."
    "Sai solemnly sits on the bed next to you, but as soon as the movie starts..."

    show sai vsad at left
    show mc happy at right
    with easeinbottom
    m "So, what did you think?"
    s "*sniff* I feel devastated, yet inspired. Miserable, yet appreciative. In my opinion, the movie was beautiful work of art."
    show mc annoyed
    m "Heh."
    show mc happy
    m "(I'm glad she's cheered up.)"
    "Because it helps you feel less guilty?"
    m "What was your favourite part?"
    show sai determinedclosed
    s "Hmm..."
    show sai shy
    s "When he described himself as an onion, it resonated with me."
    menu:
        "Why did she resonate with that line?"
        "Because Sai is also a vegetable!":
            jump onionwrong
        "Because everyone hates onions?":
            jump onionright

    label onionright:
        $ sai_rp += 10
        show mc awkwardsmile
        m "Is it... uh, no offense again, but because everyone hates onions?"
        show sai worried
        s "Mm..."
        s "Yes. I sympathised with his pain. As well as in a literal sense."
        show sai vshy
        "I taste bad, not like the nice, normal mushrooms humans enjoy."
        show mc normal
        m "Why does that matter? You don't WANT to get eaten, do you?"
        show sai sad
        s "It's the only thing I'm good at. If you had one special quality that could help others, wouldn't you want to use it?"
        m "Not if it meant losing a part of myself!"
        s "Not lost. Nothing is ever physically lost. Only transformed."
        m "(I'm getting flashback to my old physics classes. \"Matter cannot be created or destroyed\", and all that...)"


    label onionwrong:
        $ sai_rp -= 10
        show mc confused
        m "Because you are also a vegetable?"
        show sai sad
        s "What? No..."
        show sai worried
        s "Just ignore me. This doesn't matter."
        "Way to mess it up, dumbass."
        show mc stressed
        m "(That was not the vibe.)"

    show mc normalside
    "You glance at your phone again. It's past midnight."
    "You should go to bed soon. But can you do it without going on your phone for hours until you're so exhausted you bonk out into sleep?"
    "You have a feeling Sai won't approve of that particular routine."
    







    #laundry scene below:
    # show sai think
    # s "*sniff sniff* After being in the fresh air, I've noticed a certain... \"pungeance\" in your bedroom."
    # show mc normalside
    # m "Sorry."
    # show sai sigh
    # s "It's a big affront on my nose. It seems to emenate from the pile of clothes."
    # show mc stressed
    # m "I know I should've cleaned it long ago. It's on my bucket list."
    # show sai surprised
    # s "Washing your clothes is on your bucket list? As in, things to do before you die?"
    # show mc normalside
    # m "Doing laundry isn't as easy as it looks."
    # show sai normal
    # s "..."
    # show sai happy
    # s "I'll help you."
    # show mc normalsquint
    # m "No, it's my mess. I have to sort it out. I don't want you going through my rubbish because I was too lazy to sort it out."
    # show mc stressed
    # m "I'll try deal with the smell. There's a air freshener in here somewhere..."
    # window hide
    # hide mc with dissolve
    # show sai normalside
    # window show
    # s "I thought it could be fun..."
    # window hide
    # show mc normal at right with dissolve
    # m "Alright, I found some bodyspray. I hope you like the smell of masculinity."
    # "You aim the nozzle at the steaming pile of body odour, and spray away the foul scent."
    # play sound "spray.wav"
    # show mc annoyed
    # m "The beast is slain."
    # show mc vstressed
    # m "*cough* God, it like a locker room in here."
    # show sai apologetic
    # show mc normal
    # s "Um, %(player_name)s? I would like to discuss somethings with you."
    # show mc confused
    # m "O...kay..."
    # show sai shy
    # s "Then... um..."

    
    # stop music fadeout 1
    # play music "trip.mp3"
    # show mc confused
    # show sai worried
    # s "There are things I know, and things I do not."
    # s "I know many words, yet sometimes, there are things you say that make my mind go blank."
    # s "It is the same for concepts and actions. These instances just remind me that..."
    # show sai apologetic
    # s "I'm so different to everyone else. I don't know who I am."
    # s "Me being a mushroom can cause awkward miscommunication problems."
    # show sai sigh
    # s "So I apologise in advance for all the mistakes I will continue to make."
    # show mc awed
    # m "No, it's okay. I get it."
    # show mc normal
    # m "Everyone starts not knowing everything. You've got you're whole life to learn words and concepts and all that."
    # m "You already learned new things today, so just keep it up."
    # show sai shy
    # s "I do like learning. But also caused you trouble today, like jumping out the window, forcing you to garden with me..."
    # show sai vworried
    # s "And you seemed taken aback by my arrival in the first place... Maybe I should just go."
    # show mc surprised
    # m "What? Sai, you're overthinking!"
    # show sai worried
    # s "Are you sure?"
    # show mc stressed
    # m "Yes!"
    # show mc normal
    # m "You're NOT a bother. It was good for me to get out. It helped me relax and... get out my head for a bit."
    # m "I liked gardening with you. The window thing is already solved - we'll use the stairs next time."
    # show sai happy
    # s "That is a relief. So I may continue to stay here in your wonderful residence?"
    # "\"Wonderful\"? You definitely can't understand that part..."
    # show mc annoyed
    # m "Uh, yeah."
    # show mc normal
    # m "Do you feel better now?"
    # show sai shy
    # s "Indeed. Thank you for communicating with me."
    # stop music fadeout 2
    # show mc annoyed
    # m "No problem. Sometimes, all you need is to hear a fresh persepctive."
    
    # play music "night.mp3"

    show mc sad
    m "(I keep wasting time...)"
    show mc stressed
    m "(No, I went outside today. I touched grass, er, dirt. That's progress. Every little thing helps.)"
    m "(Yeah! Maybe tomorrow, I can even go to the lecture without having a panic attack...)"
    m "(Maybe I can ask all the questions I need, and get help from a classmate, and...)"
    show mc normal
    m "It's getting late. I think I should sleep soon."
    show sai happy
    s "\"Late\"? Ah yes, humans like to time their activities to the position of the sun."
    show mc normal
    m "It's just a way to mark the end of the day."
    show sai normal
    s "Time is all relative. We are all just awake in one long stretch of existence..."
    show mc stressed
    m "No existential discussions right before bed, please."
    show sai surprised
    s "Oh, my apologies!"
    show mc normal
    m "It's okay. Anyway, I need to get to sleep. Will you be okay by yourself?"
    show sai normalside
    s "I shall be \"okay\". I shall meditate."
    show mc surprised
    m "Meditate? For like... eight hours? Nothing else?"
    show sai vshy
    s "You make it sound as if it is strange, but that's all I did while until I was harvested today."
    m "And you like that?"
    s "Yes. It's like removing myself, and simply feeling the state of being alive."
    show mc confused
    m "Uh... Okay. I don't judge. Do what you want. Good night."
    show sai confused
    s "\"Good night\"?"
    show sai happy
    s "Oh, I bid you a restful stasis. And thank you for the movie."
    jump cantsleep

    # m "Why are you asking such a thing in the first place?"
    # s "I trust your judgement. You have been alive for longer, so I'm certain you will know better than me."
    # m "Th-that's a lot pressure. I don't think I'm the best role model."
    # s "I still want to hear your opinions."
    # m "(I don't think my opinions are worth listening to. I'm not smart, or wise, all I have is mistakes that I still don't know the answers to.)"
    # m "Asking someone who is lost for directions won't be helpful..."
    # show sai shy
    # s "Haha, rhetoric? I'll play along."
    # show sai happy
    # s "You're wrong. Lost people may not know what to call the land, but they have still identified certain features through their experience."
    # s "So even if you feel lost, you still possess knowledge that is useful to me."
    # show mc normalside
    # m "I see. You just want to extract my knowledge."
    # show sai worried
    # s "Well, technically... but..."


    #  I have a question I would like to ask you."
    # show mc normal
    # m "Yeah?"
    # s "What do you think about"
    # show sai shy
    # s "...eating me?"
    # show mc surprised
    # m "Uh... where'd that come from?"
    # s "Please answer the question."
    # menu:
    #     "Do I plan on eating Sai?"
    #     "EW!":
    #         show mc normalside
    #         m "Even if I was originally going to make you into soup, that plan's changed."
    #         show sai surprised
    #         s "I was going to be turned into soup?"
    #         show mc normal
    #         m "But you're a sentient person who clearly wants to live, so I won't. What's the point of even bringing this up?"
    #         show sai normalside
    #         s "I just thought of it... I'm food. You're a consumer. I thought it might be the natural end to my life."
    #         s "But you seemed so disturbed by my arrival today, that I wasn't sure what your plan was."
    #         s "So instead of just anxiously wondering about how I'd die, I just asked."
    #         show sai shy
    #         s "Sorry, I'm rambling..."
    #         m "Morbid, but guess mushrooms gotta contemplate this kinda stuff eventually."
    #         m "Well, now you can relax. I'm not going to eat you."
    #         show sai apologetic
    #         s "..."
    #         show mc confused
    #         m "You don't look very relieved."
    #         show sai embarrassed
    #         s "Why do I... feel disappointed? I don't understand these emotions."
    #         show sai sigh
    #         s "The more I learned about myself, the more confused I get."

    #     "Your choice.":
    #         show mc normal
    #         m "Uh, I'll do whatever you want."
    #         show sai surprised
    #         s "M-me? But why would what I want matter?"
    #         show mc stressed
    #         m "(I don't wanna choose something so important for you! What if I choose wrong?)"
    #         "Ah, shifting it so SOMEONE ELSE has to make the important decision."
    #         m "I'm not a mushroom, so I have no idea what you'd want. What if you really want it?"
    #         m "I hardly know you. So you should be the one who decides what happens to you."
    #         show sai think
    #         s "..."
    #         show sai vshy
    #         s "But... What if you don't like how I taste? I'm not particularly... well-liked as a flavour."
            



        # "You're okay.":
        #     if sai_rp < 0:
        #         s "That's a relief. I was worried with how much trouble I'd caused you today..."
        #         s "I've never had to think about how my actions affected others."
        #         s "I don't want to negatively impact anyone, so I'll just listen to your advice."
        #     else:
        #         s "\"Okay\", neither positive, nor negative, yet still enough."
        #         s "I suppose I should have expected such an evaluation."
        # "You're obvlivious.":
        #     m "You're kinda weird."



    # show mc normal
    # m "Aight, I'm gonna order some food. You want anything?"
    # show sai surprised
    # s "I'm lost. What are you going to order your food to do? You can speak to them?"
    # show mc stressed
    # m "Nevermind. I guess this another one of those moments where you don't know something commonplace."
    # show mc normalside
    # m "You can have some bites from whatever I get. Maybe that quadruple-cheese pizza...?"
    # show sai normal
    # s "Oh, you mean the other definition of order: having food delivered to your house."
    # show mc annoyed
    # m "Congratulations."
    # show mc normalside
    # m "Wait, that's not a problem with you, right? Eating food in front of an edible thing could be considered threatening."
    # show sai shy
    # s "No, perfectly fine, I appreciate your concern."
    # show sai happy
    # s "I don't feel threatened by you anyway. You are weaker than me."
    # show mc normalsquint
    # m "Uh, rude."
    # show sai surprised
    # s "My apologies!"
    # show sai vshy
    # s "And I taste unpalatable anyway. I doubt you'd want to satiate your hunger with me."
    # show mc annoyed
    # m "So you taste bad? Doesn't that make you a failure of a mushroom?"
    # show sai sad
    # s "I... suppose..."
    # show mc surprised
    # m "Hey, that was a joke! You're not supposed to take it seriously."
    # show mc worried
    # m "Me and my stupid sense of humor... Sorry."
    # show sai shy
    # s "Please don't restrain yourself. The fact that we are two different species is already isolating enough."
    # show mc confused
    # m "Uh-"

    # window hide
    # hide mc
    # hide sai
    # with easeoutbottom
    # window show

    # "Using a new delivery app that you became popular recently, you are able to easily, and without phoning, receive a π32^2cm portion of unhealthiness."
    # window hide
    # show sai eat at left
    # show mc eat at right
    # window show
    # m "Mmmm"
    # s "Mhm! M m mmmmmm!"
    # show sai vhappy
    # s "Pizza is heavenly. Every bite is warm, gooey, salty and cheesy. May I have another slice?"
    # show mc happy
    # m "Heh, sure. Help yourself."
    # show mc confused
    # m "I'm glad you like it and all, but... you're sure it's okay for you to eat, right?"
    # show sai eathappy
    # s "Delicious! So scrumptious! Happiness radiates through me everytime I chew."
    # show mc normalside
    # m "(She {i}seems{/i} alright.)"

    




    # m "Haven't heard that one before. Maybe you should consider writing poetry as a job."
    # show sai worried
    # s "I'm sorry. You said that I could stay with you so I followed you back."
    # show mc confused
    # m "What are you doing?"
    # show sai vshy
    # s "Nothing really. Just introspecting. I'm a little thirsty though."
    # show sai shy
    # s "Could you do it, like you used to? It brings comforting memories of growing in oblivion."
    # "You can't say no to such polite pleading."
    # "You reach over and grab the spritzer."
    # window hide
    # hide mc with easeoutbottom
    # $ watered = 2
    # show water_status at water_location with dissolve
    # call screen water_sai_1 with dissolve
        

    # screen water_sai_1:
    #     imagebutton:
    #         xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
    #         action Jump("day1_watered_1")

    # label day1_watered_1:

    #     $ watered = 0
    #     queue sound "spray.wav"
    #     pause 1
    #     $ watered = 1
    #     queue sound "spray.wav"
    #     pause 1
    #     $ watered = 2
        
    #     show mc normal at right with easeinbottom
    #     show sai happy
    #     hide water_status with dissolve
    #     window show

    #     s "This water tastes like \"live, laugh, love\"."
    #     show mc confused
    #     m "All that... from bathroom water? O-kay..."

    # show sai normal
    # s "What are you going to do now?"
    # show mc annoyed
    # m "I'm procrastinating. Today's been tiring, so I deserve a break right?"
    # show sai sad
    # s "Right... sorry for the trouble today."
    # show mc normal
    # m "Trouble is good sometimes. I was literally dying of boredom."
    # show sai shocked
    # s "L-literally!? Then you're welcome!"

    # show mc awed
    # m "Yep, um... I kinda just wanna watch something for a bit. Do you mind if I put a movie on?"
    # show sai surprised
    # s "A \"movie\"! I-I know about that! That's a story on a screen!"
    # show mc confused
    # m "Er, congrats? So it's okay, right?"
    # show sai vvhappy
    # s "Yes yes! Certainly!"
    # show black with fade
    
    # "Don't get too excited, remember: High hopes-"
    # m "Low expectations. Yeah..."
    # s "Excuse me?"
    # m "Oh, nevermind me, just thinking I should go to bed soon. I need to start getting up earlier than usual to prepare for my lecture..."
    # m "I'll need to turn off the lights, though. Is that okay?"
    # show sai happy
    # s "I welcome the darkness of my childhood memories."
    # show mc confused
    # m "You sure you don't need anything, right? I'll be out for a while, so what are you going to do?"
    # show sai confused
    # s "I have much to ruminate. Attempted murder, gardening, amputation, alienation, taste..."
    # show sai happy
    # s "You go ahead and REM! I shall occupy myself."
    # show mc annoyed
    # m "Voluntarily thinking all night? I hope I don't join you. Good night."
    
    # jump cantsleep
    
    
    
    

    
# add this somewhere, material is good, just needs a home
    # "*Rattle*"
    # show mc confused
    # m "Sai... what are you doing?"
    # show mc confused at right with move
    # show sai normal at left with easeinbottom
    # s "Trying to open your window wider. There's a certain... \"pungeance\" in your bedroom."
    # show mc sad
    # m "You'll get used to it."
    # s "It's a big affront on my nose. I think the smell is baked into the pile of clothes."
    # show mc stressed
    # m "Sorry. I know I should've cleaned it long ago. It's on my bucket list."
    # show sai surprised
    # s "Washing your clothes is on your bucket list? As in, things to do before you die?"
    # show sai happy
    # s "If it means so much to you, why don't we just do it now? I'll help."
    # show mc normalside
    # m "Yeah... definitely... maybe later."
    # "The idea of having somebody else pick up your filth fills you with shame."
    # show sai normal
    # s "What are you doing now?"
    # m "Shut-eye."
    # show sai vvhappy
    # s "I'll join you too!"
    # m "That's not literal... you kinda miss the point sometimes. I forget you're just a day old." # ???
    # show sai surprised
    # s "Despite my age, I am a mature mushroom! I got harvested and everything."
    # show mc blushside
    # m "Okay, I'm sure you're mature physcially! I meant... emotionally? Mentally? Because you don't understand a lot of basic things."
    # show sai normal
    # s "Knowledge doesn't reflect maturity. Anyone, young or old, can know stuff."
    # s "Who cares if some slang words are new to me? I can grasp concepts like ego death, which is plenty complicated."
    # s "My knowledge about life is like a tree canopy. It's expansive, but there are a lot of random holes."

    # show mc normal
    # m "This has been a really... {i}interesting{/i} day, but I'm pretty tired and my brain is a mess, so I think I should go to sleep."
    # show sai vhappy

    # show mc surprised
    # m "Yeah, your day was pretty intense. Are you okay? Do you need to rest?"
    
    jump cantsleep
        # Continue high route - good vs bad trip                
        # Bad: Mistakes people as monsters, realism, thinks dying. Choice to call ambulance or die (actually dies. Says hope its worth it). If Make him die horribly/terrifyingly, eg. he runs into road, goes to hospital/parents find/gt dies/kicked out of school/so stressed he kills self. Genre changes/becomes scary/changes screen)
        # Good: Ephiphany, parents, good / true ending

        
            


label cantsleep:

    #goodnight screen:
    window hide
    hide sai
    hide mc
    with easeoutbottom
    hide day_1
    hide sai_affection
    with dissolve
    stop music fadeout(3)
    scene black with fade
    show chibi_sleep at truecenter with Dissolve(2)
    show top_text "You shut your eyes and wait for sleep to come." with dissolve
    pause
    show top_text "One hour... two hours... three hours... of breathing slowly and lying still." with dissolve
    pause
    show chibi_awake at truecenter
    show top_text "But the one thing you can't do is block out the whispers of worry inside your head." with dissolve
    pause
    show top_text "At some point, you accept that sleep isn't coming." with dissolve
    pause
    scene black with dissolve

    show night_clouds
    show bedroom_opencurtains:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty1:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty2:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty3:
        matrixcolor TintMatrix("#6F6FBB")
    show bottle:
        matrixcolor TintMatrix("#6F6FBB")
    with Dissolve(2)
    show mc vstressed at center
    with easeinbottom

    
    window show
    "Lack of sleep. Again."
    "You're wrecking your body at such a young age."
    "And those eyebags just make you look older."
    m "(Please don't remind me.)"
    # m "What's the time? Maybe I shouldn't check, else I'll know how tired to be tomorrow."
    # m "Nah, I'm too curious."
    # show mc shocked
    # m "HOW IS IT 4 AM!?"
    show mc sad
    m "Falling alseep used to be so easy..."
    window hide
    show mc at right with move
    show sai sigh at left
    with easeinbottom
    window show
    play music "night.mp3"
    s "Greetings..."
    show mc surprised
    m "Oh! Hey. I forgot I wasn't alone."
    show mc normal
    s "..."
    show mc confused
    m "Uh, how has your meditation been going?"
    show sai apologetic
    s "With great difficulty."
    show mc awed
    m "Meaning...?"
    s "Everytime I try to clear my thoughts, I succeed for at most five minutes. And then..."
    show sai vworried
    s "I think about tomorrow... and all the food I wish to taste!"
    show sai sigh
    s "Then my mouth begins to secrete strange fluids."
    show sai worried
    s "I don't know why, but my body is being very inconvenient while I'm trying to attain peace of mind."
    show mc annoyed
    m "You sure you're not just hungry?"
    show sai determinedclosed
    s "Hungry? No, I doubt it. Mushrooms don't need to eat, after all. It only starts when I start thinking about tomorrow..."
    show sai happysigh
    s "Ah, and I get so excited wondering what kind of textures and tastes I'll experience, how they will interact on the different zones on my tongue-"
    show sai annoyed
    s "Ugh. See? I can't relax! It used to be so easy when I was a young primordia."
    show mc normal
    m "(She must really like food.)"
    show sai worried
    s "My apologies. I think I babbled about topics in which you have no interest."
    show mc normalside
    m "Nah, it's nice hearing someone else talk for a change."
    show mc normal
    m "I think we both need to take a little break. Do you want to get some hot chocolate with me?"

    show sai surprised
    s "Hot. Chocolate?"
    show sai confused
    s "Is it dangerous?"
    show mc awed
    m "..."
    show mc annoyed
    m "Oh yeah. Super dangerous. You have to be careful, else your mouth will be burnt and won't be able to taste anything."
    show sai shocked
    s "WHAT!? I don't think this is a good idea, %(player_name)s!" with sshake
    m "Be adventurous. Hot chocolate is delicious."
    show sai sigh
    s "Delicious...? Oh, crumbs... What a conundrum."
    s "{size=-12}A new experience, and a chance to bond with my companion... yet at greak risk..."
    show sai shy
    s "I'll trust you. I shall consume the hot chocolate with you."
    show sai determined
    s "But with extreme caution."
    show mc normalside
    m "Then follow me to the kitchenette."
    stop music fadeout 2 
    
    window hide
    hide mc
    hide sai
    with easeoutbottom
    play sound "door.wav"

    scene black with fade

    show chibi_mc at slightright
    show chibi_sai at slightleft
    with easeinright
    window show

    "You lead Sai to the dormitory's kitchenette."
    s "What's a kitchenette?"
    m "...a small kitchen."
    s "How self-explanatory."

    window hide
    hide chibi_mc
    hide chibi_sai
    with easeoutleft
    jump minigametest

label minigametest:

    play music "trip.mp3"
    show kitchenette_base
    show microwave:
        xalign 0.92 yalign 0.08
    show mug:
        xalign 0.6 yalign 0.07
    show powder:
        xalign 0.53 yalign 0.48



    with fade
    show mc normal at right
    show sai happy at left
    with easeinbottom
    m "Alright. This is the kitchenette."
    m "Remember to wash up after yourself. I don't want anyone knocking on my door to complain about dirty dishes, got it?"
    s "Understood."
    show mc normalside
    m "I don't come here that much, since there's a risk of running into someone."
    show sai confused
    s "Then why don't you just walk?"
    show mc confused
    m "..."
    show sai surprised
    s "What curious machinery there is in here! What does-"
    show mc annoyed
    m "Shh, patience. You'll find out how everything works very soon."
    show sai normal
    show mc normal
    m "Alright, so I'm particular about how I have my hot chocolate."
    m "When you make it-"
    show sai shocked at bounce
    s "Wait wait wait! Me? As in, {i}I{/i} do it?"
    m "I thought you'd like it, being the curious creature you are."
    show mc confused
    m "Or was I wrong?"
    show sai vsad
    s "What if I mess it up again? Like the gardening! And since hot chocoolate is so dangerous-"
    show mc surprised
    m "Whoa, whoa, calm down! Just be slow and careful, and I'll look after you."
    show sai sad
    s "I am just worried. I just hope I can translate audio instruction into physical operation successfully..."
    show mc awed
    m "You can stop any time you want and I'll take over."
    show mc happy
    m "You're going to make your own delicious drink - isn't that something you're interested in? You were just thinking about new tastes, so I though you'd enjoy this."
    show sai determinedclosed
    s "You're correct. I am. I can do this!"

    window hide
    play sound "page.wav"
    show hot_chocolate_note with easeinbottom
    pause
    pause
    play sound "page.wav"
    hide hot_chocolate_note with easeoutbottom

    show sai determined
    s "Okay. I'm awaiting your instructions."
    show mc normal
    m "The recipe is simple: First, put a spoon of hot chocolate powder into a mug. Then add some milk and stir. Lastly, heat it in the microwave."
    s "Spoon. Powder. Mug. Milk. Microwave. - Spmmm! Got it."
    hide sai with easeoutbottom
    m "I'll supervise from over here, so just call me if you get stuck."
    
   

    # hide sai
    # hide mc
    # with easeoutbottom
    
    

    #--------------------- VARIABLES AT DEFAULT STATE

    $ hot_choc_hint = 0
    
    
    
    define mug_drag = Drag(d = "bg/gt/kitchen_minigame/mug.png", drag_name = "mug", focus_mask = True, align = (0.6,0.07), dragged = dragged_func)
    define milk_drag = Drag(d = "bg/gt/kitchen_minigame/milk.png", drag_name = "milk", focus_mask = True, align = (0.59,0.47), dragged = dragged_func)
    define spoon_drag = Drag(d = "bg/gt/kitchen_minigame/spoon.png", drag_name = "spoon", focus_mask = True, align = (0.46,0.52), dragged = dragged_func)
    define microwave_drag = Drag(drag_name = "microwave", d = "bg/gt/kitchen_minigame/microwave.png", align = (0.92,0.08), draggable = False, dragged = dragged_func)
    define hot_chocolate_drag = Drag(d = "bg/gt/kitchen_minigame/powder.png", draggable = False, clicked = clicked_func, drag_name = "powder", focus_mask = True, align = (0.53,0.48), dragged = dragged_func)
    define drawer_drag = Drag(drag_name = "drawer", d = "bg/gt/kitchen_minigame/drawer_closed.png", align = (0.545,0.725),focus_mask = True, draggable = False, clicked = clicked_func, dragged = dragged_func)
    define cutlery_drag = Drag(drag_name = "cutlery", d = "bg/gt/kitchen_minigame/utensils_hover.png", align = (0.545,0.725), focus_mask = True, draggable = False, clicked = clicked_func, dragged = dragged_func)
    define fridge_drag = Drag(drag_name = "fridge", d = "bg/gt/kitchen_minigame/fridge_closed.png", align = (0.956,0.999),focus_mask = True, draggable = False, clicked = clicked_func)
    
    
    define my_draggroup = DragGroup(fridge_drag, drawer_drag,microwave_drag, hot_chocolate_drag, mug_drag)

    #---------------------

    

    window hide
    #$ renpy.force_autosave() 
    #$ renpy.notify("The game has been automatically saved.")
    scene kitchenette_base
    #hide mug with dissolve

    $ config.rollback_enabled = False

    call screen make_hot_chocolate_1 with dissolve
    
    jump hot_chocolate_made

    screen make_hot_chocolate_1:
        

        add my_draggroup


        imagebutton: #MC
            
            idle "bg/gt/kitchen_minigame/mc_idle.png" hover "bg/gt/kitchen_minigame/mc_hover.png" focus_mask True 
            action Jump("ask_mc_help")

      
    

    label ask_mc_help:
        
        show mc happy at right
        show sai happy at left
        with easeinbottom
        m "Need help?"
        menu:

            "Repeat recipe please.":
                
                if hot_choc_hint == 0:
                    
                    show mc normal
                    m "Hot chocolate is simple. It's just two things: hot chocolate powder and milk."
                    m "So grab a mug from the shelf and put in some powder."
                    m "The powder's there on the counter. And just so we're clear, you need to find and use a spoon to scoop it out, not your hands."
                    show mc normalside
                    m "So yeah, powder, then milk..."
                    m "And then, obviously, you need to make it hot."
                    show sai confused
                    s "How?"
                    show mc annoyed
                    m "The magical grey box on top of the fridge can do that."
                    show sai surprised
                    s "So it's as easy as that? Technology is truly incredible..."
                    window hide
                    hide sai
                    hide mc
                    with easeoutbottom
                    call screen make_hot_chocolate_1 with dissolve
            
                    

            "I give up!":
                show mc annoyed
                m "It's okay. Just watch and learn."
                window hide
                scene black with fade
                play sound "drawer_open.wav"
                pause 1
                play sound "fridge_open.wav"
                pause 1
                play sound "microwave.wav"
                pause 1
                show kitchenette
                show sai surprised at left
                show mc happy at right
                with dissolve
                jump hot_chocolate_made
                

label hot_chocolate_made:  
    $ renpy.block_rollback()
    $ config.rollback_enabled = True
    
    show sai surprised at left
    show mc normal at right
    with easeinbottom
    window show
    s "There's a strange smell in the air..."
    show mc happy
    m "It's good, right? And you haven't even tasted it yet."
    show sai worried
    s "I want to, but it's dangerous. How will I prevent myself from destroying my mouth?"
    show mc annoyed
    m "Haha, I was just pulling your leg. It's not THAT hot."
    show sai confused
    s "My leg? {size=-8}I didn't even notice..."
    show mc happy
    m "Go on, sip it."
    show sai eatdown
    s "*Sip*"
    show sai eathate
    s "..."
    show mc cute
    m "Well?"
    show sai eat
    s "*Increased sipping*"
    show mc annoyed
    m "I knew you'd like it."
    show sai vvhappy
    s "Haahh~ How creamy and sweet!"
    m "I know, right? my method's the -"
    show sai excited
    s "It's absolutely disgusting!"

    show mc shocked
    m "WHAT?"
    show sai shy
    s "This is my first time tasting something I disliked!"
    s "My brain feels overwhelmed from the sweetness, as if a bee is stinging my frontal lobe."
    show sai think
    s "Hating a taste has been such a fascinating experience."
    show sai happy
    s "Thank you for showing me hot chocolate."
    show mc worried
    m "Y-you're we-welcome...?"
    show mc stressed
    m "(Guess she just doesn't have a sweet tooth. That's a shame. I wish we could have enjoyed it together. I was having fun...)"
    show mc confused
    m "Do you really hate it THAT much?"
    show sai vshy
    s "I'd rather eat the dirt again, hehe..."
    show mc surprised
    m "Damn. Alright."
    show sai happy
    s "But {i}you{/i} like it, right? Would you like to finish mine?"
    show mc happy
    m "(Oh HELL yeah! Double hot chocolate.)"
    window hide
    scene black with fade



    "You fill yourself with milky goodness, help Sai wash the dishes, then head back to your bedroom together."
    
    window hide
    stop music fadeout 2
    hide sai with dissolve   
    
    show chibi_sleep at truecenter with Dissolve(2)
    
    show top_text "Stomach brimming with warmth, mind empty of all but the need of a pillow, you burrow into your blankets." with dissolve
    pause
    show top_text "And sleep carries you away on a fuzzy cloud..." with dissolve
    with dissolve
    pause
    scene black with fade
    jump morning2

    #Can pop bubble to have a dream of family and finger."

label morning2:
    
    #show bedrooom_sai_morning2 with dissolve

    play music "phonealarm.ogg" fadein 2
    pause 2
    image blurry_sai = im.Blur("images/sprites/sai/sai surprised.png", 2)
    show blurry_sai
    with dissolve
    pause 0.2
    window show
    s "Um, %(player_name)s...? This blue rectangle is wriggling and making a strange sound..."
    m "\'S too early for talk. Shhhh..."
    "You instinctively turn off your first alarm."
    window hide
    stop music
    scene black with fade
    pause 2
    play music "phonealarm.ogg"
    window show
    m "Ughh..."
    window hide
    show day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show dirty3
    show bottle
    show black:
        alpha 0.5
    with Dissolve(2)

    
    
    show day_2 at topleft
    show sai_affection at topright
    with dissolve
    show sai happy with easeinbottom
    s "Greetings. Are you awake now?"
    stop music
    m "No... sn..."
    show sai surprised
    s "Huh...?"
    show sai annoyed
    s "What a strange waking ritual..."
    show sai think
    s "Aren't humans diurnal creatures?"
    play music "normal.mp3" fadein 3
    window hide
    show sai at left
    with move

    show mc sad at right
    window show
    m "...Theoretically."
    show sai happy
    s "You're awake now?"
    show mc stressed
    m "Ugh, it doesn't count if I stay in the bed.... on my phone."
    show sai confused
    s "Is this a form of procrastination?"
    "She's right. You dread the day ahead. You're delaying starting it."
    "Your body feels like a potato sack. Devoid of energy. Wishing for stagnation."
    "It's going to be another bad day. You wish you could skip to the end of it."
    m "I don't think today's the day."
    s "What's that mean?"
    m "It means go on without me."
    show sai happy
    s "I see you're struggling to move. Do you want me to push you out of bed?"
    show mc vannoyed
    m "I'll break your arms."
    show sai shocked
    s "I-I was just trying to help!"
    show mc stressed
    m "Sorry. I'm just feeling like shit."
    show sai worried
    s "Like... \"shit\"? I don't understand."
    show mc normal
    m "I hardly slept, so what do you think? I'm dead tired."
    show sai happy
    s "You remind me of a sedentary stone, covered in moss. You should roll!"
    show mc normalsquint
    m "What...?"
    show sai shy
    s "It's a joke. Because a rolling stone gathers no moss. And you have to move-"
    show mc stressed
    m "That pathetic excuse for a joke was so bad that I'm getting up."
    show sai normalside
    s "But I thought it was clever... maybe I need to work on execution?"
    show mc annoyed
    m "You can execute me."
    show sai surprised
    s "Uh..."
    show sai worried
    s "Um, anyway..."
    "Looks like Sai can't appreciate a good self-deprecating joke."
    "Don't worry! That's what I'm here for! HAHAHA!"
    show sai shy
    s "So... yesterday you said we could go to a \"res-tau-rant\"."
    show mc confused
    m "Huh?"
    show sai happy
    s "At the community garden, remember?"
    show mc stressed
    m "That was just to stop you from eating literal dirt..."
    show sai sad
    s "..."
    s "So... we're not going? I won't get to taste new things?"
    show mc vstressed
    play sound "stomach_rumble.mp3"
    m "{sc=2}{color=#000000}*stomach rumble*" # put obvious stomach growling sfx # make the implication that hes hungry
    play sound "stomach_rumble.mp3"
    s "..."
    show mc shout
    m "Okay, shut up!"
    show sai shocked
    s "But, I-I wasn't-"
    show mc vannoyed
    m "I set aside a couple of hours after waking to scroll on my phone anyway. So I have some time before class."
    m "I may as well just do whatever you want."
    show sai worried
    s "Um... we don't have to-"
    show mc normalsquint
    m "I made a promise. Now I gotta do it. That's all there is to this."
    show sai vshy
    s "Well... thank you, I suppose."
    show mc normal
    m "Since you've been looking forward to it so much, I'll take you to this café I've wanted to check out anyway."
    show sai confused
    s "\"Ca-fay\"? But I thought we were going to a res-tau-rant?"
    show mc normalsquint
    m "Sai... It's the same thing."
    show sai surprised
    s "Oh, okay..."
    show sai worried
    s "I got confused again. Sorry."
    show mc normalside
    m "Let's go get breakfast. Come on."
    show sai shy
    s "How thrilling this is! I am excited to experiment with my mouth."
    show mc vstressed
    m "Ugh... What you say scares me sometimes."
   
    window hide
    hide sai
    hide mc
    
    with easeoutbottom #FIX 
    play sound "door.wav"
    hide day_2
    hide sai_affection
    with dissolve
    
    stop music fadeout(3)
    scene black with Fade(0.5, 1.0, 0.5)  

    
    show chibi_mc at slightright
    show chibi_sai at slightleft
    with easeinright
    window show

    "You force your poor, sleep-deprived body up and outside."
    "You didn't get to go onto your phone like usual, so you're just left feeling uncomfortably present."
    "There's a lot of people moving around in the morning, which you usually get to avoid."
    "You just clench your jaw and focus on walking forward, trying to keep as calm as possible."
    # "Soon, you reach your destination: a cute café you've been too intimidated by to enter alone."
    # "Looks like it's nearly empty."

    window hide
    hide chibi_mc
    hide chibi_sai
    with easeoutleft
       
    play sound "bell.wav"
    jump cafedate


label cafedate:

    play music "cafe.mp3"
    scene cafe with Fade(0.5, 1.0, 1)
    show mc normal at right
    show sai surprised at left
    with easeinbottom
    show mc normal
    window show
    s "How strange. It is as if a garden was brought inside."
    show sai happy
    s "I quite like it."
    m "Where do you wanna sit?"
    show sai think
    s "Hmm... each table has its own charm... How about there?"
    m "Right next to the entrance? Uh, no."
    show sai normal
    s "Then, over there?"
    show mc confused
    m "But that's right next to the only other occupied table."
    show sai confused
    s "Um... then... there?"
    show mc stressed
    m "It's too close to the window. I don't want people to see me."
    show sai pout
    s "This is futile. Please, pick your ideal spot, %(player_name)s."
    show mc normalside
    m "Sorry I'm picky. Let's sit over here."
    show sai shy
    s "With all these plants surrounding me with their refreshing scent, I feel like I am in a tropical rainforest."
    show mc normal
    m "Hey, put your feet on the ground when you sit on a chair."
    if bad_route:
        show sai normal
        s "Okay."
        show mc normal
        m "Good. It's better not to bring too much attention to ourselves."
        m "You should look at the menu and tell me what you'd like to drink."
        show sai shy
        s "Um... I can't read. Could you pick for me?"
    else:
        show sai surprised
        s "Why? I find this more comforable."
        show mc normalside
        m "True. But it's {i}rude{/i}."
        show sai think
        s "How can sitting a certain way be offensive? Human customs are ludicrous sometimes."
        show mc normalsquint
        m "It's called having manners. Even if it's uncomfortable, at least people won't-"
    window hide
    show waiter normal at center:
        xanchor 1.0
        xoffset 500
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    with easeinbottom

    show mc shocked at bounce
    show sai shocked at bounce
    show pulsingblack with dissolve
    w "{size=*1.2}MY NAME'S M̸͖̤̬̟̈́̎̾̔̀̄̒͊́̾̀͊͘̚ę̸̨̗̙͚̤̺͕̭̭̰̠̄̓̑̂͐͛̒̑̄͜͠ͅĺ̷̨̜̝̤̗͔͕̥͈̮͖̣̃̐͐̂̀̿̎̚̚͠ͅa̴̡̫͉̩̺̰͕͓̎͒̏̀̐̂̋͐̀̓̊͝͠n̸̨̯̙̺̣̠͈̺̕i̴͖͈̻̬͚̙͔̼̹̇̾̃́̄̓͝͝ͅe̵͈͇̽̋̈́̑͆͘  AND I'LL BE YOUR WAITRESS. WHAT CAN I GET YA'LL TO DRIIIINK?"
    show mc worried
    m "E-Ehem. Uh... D-D-Do you have any... coffee milkshakes?"
    w "{size=*1.5}OF COURSE WE DO!\n AND FOR {b}YOU{/b}?"
    show sai surprised
    s "Co-ffee?"
    w "{size=*1.5}YESSSS. WE'VE GOT CAPPUCINO, ESPRESSO, AMERICANO, LATTE..."
    show sai confused
    s "Uh..."
    w "{size=*1.5}... MOCHA, FLAT WHITE, MACCHIATO, CORTADO..."
    m "(All of this is going over my head. But Sai's got this, right?)"
    w "{size=*1.5}\nSO WHAT WOULD YOU LIKE?"
    show sai shy
    s "Uh, you can choose for me, %(player_name)s."
    show mc shocked at bounce
    m "(OH NO!)"
    
    hide w_normal
    show blank_1 at center:
        xanchor 1.0
        xoffset 500
    with dissolve
    show mc stressed at quiver
    "Now the waitress is staring at YOU."
    "What should you say?"
    show sai normal
    s "%(player_name)s?"
    show mc shout
    m "Um...!"
    "You have to ask for a coffee. Otherwise that whole list she gave will have been for nothing!"
    m "J-just a... normal coffee please?"
    w "{size=*1.5}\nWHAT {i}KIND{/i}?"
    show mc vstressed
    m "..."
    "The only word your anxious brain can recall is the one that sounds like a train. Express-o."
    m "A-a-a an ex-press-o, p-please."
    
    hide blank_1
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    with dissolve
    w "{size=*1.5}COFFEE MILKSHAKE AND AN \nESSPRE{b}SSSSS{/b}O, COMING UP!"
    hide waiter
    hide w_normal
    with easeoutbottom
    show mc vstressed at nothing
    hide pulsingblack with dissolve
    "That prolonged S was on purpose, wasn't it? She was correcting you. You've made a {b}fool{/b} of yourself!"
    show mc stressed
    m "(I may have taken some emotiomal damage, but I survived the first battle. It's been a while since I went to a restaurant...)"
    show mc worried
    m "Okay. We should probably decide what food we're getting now before she comes back."
    show mc normal
    m "Anything you want to eat in particular? A salad?"
    if bad_route:
        show sai vshy
        s "May I try some meat?"
        show mc awed
        m "..."
        show mc normal
        m "No. Mushrooms don't eat meat. You'll get sick."
        show sai vhappy
        s "I know it sounds weird, but I want to try a variety of things. And I think meat-"
        show mc stressed
        show sai surprised
        m "No. Don't be stupid."
        show mc happy
        m "You said you trusted me right? Let me choose for you this time, and I'll get you something delicious."
        show sai worried
        s "Um... I do trust you. But-"

    else: 
        show sai shy
        s "I was thinking about it last night..."
        s "May I try some meat?"
        show mc surprised
        m "Meat?"
        show sai happy
        s "Indeed."
        show mc confused
        m "But I thought you cared about animals!"
        m "Didn't you just say yesterday you never want to hurt another creature?"
        show sai vshy
        s "It's a little complicated. I want to experience the savagery of killing conscious things and eating them. I'm curious how humans live with the guilt."
        m "..."
        show sai shy
        s "And I'm really curious... is animal meat so desireable that it is worth killing animals for?"
        show sai happysigh
        s "So I wish to try it and make my own deductions."
        show mc normalside
        m "Plants and dirt I get, but are you sure mushrooms can physically eat -"
    
    show waiter platter at center:
        xanchor 1.0
        xoffset 500
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    with easeinbottom
    
    # show waiter platter at center with easeinbottom:
    #     xanchor 1.0
    #     xoffset 500
    show mc shocked at bounce
    show sai shocked at bounce
    show pulsingblack
    with dissolve
    w "{size=*1.5}\nYOUR DRINKS."
    play sound "put_down_drink.wav"
    show waiter normal at center with dissolve:
        xanchor 1.0
        xoffset 500
    w "{size=*1.5}READY TO PLACE\nYOUR FOOD ORDER?"
    show mc worried
    m "(Oh my God - Oh my God - Oh my God-)"
    show mc vstressed at quiver
    m "(I'm not ready! I don't know what to get!!!)"
    
    m "Um...!"
    show mc worried
    m "C-Can I..."
    "Your frantic gaze lands on the blackboards above your head. You notice 2 specials."


    if bad_route:
        show sai worried
        menu:
            "What should I get for Sai!?"
            "Salad.":
                show mc worried
                m "A pasta salad for her, please."

    else:
        show sai happy
        menu:
            "What should I get for Sai?"

            "Salmon eggs benedict.":
                $ benedict = True
                show mc worried
                m "Um, for her, a salmon eggs benedick - BENEDICT! Uh, I mean benedict."
            # "Mushroom pizza.":
            #     $ pizza = True
            #     show mc worried
            #     m "Mushroom pizza, for her, please."
            #     show sai surprised
            #     s "Mushroom?"
            #     m "I-I thought it could be interesting..."
            #     show sai think
            #     s "Well, I suppose cannibalism could be a unique experience."
            "Custard slice.":
                $ custardslice = True
                show mc awed
                m "(Everyone loves dessert!)"
                m "A-a custard slice, please."

    w "{size=*1.5}EXCELLENT CHOICE!\nAND FOR YOU, {i}SIR{/i}?"
    "Now you look at another blackboard. You notice 1 thing."
    show mc confused
    m "Mm... may I have a prego roll, please?"
    w "{size=*1.5}HOW'D YOU LIKE YOUR \nEGG?"
    show mc worried
    m "Uh..."
    
    w "{size=*1.5}SUNNYSIDE UP OR \nOVER EASY?"
    m "Um... {size=-4} what...{size=-6} does...{size=-6} that...{size=-6} mean...?"
    "Everyone is supposed to know what they mean. If you ask her, you'll just embarrass yourself EVEN MORE."
    show mc stressed
    m "U-um...!"
    hide w_normal
    with dissolve
    stop music
    "Five seconds have passed of you staring blankly into her eyes. Her expression is a void of waiting. Waiting."
    play music "heartbeat.wav"
    
    "She's waiting."
   
    "You're taking too long."
    "You look around the room."
    "You look back at her."
    "She's still staring at you."
    "She clears her throat."

    show mc vstressed
    m "(I can't think. I can't decide!)"

    if bad_route:
        show mc worried
        m "Actually, I'm not hungry, haha! This milkshake is enough for me, thanks!"
        
    else:
        show mc cry
        "Mentally frozen, you look at Sai pleadingly."
        show sai surprised
        s "..."
        show sai vvhappy
        s "Go for over easy. That means you can eat it more easily, right?"
        show mc stressed
        m "Over... easy... p-p-please...!"
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    play music "cafe.mp3"
    w "{size=*1.5}GOT IT!\nENJOY YOUR DRIIIIINKS!"
    window hide
    hide waiter
    hide w_normal
    with easeoutbottom
    hide pulsingblack with dissolve
    show mc sad
    window show
    m "Hahhhh..."
    m "(My hands are actually trembling. This is so embarrassing.)"
    "You must be the only person in the world who is so afraid of interacting with strangers."

    if bad_route:
        show mc stressed
        m "And now I don't get to eat, all because I couldn't order... What a waste."
        show sai surprised
        s "Are you alright? You seem kind of stressed."
        show mc annoyed
        m "I'm fine."
        show sai worried
        s "Okay..."
        show mc normalside
        "..."
        ".."
        "."
        "You can tell from her expression: She's not grateful. She's disappointed and resentful. She's souring the atmosphere and ruining your appetite."
        "The audacity! Even though it's coming out of your pocket!"
        "Is she trying to punish you for choosing for her? Didn't SHE say she trusted you? What's with this?"
        "Clearly, it's up to you to clear the air."
        show mc normal
        m "Do you like your coffee?"
        show sai happy
        s "I really do. It's nice and bitter! So strong too!"
        show mc normalside
        m "Cool..."
        s "Do you want some?"
        show mc vannoyed
        m "I don't like black coffee."
        show sai normal
        s "..."
        show sai happy
        s "Your milkshake looks nice! Aren't you going to try it?"
        show mc normalside
        m "Maybe. I've lost my appetite."
        show sai vvhapppy
        s "If you don't want it, I'd be happy to have it. I'm interested in trying all kinds of flavours-"
        show mc stressed
        m "Sorry, I don't like sharing my food."
        show sai vshy
        s "No problem..."

        scene black with fade
        stop music fadeout 3
        "You wait patiently for Sai to finish her meal."
        "Then, you go straight home."
        jump night2



    show sai normalside
    show mc at nothing
    s "I still can't believe such a place exists where someone brings you things to put in your mouth."
    show sai vshy
    s "Thank you for bringing me here, %(player_name)s. It is so exciting!"
    show mc awkwardsmile
    m "(I'm glad at least someone here is enjoying themselves)."
    show sai horny
    s "Let's try out this so-called \"cough-fee\". It smells so... warm."
    show mc awed
    "At that moment, you realise what the waitress has brought-"
    "The tiniest cup you've ever seen. Filled with pure black liquid."
    show mc vstressed
    "Why's it so small!? Where's the milk? Is that just pure ass black coffee??? Oh no... you messed up yet AGAIN!"
    show sai eatdown
    s "*Sip*"
    show sai happysigh
    s "Ah~ What a unique flavour."
    show mc sad
    m "Don't have to be polite. Just admit it."
    show sai surprised
    s "Admit what? That I love it?"
    show mc surprised
    m "Huh? You do? Wow... weird..."
    show sai happy
    s "How's your \"milkshake\"?"
    show mc eat
    m "*Slurp*"
    "Cold, sweet, revitalising deliciousness floods your tongue."
    show mc annoyed
    m "Ahhh... I really needed this. I love milkshakes."
    show sai surprised
    s "It's very large... May I try please? And you can try mine."
    "Not really paying attention, you two swap drinks. As you sip it, the acidic, dark flavour makes your tongue cringe."
    show mc vstressed at bounce
    show sai bleh at bounce
    m "Eugh! Sour!"
    s "Eugh! Sweet!"
    show mc surprised
    m "Whaaat? How do you like this crap more?"
    show sai vshy
    s "I like my expresso. So nice and bitter."
    show mc confused
    m "...\"Nice and bitter\"? Those words don't belong together. Bitterness is objectively bad."
    show sai normal
    s "No, that's {i}subjective{i}."
    show sai determined
    s "You can't classify tastes as good or bad. They're just different experiences. Please, return my drink at once."
    show sai normal
    show mc normal
    "You swap drinks again, and she takes another sip of her espresso while you gladly slurp your drink."
    show mc blushside
    m "(Wait, isn't this an indirect kiss? I should turn the straw over.)"
    "Don't be so childish! You're supposed to be an adult, aren't you?"
    "Still, you flip the straw over, drink and instantly feel more at ease."
    show sai happysigh
    s "Mmm~ so amazing~"
    show mc surprised
    m "You really like that coffee."
    show mc confused
    m "I've been meaning to ask, Sai - Why do you like eating so much? You don't need to eat, so is it just for the taste?"
    show sai shy
    s "Well, no... there's a little more to it."
    show sai horny
    s "Whenever I taste something for the first time, I feel..."
    "...Like I understand life."
    show mc surprised

    s "By eating life, I complete it. When I absorb it, it becomes me. I am now with it. We are all... one. It is a beautiful harmony of existence."
    show sai vblush
    s "Tasting its unique composition, appreciating the textures and flavours, is like saying \"I love you\"."
    s "And having it inside me, is like saying, \"You'll live forever\"."
    show sai vshy
    s "So, getting to be a part of that process fulfills me."
    show mc awed
    m "Damn-"
    
    
    
    #  # make line better
    # show mc normal
    # m "At least we like our own drinks. Sorry, I can't relate to liking black coffee."
    # show sai surprised
    # s "Maybe you could. Let me try explain..."
    # show sai confused
    # s "It's like... do you like the horror genre? Things that scare you?" # rewrite the phrasing here because she might not know about movies or such
    # show mc awed
    # m "Uh, yeah. I like scary movies and books."
    # show sai happy
    # s "Horror and bitterness are the same. You'd probably classify both as objectively \"bad\" experiences. But you're still trying to get scared despite that!"
    # show sai vhappy
    # s "It's fun because you go in anticipating the shock, looking forward to it, really excited to feel it..."
    # show sai vvhappy
    # s "So do you want to try that, and have another sip?"
    # show sai shy
    # s "I don't mind, but if it bothers you to share to same cup as me, you can drink from the other side."
    # menu:
    #     "Do I want to try it again?"
    #     "Nah":
    #         show mc annoyed
    #         m "Maybe next time-"
    #     "Be a chad and drink":
    #         show mc annoyed
    #         m "Nah, I don't mind. I'll try-"
            

    
    
    show waiter platter at center:
        xanchor 1.0
        xoffset 500
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    with easeinbottom
    show mc shocked at bounce
    show sai surprised at bounce
    show pulsingblack
    with dissolve

    w "{size=*1.5}YOUR FOOD HAS \nARRIVED!"

    
    show waiter normal at center:
        xanchor 1.0
        xoffset 500
    with dissolve
    play sound "put_down_drink.wav"
    w "{size=*1.5}PLEASE \nENJOY!"
    show sai happy
    s "Thank you!"
    show mc stressed
    m "Th-thanks..."
    hide w_normal
    show w_laugh at center:
        xanchor 1.0
        xoffset 500
    show mc vstressed at quiver
    w "{size=*1.5}AAAAALWAYS A \nPLEASURE!"
    window hide
    hide waiter 
    hide w_laugh
    with easeoutbottom
    hide pulsingblack with dissolve
    show sai normal
    window show
    s "Is something bothering you, %(player_name)s?"
    show mc worried at nothing
    m "I-It's nothing. I'm fine. Don't worry about me."
    show sai think
    s "I've noticed a pattern. Whenever the foodbearer arrives, your face contorts into such a strained expression-"
    show mc stressed
    m "I said it's fine! Just ignore me and focus on enjoying your meal."
    show sai worried
    s "I'm sorry... I didn't mean to offend you."
    m "..."
    show sai shy
    s "I shall do as you say, and ignore you while focusing on enjoying my meal."
    show mc shocked
    "Sai digs into her meal! Literally! With... her hands..."
    show mc sad
    "Do you even really care at this point?"
    
    m "(Just let her eat however she wants. I'm so over stressing about every little thing.)"
    "You lift the top bun off your roll. It turns out \"over-easy\" means the egg was fried on both sides but still has a runny yolk."
    "Stupid food terminology."
    "Feeling annoyed, hungry, stressed, and apathetic all at the same time, you eat your prego roll, expecting it to taste just as bad as you feel."
    show mc surprised
    m "!"
    "Damnit! It's REALLY good! You're losing your negativity!"
    "You look over at Sai to see how she likes her meal."
    show sai eat
    s "*Biting*"
    window hide
    stop music fadeout 2
    show sai_affection at topright
    with dissolve
    

    

    if benedict:
        show sai eathappy
        s "Mmm... MMmmm....MMMMMM..."
        show sai eatvhappy
        s "MMMMM! MMMMMM!"
        $ sai_rp += 10
        show mc surprised
        m "You really like it?"
        s "{sc=3}{color=#000000}{size=+40}MMMMMMMMMMMMMMMMM!"
        s "{sc=3}{color=#000000}{size=+40}MMMMMMMMMMMMMMMMMMMMMMMMMMM!"
        s "{sc=3}{color=#000000}{size=+40}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-!"
        show mc worried
        m "Shhhh! Stop- stop moaning so loud! People are going to look!"
        hide sai_affection with dissolve
        show sai eathappy
        s "I'm show showwy, bu ish show goog!~"
        show mc vstressed
        m "I can see that. Just moan internally okay!?"
        play music "cafe.mp3"
        show sai shocked
        s "*swallow* What a divine experience!"
        # show sai shocked
        # s "I can see God."
        # show mc shocked
        # m "It's that good!?"
        show sai excited
        s "Smoky, sweet, tart, saucy, liquid and rough - what a combination! It's a flavour explosion!"
        show sai sad
        s "It's so wonderful... that I feel like crying."
        show sai vsad
        s "I'm so hopelessly happy!"
        show mc surprised
        m "(You sure about that!?)"
        show sai sad
        s "I'll never be able to taste this good. I'm not even tasty by myself."
        show mc awed
        m "How do you know how you taste?"
        show sai vshy
        s "Um... well..."
        show mc normalsquint
        m "Sai... You didn't."
        show sai sigh
        s "I was just so curious! And I'd already lost a finger, so I just cleaned up the wound a little and made it all nice and straight."
        show mc vstressed
        m "..."
        show sai worried
        s "I tasted dusty. Not interesting, especially compared to this. I don't know why I was so disappointed. It makes sense."
        m "For the sake of my mental health, I'm just going to ignore your auto-cannibalism and skip straight to reassuring you."
        show mc normal
        m "Ingredients taste differently depending on how they're cooked."
        show mc annoyed
        m "The delicious food you just ate isn't just raw stuff put together."
        show sai surprised
        s "So there's hope for me?"
        show mc stressed
        m "Why are you even bothered by how you taste?"
        show sai shy
        s "Uh... I'd rather not disclose that."
        show mc normal
        m "Is it because you want to be eaten?"
        show sai shocked
        s "!"
        show mc normalside
        m "Yup. It's obvious."
        show mc confused
        m "But why?"
        show sai worried
        s "Well, I {i}am{/i} a mushroom."
        show sai vshy
        s "It's my fate, isn't it? I'm meant to be eaten. Is it wrong to want someone to enjoy my flavour?"
        show mc stressed
        m "What the hell? You're NOT like other mushrooms. You're sentient!"
        m "You've got your whole life ahead of you. You can do anything! But this just sounds like you're planning to die."
        show sai vworried
        s "No, that's not it..."
        s "I'm sorry. I'm failing to express myself properly. Can we go back to enjoying our food?"
        show mc normalside
        m "Yes please."

        
        # s "What else would I do with my corpse? Compost it? That would be such a waste."
        # show mc confused
        # m "Compost isn't a waste. You'd nourish other plants."
        # show sai normal
        # s "Yes, but... I mean that my unique properties won't be utilised."
        # m "Unique properties?"
        # show sai surprised
        # s "Of course, I-"
        # show sai shocked
        # "Oh! Um! Could I please have a bite of your food? It's making me salivate..."
        # show mc happy
        # m "We can share if you want."


    # elif pizza:
    #     show sai surprised
    #     s "Still good, and it tastes so different from the one we consumed last night."
    #     s "The crust is thinner, the cheese tastes stronger, and these button mushrooms are so soft and tender."
    #     show sai eathappy
    #     s "I think Button would have been happy to be eaten like this. She's delicious!"
    #     $ sai_rp += 5
        
    #     show sai happy
    #     s "Maybe we should fry up my finger the same way! I wonder how my taste will compare to this?"
    #     hide sai_affection with dissolve
    #     show mc confused
    #     m "Uh, no." 
    #     show mc cute
    #     m "But I'm glad you like it."
    #     show sai vvhappy
    #     s "I truly do! Honestly, I'm disappointed there's no meat, but this is still a unique experience."
    #     show mc surprised
    #     m "Oh... I completely forgot that was your one request."
    #     show mc happy
    #     m "Um, my meal has meat in it, so what if we split it?"
    #     show sai surprised
    #     s "Yes please!"
    #     show mc annoyed
    #     m "Well then. Please help yourself."   
        

    elif custardslice:
        show sai eathate
        s "!"
        $ sai_rp -= 10
        show sai bleh
        s "Ugh! I didn't expect such extreme sweetness again..."
        show mc stressed
        m "Shit."
        "You screwed up. You weren't paying attention..."
        hide sai_affection with dissolve
        show sai sad
        s "I thought I'd be tasting something unique... This is just... sweet again."
        s "Like the milkshake. And the hot chocolate..."
        show mc sad
        m "I forgot you don't like sweet things. I'm such an idiot. I'm sorry."
        show sai vshy
        s "At the very least, it has somewhat of an interesting texture."
        show mc normal
        m "No, don't force yourself to eat it. Let's just swap our food."
        show sai happy
        s "Thank you."
        show mc normal
        show sai eatdown
        s "*Munch*"
        show sai eathappy
        s "...?"
        show sai eathate
        s "My mouth is burning!"
        show mc happy
        m "It's meant to be spicy. Don't like it? You can have some more of my milkshake-"
        show sai determined
        s "No more sweetness! I can handle the heat!"
        show sai eatdown
        s "Actually, it's not so intense after a while. I like it."
        show mc annoyed
        m "Welcome to masochism."
    
    
    
    scene black with fade
    stop music fadeout 3
    "You and Sai finish up!"
    "It was kinda fun in the end, and eating something besides 3-minute noodles is a real treat."
    "You drop off Sai at the dorms, grab your backpack (after carefully removing the spider),"
    "...and, for the first time in months, go to class."
    # "As you get up to leave, you think you see someone at a nearby table look at you."
    # "Not just \"look\", that was definitely a STARE."
    # "He's staring at Sai's hand. The one missing a pinky finger."
    # "He nudges his partner and points at it."
    # m "(What the hell? That's rude!)"
    
    # show chibi_mc at slightright
    # show chibi_sai at slightleft
    # with easeinright
    # window show

    # "You replay that scene in your head."
    # "You imagine yourself going up and confronting him... and think of all the ways you could \"win\" that situation."
    # "Eventually you reach the crossroads between school and the dorms." 
    
    # m "Alright, I'm going to class."
    # m "You do remember how I told you to get inside right?"
    # s "I have your instructions looping in my head! Safe travels!"

    # window hide
    # hide chibi_sai
    # with easeoutleft
    jump college


label college:
    play music "kinda_moody.mp3"
    scene class with fade
    show mc normal with easeinbottom
    window show
    m "(Alright, I ate. I arrived on time. Everything is great. Now just to learn.)"
    t "Good morning everyone. Did you have a good Monday?"
    ee "*Enthusiastic agreements and disagreements*"

    # m "(Okay, I got here. Now just to learn.)"
    # na "I slept for thirteen hours straight last night..."
    # na "All-you-can-eat-and-drink at Trenchtown, babyyyyy!"
    # na "Yeah, the boardgame society's event was pretty cozy."
    # show mc sad
    # m "(Nothing happened for me, as usual...)"
    # show mc surprised
    # m "(Wait, what am I saying!? I made a friend yesterday, Sai! That's massive.)"
    # show mc awkwardsmile
    # m "(Literally... made a friend. Heh.)"
    # show mc normal
  
    t "Great to hear!"
    na1 "Psst~ Don't you think he's kinda hot?"
    na2 "Huh...? Who?"
    show mc blushside
    m "(Could they be talking about me?)"
    na1 "The teacher! Oh my gosh - his {i}arms{/i}. Everytime he crosses them, mmm, the bulge."
    show mc normalside
    m "(I don't know why I even bother getting my hopes up.)"
    show mc normal
    t "O-kay, so let's continue where we left off."
    t "Last week we discussed how moths evolved during the industrial revolution."
    show mc confused
    m "(Uuuuuuh whaaaat!? That happened? What page is this on???)"
    t "Because of the increased smoke from factories, the pale bark of nearby trees were covered with soot. Coincidentally, this is where the moths would come to rest."
    t "This light-coloured moth species was spotted and eaten by birds. However! Because of genetic variation, some individuals were dark-coloured..."
    t "And yada yada yada, you remember the rest."
    show mc stressed
    m "(Don't just yada-yada-yada! Explain!)"
    t "The point is, animals with traits that are advantageous to environmental conditions will survive long enough to reproduce and pass on their genes to their offspring."
    show mc vannoyed
    m "(Why is he talking so fucking fast!? Isn't he supposed to teach us? How am I supposed to write this all down?)"
    na1 "Oh my god, his teeth are so white. I want him to bite me-"
    show mc normalside
    m "(I wonder if Sai wants that too... maybe in a less sexual manner. She just want to get eaten!)"
    show mc blushside
    m "(No! Focus! Don't get distracted!)"
    show mc normal
    t "-so now you know. Neat, right? That said, let's explore other ways humans have influenced speciation..."
    show black:
        alpha 0.2
    with dissolve
    t "...rapid urbanisation isolates populations..."
    show black:
        alpha 0.5
    with dissolve
    t "But how is this different to genetic drift? Simple, it's-"
    show black:
        alpha 0.7
    with dissolve
    show mc stressed
    "You're getting lost..."
    t "One potential solution is the use of stepping stones, which are-"
    show black:
        alpha 0.8
    with dissolve
    show mc vstressed
    m "(I can't keep up. This is pointless.)"
    m "(I'm not even fast enough to write it all down to try understand later.)"
    show mc sad
    m "(I'm just getting left behind.)"
    scene black with fade
    stop music fadeout 3
    "You endure the frustrating lecture, completely zoned out."
    "When you look around you, you see some people with organised notebooks, some typing rapidly on a laptop, some just listening."
    "You don't belong with them."
    "This is your punishment."
    "Hopelessness spreads through your body."
    window hide
    jump sai_aftercollege



label sai_aftercollege:

    scene black with fade
    show afternoon_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show dirty3
    show bottle
    show day_2 at topleft
    show sai_affection at topright
    with Dissolve(3)
    # play music "normal.mp3" fadein 3

    show sai normalside at left
    with dissolve
    play sound "door.wav"
    show mc normalsquint at right with easeinbottom
    window show
    show sai happy
    s "Welcome back. Did you have a good education?"
    "Ignoring Sai, you drop your bag on the floor, faceplant onto your bed, and sigh into the pillow."
    
    show sai normal
    hide mc with dissolve
    "Who cares if you can't learn?"
    "Who cares if you won't pass?"
    "{i}You{/i} certainly can't bring yourself to care."
    "You just feel like shit."
    "You want to forget about it all."
    show sai surprised
    s "%(player_name)s...?"
    # show mc annoyed
    m "..."
    show sai sad
    s "Did I do something?"
    "Great, now she's making you feel even worse."
    "It's not fair! It's hard to just greet her like you're perfectly fine."
    "Why should you have to explain yourself? Are you not allowed to be upset? Or silent?"
    "..."
    "You can't relax with her here. You're too acutely aware of her presence."
    "You can't even relish in your self-pity."
    "You just want to be alone."
    window hide
    show mc normal at right with dissolve
    window show
    m "I'm going to the bathroom."
    show sai vworried
    s "Understood."
    window hide
    hide mc vstressed
    with easeoutbottom
    play sound "door.wav"

    stop music fadeout 2
    jump bathroom



label bathroom:

    scene bathroom with fade
    play music "lightbuzz.wav" fadein 2

    show mc normalside with easeinbottom
    window show
    "Finally, you're alone."
    "Dealing with people is so annoying. Having yourself to worry about is already hard enough."
    # m "(It doesn't make sense. Where is all that food going anyway?)"
    # m "(The only explanation is that she digests everything...)"
    # "Pondering Sai's strange anatomical processes, you do some excretions of your own."
    play sound "flush.wav"
    show mc normal
    menu:
        "Should I wash my hands?"
        "Wash your hands.":
            play sound "tapwater.wav"
            pause 1
            "The ice-cold water feels so harsh. It almost hurts."
            "You want to stick your whole head under it."
            "But the instant you splash the water onto your face, it sends a shock to your core."

        "It was just a number 1.":
            m "(It was just a piss. Maybe I don't have to wash my hands?)"
            "As soon as you consider that, you feel disappointed in yourself."
            "Why are you like this? Aren't you supposed to be grown up, doing all the right choices?"
            "This just justifies your self-hatred."
            show mc vannoyed
            m "(I should probably wash my face too. It's been a while.)"
            "But it's going to be so cold! It'll feel awful!"
            show mc normalside
            m "(I could let the water run until it's hot.)"
            "That'll waste a lot of water. And for what? You? You're not worth it."
            show mc stressed
            m "Ugh, what do I do?"
            "Give up and go. You're not strong enough for simple adult function like this."
            "Go back and feel miserable. Do nothing. Accept defeat that you can't-"
            play sound "tapwater.wav"
            pause 1
    show mc shocked at bounce
    m "SHIT! Freezing!"
    show mc shout
    m "Hah!"
    m "Okay! Okay! There! I did it! Face {i}washed{/i}!"
    show mc annoyed
    m "Good job, me."
    "You're affirming yourself for just washing your face?"
    show mc normal
    "The most basic of tasks... and it was this difficult? Is there any hope for you?"
    window hide
    scene bathroom_mirror
    show mc normal
    with Dissolve(2)
    window show
    "It's been so long since we last looked each other in the eyes."
    "Why don't you look at me in the mirror?"
    show mc worried
    m "(I shouldn't.)"
    "Why not? Go on. Look."
    "How bad do you look? Perhaps better than you think."
    "If you just lift your head..."
    show mc vstressed
    m "(I shouldn't! I know I'll regret it!)"
    show pulsingblack with dissolve
    "Look."
    "At."
    "Yourself."
    window hide
    stop music fadeout 2
    scene reflection_normal with fade
    play sound "scarybathroom.wav"
    window show
    "Look."
    window hide
    pause 3
    window show
    "Eye bags."
    "Hairline."
    "Wrinkles."
    "Sun spots."
    stop sound fadeout 2
    "You look... older. And you weren't ready for that."
    
    window hide
    play music "moody_music2.wav" fadein 2
    show reflection_sad with Dissolve(3):
        alpha 0.5
    window show
    
    "Spots, freckles, imperfections, more of them in new places."
    "Your skin sags more."
    "Creases on your forehead."
    "Blackheads on your nose..."
    "Eyes, soulless, apathetic, bloodshot."
    "Those dark circles will never go away."
    "You'll always look like a zombie."
    window hide
    scene reflection_sad with Dissolve(3)
    window show

    "Who does this face belong to?"
    "It's ugly. It's imperfect."
    "This isn't how you see yourself. It doesn't make sense."
    "But disgustingly, it's still yours."
    "You should feel ashamed for ever showing it outside."
    "You should hide it, inside where you belong."
    show pulsingblack with dissolve
    
    "Will you ever love yourself again?"
    "Will you ever be able to look at yourself, in the mirror, without your smile fading?"
    "Or will you grimace every time?"
    "This is your body."
    "Is there any fix?"

    scene black with fade
    "Time is running away."
    "You've wasted so much of it."
    "And now here you are."
    "Regretting."
    "Wishing."
    "Hating."
    "It's your own fault."
    stop music fadeout 3
    stop sound
    "There's no one else to blame."
    window hide
    play music "wind.wav"
    pause 1


    show text "{size=+200}It's{w} your{w} fault." with dissolve

    pause 1
    window show
    "You're the one in charge of your life, after all. You got yourself here."
    "This is all your fault."
    "You wasted your life as if you've got a spare."
    "But you don't."
    "You could always just-"
    window hide

    stop sound
    stop music
    play sound "door.wav"
    play music "date.wav" 
    show bathroom
    show mc vstressed at right
    with easeinbottom

    show sai sad at left with easeinleft
    s "%(player_name)s! %(player_name)s!"
    show mc shocked
    m "S-Sai!?"
    #s "%(player_name)s, I accidentally stepped on Carl!"
    show sai vsad
    s "I'm a foolish fool! I stepped on Carl! He is dead!"
    s "I just- I just STOOD on him as if he were another article of clothing! He went smush! Aah!"
    show mc surprised
    m "Calm down, Sai. Who's Carl?"
    show sai sigh
    s "Carl the spider! His form is so unrecognisable, that if he is not dead, I should rectify that immediately to end his suffering."
    show sai sad
    s "I'm so, so sorry. Words cannot describe my guilt."
    show mc awed
    m "Accidents happen. I'll take a look as soon as I'm done here, so-"
    show sai embarrassed at bounce
    s "Oh crumbs! I probably shouldn't be in here, should I...?"
    show sai blush
    s "What if I'd accidentally seen your mushroom?"
    show mc surprised
    m "My what?"
    show sai sad
    s "I-I'll go now. Sorry for intruding."
    
    hide sai with easeoutbottom
    play sound "door.wav"
    
    m "..."
    show mc annoyed
    m "(Thanks for being a good distraction, Sai.)"
    m "(Why is it so much easier to feel better when it's for someone else?)"
    show mc normalside
    m "(I haven't been kind to her. I ignored her. I don't even think I've said thank you to her once.)"
    show mc sad
    m "(And yet, I've done so much more than I would have, thanks to her.)"
    show mc happy
    m "Okay! Let's keep this stone rolling and take a quick shower while I'm here."
    stop music fadeout 2

    # "That was close. She nearly saw you at your worst."
    # "Come now. Man up before you go back. Just pretend you're happy for now."
    # show mc normal
    # m "(Alright. I'm ready.)"





    #Alt version:
    #s "I can't believe I was so thoughtless. But his body was so light, a gust suddenly came and carried him off the windowsill and I-"

    # s "I'm sorry..."
    # s "He's now... spider dust."
    # m "..."
    # s "Do you forgive me?"
    # m "{size=-10}Yeah."
    # show sai surprised
    # s "Oh."
    # show sai sad
    # s "Thank you. I'll give him a proper funeral."
    # m "..."
    # show sai shy at bounce
    # s "Oh crumbs... I probably shouldn't be in here, should I...?"
    # show sai blush
    # s "What if I'd accidentally seen your mushroom!?"
    # show mc surprised
    # m "My...? Oh!"
    # show mc annoyed
    # m "Heh."
    # show sai shy
    # s "I-I'll go now... Sorry for intruding. Ah, I'm so absent-minded sometimes..."
    
    # hide sai with easeoutbottom
    # play sound "door.wav"
    # show mc sad
    # "That was close. She nearly saw you at your worst."
    # "Come now. Man up before you go back. Just pretend you're happy for now."
    # show mc normal
    # m "(Alright. I'm ready.)"

    
    scene black with fade
    show afternoon_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show dirty3
    show bottle
    show day_2 at topleft
    show sai_affection at topright
    with Dissolve(3)
    
    play music "normal.mp3" fadein 3
    
    
    show sai sad at left with dissolve
    play sound "door.wav"
    show mc normal at right
    with easeinbottom
    
    s "May you rest in peace, Carl. As a fellow sibling in life, we are always connected."
    "Sai gives Carl a eulogy, collects his crushed remains, then lets the wind carry him out the window."
    "But the wind goes the wrong way!"
    show sai bleh
    s "Pthew! Pah! Ugh, Carl! Not there!"
    show sai eat
    s "Ugh, well, I was kind of curious anyway. Hmm, crispy..."
    show mc annoyed
    s "I guess that's one way to dispose of his remains."
    show sai surprised at bounce
    s "Oh! Y-you're back."
    show sai apologetic
    s "...and you just saw me eat your friend."
    stop music fadeout 2
    show mc normal
    m "Sai, thanks you."
    show sai surprised
    s "\"Thank you\"?"
    play music "kinda_moody.mp3"
    show mc normalside
    m "I know exactly how today would have gone if you weren't here."
    show mc annoyed
    m "And sure, maybe I'd still have a spider, but I wouldn't have left my room. Or eaten something proper. Or gone to school. Or washed up."
    show mc cute
    m "Thank you for helping me get out and for being here with me."
    show sai sad
    s "I-I thought I was causing nothing but mayhem..."
    show mc happy
    m "Yeah. Thanks for that. I needed some mayhem."
    show mc annoyed
    m "It's what helped me step out my tiny little comfort zone."
    show sai blush
    s "I assisted you? But you were the one who did it all for me..."
    show mc normalside
    m "What did you first call that thing I had with the spider? Where we help each other out?"
    show sai think
    s "A symbiotic relationship?"
    show sai excited
    s "Wait! So you can actually tolerate my company due to the benefits I provide?"
    show mc confused
    m "..."
    show mc annoyed
    m "I {i}enjoy {/i}your company, due to the benefits and just because you're a nice person."
    show sai happysigh
    s "Me...?"
    show mc sad
    m "Also, I'm sorry for ignoring you earlier. I was just in a mood and didn't want to talk."
    show sai surprised
    show mc stressed
    m "Ugh, I'm just in such a mess with my work. And it's my own fault."
    "It's all your fault."
    show sai shy
    s "Well, perhaps we can clean the mess together?"
    show mc normal
    m "I don't know... I'm out of my depth."
    show sai happy
    s "I can take out the garbage, and you can focus on the clothes."
    stop music fadeout 2
    m "..."
    show mc surprised
    m "Actually, it does kind of stink in here... more so than usual, I mean. Do you smell that?"
    show sai confused
    s "Can you describe the offending scent?"
    show mc shout
    m "Ugh, it's so bad. It smells kinda..."
    if benedict:
        m "... fishy."
    if custardslice:
        m "... rancid."
    s "Huh? Really?"
    "As she talks, the smell gets worse."
    show mc surprised
    m "Oh..."
    m "Sai, can you breathe in and out, really deeply?"
    show sai surprised
    s "*Inhale*"
    show sai normal
    s "*hold*"
    show sai sigh 
    s "*Exhale*."
    # s "What? Hah- Hah *sniff*."
    show mc stressed
    m "Urk!"
    play music "heaven.mp3"
    show sai shocked
    s "It's me!? Crumbs, this is embarrassing..."  
    show mc awkwardsmile
    m "Sai, do you have a digestive system?"
    show sai shy
    s "I have no idea..."
    m "Any urges to use the bathroom?"
    s "No. I've never made any kind of excretion."
    show mc stressed
    m "So if you're a one-way system, then doesn't that mean that everything you've eaten..."
    show mc confused
    m "... might just be rotting inside you?"
    
    show sai surprised
    s "..."
    show sai sad
    s "Possibly..."
    show sai vshy
    s "Maybe if I swallow detergent it would cover the smell?"
    show mc normalside
    m "Great idea... that'll {i}definitely{/i} help."
    show sai happy
    s "Then-"
    show mc stressed
    m "That was a joke. You have to actually fix the problem, not just make it more tolerable."
    show sai sad
    s "Then what do I do?"
    show mc normal
    m "If I were you, I'd just throw up in the toilet."
    show sai worried
    s "I can't. That requires diagphram muscles, which I lack."
    show mc confused
    m "Then do a handstand? Like, being upside down?"
    show sai surprised
    s "Handstanding... on a toilet? Um..."
    show mc normal
    m "Actually, I've got a better idea. Follow me."

    hide mc
    hide sai
    with easeoutbottom
    play sound "door.wav"

    stop music fadeout 3
    scene black with fade

    scene garden with fade:
        matrixcolor TintMatrix("#6F6FBB")
    show mc normal at right
    show sai normal at left
    with easeinbottom
    play music "date.wav"
    
    m "I once had to backwash a pool. It's the same thing."
    show mc normalside
    m "If your \"stomach\" is really a closed system, then if I stick a hosepipe in you, all the gunk will flow out."
    show sai confused
    s "Consuming more... to remove it?"
    show mc annoyed
    m "Trust me. 5 mins, full-pressure water, you'll be cleaned out in no time."
    m "Take a seat on the bench. I'll hook up the hosepipe."
    show sai worried
    
    window hide
    hide mc
    with easeoutbottom
    window show
    s "Oh gosh..."
    "You find a hose pipe in the shed, attach it to the tap, turn it on, and roll it out to the bench."
    "Sai waits on the bench as you instructed, albeit nervously."
    window hide
    show mc normal at right
    with easeinbottom
    show sai embarrassed at bounce
    window show
    s "%(player_name)s, I-I think I should definitely do this repulsive task by myself."
    show mc happy
    m "Don't worry, I don't care."
    show sai worried
    s "But this is so intimate. It's like a reverse enema! It's embarrassing..."
    show mc normal
    m "It won't bother me, I promise. I just want to help you."
    show sai shy
    s "I don't want to be a bother..."
    show mc normalsquint
    m "You're a bother for saying you're a bother."
    show sai worried
    s "Um, well... ugh... that's a conundrum... well, if you insist... but-!"
    show mc normal
    m "Alright, lie down so you don't puke this all over yourself."    
    show sai scared
    s "Wait! Don't you realise you'd see everything? All masticated and mushy and mal-odorous foods!"
    m "Yup."
    show sai sad
    s "I'm sorry..."
    s "I'm so sorry you're doing this for me."
    show mc vannoyed
    m "Sai... I'm going to say this kindly."
    show mc annoyed
    m "Shut up. Open up. Trust me."
    show sai apologetic
    s "Okay. Sorry. Thank you."
    show black with fade
    "Sai lies on the bench, scrunches her eyes closed, and waits."
    m "Alright, drink up."
    "You stick a hose pipe down her throat, and turn it on full."
    scene hosingoutsai with fade
    s "BBbb!"
    "Sai's face winches in discomfort, but she sits still."
    "For a few seconds..."
    "You just stare at each other awkwardly while waiting for the water to fill her up."

    m "Ok, I'm taking the hose out now. Just, uh, turn on your side and let it all come out."
    s "Bllllleeeegh!"
    "You try not to look at the bits of grey-coloured food being flushed out."
    "You use your ability to cross-eye at will. It blurs your vision."
    "You repeat the process three more times until nothing else comes out."

    window hide
    scene garden with fade:
        matrixcolor TintMatrix("#6F6FBB")
    show mc normal at right
    show sai bleh at left
    with easeinbottom
    window show
    s "*COUGH! COUGH!*"
    show sai apologetic
    s "Ugh! That was the{i}worst{/i} experience so far."
    show mc normal
    m "Well, at least you don't have rotting food inside you."
    show sai sigh
    s "Thank you, %(player_name)s. Hah, my body feels so... unusually lethargic."
    show sai vworried
    "Sai stares with a distant, somewhat sad expression at her hands."
    m "(What's she thinking right now?)"
    show mc awed
    m "Why don't we sit and rest a bit before we go back."
    show sai apologetic
    s "Y-yes... I think a rest is in order."
    stop music fadeout 2
    show mc confused
    m "What's wrong, Sai? It looks like something's on your mind."
    show sai worried
    s "..."
    m "(She looks really uncomfortable.)"
    show mc happy
    m "You can tell me. In fact, you must. Consider it payment for helping you empty your stomach."
    show sai sad
    s "Then... I truly must... You must forgive me in advance for being insensitive."
    show mc awed
    m "Er, sure. Go ahead."
    
    play music "thinking.mp3" fadein 1
    show sai apologetic
    s "When I burst into the bathroom earlier..."
    show mc stressed
    m "(Ah, shit... she saw.)"
    s "You looked so sad. Not as in inadequate, but as in, miserable. Malcontent. Morose. Melancholic. Et cetera."
    show sai sad
    s "I wanted to ask you, like you just asked me - \"What's wrong\"?"
    show sai angry
    s "I felt so awkward that I didn't bring it up, but I... I don't like that I did that. I'm ashamed."
    show mc normalside
    m "I'm glad you didn't."
    show sai apologetic 
    s "I know. You tend to avoid questions like that..."
    s "But if I don't ask, how can I help you? So..."
    show sai shy
    s "Could you tell me what was weighing your heart?"
    show sai vshy
    s "Please?"
    show mc worried
    menu:
        "The pressure is intense. This is a moment where you either potentially about to ruin everything, or stay safe."
        "Express your suicidal inclinations.":
            $ sai_rp += 10
            stop music fadeout 1
            show mc stressed
            m "Screw it. Fine."
            show sai surprised
            s "Ah, really? Th-thank you! That's all I want."
            show sai shy
            s "I am listening."
            show mc stressed
            "She's so earnest, it makes you feel guilty. It makes you hesitate."
            "She's going to hear some horrible things."
            show mc sad
            m "I-I don't usually talk about this kind of stuff."
            show sai normal
            s "Don't worry so much. I won't judge you."
            "She says that now. But she can't promise it, can she? Her who opinion of you might change."
            "Can you handle that again?"
            show mc normalside
            m "(I think all I can do is just have faith in her.)"
            show mc stressed
            m "Okay."
            play music "date_musicbox.mp3"
            show mc worried
            m "I don't know what I'm doing."
            m "I don't know what I want. I don't know why I'm studying. I don't know job to aim for..."            
            show mc sad
            m "I thought once I left high school, that's when my life would really start."
            m "That I'd be fit, healthy, happy, wealthy, have meaning relationships..."
            m "I wanted to be a success."
            m "But instead, I feel like I'm doing everything wrong."
            m "I don't cook, clean, or look after myself. I'm doing the bare minimum to pass my subjects."
            m "No energy. No enthusiasm. I'm get overwhelmed at the stupidest things... I don't feel like an adult."
            show mc stressed
            m "I just feel... disappointed."
            m "Everyone else is doing better than me."
            m "I'm getting older."
            show mc cry
            m "There's so much pressure. I've only got one life."
            m "I just wanted to do it perfectly so I don't regret everything when I die. But I don't know what that even means."
            show mc normalsquint
            m "Everytime I think about my life, it's like there's a voice inside my head..."
            show mc stressed
            show sai surprised
            m "Telling me how {i}hopeless{/i} everything my future is."
            m "And that I should..."

            show mc worried
            m "{size=-30}...kill myself."
            window hide
            show black with dissolve

            show text "You're not supposed to say those two words."
            with dissolve
            pause
            hide text with dissolve
            show mc worried at center with dissolve
            m "(Please don't be a mistake.)"
            m "(Please don't leave me.)"
            window hide
            hide mc worried
            show text "You can't take it back."
            with dissolve
            pause
            hide text with dissolve
            hide black 
            show mc sad at right
            with dissolve
            window show
            s "Can you tell me more about those thoughts?"
            m "I guess... It's kind of like there's a voice always floating in my head, critising me."
            show mc stressed
            m "Just constant pessimism and stress and worry. Every day. And it's like... what's the point in being happy?"
            m "..."
            show mc confused
            m "Um, are you still okay? That was a lot of me speaking."
            show sai happysigh
            s "Yes. I'm just glad I finally get to hear what it's like to be you, %(player_name)s."
            show sai shy
            s "If you are finishedm may I share my opinion on the matter?"
            show mc surprised
            m "Yeah. That could be nice."

            m "(What kind of opinion would a mushroom have?)"
            show mc normalside
            m "(Well, Sai is definitely more than just a mushroom.)"
            show mc normal
            show sai vshy
            s "I think... you are too hard on yourself %(player_name)s."
            m "I don't think I'm hard enough on myself. I never do anything."
            show sai pout
            s "Please be kind to yourself."
            show mc sad
            m "I don't deserve it."
            show sai pout
            s "No one needs to deserve kindness. No matter what, you need to be on your own side."
            show sai vshy
            s "I understand that you're worried about making the most of your life, and making the \"right\" choices..."
            show sai confused
            s "But your definition of success is vague. It's as you said: you don't know what you want. Therefore..."
            show sai happy
            s "You need to focus on yourself."
            show mc confused
            m "What kind of logic is that?"
            show sai normal
            s "You need to explore your true interests, not just do things you think you're \"supposed\" to do."
            show mc awed
            show sai shy
            s "%(player_name)s, big decisions, like what to focus on for the rest of your life, only come after you know who you are."
            s "Without that knowledge, how can you possibly feel confident while you build towards your future?" 
            show mc awed
            m "That does kinda make sense. But is that okay? I won't be working..."
            show sai determinedclosed
            s "Don't feel guilty. Reassure yourself!"
            show sai happy
            s "\"It's okay for me to do that things I've always wanted to try.\"- like that!"
            show mc slightsad
            m "So if I wanted, I can just like... explore the outside? Wherever I wanted?"
            show sai surprised
            s "Y-yes. If that's what you want."
            show mc normalside
            m "I don't have to stay inside if I don't have a reason to leave? I can just do it?"
            s "Yes!"
            show mc normal
            m "I hardly know the area I live in, or the world generally, even after 2 years of being by myself."
            m "Maybe I'll start with that."
            show mc worried
            m "You'll be with me, right?"
            stop music fadeout 2
            show sai happy
            s "I would love to. Actually, %(player_name)s..."
            show sai vshy
            s "I want to go camping with you."
            play music "trip.mp3"
            show mc surprised
            s "Like sleep outside? Why?"
            show sai pout
            s "The closest I've gotten to being in nature is this little garden. I want to experience nature properly. It's important to me."
            show sai happy
            s "And since you want to explore, it would be one of those so-called \"win-win scenarios\"."
            show mc normalside
            m "That... does sound kinda fun. I've never gone before."
            show sai happy
            s "Excellent! What if tomorrow we escape this concrete jungle and-"
            show mc surprised
            m "Whoa whoa! Tomorrow? I don't have any equipment! And I don't even know where we'd go!"
            show sai determined
            s "%(player_name)s, those are problems we can solve, okay?"
            show mc confused
            m "Eh!?"
            show mc worried
            m "But I'm not ready! What if it rains tomorrow? I can't even drive! How do we get there?"
            show sai determined
            s "%(player_name)s, if there is a hurdle in your way, you don't stop and think - you run towards it and jump!"
            show mc stressed
            m "Ugh... I haven't even had time to mentally prepare..."
            show sai normal
            s "It will be fine. We need to live each day like it's our last."
            m "(But TOMORROW!? What's the rush? I just want to take it easy...)"
            default O2 = False
            jump choose_if_go_camp
            label choose_if_go_camp:    
                menu:
                    "What should I do?"
                    "But my exams are next week!" if O2 == False:

                        show mc surprised
                        m "But I have an exam need week! I need to study!"
                        show sai angry
                        s "You won't study tomorrow anyway, will you?"
                        show mc shocked
                        m "(Damn! She's really set on this.)"
                        show mc stressed
                        m "You're right, but-"
                        show sai normal
                        s "%(player_name)s, listen to me."
                        show sai aapologetic
                        s "It's difficult for me, being the person I am, but I think this is one of those scenarios where I have to push you."
                        show sai shy
                        s "So I'm going to do that, okay? We have to go."
                        s "Don't overthink it. Don't worry. But you don't have a choice okay?"
                        "Somehow, having the choice removed from you makes everything a lot easier."
                        jump choose_if_go_camp

                    "Let's go camp.":
                        show mc worried
                        m "Okay, but I just hope I'm not making a mistake..."
                        show sai vhappy
                        s "Wonderful. I think being outside will be a wonderful way to go - I mean, {i}place{/i} to go, together with you."
                        hide sai with easeoutbottom

                    
            s "Let's go. We must keep this mossy ball of momentum moving!"
            hide sai with easeoutbottom
            show mc stressed
            m "Acting spontaneously is so stressful."
            window hide
            hide mc with easeoutbottom
            stop music fadeout 3
            scene black
            jump sai_d2_returnfromgarden_camproute
            
        "It's nothing.":
            $ sai_rp -= 10
            show mc happy
            m "Oh, that? Heh, I was just confused in class and feeling bummed out."
            show sai confused
            s "\"Feeling bummed out\"?"
            m "Yep."
            show sai pout
            s "Is that really all?"
            "You've learned that the best way to someone off your back is to give enough detail to seem real."
            "Something that makes them feel like you've been \"vulnerable\"."
            show mc happy
            m "Yeah, I was feeling worried about my class, but after coming out with you, I realise that I was just overwhelmed."
            m "So... thanks for being a good distraction, Sai."
            show sai shy
            s "I'm happy to hear that we have both benefitted from this outing."
            show mc annoyed
            m "Yup! I think I can even work a little when I get home!"
            show mc worried
            m "(Why am I saying this!?)"
            show mc stressed
            m "(Well, if it gets her to stop worrying about me, I'll do work.)"
            show sai surprised
            s "Then we should return!"
            show mc happy
            m "Yeah."
            window hide
            hide sai with easeoutbottom
            window show
            show mc normal
            m "(I kinda wish I told her the truth...)"
            show mc slightsad
            m "(No, my worries don't matter anyway. They're all just stuff in my head, not real problems.)"
            m "(And she's not even a human. She wouldn't understand.)"
            window hide
            hide mc
            with easeoutbottom
            stop music fadeout 3
            scene black
            jump sai_d2_returnfromgarden_maskroute

   
    

label sai_d2_returnfromgarden_maskroute:

    show bedroom_night_no_bg_clean:
        zoom 0.9
    with Dissolve(3)
    play sound "door.wav"
    show mc normal at right
    show sai normal at left
    with easeinbottom
    play music "night.mp3"
    window show

    m "I'm gonna quicikly make some notes from today's class before I forget it all tomorrow."
    show sai shy
    s "Oh, okay... may I watch you?"
    m "If you want to bore yourself."

    "You review your lecture, googling the points you hadn't understood, correcting your notes..."
    show mc confused
    m "(I still have a few questions. Maybe I could ask the lecturer for clarification?)"
    
    "But then you'll show how behind you are."
    show mc stressed
    "You can already imagine that look of annoyance on his face."
    m "(I wish I could just ask him without feeling so scared.)"

    "Now discouraged, you lean back in your chair and sigh loudly."
    show sai surprised
    s "Are you done?"
    "You definitely feel like you're done with all of this."
    show mc sad
    m "I can't understand anything."
    show sai happy
    s "I offer my assistance. What can I do to help?"
    "You can't even hear her..."
    "Look at everything you still need to catch up on."
    "Remember that test you heard mentioned in class today?"
    "What if you fail it?"
    show mc vstressed
    m "(Stop fucking discouraging me!)" with sshake
    show mc vshout
    m "Hot chocolate break!"
    show sai shocked
    s "O-Okay!"
    show mc stressed
    m "And just talk to me. I need a distraction for five minutes."
    show sai determined
    s "O-okay! Random fact! Did you know that fungi are genetically closer to humans, than humans are to plants?"
    

    hide mc
    hide sai
    with easeoutbottom

    "After your break, you feel calmer."
    "You watch some crash courses with Sai, who is extremely intrigued."

    show sai shocked at left
    show mc normal at right
    with easeinbottom
    m "Okay, I'm actually done this time."
    s "This is fascinating! Humans have made knowledge so easily accessible!"
    show mc normalside
    m "(Such heartfelt enthusiasm. Wish I could relate. I just want to get this degree over with.)"
    show sai determined
    s "Tell me! Are there any \"crash courses\" on mushroom?"
    show mc confused
    m "Yes, but... isn't that going to weird you out?"
    s "No. On psilocybe cubensis, please!"
    show mc stressed
    m "I'm glad you're being assertive at least."
    show sai determinedclosed
    s "Yes, I am too."
    show sai happy
    s "Thank you for encouraging me to relax more around you. It's much simpler to express myself like this."
    show sai vhappy
    s "In a way, it feels more honest too. I'm enjoying myself a lot more."
    stop music
    show mc vstressed
    "Your heart clenches."
    "You haven't been as honest."
    "And yet, here she is, happy that you are both \"comfortable with each other\"\."
    "It's wrong."    
    "But even so, how could you even fix it now?"
    "It's too late."
    "Now you have to keep up the charade, heavier and heavier."
    "Don't."
    extend " Let."
    extend " It."
    extend " Fall."

    show sai surprised
    s "Are you going to put it on?"
    show mc surprised
    m "Y-yeah. What was it again?"
    show sai normal
    s "Psilocybe cubensis!"
    show mc confused
    m "... C-can you spell that?"

    show black with dissolve
    "You and Sai watch videos on mushrooms at her request."
    "It's a good distraction, at least. But you know it's temporary, and it's difficult to fully enjoy yourself."

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with Dissolve(2)
    show top_text "It was a bad day, just like you thought it would be." with dissolve
    pause
    show top_text "You didn't study enough. You lied to your friend. You still haven't solved the problems with your life." with dissolve
    pause
    show top_text "Tomorrow is going to be a bad day too, isn't it?{size=+20} And the next, {size=+20}and the next..." with dissolve
    pause
    hide top_text
    show text "{size=+200}WHAT ARE YOU GOING TO DO?" with dissolve
    pause
    show top_left "{size=+200}WHAT ARE YOU GOING TO DO?"
    pause 
    show top_right "{size=+200}WHAT ARE YOU GOING TO DO?"
    pause
    show text "{size=+400}WHAT"
    pause
    show text "{size=+500}ARE"
    pause
    show text "{size=+600}YOU"
    pause
    show text "{size=+700}GOING"
    pause
    show text "{size=+800}TO"
    pause
    show text "{size=+900}{sc=4}DO?{/sc}"
    pause
    scene red with Dissolve(3)

    jump sai_d3



label sai_d2_returnfromgarden_camproute:

    
    show night_clouds
    show bedroom_opencurtains:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty1:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty2:
        matrixcolor TintMatrix("#6F6FBB")
    show dirty3:
        matrixcolor TintMatrix("#6F6FBB")
    show bottle:
        matrixcolor TintMatrix("#6F6FBB")
    with Dissolve(2)
    play sound "door.wav"
    show mc worried at right
    show sai happy at left
    with easeinbottom
    
    play music "night.mp3"

    
    m "This is crazy. We're so unprepared!"
    m "Your supposed to make decisions like this after carefully weighing every option-"
    show sai normalside
    s "Acting only when you feel prepared is the root of your problems."
    show mc stressed
    m "Ugh... Maybe you're right. I don't know. All I know is, right now I need to research which places to go to tomorrow."
    show mc normal
    m "I need SOME semblance of a plan, at least." 
    show mc normalsquint
    m "But if anything bad happens, I'm blaming you."
    show sai surprised
    s "O-oh... okay, but what's the point in blaming anyone?"
    show mc stressed
    m "So I don't have to be the one that feels responsible and guilty."
    show sai think
    s "I think you're approaching this incorrectly. You don't need to plan every little thing."
    show sai happy
    s "We can just go out, and do whatever we want."
    show mc normalside
    m "And get stranded? Robbed? Mauled by a mountain lion? Nah, I'm researching."
    window hide
    hide mc
    hide sai
    with easeoutbottom
    window show
    "As the only responsible person here, you spend an hour planning your route and the necessary equipment for tomorrow."
    "While Sai is full of nothing but excited optimism."
    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with Dissolve(2)
    show top_text "Having made your plans for tomorrow, you and Sai head to bed."
    pause
    show top_text "You fall asleep much faster than you usually do."
    pause
    scene black with fade
    jump sai_d3_camp
    

    
    



    
#     show sai normal
#     s "But next time you feel sad, maybe just try that meditation I taught you."
#     show sai normal
#     s "One always leaves a butterfly cacoon undisturbed."
#     show mc normal
#     m "Thanks."
#     show mc worried
#     m "Uh, we should really leave the men's bathroom before someone comes."
#     window hide
    
#     show night_clouds at bg_scroll
#     show bedroom_day_no_bg_clean:
#         zoom 0.9
#         matrixcolor TintMatrix("#6F6FBB")
#     show sai_affection at topright
#     show day_2 at topleft
#     with Dissolve(3)
#     show mc happy at right
#     show sai shocked at left
#     show night_clouds at bg_scroll
#     with easeinbottom
#     window show
#     s "H-How are you so fast? I can't even comprehend your moves!"
#     show sai sad
#     s "I can't compare..."





#     s "Okay, then... come along. You can just follow me and I'll show you my attempt at a perfect mug of hot chocolate."
#     window hide
#     hide mc
#     hide sai
#     with easeoutbottom
#     #stop music fadeout 3

#     play sound "door.wav"

#     scene black with fade
#     show chibi_mc at slightright
#     show chibi_sai at slightleft
#     with easeinright
#     window show
#     "..."
#     "What's the point in narrating anything?"
#     "You've already messed everything up."
#     window hide
#     hide chibi_mc
#     hide chibi_sai
#     with easeoutleft

#     scene kitchenette with fade
#     show sai happy at left
#     show mc sad at right
#     with easeinbottom
#     window show
#     s "Okay, um... first, the powder-"
#     show sai shocked
#     s "No, first the mug! What am I thinking? Agh, I'm so..."
#     show sai determined
#     s "Alright, mug, THEN powder - oh, I need a spoon-"
#     play sound "spoon.wav"
#     show mc normal
#     m "Here."
#     s "Oh, thank you! You're not supposed to-"
#     show sai sad
#     s "I was supposed to do this by myself for you... I'm sorry I'm this bad."
#     m "..."
#     show sai normal
#     s "Okay... now... um..."
#     show sai determined
#     s "Um..."
#     show sai shy
#     s "Come on, Sai. You did this just yesterday! Mug, spoon, powder... mmm...m-milk? Milk? Milk!"
#     show sai happy
#     s "Yes! The milk!"
#     play sound "milk.flac"
#     s "And mmmmmmicrowave!"
#     play sound "microwave.wav"
#     pause 2
#     show sai vshy
#     s "Okay, I took the path less travelled, but I still got to the summit."
#     show sai vvhappy
#     s "Enjoy your hot chocolate. May it warm your intestines with it's supposedly comforting sweetness."
#     show mc happy
#     m "Thanks."
#     show sai happy
#     s "..."
#     show mc normal
#     "Sai is watching you."
#     "You're aware of what's coming."
#     "It's got your stomach tense. You dread it. It's going to be awkward."
#     "But why even care? Nothing matters."
#     "Speaking doesn't matter. What she says doesn't matter."
#     "In the end, it won't change anything."
#     "You'll stay the same."
#     "You've already given up."
#     show sai worried
#     s "I don't know if I've earned the right to ask these questions..."
#     show sai shy
#     s "-So please interrupt me if I'm being callous-"
#     show sai sad
#     s "But I have sensed that... today especially... has been difficult for you."
#     show sai apologetic
#     s "Is that... right?"
#     m "Probably."
#     show sai worried
#     s "I see."
#     s "It seems like, from you moment you woke up, to now, you have been under some kind of..."
#     s "Internal pressure. Burdened. Like your head is full of many things."
#     show mc normalside
#     m "Yeah. That's me."
#     show sai normal
#     s "That sounds tiring."
#     m "It is."
#     s "I assume... you don't like it?"
#     show mc shout
#     m "{sc=3}{color=#000000}Of course!"
#     "Meanie."
#     "I can be helpful too sometimes. Like stopping you from making a fool out of yourself."
#     show mc sad
#     m "I haven't been able to just relax for months."
#     m "Everytime I have free time, I just waste it inside. I'm unable to do anything by myself. Such a fucking failure-"
#     show mc stressed
#     m "Ugh..."
#     m "It's all been a waste. I'm sick of it all."
#     show sai vsad
#     s "..."
#     show mc vstressed
#     m "Sorry. You can leave."
#     "You hang your head in shame."
#     "You said the wrong thing."
#     "It seems you'll just have to keep on suffering like this."
#     "Until you can't."
#     show sai sad
#     s "I want to help you defeat that part of your mind."
#     show mc normalside
#     m "You can't."
#     show sai shy
#     s "But, I, um, actually... I {i}might{/i} be able to..."
#     show mc normalsquint
#     m "Don't give me false hope."
#     show sai shocked
#     s "I'm not! I'll explain-"
#     show mc normal
#     show sai shy
#     s "Um, well, you know how I'm a mushroom?"
#     show sai vshy
#     s "I'm not as good as most mushrooms. I'm not that tasty, or that big either... I'm quite small."
#     show sai normal
#     s "But... at least, what I do have... is {i}psilocybin{/i}."
#     show sai happy
#     s "That's where my name comes from. Sai, like \"Psi\"."
#     show mc confused
#     m "So? What's psilo-something do?"   
#     show sai normal
#     s "{i}Psilocybin{/i} is a chemical changes how you see things. And it's inside my cells."
#     s "It makes it so you can look at something without all the clutter, all the distorted hues in your head, and just... see them how you really see them."
#     s "Everything being repressed, tangled or blurry... becomes clear."
#     show sai shy 
#     s "I'm probably not explaining this very well, am I?"
#     s "But I think psilocybin would be useful to you."
#     show sai happy
#     s "If you've got rigid way of thinking, or are stuck with a certain perspective..."
#     s "...it shows up in your brain, like a deep lake in the middle of a forest, making it impossible to move from one side to the other."
#     show sai normal
#     s "It kind of... makes you stuck in your way of thinking. This can hurt your well being."
#     show sai vshy
#     s "That's what depression is, basically."
#     show sai happy
#     s "But psilocybin can help you get out of it."
#     s "Well, more scientifically, psilocybin encourages brain elasticity, so you can form new connections over that lake."
#     show sai vvhappy
#     s "Like bridges!"
#     show sai happy
#     s "Do you understand?"
#     m "..."
#     show mc surprised
#     m "Wait - Are you suggesting I {i}eat{/i} you?"
#     show sai vshy
#     s "...Y-Yes..."
#     show sai surprised
#     s "But just a part of me! Just the tip of my finger, say."
#     show mc annoyed
#     m "\"Just the tip,\" she says."
#     show sai confused
#     s "Y-yes. I do."
#     show sai normal
#     s "Any other questions?"
#     show mc shout
#     m "I don't even know what to ask!"
#     show mc confused
#     m "Does it... hurt? Is it permanent?"
    
#     s "No to both -"
#     show sai surprised
    
#     s "Oh! Um, actually, I have a question in response to that -"
#     s "Does your family have a history of psychosis?"
#     show mc awed
#     m "What's psychosis?"
#     show sai normal
#     s "It's when you struggle to distinguish reality from imagination."
#     s "Those with schizophrenia or bipolar disorder may experience it... Well, anyone can really."
#     s "But I'm asking because if it's latent in your genes, psilocybin can trigger it. Which I'd like to avoid."
#     show sai determined
#     s "So, do you?" 
#     show mc normalside
#     m "Nnnnnno? Everyone in my family is pretty standard. My uncle has autism, does that count?"
#     show sai happy
#     show mc normal
#     s "You're good."
#     show sai normal
#     s "So... will you do it?"
#     show mc normal
#     m "(A part of me doesn't like this.)"
#     m "(I don't know what my mom would think. But she's not the perfect role model either.)"
#     m "(If it could help, even a little... Ugh, but can I just trust Sai's word just like that? I'm not being gullible, right?)"
    
#     menu:
#         "Should I take her advice?" 
        
#         "I'll trust her on this.":
#             show mc sad
#             m "Fine. I guess you're right."
#             m "I need help."
            
#             play sound "affection_noise.wav"
#             $ sai_rp += 10
#             show sai happy at bounce
#             s "You're serious, right?"
#             show mc normal
#             m "Uh, yeah."
#             hide sai_affection with dissolve
#             show sai surprised
#             s "Oh! I'm... kinda surprised. I thought you'd... I don't know."
#             s "You don't strike me as someone to accept help."
#             show sai happy
#             s "I'm glad to be proven wrong."
#             show mc sad
#             m "Yeah, well, I don't think I can sink any further right now. So what's the harm in trying?"
#             jump taketheshroom
        
#         "I don't do drugs. Period.":
#             m "At the end of the day, you're offering me drugs. Nope. Mom taught me to say no to peer pressure."
#             show sai worried
#             s "I'm not a bad kind of drug. I'm like penicillin. A good fungus!"
#             show sai normal
#             s "My whole purpose is to let people recognise things they've been repressing. What matters to them."
#             s "It'll make you calm, thoughtful, introspective..."
#             show sai shy
#             s "People have used me for hundreds of years, so you know that I've been tried and tested by tons of people."
#             show mc normalsquint
#             m "Look, maybe you ARE safe. But... I can't just rely on substances if I can't help myself."
#             show sai worried
#             s "Sometimes..."
#             s "You need a tool to do something."
#             s "If you think you can help yourself, then... I'll accept that."
#             show sai sad
#             s "But I don't think you can. I think you're stuck. I think you need help."
#             show sai apologetic
#             s "I'm sorry. I hardly know anything about you. How can I say that? But..."
#             s "Please trust me."
#             s "Please reconsider."
#             "..."
#             show mc stressed
#             m "(I've spent months, years, feeling miserable with seemingly no solution.)"
#             "But that's YOUR fault! You just need to listen to Mom and get out of bed!"
#             "You're just too lazy to force yourself up, like everyone else. You think you're so special."
#             m "(No, it's not that easy...)"
#             m "(Maybe I shouldn't listen to that voice anymore.)"
#             "Listen to me: Sai is a stranger."
#             "You're not supposed to take drugs, no matter how she advertises it."
#             "You'll get in trouble."
#             "You'll damage your brain."
#             "Be smart. Like your parents taught you."
#             show sai_affection at topright with dissolve    
#             menu:
#                 "Should I reconsider?"
#                 "Rather safe than sorry.":
#                     m "I don't want to make a mistake."
#                     show sai worried
#                     s "So... no?"
#                     play sound "affection_fail.mp3"
#                     $ sai_rp -= 10
#                     show mc sad
#                     m "Yeah. Sorry. Thanks for trying, anyway."
#                     "Sai nods curtly. But her frown doesn't disappear."
#                     hide sai_affection with dissolve
#                     s "What are you going to do, then?"
#                     show mc normalside
#                     m "I don't know."
#                     s "..."
#                     s "This is frustrating."
#                     show mc surprised
#                     m "..."
#                     show mc vannoyed
#                     m "What? Because of me?"
#                     show sai angry
#                     s "I'm sorry. I know that's impolite of me."
#                     s "But... I feel like... my stomach's so tense, it'll burst!"
#                     s "You say you don't want to make a mistake, as if doing something is the only way to do that."
#                     show sai determined
#                     s "But inactivity, and failure to respond accordingly, can also be a mistake."
#                     s "..."
#                     show mc stressed
#                     m "I'm the one who's suffering."
#                     show sai determinedclosed
#                     s "I know! I want help!"
#                     show sai sad
#                     s "You've done so much for me. I... I guess that's why I feel so bad when I see you like this."
#                     s "And... even when I try, you just push away my solution."
#                     show sai shy
#                     s "I'm not mad at you. I... I'm aware of the stigma against magic mushrooms."
#                     s "You probably think I'm some weird, dangerous, unknown thing..."
#                     s "I get it."
#                     s "I just got too excited."
#                     show sai vshy
#                     s "It's just that, besides psilocybin, I'm bascially worthless."
#                     show mc normal
#                     m "I don't even care about that psilo-whatever. Don't worry about that. You're good as is."
#                     m "Can we just pretend this whole conversation never happened?"
#                     show sai worried
#                     s "I'll try. I've never had to pretend before... Although..."
#                     s "I guess I pretended you didn't ask me to execute you this morning."
#                     show sai normal
#                     s "..."
#                     show mc stressed
#                     m "..."
#                     window hide
#                     scene black with fade

#                     "You finish your hot chocolate in that tense silence."
#                     "After placing your mug in the sink, leaving it for someone else to clean, you go back to the dorm."
#                     "With Sai following silently behind."

#                 "Just admit it.":
#                     show mc sad
#                     m "Fine. I guess you're right."
#                     m "I need help."
                    
#                     play sound "affection_noise.wav"
#                     $ sai_rp += 10
#                     show sai happy at bounce
#                     s "You're serious, right?"
#                     show mc normal
#                     m "Yes. No leg pulling today."
#                     hide sai_affection with dissolve
#                     show sai shy
#                     s "Thank you for trusting me on this."
#                     s "And letting me help you."
#                     jump taketheshroom
            

# label taketheshroom:
#     show mc sad
#     m "I just hope I don't die or something."
#     show sai shocked
#     s "W-What!? Definitely not!"
#     show sai happy
#     s "I'll be stuck to you like a fly on tape, so you'll be protected at all times."
#     show mc confused
#     m "You do know what you're doing, right? Because I'm completely in your hands. I have no idea what to expect..."
#     show sai determinedclosed
#     s "Yes. I'm very confident in my abilities as your guide."
#     show sai happy
#     s "And don't worry. It'll probably be very nice, relaxing time!"
#     s "We can go somewhere in nature... play some gentle music..."
#     show mc stressed
#     m "Wait, wait - in {i}nature{/i}? This is the first time you've mentioned we'd be going outside."
#     m "Can't we just stay inside?"
#     show sai pout
#     s "But... oh... but nature is so lovely! The grass, the wind, the sky!"
#     show sai vhappy
#     s "Esepcially when you feel that breeze blowing across your body... You'll feel so... at peace."
#     show sai happy
#     s "Please? I'd like you to trust me."
#     show mc worried
#     m "But what if someone SEES me? What if I act weird???"
#     show sai vvhappy
#     s "I'll deal with any problems."
#     show sai shy
#     s "You'll probably just be lying down."
#     show mc sad
#     m "*sigh* If you say so..."
#     m "So, when are we doing this?"
#     show sai normal
#     s "Tomorrow."
#     show mc stressed
#     m "Tomorrow! Great. More time to regret this."
#     show sai determined
#     s "Mindset is important, so please don't say that."
#     show sai happy
#     s "In fact, for the rest of today, I want you to enjoy yourself."
#     show mc vannoyed
#     m "Ugh, do I HAVE to?"
#     show sai shocked
#     s "What a strange reaction... I-I thought you'd be jumping for joy!"
#     show sai shy
#     s "What if I help you relax? Is there anything you think of that makes you happy?"
#     s "I'll join you in whatever it is."
#     show mc normalside
#     m "Anything...?"
#     show mc awed
#     m "Hmm..."
#     show mc normalside
#     m "Maybe..."
#     show mc happy
#     m "Do you know what Tetris is?"
#     show sai surprised
#     s "\"Te-tris\"? Is this another place to eat?"
#     window hide

#     stop music fadeout 2
#     scene black with fade
#     play music "night.mp3"

#     show night_clouds at bg_scroll
#     show bedroom_day_no_bg_clean:
#         zoom 0.9
#         matrixcolor TintMatrix("#6F6FBB")
#     show sai_affection at topright
#     show day_2 at topleft
#     with Dissolve(3)
#     show mc happy at right
#     show sai shocked at left
#     show night_clouds at bg_scroll
#     with easeinbottom
#     window show
#     s "H-How are you so fast? I can't even comprehend your moves!"
#     show sai sad
#     s "I can't compare..."
#     show mc annoyed
#     m "Then get better."
#     show sai pout
#     s "Can't you go easy on me? You're sending me walls of doom before I can even DO anything."
#     show mc happy
#     m "Your problem, Sai, is that you can't keep sending one-liners. Send me at least ONE tetris. Then I'll teach you to T-spin."
#     show sai sad
#     s "I'm lost in the maze of this terminology."
    
#     "You and Sai relax for the rest of the day in your bedroom, playing against each other."
#     "After so much stress, it feels good to stretch your adrenal cortex the other way for once."
    
#     show mc normal
#     m "Okay, you're getting good, so it's time to change."
#     m "Next up, a strategy game called \"Age of Castles\". I guess I'm feeling kinda nostalgic."
#     show sai happy
#     s "When did you last play this one?"
#     show mc normalside
#     m "I think I was like ten years old? I remember it just wouldn't install for some reason, but then my dad took over, and just spent hours figuring it out."
#     show mc annoyed
#     m "If he had given up like me, I'd never have been introduced to one of my favourite childhood games."
#     show sai normal
#     s "Resillient, like a seed in a desert."
#     show mc happy
#     m "Anyway, nowdays you don't even need the disk, so Ta~da~"
#     show mc awed
#     m "Oh, this music..."
#     m "I can just see myself sitting at home after school, playing this on the home computer until dinner."
#     show mc normalside
#     m "Damn, now I want some tea."

    

#     window hide
#     scene black with fade
#     stop music fadeout(3)
#     show chibi_sleep at truecenter with Dissolve(2)
#     show top_text "After gaming all night with Sai, you fall asleep." with dissolve
#     pause
#     hide top_text with dissolve
#     show top_text "By the time you wake up, you forget this, but..." with dissolve
#     pause
#     hide top_text with dissolve
#     show top_text "Sai asked to borrow a pen and paper." with dissolve
#     pause
#     hide top_text with dissolve
#     "END"

    
    "END"
    "Seriously"

    # #Old scene where he went to class and Sa cleaned up his mess
    # show mc anxious at bounce
    # show sai shocked
    # stop music
    # m "{size=+20}HOLY SHIT I'M LATE!!!"
    # show mc vstressed
    # m "{size=+20}GOTTA RUN GOTTA RUN! SORRY!\nBE BACK IN LIKE AN HOUR!"
    # window hide
    # hide mc vstressed
    # show day_clouds at bg_scroll 
    # show bedroom_day_no_bg_clean:
    #     zoom 0.9
    # with easeoutbottom

    # play sound "door.wav"
    # pause 0.5
    # show sai sad
    # pause 0.5
    # window show
    # s "Safe travels..."
    # window hide
    # show sai worried at center
    # show day_clouds at bg_scroll 
    # show bedroom_day_no_bg_clean:
    #     zoom 0.9
    # with move
    # window show
    # s "Ahh... If only Carl were still alive..."
    # show sai normal
    # s "..."
    # show sai determinedclosed
    # s "No! That would make him sad! And it's probably tasteless anyway... That's right..."
    # show sai pout
    # s "Maybe I should go out on my own and talk to someone new..."
    # show sai angry
    # s "...But I don't even want to..."
    # s "I just wanted to say thanks... I wish he hadn't run off like that..."
    # show sai worried
    # s "He's done so much for me. I need to pay off my debt."
    # show sai happy
    # s "Perhaps... a head start with his bucket list would suffice?"
    # window hide
    # hide sai
    # show day_clouds at bg_scroll 
    # show bedroom_day_no_bg_clean:
    #     zoom 0.9
    # with dissolve


    # show photo at truecenter
    # show day_clouds at bg_scroll
    # with easeinbottom
    # play sound "page.wav"
    # show sai surprised
    # s "That's %(player_name)s! Are these your parents?"
    # show sai happy
    # s "You look so happy, %(player_name)s. You should stop worrying and smile more often, silly."
    # hide photo with easeoutbottom
    # "Next, Sai finds a strange piece of paper."
    # show paper at truecenter with easeinbottom
    # play sound "page.wav"
    # show sai normal
    # s "I wish I could read. This seems... passionate... about something."
    # show sai surprised
    # s "Oooh, his drawings are very good! Gold star."
    # hide photo with easeoutbottom
    # "And then, at the last pile..."
    # show guitarpick at truecenter with easeinbottom
    # show sai confused
    # s "What are all of these plastic triangles!? Why are there so many? Into the trash with you!"
    # hide guitarpick with easeoutbottom

label collegereturn:
    # play sound "door.wav"
    # show sai happy at left with move
    # show mc stressed at right
    # with easeinbottom
    # s "You're back! What do you think of your room? I cleaned it."
    # show mc surprised
    # m "..."
    # "It was your mess."
    # "An insurmountable task."
    # "Done like it was nothing."
    # "You should have done it."
    # show mc stressed
    # m "Why?"
    # show sai apologetic
    # s "Did... did I do something wrong? You said it was one of your goals."
    # show mc awed
    # m "No, no, it's good. It's great! It's just been a while since I've seen the floor."
    # show mc normalside
    # m "I'm just that... You cleaned up after my mess. I should've done it myself."
    # show sai happy
    # s "I wanted to ease your burden, however I could. Was I successful?"
    # show mc normalside
    # m "...Yeah."
    # show sai vvhappy
    # s "Good!"
    # show mc stressed
    # "You should be grateful. You should be thanking her."
    #m "Thanks."
    # "You have no good excuse."
    # "You're just lazy. You lack resillience. You're a bad adult. Everyone is doing better than you."
    # show mc sad
    # m "(Why do I have to feel so bad? I can't even feel grateful for what she did.)"
    # "You feel bad because you {i}should{/i}."
    # show sai shy
    # s "Did you have a good education?"
    # show mc stressed
    # m "I need to go to the bathroom..."
    # merge with above after cafe scene 


    

    
    
    
    
    show sai vshy
    s "Um... let me think... Perhaps..."
    show sai happy
    s "Water me please! It's funny, but I feel even thirstier than yesterday. So a good spray, please."

    window hide
    hide mc with easeoutbottom
    $ watered = 1
    show water_status at water_location with dissolve
    call screen water_sai_2 with dissolve
        

    screen water_sai_2:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("day2_watered_2")

    label day2_watered_2:

        $ watered = 3
    

        queue sound "spray.wav"

        queue sound "spray.wav"
        show mc happy at right with easeinbottom
        
        hide water_status with dissolve
        window show
        m "That was was free. Tell me something you actually want now."


    show sai vhappy
    s "Well, I would really like to go to the garden again. I loved being surrounded by nature."
    show sai surprised
    s "Not that I'm complaining about the city!"
    show sai vshy
    s "There's just something about the dirt beneath me, the plants around me, and the escape from structure, that give me this... {i}wonderful{/i} feeling of tranquility. I truly love it."
    s "So if it's not too much to ask-"
    show mc happy
    m "So basically, you love nature and you want to get away from the city."
    m "I have an idea..."
    show sai happy
    s "What is it?"
    show mc annoyed
    m "It's..."
    show mc happy
    m "A surprise. You can find out tomorrow."




    

label sai_d3:

    show text "{color=#000000}At least, you have your favourite dream."
    with dissolve
    pause
    hide text with dissolve

    scene black wi  th fade

    hide window
    pause 2
    play music "heartbeat.wav"
    "That song is plaguing my mind..."
    "\"Life is but a dream\"."
    "It feels true."
    "This all has to be one, horrible, messed-up dream."
    "I've just been sleeping this whole time, right?"
    "I'm still six years old."
    "I'm still happy..."
    "Maybe when I open my eyes..."

    show day_clouds at bg_scroll
    show bedroom_day_no_bg_clean:
        zoom 0.9
        matrixcolor TintMatrix("#256fff")
    

    with Dissolve(3)

    play sound "static.wav"

    "..."
    "You bask in this feeling."
    "Staring at the ceiling."
    "Your brain screaming."
    "Your thoat aching."
    "This is just so hopeless, isn't it?"
    "You could stay here and torture yourself some more,"
    "Or, you could \"Start the day!\"."
    menu:
        "Torture yourself.":

            
            "..."
            "The more you stare,"
            "the more the static in your ears grows,"
            "the more you feel the pressure,"
            "The more discouragement grows."
            "..."
            "Why is it so hard?"
            "Why? {i}Why?{/i} {b}Why?{/b} {u}Why?{/u}"
            "{i}Please{/i}..."

    window hide
    show sai happy at left with easeinbottom
    window show
    "When you open your eyes, Sai is there, doing her own thing."
    
    s "Good morning, %(player_name)s!"
    "You're supposed to answer, but your throat is clogged, so you give her a weak wave."
    "But... that wasn't good enough."
    show sai normal
    "What happened?"
    window hide
    show mc normal at right with easeinbottom
    window show
    m "Nothing."
    show sai worried
    s "Really? You seem overcast."
    m "I'm... fine."
    play sound "heartbeat.wav"
    "You don't have the energy to fake a smile."
    "You just can't do it anymore."
    "You feel like a husk."
    m "..."
    show sai apologetic
    s "..."
    hide sai
    hide mc
    show sai_hug
    with dissolve
    stop music
    play music "date_musicbox.mp3" fadein(3) #if time, do what did for Button bad end, and make 2 layers for a sad song
    s "I understand. It is difficult to speak sometimes."
    s "I hope this hug conveys to you..."
    s "...that no matter your state..."
    s "...you can be as you are, and I will not judge."
    s "Sadness is a part of life. It is inevitable."
    s "In a way... I am glad you are suffering."
    s "Because I suspect that I have now seen more of you than you let even humans see."
    s "And, to end my insensitive speech, that is an honour. Thank you."
    s "I shall now disengage from the hug-"
    hide sai_hug
    show sai_hug_mc_cry
    with dissolve
    # play music "saddersong.wav" # add next layer here to make more intense
    m "I'm sorry for lying, Sai."
    s "O-oh?"
    m "I'm really not doing okay."
    m "That's the truth."
    s "..."
    s "Thank you for telling me, %(player_name)s."
    s "Do you know what you need?"
    m "I think... I need... a hug..."
    hide sai_hug
    show sai_hug_happy
    with dissolve
    s "Thankfully I have an infinite supply of those."
    m "..."
    stop music fadeout 2
    s "..."
    
    hide sai_hug_happy with dissolve
    show sai normal at left
    show mc stressed at right
    with dissolve
    play music "normal.mp3"
    m "Hah... I don't know what to do! I'm just fucking depressed!"
    s "..."
    show mc worried
    m "I just want to die!"
    show sai happy
    s "%(player_name)s."
    show mc stressed
    m "What?"
    show sai shy
    s "Would you like it... if we died together?"
    stop music
    show mc shocked
    m "W-"
    s "..."
    m "..."
    m "Did you really just say that?"
    show sai surprised
    s "I did. I'm genuinely offering to commit suicide at the same time."
    show awed
    m "..."
    show mc confused
    m "Why?"
    show sai shy
    s "I'm a mushroom. I don't last that long. I think I'll be dying tonight anyway."
    show sai vshy
    s "At least this way, no one is lonely."
    
    
    
    
    
    show mc awed
    m "..."
    show mc shout
    m "YOU'RE GOING TO DIE TONIGHT??? SINCE WHEN!? WHY DIDN'T YOU TELL ME!?"
    show mc worried
    m "What the hell! I've been wasting your time! You should have just-"
    show sai normal
    s "Death is just another part of life."
    m "I don't get it. How can you be so indifferent? You're... going to die."
    m "We'll never see eachother again. We can't hug or talk. You can't eat anymore food. Aren't you sad?" 
    s "No, because when I'm dead, none of those things will matter."
    show mc stressed
    m "You're so strange. I thought... you loved life."
    show sai determined
    s "I do love life."
    show sai surprised
    s "I just don't dread death."
    show sai happy
    s "It's okay if you can't sympathise."
    show sai vhappy
    s "Until it's over, I can do anything I want."
    m "I'm not ready for you to die."
    show sai sad
    s "I'm sorry about that. I really am. You were a huge part of my life, and I feel bad to leave you so abruptly."
    show sai shy
    s "Please don't let it discourage you."
    m "..."
    show mc cry
    m "You're the first friend I've made who didn't dislike me."
    show sai surprised
    s "That's probably because you haven't left your room enough, %(player_name)s."
    show sai vhappy
    s "I have a feeling that if you go out more regularly, you will find someone to replace me."
    show mc shout
    m "Don't say that!"
    show mc cry
    m "That's horrible..."
    show sai vshy
    s "Perhaps that was too crude, but you know what I mean."
    show sai determined
    s "Don't lock yourself up in your room anymore. You and I both know there's no benefit."
    show mc sad
    m "I know. Do you have any other requests?"
    show sai happy
    s "I'd quite like if you visited the garden more regularly and looked after Mrs Tomato."
    show sai vvhappy
    s "Oh, and get a pet spider and look after it!"
    show sai happy
    s "That way, you have to get up out of bed eventually."


    return


    show mc normal
    m " It's really nothing important. Just forget it. Just go back to enjoying yourself, okay?"
    show sai sad
    s "I don't mind listening."
    show mc vannoyed
    m "It's not even worth talking about."
    show sai worried
    s "Don't mask..."
    
    
label sai_d3_camp:

    play music "normal.mp3"
    scene day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show dirty3
    show bottle
    show mc stressed at center
    with easeinbottom
    show day_3 at topleft
    show sai_affection at topright
    with dissolve

    "When you wake up, the first think you do is worry about the day ahead."
    m "(I just need to follow the plan, and everything will be alright.)"
    show mc normal
    m "(Gotta buy some equipment, some food, then take a bus and a train, then it should be a 20 minute walk to the camping ground.)"
    show mc sad
    m "(That's a lot of walking... Lord, what have I gotten myself into?)"
    
    show sai happy at left with easeinbottom
    show mc at right with move
    s "Good morning. I hope you are feeling mentally prepared."
    show mc normalside
    m "No comment."
    show sai normal
    s "Things are simpler than you think."
    s "You mustn't dwell on what-if's. That is what has kept you stagnant."
    show mc stressed
    m "*Sigh*. Anyway, before we go, let me get some coffee first."
    show sai shocked
    s "E-eh!?"
    show mc confused
    m "What's wrong? You can have some too..."
    show mc surprised
    m "Oh wait... you can't."
    show sai pout
    s "You're going to drink my favourite drink in front of me?"
    show mc happy
    m "Isn't water your favourite?"
    show sai normalside
    s "Coffee is a close second."
    show sai normal
    s "On that note, please commence my daily watering."

    window hide
    hide mc with easeoutbottom
    $ watered = 2
    show water_status at water_location with dissolve
    call screen water_sai_d3 with dissolve
        

    screen water_sai_d3:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("day1_watered_d3")

    label day1_watered_d3:

        $ watered = 0
        pause 1
        queue sound "spray.wav"
        $ watered = 1
        pause 1
        queue sound "spray.wav"
        $ watered = 2
        
        show mc normal at right with easeinbottom
        show sai happysigh
        hide water_status with dissolve
        window show
        s "Ah... This is one of life's simple pleasures."
        show sai happy
        s "Are you ready? Let's embark on our day of adventure! Come good or bad, it will be a entertaining time."
        show mc stressed
        m "Please don't jinx us."
        

    
    window hide
    hide mc
    hide sai
    with easeoutbottom
    stop music fadeout(3)
    scene black with Fade(0.5, 1.0, 0.5)  

    
    play sound "door.wav"
    play music "date.wav"
    show chibi_mc at slightright
    show chibi_sai at slightleft
    with easeinright
    window show

    "You and Sai both get some coffee to go. After some debate, it is decided that liquids are fine for her."
    "You stop by an outdoors warehouse to buy a firestarting kit and some thermal gear to add to your backpack."
    "Finally, after a bus ride to the train station..."

    window hide
    hide chibi_mc
    hide chibi_sai
    with easeoutleft

    scene train
    
    show mc stressed
    show sai normal
    s "What seems to be the problem?"
    show mc shout
    m "The trains aren't working! So we just came here for nothing. I should have checked the schedule. I KNEW this was a mistake!"
    show sai annoyed
    s "You're too quick to give up. Calm down. Everything's okay."
    show mc stressed
    m "I don't know what to do. It'll take too far to just walk, and I'm already tired."
    show sai shy
    s "Cheer up, %(player_name)s! Being challenged like this is part of the fun of adventures."
    m "(HOW!?)"
    show sai normal
    s "I can see you are stressed. I'll give you some time to calm down while I try find a solution."
    window hide
    hide sai with easeoutbottom
    window show
    show mc sad
    m "This is why it's better to be prepared. Now we're just in a frustrating situation."
    "You can't even enjoy the nice weather, or feel excited anymore."
    show mc vstressed
    m "This whole trip is a failure."
    show sai happy at left with easeinbottom
    s "Solution found. A man is renting bicycles over there."
    show mc surprised
    m "Bikes? I guess I could ride one."
    show mc normal
    m "All the way there..."
    show mc normalside
    m "Hah..."
    show sai think
    s "The land is mostly downhill, so you don't need to worry about exerting yourself."
    show mc stressed
    m "(Until the return trip.)"
    show sai happysigh
    s "See? Your worries are in vain. It all worked out."
    show sai shy
    s "Um, but since I cannot ride, you'll have to take me too."
    show mc vstressed
    window hide
    scene black with fade
    stop music fadeout 2
    window show
    "And that's what you did."
    window hide
    scene farm with fade
    play music "cycle.mp3"

    window show
    "After renting the bike for two days, you begin annoyedly pedalling."
    "Past the city, it become easier, and you let your brain go offline while you follow the simple route on your phone."
    window hide
    show farm_people with dissolve
    pause 1
    window show
    s "Are you having fun, %(player_name)s? We are out the city!"
    m "Yeah. It's nice."
    "It's not to much effort, but the light exercise of muscles that you've been neglecting feels good."
    m "(And the farmlands are really pretty too. If we were on the train, I'd probably just be on my phone.)"
    "At least today wasn't a complete waste."
    s "These animals are so strange. Are they pettable?"
    m "Yeah, let's have a break. There's a vending machine over there. I'll get us something to drink."

    window hide
    jump icecreamscene

label icecreamscene:
    show icecream with dissolve
    pause 1
    window show
    "But it wasn't a normal kind of vending machine."
    window hide
    show mc surprised at center
    with easeinbottom    
    m "Wait, it sells {i}ice cream{/i}!?"
    show mc awed
    m "\"Support local dairy farmers. Made loving from our free-range cows.\" That's kinda cool. I was already sold, but still. Nice to know."
    show mc confused
    m "(But... what about Sai? If I get one for myself, that's be like flaunting a bottle in front of an alcoholic!)"
    show mc stressed
    m "(But I really want one! I love ice cream! GAH!)"
    window hide
    show sai confused at left with easeinbottom
    show mc at right with move
    s "How fascinating. A travelling cold box."
    show mc slightsad
    m "It sells ice cream, which is a kind of cold treat."
    show sai shy
    s "Sounds interesting. Let's eat some together."
    show mc surprised
    m "But then we'll have to wash you out all over again. You said you {i}hated{/i} it."
    show sai happysigh
    s "If it comes to that, I'll do it. I just don't want to hold myself back today."
    show sai vshy
    s "However, I have a feeling like won't matter."
    show mc confused
    m "Why won't it matter?"
    show sai blush
    s "Well... it's just a feeling. Today, I am prioritising experiences with you."
    show sai vshy
    s "Um, so, which one do you recommend?"
    show mc normalside
    m "So today is one of those act-first, think-later days, huh?"
    "Your instinct is to scoff at such irresponsibility, but... you're kind of tired of being so strict about everything."
    "Alright, let's just have fun."
    show mc annoyed
    m "Lemon for sour-enjoyers like you, and strawberry for sweet tooths like me."
    window hide

    hide mc
    hide sai
    with easeoutbottom
    window show
    "The endless violet-blue sky expands above you."
    "The endless wind carries the scents of farm and wild flowers from miles away."
    "You and Sai sit next to each other at on a log stump, eating your ice creams, while nature shifts in the tranquil, warm breeze." 
    window hide
    show sai eathappy at left
    show mc eat at right
    with easeinbottom
    
    show say happysigh
    window show
    s "Mmm, tangy, bitter~ this is so much better than your oversweetend milkshake."
    m "You like your stuff, and I'll like mine."
    show sai pout
    s "Although... your's looking so good too..."
    show mc annoyed
    m "What? Want some?"
    show sai happy
    s "Yes please."
    show mc normal
    m "Too bad."
    show sai surprised
    s "..."
    show sai sad
    s "..."
    show mc happy
    m "Just joking."
    "You wave the ice cream before her."
    show sai eatdown
    s "*Bite*"
    show sai eathappy
    s "Shoo goooooood~"
    s "Hrank-kyuu!"
    show mc confused
    m "You've got ice cream all over your face. They should really have some napkins available."
    "But Sai ignores you - She's already excitedly chattering away."
    show sai vhappy
    s "So this is the power of combination!"
    s "The lemon with the strawberry is a work of art. You must experience it!"
    show mc normalside
    m "Nah... I'm okay."
    show sai determined
    s "I insist! Have a taste of mine. You might reget it if you don't."
    show mc surprised
    m "(Wait, is she threatening me?)"
    "It turns out, she was."
    "Without waiting, Sai shoves her lemon sorbet in your face. You're forced to open your mouth immediately, or else hace a face smushed with cold, sticky icecream."
    show mc vstressed
    m "N, wai- gmpf!"
    show sai excited
    s "Do you like it too?"

    stop music fadeout 2
    show white with dissolve
    "Her words disappear, as your mouth is raided by the bitter-sweet flavours."
    "The strawberry coating my tongue intermixes with the sharp tangs of lemon."
    "It's..."

    show mc surprised
    hide white with dissolve
    m "Owaaa~"
    play music "cycle.mp3"
    show sai happysigh
    s "Indeed! One cannot help but moan after such a delight."
    show sai happy
    s "We shall share our ice creams. Ah, symbiosis is truly magnificent!"
    show sai surprised
    s "Oh, %(player_name)s, you have ice cream on your face."
    show mc normal
    m "And whose fault do you think that is? So where is it?"
    show sai normal
    "She points at your chin."
    "You try to stick your tongue out and try to lick it off."
    show mc awed
    m "Did I get it?"
    show sai pout
    s "No, not at all. I'll just do it."
    hide sai
    with dissolve
    "It's so casual that you don't suspect a thing, but then she closes the distance-"
    "- and places a kiss on your chin!"
    "Or at least, that's what it feels like initially."
    "Then you realise her tongue is licking at a spot near the very edge, just cleaning up some spilled ice cream."
    show sai happy with dissolve
    s "There you go! Now you are clean."
    show mc blushside
    m "(She licked me! Does she realise how suggestive that is to humans!?)"
    "Probably not."
    show sai normalside
    s "As good things must pass, so too, must ice cream be all eaten. Our delicious desserts are finished."
    window hide
    stop music fadeout 2
    jump camp_arrive

label camp_arrive:
    scene camp with Fade(0.5, 1.0, 1)
    show mc pant at right
    show sai happy at left
    with easeinbottom
    window show
    m "Huff... huff... we're... here..."
    show sai surprised
    s "Ah... I feel like I am in the womb of mother nature herself."
    s "Hues of greens and browns compounding upon another like rainbows..."
    m "Ugh... huff... finally {i}sitting{/i}... huff..."
    show sai vhappy
    s "I feel so... at home."
    m "Makes.... huff.... sense."
    show sai surprised
    s "Are you alright, %(player_name)s?"
    m "I'm... huff... just tired..."
    show sai normal
    s "Ah, fatigue, the human affliction."
    show mc annoyed
    m "It's not a sickness!"
    show mc confused
    m "We got here pretty late. Let's focus on setting up the camp first."
    
    # hide sai with easeoutbottom
    # show mc worried at center with move
    # m "S-Sai! Where are you going!? It's dangerous to be alone..."
    # show mc shout
    # m "Hold on! I'm coming! Don't eat anything weird!"
    # window hide
    # hide mc with easeoutbottom
    # show camp_gear with dissolve
    # window show
    # "You dump your gear at the campsite and race after her."
    # "You and Sai follow the trails aimlessly, and enjoy the presence of animals around you."
    # "Weavers and dragonflies come buzzing in from the nearby river."
    # "Squirrels dart around chaotically."
    # "Butterflies drift between the swaying trees."
    # "It smells so earthy, fresh and humid."
    # "This is all you wanted for so long. You let your worries disappear with every crunch underfoot."
    window hide
    show camp_gear with dissolve
    pause
    window show
    "You and Sai work together to set up your supplies for the night."
    "And then, proceed to spend much longer than you expected trying to get a fire started."
    window hide
    play sound "fire.wav"
    show camp_fire_gear with dissolve

    show mc surprised at right
    show sai normal at left
    with easeinbottom
    play music "camp_sunset.wav"
    window show

    m "Yes! It's alive! My first fire!"
    s "Very well done."
    show mc happy
    m "Marshmellow time!"    
    show mc annoyed
    m "And some corn for you since I know you don't like sweets."
    show sai surprised
    s "That was thoughtful of you."
    m "Yeah, surprising, I know."
    show sai normal

    s "%(player_name)s, I think it is time to do it."
    show sai determined
    show mc surprised
    m "\"It\"?"
    show sai normal
    s "To eat me."
    show mc normal
    m "I don't think it's necessary anymore. I'm feeling good."
    s "%(player_name)s, you feel good now, but will you still, when you return home?"
    s "Going on this mental trip will help you. I know it intrinsically. You need to be brave and trust me."
    show sai confused
    s "Do you tust me?"    
    show mc normalside
    m "..."
    show mc normal
    m "Of course."
    show sai happy
    s "Thank you. Then nibble my finger, please."
    show sai determinedclosed
    s "JUST a nibble, understand?"
    show mc stressed
    m "Alright. Here goes nothing..."
    "Are you SURE?"
    m "(I'm trusting Sai on this. There's no need to doubt her now.)"
    show mc normal
    m "*nibble*"
    show mc vstressed
    m "EUuughgh!"
    show sai vvhappy
    show mc shocked
    m "You're not as sweet as you look."    
    show sai vshy
    s "I'm sorry for the unpleasant taste."
    show mc blushside
    m "Well, I dunno. Maybe I could get used to it. Taste's subjective, like you said yesterday."
    show mc confused
    m "But anyway, When am going to... feel the effects?"
    show sai happy
    s "In thirty minutes to an hour, I believe."
    show mc worried
    m "So it'll be a surprise. Great. My favourite. What should I do?"
    s "All you need to do is relax and let yourself enjoy the present."
    m "I feel weird."
    show sai shocked
    s "Already!?"
    show mc sad
    m "No, not like that. I ate you. You literally sacrificed a part of yourself for me. I feel guilty."
    show sai confused
    s "How confusing... I asked you to do it. I'm {i}grateful{/i}. Now please relax."
    show mc annoyed
    m "Okay! It's time to roast some marshmellows!"
    show sai happy
    s "I'll join you and try one. I'll fetch the packet."
    window hide
    hide sai with easeoutbottom
    show mc normalside at center with move
    m "{size=-20}I just wanted to say thanks.{size=+20}"
    window hide
    hide mc
    with easeoutbottom
    "You find two long sticks on the forest floor, dust them off, then skewer a marshmellow onto it."
    "Sai follows your lead."
    "You both sit on the mat and hold it excitedly over the fire."
    play sound "flameburst.wav"
    "Your marshmellow immediately bursts into flames!"
    show mc surprised at right
    show sai surprised at left
    with easeinbottom
    s "Ooh! That looks fun."
    show sai happy
    "Sai lowers her marshmellow into the flames too, where it also catches on fire."
    show mc stressed
    m "That was an accident. God, I'm so bad."
    show mc normal
    m "Well, may as well eat it."
    show mc eat
    "You lift your piece of charcoal to your lips."
    show mc surprised
    m "(Mm! Wait, why is this so good?)"
    show sai eat
    s "This is somewhat tolerable. The ashiness neutralises the sweetness nicely."
    hide mc
    hide sai
    with easeoutbottom
    "The minutes tick by while you enjoy roasting corn over the fire with Sai."
    stop music fadeout 2
    window hide
    show black:
        alpha 0.2
    with dissolve
    play music "camp_night.wav" fadein 2
    window show
    "At some point, you look up from the dance of the flames and realise that you're submerged in darkness."
    "A chill wind plays on your skin, and edge closer to the fire. What if it goes out? You haven't stockpiled wood."
    "You suddenly feel very unprepared."
    "Just like with life."
    window hide
    show eyes with dissolve
    play sound "scary_noise.wav"
    window show
    "Is something's watching you...?"
    show mc worried
    with easeoutbottom
    "Is it a wild animal? A bear? A mountain lion? You can't see properly, but things seem to be moving."
    m "Sai, how long has it been?"
    show mc at right with move
    show sai happy at left with easeinbottom
    s "I'd say nearly an hour. Do you feel any different?"
    show mc stressed
    m "Yeah. Scared. I don't know if this was a good idea."
    show mc worried
    m "I don't have anything to protect myself with if an animal attacks us."
    show sai shy
    s "I don't sense anything, so you can relax."
    m "(But I'm certain there's something there!)"
    show sai vhappy
    s "Feeling more sensitive to your fears is a natural part of the process."
    show sai happy
    s "That's why I'm here to comfort you if you panic."
    show mc stressed
    m "That makes no sense. I don't think I want to do this anymore. I need to throw it up!"    
    show sai determined
    s "Even if you do, it'll be too late."
    show sai happy
    s "The best way forward is to calm down. How about a hug?"
    
    # make textbox wriggle, make sai wriggle.
    show camp_fire_gear:
        matrixcolor TintMatrix("#6F6FBB")
    show eyes 
    with dissolve
    show mc shocked
    m "Um... Sai... you said things were going to move and stuff, right?"
    s "Yes, that's to be expected."
    m "Now my teeth are tingling!"
    show sai shy
    s "That's normal."
    show mc worried
    m "(I don't think it is! I'm not going to die, am I?)"

    "Is this the end? Are you ready? The empty, eternal void of non-existance is waiting for you."
    show black with fade

    show text "Maybe the next time you blink, everything will end."
    with dissolve
    pause
    show text "You'll be nothing. Forever. You'll forget everything, as if it never even happened."
    with dissolve
    pause
    show text "Stop lying to yourself. You don't want to say goodbye to life. You just like there's an escape."
    with dissolve
    pause 
    show text "You don't want to give up. You know it."
    with dissolve
    pause 
    hide text
    hide black
    with dissolve

    show mc stressed
    m "(Could you shut up!? Why are you being so loud!?)"
    show mc worried
    m "Sai, it's like there's someone talking to me in my head, and I can't stop it."
    show sai determined
    s "Good. Listen to it and try to understand where it's coming from, okay?"
    show mc sad
    m "It's really depressing..."
    show sai shy 
    s "Sometimes you need to hear something you don't want to hear, %(player_name)s."
    show sai vvhappy
    s "Just talk with it a bit, please?"
    window hide
    hide sai with easeoutbottom
    
    show head normal at left with dissolve
    window show 
    head "Yes. Let's talk."
    show mc shocked
    head "What are you going to do when you get back?"
    show mc worried
    m "(Why do I have to stress about that now? I just want to enjoy camping with Sai.)"
    head "You can't relax. The problem isn't dealt with."
    head "You can't keep ignoring it."
    head "How much longer can you last?"
    head "You have no plans for the future. It's hopeless."
    show mc vstressed
    m "(I don't know what I'm supposed to do!)"
    m "(I don't know why I'm in university! I don't know what to aim for! I'm just stressed all the time.)"
    show mc cry
    m "(Where did it all go wrong?)"
    head "You're the problem. You do nothing but pity yourself."
    show mc vcry
    m "(That's not fair... Just doing anything is enormous effort for me. I'm always tired.)"
    head "You know you have to do something about it."
    show mc stressed

    window hide
    stop music fadeout 2
    scene POV_hands_human with fade
    pause 2

    window show
    m "(What am I? Why am I here?)"
    m "(What is life?)"
    m "(I'm going to die one day.)"

    window hide

    show POV_hands_skeleton with dissolve
    pause 2

    window show

    m "(I'm going to become a skeleton.)"
    m "(I'm going to disappear.)"
    m "(Nothing will have mattered.)"
    m "(I should just do what I want, while I can. It should be that simple.)"

    window hide

    show POV_hands_human
    pause 0.5
    show POV_hands_skeleton
    pause 0.5
    show POV_hands_human
    pause 0.5
    show POV_hands_skeleton
    pause 0.5
    show POV_hands_human

    window show 

    m "({sc=2}{color=#000000}I have to stop wasting time!)"
    m "(I have to change my life.)"

    show text "I have to change my life."
    pause 0.2
    show top_text "I have to change my life."
    pause 0.2
    show top_left "I have to change my life."
    pause 0.2
    show top_right "I have to change my life."
    pause 0.2
    show bot_right "I have to change my life."
    pause 0.2
    show text "I have to change my life, else I'll stay like this."
    pause 0.2

    





















label camp_v2:
    "You're pathetic."
    m "Why are you a girl!?"
    "Because you're so pathetically alone all the time that you've hallucinated me up."
    "I think the more important question is, what are you doing?"
    "You're at the end of your rope."
    "There's an swiss army knife right there? Why don't you grab it?"
    m "Jesus. I do NOT want to think about this right now!"
    "Or you could just throw yourself off the cliff? Wouldn't that feel so awful? Ruining your life before ever actually doing anything?"
    "Don't you just hate everything at this point, for all it's done to you?"
    m "Sai! Is it normal to not stop thinking?"
    s "Perfectly normal. Trouble?"
    m "My mind is bullying me way more aggressively than usual. It's genuinely depressing me."
    s "I can offer a reassuring hug."
    m "Hope it works."
    show sai_mc_hug with dissolve
    "..."
    "That's very cute. Sai is so nice and patient and kind. You guys have bonded a lot recently, so.."
    "What if you killed her too?"
    m "(NO! I don't want to do any of that!)"
    m "My thoughts are getting out of control. It's like someone's whispering for me to do all these horrible things."
    m "How do I ignore them?? Tell me what to do, Sai."
    s "Think about what's making you feel that way. What causes your stress?"
    m "I don't know! School?"
    s "Think..."
    hide sai with dissolve
    show mc normalside at center with move
    m "I feel stress because..."
    show mc stressed
    m "(Becaue of everything I have to do.)"
    "And everything you probably won't do."
    m "(I might fail. I might have to move back in with my parents.)"
    "And you'll have cost them so much money."
    "You'll be such a burden. An embarrassment. A failure. A waste. A disappointment."
    m "(I don't want my mom to look at me like that. She expects so much of me.)"

    

























    



label hike:
    scene hike with fade
    show sai normal at left
    show mc sad at right
    with easeinbottom
    s "Looking from this vantage, I realise that there are so many lives before us. All of them have needs, wants, struggles and fears."
    s "I feel so connected to everyone, because, no matter what, we're all in this life thing together."
    show sai happy
    s "What do you think, when you look at everything from this height?"
    m "Pant...pant...pant...."
    show sai shy
    s "Maybe later."
    show mc shout
    m "I can't believe you just... started hiking! You're too fast!"
    show sai happy
    s "My apologies, but life doesn't last forever. I wanted to see the sunset."
    show mc normal
    m "It is a pretty good sunset."


    menu:
        "On the top, looking down, everything seems so much smaller..."
        "Nothing I do will ever be enough.":
            jump validation_talk
        "I've got an intrusive thought.":
            show mc awed
            "Sai is standing awfully close to the edge of the cliff."
            "You could kill her right now."
            "It'd be so easy. In three seconds, you could ruin her life. You could commit the ultimate sin. You could watch her face twist in horror."
            "You could watch her body hit the ground and lay there motionless."
            "You'd really hate yourself then."
            show mc vstressed
            m "(What the fuck!? That's repulsive! I don't want to think about this!)"
            "But you can still feel it, can't you? You've already imagined it, so it's like you did it. Don't you feel awful?"
            m "(YES!)"
            show sai vshy
            s "It's okay to be scared... It's not particularly safe here, and we're so high up..."
            "She's so trusting. Wouldn't you like to break that trust?"
            m "(I hate this! I want to stop thinking about this! PLEASE STOP THIKNING!)"
            show sai vhappy
            s "At the same time, this is my first time experiencing fear like this. It's exhilirating, and kind of primal..."
            "She's basically asking for it."
            menu:
                "Push Sai off the cliff.":
                    m "Hey, Sai."
                    show sai happy
                    s "Yeah?"
                    "You reach forward..."
                    "...and pull her away from the edge."
                    m "Don't stand so close to the end. It's too risky."
                    show sai vvhappy
                    s "You're right. I got overzealous."
                    m "Random question. Have you ever had an intrusive thought?"
                    show sai determinedclosed
                    s "Hmm..."
                    show sai surprised
                    s "Oh!"
                    s "I don't know if this counts..."
                    show sai shy
                    s "...but I  {i}did{/i} think about kissing you."
                    show mc surprised
                    m "..."
                    s "..."
                    show mc shocked
                    m "..."
                    show sai confused 
                    s "What's the matter? You're facial expression reads as shocked."
                    m "I am."
                    m "I thought mushrooms didn't have feelings like that!"
                    show sai happy
                    s "Why? I'm capable of other emotions."
                    show sai vshy
                    "Love supposedly feels wonderful. Is it weird that I want to experience it for myself?"
                    show mc annoyed
                    m "Oh, now I get it. it's just another experience to collect."
                    show mc blushside
                    m "(Does that mean I could offer to... do that... with her? Do I have a chance?)"
                    show mc sad
                    m "(What am I saying!?)"
                    show mc worried
                    m "U-um, anyway! That's not even an intrusive thought! That's just an... impure one."
                    show sai pout
                    s "Kissing isn't impure! It's completely natural to want to do it."
                    show mc blushside
                    m "But it's not an intrusive thought!"
                    show mc shout
                    m "I was - I was thinking about pushing you off the cliff! THAT'S an intrusive thought!"
                    show sai shocked
                    s "A-a-ahm... Is that a genuine desire?"
                    show mc vstressed
                    m "No!"
                    show mc worried
                    m "I saw how far down everything is, and how close we are to the edge, and some part of my brain just went-"
                    m "\"I could kill you right now and get away with it, haha.\""
                    show mc shout
                    m "I don't even know why I'm telling you this!"
                    show sai vvhappy
                    s "Perhaps to entertain me? It is quite funny."
                    show mc shocked
                    m "It is?"
                    hide mc
                    hide sai
                    with easeoutbottom
                    jump camp_night

                    
   
    label validation_talk:
        m "I don't know. It's kinda depressing, because..."
        
        show mc vannoyed
        m "... it makes me realise how little I matter in the grand scheme of things. Nothing I do will ever matter enough to last more than a few centuries at best."
        show mc stressed
        m "Eventually, I'll be forgotten. And there's nothing I can do about it."
        show sai normal
        s "It's okay if you're forgotten. It's natural. And you won't be alive to experience it anyway."
        show mc sad
        m "It's still depressing."
        show sai surprised
        s "So you want people, who you'll never know, to remember you? Why?"
        show mc normal
        m "Because that's literally succeeding in life! Making history, getting taught to children as some awesome figure - that's how you know you've won life."
        m "That's all I want. Just to die with no regrets, knowing I did it."
        show sai confused
        s "You \"did it\"..."
        show sai surprised
        s "You're saying that whether you die with regret or not is based on what other people think of you?"
        show mc normalside
        m "You don't gotta phrase it {i}that{/i} way."
        s "Living to be remembered. Striving for acknowledgemnt and recognition. That's not... um..."
        show sai normal
        s "It's like you want to turn into a trophy, and you don't care what the embossment says, as long as it's shiny."
        show mc annoyed
        m "Yeah, still not seeing the problem. Being hailed as a hero sounds good."
        show mc surprised
        show sai angry
        s "But that's so output orientated! Do you want to enjoy your life, or do you want to fulfill this foolish notion you've set for yourself!?"
        show sai determined
        s "What a waste of your precious life!"
        show sai shocked at bounce
        s "Ah!"
        s "W-What am saying? I'm sorry. That was rude. I just worried! I-I-I-"
        show mc annoyed
        m "Don't worry about it. Seeing you angry was funny."
        show sai sad
        s "...Thank you. Haaah. I think I'm feeling kind of tired."
        show mc happy
        m "Let's go chill in the lake then. I saw a rowboat earlier."

        hide mc
        hide sai
        with easeoutbottom
    
label camp_night:    
    
    
    #alt start
    "You and Sai spend the rest of the afternoon in the true camping experience and explore anything that catches your eye!"
    "Moss covering trees? Humming dragonflies? Sugarbirds? You check them all."
    "You don't realise when you started enjoying yourself, but you feel the worries disappear from your mind."
    
    scene lake with fade

    #play sound "row.wav"

    "Rowing: As the the sun dips into the waters, you row Sai around while she leans back and shuts her eyes."
    "The sound of the tinkling waters, the cool lake air, the humming dragonflies that hover irratically around you boat..."
    
    s "Tranquil."
    s "My mind feels crystal-clear. I'm not even thinking anymore. I'm just sensing the life around us... and basking in the experience."
    s "I'm so glad I got to have this memory with you."
    "At that, Sai opens her eyes, and looks at you."
    show sai happy at left
    show mc happy at right
    with easeinbottom
    s "Thank you, %(player_name)s."
    m "I'm just happy you're enjoying yourself."
    show sai vhappy
    s "I've been meaning to ask you..."
    show sai vshy
    s "Um... I... was... wondering... if..."
    show sai shy
    s "If... if..."
    show sai blush
    s "I-I-I-"
    show sai apologetic
    show mc cute
    m "Just say what you want to say already! What happened to being assertive?"
    show sai angry
    s "I don't know why it's so hard to talk suddenly."
    show sai sad
    s "... frustrating..."
    show mc annoyed
    m "Relaaaax. We're on vacation. Let's the bad vibes flow right out of you."
    show sai worried
    s "Haaaaaah... {size=-20}I still have some time. I'll try later."
    window hide

    scene camp with fade
    



    return





    if high:
        s "It's time now. We should do it."
        show mc awed
        m "We should do \"it\"?"
        show sai surprised
        s "Yes!"
        show sai vhappy
        s "We should put on some nice music, dim the lights a little... maybe maybe sure we have enough water. It's going to make you thirstier than you think."
        s "I hope your bed is ready, because you'll be lying on it a lot."
        show mc shocked
        m "I'll be lying on it? What about you?"
        show sai happy
        s "I'll be doing whatever I must to make sure it's an enjoyable experience."
        show mc worried
        m "This has to be a misunderstanding..."
        show shy sai shy
        s "It's okay to be nervous. That's perfectly natural, especially since it's your first time."
        show sai vshy
        s "But don't worry! I want to take it gently with you and make sure you're properly prepared."
        show mc vblushside
        m "Sai, I don't know how to say this... but I'm not... doing {i}that{/i} with you."
        show sai shocked
        s "What! But... why?"
        m "It's embarrassing. I'm just not ready. We've only known each other for like... 24 hours!"
        show sai sad
        s "Oh... I thought you were comfortable around me. I overestimated our relationship, I suppose."
        m "But we hardly know each other."
        show sai worried
        s "You know everything about me. And I've know you for my whole life."
        show mc shout
        m "Look, that's {i}technically{/i} correct, but I'm just not-!"
        show mc vblushside
        m "You're cute and all, but we haven't even kissed yet!"
        show sai blush
        s "..."
        s "I sense a misunderstanding."
        show sai vshy
        s "Um... %(player_name)s... you didn't think I was talking about sex yet again, are you?"
        show mc confused
        m "..."
        show mc vstressed
        m "..."
        show sai shy
        s "While I'm honoured you see me as cute, I must decline your offer to fornicate. I don't -"
        show mc vshout
        m "I was NOT offering! I was trying to decline YOU!"
        show sai vvhappy
        s "Hehe, anyway, I need you to do something for me."
        m "I've already decided to trust in you, so... order me around, I don't care."
        s "First, we need water, snacks, and some music."
        window hide
        hide sai
        hide mc
        with easeoutbottom

        default has_music = 0
    default has_music_correct = True
    default has_water = False
    default has_snacks = False
    
    call screen getstuffinorder with dissolve

    screen getstuffinorder:
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.371 ypos 0.370 idle "pc/phone_idle.png" hover "pc/phone_hover.png"
            action Jump("get_music")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("get_water")
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
            action Jump("get_snacks")

    label get_music:
        if has_music == 0 :
            play music "sad_date.mp3"
            $ has_music += 1
            $ has_music_correct = False
            
        elif has_music == 1:
            play music "night.mp3"
            $ has_music += 1
            $ has_music_correct = False

        elif has_music == 2:
            play music "high.wav"
            $ has_music += 1
            $ has_music_correct = True

        else:
            play music "trip.mp3"
            $ has_music_correct = True
            $ has_music = 0   

        if has_water and has_music_correct and has_snacks:
            jump everything_in_order
        else:
            call getstuffinorder


label everything_in_order:
    
    show sai vhappy
    s "I can feel it intuitively, almost like I'm floating. This atmostphere is perfect."
    s "It's time to eat it."
    "Uh oh."
    "You're not ready."
    show mc worried
    m "Ahhh... actually, I dunno."
    show sai determined
    s "Trust me! I'll look after you, so everything will be okay as long as you listen to me."
    "How much can you trust someone you've only known for a day?"
    show mc stressed
    m "I'm just worried I'm making a big mistake."
    show sai sad
    s "That's just your anxiety talking."
    show sai shy
    s "Allow me to reassure you. There are no negative permanent effects, I'll be by your side, and you will be safe. It's even enjoyable if you let yourself relax."
    show sai happy
    s "You can do it!"
    menu:
        "Am I really going to do this?"
        "Eat it.":
            jump eat_gt
        "Refuse.":
            jump refuse_eat_gt

    label refuse_eat_gt:
        "Mother wouldn't approve. You shouldn't give into peer pressure."
        show mc sad
        m "I can't. I'm sorry. It's too much to ask of me."
        show sai surprised
        s "Well, my \"low hopes, high expectations\" mindset certainly paid off right now."
        show mc stressed
        m "I'm sorry. I feel bad..."
        show sai shy
        s "No, it's ok. I don't like pressuring you either."
        s "I just wanted to talk with you more on my level, but if you can't, well that's that."
        show mc confused
        m "On your level?"
        show sai happy
        s "Yes, a higher level, obviously."
        m "Funny."
        show sai worried
        s "..."
        show mc normal
        m "So, what now?"
        show sai normal
        s "I don't know. We could hangout, work, explore, anything, really..."
        m "We've already been out. I usually don't want to do that stuff."
        s "Maybe if you'd eaten me, you'd feel differently."
        #continue this route. What will happen?


    label eat_gt:
        show mc normal
        m "Okay. Tell me what to do."
        show sai normal
        s "Do you still have that finger I gave you yesterday?"
        show mc normal
        m "Uh, yeah."
        show sai happy
        
        s "Okay, then I'd recommend you eat the fingertip. Just a nibble, okay?"
        show mc stressed
        m "Here goes nothing..."
        "Are you SURE?"
        m "(Shut up! I'm not listening to you anymore!)"
        show mc normal
        m "*nibble*"
        show mc vstressed
        m "EUuughgh!"
        show sai vshy
        s "Good things often taste bad."
        show mc shocked
        m "You should have warned me. You're not as sweet as you look."    
        show mc confused
        m "When am going to... feel the effects?"
        show sai happy
        s "Around an hour or so. For now, just enjoy yourself and the sounds of nature."
        show mc worried
        m "That's a little scary."
        s "Don't worry, just let me relax you-"
        show mc annoyed
        m "Don't phrase it like that."
        


    "You."
    "Look at those bags under your eyes. They're so much worse."
    "Your hairline is looking a little lacking. That patch of \"baby hairs\" isn't getting any thicker."
    "How come you have so many new freckles and sunspots despite hermiting indoors?"
    "You've got some creases around your mouth now. Gone are the smooth-skin days of childhood."
    "..."
    "Your hands are wet. The container is overfilling."
    "You turn the taps off. You should go..."
    menu:
        "Look more.":
            jump fight_consciousness
        "Go.":
            jump good_high_route

    label good_high_route:
        #back to bedroom
        show mc sad
        m "Damn I'm getting old."
        show sai surprised
        show mc normalside
        m "Sorry, that was random."
        show sai happy
        s "That's ok. Why are you scared about getting older?"
        show mc normal
        m "It's... *yawn* nothing. Pass me the controller."
        s "Maybe you want to just talk instead?"
        show mc annoyed
        m "Talking? Ew. No, I'd rather just ignore the fact that I'm leaving my prime years."
        show sai shy
        s "And that's scary? Why? What happens when you leave your prime years?"
        m "You get ugly and you lose oppurtunities. Like if I ever wanna model, then you gotta start while you're young."
        s "Interesting! I didn't know you had an interest in modelling."
        show mc happy
        m "Everyone has that dream though, don't they? Wishing someone would scout them, tell them how hot they are and how they want you to work for them."
        m "But that stupid, so let's just play."


    label fight_consciousness:
        show reflection_normal with dissolve
        "Your skin is sagging more."
        "You've got even more burst blood vessels all around your nose and cheeks. Random red dots on your temples. If you ever wanted to model, well, now you can't."
        "Your neck has a deeper crease in the middle from always being on your phone. \"Text-neck\", you'd heard someone online describe it."
        "Your big-ass nose has blackheads all over it."
        "There are more of those weird, white bumps near your eyes. They never seem to go away."
        "Your ears are still too big, no matter how much you grow out your flat, thinning hair."
        show reflection_sad with dissolve
        "Do you see it now that you're so up close?"
        "You're tainted, aging, and..."
        "You're just plain ugly."
        "Get over yourself. You're not as handsome as your mom said."
        "Maybe you were before the late nights and lack of self-care, but now it's too late."
        "Will you ever love yourself again?"
        "Is everything you see really permanent? Is there any fix?"
        "Stop crying. You look so fucking ugly when you cry."
        "See how your face turns bright red? How you frown so deeply? How your mouth creases so unattractively?"
        "You can't bear to see yourself anymore!"
        g "%(player_name)s?"
        scene bathroom with fade
        show mc vshout with easeinbottom 
        m "Don't come in! H-hold on! I'll be right out!"
        show sai surprised at left with easeinbottom
        show mc vshout at right with move
        s "%(player_name)s, you were taking a while, and I got a funny feeling that I should check up on you."
        show mc vstressed
        m "Well, as you can see, I'm fine! Now go!"
        m "You can't be in here! This is the men's bathroom! The {i}men's{/i}!"
        show sai vshy
        s "Let's go back to the bedroom together, okay %(player_name)s?"
        show sai shy
        s "And you don't have to look away. I mind if you're crying."
        "She saw."
        "She saw your pathetic, ugly tears."
        show mc vcry
        m "I'm sorry."
        show sai happy
        s "No need to apologise. You're a little more sensitive right now, and you shouldn't repress your feelings, okay?"
        s "Let yourself feel. Learn what makes you worry, what makes you curious and happy."
        m "Even if you say that, it's still embarrassing."
        show sai vhappy
        s "Don't worry, I promise to show you my tears too. I'm just too happy right now."
        show mc cry
        m "You're happy?"
        s "Also, thank you. I think crying with friends is beautiful. And now I feel like you really do trust me."
        
        show sai happy 
        "Now come, I've got something special to show you."
        "Sai takes your hand and gently leads you back to the bedroom, water in tow."

        play sound "door.wav"
        scene bottle_phone night with Fade(1, 2.0, 1):
            zoom 0.9 
        show sai on left
        show mc stressed on right
        with easeinbottom

        g "Alright, rule number one: don't leave %(player_name)s alone. You'll get up to mischief."
        m "..."
        g "Open your eyes."
        show mc sad
        g "What's on your mind?"
        m "I don't like myself."
        g "Oh my, you really were ruminating."    
        m "Do you like yourself, Sai?"
        g "Yes!"
        m "Just like that? Isn't there something you don't like about yourself?"
        g "I'm always trying my best, so no."
        g "What about you?"
        m "I'm ugly."
        g "No, you're not."
        m "I don't believe you."
        g "You should."
        m "Even without my looks, I feel like my life is spiralling out of control."
        s "Probably because you don't challenge yourself to step out of your comfort zone. Don't you agree?"
        m "I do... It's just hard with other people always there."
        m "I'm oversharing, sorry... You have your own life to worry about."
        s "Contrary to what you may think, I care a lot about you. Talk more."
        m "About what?"
        s "Like, what's your plan? You said you don't like how you are."
        s "You're not planning on staying like this forever, are you?"
        m "You make it sound like I know what I want."
        s "You... don't?"
        m "Well, yeah... How am I? How can anyone?"
        s "I do. I want to do what I want and be happy."
        m "You can't understand. In this society, you have to work to have money and be happy."
        m "And whatever work you choose, you're in it for the rest of your life, otherwise you'll always have a low-paying entry job and never get the house or food you want."
        m "So there's a LOT of incentive to climb the work ladder. You can't do that if you change ladders all the time."
        s "Sounds stupid. So why can't you pick a ladder?"
        s "Why are you waiting to be happy?"
        m "I don't think I want to talk about this."
        s "Why not? I won't tell anyone else. Plus, I'll die soon anyway, so I'm taking it to the grave."
        m "It's not your problem."
        s "I'd like it to be. I care, so... I'm worried, you know? At the garden, and the café."
        s "That's happiness there. Sitting here with you, this is happiness too. You don't have to wait."
        m "..."
        s "Oh, trust me. I won't judge. I'll listen properly, ok?"
        s "So please tell me?"



        # Therapy talk:
        m "I just need to get over it."
        s "Are you planning to ignore it?"
        m "Yeah. I'm just wrong for feeling it. No one else ever talks about it, so... It's just me, right?"
        s "No. Not everyone thinks about it. Only one in ten. Everyone else doesn't mind."
        
        s "One day, you're going to have to actually die. How are you going to be prepared for that, unless you process and accept this feeling?"
        s "You need to cry it out. It's not just a simple thing that's going to happent to us. It's really unfair."
        s "We get one life, and then we die. We lose consciousness forever."
        s "You and I will disappear, like clouds dispearsing into nothing. It's scary."

        #Everyone loves a change story.
        #Have Sai start as 









return



#gift her sugar
# m "Hey... I have a gift for you."
# s "For me? Wow, that's unexpected."
# m "Eh, why not?"
# s "You... um, nevermind. Thank you. What is it?"
# m "So, while we were at the café, I saw something and thought you'd like it."
# m "It's a sweet. My favourite kind of candy: Chocolate."
# m "I think it's like THE most popular flavour on earth, and you really like tasting stuff, so..."
# show sai tearing up
# s "(I never thought I'd get to receive a gift. I'm so happy.)"
# m "...so I thought it'd be nice to share it between us."
# m "(I hope she likes it.)"
# m "Um, so, here."
# "Sai takes the chocolate from your outstretched hands-"
# s "Thank you, %(player_name)s. I love it. I'll have the first bite."
# "- and bites it in the corner. Right. Through. The. Wrapper."
# show mc shocked
# m "No! You have to take off the wrapper first! You can't eat that!"
# s "Pah - tew!~"
# s "Ugh, sorry, I didn't know..."
# m "Haha! Oh, you're so... Just let me break off a piece for you. THIS is how you're supposed to do it!"
# s "Eating is eating. Whether breaking, chewing, licking, or slurping. Every technique should be allowed anytime."
# m "Okay okay! Instead of lecturing me, eat chocolate."
# s "Aaaaah... nom!"
# "Instead of waiting for you to drop it in her mouth, she attacks your hand with her mouth, like a hawk swooping upon unsuspecting prey."
# "The chocolate block disappears from your hands in a blur, faster than your eyes can track!"
# m "Whoa! Sai!"
# "But Sai is too deeply focused on the sweet to hear you at all."
# "Her eyes are closed, her jaw moving silently, her eyebrows high in surprise."
# s "Mmn~!"
# s "Shew derishush!"
# s "%(player_name)s!"
# s "I'm in love."

# if sai_rp > 2:
#     "Those words make your heart stop. But her eyes are not focused on you when she says it. Not you."
# m "With the chocolate?"
# s "It's rich, creamy flavour. And it's... oh, I can't describe it. Also the smooth texture, melting all aaaaahh over your tongue, coating the sides of your mouth thickly~"
# m "Yeah. help yourself."
# if sai_rp > 2:
#     "Jealous of chocolate? How silly."
# s "Ah, so I can eat it faster, thank you!"
# m "Yes, that reason."
# s "Would you like some too?"
# "She holds up a block of chocolate and casually stares at your lips, waiting."
# if sai_rp > 2:
#     "Why are you getting so nervous?"

# m "Aaaah..."
# "Sai leans in closer, still looking intensely at you."
# if sai_rp > 2:
#     m "(Don't look at me like that! It's too embarrassing.)"
# show black with fade
# "So you shut your eyes and wait patiently, mouth open."
# #swap bacto to bedroon
# show mc shocked at right
# show sai normal at left
# "Immediately, you sit up, clutching your throat, choking."
# m "(Can't breathe! I have to cough this out first!)"
# s "Ah, sorry!"
# m "*Choking noises.*"
# s "Oh, what do I {i}do{/i}!? Please don't die!"
# m "(I don't wanna die either! Come on, lungs, let's get this thing out already!"
# "But it's not working."
# "You start to panic."
# "What if you die, for real, right now?"
# "You're supposed to have a few decades to accept it, like everyone else."
# "You're not ready to face death yet."
# "You're too scared of the eternal nothingness."
# "You're not ready."
# "Suddenly, it pops out and splats on the carpet. You're flooded with relief as you breathe fresh air again!"
# "Tremors of panic are still working their way out of you."
# "You feel Death losing His interest on you. He fades from your mind."
# s "Are you okay? Are you okay?"
# m "Y-yeah..."
# s "I'm so sorry."
# m "It's okay. I'm okay. Everythings okay."
# s "You don't look okay."
# "Sai surprises you yet again by hugging you hard."
# "So comforting and warm. How long has it been since you've last been hugged?"
# s "I was really scared you were going to die. I'm so glad you're safe. I'll be more careful."
# scene black with fade
# sai_rp += 10
# "You and Sai bonded a bit over a near-death chocolate incident."
# "After recovering from the shock, you take your revenge on the chocolate and finish it up while playing tetris."
# "Swapping the controller and the chocolate, backseat driving and tensely investing yourself in your friend's gameplay..."
# "After nearly dying, you realise that you've been taking moments like this for granted."

# "Hours pass."
# #scene early morning bg
# s "Hey, shouldn't you go to bed already?"
# m "Probably. I feel tired, but also wide awake."
# m "Stupid heart won't calm down. My brain's too awake."
# s "..."
# s "Are you too scared?"
# m "Ha. Yeaop."
# s "Haha. That's a funny word."
# m "Sorry, I'm stupid tired right now, but it's like my heart won't calm down."
# s "You should try lie down and meditate. "
# m "Eh..."
# s "Or I could sing for you."
# m "Huh? Really?"
# s "You'd like that?"
# m "No one's offered to sing for me before. And, I've never heard you sing."
# "Unfinished ----------" 
# return



# "Suddenly, you are awake, blinking with crusty eyelids."
# "An unrecognisable version of your bedroom is before you. That peace was just a dream. You're alive. Your problems are still there waiting for you to deal with them."
# "Heavy thoughts stack one upon the other like bricks."
# "The sports club you've been ditching is meeting today. Would it be awkward if you came in? No, you shouldn't do that."
# "The bank needs you to come in. Else they'll keep phoning you! But they're so scary, and you don't understand that bank stuff anyway. You should wait until vacation, so your mom can come with."
# "That photography competition! You have the camera, and the desire, but you still can't get the pictures looking right. There's no point even competing."
# ""
# day job. His night job.





#         stop music fadeout 2
#         window hide
#         scene black with fade
#         show text "Everyone wants something from you. Pulling pieces off of you like vines of viscera from your stomach."
#         $ renpy.pause ()
#         show text "It hurts so much. They're taking all of you. You just want something for yourself. But everytime you think you're about to have some slack-!"
#         $ renpy.pause ()
#         show text "Again! Again! It never ends! There's nothing left over."
#         $ renpy.pause ()
#         show text "They get your energy. You just get the sad, tired vessel that remains."
#         $ renpy.pause ()
#         hide text with dissolve
#         scene bottle_phone night with Fade(1, 2.0, 1):
#             zoom 0.9
#         play music "night.mp3"
#         show mc vstressed at right
#         show sai sad at left
#         with easeinbottom
        
#         $ sai_rp -= 10
#         show mc stressed
#         m "Oh my God... this is becoming {sc=3}{color=#000000} too much{/sc}{/color} for me. I can't do this."
#         show sai surprised
#         s "What? What's wrong?"
#         show mc worried
#         m "I'm sorry you're stuck with me. Maybe I'm not cut out for this."
#         m "I'm so overloaded. I physically can't make any decisions anymore. I'm empty."
#         show mc sad
#         m "I'm sorry, Sai. I'm useless right now."
#         s "..."
#         show sai sad
#         s "This feeling is strange. I can sense your pain. Your genuine sadness."
#         s "What is the point of saying such cruel words against yourself?"
#         show sai worried
#         s "You don't need to be useful, okay?"
#         m "But, I have to get up and help you walk around."
#         show sai happy
#         s "Don't worry about that right now. Just close your eyes. Take your much deserved rest. You've done well today."

#         window hide
#         scene black with fade
#         stop music fadeout(3)
#         show chibi_sleep at truecenter with Dissolve(2)
#         show top_text "You shut your eyes, count some sheep, and..." with dissolve
#         pause(2)
#         show chibi_awake at truecenter
#         show top_text "... and it does shit all." with dissolve
#         pause 2
#         show top_text "Your heart is beating to fast. You can't relax." with dissolve
#         pause 2
#         show top_text "All you can think about is The Future." with dissolve
#         pause 2
#         scene bottle_phone night with Fade(1, 2.0, 1):
#             zoom 0.9
#         play music "night.mp3"
#         show mc normal at center
#         with easeinbottom
#         window show
#         m "What's the time? No, maybe I shouldn't... else I'll know how tired to be tomorrow."
#         m "But, maybe it's earlier than I think. It is past midnight? Then at least-"
#         show mc stressed
#         m "4 AM? Oh my God. I'm fucked."
#         show mc sad
#         m "Why aren't I sleepy? I was so tired, and then as soon as I tried to relax..."
#         "Then you started thinking about yourself."
#         show mc normal
#         m "(I panicked too much today. I need to learn to take some breaths... I couldn't enjoy my day because of how overwhelmed I was...)"
#         show mc normalside
#         m "(But, it's also been a while since I've been out. It's okay to make mistakes!)"
#         "I have a feeling you won't manage to change. You're too afraid."
#         show mc normal
#         m "Yeah."
#         "You started getting hopeful when you went out today. You thought this was the oppurtunity that would finally fix you."
#         "Well, you messed it up."
#         "You should stop holding onto that hope soon, because it'll hurt when it shatters in your hands."
#         show mc stressed
#         m "(Ugh, get out of my head already. This is all your fault. Why won't you let me go to sleep?)"
#         "Why? Because everything is going to fail. And you haven't done anything to change its destiny."
#         "This instinctual, never-ending panic is here because its well deserved. You're not doing life correctly. Fix it."
#         "FIX IT! DO EVERYTHING! ELSE YOU'LL DIE WITH REGRETS!"
#         show mc stressed at right with move
#         show sai surprised at left with easeinbottom
#         s "Umm... sorry to interject, but... what's happening?"
#         s "Is there someone else here I can't see?"
#         show mc surprised
#         s "Ah... Sai..."
#         show mc worried
#         m "Sorry, I was just talking to myself."
#         show sai happy
#         s "Oh. An interesting concept. May I join?"
#         m "What? No. Look, sorry about the noise and disturbing you and all-"
#         m "Wait. Where did you just come from?"
#         show sai worried
#         s "Um..."
#         m "Because you weren't here a few moments ago."
#         s "Now it's my turn to apologise... I'm sorry but I went out for a bit."
#         m "Oh no, did anything happen?"
#         s "No, nothing."
#         s "Everythign was okay, and I saw something wonderful too. These white tiny glowing lights. I can't even tell where they start."
#         s "But there are so many of them! And the night air smelled amazing too-"
#         m "Ohh... you found the rooftop."


    





      






    # m "..."
    # m "You look really happy for someone who doesn't have much time left."
    # show sai surprised
    # s "I look happy because I AM happy."
    # show sai happy
    # s "Today was magical. I experienced new sensations and feelings, and I even have something wonderful to look forward to tomorrow."
    # show sai vhappy
    # s "Why would I spoil that with worrying about something that's gonna happen anyway?"
    # show mc normalside
    # m "So you can just not think about it? Lucky."
    # show sai normal
    # s "Its more that I honestly don't care about it."
    # show mc surprised
    # m "Really?"
    # show sai happy
    # s "Truly. I don't care that my time alive is finite. Before this, I couldn't do anything. But now, I can do anything."
    # show sai vvhappy
    # s "I love it."
    # show mc stressed
    # m "I'm jealous. I wish I could not care either. I'd probably enjoy life more if I could."
    # show sai shy
    # s "I'm not oblivious. I know it's hard."



label sai_day_3_worms:

    s "Ah, you're awake! Not to alarm you, but..."
    show mc normal at right
    with easeinbottom
    s "It appears my body has attracted some residents."
    show mc surprised
    show sai worm at left with easeinbottom
    m "..."
    show mc vshocked
    m "Wait, are those... {i}worms{/i}?"
    s "I think they are the larvae of some kind of fly."
    s "So, maggots."
    show mc shocked
    m "Oh my god oh my god oh my god! WHYYYYYY!?"
    show sai shy
    s "Don't worry! It doesn't hurt."
    s "As for why, I believe they were attracted to the smell of rotten food."
    show sai happy
    s "Honestly, ignoring how it may look to others, it feels quite nice to home such small, cute creatures."
    show mc worried
    m "But they're maggots!"
    show sai determined
    s "Yes, and I am quite fond of them! They clean and aerate the soil. Very important to the ecosystem."
    show mc stressed
    m "Oh my God! I should've just cleaned you yesterday."
    show mc cry
    "I'm so sorry, this is all my fault!"
    show sai shy
    s "Please, don't cry, %(player_name)s."
    s "Nature is just... reclaiming me."
    m "But Sai, how can you be so calm? They are eating you inside out, aren't they? That's what maggots do!"
    show sai vshy
    s "It does tickle, yes."
    show mc vstressed
    m "No! They're eating you alive! Sai, you're going to decompose..."
    m "You're going to die..."
    show sai normal
    s "I know. However, before they kill me, I will die."
    show mc confused
    m "Uh... what?"
    show sai vshy
    s "The truth is, I knew from the beginning that mushrooms lived short lives. It never bothered me."
    show sai worried
    s "But I kept that fact from you. I'm sorry for that."
    show mc sad
    m "It's okay. None of that matters anymore."
    show sai happy
    s "At least this way, these worms can live within me, and I can die knowing I contributed to something."
    show mc stressed
    m "You already had."
    show sai normal
    s "May I make a final request?"
    s "Would you join me until the end?"
    show mc normal
    m "Yes."
    show sai vhappy
    s "Thank you."
    s "I would like to go somewhere where there are plants."
    show mc confused
    m "Outside again? That's all you've done for the last few days... Don't you want to do something more interesting with your last day? I can show you movies or go ice skating-"
    show sai shy
    s "I hope you won't take offence, but I feel most at home surrounded by mother nature."
    s "Human inventions and establishments are fascinating, but what I want is tranquility, not entertainment, in my final moments."
    show mc stressed
    m "I understand."
    show sai happy
    s "Please, don't look so forlorn. I am at peace, especially with you at my side."
    show mc sad
    m "I just wish I could have spent more time with you."
    s "Don't worry. We will make the most of the day."
    show sai surprised
    s "Ah, could we perhaps eat more food as well? I do love it so much."
    show mc annoyed
    m "Of course you would want to eat until the very end."
    show mc happy
    m "Yeah, we can have a picnic. It's not like there's any reason to hold back anymore."
    window hide
    stop music fadeout 3
    hide mc
    hide sai
    with easeoutbottom


    scene black with fade
    play music "date.wav"
    show chibi_mc at slightright
    show chibi_sai at slightleft
    with easeinright

    "Don't let yourself think too hard about what's coming."
    "Don't think about what's happening inside of Sai right now."
    "Don't think about the larvae eating through her flesh and the flied laying their eggs in her."
    "You just try to pretend like it's any other kind of day."

    hide chibi_mc
    hide chibi_sai
    with easeoutleft
    
    scene sunset with fade

    show sai vhappy at left   
    show mc normal at right
    with easeinbottom
    s "Ah, tranquility... this spot is perfect."
    s "And thank you for the diverse array of food items. I look forward to trying them all."
    show mc confused
    m "I don't get it. Why do you like food so much? You don't even need to eat."
    show sai shy
    s "Why? I hope you're not disappointed by my answer, but it simply makes me happy."
    s "For instance, when I try this..."
    show mc annoyed
    m "Those are called \"Chips\"."
    show sai eatdown
    s "When I try these chips-"
    show sai eatvhappy
    s "My head feels like it's dancing in the sky..."
    s "My mouth feels like it's exploding with laughter..."
    s "And my body feels like it's being hit with lightning."
    show sai happy
    s "Er, lightning that feels good, that is."

    show sai vshy
    s "Eating is a full body experience for me. I just love it, and I've already been fascinated by the idea of it."
    show sai vhappy
    s "Maybe my mushroom brain just confused \"being eaten\" with \"eating\"."
    show sai happy
    s "Though in the end, I obtained both! A true glutton!"
    show mc sad

    m "Sai, I just wanted to say..."
    m "Thank you for looking after me these past few days."
    show sai surprised
    s "Me? I did?"
    show mc stressed
    m "Yeah."
    show mc cute
    m "I forgot how nice it can be. Going out. Having someone I could talk to. Making jokes again."
    m "I was looking forward to the future again."
    show mc happy
    m "Haha... Stuff like this always happens to me. The minute I start feeling happy..."
    show sai sad
    s "%(player_name)s..."
    show mc sad
    m "What do I even do when you're gone?"
    show sai happy
    s "Just leave me. Go home."
    m "And the next day?"
    s "Whatever you want to do."
    show mc stressed
    m "You want me to pretend it never happened? Just do what I want?"
    show sai shy
    s "You say \"just\" as if it is a simple task, but you are not good at it, %(player_name)s."
    s "All I want... is for you to be a friend to yourself, as we were to each other."
    show sai vvhappy
    s "Please, love yourself. I promise you that you are wonderful."

    m "I'll try..."
    stop music fadeout 2
    play sound "windchimes.wav"
    show sai vhappy
    s "Ah, the wind feels so warm and nice~ I can almost taste the flowers in the air."
    s "And the sunlit grass looks so soft..."
    s "I must lie down now."
    stop sound fadeout 3
    stop music fadeout 3
    window hide
    hide sai
    hide mc
    with dissolve

    scene sai_dead_1 with fade
    play music "date_musicbox.mp3" fadein(3)
    pause 2
    
    window show
    s "I never imagined how lovely I could feel."
    s "My chest feels so light."
    "Sai took in a deep, deep breath of air."
    "And as she did..."
    window hide
    play sound "windgust.wav"
    show sai_dead_2 with dissolve

    pause 3
    stop sound fadeout 3
    scene white with fade
    stop music fadeout 2
    $ persistent.send5 = True    
    "End 5: One last sai-m, I'm gonna celebrate."
    


            #return home



# Angsty writing

# s "..."
# m "What's wrong, Sai?"
# s "..."
# m "Won't you talk? At all?"
# s "There's no point."
# s "I don't even exist."
# s "Neither do you."
# s "Nothing is real."
# s "..."
# m "It is real. We have real lives here. Billions of people are living their own microlives."
# m "Don't stagnate. Don't... throw your life away."
# s "I'm not throwing my life away. I'm not suicidal. I'm just not going to be present."
# s "It'll be over before I know it."
# s "I'll go back..."
# s "..."
# m "Sai-"
# s "I don't have a name. I don't exist, so how could I?"
# m "You're being stupid! Why are you so careless suddenly? What happened to the curious Sai I met?"
# s "I don't know."
# s "All I know, is that I hate the pain. And pain doesn't exist, if feelings don't exist."
# s "And feelings don't exist when I don't care."
# s "This life is a lie. The experiences will disapear whether I have them or not."
# m "What about the butterfly effect? Things you do, affects others, lasting long after you're gone."
# s "Everyone will disappear when I die. Including you."
# s "You'll all be forgotten, forever. You're all a stage of performances, and when I die, you'll never play again."
# m "From your perspective."
# s "My perspective is the only one that matters."
# m "Not to me."
# s "Ah, but your perspective, from my perspective, will also vanish. So ultimately, I'm still correct."
# m "..."
# m "I don't think I can get you to understand."
# s "Same here."
# m "I'm sorry for failing you."
# s "You should go. The longer you try to talk to me, the worse you'll feel."
# s "Just go."

#Angsty writing 2
# s "I don't understand talking. Communication is supposed to be simple. I'm supposed to be able to exchange ideas to someone."
# s "I'm always messing it up! What is it I don't get? I'm just making a fool of myself."
# s "It's better when I never talk at all! At least if I'm silent, I can't offend anyone."
# s "Yes... I'm just going to stop talking forever."
# s "And then I'll never fuck it up again."

#Angsty writing 3





# Well scene:
s "Hmm... it looks dark."
m "Yeah. Getting stuck down there would be a nightmare to escape. There's basically no way unless you call for help."
m "Honestly, I'd rather die, haha..."
show sai surprised
s "You'd choose death, over rescue? That's a rather severe preference!"
show mc annoyed
m "Just imagining calling out, waiting for someone to hear me, being a problem... yeah, I think I'd die from embarrassment."
"You'd hate the sound of your own voice. You'd probably sound so stupid, screaming out loud for help."
show sai normal
s "I doubt anyone would mind helping a fellow human in trouble."
m "No, no. I'd rather die."
show sai sad
s "..."
show sai determinedclosed
s "Forgive me, player. Please do not consider this a betrayal, but an opportunity!"
s "*shove*"
show mc shocked
hide mc with dissolve
m "AAAAAAAaaaaahhh!"
scene black with dissolve
scene well with dissolve
""
show mc stressed
m "Ow..."
show mc shocked
m "You... you pushed me into the WELL!?"
m "How could you!? Why!?"
"You frantically search for a ladder, a rope, an outcropping of some bricks or SOME MEANS OF ESCAPE."
show mc vshocked
m "Smooth concrete. Oh my God. I'm stuck!"
m "Why the hell did you push me down here!? I trusted you!"
s "Worry not! I shan't abandon you. Here I cooooooooooooome!"
show mc shocked
m "Wait! No! Don't jump!-"
show sai happy at left with easeinbottom
show mc at right with move
m "Now we're BOTH stuck! How the hell am I getting out of here? We're trapped! Oh my God, this is a nightmare!"
s "Thankfully, there is a solution. Simply call for help and we will be saved."
show mc normal
m "..."
show mc normalsquint
m "Was it because of what I said? That was your point? This is so stupid... I'm not doing this. You can't just force me to do something like that."
show sai normal
s "Then stay here and die."
m "No. YOU got us into this mess, so you have to call for help, not me."
show sai determined
s "I'm afraid you must overcome this trial by your own merit. I refuse to help you."
show mc confused
m "But why did YOU come down here!? You're stuck too now!"
show sai normal
s "In the case you choose to perish, I shall join you. I believe I should only do to others what I am willing to have done upon myself."
show mc stressed
m "(This is so stupid!)"
show mc normalside
m "No. I'm not screaming."
show sai happy
s "Then we will die together. That is quite a romantic notion."
show mc confused
"You'd expect her to be annoyed at you for not being good enough, for wasting her time, for being weak..."
"But in the dim light, Sai smiles at you brightly, as if there's not a trouble in her mind. She seems resolved to simply wait patiently..."
"Resisting the desire to throttle that annoyingly sweet grin off her face, you groan frustratedly out loud."
show mc sigh
m "This is so stupid! What a waste of time! Your OWN time! And do you have to stare at me?"
s "No."
show mc normalside
m "(I've gotta be more literal.)"
show mc normal
m "..."
show mc slightsad
m "Please... stop staring at me. I can't calm down otherwise."
s "Understood."
show sai at flip
"She turns around and faces the blank, in stimulating wall. Now you feel guilty, but at least that you know how to live with."
hide sai
hide mc with dissolve
"Time passes. You hope someone will walk past and spot you. You stand, leaning tiredly from one hip to the other, ready to wave if someone looks in. Your neck hurts from looking up."
na "(small size) mumble mumble."
m "(Someone's here!)"
"But you hesitate. You're scared to call out loud and hear your own, wimpy voice echo around you, drawing attention."
show mc embarrassed at right with dissolve
m "H-hello?"
show sai normal at left with dissolve
s "You'll have to be louder than that, player."
m "..."
show mc sad
m "Please, can you do it?"
s "Why?"
show mc slghtsad
m "I'm... scared... to ask for help."
show sai determinedclosed
s "Illogically so. You are weak by choice, player. You can do it, if you choose, or not, if you prefer."
show mc confused
m "It's not a preference. I want to do it. But..."
show mc stressed
"But you feel ashamed."
m "..."
hide sai
hide mc
with dissolve
"The voices disappear. You hang your head and sigh tiredly. Your body hurts, you're hungry, you're annoyed and uncomfortable."
"You sit down so that your pants get wet and you can feel even worse."
"Everything is horrible. It isn't fair. Poor you. Give up and die and everyone will feel bad for you."
"Sai joins you. You're too dispirited to shrug her off when she puts her hand on your arm."
"You expect her to follow up the action with some kind of optimistic, reassuring pep-talk. Instead, you both sit in the echoing, dark silence, with a small heat radiating between your bodies."
show mc slightsad at right
with dissolve
m "I'm sorry I'm wasting your time when you don't have much."
show sai normal at left
with dissolve
s "Have you decided to die then?"
m "..."
"Maybe you {i}should{/i}just die."
show mc stressed
m "(I can't. I'm not ready.)"
"Right now, more than the fear of annoying someone to help you, you feel an intense, annoyed yearning..."
"...to get out this God damn well!"
show mc vstressed
m "(But I really don't want to burden someone with helping me. All the attention...)"
show mc stressed
m "(No. I know I have to do it. And if that's the case, the sooner, the better! I'm done pitying myself!)"
m "Fuck this! Okay okay okay! I'M DOING THIS!"
"You jump to your feet, and start screaming before you have a chance to back out:"
show mc shout
m "HEEEEELP! HEEEEEEEEEEELP! I'M STUCK IN THE WELL! PLEASE HELP MEEEEE!"
m "ANYONE! PLEASE! I NEED HELP! WE'RE TRAAAAPPED!"
show sai shocked
s "HEEELP UUUUUUS!"
show mc surprised
m "I thought you wouldn't help!"
show sai vvhappy
s "You did the part that mattered. Now, we scream for life together!"
"Beaming, Sai grabs your hand, lifts it up high, and resumes shouting. Unlike your urgent shouting, she sounds like she's enjoying it!"
show sai excited
s "SAAAAAVE UUUUUS! WE REQUIRE URGENT ASSISTANCE OR WE SHALL PERIIIIIISH!"
show mc annoyed
m "WE'RE STUCK! ANYONE PLEASE HEEELP!"
na "Whoa! Are you guys actually stuck down there?"
show mc shocked
m "YES! We fell down! Can you please help us?"
na "I'll get a ladder or something, so just hang tight!"

scene garden
show kellin shadow at left
show mc embarrassed at right
with easeinbottom
m "C-can I give you some money? You really helped us out."
na "I appreciate the offer, but keep your cash, get home safe and order yourself some takeout or something."
show mc cute
m "Thank you so much."
hide mc 
show sai happy at right
show sai at flip
with dissolve
s "Thank you for saving us, fellow human."
na "Haha, it was kinda fun. How'd you guys end up down there anyway?"
s "I pushed him."
na "Whoa... I'm clumsy so, so I get it, but try to be more careful next time."
na "Anyway, I'm late for dinner. Stay safe."
hide kellin shadow
hide sai
with dissolve
"He walks away. Now, you turn to Sai."
show mc sigh at right
show sai happy at left
with dissolve 
m "That was crazy... I still can't believe you did something so reckless."
m "(In retrospect, it was a tiny bit fun. Though I'll never admit that.)"
show sai worried
s "Player..."
show mc normalside
m "What? Going to finally apologise?"
show sai vblush
s "You're... so... beautiful!"
show mc vshocked
m "!?"
show sai vshy
s "I thought you were a recluse who saw no hope for the future. Like a dead log with no hope of growing again. Like a piece of trash on your room only hoping for decay."
show mc stressed
m "(Ouch.)"
show sai surprised
s "You look pained, even though I complimented you."
show mc surprised
m "(That was a compliment?)"
show sai shy
s "I would have gladly died with you. It would have been quite romantic. Enshrouded in a column of darkness, our forms degrading together into a pool of organic sludge-"
show sai vvhappy
s "But this is far better! Your desire to live has quite inspired me, player."
s "I'm quite curious! What will you do now?"
show mc confused
m "Er... why should I do anything?"
show sai happy
s "You wished to live for a reason, didn't you? Else, you would not have overcome your intense discomfort of social interaction."
s "Surely some sense of unfulfillment was driving you. So, what did you want to do so badly that you didn't want to die?"
show mc normalside
"Was there a reason like that through your mind?"
show mc normal
m "I just didn't want to die. Is that so hard to understand?"
show sai sigh
s "What a disappointing answer."
show sai normal
s "Please think about it for a minute, player. Recall your passion for survival you felt. What do you want to do?"
show mc 
m "I just want to live. Do more things. See stuff."
show sai excited
s "Oh! Wonderful!"
show mc normalside
m "Calling for help wasn't as bad as I thought it would be. It was kinda easy actually. Starting was the hardest part."
show sai happy
s "Very good! I'm happy to have been able to teach you that leaning on your peers is a beautiful thing that deserves no shame."
show mc normalsquint
m "Just because it worked out this time doesn't mean you should do this again. Your teaching methods are too extreme."
m "Agh... I'm wet, I'm tired, I feel like a piece of shit. I want to go home already."
s "Me too. Let us journey back to your habitat."
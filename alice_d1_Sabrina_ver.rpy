# Inject some vibe that she's looking down on you. Feel a little more superficial.
# Gives you a lot of compliments

label alice_d1_Sabrina_ver:
    
    default alice_rp = 0
    default alice_reject = 0

    image alice_affection = ConditionSwitch(
    "alice_rp >= 50", "sprites/affection/affection max.png",
    "alice_rp >= 40", "sprites/affection/affection almost_max.png",
    "alice_rp >= 30", "sprites/affection/affection mid_good.png",
    "alice_rp >= 20", "sprites/affection/affection min_good.png",
    "alice_rp >= 10", "sprites/affection/affection almost_good.png",
    "alice_rp == 0", "sprites/affection/affection mid.png",
    "alice_rp >=-10 ", "sprites/affection/affection almost_bad.png",
    "alice_rp >=-20 ", "sprites/affection/affection min_bad.png",
    "alice_rp >=-20 ", "sprites/affection/affection mid_bad.png",
    "alice_rp >= -30", "sprites/affection/affection almost_min.png",
    "alice_rp >= -50", "sprites/affection/affection min.png",    
    "True", "sprites/affection/affection mid.png")   

    
    stop music fadeout(2)
    scene black with fade
    show text "Four weeks of spraying later..."
    pause
    hide text with dissolve
    scene day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show bottle
    show kit_bursting
    with Dissolve(2)

    play sound "phonealarm.ogg"
    pause 0.5
    m "Shut uuuuuup..."
    stop music
    m "Ugh... Go away, morning... it's sleepy time."
    "Skipping class again? I'm so disappointed in you."
    m "No.... don't wanna... I'm too tired and sad."
    "And so the cycle continues. Honestly, if you're going to get annoyed at it every morning, why don't you just turn off the alarm?"
    m "In case tomorrow I'm different."
    "How? Are you hoping someone else will occupy your body and live it properly for you? I wouldn't be so optimistic."
    m "Maybe tomorrow I'll live properly..."
    "Always tomorrow, never today. Maybe you should give up. Though you'll probably procrastinate that too."
    m "*muffled pillow screaming*"
    window hide
    show mc stressed with easeinbottom
    window show
    m "(Of course. The instant I wake up, the thoughts won't stop.)"
    show mc normal 
    m "May as well get the mushroom-box spray of the day over with."
    show mc at right with move
    m "Alright, come here bottle-chan."
    show mc confused at bounce
    m "..."
    show mc surprised
    m "Whoa... Uh... Was this box always so engorged?"
    na "{size=-8}Rude.{size=+8}"
    m "..."
    show mc awed
    m "D... did it just... speak?"
    na "{size=-8}Yes, {i}it did{/i}."
    show mc shocked
    m "!"
    na "{size=-8}As much as I {i}love{/i} waiting for you to rescue me, I've about reached my limit."
    na "{size=-8}So excuse me while I just-"

    window hide         
    scene alice_box_1 with dissolve
    stop sound 
    play sound "ballon.wav"
    #pause 3
    $ renpy.pause(1.0, hard=True)
    show alice_box_2
    $ renpy.pause(1.0, hard=True)
    show alice_box_3
    $ renpy.pause(1.0, hard=True)
    stop sound 
    play sound "pop.ogg"  
    show alice_box_4
    #pause 2
    $ renpy.pause(2.0, hard=True)
    pause
    scene black with fade
    scene day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show bottle
    with Dissolve(2)

    show day_1 at topleft
    with dissolve
    #play music "wakabayashi.mp3"
    play music "normal.mp3" fadein(2)

    show mc shocked at right
    show alice_base_buns at left
    show dress polkadot at left
    show alice sly smile at left
    with easeinbottom
    show alice hime
    na "{size=+20}OHOHOHO~!"
    na "As you can see, I have finally COME."
    show alice sly smile
    na "I'm sure you have been anticipating this moment, edging yourself to my ultimate arrival."
    m "..."
    show alice cruel
    na "Hmph! I know I'm stunning, but this far exceeds my expectations."
    na "Don't be so shy, Master. I give you permission to speak."
    show alice sly smile
    na "Go on~ Greet me with me the true passion of your heart. Don't hold yourself back!"
    show mc vshout at bounce
    show alice surprised
    stop music
    m "{sc=3}{size=+40}{color=#000000}WHAT THE FUCK!?" with sshake
    m "{sc=3}{size=+40}{color=#000000}WHO ARE YOU!?\nWHAT JUST HAPPENED!?"

    show alice disappointed
    na "Excuse me? Is that any way to talk to a lady?"
    show alice smirk
    na "Perhaps you need me to teach you some manners?"
    show mc shout
    m "No! I need you to explain what's happening right now!"
    show alice normalside
    na "Ah, I'm parched."
    show mc shocked
    m "Are you listening to me?"
    show alice neutral
    na "Are {i}you{/i} listening to {i}me{/i}? I'm parched."
    show mc confused
    m "Huh?"
    show alice vannoyed
    na "*Sigh* Typical. Looks like I'll have to satisfy my own needs."
    $ watered = 0
    show water_status at topright with dissolve
    
    play sound "spray.wav"
    $ watered = 1
    pause 1
    queue sound "spray.wav"
    $ watered = 2
    hide water_status with dissolve
    show alice smug
    play music "normal.mp3"
    na "E-hem- ehem - Ah, much better."
    show alice normal
    show mc worried
    m "(What the hell is happening!? Did she just climb out of the mushroom box? Did I miss the part where she climbed through the window?)"
    show alice sulk
    a "Ick, there's still soil stuck to my dress."
    show mc stressed
    m "(Nope. She came out the box.)"
    show mc confused
    m "(And she looks like that spotted mushroom I was getting. So is she-?)"
    show alice normal
    na "Hmm. You seem more than just pleasantly surprised to see me. You {i}were{/i} expecting me, weren't you?"
    show mc worried
    m "Uh... n-n-no."
    show alice surprised
    na "Did you just stutter?"
    show mc surprised
    m "..."
    show alice disappointed
    na "Why? Do I intimidate you or something?"
    show mc stressed
    m "..."
    show alice sly smile
    na "Hmmmmm?"
    show mc vstressed
    m "..."
    show alice laugh
    na "I totally do! Ohohoho!"
    show alice smug
    na "Ah, I was wondering what kind of person my Master would be. If he was strong, or violent, or grouchy."
    na "I could have never expected {i}this{/i}. You're a complete pushover."
    show mc worried
    "She's right! You are!"
    show alice cruel
    na "Ah, but don't worry, darling. Weak-willed boys are fun too."
    na "Let's start small, okay? I hope you can manage a simple introduction."
    show alice smirk
    a "My name is Alice, understand? Say it."
    show mc surprised
    m "A-Alice."
    show alice flirt
    a "Mhm, that's right~ Good job! Have a reward."
    "Alice reaches her hand towards your face."
    show mc shocked at bounce
    m "W-w-what are you doing?"
    show alice pout
    a "Don't you avoid my headpat. If I've decided you're getting one, you sit still like a good boy and receive it."
    show alice disgusted
    a "GOT IT!?"
    show mc surprised
    m "AH! Got it!"
    show alice happy
    a "Mhm~ *pat pat* There we go. Doesn't that feel nice?"
    show mc stressed
    m "(Why am I enduring this!? I'm losing control of the situation! I have to stand up for myself!)"
    show mc normalside
    m "(Although, this isn't that bad... Her hands are surprisingly gentle. Honestly, it's kinda-)"
    show alice disappointed
    a "Hey. I asked you a question. Don't make me repeat myself."
    show mc surprised
    m "I-It's nice!"
    show alice happy
    a "Good boy! See? Everything is good when you listen to Alice."
    show mc stressed
    "You failed."
    show alice sly smile
    a "Next step. Tell me: what is your name?"
    show mc confused
    m "I'm... uh..."
    show mc vstressed

    jump alicename


    label alicename:                
        $ player_name = renpy.input("What's my name again!?", length = 8)
        $ player_name = player_name.strip()
        $ player_case_insensitive = player_name.lower()
        if player_case_insensitive == "alice":
            show mc normal
            m "...%(player_name)s."
            a "Try again."
            show mc stressed
            jump alicename
                
        elif player_name == "":
            "What? Can't even think of a name by yourself?"
            "You really are hopeless."
            "Fine, I'll make one up for you. Let's go with your dead family fish."
            $ player_name="Finn"
            $ playername = player_name
            m "Uh, I'm %(player_name)s."
        
        else:
            $ playername = player_name
            m "Uh, I'm %(player_name)s."
        
        

    a "%(player_name)s? Ha, adorable."
    show mc stressed
    m "Um... Alice? May I ask you something?"
    show alice surprised
    a "Oh my! Asking for permission already? You learn fast."
    show alice smug
    a "Yes, go ahead. Ask your cute, insignificant little question."
    show mc worried
    m "Um... just to confirm. Are you a mushroom? You're not a human?"
    show alice sly smile
    a "Mhm. Pure mushroom. There's not a bone in my body."
    show alice wink
    a "Unless you want to put one there."
    show mc vblushside
    m "Aaaaaa..."
    show mc vstressed
    m "(I can't handle all these innuendos! I'M NOT USED TO THIS!!!)"
    show mc confused
    m "So you're a real, talking, sentient, woman mushroom?"
    show alice neutral
    a "And you like repeating the same questions."
    show mc surprised
    m "But how did this happen!? You were supposed to be a normal mushroom. I was going to eat you-!"
    show alice smirk
    a "Oh, you still can."
    show alice flirt
    a "In fact, you could nibble a certain place right now-"
    show alice surprised
    show mc vstressed
    m "GAH! This... This doesn't make sense! I ordered normal mushrooms! But you're not-"
    show alice confused
    a "\"Normal\"?"
    show alice laugh
    a "Oh honey, normal would be so boring! Why would you ever want that?"
    "Are you CERTAIN you know what you even ordered? Suddenly, you're starting to doubt yourself."
    show mc surprised
    show alice happy
    m "(I mean, I did check it, didn't I?)"
    m "(I didn't just buy something without looking at it properly, right? That would be completely irresponsible!)"
    "Yes, that would be VERY uncharacteristic of you."
    show mc worried
    m "S-sorry, Alice. Please excuse me. I need to check what I ordered."
    show alice vannoyed
    a "Fine. I'll permit a quick break, since you asked so politely in that trembling voice of yours."
    show alice sly smile
    a "But when I call for you, little one, I expect you to answer."
    show alice disgusted
    show mc shocked at bounce
    a "Understand?"
    show mc stressed
    m "Y-yes, Alice!"
    show alice happy
    a "Good!"
    window hide
    hide mc
    hide alice
    hide alice_base_buns
    hide dress polkadot
    with easeoutbottom

    call screen alice_d1_checkpc_1 with dissolve

    screen alice_d1_checkpc_1:
        imagebutton:
            idle "pc/pc_hover.png" hover "pc/pc_click.png" focus_mask True
            action Jump("alice_d1_checkpc_2")


    label alice_d1_checkpc_2:
        play sound "<from 0 to 1>type.wav"
        scene website2 with dissolve
        window show
        show mc confused with easeinbottom
        m "This is the site. Maybe the \"About\" page will have more info about Alice?"
    
        show alice_base_buns at left
        show alice normal at left
        show dress polkadot at left
        with easeinbottom
        a "So this.... thing.... has information about me?"
        show mc surprised at right with move
        m "What are you doing here?"
        show alice neutral
        a "If you're going to discover my origins, do you honestly expect me not to participate?"
        show mc stressed
        m "(When she puts it like that, she's right. I'd do the same in her shoes.)"
        show mc normalside
        m "Yeah, I can understand that."
        window hide
        hide mc
        hide alice
        hide dress
        hide alice_base_buns
        with easeoutbottom

        call screen alice_d1_checkpc_3 with dissolve
        screen alice_d1_checkpc_3:
            imagebutton:
                xanchor 0.5 yanchor 0.5 xpos 0.8125 ypos 0.120 idle "website/about_idle.png" hover "website/about_hover.png"
                action Jump("alice_d1_checkpc_4")
        label alice_d1_checkpc_4:
            window hide
            scene website_about with dissolve
        pause
        
        show mc confused at right with easeinbottom 
        window show
        m "..."
        show mc shocked
        m "{sc=3}{color=#000000}WHAT THE HELL????\nWHAT KINDA MESSED UP WEBSITE IS THIS?"
        window hide
        show alice_base_buns at left
        show alice cute at left
        show dress polkadot at left

        with easeinbottom
        window show
        a "Sound interesting. What's it say?"
        show mc worried
        m "Are you sure you-"
        show mc confused
        m "Wait, you mean... you can't read?"
        show alice disappointed
        a "Unfortunately, this is one of those rare situations where I depend on you."
        show alice smirk
        a "So don't disappoint me, okay?"
        show mc stressed
        m "Ugh, okay. It says you're something called a..."
        show mc confused
        m "Fly A-ma-ni-ta."
        show alice normal
        a "I knew that already. Give me something more substantial, if you can."
        show mc surprised
        m "You did? How?"
        show alice sly smile
        a "My body just knows it."
        show mc confused
        m "Okay, um, moving on... it basically just says stuff like..."
        show mc blushside
        m "...they're selling mushroom girls... to eat and... be intimate with."
        m "And that you're apparently meant to be some kind of... dominating girl."
        show alice normalside
        a "Ah, that explains it."
        show mc confused
        m "Explains what?"
        show alice vannoyed
        a "Never you mind."
        # m "{size=+20}NOT THAT I WANT TO DO ANY OF THAT, OKAY!? IT'S JUST WHAT THE SITE SAYS!" with sshake
        # show alice laugh
        # a "How convincingly you deny it."
        # show mc vblushside
        # m "I-I'm serious! I'm not like that..."
        show alice sly smile
        a "Is there anything else? I quite like learning about myself."
        
        show mc sad
        m "Uh, it also gives your lifespan. Do you want to know?"
        show alice worried
        a "Oh-"
        show alice smirk
        a "A-hem! Of course. Tell me."
        "Ignorance is bliss. Maybe you shouldn't, to spare her the pain."
        show mc stressed
        m "(But she has the right to know.)"
        show mc sad
        m "It says your \"lifespan\" is three days. I'm sorry."
        show alice surprised
        a "\"I'm sorry\"?"
        show alice serious
        a "Is... is three days a short duration?"
        show mc stressed
        m "(YES!)"
        show mc awkwardsmile
        m "It's... um... not great? But you can do a lot in that time too."
        show alice think
        a "I see."
        show alice vannoyed
        a "Hmph! Good to know, I suppose."
        show mc surprised
        m "(Is she really fine?)"
        show alice sly smile
        a "What's with the surprise? Thought I'd cry? I'm not a child, %(player_name)s. I'm a mature woman."

    
    window hide
    hide mc
    hide alice
    hide dress
    hide alice_base_buns
    with easeoutbottom
    scene bottle day with dissolve:
        zoom 0.9
    show day_1 at topleft
    with dissolve
    show mc normal at right
    show alice_base_buns at left
    show alice normal at left
    show dress polkadot at left

    with easeinbottom
    # m "(Everything she says just confirms what the website says. Someone really engineered short-lived mushroom partners.)"
    # show mc stressed
    # m "(So it's true. I can't believe I've just grown someone.)"
    # show mc worried
    # "How am I going to look after her? You're responsible for an entire life. How are you going to cope when looking after yourself is such a chore?"
    # show mc vstressed
    # m "(Alice has a really strong personality too. How am I going to survive? At least it's just for three days, but still.)"
    # m "(And I feel so bad for her. None of this is right.)"
    

    m "Well, that's everything."
    show alice normal
    a "Aw, really? Well, it was useful... surprisingly."

    # show alice happy
    # a "%(player_name)s darling, are you finished with your break yet?"
    # show alice pout
    # a "I've been very patient, but there's a lot we need to catch up on." 
    # s
    show mc stressed
    
    m "Can we be serious for a second?"
    m "Are you okay?"
    show alice surprised
    a "?"
    m "I mean... you're... you've just..."
    show mc confused
    m "I'm sorry. This must be so confusing for you."
    show alice confused
    a "Huh? Well, it is now."
    show alice neutral
    a "Calm down and explain, %(player_name)s."
    m "You've been forced into this position! You've just been born."
    show alice normal
    a "And...?"
    show mc surprised
    m "Aren't you... scared? Frightened? You're experiencing the world for the first time."
    show alice sly smile
    a "Oh, sweet little %(player_name)s. I appreciate your empathy, I really do."
    show alice laugh
    a "But I'm not you! I don't give a damn about the world. It doesn't scare me, because..."
    show alice flirt
    a "I know my purpose."
    show mc shout
    m "But your purpose sucks!"
    show mc confused
    m "Spending your life, dedicated to me? I don't want that!"
    show alice surprised
    a "!"
    "There's so much else you can do!-"
    show alice disgusted
    a "Stop."
    show mc surprised
    m "But, Alice-"
    show mc worried
    show alice disappointed
    a "Quiet your insufferable squeaking and look at me."
    # show mc confused
    # show alice at center
    # show alice_base_buns at center
    # show dress at center
    # with move
    show mc surprised
    show alice neutral
    a "Don't analyse me, %(player_name)s. Don't tell me what to do, or how to do it."
    a "I don't need to explain myself. I know what I'm doing."
    show alice smirk
    a "It's encoded in me. My desire to f-"
    show mc vstressed
    m "BUT YOU DON'T HAVE TO LISTEN TO IT!"
    show alice sigh
    a "There's no need to get so worked up. I {i}want{/i} to listen to it."
    show mc confused
    m "You do? But why?"
    show alice laugh
    a "Why else? Because it feels right!"
    show alice wink
    a "Just like certain other actions do."
    show alice sly smile
    a "Now, I want you to forget about all of this, and focus on the woman in front of you."
    show alice flirt
    a "Because I really like you, %(player_name)s."
    show mc shocked
    m "(This is all moving WAY too fast!)"
    show mc stressed
    m "(Perhaps it makes sense. She was made to be this way.)"
    "Regardless, this situation doesn't sit well with you."
    "You don't even deserve love in the first place. You can't take her confession seriously at all."
    menu:
        "The guilt is already clawing at you from the inside of your stomach. You can't just let things progress as is."
        "Your love is fake.":
            show mc sad
            m "Alice, you don't like me. Not really."
            m "You only feel that way because you were made to."
            show alice normal
            a "So?"
            show mc surprised
            m "So... you should stop going after me?"
            show alice disappointed
            a "Who cares WHY I feel this way? I feel it, and that's what matters."
            show alice sly smile
            a "Oh honey, what the point in denying my feelings?"
            show mc confused
            a "All I know is that when I look at your shivering, anxious mess of a body..."
            show alice vflirt
            a "Hehe~ I don't need to explain, do I?"
            show alice smirk
            a "And I know, beneath that thick layer of insecurity, you like me too."
            show mc surprised
            m "I do?"
            show alice hime
            a "Of course you do."
            show alice sly smile
            a "So I want you to stop all of this insecure nonsense."
            show alice flirt
            a "No more anxious babbling. Just accept my love."
            a "If you just let me do my job, everyone will be happy."
            show mc confused
            m "What do you mean? What... job?"
            show alice vflirt
            stop music fadeout 2
            a "Allow me to demonstrate~"
            jump alice_bed_scene

        "You're not my type.":   
            
            $ alice_reject += 1     
            m "Alice, I'm sorry, but I can't. We just met, I hardly know you, and..."
            show mc sad
            m "I don't even {i}like{/i} you."
            show alice surprised
            # show alice at left 
            # show dress at left
            # show alice_base_buns at left
            # with move
            a "..."
            # show alice laugh
            # a "OHOHOHO! Now you grow a backbone?"
            # show mc confused
            # m "I'm serious. I don't like you."
            show alice pout
            a "Hmph! Of course you do!"
            show mc shout
            m "I don't! You're not even my type!"
            show alice worried
            a "Not you're type?"
            m "You're aggressive, you're acting selfish right out of the box-"
            show alice annoyed
            show mc surprised
            a "That's who I'm supposed to be, idiot!"
            show alice shocked at bounce
            a "Ah!"
            show alice flirtsweat
            a "Sorry~ Th-that was my bad apple side!"
            show mc stressed
            m "Eitherway, please just stop. Whether you want to or not, I can't reciprocate your advance."            
            show alice worried
            a "No... Don't say that..."
            show mc awed
            show alice cutesad
            a "Please... I'm actually not that kind of person."
            a "I'm more nervous than I let on. I-I wasn't sure what to do..."
            
            a "I just did what I thought I was supposed to! I didn't know I was pushing you away!"
            
            
            show alice vcry
            show mc shocked
            m "(SHE'S CRYING!?)"
            a "Please don't leave me~! *Sob* You're the only person who's ever cared about me!"
            show mc worried
            m "It's okay! Just please stop crying-"
            a "I wanted to say thank you, to give you everything you ever wanted! I'm sorry~!"
            show mc vstressed
            "Great job! You've made her cry!"
            show mc awkwardsmile
            m "It's okay! I swear! No hard feelings!"
            a "I need a hug!"
            # show alice pout
            # a "Okay..."
            # a "I know I'm being aggressive. I just thought I was supposed to do that."
            # #a "I don't want to actually upset you."
            # #m "..."
            # show mc normalside
            # m "(That was unexpected.)"

            # show alice hime
            # a "Hmph! Fine. Message received, loud and clear."
            # show alice happy
            # a "If you don't like them aggressive, then don't worry! I can be caring and cute too."
            # show alice sadsmile
            # a "Master %(player_name)s, I think I just got carried away earlier in my excitement to finally see you."
            # show alice sad
            # a "I didn't mean to be aggressive... I hope you forgive me."
            # show mc awed
            # m "Forgive you? Ah, sure. This is all new to you."
            # show mc awkwardsmile
            # m "I'm also pretty awkward so... a little miscommunication is bound to happen. I'm sorry if I offended you."
            # show alice happy
            # a "Thank you for being so considerate. Truthfully..."
            # stop music fadeout 2
            # play music "trip.mp3"
            # show alice cutesad
            # a "I just want to make you happy."
            # a "You grew me. I was so lonely inside that box. I just... wanted to repay your kindness. And that was the only way I knew how."
            # show mc surprised
            # m "It was that bad inside?"
            # show alice pout
            # a "It was boring! It was dark and tight and-"
            # show alice sigh
            # a "Well, usually that's a nice thing, but-"
            # show alice sad
            # a "I was conscious, yet immobile for weeks, unable to do anything. Your voice, the water you gave me, it was the highlight of my day."
            # show alice cute
            # a "You're the only person who's ever cared about me."
            # show alice vcry
            # show mc shocked
            # a "I was just excited to finally see you. To give you everything you ever wanted..."
            # m "(SHE'S CRYING!?)"
            # "Great job! You've made her cry!"
            # a "I'm sorry."
            

            show alice at center
            show alice_base_buns at center
            show dress at center

            with move
            show mc surprised at bounce
            show alice_affection at topright
            with dissolve

            menu:
                "She's walking towards you!"
                "Shove her away.":
                    $ alice_reject += 1
                    m "W-what are you doing!?"
                    show alice surprised
                    a "I just... wanted a hug."
                    show alice cutesad
                    a "You said we were okay, right?"
                    show mc worried
                    m "We are! But... I need to keep some space right now."
                    show alice worried
                    a "Do you really not like me, that much? I just wanted to clear the air, and to say thank you."
                    show mc awkwardsmile
                    m "No... it's not like that."
                    m "I can assure you that the air is cleared, and you can say anything you want from 2 feet back."
                    show alice pout at left
                    show alice_base_buns at left
                    show dress at left
                    with move
                    $ alice_rp -= 10
                    show alice pout
                    a "*Whining noises* {size=-20}Even when I was crying? You're a tougher one than I thought."
                    show alice sadsmile
                    a "Well, if you're not angry at me, then I'm happy."
                    hide alice_affection with dissolve
                    show alice happy
                    a "Master %(player_name)s, I just wanted to say-"
                    show mc shout
                    m "And please don't start with that \"Master %(player_name)s crap\". We're equals."
                    show alice sigh
                    a "Okay, {i}%(player_name)s{/i}. Now, as I was saying..."

                "Let her invade your personal space.":
                    show mc stressed
                    m "(I shouldn't be selfish.)"
                    m "(It's my fault she's crying. The least I could do I give her the hug she needs.)"
                    "You endure your discomfort and hug Alice."
                    show mc blushside
                    m "Y-you don't need to worry so much. We're okay."
                    show alice worried
                    a "Thank you. *sniff* I just felt so lonely."
                    show alice sad
                    a "I went overboard at the beginning. I'm really sorry."
                    show alice vcry
                    a "Am I annoying still you?"
                    show mc awed
                    m "No. This is fine."
                    "It's true. The longer you hug it out, the less you seem to forget your initial worries."
                    "Now, it's almost becoming enjoyable."
                    show mc vstressed
                    m "(But the way she's digging her nails into my back kinda hurts!)"
                    a "I like you. No matter what you say."
                    
                    show mc confused
                    m "What?"
            
            show alice cutesad    
            a "Before today, all I've been doing is waiting."
            show alice slightsmile
            a "Hearing your voice, your sweet daily encouragment, was the highlight of my days."
            show alice sad
            a "So I've been thinking in that horrible, dark space..."
            show alice happy
            a "...was getting to see you. Getting to be your friend, learning about you, and spending time together."
            show alice wink
            a "I've been imagining all sorts of things we could do together."
            show mc confused
            m "Something in your eye?"
            show alice sigh
            a "..."
            a "I'll be more direct."
            show alice vflirt
            stop music fadeout 2
            a "I'd like to show you how much I appreciate everything you've done."
            a "Have a seat, %(player_name)s~"
            jump alice_bed_scene
    

label alice_bed_scene:    
    window hide
    hide mc
    hide alice
    hide alice_base_buns
    hide dress
    with dissolve

    scene alice_bed_1 with fade
    play music "sexy.mp3"

    # Use audio filters in renpy to make the music sound like it's melting the closer she gets.
    
    # renpy.music.set_audio_filter("music",
    #     af.Sequence([
    #     af.Reverb(0.5),
    #     af.Highpass(900),
    #     ]))

    m "Why'd you push me!?"
    a "Because you're going to want to get more comfortable."
    "WAIT A SECOND! What's with that obviously suggestive line!? And why is she looking at you like THAT?"
    m "(I-I must be misinterpreting-)"
    a "%(player_name)s... I've been so lonely~ I haven't been able to say a thing for weeks..."
    a "You understand, don't you? How horrible that can feel?"
    m "I... kinda do...?"
    a "Then, maybe we can help each other out."
    
    show alice_bed_2 with dissolve 
    "OOOOOH! SHE'S APPROACHING! I DON'T THINK YOU'RE MISINTERPRETING ANYTHING!" with sshake
    "Are ya ready, champ?"
    m "(Of course not! I've never been so unprepared in my life! I haven't even brushed my teeth yet!)" with sshake
    m "(And I hardly know her! And she's a mushroom! And- And-!)"
    m "(What should I do!?)"
    a "Oh my~ Your head is practically steaming."
    a "What's with your frown? There's nothing to worry about."
    a "It's just me and you here."
    "It feels like your brain is melting the closer she gets!"
    m "(It's really hard to think right now...)"
    m "(Your heart is thumping loudly in your chest, as Alice inches closer.)"

    a "That's right. Just relax."
    show alice_bed_3 with dissolve
    pause 1
    "Alice gives your cheek a gentle caress with her fingertips, sending an ice-cold bolt of pure sensation up your spine."
    m "A-ah..."
    a "See? Everything is starting to feel so niiiiice, riiiiight~?"
    a "You can stop thinking, okay, sweetheart? Just let go of all your worries~"
    a "Mm, I want to be even closer to you."
    a "Please %(player_name)s, will you let me?"
    a "All you have to say, is \"yes\"."
    
    show alice_affection at topright with dissolve
    
    menu:
        m "(It's really heart to think... but I need to choose now what I'm doing.)"
        "Yes?":
            #play sound "bite.mp3"
            #show alice_bed_4 with dissolve
            m "Y-Yes?"
            "You say it like a question... but it seems Alice takes it as an answer."
            $ alice_rp += 30
            a "Oh? After all that denial, you {i}do{/i} like me, you coy thing~"
            scene black with fade
            "Placing her hands against your chest, Alice presses her mouth against yours."
            "Your head feels dizzy, but in an increasingly good way."
            "She moves her lips slowly against yours, gently pulling herself closer to you, until you realise she's lying on top of you."
            "You can't keep track of time, your heart is beating so fast."
            m "(I can't believe she's kissing me. Am I dreaming? Why would she ever like someone like me?)"
            "You're right. It doesn't make sense."
            "But does it need to?"
            "It doesn't."
            #Make music here strong
            stop music fadeout 2
            "Your reason, along with your worries, dissolves..."
            "You relax, to the point that it feels like you have no control over your body anyone."
            "Everything distorts into a dream-like movie. Drifting in and out of awareness."
            "Morphing slowly into delirium. You can't keep time."
            "You're aware that you're salivating and sweating more, that there is euphoria in the moments that you're present."
            "Everything revolves around you, up and down, all around, like you're stuck on a carasoul."

            window hide
            stop music fadeout 2
            scene black with dissolve

            $ alice_rp += 100
            # scene bottle night:
            #     zoom 0.9
            # show day_3 at topleft
            # show alice_affection at topright
            # with dissolve

            # show mc happy at right
            # show alice_base_buns at left            
            # show alice flirt at left
            # show dress polkadot at left
            # with easeinbottom

            # window show
            # a "Hey, dog."
            # m "Yes, Alice?"
            # show alice smirk
            # a "It's time for me to go."
            # show mc sad
            # m "Already...?"
            # show alice cute
            # a "Aw, don't be sad."
            # show mc stressed
            # show alice hime
            # a "You've been so good to me afterall, so I'm happy."
            # show alice happy
            # m "I trust you've had a wonderful time these past few days?"
            # show mc happy
            # m "Yes, Alice."
            # show alice flirt
            # show mc blushside
            # a "Good dog! *pat*"
            # show alice sly smile
            # a "Do you remember what you're going to do when I'm gone? Tell me."
            # show mc annoyed
            # m "I'm going to !"
            # show alice laugh
            # a "Aw, that's right! I love you so much!"
            # show mc blushside
            # m "I... I love you too."
            # show alice vflirt
            # a "Mhm~ and you know what would be the most romantic way to send me off?"
            # show mc awed
            # m "W-what, Alice?"
            # show alice normalside
            # a "Well, I was thinking it would be a shame if I got old and wrinkly, don't you think?"
            # show mc surprised
            # m "No!"
            # show alice cruel
            # a "Sweet of you to say, but still. As your final act of love, my order for you is..."
            # a "To eat me."
            # show mc shocked
            # m "But-"
            # show alice disappointed
            # show mc worried
            # a "...?"
            # show mc stressed
            # m "..."
            # show mc sad
            # m "Yes, Alice."
            # window hide
            # scene black with fade
            # pause 1
            # window show
            # "End 1: Romeo and Juliet."
            



        "AAAHHHH!":
            $ alice_reject += 1
            $ alice_rp -= 10
            window hide
            stop music
            play sound "punch.wav"
            show alice_bed_reject
            pause
            scene black with dissolve
            



    scene bottle day:
        zoom 0.9
    # show dirty1:
    #     zoom 1.1
    # show dirty2:
    #     zoom 1.1
    # show bottle:
    #     zoom 1.1
    
    
    with dissolve
    show day_1 at topleft
    show alice_affection at topright    
    with dissolve
    # if alice_reject <= 1:
    #     show mc worried at right
    #     show alice sad at left
    #     with easeinbottom
    #     m "I'm sorry for shoving you. That was just too much for me and I..."
    #     show alice pout
    #     a "..."
    #     show mc stressed
    #     m "Sorry. I just needed some space and panicked. Hope you're not hurt."
    #     show alice sigh
    #     a "Heh, it's okay."
    #     show alice happy
    #     a "Honestly, sometimes I don't know how to hold back."
    #     a "And it's adorable how green you are."
    #     show mc confused
    #     m "So we're okay, right?"
    #     play music "normal.mp3"
    #     show alice flirt
    #     a "Mhm~ As long as you forgive me for being too excited."



    # elif alice_reject >= 2:

    if alice_reject >=2:
        jump real_route
    else:
        jump nice_route

label real_route:
    show mc worried at right
    show alice_base_buns at left
    show dress polkadot at left
    show alice vannoyed at left

    with easeinbottom
    window show

    m "Are you okay? I just panicked and-"
    show alice angry
    a "WHAT THE HELL!?"
    a "You punched me! Do you have a problem with me or something?"
    show mc stressed
    m "I know, I'm really sorry. Technically, it was a headbutt-"
    show alice annoyed
    a "WHO CARES!?"
    show mc worried
    m "You're right, sorry. I just couldn't do it. I couldn't do..."
    show mc vblushside
    m "That."
    show alice mendokusai
    a "What are you, a child? It's called sex."
    show alice surprised
    a "Ah! I mean..."
    show alice sigh
    a "Hah, clearly I approached you incorrectly..."
    show alice disappointed
    show mc surprised
    a "I think this would all work out better if you told me exactly what you want."
    a "So tell me: should I be more gentle? Coy? Do you want me stutter too?"
    a "Do you like them silent? I'll be anything you want. I can do it."
    show mc confused
    m "Can't you just be yourself?"
    show alice neutral
    a "What's the point of being myself if you don't like me?"
    show alice normal
    a "So if you help me here, I can fix this all."
    show mc surprised
    m "You were just too fast!"
    show alice confused
    a "Ah, so I need to be slow. Gotta slowly melt the ice around your heart and all that. Ugh."
    show mc confused
    m "Alice, you don't even want to be with me. Why do you care so much?"
    a "What are you talking about? There's nothing I'd like more than-"
    show mc stressed
    m "Stop lying to yourself. "
    show alice flirt
    a "So you do want to have sex with me?"
    show mc shout
    m "NO!"
    show alice hime
    a "Ah ha! See!? There's the problem!"
    show mc confused
    m "Huh!? What the hell... You're messed up."
    show alice disappointed
    a "…"
    show mc sad
    m "Sorry."
    show alice vannoyed
    a "Just tell me what you want!"
    show mc stressed
    m "…"
    m "Stop harrassing me!"
    show mc shout
    m "Stop trying to force yourself on me! I don't want you!"
    show mc normalsquint
    m "Just leave me alone already."
    show alice surprised
    a "..."
    show alice sad
    a "..."
    show alice cry
    a "Ugh!"
    show alice angry tears
    a "Fine! You've rejected me enough. I failed! I get the point!"
    show mc surprised
    m "Alice-"
    a "But if you don't like me, maybe someone else will!"
    window hide
    hide dress
    hide alice_base_buns
    hide alice
    with easeoutbottom

    play sound "door.wav"

    show mc awed
    window show
    m "She's gone..."
    window hide
    show mc stressed at center with move
    play music "normal.mp3"
    window show
    m "What just happened?"
    m "I grew a mushroom girl? And right off the bat, she wants to do {i}THAT{/i}?"
    show mc normalside
    m "Maybe it's like a mushroom instinct? Ugh... I don't know anymore."
    "You made her cry and run out."
    show mc worried
    m "But I had to stop her! I wasn't too harsh, was I? Rather that, than lead her on."
    play sound("phonealarm.ogg")
    show mc shocked
    m "AAH!"
    show mc awed
    m "Oh, my phone got a message."
    window hide
    hide mc with dissolve

    call screen check_phone_alice_1 with dissolve
    
    screen check_phone_alice_1:
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.371 ypos 0.370 idle "pc/phone_idle.png" hover "pc/phone_hover.png"
            action Jump("check_phone_alice_2")
    
    label check_phone_alice_2:
        show mc stressed with easeinbottom
        window show
        m "(Please don't be Mom. I do NOT have the energy to tell her how \"great\" today is going.)"
        show mc normal
        m "Oh, it's just Rom."

        "Ah yes, that one guy you met randomly whose entire life revolves around an anime girl."
        "Who won't stop talking to you."
        show mc normalside
        m "(He's not THAT bad. He understands what I'm going through.)"
        "Birds of a feather stick together and all that, right?"
        window hide
        jump dischord_chat_Sabrina

    label dischord_chat_Sabrina:
        #play music "computerHum.wav"
        scene discord with fade
        window show
        rb "sup i was wondering if you wanted to hop in vc"
        m "Sorry, kinda busy rn... can you type?"
        rb "np i was just bored and your always online so..."
        m "ouch"
        rb "are u eeping soon? little eep moder?"
        m "i just got up"
        rb "o"
        rb "your sleep finally looped back to humanity"
        rb "vampirism cured"
        m "i guess"
        rb "are you okay, you don't usually respond so short"
        m "yeah i'm fine... it's just"
        m "idk"
        rb "did something happen?"
        m "you probably won't believe me so..."
        rb "don't be like that"
        m "fine"
        m "You know I told you I was growing mushrooms..."
        m "It bloomed today... into a girl"
        rb "lmao nice nice"
        m "No like a real one, that talks and everything"
        rb "can u send link to site"
        m "https://mushroom-site.something"
        m "and then umm "
        m "She got all close to me and then ran off crying..."
        rb "wait, did you make this site? I didn't know you could make websites"
        rb "it looks so professional"
        rb "how many hours did it take"
        rb "like for a joke it's so good" #changed from based bc its politically charged apparently
        m "I can't code, and it's real."
        rb "wait like real real>"
        m "yeah"
        rb "emoji upside down smile" #make into emoji
        rb "lmao wtf"
        rb "let me order one real quick"
        rb "I wonder if I can get it to cosplay Rom"
        m "What? Is he not listening to me?"
        m "are you for real?"
        rb "like was she hot? I've always wanted an irl waifu"
        m "I'm being serious, she's like a living being... She talks and moves and everything"
        rb "sounds like I don't need my onahole anymore"
        m "What the fuck?"
        m "I'm sorry, I think i've gotta go"
        rb "don't have too much fun"
        window hide


    scene bottle_phone noon with fade:
        zoom 0.9
    show mc stressed with easeinbottom
    window show
    m "Am I the weird one?"
    m "Is that how normal guys are supposed to react?"
    show mc worried
    m "I should probably get her..."
    "What will you even say? Do have the words?"
    show mc sad
    m "But she's my responsiblity. I grew her."
    m "I have to find her and straighten things out with her."
    "Even if people see you in the gross, unclean state you are?"
    m "(Just don't think it!)"
    "Or you could think about it, realise that you will probably embarrass yourself, and stay here."
    window hide
    show mc at right with move
    menu:
        "Stay here.":
            window hide
            show mc sad at center with move
            window show
            m "*Sigh*... what's the point? She's mad at me, and I'm in no state to walk around the dorm."
            "I doubt she wants your help anyway."
            show mc stressed
            m "(Yeah... I shouldn't do anything. I'd just make things worse.)"
            "Exactly. Don't assume people want you in their vicinity."
            "You think you'd be helping, but really, they'll be thinking how annoying you are."
            show mc vstressed
            m "(She's confident, attractive... She made the right call leaving me.)"
            window hide
            hide mc with dissolve
            scene black with Fade(0.5, 1.0, 0.5)
            pause 1
            stop music fadeout(2)
            window show
            m "(But it still stings.)"
            $ persistent.aend1 = True        
            
            "End 1: Be free, Alice."

        "Find her.":
            show mc stressed at center with move
            window show
            m "Okay, you can do this! Just find her, and get back, quickly!"
            window hide
            hide mc with easeoutbottom
            play sound "door.wav"

            scene hallway with fade
            show mc worried with easeinbottom
            window show
            m "(Okay, coast is clear. That's good, at least.)"
            show mc surprised
            m "(Wait - no it's not! I have no idea where Alice is!)"
            show mc stressed
            m "(God... this is way more stress than I signed up for.)"
            show mc normalside
            m "What if she doesn't know you're supposed to wait before you cross the road?"
            m "I wonder if she'd just explode into mushroom pieces if she got hit by a car..."
            show mc stressed
            m "(Ah! I'm getting distracted! Focus!)"
            # m "She got upset in the heat of the moment"
            # m "But as soon as she realizes she has no shelter, she's gonna come running back, right?"
            # m "Maybe I should just go and wait for her in my room?"

            na "KYAAAAAAAAAA!" with sshake
            show mc surprised at bounce
            m "Alice!"
            window hide
            hide mc with easeoutbottom
            scene bathroom with fade
            show showerguy scream at right 
            show showerguy scream at quiver
            show alice_base_buns at left
            show dress polkadot at left
            show alice pout at left

            with dissolve
            window show
            keshad "{sc=3}{color=#000000}AAAAA!"
            ali "Why are you backing away?"
            show alice:
                xpos 0.1
            show dress:
                xpos 0.1
            show alice_base_buns:
                xpos 0.1
            with move
            show alice flirt
            ali "Don't you want to get closer to me?"
            
            keshad "{sc=3}{size=+20}{color=#000000}AAAAHHGH!!!"

            play sound "door.wav"
            show mc stressed at center
            with easeinbottom
            show mc shocked at bounce
            
            m "What the-!?"
            #show mc vstressed at center with move
            show alice disappointed
            show alice:
                xpos 0
            show dress:
                xpos 0
            show alice_base_buns:
                xpos 0
            with move
            a "Well look who came running back."
            show alice smirk
            a "Sorry~ but I'm in the middle of something right now-"
            show mc vshout
            m "YOU! Get out of here!"
            show alice shocked
            ali "Wh- Hey!"
            window hide
            # show mc at right
            # show alice at right
            # show dress at right
            # show alice_base_buns at right
            # with move
            
            hide mc
            hide alice
            hide dress
            hide alice_base_buns
            with easeoutbottom
            play sound "door.wav"
            window show
            m "{size=-20}Sorry!"

            show showerguy sad

            keshad "{sc=2}{color=#000000}*Whimpers*"
            window hide
            scene black with fade
            


    show afternoon_clouds
    show bedroom_opencurtains:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty1:
        matrixcolor TintMatrix("#f4ca9a")
    show dirty2:
        matrixcolor TintMatrix("#f4ca9a")
    show bottle:
        matrixcolor TintMatrix("#f4ca9a")
    with Dissolve(2)
    play sound "door.wav"

    show mc normalsquint at right
    show alice_base_buns at left
    show dress polkadot at left
    show alice disgusted at left
    with easeinbottom

    # I feel like the tone is kinda off
    window show
    ali "Where are you dragging me you pervert?"
    ali "What kind of sick,"
    show alice flirt
    ali "tormented,"
    show alice disgusted
    ali "degenerate things are you going to-"
    play music "fight.mp3"
    show mc vshout 
    m "{size=+20}What the fuck were you \n{sc=2}{size=+20}{color=#000000}doing{/sc} down there?!" with sshake
    show alice neutral
    ali "It-"
    show mc shout
    m "You were harassing... {i}assaulting{/i} someone! My God!"
    show alice pout
    ali "I-"
    show mc vstressed
    m "Don't you get how stupid that was?"
    show mc worried
    m "It's bad enough you let someone see you!"
    m "What am I supposed to do if they call the police?"
    show alice annoyed at quiver
    ali "It-!"
    show mc vannoyed
    m "You {i}what{/i}?"
    # try to spell stuff to make it sound like she's sobbing
    show alice angry at bounce
    ali "It's not {i}my{/i} fault that you ignored me!"
    ali "The only reason I went looking for someone else is because you humiliated me!"
    show mc shout
    m "How did {i}I{/i} humiliate {i}you{/i}?" 
    show mc normalsquint
    ali "You bought me, and picked me out for one reason."
    show alice vangry tears
    ali "But when you actually see me, you THROW ME AWAY!"
    show alice serious
    ali "How am I not good enough for you?"
    show mc surprised
    m "What are you {i}talking{/i} about?"
    show mc worried
    m "You just came up to me, and started touching my face."
    m "and... saying weird stuff."
    #show mc stressed
    #m "And then you just ran away! I didn't do anything."

    show alice sad
    ali "But that's why you raised me, right?"
    show mc shout
    m "No! It's a misunderstanding!"
    show mc stressed
    m "I didn't know anything about you until literally five minutes ago."
    show alice sulk
    ali "So what? I'm supposed to be irresitible. That's my whole thing."
    ali "That's my purpose."
    show alice disappointed
    ali "So either there is something is wrong with you..."
    show alice sad
    ali "...or there's something wrong with me."
    show mc worried
    stop music fadeout 2
    m "..."
    show mc normal
    m "So that's why you went to find someone else."
    show alice sigh
    ali "But all he did is {i}scream{/i}."
    ali "..."
    show alice think
    ali "Maybe there {i}is{/i} something wrong with me?"
    show mc confused
    ali "Maybe it's my face or..."
    window hide
    #Choice: It's okay ; I think you're valueble ; step on me mommy; 
    #You're valueble
    menu:
        "But you ARE pretty! (N/A)":
            show mc confused
            m "What...? But you're like... objectively attractive."
            show mc awed
            m "You're incredibly pretty."
            m "So much that anyone would be jealous."
            show mc stressed
            m "..."
            show mc normalside
            m "Especially compared to someone so plain like me."
            show alice neutral
            ali "Oh yeah, self depreciation always makes people feel better."

            return
        # "Step on me mommy (N/A)":
        #     return
        "Your appearance isn't the problem": #you can change the phrasing
            window show
            show mc awed

            # Change this argument! Too sage like. 
            show mc confused
            m "You're incredibly pretty."
            m "So much that anyone would be jealous."
            show mc stressed
            m "..."
            show mc normalside
            m "Especially compared to someone so plain like me."
            show alice neutral
            ali "Oh yeah, self depreciation always makes people feel better."
            show mc normal
            m "Anyway, I was just trying to say that..."
            m "I don't think that's what makes you valuable."
            ali "..."
    show mc confused
    m "I started growing you because I felt worthless, and like I couldn't accomplish anything."
    m "And you grew to be so much more than I could have imagined."
    show mc vstressed
    m "In... many ways."
    show mc normal
    m "I don't know that much about you, or how you feel but..."
    m "I think that you're worth more than what you were being sold as."
    show alice normal
    ali "..."
    show alice normalside
    ali "Whatever... It's not that big of a deal I guess"
    show mc confused
    m "..."
    show mc normalside
    m "I had a look over the website that I got your growing kit from."
    m "And I saw the way that you were being sold."
    show mc blushside
    m "As a... \"good time\", and as really... aggressive and dominant."
    show alice neutral
    ali "..."
    show mc confused
    m "Do you know anything about your manufacturer?"
    show alice sigh
    ali "... *sigh*"
    show alice normalside
    ali "Not really anything detailed."
    ali "I just have a vague sense of like."
    show alice sulk
    ali "What I'm {i}supposed{/i} to do, I guess."
    show alice sly smile
    ali "As well as every possible way to tie you up." #you already made this joke in d2 cafe scene
    show mc blushside
    m "..."
    
    show alice confused
    ali "But all I could think when I first woke up was that..."
    show alice normal
    show mc awed
    ali "I'm supposed to pleasure whoever grew me."
    show alice sigh
    ali "That's my goal."
    show alice disgusted
    ali "So for you to turn me down how you did really sucked."
    show mc worried
    m "..."
    show alice disappointed
    ali "Even if that wasn't your intention, and that's not why you grew me..."
    show alice think
    ali "If I can't do that, then what AM I supposed to do?"

    #Maybe a choice here in response to this question? Idk vs pessimistic "life is purposeless anyway"
    show mc awed
    m "I..."
    show mc awkwardsmile
    m "I don't know how to answer that."
    m "I guess you could say I'm struggling with the same question."
    show alice sulk
    ali "..."
    show alice disappointed
    a "What do you even do in here all day? This pathetic excuse for a room is legitimately making me depressed."
    show mc normalside
    m "Yeah. I can agree with that."
    a "Come on. You owe me. If you're going to mess my entire life up right out of the box..."
    show alice normal
    a "Then the least you could do is clean up the mess."
    show mc surprised
    m "W-what do you want?"
    show alice neutral
    a "Stimulation. I need something to fill the empty void inside my cruel heart, so show me something you humans do that can do that."
    
    a "So I'm thinking... take me out somewhere interesting."
    show mc worried
    m "I-I'm not the kind of person who can just... go out."
    a "Too bad, so sad, I don't care. You can't just ignore the consequences of your actions."
    "She doesn't get it. How can you expect a mushroom to understand your anxiety?"

    "Just the thought of leaving the safe, albeit depressing, box of your room makes your heart start racing."
    "And being seen with a woman like Alice is sure to draw attention."
    "You're definitely going to be looked at."
    show mc stressed at quiver
    m "..."
    show alice annoyed
    a "Really? Trembling? Are you broken or something? What's so bad about going outside?"
    m "It's overwhelming."
    show alice serious
    a "You're the one making it so."
    show alice normalside
    a "What, want me to hold your hand? Would that help you take responsibility for ruining my life?"
    show alice normal
    a "Come on. There has to be SOMETHING that even someone like you can do outside."
    a "Do I need to remind you that I die in three days?"
    show mc stressed
    "Guilt is something you cannot ignore."
    "She doesn't have time. You can't make her wait until you're mentall ready."
    "You just have to force yourself, no matter how horrible it feels."
    show mc sad at nothing
    m "I guess... there is one thing..."
    window hide

    show mc normal
    m "Actually, there's this arcade I've always wanted to check out-"
    show alice confused
    ali "An arcade?"
    m "We could go and I could maybe try show you how to play some video games."
    show alice surprised
    ali "What's that?"
    show mc normalside
    m "Like... you pretend to be someone else, and you complete fun missions using a device."
    show alice neutral
    a "..."
    a "I trust my expression speaks for itself."
    show mc confused
    m "You want to find stuff you're interested in right?"
    show mc annoyed
    m "How do you know you don't like it if you don't give it a go?"
    show alice pout
    ali "..."
    show alice mendokusai
    ali "...FINE~"
    scene arcade with fade
    show mc surprised at right
    show alice disappointed at left
    with easeinbottom
    #black scene


    #Change this so alice has an appropriate amount of knowledge about this stuff
    $ arcadeWent = True
    m "Woah, look at this place! They have so many retro titles!"
    show alice normalside
    ali "Isn't that like a nice way of saying they're charging a dollar for games that have been out of date for like 30 years?"
    show alice confused
    ali "Can't you play these on your computer anyway?"
    show mc normalside
    m "I guess I could set up a MAME emulator on RetroArch, but-"
    show alice annoyed
    ali "Are you listening to yourself right now?"
    ali "I have no fucking clue what you're talking about."
    show mc awed
    m "I just meant like, we could use my PC..."
    show mc normalside
    m "but then we're really compromising on the authenticity of the experience."
    show alice smug
    ali "The experience of being in a run down shit hole?"
    show mc surprised
    m "Woah! They have that weird train game?"
    show mc happy
    m "It's a weird Japan-only game where you play as a train conductor and like, there's train levers, and-"
    show alice neutral
    ali "You're really making this whole gaming thing SO interesting."
    show mc normal
    m "Well there's a whole bunch of other games too."
    m "What kind of thing do you think you might like?"

    show alice confused
    ali "I don't know... What about that one over there?"
    show alice happy
    ali "Those little dinosaur things are kinda cute~"
    show mc happy
    m "Oh Bubble Bobble?"
    m "I haven't played that game since I was a kid."
    m "Lemme get some tokens..."

    #interlude
    show black with dissolve
    "You show Alice how to move, blow bubbles, and capture monsters."
    "She quickly grasps the basics and is able to beat the first level without any issues."
    "However, after only a few levels, the difficulty begins to increase dramatically, and before more than a few minutes have passed..."
    show alice annoyed
    hide black with fade

    ali "Game Over? What the fuck is this shit?"
    show mc annoyed
    m "In these kind of games you only get a few lives, and if you use them all up, you need to pay more to keep playing."
    show mc happy
    m "Do you want to keep playing this?"
    show alice sulk
    ali "What's the point? What do I {i}get{/i} if I keep playing?"
    show mc awed
    m "Well... The satisfaction of having gotten further, and accomplishing something that not many people have done?"
    show alice disappointed
    ali "That's stupid."
    ali "Who cares if you are the best in the world at playing stupid children's games?"
    show mc normal
    m "..."
    show mc sulk
    m "It's not stupid to me..."
    m "...or lots of other people."

    m "These games represent memories of our childhoods."
    m "Friendships."
    show mc normalside
    m "Although looking around here, you might not get it but..."
    m "There are all sorts of games."
    m "Games about guns, games about fishing, games about defusing bombs."
    show mc stressed
    m "Games about just talking to people."
    m "Games that give you a new outlook on the world..."
    show alice neutral
    ali "..."
    show mc awed
    m "Games to play by yourself, games to pass the controller back and forth..."
    m "Games that let you meet new people."
    m "I think that for me, it helps to feel connected to something bigger."
    m "The community of people brought together by having this small thing in common."
    show mc normalside
    m "I just thought it would be cool if you would be able to find something like that too."
    show alice sulk
    ali "I guess..."
    show alice normalside
    ali "I'm sorry okay?"
    ali "I shouldn't have called it stupid."
    show alice normal
    ali "But even so, I don't really think this is for me."
    show mc slightsad
    m "Okay... let's go home."
    
    window hide
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
    show day_1 at topleft
    show alice_affection at topright
    with dissolve
    play music "night.mp3"
    play sound "door.wav"

    show mc normal at right
    show alice neutral at left
    with easeinbottom
    window show
    a "Well, that was a complete waste of time."
    m "I'm sorry. I did my best, but I'm not good at this kind of thing. I just did what I thought would be fun..."
    show alice sigh
    a "If that was your best, then I'm in trouble."
    show mc normalside
    m "It's getting kinda late... Can we think about this more tomorrow?"
    show alice surprised
    ali "You're going to sleep already?"

    show mc normal
    m "Yeah, I didn't quite get my full 8 hours."

    #needs something here
    show mc stressed
    m "Ugh, so tired. Good night."
    window hide
    hide mc 
    hide alice
    with easeoutbottom
    window show
    "You climb into bed and close your eyes."
    "After a few seconds you feel the weight of the mattress shift and the duvet being lifted."
    show mc shocked at right
    with easeinbottom
    m "What are you doing??!!"
    show alice sly smile at left with easeinbottom
    ali "I was gonna cuddle you while you slept."
    show mc vblushside
    m "No! W-why would you-?"
    show alice pout
    ali "I don't know! As soon as I saw your sad little body in the bed, I just... I don't know. I guess that's my stupid mushroom brain again."
    show alice normalside
    ali "It's not like I sleep. I'm a fungus."
    show mc stressed
    m "Ugh... What the hell has that company taught you?"
    show alice normal
    ali "Isn't this normal?"
    show mc vstressed
    m "Ummm... Well it depends."
    show alice confused
    ali "On?"
    show mc worried
    m "Look I don't really want to explain this right now..."
    show mc confused
    m "There's my laptop up on the table."
    m "Why don't you grab it and learn a little about the world."
    show alice neutral
    ali "I can't read, doofus."
    show mc annoyed
    m "Then just watch some videos on my homepage or something!"
    show mc normal
    m "Maybe you'll be able to find something that inspires you there."
    show alice sigh
    ali "Sigh... Okay..."
    hide alice with easeoutbottom

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "You fall asleep to the faint humming of the laptop fan..."
    with dissolve 
    pause 3

    jump day2Morning














    

                
            



    # a "Mhm?"
    # show mc blushside
    # m "You're... in my bed...."
    # a "You're not going to leave me alone all night are you?"
    # a "I think I would cry."
    # m "Um, well, if it'll stop you from crying..."
    # m "But don't you want to do anything more interesting than just wait for me? I've got a laptop you can use."
    # a "This is all I want."
    # m "But... isn't there a better use of your time? I sleep for a long time."
    # a "Nope."
    # m "(Well, I'll be damned... Someone is happy to just lie next to me all night long.)"
    # m "(I feel both embarrassed and guilty.)"
    # m "You've got limited time. Please. Use it more wisely."
    # a "What would you like me to do?"
    # m "To like... just learn about the world! Watch videos and stuff. Get interested!"
    # m "You can't just rely on me to entertain you. Make the most of your life, Alice."
    # a "Alright, I will."
    # a "And tomorrow you and I will have a date together."
    # m "Uh..."
    # "Too afraid to make her cry, you simply nod."

    # chibi sleep while spoon



label nice_route:
    

    show mc shocked at right
    show alice_base_buns at left
    show dress polkadot at left
    show alice shocked at left
    with easeinbottom
    m "I'm so SO sorry! That was just too much for me and I panicked!"
    show alice pout
    a "Well, I was certainly taken aback."
    show mc worried
    m "Sorry. I just needed some space quick. Hope you're not hurt."
    show alice sigh
    a "I can deal with a little abuse here and there."
    show alice sly smile
    a "Perhaps in my eagerness I rushed things. You seem even greener than I first thought."
    m "So we're okay?"
    play music "normal.mp3"
    show alice vflirt
    a "Mhm~ As long as you forgive me for being too excited."
    show mc awkwardsmile
    m "Uh, yeah. Just don't do that again."
    show alice hime
    a "Mhm. More foreplay. Got it."
    show mc stressed
    m "That's not... *sigh*."
    show bottle noon with Dissolve(2):
        zoom 0.9
    # show bottle_phone noon with dissolve:
    #     zoom 0.9
    # show mc confused at right
    # show alice_base_buns at left
    # show dress polkadot at left
    # show alice flirt at left
    play music "normal.mp3"
    # with easeinbottom
    show mc awed
    m "I can't believe it's already afternoon. We've been talking for a while..."
    show alice wink
    a "Oh my. We're all alone in your bedroom and it's nearly night... Whatever shall we do?"
    m "(Yeah, I can understand why she'd feel bored. There's nothing to do here.)"
    show mc normalside
    m "Hmm... I guess we could go somewhere to pass the time."
    show alice sigh
    a "*Sigh* That's not..."
    show alice surprised
    a "Oh! I see! A date!"
    show alice flirt
    a "Who am I to deny you something like that? Of course we can go!"
    show mc stressed
    m "This is not a date! I'm traumatised enough from earlier."
    show alice pout
    a "Sure, you can call it whatever you want. In the end, it's the same thing."
    show mc confused
    m "A-alright then..."
    show alice sly smile
    a "So where are you taking me?"
    show mc normalside
    m "(Getting out this room would be nice, but that said, I don't actually want to leave.)"
    show mc stressed
    m "(The connundrum of a socially anxious person. Isn't there a place super close by? With no people? And something nice to see for Alice?)"
    show mc surprised
    m "Ah. Actually..."

    stop music fadeout 2
    scene black with fade

    scene rooftop with fade
    show alice_base_buns at left
    show alice sly smile at left
    show dress polkadot at left

    show mc happy at right

    with easeinbottom
    play music "trip.mp3"
    a "Oooh~ romantic. And we're all alone too."
    a "Alright. What did you want to show me?"
    m "You can see the stars pretty well up here."
    m "..."
    a "..."
    show alice confused
    a "So what are you going to show me?"
    show mc confused
    m "I'm already showing you - the stars!"
    show alice flirtsweat
    a "Oh!"
    a "Those... white things?"
    show mc awed
    m "Yes. Aren't they beautiful?"
    show alice happy
    a "If you think so, then I agree."
    show alice normal
    m "Don't you think it's terrifying how far away they are?"
    m "Each one is a different place with its own conditions. There's so much out there that we will never know."
    a "..."
    m "Seeing them, thinking of how lucky I am to be alive, it makes life feel magical again."
    show mc normal
    m "Or maybe that's just me."
    show alice happy
    a "No, no, I get it! The stars are beautiful."
    a "Especially those ones over there, the purple and blue ones!"
    show mc confused
    m "E-eh!? Where?"
    show alice surprised
    a "There! They just changed colour again. Now they're green and yellow."
    show mc shocked
    m "WHAT?"
    show mc confused
    "You follow the direction of Alice's finger."
    "Instead of pointing up to the sky, it's pointed down, below the edge of the railing, at the building across the street."
    show mc surprised
    m "Oh..."
    show mc normal
    m "The arcade. Those aren't stars, they're just ordinary lights."
    show alice pout
    a "Aw, but they're so pretty..."
    show mc awed
    m "Hm, it doesn't look too busy tonight. I wonder if..."
    show mc worried
    m "Ah, but I'm here with you. I shouldn't."
    show alice hime
    a "Aha! Gotcha!"
    show mc surprised
    m "?"
    show alice sly smile
    a "You want to go there, do you? Well, it just so happens..."
    show alice wink
    a "So do I!"
    show mc confused
    m "You don't even know what an arcade is, do you?"
    show alice laugh
    a "I know it's a place you want to visit, and that's all I need to know!"
    show mc worried
    m "But-"
    show alice smirk
    a "I won't allow you to be bored with me, so move your little butt over there already!"
    show mc shocked
    m "BUT-"
    show black with fade
    stop music fadeout 3

    "You quickly learn that once Alice sets her mind to something. She gets it."
    "After a minute of her physical pushing and verbal insistence, you finally give up and conceed. You are not match for her confidence."



    window hide
    hide mc
    hide alice
    hide dress
    hide alice_base_buns
    with easeoutbottom
    stop music fadeout 2
    scene black with Fade(0.5, 1.0, 0.5)        
    play sound "door.wav"
    play music "mall.mp3"
    show chibi_mc at slightright
    show chibi_alice at slightleft
    with easeinright
    window show
    
    "As soon as you leave your dorm with Alice, she hooks her arm through yours."
    "You instinctively freeze up, but she simply smiles at you."
    "You don't have the heart to push her away when she looks so happy to be out together."
    "And with your destination just across the street, it's not even worth the effort."
    "After crossing the road, you arrive at the place you've been wanting to visit for ages."
    window hide
    hide chibi_mc
    hide chibi_alice
    with easeoutleft

    scene arcade with fade
    show alice_base_buns at left
    show dress polkadot at left
    show alice normal at left
    show mc surprised at right
    with easeinbottom
    m "Huh. Not bad. This place has good variety."
    m "(They even have that old train game I played when I was ten!)"
    show mc slightsad
    m "(I've been wanting to come here for so long... Why did I stop myself?)"
    show mc sad
    m "(I wasted so much time...)"
    show alice happy
    a "Hey, %(player_name)s, you look distracted."
    show alice wink
    a "Perhaps you're thinking about... me?"
    show mc normal
    m "Sorry, I got lost in thought for a minute. This is the aracde. You play games-"
    show alice hime
    a "Aha! Games! I know {i}all{/i} about games. Strip poker, for instance-"
    show mc stressed
    m "{i}Aracde{/i} games. Clothes stay on. Please."
    show alice neutral
    a "Oh..."
    show alice flirtsweat
    a "Regardless! I'm such a fast learner, you can call me a Master before I've even tried it."
    show mc normal
    m "Hmm, I can see Bubble Bobble. You might like that one."
    show mc happy
    m "It was the first arcade game I ever played."
    show alice sly smile
    a "So, you want me to play this little game? Fine. I'll show you just how good I am with my hands~"
    show mc stressed
    m "(Why does it always have to be an innuendo?)"
    show black with dissolve
    "You supervise while Alice pops in a token, loads up the game and flies through the first few levels, laughing haughtily all the while."
    "She seems to be enjoying herself, but..."
    show alice annoyed
    show mc normal
    hide black with dissolve
    play sound "gameover.wav"
    a "What the..."
    show mc annoyed
    m "Welp, you lost."
    show alice disgusted
    a "LOST!? Me!?"
    show mc confused
    a "Yeah...?"
    show alice shocked
    a "Urk!"
    show alice flirt
    a "I mean!- I got distracted by you so close next to me, so that was a fluke!"
    show alice annoyed
    a "It doesn't count, got it?"
    show alice flirtsweat
    a "You were just... so... SO... distracting!"
    show mc surprised
    m "I was? Uh, sorry..."
    show mc awkwardsmile
    m "But I mean, you did decently, and it's your first time playing, so of course you won't be able to finish the entire game-"
    show alice disgusted
    a "Don't think so little of me! I'm perfect - remember that!"
    show alice serious
    a "Go and put more of those tokens in. I don't give up that easily!"
    show alice flirtintense
    a "I'll win this game and show you! HOW! GOOD! I! AM!"
    show mc shocked
    m "(She's intense!)"

    scene black with fade

    "Alice proceeds to play nothing but that one arcade game for the next two hours."
    "Children wanting to play it soon learn that waiting in line is futile."
    "It's fun to watch her try so hard. You play a some other games too, but Alice is so zoned in she doesn't even notice you there or not."
    "For the first time in a while, you feel actual entertainment. Not just a relief from sadness."
    window hide
    stop music fadeout 2

    #go home, assault scene, she snaps or not.

    #home:

    
    scene bottle_phone night with Fade(1, 1.0, 1):
        zoom 0.9 
    play sound "door.wav"
    play music "night.mp3 "
    show alice_base_buns at left
    show dress polkadot at left
    show alice sly smile at left
    show mc happy at right
    with easeinbottom

    m "I'm impressed you actually beat the game!"
    show alice hime
    a "I'm glad you appreciate all the effort I went to. Tenacity. Patience. Dexterity. Reaction time."
    a "These four qualities make up the perfect partner. Of course I would complete it."
    show mc annoyed
    m "Uh... I'm glad you enjoyed yourself."
    show alice sly smile
    a "Mhm~ That was a lovely date, %(player_name)s. And after you witnessed my power, I'm sure you're just dying to-"
    show mc normalsquint
    m "Hold up! A {i}date{/i}!? We agreed it was just as friends, remember?"
    show alice pout
    a "Don't be pedantic."
    show alice sly smile
    a "But if you like the friends-to-lovers tag so much, I suppose I can work with that too."
    show mc surprised
    m "What?"
    show alice laugh
    a "OHOHO! Are you finally realising it, %(player_name)s? I'm not just like any other girl."
    a "You can't discourage me that easily. I'm like a tiger whose caught scent of my prey."
    show alice vflirt
    a "And you..."
    show alice flirtsweat
    a "...certainly smell."
    show mc worried
    m "I'm so sorry. I wasn't expecting company and... ugh..."
    show mc stressed
    m "This is so embarrassing."
    show alice happy
    a "No need to feel embarrassed around me. I'm dying soon... anyway. Uh-"
    show alice flirtsweat
    a "What I mean is! Why not go take a shower now and I'll wait here?"
    show mc vannoyed
    m "You're not planning to follow me into the shower, are you?"
    show alice happy
    a "No. I have better things to do."
    show mc surprised
    m "You do? Oh... Alright then."
    show alice sly smile
    a "Wonderful. That way, you'll be clean when we'll go out again for our second date tomorrow."
    show mc confused
    m "But they're not-!"
    show alice wink
    a "A \"just-as-friends\" date."
    show mc stressed
    m "(She's totally lying, isn't she?)"
    m "Heading to the showers now. See ya."
    window hide
    hide mc with easeoutbottom
    play sound "door.wav"
    show black with dissolve
    window show
    # shower chibi?
    "One wonderfully uneventful shower later..."
    window hide
    hide alice_base_buns
    hide alice
    hide dress polkadot
    hide black with dissolve
    show mc happy at right with easeinbottom
    window show
    m "I have been reborn."
    show mc awed
    m "Alice...?"
    window hide
    show alice_base_buns at left
    show alice sly smile at left
    show dress polkadot at left
    with easeinbottom
    window show
    a "Welcome back, %(player_name)s. Enjoy your shower?"
    m "You... cleaned?"
    show alice hime
    a "Oh, I supposed I did. Why? Does it make you feel happy or something?"
    show alice sly smile
    a "Perhaps, grateful?"
    m "..."
    m "Y-yeah. It looks so much... better."
    show mc stressed
    m "I'm just sorry you cleaned up after me. You shouldn't have folded all those dirty clothes."
    show alice hime
    a "Good, because I didn't."
    show mc confused
    m "But... where did you put all my clothes?"
    show alice confused
    a "Oh, those dreadful rags? I just tossed them out the window."
    show mc shocked
    m "You didn't!"
    "She put your dirty-ass clothes on the pavement for everyone to see and smell?"
    "You can't collect them now! If you did, everyone would know who to be annoyed at!"
    show alice hime
    a "You're welcome."
    show mc stressed
    m "Well... I appreciate that you took the time to clean the room."
    show mc awkwardsmile
    m "But please don't do it again."
    show alice sly smile
    a "Who knows? If I have spare time, I might feel inclined to assist your insurmountable task of cleaning this wretched place."
    show mc stressed
    m "Ugh... I need to sleep. Today has been... a day."
    show alice flirt
    a "You have such a way with words, %(player_name)s. I just love a poetic man."
    show mc confused
    m "Thanks?"
    a "We should go to bed then, so you can sleep."
    
    "You head to bed, Alice right behind you, and get in."
    show alice pout
    a "Aw, could you scoot up a little please?"
    show mc surprised
    m "Ah, sure..."
    "You move up."
    show alice happy
    show mc confused
    m "..."
    show mc shocked
    m "Wait a second! Why are you in here with me!?"
    show alice surprised
    a "What do you mean? It's time for bed, isn't it?"
    show alice wink
    a "You said it yourself. You let me in here."
    show mc shout
    m "That's because you - you CONFUSED me!"
    show alice sly smile
    a "Did being in my proximity cloud your judgement? Get your heart racing? Maybe it's time to confess."
    show mc confused
    m "I don't know! All I know is that you're not staying in here!"
    show alice pout
    a "But %(player_name)s, I'll get lonely. And it's my first night of being here."
    show alice cutesad
    a "Put yourself in my shoes. You're such a kind man. I know you'll understand."
    show mc stressed
    m "Nope nope nope! After what you tried earlier, after what I've read about you, I know NOTHING good will come of this!"
    a "So I'm getting punished for following my instincts?"
    show mc vannoyed
    m "Yes. Get used to repressing your desires. That's life. I'm not comfortable with physical touch - you know this by now."
    show alice serious
    a "Only because you're a first-timer! They're all like that. After a little touching, you'll be addicted, I swear!"
    show mc normalsquint
    m "..."
    show alice sigh
    a "Ugh, so it came to this."
    show alice pout
    a "Fine. I'll compromise. What if I PROMISE... only to spoon you?"
    show mc confused
    m "How does that help? No!"
    show alice shocked
    a "N-not even spooning...? This is verging on neglect here!"
    show alice sad
    a "Please %(player_name)s! Cuddling, affection... it's like breathing to me! And I am suffocating after today's rejections. I need it!"
    show mc normalsquint
    m "..."
    show mc normalside
    m "Nope. I don't buy it. The only thing you need is water. Get out."
    show alice vcry
    a "%(player_name)s..."
    show mc stressed
    m "No more crocodile tears either!"
    "Realising that she's not going to leave on her own, you kick her out as gently as possible, and she lands right onto the desk chair."
    show alice pout
    show mc normal
    m "You know what, Alice? I just want a good night's sleep. I don't have the energy for this."
    m "I've got my laptop open right there. Why don't you face the screen and learn a little about the world?"
    m "Maybe then I won't have to explain every single concept to you."
    show alice cutesad
    a "But... how do I do that? I can't read."
    show mc awed
    m "Like this."
    "You lean over to operate the mouse."
    show alice normal
    show mc normal
    m "Look, you use the mouse to click on anything that looks interesting. *Click*. See? It's easy."
    show alice hime
    a "Hmph! As you wish. I'll try to educate myself so I can be the perfect partner for you."
    show mc normalside
    "You're so tired that you don't bother to correct her. Instead, you plop into bed."

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "You fall asleep to the faint humming of the laptop fan..."
    with dissolve 
    pause

    jump alice_d2_morning_badroute













label alice_d2_morning_badroute:

    window show
    a "{size=-20}Hey."
    window hide

    show bedroom_day with fade:
        zoom 0.9

    window show
    a "{size=-10}Hey~"
    window hide
    
    show day_2 at topleft
    with dissolve

    
    a "Hey hey~"
    play music "normal.mp3"
    window show
    a "Hey~ are you awake yet? Hey? Hey?"
    show mc stressed at right
    show alice_base_buns at left
    show dress polkadot at left
    show alice normal at left
    with easeinbottom
    m "Ugh..."
    show alice neutral
    a "Finally. You really know how to keep a lady waiting."
    m "*Groaning from sleepiness*"
    show alice flirt
    a "Aw, are you sleepy? Would you like a little... wake-up kiss?"
    show mc shocked at bounce
    m "I'm awake! I'M AWAKE!"
    show mc vstressed
    m "Uuuuuugh... it's so... early... Why'd you have to wake me up?"
    show alice hime
    a "Because I don't have time to waste!"
    show alice sly smile
    a "I spent all night planning the perfect outing for today. Every last detail, from location, to time, to event."
    show mc slightsad
    m "(A whole day of walking around outside? That sounds like hell!)"
    show alice pout
    a "Is gloomy your default? Come on, can't you be a little more enthusiastic?"
    show alice wink
    a "You'll have {i}me{/i} as your companion, after all, so it'll be the perfect time."
    show mc stressed
    m "(So much energy, so early...)"
    "But if she DID \"spend all night planning the perfect itinerary\"... some enthusiasm is the least you can do, right?"
    "She won't have many chances to go out. Tomorrow is her last day"
    show mc vstressed
    m "...Woohoo..."
    show alice sigh
    a "Hah. I appreciate the effort."
    show alice vflirt
    a "Hey... I'm feeling thirsty. Now that you're up, why don't you grab your bottle and put something wet in my mouth?"
    show mc confused
    m "Just to confirm, you're talking about water, right?"
    show alice sly smile
    a "Of course! What else could I possibly be talking about?"
    window hide
    hide mc with easeoutbottom
    $ watered = 1
    show water_status at topright with dissolve

    call screen water_alice_d2_badroute
        

    screen water_alice_d2_badroute:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("watered_alice_d2_badroute")

    label watered_alice_d2_badroute:
        queue sound "spray.wav"
        $ watered = 2
        pause 1
        queue sound "spray.wav"
        $ watered = 3
        show alice flirt
        window show
        "Alice leans into the mist, sticking her tongue out."
        window hide
        show mc normal at right with easeinbottom
    m "Thirst quenched?"
    show alice hime
    a "It'll keep me at bay."
    show alice happy
    a "Alright! Before we go, I'm gonna comb your hair a little. I want you feeling extra comfortable today."
    show alice wink
    a "And don't forget your wallet, okay? We're gonna need it."

    window hide
    stop music fadeout 2
    scene black with Fade(0.5, 1.0, 0.5)        
    play sound "door.wav"
    play music "mall.mp3" fadein 2
    show chibi_mc at slightright
    show chibi_alice at slightleft
    with easeinright
    window show
    
    "After helping you get ready, Alice grabs your hand and leads you out the dorms at a brisk pace."
    "The instant you're out on the bustling street, the reality of what you're doing sets in and you start to panic a little."
    "Thankfully, Alice seems to know where she is going, so you can just focus on breathing slowly to calm down."
    
    window hide

    hide chibi_mc
    hide chibi_alice
    with easeoutleft

    scene mall with Fade(0.5, 1.0, 1)
    show mc worried at right
    show alice_base_buns at left
    show alice excited at left
    show dress polkadot at left
    with easeinbottom
    a "Wow... This place is even grander than the video!"
    m "It's so busy..."
    show mc stressed
    m "So what are we doing at the mall, Miss Event Organiser?"
    show alice sly smile
    a "I'm glad you asked. We're doing the top three things to do on a date-"
    show mc normalside
    m "(We agreed it wasn't a date yesterday! I knew she wasn't listening. Welp, I tried.)"
    show alice happy
    a "And first is... trying on clothes!"
    show mc confused
    m "Trying on clothes?"
    show alice wink
    a "Well? Aren't you excited? You'll get to see me dress up in whatever you want."
    show mc normal
    m "..."
    show mc normalside
    m "(I hate clothes shopping. Always takes so long.)"
    show alice pout
    a "..."
    show alice hime
    a "Ha! Well! Anyway! I'll just pick the first clothes store then!"
    show alice happy
    a "Ohh~ this one looks cute!"
    window hide
    scene clothes_shop with fade
    show mc normal at right
    with easeinbottom
    window show
    a "Oh %(player_name)s, I think I've found two outfits that will make your jaw drop~"
    a "Prepare your heart... for outfit number one!"
    window hide
    show alice_base_buns at left
    show dress sexy at left
    show alice sly smile at left
    with easeinbottom

    show mc surprised
    window show
    a "I think this dark colour looks so good on me, don't you think?"
    show alice flirt
    a "And this really accentuates my curves."

    show mc blushside
    m "Yeah... but, like..."
    m "Isn't that too revealing?"
    show alice laugh
    a "Aw, you're so considerate, %(player_name)s."
    show alice vflirt 
    a "But don't be shy. I want to hear it from your lips: You like this dress, right?"
    show mc worried
    m "Um, what's the other outfit?"
    show alice happy
    a "Too excited to wait, are you? Well, just a minute~"
    hide alice
    hide alice_base_buns
    hide dress 
    with easeoutbottom
    show mc stressed
    m "(I should have expected this...)"
    m "(I just have to endure...)"
    "Or... you could enjoy it. She's attractive. She likes you. What's the problem?"
    "Are you just coy? Shy?"
    show mc slightsad
    m "(Maybe I just don't know how to respond. Nobody acted like this to me before.)"

    a "Alright~ here I come!"
    show mc normal
    window hide
    show alice_base_buns at left
    show dress plain at left
    show alice happy at left
    with easeinbottom
    show mc surprised

    window show
    a "I thought that someone as innocent as you might like the pure look more, so I took a gamble."
    a "Do you like it?"
    m "..."
    show alice flirt
    a "Speechless?"
    show mc awed
    m "It... uh... looks really good on you."
    show alice surprised
    a "Really? You like this? You think I look cute?"
    show alice sly smile
    a "So I was right?"
    show mc blushside
    m "..."
    show alice happy
    a "So which one did you like most? The first or the second dress?"
    show mc normalside
    default outfit_choice = "images/sprites/alice/dress polkadot.png"
    image outfit = "[outfit_choice]"

    default outfit_neither = False
    jump choose_dress_menu
label choose_dress_menu:   
    menu:
        "Which did I like most?"
        "The first dress.":
            if outfit_neither:
                $ outfit_neither = False
            $ outfit_choice = "images/sprites/alice/dress sexy.png"
            show mc awed
            m "First dress. It's... uh..."
            show mc blushside
            m "It looks good on you. I mean, so does the other one, but-"
            show alice sly smile
            a "Then may I get this, %(player_name)s?"
            show mc happy
            m "Yeah, if you want it."
            

        "The second dress.":
            if outfit_neither:
                $ outfit_neither = False
            $ outfit_choice = "images/sprites/alice/dress plain.png"
            show mc awed
            m "The second dress. I think..."
            show mc blushside
            m "It looks good on you. I mean, so does the other one, but-"
            show alice sly smile
            a "Then may I get this, %(player_name)s?"
            show mc happy
            m "Yeah, if you want it."
        
        "Neither.":
            if outfit_neither:
                show mc worried
                "You don't know. Which one? Which one?"
                "The more you try to pick, the more your heart races, the more frozen you feel..."
                "You've always had the wrong taste in clothes, and you always will."
                "Rather than extend this situation, just end it."
                show mc stressed
                m "Sorry. Just pick whatever you want."
                show alice sad
                a "..."
                show alice cutesad
                a "Does nothing suit me?"
                show mc surprised
                m "No, it's just...."
                show mc normalside
                m "I'm just not good at picking clothes."
                show alice worried
                a "So you're mad at me?"
                show mc confused
                m "Mad? No! Where'd you get that idea from?"
                show alice happy
                a "I misunderstood then. For a second, I thought..."
                show alice flirtsweat
                a "Let's just get out of here!"

            else:
                $ outfit_choice = "images/sprites/alice/dress polkadot.png"
                $ outfit_neither = True
                show mc slightsad
                m "Alice, I don't know. I'm not stylish. Don't ask me."
                m "You choose."
                show alice pout
                a "But I want YOU to pick."
                show alice happy
                a "Come on, don't look so sad. This is meant to be fun."
                a "There's no wrong answer. Just tell me honestly."
                jump choose_dress_menu
            

    


    scene mall with fade
    show alice_base_buns at left
    show outfit at left
    show alice normal at left # show her in the outfit
    show mc normal at right
    with easeinbottom
    m "At least that didn't take too long. So what's next on the list?"
    show alice flirt
    a "Getting excited now? That's what I like to see. Next up is..."
    show alice happy
    a "... the cafe!"
    show mc shocked
    m "The cafe...? Oh no..."
    show mc worried
    m "As in, we're going inside?"
    show alice laugh
    a "Precisely. We'll go inside, you'll eat and replenish your energy."
    a "I know aaaaaaall about you humans and how you'll get grumpy if you miss your meals."
    show alice smug
    a "Don't think I haven't noticed you skipping your meals."
    show mc stressed
    m "That's nice of you, Alice, but I'm not really a cafe kind of guy."
    show alice hime
    a "I know, I know! You get a little shy sometimes, but that's part of your charm. I don't mind."
    show mc worried
    m "Uh, I don't know..."
    show alice flirt
    a "Hush! Leave all the talking to me. I'll take good care of you, okay?"
    window hide
    stop music fadeout 2
    scene mallcafe with fade
    play music "mallcafe.mp3"
    show mc worried at right
    show alice_base_buns at left
    show outfit at left
    show alice happy at left
    with easeinbottom
    window show
    m "You're sure you know what to do?"
    show alice hime
    a "Of course I do. I prepared meticulously for today."
    show alice smug
    a "Nothing can go wrong, not even if you tried."
    window hide
    show waiter normal at center with easeinbottom
    window show
    w "Welcome. Can I get you guys a table?"
    show alice happy
    a "Yes, please."
    w "Alright, this way please."
    window hide
    hide waiter with easeoutbottom
    window show
    show alice smug
    a "See? It's going exactly as the video foretold. I've got everything under control."
    
    show black with dissolve:
        alpha 0.5

    "You are escorted to a large table, with 2 chairs on one side, and couch seat built against the wall on the other."
    "Alice gestures for you to have the couch seat, and sits opposite you."

    default food_neither = False
    show mc normal
    show alice happy

    hide black with dissolve
    a "So, see anything you like?"
    menu:
        "Do I want to eat anything?"
        "Grilled cheese!":
            show mc happy
            m "The grilled cheese sandwhich looks pretty good."
            show mc normal
            m "And you? Gonna order anything for yourself?"
            a "How considerate of you to ask. But I don't need to eat. All I need is a glass of water."
            show mc confused
            m "You sure? But..."
            show mc slightsad
            m "That doesn't sound very fun for you."
            show alice hime
            a "Oh? I disagree."
            show alice flirt
            show mc blushside
            a "I quite look forward to watching your lips close around your meal, and seeing the expression of gluttonous pleasure-"
        "I don't have an appetite.":
            $ food_neither = True
            "Spending money, eating food, enjoying being out..."
            "That's what Alice wants of you. But she doesn't understand."
            "But every second you're here, in the mall, being seen, you feel a shame you cannot ignore."
            "Everyone else looks like they are doing better than you."
            "You shouldn't be here."
            show mc slightsad
            m "I... I don't know. I don't have much of an appetite."
            show mc stressed
            m "You just get whatever you want."
            show alice worried
            if clothes_neither:
                a "Again?"
                show mc normal
                show alice sad
                a "You didn't like the dress, and now..."
                show alice vcry
                show mc shocked at bounce
                a "Am I just messing everything up?"
                show mc worried
                m "Please don't cry! I'll get something! Just don't make a scene, please!"
                a "But-"
                show mc surprised
                show alice surprised
                m "The grilled cheese! That looks super good!"
                show mc happy
                m "Haha, I can't wait! I'm so excited to eat it!"
                show mc annoyed
                m "Thank you for recommending this place, Alice! Great choice!"
                show alice sadsmile
                a "It was? I'm glad to hear that..."
                show alice worried
                a "I'm sorry for crying. I was just-"
                show mc happy
                m "No problem!"
                show mc awkwardsmile
                m "Just, uh, do you think you can still place the order?"
                show alice hime
                a "Of course! As I said earlier, I prepared for today! I spent hours researching the proper etiquette!"
                show mc stressed
                m "(Phew. She's smiling again. Crisis averted.)"
            else:    
                a "Is something the matter? Am I upsetting you? Just tell me if I am, otherwise, I can't improve anything for you."
                show mc normalside
                m "You're fine, Alice. It's just me being stupid again."
                show alice pout
                a "I can agree with that. You should really eat, you know!"
                a "I won't allow you to just ignore your needs. Come on! Pick something! You'll feel better. It's an order."
                show mc normalisde
                m "Ugh, I guess... the grilled cheese."
                show alice laugh
                a "Wonderful!"
    window hide
    show waiter normal at center with easeinbottom
    show mc worried
    w "Uh... hey... you ready to order?"
    show alice smug
    a "Why yes, we are! My partner will have the grilled cheese sandwich and I'll have a glass of water."
    show mc surprised
    m "(Partner!?)"
    show mc blushside
    m "(Argh, she did that on purpose, didn't she?)"
    w "Still or sparkling?"
    show alice confused
    a "..."
    show alice hime
    a "Sparkling, of course."
    w "And is that all?"
    a "Mhm, thank you darling."    
    window hide
    hide waiter with easeoutbottom
    show mc normal
    m "(She handled that way better than I could have.)"
    m "..."
    show alice sly smile
    a "Yes?"
    show mc annoyed
    m "Do you even know what sparkling water is?"
    show alice flirtsweat
    a "...I know I WANTED it."
    show alice hime
    a "A sparkling water, for a sparkling girl."
    show mc happy
    m "You seem confident, but not everyone likes it."
    show alice smirk
    a "Is that a challenge? I'm not just anyone. I'm perfect, remember?"
    m "Whatever you say. But if you don't like it, I'll finish it for you."
    show alice wink
    m "You'll \"finish\"? Oh my."
    
    if outfit_neither and food_neither: #Leads to bad route
        show mc stressed
        m "..."
        show alice normal
        a "..."
        show alice sadsmile
        a "Are you enjoying yourself, %(player_name)s?"
        show mc surprised
        m "Me?"
        show mc awkwardsmile
        m "Yeah! I'm okay!"
        show alice worried
        a "Just \"okay\"?"
        m "I'm good! I'm just feeling tired. The mall isn't really my scene."
        show alice cutesad
        a "*Sigh* So we shouldn't have come here..."
        show alice flirtsweat
        a "No, it's too soon to give up! We still have another place! It's the best!"
        window hide
        scene black with fade
        "You scarf down your food, eyes darting around the cafe, taking in every movement."
        "Alice watches you intensely. You force a smile every now and then."
    
    else:
        show mc annoyed
        m "Heh."
        "You finally laughed to one of her dirty jokes. It only took a day."
        show alice flirt
        a "You're smiling, %(player_name)s. Are you perhaps enjoying our date?"
        show mc blushside
        m "I told you-"
        show alice laugh
        a "Oh, come on! Fine, our not-a-date date, then. I'm just teasing you."
        show alice sly smile
        a "But really, tell me. Are you liking everything so far?"
        show mc normal
        m "It's been a while since I went to the mall. Honestly, I thought I'd hate it. I usually avoid it, since I'm not so good with busy places..."
        show mc happy
        m "But with you, it helps knowing I can depend on you if I get overwhelmed."
        show mc annoyed
        m "As much as I hate to bolster your ego even more, you've done pretty well."
        show mc happy
        m "So yeah. Thanks. It's been fun."
        show alice laugh
        a "OHOHOHO! Of course. All according to plan."
        show mc confused
        m "Alice, why are you being so nice to me?"
        show alice smirk
        a "Why else? It's so that I..."
        show alice cruel
        a "... can worm my way into that guarded heart of yours! OHOHO!"
        show alice smug
        a "And there's still so much in store for us, hehe~"
        show mc happy
        m "Alright. I am unironically looking forward to it."

        window hide
        scene black with fade
        "You enjoy eating at the cafe while Alice chats to you, teasing, joking, giving you reasons to grin."
        "The music is calm. You don't have to say a word to the waiter even once. The food is hot, cheesy and comforting."
        "With no reason to worry, you let yourself enjoy the moment."

    stop music fadeout 3
    "After you pay the bill, Alice takes you to the next phase of her plan."
    m "We're leaving the mall?"
    a "Mhm~ I've got something special planned for us."
    scene enbankment with fade
    play music "cliff_date.mp3"
    show mc awed at right
    show alice_base_buns at left
    show outfit at left
    show alice happy at left
    with easeinbottom
    m "I never knew how close I lived to a river."
    show alice happy
    a "Yeah, it seemed so romant-"
    show alice flirtsweat
    a "Ahem! So {i}wonderful{/i}, I wanted to see it with you."
    window hide
    
    hide outfit
    hide alice_base_buns
    hide alice
    with easeoutbottom
    window show
    "Alice sits down on the grassy hill facing the river, then looks up at you and pats the ground next to her."
    a "Sit with me?"
    if not outfit_neither and not food_neither:
        show mc happy
        m "Yeah."
    else:
        show mc stressed
        m "Fine."
    window hide
    hide mc with easeoutbottom
    window show
    "You both watch the orange light reflect on the river."
    "The warm wind fingers your hair, and, for a long moment, you close your eyes..."
    if outfit_neither and food_neither:
        "The suffering of the day flashes past your mind. All the things you should have done, but couldn't, echo with shame in your head."
        m "(I'm never going to get better, am I? I'm always going to miss out on fun because of my anxieties.)"
        m "(I wish I could enjoy life.)"
        "But instead, it feels like it's slipping through your fingers."
        
        

        hide black with dissolve
        show alice_base_buns at left
        show alice outfit at left
        show alice sad at left

        show mc confused at right
        with easeinbottom
        m "Alice, are you okay?"
        show alice flirtsweat
        a "Oh! Me? Of course!"

        show mc sad
        m "Alice, I know I've been acting distant today. My anxiety has been really tough lately, and... I'm sorry."
        show alice surprised
        m "You're apologising? But... it was my fault you had to go out today."
        show mc stressed
        m "No, how I react is not your fault."

        m "I don't know why you're wasting your time on me."
        m "I just hope that you were able to enjoy yourself today."

    


    else:
        show black with dissolve
        "And you think of nothing."
        "..."
        play sound "bird.wav"
        "You hear the birds. You feel the long grass under your hands. You feel the late afternoon heat against your face."
        "..."
        ".."
        "."
        a "Hey, %(player_name)s... The sun's about to set."

        # Chaos scene - Zeynep's idea:
        hide black with dissolve
        show alice_base_buns at left
        show outfit at left
        show alice flirt at left

        show mc happy at right
        with easeinbottom

        a "I really hope you enjoyed today's outing~"
        a "I tried to think of things you would like, so I hope it made you happy."
        show mc confused
        m "(She thought of things {i}I{/i} would like? When she's the one dying tomorrow?)"
        "As soon as you think that, that sentence won't go away."
        "She's dying tomorrow."
        "You're not ready. Hell, she probably isn't either."
        "But it's going to happen. You can't do anything to stop it."
        "And yet, right now, you're sitting here, having a fun time, smiling like nothing's wrong?"
        "You should be ashamed of yourself. What have you done for Alice today?"
        a "Well? Are you still happy?"
        show mc surprised
        m "Definitely, but-"
        show alice laugh
        a "Perfect, exactly as expected."
        show alice sly smile
        a "And you can expect that from me in every way."
        show mc sad
        m "Alice, can we talk more seriously for a second? Are YOU actually enjoying yourself?"
    
    
    show alice happy
    a "Of course. I'm watching the sunset with my wonderful partner. What could be more perfect than this?"
    show mc normal
    m "..."
    show mc sad
    m "It's just that... you said you planned today around me."
    show mc slightsad
    m "But what about you? We should have just done something {i}you{/i} wanted."
    show alice sly smile
    a "No, we still did what I wanted. Because doing whatever you want to do, IS what I want to do."
    show alice laugh
    a "It's literally why I was made."
    show mc stressed
    "She laughs like it makes perfect sense, but last last comment twists your stomach."
    m "Alice, who cares why you were made?"
    show mc sad
    m "You can have your own goals. You only get one life."
    show alice sly smile
    a "You're such an empathetic man, %(player_name)s. Such a sweetheart."
    show alice happy
    a "I've always known what I wanted. I know what success means to me. And it's you."
    m "(But that also puts a lot of pressure me then too, doesn't it?)"
    show mc awed
    m "You should think about what you want to do with your last day tomorrow."
    show mc normalside
    m "Because I'm scared you don't understand what's going to happen."
    show mc stressed
    m "You're going to die."
    show alice serious
    a "You're the one who doesn't understand."
    show alice normalside
    a "You bought me. I'm a product. Nothing more than that."
    show alice smug
    a "And I'm quite happy to be one. See?"
    show mc shout
    m "You have opinions, you can talk, you have feelings. You're not a product- You're a person!"
    show alice flirtsweat
    a "Hey~ It's getting kinda heated, and not in the good way. What's the point in spoiling this nice time with fighting?"
    show mc sad
    m "(But it's important...)"
    show alice laugh
    a "Let enjoy this beautiful sunset, just like you wanted."
    show alice flirt
    a "And if you want to hold my hand at any point, which I'm sure you will, no need to ask."
    show alice happy
    show mc stressed

    "You can't bear the feeling that she's making a mistake. Why is she so stubborn? What can you say to convince her?"
    "Maybe someone else could have, but you're not good enough. And because of that inadequacy, you fail to help Alice in the way she deserves to be helped."
    "You feel guilty."
    "Maybe you SHOULD just hold her hand, just to make it up to her. It's the only thing she wants..."
    "You're the only one who can give it to her."
    "This decision is like choosing whether Alice gets to be happy or not."
    "After all she's done, doesn't she deserve it?"
    show alice_affection at topright with dissolve
        
    menu:   # Remove option - if you rejected all her previous stuff today, it locks you in the worst ending + she's paranoid. Else, you get more happy time with her.
        "Hold her hand." if not outfit_neither and not food_neither:
            $ alice_rp += 10
            show mc sad
            m "(I just want her to be a little selfish in the time she has left.)"
            m "(And if this is all I can do for her, then...)"
            "But can you physically do it?"
            hide alice_affection with dissolve
            show mc worried
            m "(Okay, go! Move, hand! Come on! Just! Do! It!)"
            show mc stressed
            m "(Damn it! This is scarier than I expected. I feel really embarrassed for some reason...)"
            "Hah. You are pathetic, and everyday, you just prove my point."
            show mc normal
            m "(No! It's for Alice! Failure isn't an option!)"
            "You rush in and snatch Alice's hand!"
            show alice shocked at bounce
            show alice_base_buns at bounce
            show outfit at bounce
            show mc shocked at bounce
            a "AH!"
            show alice surprised
            a "Oh? You're holding my-"
            show alice laugh
            a "Haha! That was your attempt at holding my hand?"
            show mc awkwardsmile
            m "Yeah... sorry... I don't have any experience in any of this stuff. Should I stop?"
            show alice sly smile
            a "Nope, I won't let you. You're trapped now."
            "Her hand interwines with your's tightly."
            show mc surprised
            m "What are you, a Venus flytrap?"
            show alice hime
            a "Hmph! Well, I am something of a goddess of beauty."
            show alice pout
            a "You shouldn't call yourself a fly, though."
            show mc annoyed
            m "Uh, thanks?"           
            show mc happy
            show alice sly smile
            "You both stare at the river as the sun dips into it..."

        "Tell her you'll never love her the way she wants." if outfit_neither and food_neither:
            stop music fadeout 3
            $ alice_rp -= 30
            m "(Even if it's for her, even if she did this for me, even if she's dying soon, even if she can't help it...)"
            show mc sad
            m "(I don't feel that way about her. The longer she allows herself to believe it, the worse everything will be.)"
            hide alice_affection with dissolve
            m "(I don't want to lead her on. I can't.)"
            show mc stressed
            m "(But I do I have to feel like such a prick for it?)"
            m "Alice."
            show alice sly smile
            a "%(player_name)s?"
            m "(Like you're ripping off a bandage. Make it hurt, but only for a second.)"
            show mc sad
            m "I still don't like you. I never will."
            show alice shocked
            a "..."
            a "Where is this coming from? Did I do something wrong?"
            a "If you tell me, I'll make it right-"
            m "You didn't do anything wrong. Sometimes, people aren't attracted to others in a sexual or romantic way."
            show alice worried
            a "Was it my freckles?"
            show mc surprised
            m "Y-your... freckles? No. Not all."
            show alice sad
            a "Was it... my chubby face?"
            show mc confused
            m "What? No! I'm just not interested in you that way."
            show mc sad
            m "And that's okay. I just don't want you to waste your time. I still want to be friends-"
            show alice angry at quiver
            show mc shocked at bounce
            a "{sc=3}{size=+40}{color=#000000}DON'T YOU DARE FRIENDZONE ME!"
            show alice angry tears
            a "After everything I've done! After I spend ALL MY TIME trying to make you happy!?"
            a "HOW CAN YOU SAY THAT TO ME!? AM I STILL NOT GOOD ENOUGH?"
            show mc worried
            m "You ARE good enough!"
            show alice angry
            a "BULLSHIT! Nothing I do is EVER good enough for you! The whole of today, you haven't enjoyed the date ONCE!"
            a "YOU PUSH ME AWAY! NO MATTER WHAT!"
            a "WHAT ABOUT ME MUST I CHANGE FOR YOU TO ACCEPT ME!?"
            show alice vvdespair
            a "JUST TELL ME! I'LL DO ANYTHING! I SWEAR IT!"
            a "..."
            m "..."
            show mc cry
            m "I'm sorry..."
            show alice vannoyed
            a "..."
            show mc confused
            m "..."
            show alice happy
            a "Phew. Sorry for exploding. I'm okay now."
            show mc surprised
            m "You're... \"okay\"?"
            a "Mhm! Everything's okay. That never happened."
            show alice wink
            a "Because there's still time! I haven't failed yet, so don't say it's over \'til it's over."
            show mc worried
            m "(She must been really stressed...)"
            jump alice_worstending



label alice_d2_night_badroute:
    window hide
    stop music fadeout 2
    scene black with fade
    window show
    "After the sun sets, you and Alice make your way back home."

    scene bottle_phone night with fade:
        zoom 0.9
    play music "night.mp3"
    show day_2 at topleft
    show alice_affection at topright
    with dissolve

    show alice_base_buns at left
    show outfit at left
    show alice sly smile at left
    show mc normal at right
    with easeinbottom

    a "Was that great or what?"
    m "What."
    show alice pout
    m "..."
    show mc annoyed
    m "Just joking."
    show mc happy
    m "It was fun. Thanks, Alice."
    show alice smirk
    a "Hah! Of course it was. Just as I predicted. I've got you all figured out, %(player_name)s. You're welcome."
    show alice sigh
    a "Ah, wow, my back kinda hurts..."
    show mc annoyed
    m "Why? Old age?"
    show alice sulk
    a "No."
    show mc surprised
    m "I was just joking."
    show alice worried
    a "Do I have wrinkles showing? Am I still pretty?"
    show mc confused
    m "You wouldn't get wrinkles, would you? You're a mushroom!"
    show alice sigh
    a "I'll take that as a no. Phew~" 
    show mc normal

    m "So... Alice. How will tomorrow work exactly? Do you know how you actually die, like from your mushroom memories?"
    show alice serious
    a "What a morbid question."
    show mc surprised
    m "It's important though."
    show alice vannoyed
    a "Fine. I'll explain. I just know that by tomorrow, I'll keep withering up, until I can't move, and eventually die."
    show alice cutesad
    a "Ugh. I'm going to look so gross..."
    show mc confused
    m "Okay. And, um, how do you feel physically, right now?"
    show alice flirt
    a "Horny."
    show mc annoyed
    m "Ugh, you know what I mean!"
    show mc confused
    m "Do you hurt anywhere?"
    show alice laugh
    a "Only in my heart, darling."
    show mc normal
    m "Well if you feel good enough to joke, you must be fine."
    show mc normalside
    m "(Though I do wish she'd be serious for once.)"
    show mc sad
    m "Alice, I can stay up a bit later tonight - Is there anything you want to do that I can help you with?"
    show alice flirt
    a "I-"
    show mc stressed
    m "And don't say THAT."
    show alice pout
    a "But it's true! Is it so wrong? I don't get it."
    show alice hime
    a "You said you needed time, and I gave that to you."
    show mc normal
    m "Anyway..."
    show alice sigh
    a "Ignoring me now?"
    show mc happy
    m "Hey, you'll do anything I ask you to, right?"
    show alice hime
    a "Of course! Anything is on the table. And I mean anything."
    show mc annoyed
    m "Good. Then... I want you to think about what you've done outside for the last two days."
    show alice confused
    a "Okay..."
    show alice vannoyed
    a "Hmmmm~ Alright, I'm thinking about it. Now what?"
    show mc happy
    m "Now, when I say the word \"fun\", what's the first image that pops into your mind?"
    a "Mall."
    m "And the second one?"
    a "Um... the sound of the arcade."
    show mc confused
    m "The sound? Like, the general noises of the arcade?"
    show alice cute
    a "No, no! There was this cute jingle in the game I was playing, going on and on the whole time."
    a "It goes like do-do-do, do-do! Da-dee-dee, doo-ba-doo-ba-dooooo~"
    show mc surprised
    m "Whoa, you sing nicely."
    show alice sigh
    a "Thanks. It's actually been stuck in my head ever since. It's catchy, but man, it's getting kind of annoying."
    show mc annoyed
    m "Yup, having songs stuck in your head can do that to you."
    show mc happy
    m "I can play it for you on my laptop, if you'd like. Sometimes listening to it again can help you get it out."
    show alice flirtsweat
    a "I-I don't want to take up your time just for me-"
    show mc normal
    m "What if I say it's what I want to do?"
    show alice normal
    a "..."
    show alice sigh
    a "Ah... fine..."
    window hide
    hide mc
    hide alice
    hide alice_base_buns
    hide outfit
    with easeoutbottom
    window show
    "You search for the arcade music and play it out for Alice, who immediately starts bobbing her head to the music, eyes closed."
    "After the track ends, you queue a bunch of your favourite game songs."
    "With that playing in the background, you play some cards you find laying around."
    "But you're not prepared for Alice's competitiveness."
    "Despite having only been alive for 2 days, she's somehow way better at playing Old Maid than you."
    show alice_base_buns at left
    show outfit at left
    show alice laugh at left
    show mc happy at right
    with easeinbottom
    a "OHOHOHO! I win! You know what that means, %(player_name)s~"
    show mc annoyed
    m "*Sigh* Sure, I'll take off my right shoe if that makes you happy."
    show alice shocked
    a "Wait a second. Why am I winning? I should be losing!"

    
    window hide
    hide mc
    hide alice
    hide alice_base_buns
    hide outfit
    with easeoutbottom

    window show
    "Despite saying that, she keeps on winning, and you end the game after the socks come off."
    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "Feeling at peace, you drift off..."
    with dissolve 
    pause 3

    jump alice_d3_morning_badroute

label alice_d3_morning_badroute:

    scene bottle day
    with fade
    $ watered = 0
    show day_3 at topleft
    show alice_affection at topright
    show water_status at water_location
    with dissolve

    window show

    "It's the last day."
    window hide
    show mc normal at right with easeinbottom
    window show
    "That's the first thing you think of."
    "You get one more day of happiness, and then everything ends."
    "Alice dies. You'll lose the closest friend you've had for years. You'll wake up alone again. Everything will resume, the same as it was before."
    "Like it was all a dream."
    show mc stressed
    m "(I don't want this to be over. I wish she had more time.)"
    "But it's natural. It's life. It'll be over for you too, one day."
    show mc sad
    m "(Why does everything have to end?)"
    show alice_base_buns at left
    show outfit at left
    show alice sly smile at left
    show mc shocked at bounce
    play music "normal.mp3"
    m "{size=+20}ALICE!?"
    a "Mmm, good morning, %(player_name)s. Sleep well?"
    show mc vshout
    m "{size=+20}WHAT ARE YOU DOING IN MY BED!?"
    show alice wink
    a "Don't tell me you've forgotten what happened last night?"
    show mc shout
    m "Nothing happened. We just played cards and listened to music!"
    a "And what about {i}after{/i} you fell asleep? Hmmmmmm?"
    show mc surprised
    show alice flirt
    a "When you put your arms around me? When you cuddled me?"
    show alice hime
    a "OHOHO! I got my spoon in the end!"
    show mc vblushside
    m "But, I was sleeping! That's not fair!"
    show alice sly smile
    a "Really? You seemed to REALLY enjoy it."
    show mc vstressed
    m "..."
    show mc normalside
    m "Fine. I'm happy you got something you wanted."
    show alice surprised
    m "Oh, less resistance than I expected."
    "You get out of bed and reach for your spray bottle."
    window hide
    hide mc with easeoutbottom
    call screen water_5
    
    screen water_5:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("alice_day3_badroute1_watered")

    label alice_day3_badroute1_watered:
        play sound "spray.wav"
        $ watered = 1
        pause 1
        play sound "spray.wav"
        $ watered = 1
        show mc normal at right with easeinbottom
        show alice wink
        window show
    a "Mm, nice and wet."    
    hide water_status with dissolve
    show mc happy
    m "Heh. That's what she said."
    show alice sly smile
    a "Mhm, I did."
    "You're not even TRYING to deny these immature jokes anymore!"
    show mc normalside
    m "(I may as well enjoy them. People always say, the thing that most annoyed you about a person is what you'll miss most when they're gone.)"
    show mc happy
    m "Hey, Alice. I saw an advert in the mall... Would you like to go to a live music show together this afternoon?"
    m "It's when musicians gather in a single place, like a club or a bar, and perform their songs for everyone to hear."
    show mc awkwardsmile
    m "There'll be a variety of genres, so I thought... you might like it?"
    show alice surprised
    a "..."
    show alice confused
    a "You're offering to go OUTSIDE, for me? After being outside all of yesterday? You?"
    a "I thought you'd feel more comfortable staying inside."
    show mc normalside
    m "I don't really care about feeling comfortable today."
    show alice normal
    a "You don't care about all the people?"
    show mc worried
    m "N-no... Not at all."
    show alice pout
    a "%(player_name)s, you're not fooling me."
    show mc shout
    m "I'm just doing what you did for me, okay?"
    show mc normal
    m "Yesterday, I just needed to dip my toes into the waters of the outside. And it's not as freezing as I thought, so..."
    show mc happy
    m "So I wanna go. I always have. I've just been too scared."
    show mc normalside
    m "And... I might not have the strength to go alone, after you're gone."
    show mc cute
    m "So it's a win-win, see?"
    show alice sly smile
    a "Hmm, you sneaky thing. Fine."
    show mc annoyed
    m "Yes!"
    show mc happy
    m "Okay, I'm going to get showered and ready for the day."
    show alice surprised
    a "You're washing yourself? Oh my, I've been an even better influence than I thought!"
    show mc blushside
    m "I just thought I should try keep it up."

    window hide
    hide mc
    hide alice
    hide outfit
    hide alice_base_buns
    with dissolve
    stop music fadeout 2
    scene black with Fade(0.5, 1.0, 0.5)        

    play sound "door.wav"
    
    show chibi_mc at slightright
    show chibi_alice at slightleft
    with easeinright
    window show
    
    "After cleaning up and eating some breakfast noodles, you and Alice head out."
    "Once again, as soon as you leave the dorms, she hooks her arm through yours. Instead of feeling embarrassed, you relish in this temporary feeling."
    "By the end of tonight, you won't be able to feel it again."
    "You just try to push away every thought of fear, and instead appreciate every bit of the day." 
    "Finally, you arrive at the music venue."

    window hide
    hide chibi_mc
    hide chibi_alice
    with easeoutleft
    
    scene music_club with fade
    play music "mall.mp3"
    show alice_base_buns at left
    show outfit at left
    show alice excited at left
    show mc shocked at right
    with easeinbottom
    a "Whoa! There are so many people here!"
    show mc stressed
    m "That's for sure."
    show alice surprised
    a "All the ladies here look so gorgeous! Their faces looks so... much more {i}vibrant{/i} than mine."
    show mc normal
    m "Probably just make-up."
    show alice worried
    a "Am I dressed well enough? Maybe I should go home and change-"
    show mc awed
    m "What are you talking about? You're gorgeous too!"
    show alice surprised
    a "..."
    show alice pout
    a "Really?"
    show mc blushside
    m "Well... Um, we should join the line for a table!"
    window hide
    hide mc
    with easeoutbottom
    show alice sigh
    window show
    a "..."
    window hide
    hide alice_base_buns
    hide outfit
    hide alice
    with easeoutbottom

    window show
    "You wait in line for a few minutes, trying to acclimatise to the energetic atmosphere of the club."
    "You feel way out of your depth, even though many of the other people here look around your age."
    "However, every time to start to doubt coming here, you just glance at Alice."
    "For once, she's not looking at you, but staring at everything around her excitedly."
    "Eventually, you're taken to one of the tables near the stage."

    show music_stage with dissolve
    stop music fadeout 3
    announcer "Okay ladies and gentlemen, and those in between!"
    announcer "First up, I want you all to give a warm welcome to a very special up-and-coming band -"
    announcer "Vicious Fish!"
    
    a "Pfft!"
    window hide
    hide music_stage with dissolve
    show alice_base_buns at left
    show outfit at left
    show alice laugh at left
    show mc happy at right
    with easeinbottom
    window show
    a "What a ridiculous name!"
    show mc annoyed
    m "What? It's so good! It's stupid, it's got assonance... it's perfect."
    show mc happy
    m "Let's see what kind of music they play."
    window hide
    show music_stage with dissolve
    window show

    fish "Yah! It's Viscious Fish! Tonight we'll be playing our latest song, \"Dancing like a Discoball!\""
    fish "If you've had a hard week, now's the time to DANCE IT OFF! Come on!"
    fish "If you're sitting down, stand up now, get pumped, and get ready to DAAAAANCE!"

    play music "visciousfish.mp3"
    show alice awe
    show mc surprised
    hide music_stage with dissolve
    a "Wow, everyone's dancing! Hah, this is incredible!"
    show alice laugh
    a "Stand up with me, %(player_name)s!"
    show mc worried
    m "I-I don't dance. Everyone will-"
    show alice smirk
    a "Up you go!"
    show mc stressed
    m "Ugh, Alice..."
    show alice laugh
    a "The music is too good! You're not going to let a dying girl dance alone, will you?"
    show mc sad
    m "I'll try. But I'm not good."
    show alice sly smile
    a "I don't care if you're good or not. Let's both dance however we want!"
    "Alice grins and sways her body in tune to the music."
    "She doesn't give a damn about whether anyone's watching. But even if she did, she's a good dancer. Another one of those natural skills she has."
    show mc embarrassed
    "Awkwardly, you gently move side to side on beat. The instant you do it, you feel embarrassed for even trying."
    show alice laugh
    a "There we go!"
    show mc happy
    "But it makes her happy. So you force yourself to ignore your awkwardness, and let it out!"
    show black with dissolve
    stop music fadeout 3
    show music_stage with dissolve
    announcer "What a performance! That was Viscious Fish! Let's give them an applause!"
    announcer "And next up, we have a solo performance by..."
    announcer "Miranda The Megaphone!"
    show alice confused
    show mc happy
    hide music stage
    hide black with dissolve
    a "It's just one person?"
    m "Yup."
    show alice surprised
    a "Aw, I feel so bad for her."
    show mc annoyed
    m "Don't underestimate soloists."
    show music_stage with dissolve
    miranda "Um, h-hey. First-time being on a stage. Ah.... I'm doing this because of a dare, so like... don't be too mean, okay?"
    miranda "This song is called \"Nights of Sleeplessness\". It's dedicated to all the exams in the world."
    show black with dissolve
    miranda "*Long inhale*"
    show alice shocked
    show mc shocked
    play sound "miranda.mp3"
    pause 2
    hide music_stage with dissolve
    a "AH!"
    show mc surprised
    m "Ooooh, she's a metal singer."
    show alice mendokusai
    a "UGH! This is awful! Why would she volunatrily sing so horribly? I can't dance to this!"
    show mc normal
    m "I know a lot of people like it. And yes, you can. Look, you can see some people headbanging."
    show alice vannoyed
    a "I don't like it."
    show mc annoyed
    m "You don't have to. She's just singing the way she wants, just like you were dancing the way you wanted."
    show mc happy
    m "You can make any kind of music you want here. There's no judgement."
    show alice pout
    a "People will always judge. It's just whether they say it or not."
    show mc normal
    m "Sure. But right now she's choosing to sing what she wants, rather than what others think she should."
    show mc cute
    m "That takes a special kind of strength. I can respect that."
    show alice normal
    a "..."
    show mc happy
    m "I don't like metal music much either, but what do I love about it, is that I can feel the emotion in a way that standard, beautiful singing can't convey."
    show mc annoyed
    m "I can feel her hatred, the frustration, the panick, for exams, haha."
    show alice sad
    a "I can feel it too."
    stop music fadeout 3
    window hide
    scene black with fade
    window show
    "A few more songs play. Some upbeat, some eletronic, some classy, some aggressive."
    "You keep an eye on Alice, trying to guage how she's feeling."
    "She seems a little... solemn. What's going through her head?"
    "Did you do something wrong in bringing her here? This was supposed to be a fun night."
    "Now it's night-time. She doesn't have much time left."
    "There's an increasing feeling of dread builing in the pit of your stomach as the event concludes."
    "You and Alice walk home. She doesn't hook her arm through yours."
    "The only think you can do, is keep on smiling for her."
    $ watered = 1
    scene bottle night with fade
    show day_3 at topleft
    show water_status at water_location
    show alice_affection at topleft
    with dissolve

    play sound "door.wav"
    show mc happy at right
    show alice_base_buns at left
    show alice think at left
    show outfit at left
    with easeinbottom

    play music "night.mp3"

    m "Well, we're back. What did you think?"
    a "I enjoyed it."
    show mc cute
    m "You did? I'm really glad we went then."
    a "..."
    show mc happy
    m "I bet you're thirsty after all the dancing, aren't you?"
    a "..."
    show mc awkwardsmile
    m "I'll just... water you..."
    
    call screen water_alice_d3_night_badroute
    
    screen water_alice_d3_night_badroute:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.769 ypos 0.42 idle "mushroom_display/water_bottle_select.png" hover "mushroom_display/water_bottle_hover.png"
            action Jump("watered_alice_d3_night_badroute")

    label watered_alice_d3_night_badroute:
        queue sound "spray.wav"
        $ watered = 2
        queue sound "spray.wav"
        window show
        "Even when you spray the water right at Alice, she doesn't react."
        window hide
        show mc sad at right with easeinbottom
    window show
    "You can't keep smiling like everything's okay."
    m "Alice, what's wrong? You've looked kinda sad for a while."
    show alice normal
    a "..."
    show alice sad
    a "I... hurt."
    show mc confused
    a "Everywhere hurts. Like I'm being suffocated."
    show alice sad smile
    a "And not in the good way."
    show mc sad
    m "I'm sorry. Is it-"
    show alice normal
    stop music fadeout 3
    a "I think I've made a mistake."
    show alice sulk
    play music "date_musicbox.mp3"
    a "And I've realised it too late."
    show mc confused
    m "..."
    show mc cute
    m "Tell me how I can help you."
    show alice vannoyed
    show mc awed
    a "You can't. Not anymore."
    show alice sad
    a "I..."
    a "... failed."
    a "But, strangely, I don't care as much as I thought."
    m "Then, isn't everything okay?"
    show alice cry
    a "No. I just wish I'd realised it sooner!"
    show mc surprised
    a "As soon as I saw that girl on the stage, I wished it was me."
    a "This whole time, I've just been doing what I thought I should have."
    a "I didn't know I could do whatever I wanted."
    show mc confused
    m "I tried to tell you."
    a "Everytime you did, I heard a voice in my head telling me that you were wrong."
    show alice vcry
    a "But you were right."
    a "I'm sorry for everything."
    show mc awed
    m "I understand. It's okay."
    show alice smile cry
    a "Honestly, sorry for all the pressure I place on you. Even if we never became lovers, can we still be friends?"
    show mc cute
    m "Of course! Always have been."
    show alice sigh
    a "And always will be. I should have realised it sooner."
    show alice sad
    a "Even now, I'm still wondering why."
    show alice worried
    a "Why is it you kept rejecting me? I tried my best. I was made for it. I had no doubt that eventually you'd fall for me."
    a "But you never did. Why?"
    show mc normal
    m "Ah... well... I'm not the standard guy your creators probably made you for."
    show mc normalside
    m "I'm like a snail. The more you touch me, the more I shrink into my shell."
    m "I think, if you had more time, maybe then... but that was never possible."
    show alice normal
    show mc happy
    m "You're a cool person, Alice. You're funny and confident and caring, in your own pushy way."
    show alice neutral
    a "You sure that last was one a compliment?"
    show mc happy
    m "To me, it is. Because of your pushiness, I was able to do things that I never would usually."
    show alice sly smile
    a "I'm glad I could impact someone postively."
    show alice pout
    a "Make sure you leave your shell even when I'm dead and can't push you anymore. Got that?"
    a "Take your showers, brush your teeth, and do the fun things you want to do!"
    show mc annoyed
    m "So bossy. But okay, got it."
    show alice laugh
    a "Good. That helps me feel a little better."
    show alice depressed
    a "Ugh. It hurts so much. Dying sucks."
    show mc sad
    m "..."
    show alice worried
    a "Don't be like me, please. If there's something inside of you that you're ignoring, like I was..."
    a "Please, just do it. It's over for me, but you still have time."
    show mc cry
    m "Okay."
    show alice smile cry
    a "Good."
    a "I'm going to go now."
    m "Where?"
    a "I won't say, but..."
    a "Thank you for everything. Don't forget me, please."
    
    window hide
    stop music fadeout 3
    
    window hide
    scene black with dissolve
    show text "You're in your room. Sitting on a chair. Staring at your screen. One hand on your mouse. You've just finished playing a game."
    pause
    hide text
    show text "It's a normal day for you. By now, you've lived through thousands... How do you feel? Are you happy?"
    pause
    hide text
    show text "If you look into the deep crevices of your brainfolds, in a little space you've labelled \"Ignoring\"..."
    pause
    hide text
    show text "... can you find something in there, that, in your thousands of days of life, once interested you? Made your eyes grow wide? Filled you with awe?"
    pause
    hide text
    show text "Now, that small aspiration brews with resentment, among others, because you've convinced yourself that you're okay with never achieving it."
    pause
    hide text
    show text "You can't remove the desire. You've only made it smaller, more ignorable, more tolerable."
    pause
    hide text
    show text "Do you perk up a little every time you see it, or hear someone mention it? Or do respond with hatred, because others have achieved what you \"won't\"?"
    pause
    hide text
    show text "Everyone has a reason why they don't do it."
    pause
    hide text
    show text "\"That's the harsh reality of life. I don't have a choice.\""
    pause
    hide text
    show text "If you can relate to that sentence... You aren't who you wish you were."
    pause
    hide text with dissolve


    "End 5: Regret message."


label alice_worstending:
    window hide
    stop music fadeout 2
    scene black with fade
    window show
    "Still feeling awkwardly tense, you and Alice go back home."
    "Even though she's smiling, it feels like something is brewing..."

    scene bottle_phone night with fade:
        zoom 0.9
    #play music "night.mp3"
    show day_2 at topleft
    show alice_affection at topright
    with dissolve

    show alice_base_buns at left
    show outfit at left
    show alice happy at left
    show mc sad at right
    with easeinbottom

    a "..."
    m "..."
    show mc stressed
    m "(I don't know what to say. It still feels so awkward.)"
    show mc worried
    m "(What do I do?)"
    show alice flirt
    a "So... you had a good time in the end, right?"
    show mc normal
    m "Y-Yeah..."
    show alice hime
    a "Wonderful! Then-"
    show alice vflirt
    a "Then we can have sex now!"
    show mc confused
    m "..."
    show mc stressed
    m "No."
    show alice worried
    a "But why? The date was a success! This is how it's supposed to go!"
    show alice pout
    a "Are you just playing hard to get?"
    show mc sad
    m "N-no. I'm... I just... I'm not interested. Generally speaking."
    show alice flirtsweat
    a "You're not saying the right lines."
    show alice vflirt
    a "Come on. Surely you want to-"
    show mc stressed
    m "No."
    show alice flirtintense
    a "Fine! Do you want me to be pathetic? Shall I beg? I'll throw away my dignity for you!"
    show mc surprised
    m "No! Keep your dignity!"
    show alice annoyed
    a "Then what do you WANT FROM ME!?"
    a "Do you want me to cry? Just TELL me! I'll do it!"
    show mc sad
    m "I want you to calm down."
    show alice sigh
    a "*Sigh*"
    show alice happy
    a "Okay! I'm calm!"
    show mc normal
    m "And now, I want you to stop chasing after me."
    show alice sad
    a "..."
    a "Am I not attractive enough? Is that it?"
    a "Maybe if I didn't have my blemishes..."
    show mc normal
    m "What blemishes?"
    show alice sad
    a "Don't pretend. I couuld see them in the changing room's mirror. I have freckles."
    show mc stressed
    m "That again? You need to listen to me - you are attractive!"
    show mc confused
    m "And anyway, freckles ARE pretty! Lots of women put them on with makeup even."
    show alice depressed
    a "Don't lie just to make me feel better."
    m "Why don't you just forget your whole purpose and we can just be friends?"
    show alice neutral
    a "You're still rejecting me?"
    show alice disappointed
    a "Still? After everything? Even with my best effort, I still couldn't get you to like me?"
    show mc confused
    m "Um... sorry. I can see you're taking this hard."
    show alice flirtsweat
    a "Haha! I sure wish I taking {i}something{/i} hard!"
    show mc vblushside
    m "Uh, sorry, but I can't be the one to provide that."
    show alice annoyed
    a "Why? Why don't you like me? You should have fallen for me by now."
    show mc surprised
    show alice vannoyed
    a "I've used every tactic I know."
    a "But you flinch at every touch, every move I make! Like... like there's something wrong with me!"
    show alice vangry tears
    a "What did I do wrong? What must I do? Can I fix it? Do I have enough time? I..."
    show alice despair
    a "I'm running out of time!"
    show alice vdespair
    a "I can't keep waiting for the solution! I have to do something now! Please help me!"
    a "{sc=1}{color=#000000}I'm going to fail! I'm going to fail! Fail! Fail!"
    show alice vvdespair
    a "{sc=3}{size=+20}{color=#000000}FAAAAAAAIIIL!"
    stop music
    show mc shout
    m "STOP!" with sshake
    show mc vshout
    m "I'm the one who's wrong! Not you!"
    m "Whoever made you clearly didn't anticipate that there'd anyone but a healthy adult waiting for you-"
    m "But instead of that, you got a worthless, emotional-wreck of a human who can't truly relax for one moment!"
    m "The thought of someone being close to me drives me insane with guilt! It's not even an option!"
    show mc stressed
    m "I'm sorry! I wish I could just have cute, happy little relationships like everyone else..."
    show mc vstressed
    m "I'm sorry you got me."
    show mc cry
    m "Just please stop tormenting yourself. Please stop. If you want to get angry at me, you can. Just not yourself."


    show alice depressed
    a "He doesn't want me. I tried everything, but still! What did I do wrong? What? What? What?"
    show alice despair
    a "I failed."
    a "I failed, I failed, I failed, I failed, I failed..."
    a "I failed!"
    m "Alice, calm down!"
    show alice vangry tears
    a "I'm DONE doing what you tell me to do!"
    show mc shocked
    m "I'm just trying to help!"
    a "Screw your help! You can't help me! YOU'RE THE REASON I FAILED!"
    show mc surprised
    show alice vvdespair
    a "UUuuuuuuuh...."
    a "UuuUuuuuuuUUUUUUuuuuuuuuUUUUUuuuuuu..."
    show mc confused
    m "Alice..."
    show alice angry tears
    show mc awed
    a "DON'T SAY MY NAME! I'm... I'M GOING TO GO CRY ALONE!"
    show mc confused
    a "So don't you dare follow me right now."
    hide alice
    hide alice_base_buns
    hide dress
    with easeoutbottom
    play sound "door.wav"
    window hide
    scene bathroom with fade
    show alice_base_buns
    show dress polkadot
    show alice cry
    with easeinbottom
    window show
    a "I'm so stupid..."
    a "I'm so... ugh..."
    show alice depressed
    a "I was supposed to... but I... he..."
    a "And I'm supposed to just go like this?"
    a "I'm not ready."
    show alice worried
    a "!"
    window hide
    scene black with fade
    scene alicemirror shocked with dissolve
    play music "trip.mp3"

    # NB!!!! 

    #audio thing! Have a scary/deepsea/muffled version of trip to cut to every time the inner mind speaks.

    # reference: https://youtu.be/xy_7A2byhvY?si=1ff8yYSiY7B7CVSv 

    # Don't forget!

    window show
    a "That's me?"
    a "......."
    a "......"
    a "....."
    # audio switch
    show black
    show text "This is how I look?"
    pause
    hide black
    hide text
    # audio switch
    a "...."
    # audio switch
    show black
    show text "The instant I see myself, all I see are the imperfections."
    pause
    hide black
    hide text
    # audio switch
    a "..."
    # audio switch
    show black
    show text "The answer to why I failed... it comes so clearly."
    pause
    hide black
    hide text
    # audio switch
    a ".."
    # audio switch
    show black
    show text "Of course. It must have been my freckles."
    pause
    hide black
    hide text
    # audio switch
    a "."
    show black
    show text "It's like I can feel my pain through my own gaze. I'm scaring myself... I almost want to laugh."
    pause
    hide black
    hide text
    show alicemirror smile
    a "Even your smile is disgusting."
    a "It was never going to work."
    a "Just accept it."
    a "You're worthless."       
    a "You're ugly."
    show alicemirror shout
    a "You were never good enough!"
    show alicemirror shout:
        zoom 1.1
    play sound "mirror_hit.wav"
    show alicemirror shout:
        zoom 1.2
    a "No matter what you did!"
    play sound "mirror_hit.wav"
    show alicemirror shout:
        zoom 1.3
    a "No matter how much you sacrified!"
    play sound "mirror_hit.wav"
    show alicemirror shout:
        zoom 1.4
    a "{size=+20}YOU'RE NOT GOOD ENOUGH!"
    

    stop music
    stop sound
    show black
    a "{size=+40}AAAAAAAAAAAAAGH!"
    play sound "tear.wav"
    a "{size=+50}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
    a "..."
    a "No."
    a "No no no! NO!"
    play music "moody_music2.wav"
    scene alicemirror scratchface with dissolve
    a "..."
    a "I'm ugly."
    a "I'm ugly! Forever!"
    a "I-!"
    show black with Dissolve(3)
    
    stop music fadeout 3
    scene bottle night with fade

    show mc sad at right


    m "She's been a while."
    play sound "door.wav"
    show mc surprised
    m "Alice...! How are you feeling? Are you-?"
    show alice_base_buns at left
    show alice depressed
    show scar at left
    show outfit at left
    with dissolve
    show mc shocked at bounce
    m "{size=+30}WHAT DID YOU DO TO YOURSELF!?"
    a "I deserved it."
    show mc vstressed
    m "What? Why would you...!?"
    
    show mc cry
    m "I'm so sorry! Everything I did, and everything I couldn't..."
    m "I'm just sorry for everything that's happened."

    # bathroom

    a "I'm a failure of a woman. I hate my body! Nothing is right."
    a "Ugh, I'm... I'm worthy of being alive. I'm glad I'm going to die!"
    show mc shocked
    m "Don't say that! Get away from the mirror - you're... you're just overthinking everything!"
    show mc stressed
    m "Come... Let's go back to the bedroom."

    show bottle night with fade
    show day_2 at topleft
    with dissolve

    a "How... how do I stop this? Every time I see myself, I just want to rip my face off!"
    show mc shocked
    m "Don't do that! You're just emotional right now. You need calm down."
    a "I. Can't. S-stop. Thinking!"
    a "I'm ruined. I'm ugly. I failed. If only, I didn't have those damn freckles, maybe you would have accepted me!"
    show mc confused
    m "It wasn't the freckles! There's nothing wrong with your appearance! Please! Just take a deep breath."
    a "{sc=1}{size=-20}{color=#000000}I'm ugly."
    show mc normal
    m "Alice, stop saying that. You need to accept yourself, just like everyone else."
    show mc cute
    m "Everything's okay, I promise. We're still friends, no matter what."
    show alice angry tears
    a "{sc=1}{size=-20}{color=#000000}Don't say that!"
    show mc surprised
    m "I'm sorry. I didn't mean... I'm just trying to say that I'm here for you."
    show mc sad
    m "Stop being so cruel to yourself. Whatever flaws you see, only you see them."
    a "No. You all see them! You all judge me! Nobody..."
    show alice vvdespair
    a "... likes me."
    show mc stressed
    m "(What do I do? This is getting out of hand, and nothing seems to help.)"
    show mc worried
    m "(I'm scared. She's spiralling. Is this all my fault? Should I have just lied? Just... done whatever she wants?)"
    show mc vstressed
    m "(Was setting my boundaries selfish? If I'd known this would happen, I would have just ignored my discomfort.)"
    m "(This is too much!)"
    show mc sad
    m "Alice, would a cuddle help? You like those, don't you?"
    show alice vcry
    a "Even though I look like this?"
    show mc cute
    m "Yes. I don't-"
    show mc stressed
    m "(No! I have to be careful what I say. No comments on her appearance. She's extremely sensitive right now.)"
    show mc happy
    m "Yes. I'd enjoy it."
    show alice think
    a "Then... I'll do it."






    stop music fadeout 3
    window hide
    scene black with fade

    "You hold Alice tight."
    "You're so worried, your heart is beating so fast with dread, that you can't calm down enough to sleep."
    "It feels like you're awake for hour, just holding her, where you know she's safe..."
    "Until the emotional exhaustion and fatigue of the day overwhelms you."

    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "For a few hours, you drift into a dreamless sleep."
    with dissolve 
    pause
    hide top_text
    show chibi_awake at truecenter with dissolve
    show top_text "Until you realise that the presence next to you in bed it missing."

    scene bottle day with fade
    show day_3 at topleft
    show alice_affection at topright
    with dissolve

    show mc confused
    m "Alice?"
    "She's not here."
    show mc shocked
    m "No no no..."
    show mc worried
    m "Oh God. Please be okay!"
    play sound "door.wav"
    scene bathroom with fade
    show mc shocked with easeinbottom
    m "..."
    show alice cry


    
    


    # scarred face scene
    a "I... I fixed myself, %(player_name)s!"
    show mc confused
    m "You-"
    show fog_base with dissolve
    show mc shocked at bounce
    show mc shocked at quiver
    a "{i}I'm pretty now! Look!"
    window hide

    play music "audio/dynamic_audio/pad.mp3"
    show mcshocked with dissolve
    window show

    a "{sc=1}{color=#000000}All the bad parts are gone now! No more freckles! And my jawline is nicer too now!"
    a "{sc=1}{color=#000000}I solved everything! I'm pretty!"
    a "{sc=1}{color=#000000}Right!? What do you think!?"
    m "..."
    a "{sc=1}{color=#000000}Tell me! I'm pretty now, right?"
    m "..."
    a "{sc=1}{color=#000000}Why do you look at me like that? S-say something..."
    m "..."
    a "{sc=1}{color=#000000}Is something..."
    show alicescarredface
    pause 0.5
    hide alicescarredface
    play sound "audio/dynamic_audio/horror_EerieResonance3.mp3"
    a "{sc=1}{color=#000000}... wrong?"
    m "..."
    a "{sc=1}{color=#000000}Even now, do you still think I'm so ugly?"
    a "{sc=1}{color=#000000}It's still... Still? STILL?"
    a "{sc3}{size=+40}{color=#000000}STILL NOT ENOUGH!?" with Shake((0, 0, 0, 0), 2.0, dist=20)
    "You are frozen. You cannot speak. You can only stare, wide-eyed."
    window hide
    scene black with fade
    play sound "door.wav"
    window show
    "She ran away."
    scene bottle day with fade
    show mc vstressed with dissolve
    m "(She's unstable, but I have to find her. She's my responsibilty.)"
    show mc shout
    m "Wait! Alice!"
    hide mc with easeoutbottom
    scene hallway with fade        
    show mc surprised with easeinbottom
    "You catch sight of her, just as she runs down the stairs."
    show mc shout
    m "Wait! Please!"
    window hide
    hide mc with easeoutbottom
    scene black with fade
    window show
    "But you're not fast enough."
    "Alice gets outside first."
    "By the time you reach the dorm's entrance, she's..."
    play music ""
    # truck scene
    a "Doesn't anyone think I'm pretty?"
    play sound "malescream1.mp3"
    a "Why are you screaming?"
    play sound "womanscream1.mp3"
    a "What about you? Do you-"
    play sound "malescream2.wav"
    a "Anyone! Please! No one!?"
    show truck1
    a "{sc3}{size=+30}{color=#000000}DON'T SCREAM AT ME!"
    
    
    show truck2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5) with dissolve
    a "{sc3}{size=+40}{color=#000000}DOESN'T ANYONE LIKE ME!?"
    window hide
    play sound "truckhorn.wav"
    show black
    pause 3
    
    m "..."
    m "..."
    m "(Should I have sacrificed my boundaries, for her sake?)"
    m "(Even after everything, I still don't believe that.)"
    m "(It's not my fault. I shouldn't feel guilty for this. It's impossible to help someone, if they can't listen.)"
    m "(She destroyed herself.)"
    "End 8: Unrecognisable."
    return





# Bad End: You don't do the deed with Alice

# fight earlier, explain self, want alone time, she joins you, does her own thing next to you



# m "If I went to the other room, would you stay here?"
# a "No, I would follow you."
# m "Don't you want to do something you can actually enjoy?"
# m "Not just Twitter?"
# a "I'm enjoying myself. Can't you just focus on yourself?"
# m "(That's all I can do. You don't give me any other choice. I'm stuck.)"

# "The episode ends."
# m "You're still on Twitter-"

# a "I was going to get up literally right now. I was having a nice time, until that exact comment."

# "She stands up to leave, hovering at the doorframe for a second."
# "..."
# "Her eyes stare at me, deadpan."
# hide alice with dissolve
# play sound "door.wav"
# m "(How was I supposed to know you were about to get up? Why is asking a question bad?)"
# m "(I'm being punished for caring. I should have just not cared.)"
# "You look inwards. The happiness that had been building for the past hour is gone. You are empty now."
# "This isn't fair."
# "You never should have talked to her."
# "Again and again, you learn this lesson, yet when you say it like that, you're told it's wrong."
# "What is the lesson? What did you do wrong? What must you change? How do you not accidentally upset someone?"
# "This numb feeling in your body, the feeling of your heart twisting, the feeling of your smile falling, the feeling of hope vanishing, "
# "Even when you resume what you were doing, you can't pay attention anymore. It's meaningless."
# "The hopelessness is overwhelming."
# "You need a stronger distraction."


# m "Are you okay? Is something wrong?"
# a "..."
# m "You look kind of..."
# a "Just shut up!"






label alice_d3_sabrina_ver:
    #starts with Alice masking - sad (picked dress OR alice happy mask bc picked dress and 

    # scene bottle_phone day with fade:
    #     zoom 0.9
    # show day_3 at topleft
    # show alice_affection at topright
    # with dissolve
    # play music "normal.mp3"

    # show mc normal with easeinbottom
    # window show
    # m "(Hmm, she's not in my bed today?)"
    # m "(I mean that's a good thing, but... where is she?)"
    # show mc normalside
    # m "Alice?"
    # window hide
    # show mc at right with move
    # show alice sad at left with easeinbottom
    # window show
    # a "Good morning, %(player_name)s."
    # show mc surprised
    # m "Good morning. You alright?"
    # a "I'm fine, thank you."
    # show mc normal
    # m "(Clearly not... Though it is her last day. I can understand the melancholy.)"
    # show mc sad
    # m "(What am I going to do? She can't go like this. I need to lift her spirits.)"
    


#     else:
        
#         show mc normal with easeinbottom
#         window show
#         m "(Hmm, I don't feel as tired this morning as I usually do. I guess going to bed earlier really helped.)"
#         m "(Where is Alice?)"
#         show mc stressed
#         m "Don't tell me..."
#         window hide
#         show mc at right with move
#         show alice flirt at left with easeinbottom
#         window show
#         a "*Yaaaaaawn*, morning."
#         show mc normal
#         m "Of course you're in my bed again. *Sigh*... Well, let's get up."
#         show alice flirt
#         a "Aw, don't you want to stay and snuggle a little longer?"
#         show mc blushside
#         m "N-no thanks!"
#         "You hurry out of the covers before Alice can snake her arms around you."
#         show alice laugh
#         a "Hehe, you're pretty quick when you want to be."
#         show mc stressed
#         m "Phew..."
#         show mc normal

#         m "(Today is her last day. What should I do? I should make her feel happy, somehow...)"

#         m "(Maybe that flyer I saw yesterday. She'd probably like being outside.)"

#         jump alice_d3_date_sabrina_ver



# label alice_d3_date_sabrina_ver:

#     m "At an art exhibit, you can walk around and look at things that people have made."
#     a "I don't understand this."
#     m "I can get that. Abstract isn't for everyone. What's you favourite?"
#     a "The sculpture of the naked woman. Though still, she isn't THAT pretty."
#     m "Uh, interesting take. That's literally Venus. She's supposed to represent beauty."
#     a "She could do better. She's chubby."
#     m "..."
#     a "And she's got like NO eyebrows. And a big nose. And thin lips."
#     m "And beautiful people don't have those things?"
#     a "Mhm."
#     m "That's just the current beauty standard, you know? It hasn't always been like that."
#     a "Really?"
#     m "The people who made you probably didn't think history would be important, but yeah."
#     m "Hundreds of years ago, being skinny meant you were frail and fall sick more easily. So chubbiness was in."
#     m "I know plenty of guys who aren't that into the same thing."
#     m "Attractiveness is just subjective. Don't assume it's the same for everyone."
    
    
#     if alice_affection < 0: #sad
#         a "So there's no point in even trying to be hot?"
#         m "Not for others, no."


#     else:
#         show alice flirt
#         a "{i}You{/i} think I'm pretty, right?"
#         m "Yeah. Especially when you look happy."
#         show alice confused
#         a "That doesn't make sense."
#         show mc annoyed
#         m "It makes sense to me. Anyway, let's go to the next one."

#         "You and Alice spend an hour hopping through art exhibits."
#         "She has a clear preference for the obscene."






    #return home
    #happy
    # m "So... how does this work exactly? Do you know, like from your mushroom memories?"
    # a "Unfortunately, no. I just know that by tomorrow, I'll be dead."
    # m "How do you feel physically?"
    # show alice flirt
    # a "Horny."
    # show mc annoyed
    # m "Ugh, you know what I mean!"
    # show mc confused
    # m "Do you hurt anywhere?"
    # show alice laugh
    # a "Only in my heart, darling."
    # show mc normal
    # m "Well if you feel good enough to joke, you must be fine."
    # show mc normalside
    # m "(Though I do wish she'd be serious for once. I just want to help.)"
    # show mc sad
    # m "Alice, I can stay up a bit later tonight - Is there anything you want to do that I can help you with?"
    # show alice flirt
    # a "I-"
    # show mc stressed
    # m "And don't say THAT."
    # show alice pout
    # a "But it's true! That's all I want! Is it so wrong? I don't get it."
    # show mc normal
    # m "I've been clear from the start. I'm not okay with doing that."
    # show alice normal
    # a "You said you needed time. I gave that to you. I gave all my time to you. But I can't keep waiting anymore."
    # a "Please?"
    # m "Why do you even want it that much?"






# label maid_cafe:

#     scene maid_cafe with fade
#     play music "maid_cafe.mp3"
#     show aya happy with easeinbottom
#     window show
#     na "Hello Master! Hello Mistress! Welcome back home!"
#     window hide
#     show alice surprised at left
#     show mc worried at right
#     with easeinbottom
#     a "Uh, \"Mistress\"? Me?"
#     aya "Mew must be so tired! Please sit down and let Aya take care of mew!"
#     show mc confused
#     m "(Mew???)"
#     show alice hime
#     a "Hmph, well, if you insist~ but I must warn you: I have high standards."
#     aya "Mew-course, Mistress! You only deserve the best! This little kitty will try bring a smile to your day! Please, follow me!"
#     window hide
#     hide aya with easeoutbottom
#     show mc vblushside
#     window show
#     m "{size=-20}Wait, Alice! Are you sure? This place is weird!"
#     show alice normal
#     a "If a cute girl begs me to let her pamper me, it would be cruel of me to deny her. I'm not like YOU."
#     hide alice with easeoutbottom
#     show mc stressed
#     m "(Oh lord... Why a maid cafe? I've never had the courage to enter one. What even happens inside here?)"
#     window hide
#     hide mc with easeoutbottom
    
#     show black:
#         alpha 0.5
#     with dissolve
#     window show
#     "Aya leads you to a table and hands you a small, cutesy menu to peruse on your own for a minute."
#     window hide
#     hide black with dissolve
#     show mc surprised at right
#     show alice normal at left
#     with easeinbottom
#     window show
#     m "(Every food item looks so cute! And some come with performances?? WHY???)"
#     show alice confused
#     a "Pretty girls in cute, revealing dresses, serving everyone with their heart..."
#     show alice sigh
#     a "You made me think I was weird or something. But maybe you're just the weird one."
#     show mc confused
#     m "You know she's just pretending, right? No one would genuinely be like that..."
#     show alice annoyed
#     a "The fact that a place like this exists in the first place tells me all I need to know."
#     show alice sulk
#     a "She gets to do what I wanted... You wouldn't even let me call you Master."
#     show mc stressed
#     m "Because she's getting paid! Again, NOT because she wants to get fetishised!"
#     show mc normalside
#     m "I can't even understand why would someone voluntarily work here... So high energy."
#     window hide
#     show aya happy with easeinbottom
#     aya "Aya is working here to pay off my degree in Art, Master!"
#     show mc surprised
#     m "AH!"
#     show mc worried
#     m "O-oh. I'm sorry."
#     aya "Nyathing to worry about! Just five more years and Aya will be a free kitty unshackled from the chains of college debt!"
#     show mc sad
#     "You'll have to work to pay off your debt too, and you don't even LIKE what you're studying."
#     "This girl actually is doing something she wants."
#     aya "Master and Mistress, would mew like something to eat or drink?"
#     aya "Or mewhaps a dance?"
#     show alice cruel
#     a "A dance? What kind of dance?"
#     show mc normal
#     m "{size=-20}Not the kind you're thinking."
#     show aya excited
#     aya "A happy dance for my beautiful Mistress! Mew can pick the song for me!"
#     show alice laugh cruel
#     a "What charming devotion~ %(player_name)s, shall we make her dance?"
#     show mc stressed
#     m "(Don't bring me into the conversation! I'm still recovering from embarrassing myself!)"
#     show mc worried
#     m "But that's going to cost money..."
#     show alice pout
#     a "Money that would make me {i}very{/i} happy."
#     show aya happy
#     aya "It would help Aya's college fund too, Master!"
#     show mc stressed
#     m "Alright."
#     show mc normalside
#     m "Consider it my thanks for taking me out today."
#     m "And my apology for earlier, Aya..."
#     show alice smug
#     a "Go ahead and pick your favourite song for us, Aya. Show me what you can do."
#     show aya excited
#     aya "YAAAAAAAY! Thank mew, Master and Mistress! Oh, Aya almost forgot! Would mew like anything to eat?"
#     show mc normal
#     m "Um, maybe the omelette rice, please?"
#     aya "Our super-special omelette! Yes, Master, right away! And Aya will dance after you eat~"
#     window hide
#     hide aya with easeoutbottom
    
#     show mc confused
#     window show
#     m "You seem to be enjoying yourself."
#     show alice neutral
#     a "Not that you'd understand the joy of being doted on."
#     show alice hime
#     a "But it's nice to experience the otherside of the coin. I have a lot of appreciation for their hard work."
#     show mc normal
#     m "It's not like Aya will spend her whole life like that. She has dreams - she wants to be an artist."
#     show alice sulk
#     a "Just shut up and let me enjoy feeling valid for once."
#     show alice sigh
#     a "Let me dream of a world where I got what I want."
#     show mc confused
#     m "It really bothers you that much... that I don't feel that way towards you?"
#     show alice disappointed
#     a "I've already been rejected, so what's the point in caring anymore?"
    
#     show aya happy with easeinbottom
#     window show
#     show mc surprised
#     aya "Ta-da~! Mewr special meal has arrived!"
#     show alice pout
#     a "Oh, Aya, what do you do when someone doesn't like you, no matter what you do?"
#     show aya pout
#     aya "Hmm... that's happened a few times."
#     aya "Sometimes, people come in and want prettier maids."
#     aya "They don't like being stuck with me. Their sadness makes Aya sad too!"
#     show alice sigh
#     a "I completely understand."
#     show aya happy
#     aya "But Aya always does her bestest for the Masters and Mistresses that will appreciate it!"
#     show alice hime
#     a "You're wise beyond words, Aya. Our effort is wasted on those who won't appreciate it."
#     show mc stressed
#     m "Okay, but, Aya - what if these people don't like being pampered?"
#     show aya happy
#     a "Every-nyan is different, so Aya will give her Masters and Mistresses the space they want."
#     show mc annoyed
#     m "Oh? That's very respectful of you, right Alice?"
#     show alice annoyed
#     a "I'm sure Aya would feel sad if she could only work here for three days, and the entire time no body wanted her."
#     show aya pout
#     aya "Yes, Aya would feel very lonely."
#     show alice cruel
#     a "I'd feel so bad for her, wouldn't you, %(player_name)s?"
#     show aya happy
#     a "Every-nyan, Aya loves talking about hypotheticals, but we almost forgot about the food!"
#     aya "We must bless this food with a magical spell of delici-lici-liciousness!"
#     aya "Please, let's all say: Mew mew yum yum!"
#     show alice neutral
#     a "Excuse me?"
#     show mc normalside
#     m "{size=-20}I'm so not doing that."
#     show aya pout
#     aya "But Master... Mistress... the omelette...! We must work together for the spell to work!"
#     aya "And Aya will use her hard-earned Art degree to draw on it with ketchup for mew!"
#     show alice flirtsweat
#     a "I love the enthusiasm, but he'll just eat it up anyway. You can just leave the bottle here."
#     aya "Aw... Aya loves drawing... Aya wants to express her happy feelings!"
#     show alice confused
#     a "And drawing will allow you to do that?"
#     show aya excited
#     aya "YES! Aya has a vision! She wants to put her head-vision on the omellete!"
#     show alice hime
#     a "If you can even do such a thing, then fine! Impress me."
#     aya "Yay! All together now!"
#     show alice smug
#     a "You heard her, %(player_name)s. Together, now!"
#     a "Mew mew yum yum~"
#     show mc stressed
#     m "Mew... mew... yum yum..."
#     show aya happy
#     aya "MEW MEW YUM YUM!!! Pshhhh~Wawawa~Tada!~*magical noises*"
#     show omelette_rice with dissolve
#     pause 3
#     hide omelette_rice with dissolve
    
#     show mc surprised
#     m "DAMN!"
#     a "Aya! That's amazing!"
#     show alice sad
#     a "But now %(player_name)s is going to destroy it..."
#     show aya excited
#     aya "Hehe~ drawing itself was the bestest part! I love it!"
#     aya "Enjoy your meal, Master and Mistress! Aya will begin her dance shortly!"
#     window hide
#     hide aya with easeoutbottom
        
#     scene black with fade

#     "After having your food blessed, you eat it while Alice smiles in good humor."
#     "The omelette rice does taste pretty good. Annoyingly, your mood is improving."
#     m "(God dammit! I actually enjoyed that stupid maid cafe!)"
#     #dance sequence
#     return
#     scene mall with fade



# label maid_cafe_badroute:

#     scene maid_cafe with fade
#     play music "maid_cafe.mp3"
#     show aya happy with easeinbottom
#     window show
#     na "Hello Master! Hello Mistress! Welcome back home!"
#     window hide
#     show alice surprised at left
#     show mc worried at right
#     with easeinbottom
#     a "Mistress? Me?"
#     aya "Mew must be so tired! Please sit down and let Aya take care of mew!"
#     show mc confused
#     m "(Mew???)"
#     show alice hime
#     a "Hmph, well, if you insist~ but I must warn you: I have high standards."
#     aya "Mew-course, Mistress! You only deserve the best! This little kitty will try bring a smile to your day! Please, follow me!"
#     window hide
#     hide aya with easeoutbottom
#     show mc vblushside
#     window show
#     m "{size=-20}Wait, Alice! Are you sure? This place is weird!"
#     show alice normal
#     a "If a cute girl begs me to let her pamper me, it would be cruel of me to deny her. I'm not like YOU."
#     hide alice with easeoutbottom
#     show mc stressed
#     m "(Oh lord... Why a maid cafe? I've never had the courage to enter one. What even happens inside here?)"
#     window hide
#     hide mc with easeoutbottom
    
#     show black:
#         alpha 0.5
#     with dissolve
#     window show
#     "Aya leads you to a table and hands you a small, cutesy menu to peruse on your own for a minute."
#     window hide
#     hide black with dissolve
#     show mc surprised at right
#     show alice happy at left
#     with easeinbottom
#     window show
#     m "(Every food item looks so cute! And some come with performances?? WHY???)"
#     a "Pretty girls in cute dresses, serving everyone with their heart... Ah, I feel so at home."
#     show mc normal
#     m "Seems like difficult work to me."
#     show alice flirt
#     a "Really, you need to understand that all I want to do is serve you. You should just let me."
#     m "No comment."
#     show mc normalside
#     m "Why would someone voluntarily work here... So high energy."
#     window hide
#     show aya happy with easeinbottom
#     aya "I'm working here to pay off my degree in Art, Master!"
#     show mc surprised
#     m "AH!"
#     show mc worried
#     m "O-oh. I'm sorry."
#     aya "Nyathing to worry about! Just five more years and Aya will be a free kitty unshackled from the chains of college debt!"
#     show mc surprised
#     m "(Wow. Sometimes I forget how lucky I am that my parents are paying for my college.)"
#     "Which you're probably failing, by the way."
#     aya "Master and Mistress, would mew like something to eat or drink?"
#     aya "Or mewhaps a dance?"
#     show alice surprised
#     a "A dance?"
#     show aya excited
#     aya "Mew-course! Anything for my beautiful Mistress! Mew can pick the song for me!"
#     show alice happy
#     a "Hehe, what charming devotion~ %(player_name)s, shall we make her dance?"
#     show mc stressed
#     m "(Don't bring me into the conversation! I'm still recovering from embarrassing myself!)"
    
#     show alice pout
#     a "Come on, %(player_name)s? Please, for me?"
#     show mc worried
#     m "But that's going to cost money..."
#     show alice happy
#     a "Mhm~ Money well spent! Money that would make me {i}very{/i} happy."
#     show aya happy
#     "It would make her happy? When it's as simple as that, it's hard to say no."
#     aya "It would help Aya's college fund too, Master!"
#     show mc stressed
#     m "Alright."
#     show mc normalside
#     m "Consider it my thanks for taking me out today."
#     m "And my apology for earlier, Aya..."
#     show alice happy
#     a "Go ahead and pick your favourite song for us, Aya."
#     show aya excited
#     aya "YAAAAAAAY! Thank mew, Master and Mistress! Oh, Aya almost forgot! Would mew like anything to eat?"
#     m "The omelette rice, please."
#     aya "Our super-special omelette! Yes, Master, right away! Aya will dance while you eat~"
#     window hide
#     hide aya with easeoutbottom
    
#     show mc happy
#     window show
#     m "I wonder if she really has to say \"mew\" everytime? Would she get fired if she slipped up?"
#     show alice surprised
#     a "She got you to smile? I should be taking notes."
#     show mc blushside
#     m "I was so surprised by everything that I ended up forgetting my nervousness."
#     show mc awkwardsmile
#     m "It's just because she's so weird that even I feel acceptable."
#     show alice happy
#     a "You deserve a little more confidence, %(player_name)s. You can go anywhere you want."
#     show mc normalside
#     m "Eh. I don't think I've done anything to deserve it."
#     "That's right."
#     "The only thing you deserve is to suffer."
#     show mc stressed
#     "For wasting time and others' money, for not working hard enough, for letting your to-do list pile so high that you just gave up."
#     "You should just waste away yourself."
#     "In a hopeless, rotting spiral."
#     show alice normal
#     a "Oh, goodness. What a little worrywart you are..."
#     a "You don't need to do anything to deserve it. You should have it, just by default."
#     show mc normal
#     m "Let's stop talking about me."
#     show alice hime
#     a "As you wish. But you really should listen to me. I'm a very good judge of character."
#     show mc annoyed
#     m "I think you suffer from overconfidence."
#     show alice flirt
#     a "And confidence is so attractive in a woman, right?"    
#     show mc normalside
#     m "Nah. I always feel out-of-my league..."
    
#     show alice pout
#     a "What? Should I be more shy, then? More blushy librarian-cored?"
#     show alice shy
#     a "Th-thank you for inviting me here, %(player_name)s. Ever since you checked out those books-"
#     show mc stressed
#     m "Ugh. No stupid roleplaying. Just be yourself, please."
#     show alice pout
#     a "You and your impossible requests..."
#     window hide
    
#     show aya happy with easeinbottom
#     window show
#     aya "Ta-da~! Mewr special meal has arrived!"
#     show alice sad
#     a "Oh, Aya, what should I do? Master doesn't like me."
#     show aya pout
#     aya "Oh NO! Please don't frown, Mistress!"
#     show aya at flip
#     aya "Master, don't be mean to Mistress! No fighting, okay? Evil spirits cannot enter here, so only happy feelings, okay?"
#     m "Uh, okay...?"
#     aya "Master, remember that a smile can make everyone happy!"
#     aya "So don't forget, okay? Smile! PROMISE!"
#     show mc awkwardsmile
#     m "Urk, okay, I promise!"
#     show aya happy
#     a "Yay! Now every-nyan is happy! Ah- Aya almost forgot about the food!"
#     aya "We must bless this food with a magical spell of delici-lici-liciousness!"
#     aya "Please, let's all say: Mew mew yum yum!"
#     show mc normalside
#     m "{size=-20}I'm so not doing that."
#     show aya pout
#     aya "But Master... the omelette...! We must work together for the spell to work!"
#     show alice happy
#     a "You heard her, %(player_name)s. Together, now!"
#     a "Mew mew yum yum~"
#     show mc stressed
#     m "Mew... mew... yum yum..."
#     show aya happy
#     aya "MEW MEW YUM YUM!!! Pshhhh~Wawawa~Tada!~*magical noises*"
#     aya "Enjoy your meal, Master and Mistress! Aya will begin her dance shortly!"
        
#     scene black with fade

#     "After having your food blessed, you eat it all while Alice smiles in good humor."
#     "The omelette rice does taste pretty good. Annoyingly, your mood is improving."
#     m "(God dammit! I actually enjoyed that stupid maid cafe!)"
#     #dance sequence

#     scene mall with fade





# label after_maidcafe:
#     #bad route - good route
#     stop music fadeout 2
#     play music "mall.mp3"
#     scene mall with fade
#     show alice hime at left
#     show mc happy at right
#     a "You enjoyed that, right?"
#     show mc normalside
#     m "..."
#     show alice smug
#     a "Admit it! You enjoyed that, didn't you?"
#     show mc annoyed
#     m "Yeah, it was pretty fun."
#     show mc surprised
#     m "Seeing that artwork was awesome. She danced well too."
#     show mc happy
#     m "And the food was tasty."
#     show alice pout
#     a "Then you'll agree that I deserve a headpat at the very least, right?"
#     show mc confused
#     m "I-I don't mind, but... why do you even-"
#     show alice hime
#     a "You don't need to understand. But I would like it very much."
#     show mc normal
#     m "*pat pat*"
#     show alice happy
#     a "Ah~ just like that~"
#     show mc blushside
#     m "Ok that's enough. Where to next?"
#     show alice confused
#     a "There should be a cute little river somewhere close..."

#     scene enbankment with fade
#     hide alice
#     with easeoutbottom
#     window show
#     "Alice sits down on the grassy hill facing the river, then looks up at you and pats the ground next to her."
#     a "Sit with me?"
#     show mc normalside
#     m "Sure."
#     window hide
#     hide mc with easeoutbottom
#     window show
#     "You both watch the light reflect on the river."
#     "The warm wind fingers your hair, and, for a moment, you close your eyes..."
#     show black with dissolve
#     "And you think of nothing."
#     "..."
#     play sound "bird.wav"
#     "..."
#     "..."
#     a "*gasp*"
#     hide black with dissolve
#     show alice happy at left
#     show mc surprised at right
#     with easeinbottom
#     m "Alice?"
#     a "Look, a butterfly."
#     show mc surprised
#     m "Ooh, where?"
    
#     show butterfly with dissolve
#     stop music fadeout 2
#     window show
    
#     m "Wow. It's beautiful."
#     a "Such a gorgeous blue colour. What a pretty little thing you are~"
#     a "It's so beautiful that I don't even care if it's dead."
#     m "It's dead!?"
#     a "*chu~*"
#     m "Why are you kissing it?"
#     a "Because it's pretty, why else?"
#     a "You should take a hint, hehe..."


#     show alice happy

#     hide butterfly with dissolve




# make her date end in disaster -

# Alice plans a perfect event, things go really well, she makes a move, MC pushes her off, and she reaches her breaking point.
# I haven't managed to make you fuck you yet. Am I just horrible? Am I ugly? What the FUCK!?" breakdown cg! Scratch face
# Mc is having a good time but Alice is NOT SATISFIED with what's happening.
# She's doing everything with the expectation.
# Make her desparate by the end of day 2 - maybe while she is waiting for mc, we see her worrying and panicked.
# Make day 3 just trying to survive. Wake up with a knife pushes to his cheek.
 
#Alice breakdown after push away



show alice sad
a "..."
a "So you're saying I was always doomed to fail?"
show mc cry
m "Yes. Because of how I am."
show mc stressed
m "BUT-"
show mc awed
m "I'll still do my best to help you in any other way. You won't be alone..."
show mc sad
m "If you even want me."
a "You're saying I should just ignore the part of my head that's constantly screaming at me like:"
show alice normal
a "\"Have sex with your owner to reach true happiness!\"?"
show mc confused
m "So that's the only reason you were being nice to me?"
show alice sulk
a "It's complicated."
show mc normal
m "Was I the only one who was actually enjoying themself for the past two days?"
show alice sad
a "*Sigh* No, I enjoyed some parts. But mostly, I was just really stressed."
show alice sigh
a "I'm always critisising my every word and action. If my voice sounded cute or sultry enough, if my lips were pursed enough, if I was boring you..."
a "Every time you pushed me away, or looked disinterested, it felt like my life was over."
a "Trying to have sex with you is like playing Bubble Bobble on Insane mode. I feel like there's still a chance, but that I'm just not good enough."
show alice sulk
a "I thought if I just kept working hard, trust the instincts and knowledge I was born with, you'd like me."
show mc confused
m "But-"
show alice normalisde
a "Yeah, I know. Impossible."
show mc stressed
m "Sounds like a nightmare. I feel guilty for even enjoying myself, while you've been so stressed."
show alice neutral
a "That was my goal, so at least I managed that..."
show alice sulk
a "I should have just listened the first time you rejected me. What a waste."
show mc normalside
m "If I could go back in time, I'd just tell you straight up that I'm asexual or something."
a "Maybe THAT would have stopped me. I don't know."
show alice sigh
a "Hah... Okay... I'm done."
show mc surprised
m "With what?"
show alice neutral
a "What do you think? I failed. The sooner I'm out of here, the sooner this horrible feeling can end."
show mc shocked
m "But you still have another day left!"
show alice normalside
a "..."
show alice cry
a "I'm tired."
show mc happy
m "Relax! Want a footrub? How about you let ME serve YOU?"
show alice normal
a "..."
show alice sad
a "I just want to cry."
show alice angry
a "Ugh, and these fucking space buns are so heavy!"
show alice_base_longhair_choker with dissolve

# show alice hair loose.



# Alice bad route breadown:


    # a "It's okay, %(player_name)s."
    # a "It doesn't matter anymore."
    # a "I just came here to say goodbye."
    # show mc confused
    # m "Goodbye? Where are you going?"
    # a "It doesn't matter."
    # a "I'm going to spend the last few hours of my life by myself."
    # show mc vcry
    # m "Won't you be lonely?"
    # a "Goodbye, and thank you for having me."
    # show mc awed
    # m "Wait!"
    # show mc cry
    # m "Alice. You are enough. Just as you are. You don't need to pretend."
    # m "And... I hate that I'm the reason all of this happened."
    # m "Do you forgive me?"
    # a "..."
    # a "I'm the one who's sorry."
    # a "I tried to manipulate you into doing what I wanted."
    # a "All this time, I was just doing the same thing I hated."
    # a "Everything, so unnecesarily complicated... Hah..."
    # m "..."
    # a "I only understand now."
    # a "You were right. I should have just been myself, not appease the voices..."
    # a "I wasted my whole life, just living for another person. And now that it's over..."
    
    # a "I never figured out who I am."
    # a "That's why I'm so sad."
    # a "I don't know who I am. I don't know what I like. I don't know myself at all..."
    # a "This life..."
    # a "Was a complete and utter waste."
    # hide alice
    # hide dress
    # hide alice_base_buns
    # with easeoutbottom



    # window hide
    # hide alice with easeoutbottom
    # show mc vstressed
    # window show
    # m "(What should I have done? Am I to blame? Should I feel guilty?)"
    # "You'll feel it whether you deserve it or not, because at the end of the day, YOU were the reason she went down this path."
    # "All because of you."



    # show black with dissolve
    # pause 1
    # show text "What are you supposed to do with yourself after that?"
    # with dissolve
    # pause 
    
    # hide text
    # show text "What are you supposed to do?"
    # with dissolve
    # pause 
    # hide text
    # with dissolve

    # pause 1
    # window show

    # "End 8: Scars."
    # return






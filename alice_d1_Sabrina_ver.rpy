# Inject some vibe that she's looking down on you. Feel a little more superficial.
# Gives you a lot of compliments

label alice_d1_Sabrina_ver:
    
    default alice_rp = 0

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

    m "But everytime I try to do one of my big dreams, something that needs committment, I struggle to finish stuff."
    m "I just want someone to tell me what to do. I don't want to be responsible for my own life."
    m "I'm scared that when I start... I'm going to feel the same way."

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
    m "Alright, let's get spritzing."
    show mc confused at bounce
    m "..."
    show mc surprised
    m "Whoa... Uh... Was this box always so engorged?"
    na "{size=-8}Whaaaa- Rude~!{size=+8}"
    m "..."
    show mc awed
    m "D... did it just... speak?"
    na "{size=-8}Mhm, {i}that's right{/i}!"
    show mc shocked
    m "!"
    na "{size=-8}Eheh~ As much as I {i}love{/i} waiting for you to rescue me, I think I've about reached my limit."
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
    na "{size=+20}AAAAAAAAAA~! Fresh air!"
    na "Oh my gosh - sorry for the long wait, but I'm finally here!"
    m "..."
    show alice wink
    na "Aw, am I really that breath-taking? You're too kind, hehe."
    show alice surprised
    na "Woooow! Your place is so..."
    show alice confused 
    na "Um, what's the word? Hmm..."
    show alice laugh
    na "Cosy! It feels so {i}warm{/i} in here! Like a snuggly blanket of cuddles! It's sooooo nice!"
    show mc vstressed
    m "WHO-" with sshake
    show alice happy at bounce
    show dress at bounce
    show alice_base_buns at bounce
    na "\"Who am I\"?"
    show mc surprised
    m "Y-yes..."
    show alice wink
    show mc confused
    na "I beat ya! Too super-speedy for you to even finish your question! Teehee!"
    show alice hime
    a "I'm Alice! Short and sweet, just like me!"
    show alice normalside
    a "Well, it's the cute-ified version of my full name, but Amanita muscaria is a mouthful, y'know?"
    show alice normal
    "Aaaaanyway-"
    show alice laugh
    a "It's such, such, such, SUCH a pleasure to finally meet you, Master!"
    show mc shocked
    m "MASTER!?"
    show alice confused
    a "Um, it is YOU who's been growing me this whole time, right?"
    show alice flirtsweat
    a "It would be SUUUUUPER AWKWARD if I did my whole one-time entrance in front of the wrong person, so please say yes!"
    a "You watered me everyday, right? I'm your one-and-only special mushroom, right?"
    show mc confused
    m "Yes..."
    show alice sigh
    a "PHEW! Ah, for a second I thought-"
    show alice depressed
    a "{size-=20}I'd messed up-"
    show alice happy
    a "But I didn't! So everything's wonderful!"
    show mc stressed
    m "You're... not really a mushroom, are you?"
    show alice pout
    a "Of course I am! I'm 100% pure mushroomy goodness. There's not a bone in my body."
    show alice wink
    a "Unless you want to put one-"
    show alice vannoyed
    a "E-e-eHEM! Ugh, my throat..."
    $ watered = 0
    show water_status at topright with dissolve
    
    play sound "spray.wav"
    $ watered = 1
    pause 1
    queue sound "spray.wav"
    $ watered = 2
    hide water_status with dissolve
    show alice sigh
    play music "normal.mp3"
    na "E-hem- ehem - Ah, much better."
    show alice normal
    show mc surprised
    m "Did you just spray yourself in the face?"
    show alice surprised
    a "Oops! I completely forgot that was your whole thing! Sorry, did I accidently make you obsolete? Do you wanna do it?"
    show mc stressed
    m "No, I don't-"
    show alice happy
    a "So Master, what's your name?"
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
            a "Not MY name, silly! Yours!"
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

    show alice surprised 
    a "%(player_name)s? No way. You have to be kidding me! That's literally the most amazing name I've ever heard."
    show mc confused
    m "..."
    show alice laugh
    a "I'm serious! %(player_name)s~ %(player_name)s~ %(player_name)s! Aaaah, how sweetly it rolls off the tongue."
    show mc awkwardsmile
    m "Thanks? Alice is a good name too."
    show alice cutesad
    a "Eeeeh? Really really really? I just thought of it for some reason. So I picked a good name?"
    show mc confused
    m "Alice? May I ask you something?"
    show alice pout
    a "Answering a question with a question? Not fair."
    show mc stressed
    m "Sorry, but it's really important, and I need your help."
    show alice cute
    a "Fine, ask away! No matter the question, I have to answer 100% truthfully."
    show alice wink
    a "It's a promise."
    show mc confused
    m "If you're a mushroom, then why do you look like a human?"
    show alice surprised
    a "!"
    show alice sad
    a "Um, are you sure you can handle the truth? It would be troublesome if I melted my master's brain."
    show mc surprised
    m "(Damn, how bad can it be?)"
    "Famous last words."
    show mc worried
    m "Okay, tell me!"
    a "Then prepare yourself. The truth is..."
    show alice wink
    a "I have no idea! I was just born this way!"
    show mc confused
    m "Wh- Then what was the point of all that \"Can you handle the truth\" stuff!?"
    show alice laugh
    a "I was playing around~! Hehehe!"
    show mc stressed
    m "..."
    show mc normalside
    m "Now what? I still don't understand why this happened..."
    show alice confused
    a "Hmmm? I don't get it. What's the problem exactly?"
    show mc confused
    m "You were supposed to be a normal mushroom. I was going to eat you-!"
    show alice happy
    a "Then there's no problem! You still can."
    show mc surprised
    m "I... {i}can{/i}? And that doesn't bother you!?"
    show alice flirt
    a "Nu-uh!  In fact, you could nibble a certain place right now-"
    show alice surprised
    show mc vstressed
    m "GAH! This... This doesn't make sense! I ordered normal mushrooms! But you're not-"
    show alice normal
    a "\"Normal\"?"
    show alice confused
    a "Eeeh? But normal would be so BORING!"
    "Are you CERTAIN you know what you even ordered? Suddenly, you're starting to doubt yourself."
    show mc surprised
    m "(I mean, I did check it, didn't I?)"
    m "(I didn't just buy something without looking at it properly, right? That would be completely irresponsible!)"
    "Yes, that would be VERY uncharacteristic of you."
    show mc worried
    m "S-sorry, Alice. Please excuse me. I need to check what I ordered."
    show alice happy
    a "Mhm~ No problem!"
    hide mc with easeoutbottom
    show alice normal
    a "Wait..."
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
        a "Hmm? So this thingy has information about me?"
        show mc surprised at right with move
        m "What are you doing here?"
        show alice pout
        a "Master %(player_name)s, why are you trying to spy on me? You don't need to resort to that - You can ask me anything!"
        show mc normal
        m "But I don't want jokes. I want the truth."
        show alice happy
        a "You don't need to know the truth! Let's just be happy together and have some fun!"
        show mc stressed
        m "Sorry Alice, but that's not my style."
        show alice normalside
        a "*Sigh* Fine... As long as you share whatever truth you find."
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
        show alice surprised at left
        show dress polkadot at left

        with easeinbottom
        window show
        a "What's it say? What's it say?"
        show mc worried
        m "Are you sure you-"
        show mc confused
        m "Wait, you mean you can't read?"
        show alice cutesad
        a "No, these squiggle-lines are 100% incongruous to me, so I'm depending on you, okay?"
        show mc surprised
        m "(\"incongruous\"?)"
        show mc normal
        m "Well, okay. I'll read for you. Firstly, there's this word you should know:"
        show mc confused
        m "Fly A-ma-ni-ta."
        show alice happy
        a "Hey, that's me!"
        show mc surprised
        m "You did? How?"
        show alice confused
        a "Hmm... My body kinda just recognised it. Like, on an instinctual level!"
        show mc confused
        m "Okay, um, moving on... the site basically just says stuff like..."
        show mc blushside
        m "They're selling mushroom girls... to eat and..."
        m "Be intimate with..."
        show alice confused
        a "You mean when people know each other carnally?"
        show mc vstressed
        m "Just so you know! I didn't know ANYTHING about this when I first got you!" with sshake
        show alice happy
        a "AAAANYWAY, what else does the thingy say about me? Does it say what else I should do?"
        show mc normal
        m "..."        
        show mc sad
        m "Uh, it also gives your lifespan. Do you want to know?"
        show alice worried
        a "Oh, um... is it good or bad?"
        "Ignorance is bliss. Maybe you shouldn't, to spare her the pain."
        show mc stressed
        m "(But she has the right to know.)"
        show mc sad
        m "It says your \"lifespan\" is three days. I'm sorry."
        show alice surprised
        a "\"I'm sorry\"? Is three days a short or long duration?"
        show mc awkwardsmile
        m "Kinda short? Compared to humans, at least. But you can do a lot in that time too, so..."
        show alice normalside
        a "Oh well."
        
    
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
    

    
    m "..."
    a "...?"
    show mc surprised
    m "\"Oh well\"? That's it?"
    show alice sly smile
    a "Mhm! I just gotta focus on my goals and everything'll be perfect, Master %(player_name)s."
    a "And you'll help me, won't you?"
    show mc normalside
    m "(I am responsible for her life. I still can't believe I've just grown someone, but it's true.)"
    "How are you going to cope when looking after yourself is such a chore?"
    show alice pout
    a "You won't abandon me, will you, Master?"
    show alice cutesad
    a "You keep talking about how I'm not what you wanted. Do you dislike me?"
    show mc shocked
    m "No! Not at all!"
    show alice vcry
    a "Because I just wanna spend time with you! I'm trying my best!"
    show mc shocked
    m "(SHE'S CRYING!?)"
    a "Please don't leave me~! *Sob* I need you! If you leave me, what will I do?"
    show mc worried
    m "It's okay! Just please stop crying-"
    a "You promise you like me?"
    show mc vstressed
    "Great job! You've made her cry!"
    show mc awkwardsmile
    m "Yes! I swear! No hard feelings!"
    a "*Sniffle* I need a hug!"
    

    show alice at center
    show alice_base_buns at center
    show dress at center

    with move
    show mc surprised at bounce
    show alice_affection at topright
    with dissolve

    menu:
        "She's walking towards you!"
        "Enforce your boundaries!":
            m "W-what are you doing!?"
            show alice worried
            a "Mm? I just wanted a hug. Pwease, %(player_name)s?"
            show mc worried
            m "Sorry, I don't do hugs like that. I'm... I'm just not a hugger."
            show alice cutesad
            a "Aw, then..."
            "Alice reaches for your hand."
            show mc shocked
            m "Gah! Don't hold my hand either! No touching!"
            show alice worried
            a "Huh? But this is what I'm supposed to do. Are you mad at me? I thought you said no hard feelings! You didn't lie to me, did you?"
            show mc worried
            m "I'm not mad at all! Seriously, I just need to keep some personal space right now."
            show alice worried
            a "But... I just wanted to clear the air... and to say thank you for everything."
            show mc awkwardsmile
            m "I can assure you that the air is cleared, and you can say anything you want from 2 feet back!"
            hide alice_affection with dissolve
            show alice happy
            a "Aw, come on, Master %(player_name)s! There's no need to act so coy around me."
            show mc shout
            m "I'm not being \"coy\"! I'm just reininforcing my boundaries!"
            show alice disgusted
            a "Why would you do that?"
            show mc worried
            m "You're just... {i}really close{/i}!"
            a "I'm SUPPPOSED to!"
            show alice sigh
            a "E-hem!"
            show alice happy
            a "So just {i}relax{/i}, %(player_name)s."
            "Alice steps in and grabs your hand."
            show mc shout
            m "No no no! Get away! I don't know what you want, but whatever it is-"
            show mc vshout
            show alice shocked
            m "{sc=4}{color=#000000}{size=+40}I DON'T WANT YOU!" with sshake
            show alice flirtsweat
            a "O-of course you want me! Don't say that! Why else am I here?"
            show mc stressed
            m "I don't know! It was a mistake! I didn't want you here in the first place."
            a "You must be so stressed, %(player_name)s. Come, why don't we just calm down for a second?"
            show mc confused
            m "..."
            "Alice doesn't make anymore moves. She's still clenching onto your hand, but..."
            m "(I can endure it. I said some things I shouldn't have, so this is just my punishment.)"
            show mc sad
            m "Y-yeah... I'm sorry."
            show alice happy
            a "I understand. You're so tense, so aggravated, so let's just take a seat on your bed, okay?"
            show mc stressed
            m "Okay. *Inhale*... *Exhale*..."
            m "(I really panicked there, but it's all over now.)"
            show alice flirt
            a "Mhm~ just like that. Don't you feel so much better now?"
            show mc confused
            m "I do, thanks-"
            show alice at right
            show alice_base_buns at right
            show dress at right
            with move
            show mc surprised
            m "Whoa-!"
            jump alice_bed_scene
            

        "Offer a consoling hug.":
            jump nice_route

    

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
    a "Because you're more innocent than I expected. You just need a {i}helpful little push{/i}!"
    "WAIT A SECOND! Why is she looking at you like THAT?"
    m "(I-I must be misinterpreting-)"
    a "%(player_name)s... I've been so lonely~ I haven't been able to say a thing for weeks..."
    a "You understand, don't you? How horrible that can feel?"
    m "I... kinda do...?"
    a "Then, maybe we can help each other out."
    
    show alice_bed_2 with dissolve 
    "OOOOOH SHE'S APPROACHING! I DON'T THINK YOU'RE MISINTERPRETING ANYTHING!" with sshake
    "Are ya ready, champ? This is THE MOMENT! The one all boys wait for their entire lives!"
    m "(Of course not! I've never been so unprepared in my life! I haven't even brushed my teeth yet!)" with sshake
    m "(And I hardly know her! And she's a mushroom! And- And-!)"
    m "(I don't even think I want to! I'm scared! She's so pushy and I don't even like it!)"
    "But that's strange. You {b}SHOULD{/b} want this."
    m "(I should?)"
    "Yes! This is what real men do when they come to college! You've seen it on tv, movies, the radio..."
    "Every man wants a cute girl! And now you've got one!"
    "So what's with the hesitance?"
    a "Oh my goodness~ What's with your frown? There's nothing to worry about."
    a "It's just me and you here."
    "There is a clear expectation in her eyes."
    "The closer she gets, the more your body tightens with immobilising discomfort."
    a "Hey, hey, don't worry so much, okay? I'm good for first-timers too!"
    show alice_bed_3 with dissolve
    pause 1
    "Alice gives your cheek a gentle caress with her fingertips, sending an ice-cold bolt of pure sensation up your spine."
    "To anyone else, it would feel good, but you don't want it."
    "You flinch away, but Alice grapples you before you can escape."
    m "Don't come any closer! I-I-I don't-"
    a "Come on! Stop acting like this! Why don't you like it? This is why you made me, right? So-"
    m "I don't want you! Not like this!"
    a "You'll like it! Just stop resisting-"

    show alice_affection at topright with dissolve
    
    menu:
        "She's stronger than you. You can't even rip your wrists out of her grasp."
        "Give in.":
            "Alice isn't the problem. It's you. You're the one acting strange."
            "You have a willing woman in front of you. This is the supposed task that every man should aim to fulfill in his life."
            "If you don't want to do it, then you're wrong."
            "You're wrong. Not her. She's helping you. You're lucky."
            "You should be thankful for this oppurtunity."
            "Even if you don't want it, you have to do it."
            "You grit your teeth, squeeze your eyes shut, and just let it happen like you're supposed to."
            scene black with fade
            #Make music here strong
            "Placing her hands against your chest, Alice presses her mouth against yours."
            "Your head feels so dizzy, the world so confusing, that you can't tell what's happening. You embrace that, and dissociate."
            "You don't keep track of time, you don't do anything."
            stop music fadeout 2
            "Everything distorts, revolving around you, up and down, all around, like you're stuck on a carasoul."
            "You just wait, keeping the urge to vomit in, until the ride is over."

            window hide
            stop music fadeout 2
            scene black with dissolve

            $ alice_rp -= 100
            scene bottle night:
                zoom 0.9
            show day_1 at topleft
            show alice_affection at topright
            with dissolve

            show mc vstressed at right
            show alice_base_buns at left            
            show alice depressed at left
            show dress polkadot at left
            with easeinbottom

            window show
            a "Why didn't you like it?"
            show alice angry
            a "I did all of that for you, and you didn't even enjoy it!? Why!? I was just doing what I was supposed to!"
            "As soon as you hear the anger in her voice, it all becomes too much."
            hide mc with easeoutbottom
            play sound "door.wav"
            window hide
            scene black with fade
            pause 1
            window show
            "You sprint out the door, down the hallway, and out the dorms."
            "Not caring about how you'll be perceived or who will see, you only listen to the urgent screaming inside your heart."
            "It doesn't matter where, or who sees. Right now, you have to run! Fast, hard and desperately, you run."
            "But no matter how far you go, how much you distance yourself mentally or exhaust yourself physically..."
            "The feeling of violation in your body doesn't leave."
            "And you are left feeling more broken. More hopeless. More ashamed."
            "End 1: Violated."
            



        "{sc=4}{i}{color=#000000}{size=+40}AAAHHHH!":

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
    a "Hah, look, clearly I approached you {i}incorrectly{/i}..."
    show alice disappointed
    show mc surprised
    a "I think this would all work out better if you told me exactly what you want."
    a "So tell me: should I be more gentle? Sultry? Do you want me stutter too?"
    a "Do you like them silent? I'll be anything you want. I can do it."
    show mc confused
    m "Can't you just be yourself?"
    show alice neutral
    a "What's the point of being myself if you don't like me?"
    show alice normal
    a "So if you help me here, I can fix this all."
    show mc surprised
    m "Fix what? There's no problem!"
    show alice flirt
    a "So you do want to have sex with me?"
    show mc shout
    m "NO!"
    show alice hime
    a "Ah ha! See!? There's the problem!"
    show mc confused
    m "What the hell. You're totally different from before. What AM I to you exactly?"
    show alice disappointed
    a "Why? Did you prefer THAT Alice and all her cuteness? Then tell me, and you can have it."
    show alice vannoyed
    a "Just tell me what you want!"
    show mc stressed
    m "What I WANT is for you to stop harrassing me!"
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
        m "?"
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
    ali "I have no clue what you're talking about."
    show mc awed
    m "I just meant like, we could use my PC..."
    show mc normalside
    m "but then we're really compromising on the authenticity of the experience."
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

    ali "Game Over? What is this shit?"
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














    

                
            




label nice_route:
    
    show mc stressed
    m "(It's my fault she's crying. The least I could do I give her the hug she needs.)"
    m "Uuurk... okay."
    show mc vstressed
    "Stiffly, you open your arms and allow someone who is basically a stranger to hug you."
    "As soon as the hug happens, however..."
    show mc and alice hug
    m "(Oh, it's not as bad as I worried.)"
    show mc blushside
    m "Y-you don't need to worry so much. I'll help you do whatever you need to do. It's my responsibility."
    show alice worried
    a "You promise? *sniff* You really, {i}really{/i} promise? No matter what?"
    m "(The way she says that... kinda makes me hesitate for some reason.)"
    "For a second - No, what are you thinking? You must be imagining it!"
    m "Um, as long as it's not dangerous or bad."
    show alice sadsmile
    a "Thank you! Knowing you'll be with me makes this all a lot easier. I'm really scared of being alone..."
    a "I'm glad my master is such a sensitive soul. He understands me."
    "As soon as you hear those words, her trust in you, you feel ashamed for ever doubting Alice."
    show mc cute
    m "Hey, don't worry. I won't let you feel alone. I can promise that too."
    show alice vcry
    a "Thank you... Ah gosh, I'm crying again. I'm such a dummy."
    m "If you gotta cry, you gotta cry."
    "The longer you hug it out, the less you seem to forget your initial worries."
    "Now, it's become enjoyable."
    show alice cutesad
    a "It's embarrassing, but... Can I tell you a secret? You have to promise not to laugh at me."
    show mc surprised
    m "Okay."
    show alice sadsmile    
    a "Well, you probably know there's not a lot to do in the box, right? So what do you think I did most often while waiting to grow?"
    show mc normal
    m "Damn, that sounds boring as hell. Isn't the only thing you can do {i}think{/i}?"
    show alice laugh
    a "Ding ding! Yup! I could only think. And it WAS boring. The only thing that happened was when I'd feel the cool, refreshing mists of water against soil."
    show alice happy
    a "I'd always hear your gruff, manly voice encouraging me on. That was always the highlight of my day."
    show mc normalside
    m "(Manly? Gruff? That wasn't me. Who is she talking about?)"
    show alice sad
    a "All I've been thinking in that horrible, dark space..."
    show alice happy
    a "...was getting to see you. Getting to be your friend, learning about you... and spending time together."
    show alice wink
    a "I've been imagining all sorts of things we could do together."
    show mc confused
    m "Something in your eye?"
    show alice sigh
    a "..."
    show bottle noon with Dissolve(2):
        zoom 0.9
    play music "normal.mp3"
    show mc awed
    m "I can't believe it's already afternoon. We've been talking for a while."
    show alice wink
    a "Oh my. We're all alone in your bedroom and it's approaching night-time. Whatever shall we do?"
    "She's bored. You're boring her."
    "You're wasting her life."
    show mc normalside
    m "(Of course I am. There's nothing to do here, and I'm hardly entertainment.)"
    show mc stressed
    "You don't seriously expect her to stay here, do you? That's not a real life. Real life is outside."
    "Waiting is all that she's been doing for her whole life so far. She's only got three days."
    "You'd make her cry again."
    show mc vstressed
    m "(I get it! I GET IT!)"
    "Good. If you don't..."
    m "(I know! I'll disappoint her. I'll ruin her life. Ugh, being a parent is difficult.)"
    show mc sad
    m "(Ugh. Why the outside though...)"
    show mc normal
    m "What if..."
    "If you say it, you have to go through with it."
    "You know this. So say it. Bind yourself with your own words. And force yourself to a fate you hate with this guilt."
    m "...Urk, what if we go... somewhere else to pass the time?"
    show alice sigh
    a "*Sigh* That's not..."
    show alice confused
    a "...!"
    show alice surprised
    a "OOOOOOOOH! I understand! You want to go on a DATE!"
    show mc shocked
    m "A date!? I never-"
    show alice laugh
    a "AaaaAAaaaaAAaa! Yes! Wonderful!"
    show alice flirt
    a "Geez, %(player_name)s! I thought you were being purposefully obtuse or something, but you DO understand, hehe~! Of course we can go!"
    show mc worried
    m "I didn't say DATE!"
    show alice worried
    a "Eh? Wait, so... you {i}don't{/i} like me?"
    show alice vcry
    a "%(player_name)s..."
    show mc stressed
    m "No no no! Don't cry! This is a misunderstanding! That's not what I'm saying at all!"
    a "But I just want to go out with you!"
    show mc confused
    m "Yes! We'll do that!"
    a "And talk with you!"
    m "Yes!"
    a "And... and hold your hand!"
    show mc normal
    m "..."
    show alice vvdespair
    a "*Sob* So I'm going to die without holding a hand... I'll miss out on it!"
    show mc stressed
    m "Okay, {i}fine{/i}! Just don't cry, please."
    show alice sadsmile
    a "So you promise we can do all that?"
    show mc normalside
    m "...Yes."
    show alice laugh
    a "Aw, you're the best! Thank you, %(player_name)s~! I love you!"
    show mc shocked at bounce
    "{size=+40}WHAT?"
    m "{size=-10}W-what... {size=-20} did she just say?"
    show alice happy
    a "So where are you taking me?"
    show mc stressed
    m "(Okay, if she's not addressing it, clearly it wasn't serious.)"
    "You're heart actually stopped for a second, haha. As if she'd be interested in you that way."
    show mc normalside
    m "(Getting out this room would be nice, but that said, I don't actually want to leave.)"
    show mc stressed
    m "(The connundrum of a socially anxious person. If only there a place super close by, with no people, and had something nice to show Alice...)"
    show mc surprised
    m "Ah. Actually..."

    stop music fadeout 2
    scene black with fade

    scene rooftop with fade
    show alice_base_buns at left
    show alice laugh at left
    show dress polkadot at left

    show mc happy at right

    with easeinbottom
    play music "trip.mp3"
    a "Oooh~ Eek, it's soo windy up here! I'm getting a little cold."
    show mc annoyed
    m "Yeah, same."
    a "..."
    show alice sly smile
    a "I sure wish I had something warm~"
    show mc normal
    m "..."
    show mc awed
    m "Oh! Uh, should I go back down and grab a jacket for you? It's great at insulating."
    show alice sigh
    a "No, no, nevermind. Just stay here."
    show alice cute
    a "So what did you want to show me?"
    show mc normal
    m "Well, you can see the stars pretty well up here."
    m "..."
    a "..."
    show alice confused
    a "Um... what exactly are you going to show me?"
    show mc confused
    m "I'm already showing you - the stars!"
    show alice flirtsweat
    a "O-oh!"
    a "Those... tiny... white... dots?"
    show mc awed
    m "Yes. Aren't they beautiful?"
    show alice happy
    a "If you think so, then I agree."
    show alice normal
    m "Don't you think it's terrifying how far away they are?"
    m "Each one is a different place with its own conditions. There's so much out there that we will never know."
    show alice normalside
    a "Mhm~"
    show mc stressed
    m "Sometimes, it feels like life has lost its magic, and I'm just going through the motions while times slips by."
    show alice surprised
    a "How unexpectedly... depressing."
    m "But when I see the stars, I think of possibilities and mysteries and how grand everything is."
    m "I always forget how lucky I am to be alive."
    show alice happy
    a "Aw, I'm lucky too!"
    show alice cute
    "My master is big-hearted and understanding. He takes good care of my every needs and puts me first!"
    show alice laugh
    a "How much luckier can I get than that?"
    show mc sad
    "But her words only make you feel more guilty."
    "You're only doing all of this out of a sense of responsibility. You're not kind. You just can't handle disappointing someone."
    show alice happy
    a "%(player_name)s, can I hold your hand now?"
    show mc worried
    m "Do you... have to?"
    show alice pout
    a "You don't want to hold my wonderful, petite, perfect little hand?"
    show mc stressed
    m "If you don't mind..."
    show alice cruel
    a "!"
    show alice hime
    show mc normal
    a "On second thought, I'm going to look more at the stars and really appreciate what you've shown me!"
    
    show alice look_up
    show alice at slightleft
    show dress at slightleft
    show alice_base_buns at slightleft    
    with move
    "Staring up, Alice suddenly walks to the edge of the rooftop."
    a "I wish I could just SEE them better."
    show mc confused
    m "Me too, but you shouldn't walk so close to the edge."
    a "Mm, I can't-"
    show alice shocked
    a "EYAAAA! I'M GONNA FALL! HELP!"
    show mc shocked at center with move
    m "Got you!"
    show alice at center
    show dress at center
    show alice_base_buns at center
    show mc at right 
    with move
    "In a burst of panic, you grab Alice's waist and yank her back to safety."
    show mc stressed
    m "Oh my God! You need to be more careful! That could have gone so wrong!"
    "For a second of relief and draining adrenaline, you close your eyes."
    show alice cruel
    a "{size=-20}Hehe."
    show alice vcry
    show mc confused
    m "Are you okay?"
    a "I-I-I-"
    show mc awed
    m "Hey, hey, it's okay! You're safe now."
    show mc cute
    m "Just breathe in and out slowly, and you'll calm down."
    show alice vvdespair
    a "{sc=3}{color=#000000}I was going to die! If you hadn't caught me, I-I... I-I!"
    show mc worried
    m "(What do I do to calm her down!? I can't just continue to awkwardly stand and stare at her while she weeps.)"
    show mc confused
    m "Is there anything I can do-"
    show alice happy
    a "Hold my hand!"
    show mc surprised
    m "(That was fast.)"
    show alice worried
    a "Please? If you had done as you'd promised in the first place, none of this would have happened."
    show mc normalside
    "That's true. She wouldn't have walked off. It's your fault."
    "Defeated, and just glad that she's not crying anymore, you hold out your hand for Alice, who eagerly grabs it and beams."
    show alice laugh
    a "Hehehe~ Ah, isn't so wonderful, %(player_name)s? I love holding your hand! Now we're even closer!"
    m "I guess..."
    m "(This is too embarrassing to look at her in the eyes.)"
    m "(But also, she didn't plan this, did she? That sw)"
    show alice cutesad
    a "Thank you for saving me back there. I'm just {i}so{/i} clumsy!"
    show alice cute
    a "But my hero was there to save me! Please allow me to bestow a gift in acknowledgement of your deed."
    show mc shocked
    m "Wait wait-"
    show alice flirt
    "Alice leans over and kisses your cheek."
    "You freeze. Her kiss burns into your cheek, even after she moves away."
    a "Mmm, you..."
    show alice flirtsweat
    a "Wow. You kinda have a really... {i}manly{/i} odour, %(player_name)s."
    "SHE SAYS YOU STINK!"
    show mc worried
    m "I'm so sorry! I wasn't expecting company and... ugh... this is so embarrassing."
    show alice happy
    a "No need to feel embarrassed around me. I'm dying soon anyway. Uh-"
    show alice flirtsweat
    a "What I mean is! Why not go take a shower now and I'll wait for you in your room?"
    show mc sad
    m "I hate to make you wait for me."
    show alice happy
    a "Nonsense! If you're happy, then I'm happy, so go take care of your needs!"
    show mc stressed
    m "Hah. Okay, thanks. See you soon."
    stop music fadeout 2
    
    window hide
    hide mc with easeoutbottom
    scene black with dissolve
    window show
    # shower chibi?
    "One wonderfully uneventful shower later..."
    window hide

    scene bottle_phone night with Fade(1, 1.0, 1):
        zoom 0.9 
    play sound "door.wav"
    play music "night.mp3"
    show mc happy at right
    with easeinbottom
    window show
    m "I have been reborn."
    show mc surprised
    m "Whoa! Uh, Alice...?"
    window hide
    show alice_base_buns at left
    show alice happy at left
    show dress polkadot at left
    with easeinbottom
    window show
    a "Welcome back, %(player_name)s~ Enjoy your shower?"
    m "You cleaned!"
    show alice hime
    a "Mhm~ I suppose I did! Why? Does it make you feel happy or something?"
    show alice wink
    a "Perhaps, super duper grateful?"
    m "Yeah! It looks great!"
    show mc stressed
    m "I'm just sorry you cleaned up after me. You shouldn't have folded all those dirty clothes."
    show alice happy
    a "I shouldn't have? Good!"
    show mc confused
    m "...?"
    show mc normal
    m "Where did you put my clothes, by the way?"
    show alice confused
    a "Oh, those dreadful rags? I just tossed them out the window."
    show mc shocked
    m "(She didn't!)"
    "She put your dirty-ass clothes on the pavement for everyone to see and smell?"
    "You can't collect them now! If you did, everyone would know who to be annoyed at!"
    show alice cute
    a "You're welcome!"
    show alice cutesad
    a "You grew me, saved my life, and promised to always be with me. I wanted to help you some way."
    show alice happy
    a "So I'm really glad you like it!"
    show mc stressed
    m "Thank you... Um, I need to sleep. Today has been... a day."
    show alice sigh
    a "Sleep? Thank goodness!"
    show mc normal
    m "Are you also tired?"
    show alice happy
    a "No silly! It means it's snuggling time!"
    show mc normalsquint
    m "No."
    show alice pout
    a "But %(player_name)s, I'll get lonely. And it's my first night of being here."
    show alice cutesad
    a "Put yourself in my shoes. You're such a kind man. I know you'll understand."
    show mc vannoyed
    m "Nope. I'm sorry, I'm not rejecting you, but after what I've read about you, and some... signs... I know NOTHING good will come of this!"
    a "So I'm getting punished for following my instincts?"
    show mc normalside
    m "Yes. Get used to repressing your desires. That's life. I'm just not comfortable with physical touch."
    show alice serious
    a "Only because you're a first-timer! After a little touching, you'll be addicted to my snuggles, I swear!"
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
    show alice pout
    a "{size=-20}Not even crying?"
    "Realising that she's not going to leave on her own, you sigh, clasp her shoulders, and direct her right onto the desk chair."
    show mc normal
    m "You know what, Alice? I just want a good night's sleep. I don't have the energy for this."
    m "I've got my laptop open right there. Why don't you face the screen and learn a little about the world?"
    m "Maybe you'll understand more about yourself too."
    show alice cutesad
    a "But... how do I do that? I can't interpret the squiggles."
    show mc awed
    m "Like this."
    "You lean over to operate the mouse."
    show alice normal
    show mc normal
    m "Look, you use the mouse to click on anything that looks interesting. *Click*. See? It's easy."
    show alice happy
    a "Mhm! I'll try to educate myself so I can be the perfect partner for you."
    "You're so tired that you don't bother to correct her. Instead, you plop into bed."
    hide mc with easeoutbottom
    show alice surprised
    a "Ooh, this lady looks so pretty..."

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "You fall asleep to the faint humming of the laptop fan..."
    with dissolve 
    pause

    jump alice_d2_morning_badroute




    # Retracted hug scene to arcade scene
    # show alice cutesad
    # a "*Sniffle* Y-yes, I need to be held right now."

    # hide mc
    # hide alice
    # hide dress
    # hide alice_base_buns

    # show alice_mc_hug_smirk
    # with dissolve

    # a "{size=-20}Hehehe..."
    # m "Are you still crying?"
    # a "*Sniffle* Y-yeah. Thank you for saving me back there. I'm just {i}so{/i} clumsy."
    # m "As long as you're safe, that's all that matters."
    # a "I'm so glad you're here with me. That you care about me."
    # a "For the longest time, it was just me, in my own little box world."
    # a "I've missed the feeling of human touch like this. It's so... reassuring."
    # m "I'm glad I could provide that for you?"
    # a "Hehe, you're funny. You sound like you're asking a question. You don't need to be so nervous around me."
    # a "Actually, I'd like it more if you could relax. If we could just... enjoy our time together more like this."
    # m "Uh... I'll try."

    # hide mc
    # hide alice
    # hide dress
    # hide alice_base_buns

    # show alice_mc_hug_smirk
    # with dissolve

    # a "When I look at those... {size=-20}"
    # a "Especially those ones over there, the purple and blue ones!"
    # show mc confused
    # m "E-eh!? Where?"
    # show alice surprised
    # a "There! They just changed colour again. Now they're green and yellow."
    # show mc shocked
    # m "WHAT?"
    # show mc confused
    # "You follow the direction of Alice's finger."
    # "Instead of pointing up to the sky, it's pointed down, below the edge of the railing, at the building across the street."
    # show mc surprised
    # m "Oh..."
    # show mc normal
    # m "The arcade. Those aren't stars, they're just ordinary lights."
    # show alice pout
    # a "Aw, but they're so pretty..."
    # show mc awed
    # m "Hm, it doesn't look too busy tonight. I wonder if..."
    # show mc worried
    # m "Ah, but I'm here with you. I shouldn't."
    # show alice hime
    # a "Aha! Gotcha!"
    # show mc surprised
    # m "?"
    # show alice sly smile
    # a "You want to go there, do you? Well, it just so happens..."
    # show alice wink
    # a "So do I!"
    # show mc confused
    # m "You don't even know what an arcade is, do you?"
    # show alice laugh
    # a "I know it's a place you want to visit, and that's all I need to know!"
    # show mc worried
    # m "But-"
    # show alice smirk
    # a "I won't allow you to be bored with me, so move your little butt over there already!"
    # show mc shocked
    # m "BUT-"
    # show black with fade
    # stop music fadeout 3

    # "You quickly learn that once Alice sets her mind to something. She gets it."
    # "After a minute of her physical pushing and verbal insistence, you finally give up and conceed. You are not match for her confidence."



    # window hide
    # hide mc
    # hide alice
    # hide dress
    # hide alice_base_buns
    # with easeoutbottom
    # stop music fadeout 2
    # scene black with Fade(0.5, 1.0, 0.5)        
    # play sound "door.wav"
    # play music "mall.mp3"
    # show chibi_mc at slightright
    # show chibi_alice at slightleft
    # with easeinright
    # window show
    
    # "As soon as you leave your dorm with Alice, she hooks her arm through yours."
    # "You instinctively freeze up, but she simply smiles at you."
    # "You don't have the heart to push her away when she looks so happy to be out together."
    # "And with your destination just across the street, it's not even worth the effort."
    # "After crossing the road, you arrive at the place you've been wanting to visit for ages."
    # window hide
    # hide chibi_mc
    # hide chibi_alice
    # with easeoutleft

    # scene arcade with fade
    # show alice_base_buns at left
    # show dress polkadot at left
    # show alice surprised at left
    # show mc surprised at right
    # with easeinbottom
    # a "Woow~ it's so dazzling!"    
    # m "Huh. Not bad. This place has good variety."
    # m "(They even have that old train game I played when I was ten!)"
    # show mc slightsad
    # m "(I've been wanting to come here for so long... Why did I stop myself?)"
    # show mc sad
    # m "(I wasted so much time...)"
    # show alice happy
    # a "Hey, %(player_name)s, you look distracted."
    # show alice wink
    # a "You weren't thinking about me, were you? Eek! You're so naughty!"
    # show mc surprised
    # m "Eh! N-no! I would never!"
    # show alice pout
    # a "How could you say that? You'll hurt my feelings..."
    # m "Urk, I just meant-"
    # show alice laugh
    # a "Haha, I'm just teasing you!"
    # show mc annoyed
    # m "Ha. Ha. Very funny."
    # show mc normal
    # m "So, wanna try play a game? I'd recommend starting with a classic, like Boba Bubble."
    # a "Aw, I appreciate that so much! But I just wanna watch you."
    # show mc surprised
    # m "You sure? Won't you get bored?"
    # show Alice pout
    # a "Don't suggest such a thing! Me? Bored? Watching you? Never!"
    # show alice wink
    # a "Come on. Show me what those fingers do."
    # show mc stressed
    # m "(Why does it always have to be an innuendo?)"
    # show black with dissolve
    # "You pop in a token, load up the game, and fly through the first few levels, while Alice oohs and aahs appreciatively at your side."
    # "You hope she's enjoying herself. Even while you're playing, you just worry that you're boring her, since all she does is just watch."
    # show alice cute
    # show mc normal
    # hide black with dissolve
    # play sound "gameover.wav"
    # show mc annoyed
    # m "Welp, I lost."
    # show alice cute
    # a "Awwww, I'm so sorry! I was probably being too distracting, hehe~"
    # a "So it doesn't count! It's a fluke!"
    # m "Really?"
    # a "Mhm! No counts! You can do it all over again!"
    # m "..."
    # a "Eeeeh? What's with the frown?"
    # m "You're just watching me. Aren't you bored?"
    # show alice surprised
    # a "You're so attentive, I feel guilty, %(player_name)s! "
    # a "Come on! Cheer up and let's go play some more games. I'll even join you this time."
    # m "You will? I thought you didn't want-"
    # a "Mhm, so you better get ready for some competition."
    # scene black with fade

    # "You and Alice shoot basketball hoops, race eachother on motorcycles, beat drums to the rhythm, and jump over virtual skipping ropes."
    # "To tie it all up, you play a crane game."
    # stop music fadeout 2
    # "..."
    # "What? You think you're suddenly good at crane games?"
    # "OF COURSE NOT! WHO IS? YOU DON'T EARN A SINGLE PLUSHIE!"
    # "But that's not what matters anyway."
    # "For the first time in a while, you feel actual entertainment. You don't even realise it, but you're smiling the whole way through."
    # window hide
    # stop music fadeout 2

    #go home, assault scene, she snaps or not.

    #home:

    











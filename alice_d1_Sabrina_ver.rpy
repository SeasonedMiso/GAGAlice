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

    stop music fadeout(2)
    scene black with fade
    show text "Four weeks of spraying later..."
    pause
    hide text with dissolve
    pause 1
    play sound "phonealarm.ogg"
    m "Nnn..."
    show bg bedroom_day_growing:
        zoom 0.9    
    show bedroom_clutter
    show black:
        alpha 0.3
    # scene day_clouds
    # show bedroom_opencurtains
    # show dirty1
    # show dirty2
    # show bottle
    # show kit_bursting
    with Dissolve(4)
    play music "dynamic_audio/clock.mp3" fadein(2)
    play sound "phonealarm.ogg"
    pause 0.5
    m "Nnnn..."
    stop music

    "Another day, you ignore your morning alarm. Honestly, I don't know why you don't just turn it off entirely."
    # "True. Your teacher probably hates you by now. If you joined today, everyone would think you shouldn't be there."
    m "In case tomorrow I'm different."
    "How? Are you hoping someone else will occupy your body and live it properly for you? I wouldn't be so optimistic."
    "You'll always be the same. You'll never improve."
    "Always tomorrow, never today. Maybe you should give up. Though you'll probably procrastinate that too."
    "Indecision is a decision in and of itself."
    m "*Muffled pillow groaning*"
    window hide
    show mc sigh at right with easeinbottom
    window show
    m "(Of course the instant I wake up, the thoughts won't stop. Now I can't even go back to sleep... What am I going to do?)"
    "Nothing. Do nothing. Stay in bed and rot."
    show mc sad
    m "I should spray the mushrooms while I have the energy."
    m "..."
    show mc surprised
    m "Uh... Was this box always so engorged?"
    stop music fadeout(2)
    na "{size=-8}Whaaaa- Rude~!{size=+8}"
    show mc awed
    m "Did it just... speak?"
    na "{size=-8}Mhm, {i}that's right!"
    show mc shocked
    m "Huh? You're actually talking to me?"
    na "{size=-8}As much as I {i}love{/i} waiting for you to rescue me, I've just about reached my limit."
    na "{size=-8}So excuse me while I rescue myself."

    window hide         
    scene alice_box_1 with dissolve
    stop sound 
    play sound "ballon.wav"
    #pause 3
    $ renpy.pause(1.0, hard=True)
    show alice_box_2
    $ renpy.pause(2.0, hard=True)
    stop sound 
    play sound "pop.ogg"  
    show alice_box_3
    #pause 2
    $ renpy.pause(2.0, hard=True)
    pause
    scene black with fade
    show bottle day:
        zoom 0.9  
    show bedroom_clutter
    # scene black with fade
    # scene day_clouds
    # show bedroom_opencurtains
    # show dirty1
    # show dirty2
    # show bottle
    with Dissolve(2)

    show day_1 at topleft
    with dissolve
    play music "normal.mp3" fadein(1)

    show mc vshocked at right with dissolve
    show alice_base_buns at left
    show dress polkadot at left
    show alice mendokusai at left
    with easeinbottom
    na "AAAAAAAAAAH~! FINALLY! *COUGH COUGH* Ugh, that better not have messed up my hairrrrr-"
    show alice flirtsweat
    na "-rrrrrr..."
    show alice laugh
    na "Heyyyyyy~! Didn't see you there!"
    na "So this is your place, huh? WOoooOOoooow! Amazing! It's so..."
    show alice confused 
    na "{size=-10}Ugh, how do I put it?"
    show alice happy
    na "Cosy! Yeah! It's so {i}warm{/i} in here! Like a snuggly, old, blanket of cuddles! SOOOOOooooo nice!"
    show mc shocked
    m "{size=+20}WHO-"
    show alice wink
    na "\"Who am I\"? Beat ya to it!"
    show mc surprised
    show alice hime
    a "I'm Alice. Easy and cute, just like me!"
    show alice sigh
    a "Trust me, you do NOT want to know my full name. Aaaaanyway-"
    show alice laugh
    a "It's such, such, such, SUCH a pleasure to finally meet you, Master!"
    show mc shocked
    m "{sc=2}{color=#000000}Master? ME?"
    show alice confused
    a "It {i}is{/i} YOU who's been growing me this whole time, right?"
    show alice shocked
    a "No... Don't tell me I just did my whole one-time entrance in front of the wrong person!"
    show mc worried
    m "I did water a mushroom...?"
    show alice sigh
    a "PHEW! Ah, for a second I thought..."
    show alice depressed
    a "{size=-20}I'd messed up."
    show alice happy
    a "But everything's perfect! So, what do you wanna do first? I'm sure you're impatient to get right to it."
    show mc shocked
    m "Wait! I-I'm still confused!"
    show mc awkwardsmile
    m "You're not {i}really{/i} a mushroom, are you? This a joke, right?"
    show alice mendokusai
    a "Huh?"
    show mc worried
    m "Or... not?"
    show alice laugh
    a "Haha! You're so funny! Are you a comedian? Of course, as my Master, you should know that I'm pure mushroomy goodness!"
    show alice wink
    a "There's not a bone in my body. Unless you want to put one-"
    show alice vannoyed
    a "*{sc=2}{color=#000000}{size=+20}COUGH COUGH*"
    show mc surprised
    m "You okay?"
    show alice sad
    a "Don't- *{sc=3}{color=#000000}COUGH{/sc}* look at me!"
    show alice vannoyed
    a "{sc=3}{color=#000000}{size=+20}E-e-e-e-HEM!" with sshake
    show alice depressed
    a "I don't usually sound this gross, okay!? I just haven't had my water yet!"
    "Alice looks around panickedly, then reaches for the spray bottle on the table."
    $ watered = 0
    show water_status at topright with dissolve
    
    play sound "spray.wav"
    $ watered = 1
    pause 1
    queue sound "spray.wav"
    $ watered = 2
    hide water_status with dissolve
    show alice sigh
    na "E-hem- Ah, much better."
    show mc awed
    m "You just sprayed yourself in the face."
    show alice wink
    a "Yup. I just love getting sprayed. If you want, you can do it next time, Master."
    show mc shout
    m "M-my name's not Master!"
    show alice happy
    a "I can call you cutie-pie if you want."
    show mc stressed
    "Uugh..."
    show alice flirtsweat
    a "Okaaaaaay then. I can see that's a hard pass. What IS your name then?"
    show mc normalside
    m "I'm..."

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
            show mc normal
            m "Uh, I'm %(player_name)s."
        
        else:
            $ playername = player_name
            show mc normal
            m "Uh, I'm %(player_name)s."

    show alice neutral
    a "Out of all the names in the world... %(player_name)s?"
    show mc confused
    m "..."
    show alice laugh
    a "It's so AMAZIIIIIING! Ha. Ha. Ha. That's literally the coolest name I've ever heard!"
    "It's the ONLY name she's ever heard."
    # show mc normalside
    # m "(It's the ONLY name she's ever heard.)"
    # show mc sigh
    # m "(But more importantly-)"
    # m "(I should just be direct with her, but her confidence is overwhelming!)"
    # "You mean, because socialising is \"too difficult\"? Ah yes, whining again, like always."
    # show mc stressed
    # m "(No, I can do this! Just... ask!)"
    show mc worried
    m "A-Alice, if you're a mushroom, then why do you look like a human?"
    show alice blushside
    a "Oh my~ You're thinking about my body? I didn't know you were such a pervert!"
    show mc shocked
    m "N-no! I didn't mean it that way!"
    a "Then again, I can't really blame you. You probably can't even help it, can you?"
    show mc stressed
    m "..."
    show alice pout
    a "What? Come on. I'm just teasing!"
    show alice wink
    a "... Unless?"
    show mc normal
    m "Can you answer the question please? Why you look like a human?"
    show mc embarrassed
    m "Because... I don't know if you know, but normal mushrooms don't usually-"
    show alice flirt
    a "Have boobs?"
    show mc vblushside
    m "That and-"
    show alice hime
    a "I know, the list goes on and on. Thank goodness you got me instead of that boring, inferior version, right?"
    show alice happy
    a "Now we can keep each other company! Speaking of, how about we do something already?"

    
    # show alice sigh
    # a "Look, I don't know why and it doesn't matter."
    # show alice wink
    # a "All that matters is that I'm here now. Don't worry your cute little head over the details."
    # show mc shout
    # m "We can't just ignore the fact that you're a TALKING, BREATHING MUSHROOM!"
    
    # a "Oh no! You asked THAT question! The one that's super secret!"
    # m "It's... a secret?"
    # show alice cutesad
    # a "Yeah! It really is. But... since you're Master and all-"
    # show mc stressed
    # m "Just call me %(player_name)s, please."
    # show alice happy
    # a "Okay, Master %(player_name)s. I'll tell you-"
    # show alice worried
    # a "But you must promise to let your brain melt!"
    # show mc surprised
    # m "I, uh, promise?"
    # show alice cutesad
    # a "Okay then.... The truth is..."
    # show alice wink
    # a "I have no idea! I was just born this way!"
    # show mc confused
    # m "..."
    # show mc vshout
    # m "Then what was the point of all that \"Can you handle the truth\" stuff!?"
    # show alice laugh
    # a "I was playing around~! Soooooorryyyyyy!"
    # show alice disappointed
    # a "Why not? I can."
    # show mc worried
    # m "Because I was expecting small, non-talking, NORMAL mushrooms!"
    # show mc vstressed
    # m "Not a whole person! And... and this is impossible! Why is this happening to me?"
    # show alice hime
    # a "In my opinion, you're lucky! Normal would be so BORING anyway! Compared to such primitive things, I'm a massive upgrade."
    # show alice sly smile
    # a "I mean, just look at me. You'd really rather take some tiny little versions of me? I bet they wouldn't have boobs."
    show mc sigh
    m "(That's what I'm afraid of! I don't want to talk to ANYONE! I just want to be alone...)"
    m "(And crawl back into bed and just scroll on my phone and forget all of this ever happened.)"
    "Ah, the dream life."
    show mc worried
    m "(Why is this happening to me? Did I make a mistake somehow?)"
    # "{size=-20}I just wanted to grow and eat some mushrooms..."
    # show alice laugh
    # a "Oh! Then there's no problem! You still can."
    # show mc surprised
    # m "I... {i}can{/i}? And that doesn't bother you!?"
    # show alice wink
    # a "Nu-uh! What's wrong with a little nibble here and down there?"
    # #a "Nu-uh!  In fact, you could nibble a certain place right now-"
    # show alice surprised
    # show mc vstressed
    # m "GAH! But this still doesn't make sense!"]
    "Who knows? For instance, are you CERTAIN you know what you ordered?"
    show mc surprised
    m "(I mean, I did check it, didn't I?)"
    m "(I didn't just buy something without looking at it properly, right? That would be completely irresponsible!)"
    "Oh yes. That would be so uncharacteristic of you... *cough cough*."
    show mc stressed
    m "S-sorry, Alice. I just need to check something."
    hide mc with dissolve
    show alice shocked
    a "Wh- You're leaving me ALREADY!?"
    window hide
    hide alice
    hide alice_base_buns
    hide dress polkadot
    with dissolve

    call screen alice_d1_checkpc_1 with dissolve

    screen alice_d1_checkpc_1:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.284 ypos 0.51 idle "pc/pc_hover.png" hover "pc/pc_click.png"
            action Jump("alice_d1_checkpc_2")


    label alice_d1_checkpc_2:
        play sound "<from 0 to 1>type.wav"
        scene website2 with dissolve
        window show
        show mc confused with easeinbottom
        m "This is the place. Hmm, everything looks normal so far. Maybe I just got a bad batch?"    
        show alice_base_buns at left
        show alice pout at left
        show dress polkadot at left
        with easeinbottom
        a "What are you doing over here?"
        show mc shocked at bounce
        m "{size=+50}GAH!"
        show mc embarrassed at right with move
        m "Oh! Uh, just trying to find out more about you and make sense of this whole situation."
        show alice laugh
        a "Ahh~ So THAT'S what it is! Now it makes sense! You're just curious about little ol me!"
        show alice flirt
        a "Why, we can get to know each other real well, so why don't you come back, we'll sit on your bed and-"
        show mc awkwardsmile
        m "C-can I just do this first?"
        show alice puppyeyes
        a "But I'm {i}tired{/i} of waiting! Pweeeease?"
        window hide
        stop music
        show alice_base_buns at center
        show dress polkadot at center
        show alice at center
        with move
        show mc vshocked
        window show
        "Pouting innocently, Alice grabs your arm and yanks it off the laptop."
        "{sc=3}{color=#000000}{cps=2}{size=+40}SHE'S TOO CLOSE."
        
        show fog_2
        show pulsingblack
        hide alice
        hide dress
        hide alice_base_buns
        hide mc
        show alice_base_buns at center
        show dress polkadot at center
        show alice puppyeyes at center
        show mc vshocked at right
        show mc at quiver
        with dissolve
        a "Don't you know how mean it is to keep a lady-"
        show alice surprised
        a "Uh..."
        show alice flirtsweat
        a "Haha! You look like you're {i}scared{/i} of me or something! Haha..."
        m "..."
        show alice pout
        a "Jeez, fine! If you wanna learn about me so badly, go ahead!"
        # a "And you're ignoring me just after I arrived! Don't you want to do something together?"
        # show alice wink
        # a "Anything you like~"
        # show mc normal
        # m "Great. Then I'd {u}like{/u} to just search this."
        
        # a "..."
        show alice_base_buns at left
        show alice pout at left
        show dress polkadot at left
        with move
        
        hide fog_2
        hide pulsingblack
        with dissolve
        play music "normal.mp3"
        "Alice releases her hold on you. You can breathe again."
        show mc vstressed at nothing
        "Freezing up like that at the touch of a woman? You're an awkward failure of a man."
        show mc sad
        m "(I'd rather not spiral right now. Just gotta focus and survive this.)"
        show mc stressed
        m "(Maybe the \"About\" page will have more info about Alice.)"
        # "Before Alice can find the right words to rebuttal you more, you continue your search."
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
        m "{sc=3}{color=#000000}WHAT?"
        m "This is insane! Mushroom girls? How did they do it?"
        "Does this mean catgirls are finally an attainable dream?"
        show mc worried
        m "(Why did they pick mushrooms of all things to turn into girls? Is this even ethical? How did this get approved?)"
        window hide
        show alice_base_buns at left
        show alice normal at left
        show dress polkadot at left
        with easeinbottom
        window show
        a "What's with that reaction? What's it say about me?"
        show mc awed
        m "You can't read it?"
        show alice vannoyed
        a "No! Ugh, stupid, inconvenient text-"
        show alice puppyeyes
        a "I mean- The squiggles don't make sense! I really can't understand aaaaaanything~! So, I'm depending on you, okay?"
        show mc sigh
        m "(I don't want to tell her everything here! It's way too intense!)"
        "Then don't tell her, and accept that you're a bad person."
        show mc vstressed
        m "(You offer the worst advice!)"
        "You can always count on that~ Teehee!"
        show mc slightsad
        m "Okay. I can try give you a summary."
        
    
    hide mc
    hide alice
    hide dress
    hide alice_base_buns
    with dissolve

    
    "Mentally preparing to talk to a mushroom about its creation, you sigh and awkwardly stand up from your desk."
    window hide

    scene bottle day:
        zoom 0.9
    show bedroom_clutter
    with fade
    show day_1 at topleft
    with dissolve
    show mc slightsad at right
    show alice_base_buns at left
    show alice normal at left
    show dress polkadot at left

    with dissolve  
    
    # -
    m "It's kind of crazy, and this'll probably come as a big shock, but apparently..."
    show mc blushside
    m "You were made for people to eat and... be {size=-20}intimate{size=-20} with."
    show alice confused
    a "What was that last part? You were mumbling in that husky voice of yours, so I couldn't quite make it out."
    show mc stressed
    m "To be intimate with!"
    a "You mean when people know each other carnally?"
    show mc vstressed
    m "(How can she just say it so casually!? Am I the only one who feels embarrassed?)"
    show alice normal 
    a "I already knew that."
    show mc surprised
    m "How? That's pretty unusual... Even humans don't even know why we were made."
    show alice laugh
    a "Call it instinct. Anything else?"
    show mc worried
    m "Well... There is something else. Do you want to know your lifespan?"
    show alice shocked
    a "So morbid!"
    show mc surprised
    m "So you don't? Surprising. If it were me, I'd want to know."
    show alice sulk
    a "..."
    show mc awed
    m "That's fine. That was everything, so-"
    show alice pout
    a "This is all your fault! Now I'm curious! Tell me!"
    show mc sad
    m "Then... It says your \"lifespan\" is three days."
    show alice confused
    a "Three days?"
    show mc slightsad
    m "..."
    # show mc awkwardsmile
    show alice happy
    a "Yeah, that doesn't mean anything to me. So what are you going to do now?"
    # m "Shortish?"
    # show alice think
    # a "..." 
    show alice 
    # show mc surprised
    # m "..."
    # a "..."
    # show mc surprised
    # m "That's it?"
    # show alice normal
    # a "Yeah?"
    show mc awed
    m "(Do some people really not care about the endless abyss of nothing that awaits us all?)"
    show mc worried
    m "(But more importantly - She's right! WHAT THE HELL DO I DO NOW!?)"
    "You've suddenly got a hot lady in your room. Well, you grew it, so not so sudden. It took weeks. But still."
    m "(I have to look after someone all of a sudden? This isn't fair! I can't do this!)"
    show mc vstressed
    "This is hopeless."
    show alice surprised
    a "Hey hey hey~ You look really stressed. Calm down, silly. Everything's okay."
    show mc slightsad
    m "I just don't know what I'm supposed to do to look after you."
    show alice puppyeyes
    a "AWWwwwwww~! That's so considerate it makes me want to throw up!"
    show mc confused
    m "..."
    show alice blushside
    a "You're so worried about me! Eek! I don't know what to say!"
    show mc embarrassed
    m "I mean... I just don't to neglect you or cause you to die."
    show alice cutesad
    a "So romantic..."
    show alice happy
    a "You don't need to look after me at all, though. I'm super duper independent! I'm the opposite of demanding."
    show mc normalside
    m "(The opposite of demanding? That would be ING -> GNI. And demand backwards would be...)"
    show alice wink
    a "I'll water myself, so you don't need to worry so much, okay? And once you're calm, we can-"
    m "(DMNA... no this is confusing. I'll break it up into section. DEM and AND become...)"
    show alice blushside
    a "... if you'd be into that. Not that I am or anything! But it could be fun, right? Maybe? Just you and me-"
    show mc stressed
    m "(So it's GNI + MED + DNA, which becomes...)"
    show mc happy
    m "(Gnidnamed! I did it!)"
    show mc normalside
    m "(... Why did I do that?)"
    stop music fadeout 2
    show alice happy
    a "..."
    show mc surprised
    m "(Oh no! I spaced out!)"
    "She's staring expectantly at you, waiting for an answer! YOU HAVE TO ANSWER! NOW!"
    show mc awkwardsmile
    m "Sorry. What was the last thing you said?"
    show alice blushside
    a "Must I really say it again? Nnn... It's embarrassing, but if you insist~!"
    show alice flirt
    a "I said: how about we take off our clothes?"
    show mc normal
    m "..."
    a "Or would you prefer if I take it off for you?"
    show mc confused
    m "I'm... sorry... Why would we be taking off our clothes?"
    show alice vflirt
    a "Oh, you know why. It's the whole reason why I'm here, after all."
    show alice wink
    a "To make you happy~"
    show mc vshocked
    m "(She's behaving just like how the website said!)"
    
    menu:
        m "(What do I do!? I can't do that with her! That would be...)"
        "Clearly reject her.":
            show mc stressed
            m "(Straight and to the point! Leave no room for misinterpretation!)"
            show mc shout
            m "No."
            show alice surprised
            a "W-"
            show alice disgusted
            a "WHAT DID-"
            show alice flirtsweat
            a "E-hem~! Aw, come on, Master %(player_name)s! There's no need to act so coy around me."
            show mc worried
            m "I'm not being coy! I-I'm reininforcing my boundaries. I'm not interested in any kind of that stuff with you."
            show alice wink
            a "Aw~ What a shame! I'm softer than you think, you know. Inside and out."
            m "(I never thought I'd be in this kind of situation, but I have to stand my ground!)"
            show mc shout
            m "No, no, no! Get away! I don't know what you want, but whatever it is-"
            show mc vshout
            show alice shocked
            m "{sc=4}{color=#000000}{size=+40}I DON'T WANT YOU!" with sshake
            a "..."
            show mc worried
            m "(Was that too harsh?)"
            show alice puppyeyes
            a "But... what else would I do?"
            show mc stressed
            m "I don't know! This was all a mistake! I didn't want you here in the first place."
            show alice sulk
            a "..."
            show mc worried
            m "Sorry. I didn't mean to say it so harshly. I'm just..."
            show mc stressed
            m "... really, REALLY not a big on {i}that kind of stuff{/i}. There's a lot going on, and... I just wanted to be upfront."
            show alice normal
            a "..."
            show alice hime
            a "Oh my~ You should have told me sooner! That sounds {sc=2}{color=#000000}HOOoooOORRIBBLEEEeeeee{/sc}!"
            show mc confused
            m "...?"
            show alice puppyeyes
            a "How hard it is for you! You must be so, SOoooOOooo stressed, %(player_name)s!"
            show mc normalside
            m "Well, yeah..."
            "Despite the fact you never do any work, you're always stressed."
            show alice happy
            a "Well, I understand now! So why don't we just calm down for a second?"
            show mc confused
            m "..."
            "Alice doesn't make anymore moves. Seems safe now."
            show mc sad
            m "Y-yeah... I'm sorry."
            show alice cute
            a "I understand. You're so tense, so aggravated, so let's just take a seat on your bed, okay?"
            show mc stressed
            m "Okay. *Inhale*... *Exhale*..."
            m "(I really panicked there, but it's all over now.)"
            show alice sly smile
            a "Mhm~ just like that. Don't you feel so much better now?"
            show mc confused
            m "I do, thanks-"
            show mc surprised
            show alice at right
            show alice_base_buns at right
            show dress at right
            with move
            # m "{i}Whoa-!"
            jump alice_bed_scene
            
        "Dodge the question.":
            show mc awkwardsmile
            m "H-hey, how could I do that? I hardly know you!"
            m "You're supposed to go out on a few dates and see if you like the other person because you can even CONSIDER that! So-"
            show alice think
            a "..."
            m "So really, it's not even a possibility... Sorry..."
            show alice vannoyued
            a "Ha."
            show mc surprised
            m "...?"
            #play music "upbeatsong.wav"
            show alice laugh
            a "Then let's go on a date! Teehee!"
            a "You'll love it, you'll see what a nice girl I am, and THEN we do it!"
            show mc shocked
            m "{sc=2}{color=#000000}No... but... I didn't agree to that either! I can't go on a date with you!"
            show alice pout
            a "Why not? You'll like the date! I'm certain of it! I deserve a fair trail! A courteous man would at least do that much!"
            show mc worried
            m "It's not YOU, it's ME! I-I don't go out on dates! I'm not fun, or attractive or-!" 
            show alice puppyeyes
            a "But it's only fair! Everyone deserves a chance! PWEASE PWEASE PWEASE PWEASE PWEASE PWEASE?"
            show mc embarrassed
            m "But... I'm not..."
            a "{size=+20}{cps=15}PWEEEEEEASE?"
            show mc stressed
            m "But I can't go outside! I can't talk to people! I can't-"
            show alice vpuppyeyes
            a "{size=+50}{cps=10}PWEEEEEEEEEEEEEEEEEEEEEASE?"
            show mc vstressed
            m "{sc=2}{color=#000000}{size=+20}AAAAAAARGH FIIIIIIINE!" with sshake
            show alice excited
            a "YAAAAAY!"
            show mc sigh
            m "(I couldn't take the pressure!)"
            show alice happy
            a "Now everything's sorted! Let's go!"
            show mc shocked
            m "A-already!? Don't I get time to prepare? This is so sudden!"
            a "I hardly need to remind you that-"
            show alice neutral
            a "I don't have time."
            show alice happy
            a "Which is why I'm ssoooooOoo glad we can go out right away, hehe~!"
            show mc worried
            m "(Okay... okay... Never been on a date before, but... how hard can it be?)"
            
            # arcade scene
                
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
            "You instinctively freeze up, but she simply smiles at you, so sweetly that you feel too presured to push her away."
            "And with your destination just across the street, it's not even worth the effort."
            "After crossing the road, you arrive at a place you've been dying to visit for ages."
            window hide
            hide chibi_mc
            hide chibi_alice
            with easeoutleft

            scene arcade with fade
            show alice_base_buns at left
            show dress polkadot at left
            show alice excited at left
            show mc embarrassed at right
            with easeinbottom
            a "WOOOOoooow~ dazzling!"
            m "Well... It's not bad. There's decent variety..."
            show mc surprised
            m "(They even have that old train game I played when I was ten! I should have come here soon)"
            m "(Maybe this date won't be so bad afterall. Did I overreact?)"
            show mc stressed
            m "(No, wait! I'm forgetting about the fact that she's got an ulterior motive!)"
            show mc normalside
            m "(Maybe I can just show her a good time and let her down gently tonight. Yeah."
            m "(Maybe once she learns how to have fun, she'll forget all about it!)"
            show alice cute
            a "Hey, %(player_name)s, you look distracted."
            show alice wink
            a "You weren't thinking about me, were you? Eek! You're so naughty!"
            show mc worried
            m "Uh... I guess... in a way?"
            a "Hehe~ I was thinking of you too~"
            show mc surprised
            m "..."
            show alice laugh
            a "Haha, I'm just teasing you!"
            show mc stressed
            m "Very funny."
            show mc normal
            m "So, shall we play a game? I'd recommend starting with a classic, like Boba Bubble."
            show alice happy
            a "Nah, I'll just watch you!"
            show mc surprised
            m "But... we can all this way! Won't you get bored?"
            show Alice flirtsweat
            a "Don't suggest such a thing! Me? Bored? Watching you? Never!"
            show alice wink
            a "Come on. Show me what those fingers do."
            show mc blushside
            m "(Why does it always have to be an innuendo?)"
            show black with dissolve
            "You pop in a token, load up the game, and fly through the first few levels, while Alice oohs and aahs appreciatively at your side."
            "You hope she's enjoying herself. Even while you're playing, you just worry that you're boring her, since all she does is just watch."
            show alice cute
            show mc normal
            hide black with dissolve
            #play sound "gameover.wav"
            show mc annoyed
            m "Welp, I lost."
            show alice puppyeyes
            a "Awwww, I'm so sorry! I was probably being too distracting~"
            a "So it doesn't count! It's a fluke!"
            show mc normalside
            m "..."
            show alice cute
            a "Mhm! No counts! You can do it all over again!"
            show mc slightsad
            m "..."
            show alice pout
            a "Eeeeh? What's with the frown? You picked this date and everyting. Why aren't you enjoying it?"
            m "Playing at the arcade is only fun when you're playing together, and you're... just {i}watching{/i} me."
            m "I'm probably just too bad at doing dates. I shouldn't be surprised."
            show alice surprised
            a "What a sensitive thing you are. I almost feel guilty, %(player_name)s!"
            show alice happy
            a "Come on! Cheer up and let's go play some more games. I'll even join you this time."
            show mc awed
            m "You will? I thought you didn't want-"
            show alice hime
            a "Mhm! so you better get ready for some competition."
            scene black with fade

            "You and Alice shoot basketball hoops, race each other on motorcycles, beat drums to the rhythm, and jump over virtual skipping ropes."
            "To tie it all up, you play a crane game."
            stop music fadeout 2
            "..."
            "What? You think you're suddenly good at crane games?"
            "OF COURSE NOT! WHO IS? YOU DON'T EARN A SINGLE PLUSHIE!"
            "But that's not what matters anyway."
            "For the first time in a while, you feel actual entertainment. You don't even realise it, but you're smiling the whole way through."
            "So happy you are, that you forget something important."
            window hide
            stop music fadeout 2

            # Return to night
            scene bottle_phone night with Fade(1, 1.0, 1):
                zoom 0.9 
            play sound "door.wav"
            play music "night.mp3"
            show alice_base_buns at left
            show alice happy at left
            show dress polkadot at left
            show mc awed at right
            with easeinbottom
            window show
            m "-Seriously, I've never seen someone memorise those combos so quickly before!"
            show alice hime
            a "Dexterity, patience, and reaction time. I don't liike to brag, but what can I say?"
            m "No, but you've got serious potential! With a bit of training, you could go-"
            show mc stressed
            m "(No. She can't.)"
            show mc sad
            m "(Her future is so limited, because of...)"
            show alice happy
            a "Well, %(player_name)s~ it seems you've enjoyed yourself."
            show mc happyside
            m "Ah... Yeah. It wasn't so bad. It was nice to go out. So, thanks."
            show sly smile
            a "I am so, so happy to hear that."
            show alice flirt
            a "SOOOOOooooooooooo..."
            a "Now that we had a successful date together, that means you want to have sex now, right?"
            show mc vshocked
            m "..."
            show alice wink
            a "I mean, that IS what you said. You said you needed to go on dates to see if you like the other person first."
            a "And that's what we did! The date was a success."
            show mc worried
            m "Um..."
            show mc stressed
            m "(What do I do!? I shouldn't have said that! Now she has these weird expectations of me!)"
            m "(I have to just be upfront!)"
            "But you lied. This is your fault."
            show alice blushside
            a "Well, %(player_name)s? Could you help me out of my dress?"
            show mc embarrassed
            m "I'm sorry, but... it's not like I could like you after just one date."
            show alice serious
            a "But you {i}said{/i}-"
            show alice flirtsweat
            a "That you just needed to see what a nice girl I am! And I AM, aren't I?"
            show mc surprised
            m "(She sounds angry!)"
            show mc worried
            m "Y-yes! I think you're great!"
            show alice flirtintense
            a "Then you like me. And if you like me-"
            show mc shout
            m "We need to go on more dates! I'm pretty sure when I first told you about this, I said \"a few\", as in plural. As in... we just need to go out again!"
            show mc worried
            m "I'm sure that'll help me like you more."
            show mc stressed
            m "(WHAT AM I SAYING!? I'M JUST MAKING AN EMPTY PROMISE!)"
            "But you can't take it back now, can you?"
            show alice confused
            a "..."
            show alice laugh
            a "Oh, you're right! You did say \"a few\"! My memory of you is completely accurate, so I'm certain of it!"
            show mc vshocked
            m "(Did I avoid it? So I'm... safe?)"
            show mc sigh
            m "(Thank God!)"
            show alice normalside
            a "Though I'm surprised you're still uncertain about me-"
            show alice laugh
            a "But that just means I need to show you how cute I am, hehe~!"
            a "Tomorrow I'll take you on the funnest, romanticest, good-feelingest date - It'll be so good, it'll blow your clothes off!"
            show mc awkwardsmile
            m "O-okay..."
            show mc embarrassed
            m "(Tommorrow... I've got to end this! The sooner the better, because there's no way I can do what she wants me to.)"
            show mc slightsad
            m "(And I know that, so why can't I just tell her? Why do I feel so pressured to agree to something I don't want to do?)"
            "Because you can't say no to people who want you to do things for them?"
            "Because you don't respect yourself?"
            "Because you'd hurt their feelings and you can't stand the shame?"
            show mc stressed
            m "(Yeah, yeah... I just want to get to bed and be alone.)"
            show mc normal
            m "Uh, thanks for the date. It was fun, but I need to sleep. Today has been a day."
            show alice sigh
            a "How poetic."
            show alice wink
            a "Okay, let's get to bed then!"
            show mc shocked
            m "You're not joining me! I-I already told you! I don't want to do that!"
            show alice cutesad
            a "Just a cuddle! You're not going to leave me by myself on my first night here, are you?"
            a "Put yourself in my high-heeled shoes. You're such a kind man. I know you'll understand."
            show mc worried
            m "(But then she'd touch me! I do NOT trust her!)"
            m "Thank you for the offer. I appreciate it, but-"
            show alice flirtsweat
            a "Wait!"
            show alice hime
            a "Don't worry! I'm prepared to compromise. What if I PROMISE, and I'm really compromising here, only to {i}spoon{/i} you? It's so basic, it's just a hug!"
            show mc confused
            m "How does that help? No!"
            show alice shocked
            a "N-not even spooning...? But why would you want to? And... this is verging on neglect here! You said you'd take care of me!"
            show alice sad
            a "Please %(player_name)s! Cuddling, affection... it's like breathing to me! And I am suffocating after today's rejections. I need it!"
            show mc embarrassed
            m "You're not allowed in my bed!"
            show alice pout
            a "{size=-20}Curses."
            "Realising that she's not going to leave on her own, you sigh, clasp her shoulders, and direct her right onto the desk chair."
            show mc normal
            m "You know what, Alice? I just want a good night's sleep. I don't have the energy for this."
            m "I've got my laptop open right there. Why don't you face the screen and learn a little about the world?"
            show alice cutesad
            a "Oh? But whatever shall I do? The squiggles... they float so incomprehensingly."
            show alice vflirt
            a "I'm such a dumb-dumb, that I guess there's no choice but to snuggle-"
            show mc annoyed
            m "OR just watch a video."
            "You lean over to operate the mouse."
            show alice normal
            show mc normal
            m "Look, you use the mouse to click on anything that looks interesting. *Click*. See? It's easy."
            m "Or you can use the voice function to ask a question and select the first result."
            show alice surprised
            a "Wait WHAT!? HOW...?"
            show alice sly smile
            a "So, this can answer {i}any{/i} question? Very interesting..."
            m "Yeah, for videos like these, you don't need to read. You can just watch and listen."
            show alice hime
            a "Thank you for showing me this. Off to bed with you!"
            show alice puppyeyes
            a "And make sure to dream about me, okay!?."
            show mc stressed
            "You're so tired that you don't bother to respond. Instead, you plop into bed."
            window hide
            hide mc with easeoutbottom
            scene black with fade
            stop music fadeout(3)
            show chibi_sleep at truecenter with dissolve
            show top_text "You fall asleep to the faint humming of the laptop fan..."
            with dissolve 
            pause
            hide top_text
            show top_text "And you have a really nice dream about flying over a city by flapping your arms."
            pause
            hide top_text
            show top_text "You see people, cars, even horses eating-"
            pause
            jump alice_d2_morning_badroute



            # m "I have been reborn."
            # show mc surprised
            # m "Whoa! Uh, Alice...?"
            # window hide
            # show alice_base_buns at left
            # show alice happy at left
            # show dress polkadot at left
            # with easeinbottom
            # window show
            # a "Welcome back, %(player_name)s~ Enjoy your shower?"
            # m "You cleaned!"
            # show alice hime
            # a "Mhm~ I suppose I did! Why? Does it make you feel grateful or something?"
            # show mc sad
            # m "Yeah. It looks... great."
            # show alice normal
            # a "Uh, that's a reaction I didn't expect. Are you okay?"
            # show mc stressed
            # m "I'm just sorry you cleaned up after me. You shouldn't have folded all those dirty clothes."
            # show alice wink
            # a "Good, because the only thing I fold, is over."
            # show mc confused
            # m "...?"
            # m "Dirty joke aside, where did you put my clothes?"
            # show alice confused
            # a "Oh, those dreadful rags? I just tossed them out the window."
            # show mc shocked
            # m "(She didn't!)"
            # "She put your dirty-ass clothes on the pavement for everyone to see and smell?"
            # "You can't collect them now! If you did, everyone would know who to be annoyed at!"
            # show alice hime
            # a "It was hard work, but you're welcome~!"
            # show alice sad
            # a "Wow, after all that hard work, my feet could really use a rub..."
            # show alice sly smile
            # a "..."
            # show mc stressed
            # m "Thanks for your help, but I need to sleep. Today has been... a day."
            # show alice sigh
            # a "Sleep? Thank goodness!"
            # show mc normal
            # m "Are you also tired?"
            # a "I'm exhausted!"
            # show alice laugh
            # a "Because I'm so tired of waiting for some good snuggles!"
            # show mc normalsquint
            # m "No."
            # show alice cutesad
            # a "But %(player_name)s, I'll get lonely. And it's my first night of being here."
            # a "Put yourself in my shoes. You're such a kind man. I know you'll understand."
            # show mc vannoyed
            # m "Nope. There are just something boundaries you just can't cross."
            # a "So I'm getting punished for following my instincts?"
            # show mc normalside
            # m "Yes. Get used to repressing your desires. That's life. I'm just not comfortable with physical touch."
            # show alice serious
            # a "Only because you're a first-timer! After a little touching, you'll be addicted to my snuggles, I swear!"
            # show mc normalsquint
            # m "..."
            # show alice sigh
            # a "Ugh, so it came to this."
            # show alice pout
            # a "Fine. I'll compromise. What if I PROMISE... only to spoon you?"
            # show mc confused
            # m "How does that help? No!"
            # show alice shocked
            # a "N-not even spooning...? This is verging on neglect here!"
            # show alice sad
            # a "Please %(player_name)s! Cuddling, affection... it's like breathing to me! And I am suffocating after today's rejections. I need it!"
            # show mc normalsquint
            # m "..."
            # show mc normalside
            # m "The only thing you need is water."
            # show alice vcry
            # a "%(player_name)s..."
            # show mc stressed
            # m "No more crocodile tears either!"
            # show alice pout
            # a "{size=-20}Curses..."
            # "Realising that she's not going to leave on her own, you sigh, clasp her shoulders, and direct her right onto the desk chair."
            # show mc normal
            # m "You know what, Alice? I just want a good night's sleep. I don't have the energy for this."
            # m "I've got my laptop open right there. Why don't you face the screen and learn a little about the world?"
            # show alice cutesad
            # a "Oh? But whatever shall I do? The squiggles... they float like "
            # show alice vflirt
            # a "I guess there's no choice but to snuggle-"
            # show mc annoyed
            # m "OR just watch a video."
            # "You lean over to operate the mouse."
            # show alice normal
            # show mc normal
            # m "Look, you use the mouse to click on anything that looks interesting. *Click*. See? It's easy."
            # show alice surprised
            # a "Whoa! Someone's in the screen! And I can hear her!"
            # m "Yeah, for videos like these, you don't need to read. You can just watch and listen."
            # show alice happy
            # a "Your wish is my command."
            # show mc stressed
            # m "(What is she, a genie?)"
            # "You're so tired that you don't bother to ask it. Instead, you plop into bed."
            # window hide
            # hide mc with easeoutbottom

            

    
    





            




    


    # a "As long as I stay focused, everything'll be perfect, Master %(player_name)s."
    # a "You'll help me... won't you?"
    # show mc stressed
    # m "(I have to help her. I'm the one who grew her after all...)"
    # "But how will you cope when looking after yourself is already such a chore?"
    # 
    # a "You WILL help me, won't you? I just a weak woman who doesn't know how to do anything..."
    # show mc confused
    # m "You seem pretty capable to me."
    # a "Won't you help me? You won't leave me all by my lonesome, will you?"
    # show mc normal
    # m "No, I won't."
    # show alice shocked
    # a "You won't help me!?"
    # show mc shocked
    # m "No - I mean, yes-?"
    # show alice depressed
    # a "*Sniffle* You're so cruel, Master %(player_name)s!"
    # show mc shocked
    # m "This is a miscommunication!"
    # show alice vcry
    # a "I don't know how I'll ever get over this!"
    # show mc shocked
    # m "(SHE'S CRYING!?)"
    # "How did you fumble your words so badly!?"
    # show mc worried
    # m "I-I already said I won't leave you, so please stop crying..."
    # show alice depressed
    # a "*Sniffle* I think the only thing that would stop me from crying right now..."
    # show alice vvdespair
    # a "No! I can't be so selfish! I-I mustn't even consider asking! *Sob*"
    # show mc stressed
    # m "Ask please! I beg you."
    # show alice vcry
    # a "Oh Master %(player_name)s... I feel so fragile, but I think what I crave most right now..."
    # show alice puppyeyes
    # a "A simple, loving hug."
    # a "Pwease? Will you engulf me in you big, manly arms and tell me everything's going to be okay?"
    

    # show alice at center
    # show alice_base_buns at center
    # show dress at center

    # with move
    # show mc surprised at bounce
    # show alice_affection at topright
    # with dissolve
    # "She's walking towards you!"
    # show mc worried

    # menu:  
    #     m "(Oh God no! Anything but a hug with a stranger!)"
    #     "Enforce your boundaries!":
    #         m "W-what are you doing!?"
    #         show alice worried
    #         a "Mm? I just wanted a hug. Pwease, Master %(player_name)s?"
    #         show mc worried
    #         m "I'm... I'm REALLY not a hugger."
    #         show alice cutesad
    #         a "Aw, then..."
    #         "Alice reaches for your hand."
    #         show mc shocked
    #         m "Gah! Don't hold my hand either! No touching!"
    #         show alice worried
    #         a "Huh? But this is what I'm supposed to do. Are you mad at me? I thought you said no hard feelings! You didn't lie to me, did you?"
    #         show mc worried
    #         m "I'm not mad at all! Seriously, I just need to keep some personal space right now."
    #         show alice worried
    #         a "But... I just wanted to clear the air... and to say thank you for everything."
    #         show mc awkwardsmile
    #         m "I can assure you that the air is cleared, and you can say anything you want from 2 feet back!"
    #         hide alice_affection with dissolve
           
    #         show alice disgusted
    #         a "Why would you do that?"
    #         show mc worried
    #         m "You're just... {i}really close{/i}!"
    #         a "I'm SUPPPOSED to!"
    #         show alice sigh
    #         a "E-hem!"
    #         show alice happy
    #         a "So just {i}relax{/i}, %(player_name)s."
            
            

    #     "Offer a consoling hug.":
    #         jump nice_route

    

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

    m "Y-you pushed me!"
    a "Oh, sweet little, %(player_name)s... You must forgive me, but you are unexpectedly skittish."
    a "One of the many things I know is that, sometimes, someone needs a {i}helpful, little push!{/i}"
    "WAIT A SECOND! Why is she looking at you like THAT?"
    m "(I-I must be misinterpreting-)"
    a "%(player_name)s... I've been so lonely~ I haven't been able to say a thing for weeks..."
    a "You understand, don't you? How horrible that can feel?"
    m "I... kinda do...? But-"
    a "Then, maybe we can help each other out."
    
    show alice_bed_2 with dissolve 
    "OOOOOH SHE'S APPROACHING! I DON'T THINK YOU'RE MISINTERPRETING ANYTHING!" with sshake
    "Are ya ready, champ? This is THE MOMENT! The one all boys wait for their entire lives!"
    m "(Of course not! I've never been so unprepared in my life! I haven't even brushed my teeth yet!)" with sshake
    m "(And I hardly know her! And she's a mushroom! And- And-!)"
    m "(I don't even want to do this!)"
    "That's strange. {b}You SHOULD want this.{/b}"
    m "(I... should?)"
    "Yes! This is what real men do when they come to college! You've seen it on tv, movies, the radio..."
    "Every man wants a cute girl! And now you've got one!"
    "So what's with the hesitance?"
    a "Oh my goodness~ Why the frown? It's just me and you here."
    "There is a clear expectation in her eyes."
    "The closer she gets, the more your body tightens with immobilising discomfort."
    a "Heeeey, don't worry so much, okay? I'm good for first-timers too."
    show alice_bed_3 with dissolve
    pause 1
    "Alice gives your cheek a gentle caress with her fingertips, sending an ice-cold bolt of pure sensation up your spine."
    "To anyone else, it would feel good, but for you, it feels wrong, as if your body rejects the notion of liking it."
    "You flinch away, but Alice grapples you before you can escape."
    m "Don't come any closer! I-I-I don't-"
    a "Come on! Stop acting like this! Why don't you like it? This is why you made me, right? So-"
    m "I don't want you! Not like this!"
    a "You'll like it! Just stop resisting-"

    show alice_affection at topright with dissolve
    
    menu:

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
    show bedroom_clutter
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
    show mc vshocked
    a "{sc=3}{size=+50}{color=#000000}WHAT THE HELL!?"
    a "{sc=3}{size=+20}{color=#000000}You just PUNCHED m! Do you \nhave a problem with me or something?"
    show mc worried
    m "I know, I'm really sorry! And technically, it was a headbutt-"
    show alice annoyed
    a "{size=+40}WHO CARES!?"
    show mc stressed
    m "You're right, sorry. I just... I couldn't do..."
    show mc embarrassed
    m "... that."
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
    m "What do you mean...? Can't you just be yourself?"
    show alice neutral
    a "What's the point of being myself if you don't like me?"
    show alice normal
    a "So if you help me here, I can fix this all."
    show mc surprised
    m "Fix what? What's the problem?"
    show alice flirt
    a "So you do want to have sex with me?"
    show mc shocked
    m "NO!"
    show alice hime
    a "Ah ha! See!? There's the problem!"
    show mc worried
    m "What the hell! That's not right! What AM I to you exactly?"
    # show alice disappointed
    # a "Why? Did you prefer THAT Alice and all her cuteness? Then tell me, and you can have it."
    show alice vannoyed
    a "Just tell me what you want!"
    show mc stressed
    m "What I WANT is for you to stop harrassing me!"
    show mc shout
    m "Stop trying to force yourself on me! I don't want you!"
    show mc normalsquint
    m "Just... stop embarrassing yourself and leave me alone already."
    show alice surprised
    a "..."
    show alice sad
    a "..."
    show alice cry
    a "Ugh!"
    show alice angry tears
    a "Fine! You've rejected me enough. I failed! I get the point!"
    show mc slightsad
    m "..."
    a "But if you don't like me, maybe someone else will!"
    window hide
    hide dress
    hide alice_base_buns
    hide alice
    with easeoutbottom

    play sound "door.wav"

    
    window show
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
    m "I didn't mean to make her cry... I just needed her to stop."
    play sound("phonealarm.ogg")
    show mc shocked
    m "AAH!"
    show mc awed
    m "Oh, my phone got a message."
    window hide
    hide mc with dissolve
    show bottle_phone day:
        zoom 0.9
    with dissolve
    call screen check_phone_alice_1 with dissolve
    
    screen check_phone_alice_1:
        imagebutton:
            xanchor 0 yanchor 0 xpos 0.371 ypos 0.370 idle "pc/phone_idle.png" hover "pc/phone_hover.png"
            action Jump("check_phone_alice_2")
    
    label check_phone_alice_2:
        show mc stressed with easeinbottom
        window show
        m "(Please don't be Dad. I do NOT have the energy to tell him how \"great\" today is going.)"
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
    show mc stressed
    m "(I can't overthink like again. Not right now, please...)"
    "Or you could think about it, realise how much you'll embarrass yourself, and stay here."
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
            
            "End 1: Too afraid."

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
            m "A girl's voice! Alice!"
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
            keshad "{sc=3}{color=#000000}{size=+30}KYAAAAA!"
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
            show mc vshocked at bounce
            
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
            a "Well, look who came running back."
            show alice smirk
            a "Sorry~ but I'm in the middle of something right now."
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
            


    # show afternoon_clouds
    # show bedroom_opencurtains:
    #     matrixcolor TintMatrix("#f4ca9a")
    # show dirty1:
    #     matrixcolor TintMatrix("#f4ca9a")
    # show dirty2:
    #     matrixcolor TintMatrix("#f4ca9a")
    # show bottle:
    #     matrixcolor TintMatrix("#f4ca9a")
    show bottle noon:
        zoom 0.9
    show bedroom_clutter
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
    m "{size=+20}What the fuck were you doing down there?!" with sshake
    show alice surprised
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
    show alice at quiver
    show dress at quiver
    show alice_base_buns at quiver
    ali "It-!"
    show mc vannoyed
    m "You {i}what{/i}?"
    # try to spell stuff to make it sound like she's sobbing
    show alice angry at bounce
    show dress at bounce
    show alice_base_buns at bounce
    ali "It's not {i}my{/i} fault that you ignored me!"
    ali "The only reason I went looking for someone else is because you humiliated me!"
    show mc shout
    m "How did {i}I{/i} humiliate {i}you{/i}?" 
    #show mc normalsquint
    ali "You bought me, and picked me out for one reason."
    show alice vangry tears
    ali "But when you actually see me, you THROW ME AWAY!"
    show alice serious
    ali "How am I not good enough for you?"
    show mc vannoyed
    m "What are you {i}talking{/i} about?"
    show mc worried
    m "You just came up to me, and started making advances! You're just trying to use me!"
    # m "and... saying weird stuff."
    #show mc stressed
    #m "And then you just ran away! I didn't do anything."

    show alice vannoyed
    ali "But that's why you raised me!"
    show mc shout
    m "No! It's a misunderstanding!"
    # show mc stressed
    m "I didn't know anything about you until literally five minutes ago."
    show alice sulk
    ali "So what? I'm supposed to be irresistible. That's my whole thing."
    # ali "That's my purpose." #Too on the nose
    show alice disappointed
    ali "So either there is something is wrong with you..."
    show alice sad
    ali "...or there's something wrong with me."
    show mc worried
    stop music fadeout 2
    m "..."
    show mc slightsad
    m "So that's why you went to find someone else? Sorry, I didn't mean to humiliate you."
    show alice sulk
    ali "And all he did is {i}scream{/i}."
    ali "..."
    show alice think
    ali "Maybe there {i}is{/i} something wrong with me."
    show mc confused
    ali "Maybe it's my face or..."
    show mc confused
    m "Your appearance isn't the problem. You're objectively pretty."
    show mc normalside
    m "Especially compared to someone so plain like me."
    show alice neutral
    ali "Oh yeah, self depreciation always makes people feel better."
    show mc embarrassed
    m "I just mean... You only see a problem because you care what ."



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
    show alice_base_buns at left
    show alice disappointed at left
    show dress polkadot at left
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
    show alice_base_buns at left
    show dress polkadot at left
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
    hide alice_base_buns
    hide dress polkadot
    with easeoutbottom
    window show
    "You climb into bed and close your eyes."
    "After a few seconds you feel the weight of the mattress shift and the duvet being lifted."
    show mc shocked at right
    with easeinbottom
    m "What are you doing??!!"
    show alice_base_buns at left
    show dress polkadot at left
    show alice sly smile at left
    with easeinbottom
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

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "You fall asleep to the faint humming of the laptop fan..."
    with dissolve 
    pause 3

    jump day2Morning














    

                
            




# label nice_route:
    
#     show mc stressed
#     m "(It's my fault she's crying. The least I could do is try to endure it.)"
#     m "Uuurk... okay."
#     show mc vstressed
#     "Stiffly, you open your arms and allow someone who is basically a stranger to hug you. Then, you make an attempt at reassurance."
#     #show mc and alice hug

#     m "Look, I promise help you do whatever you need to do. It's my responsibility, so... just don't cry anymore."
#     show alice cruel
#     pause 0.2
#     show alice worried
#     a "You promise? *sniff* You really, {i}really{/i} promise? No matter what?"
#     show mc surprised
#     "For half a second, you saw her face light up- No, what are you thinking? You must be imagining it!"
#     show mc normal
#     m "As long as it's not dangerous or bad."
#     show alice sadsmile
#     a "Thank you! Knowing you'll be with me makes this all a lot easier. I'm really scared of being alone..."
#     show alice flirt
#     a "I'm glad my Master %(player_name)s is such a sensitive soul. He understands me."
#     "As soon as you hear those words proclaiming her trust in you, you feel ashamed for ever doubting Alice."
#     show mc normalside
#     m "I can only promise to try my best."
#     a "Oh my! What a dedicated, responsible man you are!"
#     show mc awkwardsmile
#     m "Th-that's too much. Please stop."
#     show alice blushside at left
#     show alice_base_buns at left
#     show dress at left
#     with move
#     show alice happy
#     a "Hey... %(player_name)s..."
#     show alice flirt
#     a "Has anyone ever told you what a gruff, manly voice you have?"
#     show mc normalside
#     m "(I'm sure getting a lot of compliments. Is she... flirting with me?)"
#     "Don't disappoint yourself. She's just being nice."
#     show alice blushside
#     a "For a long, long, loooong time, I've just been trapped in darkness. And that whole time..."
#     show alice wink
#     a "I've been imagining all sorts of things we could do together."
#     show mc confused
#     m "Something in your eye?"
#     show alice sigh
#     a "{size=-20}This guy..."
#     show bottle noon with Dissolve(2):
#         zoom 0.9
#     show mc surprised
#     m "Wow, it's already afternoon? We've been talking for a while."

#     # A nice segment to put in
#     show alice flirt
#     a "Oh my! We're all alone in your bedroom and it's approaching night-time. Whatever shall we do?"
#     "She's bored. You're boring her. You're wasting her life."
#     show mc normalside
#     m "(Of course I am. There's nothing to do here, and I'm hardly entertainment.)"
#     show mc stressed
#     "You don't seriously expect her to stay here, do you? That's not a real life. Real life is outside."
#     "Waiting is all that she's been doing for her whole life so far. She's only got three days."
#     show alice normal
#     a "Um... hello?"
#     show mc vstressed
#     m "(I get it! I GET IT!)"
#     "Good. If you don't..."
#     m "(I know! I'll disappoint her. I'll ruin her life. Ugh, being a parent is difficult.)"
#     show mc sad
#     m "(Why the outside though...)"
#     show mc normalside
#     m "What if..."
#     show alice happy
#     a "Ah! Yes?"
#     "If you say it, you have to go through with it."
#     "You know this. So say it. Bind yourself with your own words. And force yourself to a fate you hate with this guilt."
#     show mc stressed
#     m "Ngg... what if we go... somewhere else to pass the time?"
#     show alice sigh
#     a "*Sigh* That's not..."
#     show alice confused
#     a "...!"
#     show alice surprised
#     a "OOOOOOOOH! I understand! You want to go on a DATE!"
#     show mc shocked
#     m "A date!? I never-"
#     show alice laugh
#     a "Yes! A wonderful idea!"
#     show alice flirt
#     a "Geez, %(player_name)s! I thought you were dense or something, but you DO understand, hehe~! Of course we can go!"
#     show mc worried
#     m "I didn't say DATE!"
#     show alice worried
#     a "Eh? Wait, so... you {i}don't{/i} like me?"
#     show alice vcry
#     a "But %(player_name)s..."
#     show mc shocked
#     m "No no no! Don't cry! This is a misunderstanding! That's not what I'm saying at all!"
#     a "But I just want to go out with you!"
#     show mc stressed
#     m "Yes! We'll do that!"
#     a "And talk with you!"
#     m "Yes!"
#     a "And... and hold your hand!"
#     show mc worried
#     m "..."
#     show alice vvdespair
#     a "*Sob* So I'm going to die without holding a hand... I'll miss out on it!"
#     show mc stressed
#     m "Okay, {i}fine{/i}! Just don't cry, please."
#     show alice sadsmile
#     a "So you promise we can do all that?"
#     show mc surprised
#     m "...Yes."
#     show alice laugh
#     a "Aw, you're the best! Thank you, %(player_name)s~! I love you!"
#     show mc shocked at bounce
#     "{size=+40}EXCUSE ME?"
#     m "{size=-10}W-what... {size=-10} did you just say?"
#     show alice happy
#     a "So where are you taking me?"
#     show mc stressed
#     m "(Okay, if she's not addressing it, clearly it wasn't serious.)"
#     "You're heart actually stopped for a second, haha. As if she'd be interested in you that way."
#     show mc normalside
#     m "(Getting out this room would be nice, but that said, I don't actually want to leave.)"
#     show mc stressed
#     m "(The connundrum of a socially anxious person. If only there a place super close by, with no people, and had something nice to show Alice...)"
#     show mc surprised
#     m "Ah. Actually... there's something I want to show you..."

#     stop music fadeout 2
#     scene black with dissolve
#     pause 1
#     scene rooftop with dissolve
#     show alice_base_buns at left:
#         matrixcolor TintMatrix("#ffbbaf")
#     show alice laugh at left:
#         matrixcolor TintMatrix("#ffbbaf")
#     show dress polkadot at left:
#         matrixcolor TintMatrix("#ffbbaf")

#     show mc happy at right:
#         matrixcolor TintMatrix("#ffbbaf")

#     with easeinbottom
#     play music "trip.mp3"
#     a "Oooh~ Eek, it's soo windy up here! I'm getting a little cold."
#     show mc annoyed
#     m "Yeah, same."
#     show alice sly smile
#     a "I sure wish I had something warm~"
#     show mc normal
#     m "Should I go back down and grab a jacket for you? I've got one that's great at insulating."
#     show alice sigh
#     a "Nevermind..."
#     show alice cute
#     a "So what did you want to show me?"
#     show mc happy
#     m "Well, you can see the stars pretty well up here."
#     m "..."
#     a "..."
#     show alice confused
#     a "Um... what exactly are you going to show me?"
#     show mc confused
#     m "I'm already showing you - the stars!"
#     scene rooftop_stars
#     show alice_base_buns at left:
#         matrixcolor TintMatrix("#c1a4da")
#     show alice confused at left:
#         matrixcolor TintMatrix("#c1a4da")
#     show dress polkadot at left:
#         matrixcolor TintMatrix("#c1a4da")
#     show mc confused at right:
#         matrixcolor TintMatrix("#c1a4da")
#     with Dissolve(3)
#     show alice surprised
#     a "O-oh!"
#     show alice neutral
#     a "Those... tiny... white... dots... that I can hardly see?"
#     show mc happy
#     m "Yeah. Aren't they beautiful?"
#     show alice happy
#     a "If you think so, then I agree."
#     show mc awed
#     m "Don't you think it's terrifying how far away they are?"
#     m "Each one is a different place with its own conditions. There's so much out there that we will never know."
#     show alice normalside
#     a "Mhm~"
#     show mc stressed
#     m "Sometimes, it feels like life has lost its magic, and I'm just going through the motions while times slips by."
#     #show alice surprised
#     #a "How unexpectedly... depressing."
#     m "But when I see the stars, I think of possibilities and mysteries and how grand everything is."
#     m "I always forget how lucky I am to be alive."
#     # show alice laugh
#     # a "Aw, I'm lucky too!"
#     # a "My master is big-hearted and understanding. He takes good care of my every needs and puts me first!"
#     # a "How much luckier can I get than that?"
#     # show mc sad
#     # "But her words only make you feel more guilty."
#     # "You're only doing all of this out of a sense of responsibility. You're not kind. You just can't handle disappointing someone."
#     m "..."
#     show alice flirt
#     a "Hey, %(player_name)s... Can I hold your hand now?"
#     show mc worried
#     m "Do you... have to?"
#     show alice pout
#     a "Whaa-? But you promised! You don't want to hold my petite little hand?"
#     show mc stressed
#     m "I'm not much of a toucher..."
#     a "..."
#     show alice cruel
#     a "!"
#     show alice hime
#     show mc normal
#     a "On second thought, I'm going to look more at the stars and really appreciate what you've shown me!"
    
#     #show alice look_up
#     show alice at actualslightleft
#     show dress at actualslightleft
#     show alice_base_buns at actualslightleft    
#     with move
#     "Staring up, Alice suddenly walks to the edge of the rooftop."
#     a "I wish I could just SEE them better."
#     show mc confused
#     m "Me too, but you shouldn't walk so close to the edge."
#     a "Mm, I can't-"
#     show alice shocked
#     a "EYAAAA! I'M GONNA FALL! HELP!"
#     show mc shocked at center with move
#     m "Got you!"
#     show alice at center
#     show dress at center
#     show alice_base_buns at center
#     show mc at right 
#     with move
#     "In a burst of panic, you grab Alice's waist and yank her back to safety."
#     show mc stressed
#     m "Oh my God! You need to be more careful! That could have gone so wrong!"
#     show alice vcry
#     show mc confused
#     m "Are you okay?"
#     a "I-I-I-"
#     show mc awed
#     m "Hey, hey, it's okay! You're safe now."
#     show mc cute
#     m "Just breathe in and out slowly, and you'll calm down."
#     show alice vvdespair
#     a "{sc=3}{color=#000000}I was going to die! If you hadn't caught me, I-I... I-I!"
#     show mc worried
#     m "(What do I do to calm her down!? I can't just continue to awkwardly stand and stare at her while she weeps.)"
#     show mc confused
#     m "Is there anything I can do-"
#     show alice happy
#     a "Hold my hand!"
#     show mc surprised
#     m "(That was fast.)"
#     show alice worried
#     a "Please? If you had done as you'd promised in the first place, none of this would have happened."
#     show mc normalside
#     "That's true. She wouldn't have walked off. It's your fault."
#     "Defeated, and just glad that she's not crying anymore, you hold out your hand for Alice, who eagerly grabs it and beams."
#     show alice laugh
#     a "Hehehe~ Ah, isn't so wonderful, %(player_name)s? I love holding your hand! Now we're even closer!"
#     m "I guess..."
#     m "(I'm too embarrassed and guilty to look at her in the eyes.)"
#     show alice cutesad
#     a "Thank you for saving me back there. I'm just {i}so{/i} clumsy!"
#     show alice happy
#     a "But my hero was there to save me! Please allow me to bestow a gift in acknowledgement of your deed."
#     show mc shocked
#     m "Wait wait-"
#     show alice flirt
#     "Alice leans over and kisses your cheek."
#     "You freeze. Her kiss burns into your cheek, even after she moves away."
#     show alice at left
#     show dress at left
#     show alice_base_buns at left 
#     with move






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




    #go home, assault scene, she snaps or not.

    #home:

    











    # A nice segment to put in
    show alice flirt
    a "Oh my! We're all alone in your bedroom and it's approaching night-time. Whatever shall we do?"
    "She's bored. You're boring her. You're wasting her life."
    show mc normalside
    m "(Of course I am. There's nothing to do here, and I'm hardly entertainment.)"
    show mc stressed
    "You don't seriously expect her to stay here, do you? That's not a real life. Real life is outside."
    "Waiting is all that she's been doing for her whole life so far. She's only got three days."
    show alice normal
    a "Um... hello?"
    show mc vstressed
    m "(I get it! I GET IT!)"
    "Good. If you don't..."
    m "(I know! I'll disappoint her. I'll ruin her life. Ugh, being a parent is difficult.)"
    show mc sad
    m "(Why the outside though...)"
    show mc normalside
    m "What if..."
    show alice happy
    a "Ah! Yes?"





    # Shower scenes
    show alice flirtsweat
    a "Wow. You kinda have a really... {i}manly{/i} odour, %(player_name)s."
    "THAT MEANS YOU STINK!"
    show mc worried
    m "I'm so sorry! I wasn't expecting company and... ugh... this is so embarrassing."
    show alice happy
    a "How about you have a nice, relaxing shower? That way I can plot- er- wait for you in your room!"
    show mc sad
    m "I don't want to make you wait for me."
    show alice pout
    a "Sometimes, you are TOO considerate, %(player_name)s! Just go take a damn-"
    show alice laugh
    a "-a damn-good shower! Go get squeaky-clean, and make sure to wash up between every fold, okay~?"
    show mc stressed
    m "(The sooner I'm out of here, the better!)"
    window hide
    stop music fadeout 2

    #hide mc with easeoutbottom
    scene black with dissolve
    play sound "shower.wav" fadein 1
    show chibi_shower at truecenter with dissolve
    pause 1
    show shower_text "One wonderfully uneventful shower later..."
    with dissolve 
    pause
    stop sound fadeout 1
    hide shower_text
    hide chibi_shower
    with dissolve

        # Day 1:

    # after agree to go on date, jump to arcade (tweak text so more context from before), at night she makes attempt bc had date and mc says no bc it's just been one, and he doesn't want to, Alice get a little annoyed, but reassures by saying that it's only been one day. She had plenty of time! She studies on pc for date
    # day 2. Wake up. Dates. At river, choose if end this all (= bad route), or if you kiss her (= mc guilt tripped and pressured into doing sexual favours because of what he said on d1 and Alice's clear expectations and impending death).
    #If bad = bad route (despair that failed).
    #If kiss = mc bails at the last second, Alice does a suicidal guilt trip. And he takes it as a threat.
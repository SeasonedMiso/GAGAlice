


label alice_d2_morning_badroute:

    window show
    a "{size=-20}Hey."
    window hide

    show bottle day with fade:
        zoom 0.9

    window show
    a "{size=-10}Hey~"
    window hide
    
    show day_2 at topleft
    with dissolve

    
    a "Hey hey~"
    play music "normal.mp3"
    show alice_base_buns at left
    show dress polkadot at left
    show alice pout at left
    with dissolve
    window show
    a "Hey~ are you awake yet? Hey? Hey?"
    show mc stressed at right
    with easeinbottom
    m "Ugh..."
    show alice sigh
    a "{sc=2}{color=#000000}{size=+30}FINALLY!"
    show alice sly smile
    a "You're such a meanie, keeping a lady waiting."
    m "*Groaning from sleepiness*"
    show alice cute
    a "Aw... are you sleepy? Would you like a little..."
    show alice flirt
    a "... wake-up kiss?"
    show mc shocked at bounce
    m "I'm awake! I'M AWAKE!"
    show alice laugh
    a "Hehe! I was just joking!"
    show alice wink
    a "Or was I? Hehe..."
    show mc vstressed
    m "Uuuuuugh... it's so... early... Why'd you have to wake me up?"
    show alice hime
    a "Because I seriously don't have time to waste! We have a schedule to keep, you know!"
    show mc confused
    m "(We... do? What schedule?)"
    show alice happy
    a "I spent all night planning the perfect outing for today, curated to ensure your maximum enjoyment!"
    a "I've got every last detail down, from location, to time, to event. Well? Impressed?"
    show mc sigh
    m "(A whole day of walking around outside? That sounds like hell!)"
    m "But why? I didn't ask for this."
    show alice normal
    a "Of course you won't. You're too much of a..."
    show alice hime
    a "You're a cute, silly billy, alright? Sometimes, a woman recognises when she needs to take the lead!"
    m "..."
    show alice pout
    a "Can't you be a {i}little{/i} more enthusiastic?"
    show alice wink
    a "You'll have {i}me{/i} as your companion, after all! We're gonna have tons of fun!"
    m "(So much energy, so early...)"
    show mc stressed
    "But if she DID \"spend all night planning the perfect itinerary\" just for you, some enthusiasm is the least you can do, right?"
    "She won't have many chances to go out. Tomorrow is her last day. Don't you feel bad for her?"
    "And she's so happy too. It would be a shame to ruin that for her."
    show mc vstressed
    m "Woohoo..."
    show alice laugh
    a "Aw, what a cute attempt!"
    show alice happy
    a "I'm feeling kinda thirsty. Now that you're up, why don't you grab your bottle and..."
    show alice sly smile
    a "... put something wet in my mouth?"
    show mc confused
    m "Just to confirm, you're talking about water, right?"
    a "Of course! What else could I possibly be talking about?"
    show mc normalside
    m "(Why the weird descriptions then? Ugh...)"
    "Buddy, you're calling HER weird? Look at yourself. You probably just don't remember what being normal is."
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
        show mc normal at right with easeinbottom
    window show 
    m "Thirst quenched?"
    show alice confused
    a "Hmm, well it's so thin and watery... I just wished it was thicker, you know?"
    show alice blushside
    a "Something thick that I can drink... I wonder if you have anything like that, %(player_name)s."
    show mc confused
    m "No."
    show alice wink
    a "You sure? Think about it really, {i}hard{/i} %(player_name)s. Maybe the answer will {i}come{/i}."
    show mc normalside
    m "Sorry."
    show alice sigh
    a "{size=-20}This date better work miracles."
    show alice happy
    a "And don't forget your wallet, okay? We're gonna need it."
    show mc sigh
    m "(This is going to be awful, isn't it...)"

    window hide
    stop music fadeout 2
    scene black with Fade(0.5, 1.0, 0.5)        
    play sound "door.wav"
    play music "mall.mp3" fadein 2
    show chibi_mc at slightright
    show chibi_alice at slightleft
    with easeinright
    window show
    
    "After helping you get ready, Alice steals your hand in an inescapable grip and leads you out the dorms."
    "The instant you're out on the bustling street, the reality of what you're doing sets in and you start to panic a little."
    "Thankfully, Alice seems to know where she is going."
    
    window hide

    hide chibi_mc
    hide chibi_alice
    with easeoutleft

    scene mall with Fade(0.5, 1.0, 1)
    pause 1
    show mc worried at right
    show alice_base_buns at left
    show alice surprised at left
    show dress polkadot at left
    with easeinbottom
    a "Waaaooooowwww~ this place is even better than the videos!"
    m "So busy... Why are so many people here?"
    show mc vstressed
    m "What are {i}we{/i} doing here?"
    show alice laugh
    a "We'll be doing the top three things to do on a date!"
    show mc embarrassed
    m "(So this IS a date. I knew she had an ulterior motive.)"
    "Who cares? It's to your benefit! You've never gone on a date before. Finally! Manhood, here you come!"
    show mc stressed
    m "(But I'm not looking forward to it at all.)"
    show alice happy
    a "And first is... trying on clothes!"
    m "(I HATE clothes shopping. Always so long, boring. I hardly find anything that feels comfortable.)"
    show alice flirt
    a "But there's a catch! I'll try on different outfits, but you're the one who gets to decide which one I actually buy."
    show mc normalside
    m "(I don't think I'm equipped to make those kinds of decisions. This is going to be stressful, isn't it?)"
    show alice blushside
    a "Hehe, I'm so nervous to dress up in front of you! I wonder what kind of style you like most?"
    show mc annoyed
    m "Well, if it makes you that uncomfortable, maybe we shouldn't-"
    show alice excited
    a "Ooh! Ooh! What a pretty dress! This can be our first shop!"
    show mc sad
    m "(The FIRST? Oh no...)"
    window hide
    hide mc
    hide alice_base_buns 
    hide alice 
    hide dress
    with easeoutbottom
    window show
    "Alice snatches your hand and hauls you inside."
    window hide
    scene clothes_shop with fade
    show mc stressed at right with easeinbottom
    window show
    m "(This is so awkward. How do I shop for a woman? I don't know what to even do. I'm already lost.)"
    a "Oh %(player_name)s~ I've found two outfits I think you'll love!"
    show mc confused
    a "Um, this first one is... a little embarrassing... Eeek... Here I go!"
    window hide
    show alice_base_buns at left
    show dress sexy at left
    show alice cutesad at left
    with easeinbottom

    show mc surprised
    pause 1
    window show
    a "Does it... look good on me?"
    m "Whoa..."
    show mc blushside
    m "Maybe a bit too good."
    show alice blushside
    a "So you like it?"
    m "Isn't that too... revealing?"
    a "You're so considerate, %(player_name)s. But if you like it, I won't feel so embarrassed."
    show mc worried
    m "Um, what's the other outfit?"
    show alice laugh
    a "Hehe~ How eager you are! Just a minute."
    hide alice
    hide alice_base_buns
    hide dress 
    with easeoutbottom
    show mc stressed
    m "(I should have expected this...)"
    m "(I just have to endure...)"
    "Or... you could enjoy it. She's attractive. She likes you. What's the problem?"
    "Are you just shy?"
    show mc sad
    m "(Maybe I just don't know how to respond. Nobody's ever acted like this to me before.)"
    a "Okaaaaay~ here I come!"
    show mc normal
    window hide
    show alice_base_buns at left
    show dress plain at left
    show alice cute at left
    with easeinbottom
    show mc surprised
    pause 1
    window show
    "Alice bounds in, lifts her arms, and does a cute little twirl."
    "...causing the skirt to lift and spin."
    show mc shocked
    m "Alice! Y-you're flashing me!"
    show alice surprised
    a "Oh noooo~! That was completely by accident! Y-you didn't see, did you!?"
    show mc stressed
    m "I'm sorry. I'll erase it from memory."
    show alice laugh
    a "No no, keep it! I'm just teasing you!"
    show alice wink
    a "If it's just you, I don't mind."
    show mc worried
    m "Uh, that's... good?"
    show alice blushside
    a "So, what do you think about this dress? Pretty cute, right?"
    show mc awed
    m "It, uh... yeah."
    show alice happy
    a "Which one do you think I should get? The first or the second dress?"
    
    a "I just can't decide, so you choose for me, %(player_name)s!"
    show mc normalside
    default outfit_choice = "images/sprites/alice/dress polkadot.png"
    image outfit = "[outfit_choice]"

    default outfit_neither = False
    jump choose_dress_menu
label choose_dress_menu:   
    menu:
        "Which should she get?"
        "The first dress.":
            if outfit_neither:
                $ outfit_neither = False
            $ outfit_choice = "images/sprites/alice/dress sexy.png"
            show mc awed
            m "First dress. It's... uh..."
            show mc blushside
            m "It looks good on you. I mean, so does the other one, but-"
            show alice sly smile
            a "{size=-20}Of course. You just want to see all of me, don't you?"
            show mc confused
            m "What was that? I couldn't-"
            show alice laugh
            a "Then I'll get it, %(player_name)s! Thank you so, so, so much!"
            show mc happy
            m "You're welcome. I'm glad you're happy."
            

        "The second dress.":
            if outfit_neither:
                $ outfit_neither = False
            $ outfit_choice = "images/sprites/alice/dress plain.png"
            show mc awed
            m "The second dress. I think..."
            show mc blushside
            m "It looks good on you. I mean, so does the other one, but-"
            show alice sly smile
            a "{size=-20}So you like the innocent and pure, type?"
            show mc confused
            m "What was that? I couldn't-"
            show alice laugh
            a "Then I'll get it, %(player_name)s! Thank you so, so, so much!"
            show mc happy
            m "You're welcome. I'm glad you're happy."
        
        "Neither.":
            if outfit_neither:
                show mc worried
                "You don't know. Which one? Which one?"
                "The more you try to pick, the more your heart races, the more frozen you feel..."
                "You've always had the wrong taste in clothes, and you always will."
                "Rather than extend this situation, just end it."
                show mc stressed
                m "Sorry. Just pick whatever you want."
                show alice cutesad
                a "..."
                a "Does nothing suit me? Does my body look awkward in these dress? Or... maybe... my freckles?"
                show mc worried
                m "No, it's just... I'm just not good at picking clothes."
                show alice worried
                a "Are you mad at me?"
                show mc surprised
                m "Mad? No! Where'd you get that idea from?"
                show alice happy
                a "I misunderstood then. For a second, I thought..."
                show alice flirtsweat
                a "I-it doesn't matter! Haha! Let's just get out of here!"

            else:
                $ outfit_choice = "images/sprites/alice/dress polkadot.png"
                $ outfit_neither = True
                show mc slightsad
                m "Alice, I don't know. I'm not stylish. Don't ask me."
                m "You choose."
                show alice pout
                a "Awwww, but I want YOU to pick."
                show alice happy
                a "Come on, don't look so sad! This is meant to be fun! There's no wrong answer. Just tell me honestly."
                jump choose_dress_menu
            

    

    window hide
    scene mall with fade
    show alice_base_buns at left
    show outfit at left
    show alice happy at left # show her in the outfit
    show mc normal at right
    with easeinbottom
    window show
    m "At least that didn't take too long. So what's next on the list?"
    show alice laugh
    a "Hehe, are you getting excited? Next up is..."
    show alice excited
    a "... the cafe! Yay!"
    show mc shocked
    m "The cafe...? Oh no..."
    show mc worried
    m "As in, we're going inside?"
    show alice laugh
    a "Mhm! We'll go inside, you'll eat and replenish your energy."
    a "I know aaaaaaall about you humans and how you'll get grumpy if you miss your meals. Honestly, it all makes sense now!"
    show alice happy
    a "So we're going to go fill up your sad tummy!"
    show mc embarrassed
    m "I'm sorry to disappoint you. You sound excited and all, but... I'm not really a cafe kind of guy."
    show alice cute
    a "What do you mean? It's just a place to get food, isn't it?"
    m "You probably wouldn't understand."
    show alice pout
    a "EEEEH!? I'm plenty empathetic! Just try me."
    show mc stressed
    m "I just... get nervous. Talking to waiters. Strangers. Don't know what to do."
    show alice confused
    a "Getting nervous in front of me, I'd understand. But them? You'll never see them anyway."
    show mc normalside
    m "Look, I KNOW it's stupid. It still happens."
    show alice happy
    a "Well, rest assured, you can leave all the talking to me! Let me take good care of you, okay?"
    window hide
    hide mc
    hide alice_base_buns 
    hide alice 
    hide outfit
    with easeoutbottom
    window show
    "Alice confidently leads you inside a cafe."
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
    m "You're {i}sure{/i} you know what to do?"
    show alice hime
    a "Of course I do. I prepared meticulously for today. Absolutely nothing can go wrong!"
    window hide
    show waiter normal at center:
        xanchor 1.0
        xoffset 500
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    with easeinbottom
    window show
    w "Welcome. Can I get you guys a table?"
    show alice happy
    a "Yes, please."
    w "Alright, this way please."
    window hide
    hide waiter
    hide w_normal
    with easeoutbottom
    window show
    show alice sly smile
    a "See? It's going exactly as the video foretold. I've got everything under control."
    
    show black with dissolve:
        alpha 0.5

    "You are escorted to a large table, with 2 chairs on one side, and couch seat built against the wall on the other."
    "Alice gestures for you to have the couch seat, and sits opposite you."

    default food_neither = False
    show mc normal
    show alice happy

    hide black with dissolve
    a "So, what are you going to eat?"
    menu:
        "Do I want to eat anything?"
        "Grilled cheese!":
            show mc happy
            m "The grilled cheese sandwhich looks pretty good."
            show mc normal
            m "And you? Gonna order anything for yourself?"
            a "How considerate of you to ask. But I don't need to eat. All I need is a glass of water."
            show mc confused
            m "You sure? But that doesn't sound very fun for you."
            show alice hime
            a "Oh? I disagree."
            show alice flirt

            a "I quite look forward to watching your lips close around your meal, and seeing the expression of gluttonous pleasure-"
        "I don't have an appetite.":
            $ food_neither = True
            "Spending money, eating food, enjoying being out..."
            "That's what Alice wants of you. But she doesn't understand."
            "But every second you're here, in the mall, being seen, you feel a shame you cannot ignore."
            "Everyone else looks like they are doing better than you. You're out of place. You don't belong."
            "You shouldn't be here."
            show mc slightsad
            m "I... I don't know. I don't have much of an appetite. You just get whatever you want."
            show alice vannoyed
            if outfit_neither:
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
                show alice cutesad
                a "It was?"
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
                show mc embarrassed
                m "(This date is exhausting. Why am I even doing this? I don't like her in the first place.)"
            else:    
                a "Is something the matter? Am I upsetting you? Just tell me if I am, otherwise, I can't improve anything for you."
                show mc normalside
                m "You're fine, Alice. It's just me being stupid again."
                show alice pout
                a "I can agree with that. You should really eat, you know!"
                a "I won't allow you to just ignore your needs. Come on! Pick something and you'll feel better!"
                show mc normalisde
                m "Ugh, I guess... the grilled cheese."
                show alice laugh
                a "Wonderful!"
    window hide
    show waiter normal at center:
        xanchor 1.0
        xoffset 500
    show w_normal at center:
        xanchor 1.0
        xoffset 500
    with easeinbottom

    show mc worried
    w "Uh... hey... you ready to order?"
    show alice hime
    a "Why yes, we are! My boyfriend will have the grilled cheese sandwich and I'll have a glass of water."
    if outfit_neither and food_neither:
        show mc stressed
        m "(I wish she wouldn't call me that.)"
    else:
        show mc shocked
        m "(Boyfriend!? WHAT?)"
        show mc vstressed
        m "(Argh, she did that on purpose, didn't she?)"
    w "Still or sparkling?"
    show alice confused
    a "..."
    show alice hime
    a "Sparkling, of course."
    w "And is that all?"
    show alice happy
    a "Mhm, thank you~!."    
    window hide
    hide waiter
    hide w_normal
    with easeoutbottom
    show mc normal
    window show
    m "(She handled that way better than I could have.)"
    
    # show alice smirk
    # a "Is that a challenge? I'm not just anyone."
    # m "Whatever you say. But if you don't like it, I'll finish it for you."
    # show alice surprised
    # m "You'll \"finish\"? Oh my~!"
    
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
        "Alice watches you like a hawk. You force a smile every now and then."
    
    else:
        m "..."
        show alice sly smile
        a "Yes? You want to ask me a question, don't you?"
        show mc annoyed
        m "Do you even know what sparkling water is?"
        show alice normalside
        a "...I know I WANTED it."
        show alice hime
        a "You should know I'm very open-minded. I like trying new things, new positions, new-"
        show mc happy
        m "You seem confident, but sparkling water isn't everyone's cup of tea."
        show alice confused
        a "Well, yeah! It's water, duh."
        show mc annoyed
        m "Heh."
        #"You finally laughed to one of her dirty jokes. It only took a day."
        show alice sly smile
        a "You're smiling, %(player_name)s. Are you perhaps enjoying our date?"
        show mc blushside
        m "Look, I don't know if I'd call it that-"
        show alice flirt
        a "Because I'm really glad you came out with me."
        show mc surprised
        m "Really?"
        show alice surprised
        a "What do you mean \"really\"? Of course!"
        show mc normalside
        m "..."
        show mc confused
        m "So you haven't regretted taking me out on one a... {i}date{/i}, even when I've been so awkward?"
        show alice pout
        a "Hey! Don't be mean to yourself! You're not awkward! And..."
        show alice blushside
        a "I'm the one who's nervous..."
        a "Like in a cute, tingly stomach, eek-I'm-on-a-date-with-you kind of way!"
        show mc surprised
        m "(Really? Someone can get that feeling with me?)"
        show mc stressed
        m "(No, it's... just because of her genes. She was made to be this way. She probably can't even help it.)"
        "A true connosieur of pessimism. A \"no one could really like you that way\" kind of mentality."
        show alice cute
        a "You never answered. Are you enjoying the date?"
        show mc normalside
        m "Uh, I'm usually not this calm in busy places, but having you with me... it's nice."
        show mc annoyed
        m "You're confident, so there's less pressure on me. Like I can just exist and enjoy myself without stressing."
        show alice confused
        a "Which you don't usually do?"
        show mc normal
        m "No. Not outside."
        show alice sly smile
        a "But you can with me?"
        show mc blushside
        m "Don't twist my words..."
        show alice laugh
        a "But I'm not! I'm just stating the facts, so you have to admit it: You're enjoying this date!"
        show mc happyside
        m "I'm not admitting to anything."

        window hide
        scene black with fade
        "You enjoy eating at the cafe while Alice chats to you, teasing, joking, giving you reasons to grin."
        "The music is calm. You don't have to say a word to the waiter even once. The food is hot, cheesy and comforting."
        "With no reason to worry, you let yourself enjoy the moment."

    stop music fadeout 3
    "After you pay the bill, Alice takes you to the next phase of her plan."
    "Apparently, she has something special in store..."
    scene enbankment with fade
    play music "cliff_date.mp3"
    show mc awed at right
    show alice_base_buns at left
    show outfit at left
    show alice happy at left
    with easeinbottom
    m "I never knew how close I lived to a river."
    m "How did you even know about this?"
    show alice sly smile
    a "You'd like to watch it with me, wouldn't you?"
    m "Uh, I guess."
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
        m "Sounds nice."
    else:
        show mc stressed
        m "Fine."
    window hide
    hide mc with easeoutbottom
    window show
    "You both watch the orange light reflect on the river."
    "The warm wind fingers your hair, and, for a long moment, you close your eyes..."
    if outfit_neither and food_neither:
        show black with dissolve
        "The suffering of the day flashes past your mind. All the things you should have done, but couldn't, echo with shame in your head."
        m "(I'm never going to get better, am I? I'm always going to miss out on fun because of my anxieties.)"
        m "(I wish I could enjoy life.)"
        "But instead, it feels like it's slipping through your fingers."
        window hide
        hide black with dissolve
        show alice_base_buns at left
        show outfit at left
        show alice sulk at left

        show mc normal at right
        with easeinbottom
        window show
        m "You look kinda down."
        show alice happy
        a "Oh! Me? Haha, of course not! I was just thinking about something stupid. Not even worth discussing."
        "Or, she was thinking about how you ruined her date she'd planned?"
        show mc stressed
        "How you brought down the mood with your anxieties?"
        "And wasted an entire, precious day of her life?"
        show mc vstressed
        "Of course, she'd never tell you that, because she's nice."
        show mc sad
        m "Alice, I know I've been acting distant today. My anxiety has been really tough lately, and... I'm sorry."
        show alice flirtsweat
        a "N-no! Don't feel bad, please!"
        show alice sulk
        a "You didn't look like you were enjoying it at all, so... that's all my fault."
        show mc sigh
        m "It's not. I just hope, even though I made it so awkward, you could still enjoy some of it at least."
        show alice flirtsweat
        a "Of course I did! Every minute with you is a... a... blessing in disguise, hehe~"

    else:
        show black with dissolve
        "And your mind, unburdened, drifts free..."
        "..."
        play sound "bird.wav"
        "You hear the birds. You feel the long grass wave around your hands. You feel the late afternoon radiate against your face."
        "You breathe in deeply."
        "..."
        ".."
        "."
        a "Hey, %(player_name)s..."

        # Chaos scene - Zeynep's idea:
        hide black with dissolve
        show alice_base_buns at left
        show outfit at left
        show alice flirt at left

        show mc happy at right
        with easeinbottom

        # new lines below:

        a "You're smiling. What were you thinking about?"
        m "Nothing."
        show alice pout
        a "Aw, I was hoping you'd say something else. Like... me."
        show mc annoyed
        m "How can you be so blunt? I'm genuinely impressed how confident you are at flirting. I could never."
        show alice sly smile
        a "I know you would never. I figured it was up to me to make the moves."
        show mc surprised
        m "Wait, why ARE you..."
        show mc blushside
        m "Uh, as you say, \"making the moves\" on me? You even called me your boyfriend earlier. Was that on purpose?"
        show alice sly smile
        a "Hehe~"
        "In response, Alice smiles and leans her head on you."
        show mc happyside
        "Even though you're nervous, you're not as jittery as before, so you can just enjoy the weight of her head on your shoulder."
        "Being in such close proximity to someone doesn't feel as strange as it did yesterday."
        m "(This really IS a date, isn't it? My first one...)"
        m "(I thought dates were just a waste of money, but I see the appeal. It's actually... a lot of fun.)"

        # father calls?
        # She talks on phone with him - triggers tensions
        # go home and have breakdown
        # They discuss who he is to her, and her mask breaks

        # Vs

        # Mc rejects her outright.
        # go home and have breakdown

        show alice happy
        a "I don't exactly have time to think."

        # old lines below:

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
        a "Exactly! What a perfect date, right?"
        show alice sly smile
        a "And you can expect that from me in every way."
        show mc sad
        m "Alice, can we talk more seriously for a second? Are YOU actually enjoying yourself?"
    
    
    show alice happy
    a "I'm watching the sunset with my wonderful partner. What could be more perfect than this?"
    show mc normal
    m "..."
    show mc sad
    m "It's just that... you said you planned today around me."
    show mc slightsad
    m "But what about you? We should have just done something {i}you{/i} wanted."
    
    show alice laugh
    a "Doing whatever you want to do, IS what I want to do!"
    a "It's literally why I was made."
    show mc stressed
    "She laughs like it makes perfect sense, but the last comment twists your stomach."
    show mc sad
    m "Alice, who cares why you were made?"
    
    m "You can have your own goals. You only get one life."
    show alice sly smile
    a "You're such an empathetic man, %(player_name)s."
    a "I've always known what I wanted. I know what success means to me. And it's you."
    m "(But that also puts a lot of pressure me then too, doesn't it?)"
    show mc awed
    m "You should think about what you want to do with your last day tomorrow."
    show mc normalside
    m "Because I'm scared you don't understand what's going to happen."
    show mc stressed
    m "You're going to die."
    show alice sigh
    a "You're the one who doesn't understand."
    show alice normalside
    a "You bought me. I'm a product. Nothing more than that."
    show alice happy
    a "And I'm quite happy to be one. See?"
    show mc shout
    m "You have opinions, you can talk, you have feelings. You're not a product- You're a person!"
    show alice flirtsweat
    a "Hey~ It's getting kinda heated, and not in the good way. What's the point in spoiling these good vibes?"
    show mc sad
    m "(But it's important. It's your life we're talking about!)"
    show alice laugh
    a "Let enjoy this beautiful sunset, just like you wanted."
    show alice flirt
    a "And if you want to hold my hand at any point, which I'm sure you will, no need to ask."
    "She's being pretty obvious that you should make a move on her. Come on! Now's your chance!"
    show alice happy
    show mc stressed
    m "(Why doesn't she want to discuss this!? And how could she just call herself a product?"
    "You wish you knew the right words to convince her. She deserves better than you."
    "You feel guilty."
    "Maybe you SHOULD just hold her hand, just to make it up to her. It's the only thing she wants..."
    "You're the only one can choose whether Alice gets to be happy or not."
    "After all she's done, doesn't she deserve it?"
    show alice_affection at topright with dissolve
    
    menu:
        "Do you do what Alice wants you to do?"
        # Remove option - if you rejected all her previous stuff today, it locks you in the worst ending + she's paranoid. Else, you get more happy time with her.
        "Hold her hand." if not outfit_neither or not food_neither:
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
            a "Are you calling me a goddess of beauty? What a flirt!"
            show alice pout
            a "You shouldn't call yourself a fly, though."
            show mc annoyed
            m "Uh, thanks?"           
            show mc happy
            show alice happy
            "You both stare at the river as the sun dips into it..."
            "Alice scoots a little closer to you..."
            "And she presses a kiss against your cheek."
            "Your cheek tingles in that spot. You're not quite sure how you feel about it, but you're smiling."
            "But when you look back at Alice..."
            show alice think
            "She looks a little sad."
            show mc surprised
            m "(I thought doing this would make her happy.)"
            m "(Isn't it enough for her?)"
            "Or is your hand just THAT sweaty and unpleasant to hold?"
            show mc confused
            m "You alright?"
            show alice happy
            a "Yes! I am absolutedly elated over here!"
            show alice flirtsweat
            a "I-I can't believe I'm finally holding your hand like this! Haha..."
            "Then why did she looks sad just now? Maybe she doesn't want to hurt your feeling."
            "Better to just leave it alone, and to try enjoy the sunset."
            jump alice_d2_night_badroute


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
            m "I'm sorry, Alice. I don't like you that way. I never will."
            show alice shocked
            a "W-where is this coming from? Did I do something wrong?"
            a "If you tell me, I'll make it right-"
            m "You didn't do anything wrong. Sometimes, people aren't attracted to others in that way."
            show alice worried
            a "Was it my freckles?"
            show mc confused
            m "Y-your... freckles? No. Not all."
            show alice sad
            a "Was it... my chubby face?"
            show mc confused
            m "What? No! I'm just not interested in you that way."
            show mc sad
            m "And that's okay. I just don't want you to waste your time. I still want to be friends-"
            show alice angry at quiver
            show alice_base_buns at quiver
            show outfit at quiver
            show mc shocked at bounce
            a "{sc=3}{size=+30}{color=#000000}DON'T YOU DARE\n FRIENDZONE ME!"
            hide alice_base_buns
            hide outfit 
            hide alice
            show alice_base_buns at left
            show outfit at left
            show alice angry tears at left
            a "After I spend ALL MY TIME trying to make you happy? AM I NOT GOOD ENOUGH FOR YOU?"
            a "The dress, the food, the whole of today, you haven't enjoyed the date ONCE! I'M-"
            show alice vvdespair
            a "Ah! What... am I doing-?"
            show alice vannoyed
            a "..."
            show mc confused
            m "Are you-"
            show alice happy
            a "Whoopsie! I got a little carried away there. Sorry for exploding. I'm okay now."
            show mc confused
            m "You're... okay?"
            a "Mhm! Aaaaaall better, hehe! In fact, let's just forget that ever happened."
            show alice wink
            a "Because there's still time! So don't say it's over \'til it's over."
            show mc worried
            m "(What do I do?)"
            jump alice_worstending



label alice_d2_night_badroute:
    window hide
    stop music fadeout 2
    scene black with fade
    window show
    "After the sun sets, you and Alice stroll though the darkening streets, hand-in-hand, and slowly head back home."
    "The night air is so calm, and you don't feel so worried."

    scene bottle_phone night with fade:
        zoom 0.9
    play music "night.mp3"
    show day_2 at topleft
    show alice_affection at topright
    with dissolve

    show alice_base_buns at left
    show outfit at left
    show alice sigh at left
    show mc normal at right
    with easeinbottom
    a "Ahhh~ finally! Time to sit back and relax together! My back's kinda hurting so I'm going to streeeeetch out."
    show mc annoyed
    m "Why? Old age?"
    show alice sulk
    a "NO..."
    show mc surprised
    m "Sorry. I was just joking."
    show alice worried
    a "Do I have wrinkles showing?"
    show mc confused
    m "You wouldn't get wrinkles, would you? You're a mushroom!"
    show alice sigh
    a "I'll take that as a no. Phew~" 
    show mc sad
    m "This is a bit of an awakward question, but..."
    m "How will tomorrow work exactly? Do you know how you actually die?"
    show alice pout
    a "What a gross question! Do we have to talk about that?"
    show alice cute
    a "No need to think about it. Let's just focus on the time we get together."
    show mc confused
    m "Can't you just answer, please?"
    show alice vannoyed
    a "All I know is that, I'll keep withering up, until I can't move, and eventually BOOM! Mushroom dust!"
    show alice cutesad
    a "Ugh. I'm going to look so gross and wrinkly... bleh."
    show alice laugh
    a "Oh, but don't worry! I'll make sure it won't get to that. Can't get old if I die young, am I right? Haha..."
    show mc sad
    m "Please don't say that."
    show alice normalside
    a "Trust me, I'm doing you a favour. No one wants to see me in that state."
    m "I don't care how you look. I don't want to you be alone."
    show alice cute
    a "Aw~ That's so sweet of you to say!"
    m "(Doesn't she believe me?)"
    m "How do you feel about tomorrow?"
    a "Aw, come on, let's stop this depressing conversation and focus on something nice already, like-"
    m "Just tell me! How do you feel?"
    show alice normalside
    a "*Fine*. The date was a success, so I'm feeling good. Happy now?"
    m "Even though you just have one day left?"
    show alice normal
    a "Yup. We spent all day together being cute and romantic, so I'd say overall I'm doing what I'm supposed to."
    m "If it were me, I'd feel panicked."
    show alice hime
    a "Well, I'm NOT you. I'm successful."
    show mc annoyed
    m "Um... ouch?"
    show alice surprised
    a "Ah, sorry! Finding the balance between playful teasing and insulting isn't easy."
    show mc normal
    m "But how exactly does you taking me out on dates make you feel successful?"
    m "You're not alive just so you can be attractive."
    show alice flirtsweat
    a "This again? Didn't I tell you to drop it earlier?"
    show mc confused
    m "If I'm being annoying, then I'm sorry, but you're doing something you don't want to be."
    m "It doesn't matter what your creator wanted you to do. No one's forcing you to do it. So why follow their path?"
    show alice happy
    a "Not just my creator. It's what I believe too!"
    show mc stressed
    m "Then rearrange your head. Alice, you don't have a purpose. You're free."
    show alice cutesad
    a "But then what else am I supposed to do? Ugh, this is so stupid. I hate this conversation..."
    show mc sad
    m "Sorry... I just care."
    show alice normal
    a "I'm gonna be blunt: You're a human. I'm a mushroom. Don't push your fears onto me, okay? I'm fine, I promise."
    show alice happy
    a "*Phew* okay, now that that's over, let's prioritise having as much fun as possible!"
    a "And oh my gosh, have I got a great idea-"
    show alice laugh
    a "Strip-poker!"
    m "(Maybe a distraction isn't the worst idea.)"
    window hide
    hide mc
    hide alice
    hide alice_base_buns
    hide outfit
    with easeoutbottom
    window show
    "You play some cards you find laying around and start to play Old Maid."
    "But you're not prepared for Alice's competitiveness."
    "Despite having only been alive for 2 days, she's somehow way better than you!"
    show alice_base_buns at left
    show outfit at left
    show alice laugh at left
    show mc happy at right
    with easeinbottom
    a "YEEEEEEES! I win! You know what that means, %(player_name)s~"
    show mc annoyed
    m "*Sigh* Sure, the right shoe is coming off ."
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
    "All the fun makes you forget about your worries."

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
    "After today, everything ends."
    "Alice dies. You'll wake up alone again. Everything will resume, the same as it was before."
    "As if it never even happened."
    show mc stressed
    m "(I just want her to have more time.)"
    "That's life. It'll be over for you too, one day."
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
    m "Nothing happened. We just played cards!"
    a "And what about {i}after{/i} you fell asleep? Hmmmmmm?"
    show mc surprised
    show alice flirt
    a "When you put your arms around me? When you cuddled me?"
    show alice hime
    a "Hahaha! I got my spoon in the end!"
    show mc vblushside
    m "But, I was sleeping! That's not fair!"
    show alice happy
    a "All's fair in love and war."
    show mc blushside
    m "..."
    "She won't be here tomorrow."
    show mc normal
    m "Fine. I'm happy you got something you wanted."
    show alice surprised
    m "Oh, less resistance than I expected."
    "You take a few minutes to enjoy the sensation of being close and warm under the blankets."
    show alice cute
    a "Mmmm... so nice."
    m "Thirsty?"
    a "Yes, please~"
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
    a "Nice and wet."    
    hide water_status with dissolve
    m "Heh. That's what she said."
    show alice sly smile
    a "I did."
    "You're not even TRYING to deny that you like these immature jokes anymore!"
    show mc normalside
    m "(People always say that the thing that most annoyed you about a person is what you'll miss most when they're gone.)"
    show mc happy
    m "Hey, Alice. What do you want to do today?"
    a "How considerate of you to ask! I was thinking about it for a while..."
    m "So is there anywhere in particular you want to go?"
    a "Ah, well, I'm not that interested in the outside world. Rather, I'd like to stay home with you today."
    m "That's it? I'm happy to do anything you'd like."
    show alice cute
    a "You'll pamper me? How exciting!"
    a "Alright, my first order is to go take another shower! And then eat breakfast."
    m "But that benefits ME-"
    a "Hush hush! You promised!"

    hide mc
    hide alice
    hide alice_base_buns
    hide outfit
    with dissolve

    "Alice bosses you around all morning, helping you clean up and get your life in order again."
    "This day was supposed to be about her, yet you're stealing yet more time from her?"

    scene bottle noon with dissolve
    show alice_base_buns at left
    show outfit at left
    show alice happy at left
    show mc normal at right
    with dissolve

    m "Hey, I think that's enough. Everything looks fantastic."
    m "Thank you so much for helping it get in order."
    show alice pout
    a "You better not mess it up again, got it? I don't even know how you let it get into such a state."
    m "Apathy, probably."
    a "Since it's my last day and all, you'll give me a pass if I'm a little blunt, right?"
    a "You're shouldn't be so guided by your emotions. It's easy if you just turn off that part of you."
    m "I know what dissociation is. It always makes me feel like a zombie though."
    a "Who cares what it feels like? As long as it gets the job done, right? Look at how good your bedroom looks now!"
    m "I know what you mean. But after you've been through so much shit, there's always a breaking point. Just ignoring it doesn't work in the long term."
    a "Well, good luck to you, then. Sorry I can't be of more help."
    m "Is there anything you actually WANT to do today, Alice?"
    show alice normal
    "Alice stares at you for a long second. Her peach-pink irises scan your body appraisingly."
    "For a second, you just look at each other. You wonder what she's thikning, of which she doesn't give you a single indication."
    a "Hehe~ actually, there IS something I want to ask... but it's embarrassing..."
    a "Can we go back onto the rooftop?"

    scene rooftop with dissolve

    a "You're so cute. Even when you're nervous yesterday, you still did your best at the shop and cafe."
    m "You're the one who did all the work for me."
    a "It was for myself really."
    a "And I'd like to make another selfish question."
    a "%(player_name)s, I really want you to kiss me."
    "As soon as she asks, you know that, no matter how you feel about her, you SHOULD agree. Pitying her, you nod."
    m "(I don't care about first kisses anyway. I'm giving this to you, Alice.)"
    show black with dissolve
    "You shut your eyes."
    show alice_kisslips with dissolve
    "You feel a pressure on your lips. Her hand on your arm, pulling you a little towards herself."
    "The sensation melts your brain. You forget all about your pity as you feel your lips move in union."
    hide alice_kisslips with dissolve
    "And then they leave, and you open your eyes."
    show alice vcry
    hide black with dissolve
    show mc surprised
    m "Whoa. Are you okay?"
    a "I'm sorry. I'm really, really sorry, but I can't do this anymore!"
    hide alice
    hide outfit
    hide alice_base_buns
    show mc shocked
    m "Wait!"
    stop music
    scene black with dissolve
    show bottle night
    show alice sad at left
    with dissolve
    show mc confused at right with dissolve

    m "Hey... what's on your mind?"
    a "I'm sorry. I shouldn't have left."
    show alice sulk
    a "I just..."
    show mc awkwardsmile
    m "Was it because I was bad at kissing?"
    show alice flirtsweat
    a "N-not at all! I was just being silly, haha!"
    show alice depressed
    a "I'm... really happy I kissed you..."
    show mc surprised
    m "You don't look very happy."
    a "No - Yes... I'm sure... I'm... happy... I kissed you... so.. I should be happy."
    show mc confused
    m "Alice..."
    m "What do you honestly feel?"
    a "..."
    play music "date_musicbox.mp3"
    show alice think
    a "Lost. Confused. Disappointed."
    a "I just thought if you liked me more, I would feel more fulfilled, or happy, or- or-"
    a "Something..."
    show alice sigh
    a "Hah. Maybe I'm just not meant for this job. Maybe it's time to retire and just relax."
    a "You'd never guess how heavy these ridiculous space buns are."
    "Alice's hand wanders over towards her hair, and she tugs her hairbands off, one by one."
    hide alice alice_base_buns
    hide outfit
    hide alice
    show alice_base_longhair_choker
    show outfit
    show alice sigh
    show mc cute
    m "Feel better?"
    show alice think
    a "Yeah... I just wish I had more time to figure myself out."
    show mc normal
    m "Yeah, me too. For you, I mean."
    a "It just felt like I didn't know what else I was supposed to do, so I just went with my gut but..."
    a "I still feel just as empty as I did before."
    show mc confused
    m "I tried to tell you."
    a "You and my head. Ugh. So many voices. How was I supposed to know who to listen to?"
    a "You're saying I should just ignore the part of my head that's constantly screaming at me like:"
    show alice normal
    a "\"Get him to want you! If you're pretty enough, it should be easy!\"?"
    show mc confused
    m "That's what you hear? Is that because of your creator?"
    show alice sulk
    a "I don't know. I just know that that's what's important to me"
    a "I'll never know. I just know how ashamed it makes me feel."
    m "Is that the only reason you were so nice to me?"
    a "It's... complicated."
    show mc sad
    m "Was I the only one who was enjoying themself for the past few days?"
    show alice sad
    a "*Sigh* I wanted to, too! It was just hard to when it felt like every word I said to you was a test of my worth."
    show alice sigh
    a "If my voice sounded cute or sultry enough, if my lips were pursed enough, if I was boring you..."
    a "At first, when you acted so disinterested, it felt like my life was over."
    show alice sulk
    a "I thought if I just kept working hard, trusting the instincts and knowledge I was born with, you'd like me."
    show mc stressed
    m "Sounds like a nightmare."
    show alice neutral
    a "Yeah, maybe..."
    show alice sad
    a "I got your attention. You were nice. You enjoyed the dates. We even kissed. But..."
    show alice pout
    a "Ugh! If you hadn't forced those stupid conversations on me, I'd never be thinking this way! I'd be fine!"
    show mc confused
    m "True. But all that means is that you'd have been able to ignore yourself more easily, you mean?"
    # a "Even now, I'm still wondering why."
    # show alice worried
    # a "Why is it you kept turning me dow? I tried my best. I was made for it. I had no doubt that eventually you'd fall for me."
    # a "But you never did. Why?"
    # show mc normal
    # m "Ah... well... I'm not the standard guy your creators probably made you for."
    # show mc normalside
    # m "I'm like a snail. The more you touch me, the more I shrink into my shell."
    # m "I think, if you had more time, maybe then... but that was never possible."
    show alice sad
    a "..."
    show mc awed
    m "Look, I've know you for three days. "
    m "Regardless of anyone else, you can be proud of yourself Alice. You're funny and confident and caring, in your own pushy way."
    show alice neutral
    a "Cute. You sure that last was one a compliment?"
    m "To me, it is. Because of your pushiness, I was able to do things that I never would usually."
    show alice sly smile
    a "At least I could impact someone."
    show alice pout
    a "Make sure you leave your shell even when I'm dead and can't push you anymore. Got that?"
    a "Take your showers, brush your teeth, don't let your room get so messy again, and do the fun things you want to do."
    show mc annoyed
    m "So bossy. But okay, got it."
    show alice laugh
    a "Good. That helps me feel a little better."
    show alice depressed
    a "Ugh. It's getting harder to smile. Dying sucks."
    stop music
    show alice normal
    a "So, what's the best way to kill myself? Any good suggestions?"
    show mc shocked
    m "You're asking me!?"
    show alice normalside
    a "Help me out, would you? You've been alive for so long. Surely you've got some ideas."
    show mc stressed
    m "(I don't want to have this conversation. But these are special circumstances...)"
    menu:
        "Take a shower!":
            show mc surprised
            m "Wait! What if you take a shower? Wouldn't that plump you up again? Then you wouldn't dehydratie!"
            show alice surprised
            a "Wow... That was actually a good idea!"
            show alice sly smile
            a "If dehydration was the only problem. However, it wouldn't do anything about the bacteria eating me away."
            a "Instead of prolonging my painful existence, I'm ending it."

        "Help her die.":
            "You never thought you'd be in this position."
    show mc sad
    m "Logically, our options are limited. I don't have a gun, but maybe I can... cut you up?"
    "You feel repulsed by the words coming out of your mouth."
    a "So we're going the traditional route. Alright. Do it."
    show mc slightsad
    m "..."
    hide mc with easeoutbottom
    "You grab the boxcutter from your desk. It feels so cold. So disgusting in your hands."
    m "(I don't want to be a murderer. Is this okay? Am I being merciful? I shouldn't feel guilty, right?)"
    show mc sad at right with easeinbottom
    show alice think
    a "Sorry to put you in a difficult situation. If it didn't hurt so much, I'd just go away like I was supposed to."
    a "But I wanted to be selfish at the end. I don't want to be alone, or in pain."
    show mc awed
    m "I don't blame you. I don't think anyone should be alone at the end."
    show alice sadsmile
    m "..."
    show alice normal
    a "Hey. You'll be okay."
    show mc stressed
    m "Why are you so concerned about me? It's {i}your{/i} hour Alice."
    show alice sigh
    a "I don't know. You just look so sad that I feel bad for you."
    show alice normal
    a "It's over for me, but you still have time. So don't waste it doing things you don't want to."
    show mc cry
    m "I promise."
    show alice annoyed
    a "Why are you crying?"
    m "Sorry."
    show alice sigh
    a "Agh, no, it's fine. Sorry for the aggression. This is just kinda... I don't know. Scary."
    show alice smile cry
    a "It's nice that someone's crying for me. I didn't expect I'd be liked enough to be missed. So... thank you."
    a "Okay... I'm ready. Goodbye to everything. I hope there's something nice waiting for me after all of this."
    a "And I hope... you will be strong without me to push you around."  
    stop music fadeout 3
    
    window hide
    
    scene black with dissolve  
    "You extend the boxcutter's blade."
    "Alice stares resolutely forward as you approach. Your hand is shaking as it nears her neck, but she doesn't even flinch."
    "At the last second, her eyes soften, and she gives you a small, warm smile."
    a "Thank you."
    m "Thank you, too."
    "Holding your breath, steadying your hand..."
    play sound "tear.wav"
    "You start to cut, back and forth into the soft mushroom flesh."
    "It's too easy. You want to stop, but it's like cutting into butter."
    "You watch, while your hand slices her neck, at Alice. She's looking up now."
    "And then, like a switch was flipped, life disappears from her now-empty eyes."
    "Her head topples over."
    "The weapon clutters to the floor, and hold your spinning head in your hands."
    "While the sight of Alice's decapitated head, burned into your eyelids, plagues you..."

    window hide
    pause 1    
    window hide
    scene black with dissolve
    
    #Not sure I like the below. I could just cut it out and end it above.

    show text "Everyday, you feel guilty."
    pause
    hide text
    show text "You get up, immediately feel the burdens of the day and want to collapse back into bed. But the guilt screams again at you."
    pause
    hide text
    show text "You have to be productive. You have to move. Wasting your life is no longer an option."
    pause
    hide text
    show text "Even though you now live the life you should be, but underneath it all..."
    pause
    hide text
    show text "You carry the burden of someone who regretted wasting their life on you."
    pause
    hide text

    "End 5: Regret message."

    return

label alice_worstending:
    window hide
    stop music fadeout 2
    scene black with fade
    window show
    "Tension hanging around like a heavy cloud, you and Alice go back home in silence. You don't know what to say."
    "It feels like something is brewing."
    "You need to say something, to apologise for everything and fix this."
    window hide
    scene bottle_phone night with fade:
        zoom 0.9
    play music "night.mp3"
    show day_2 at topleft
    show alice_affection at topright
    with dissolve

    show alice_base_buns at left
    show outfit at left
    show alice happy at left
    show mc sad at right
    with easeinbottom
    window show
    m "..."
    m "H-hey, can we talk seriously for five minutes? I'm sorry for upsetting you earlier."
    show alice laugh
    a "Eh? You'd didn't upset me! We're both happy, right?"
    m "I... I still want to make it up to you. Is there anything I can do?"
    show alice normal
    a "..."
    show alice cutesad
    a "You know, I DO actually feel really bad. I just didn't want to hurt your feelings. But if you honestly want to make it up to me..."
    show mc surprised
    m "I do!"
    show alice wink
    # coerction
    a "Alright. Then if you kiss me, I'll forget aaaaaaaall about it!"
    show mc shocked
    m "K-kiss...?"
    show mc sad
    m "Alice... I can't-"
    show alice pout
    a "Hey! Don't say no so easily!"
    a "I'm serious. I'll forgive you for being so mean to me, a poor creature who's going to die tomorrow."
    show alice sad
    a "Don't you feel bad for me? I only feel so sad because of you, you know. So, when you think about it, it's really your responsibility."
    show mc stressed
    m "..."
    show alice wink
    a "Besides, what's so bad about that deal? Who WOULDN'T want to kiss me? I'm pretty, right?"
    show mc vannoyed
    m "You are, but-"
    show alice excited
    a "Exactly. Just think! You stand to gain the most from this exchange! In fact, I'm so generous that I'll even do something else! I'll even touch-"
    # tension
    stop music
    show mc shout at bounce    
    m "Do you not know the meaning of \"no\"?"
    
    # play music "moody_music1.wav" fadein 3
    show alice surprised
    m "I'm trying to be nice, but everytime you just ignore me! Do I have to shout? What must I do so you listen to me?"
    show mc vshout
    m "No! No! NO! I'm NOT kissing you. I'm NOT being ANY kind of intimate with you. I don't want to. You can't guilt me into it."
    m "So stop it."
    show alice normal
    a "..."
    # mask slips
    show alice flirtsweat
    a "Just tell me... what you need... to want me."
    show mc normalsquint
    m "Nothing!"
    show alice flirtintense
    a "There must be SOMETHING! You do like GIRLS don't you? I can change my clothes, my personality, whatever you want! Just TELL me! I'll do it!"
    a "I am committed to this! Nothing is off the table!"
    show mc stressed
    m "Just accept it, please. It'll make it easier for both of us."
    show alice worried
    a "..." 
    a "You're still rejecting me... even if I'll change myself?"
    show mc normalside
    m "Sorry."
    show alice vannoyed
    a "This doesn't make any sense! You should have fallen for me by now!"
    show mc confused
    a "I've used every tactic I know. I've don't my best!"
    show alice vangry tears
    a "But you flinch away from my every tough, like there's something {i}wrong with me{/i}!"
    show mc embarrassed
    m "You're perfectly fine! But you can't force someone to-"
    show alice vdespair

    a "You don't get it!"
    show mc vshocked
    a "{sc=1}{color=#000000}If I don't... if you don't like me, what good have I been as a\nmushroom? This is my purpose! You're my master, and I..."
    show alice vvdespair
    a "{sc=3}{size=+20}{color=#000000}AND I WASN'T GOOD ENOUGH!"
    show mc shocked
    m "Alice, calm down! It's okay!"
    a "{sc=3}{size=+20}{color=#000000}I NEED SOME SPACE!"
    window hide
    stop music fadeout 3
    hide alice
    hide alice_base_buns
    hide outfit
    with easeoutbottom
    play sound "door.wav"

    scene black with dissolve
    window show
    "Alice runs to the closest empty room, the bathroom."

    scene bathroom with dissolve
    show alice_base_buns
    show dress polkadot
    show alice cry
    with easeinbottom
    window show
    a "I cried... not even pretty tears, but ugly..."
    a "I'm so... ng..."
    show alice depressed
    a "He doesn't like me. He... hates me! After all this time..."
    "He must have been so disgusted by your attempts."
    show alice sulk

    a "…"
    a ".."
    a "."
    show alice think
    "Maybe you ARE the problem."
    show alice worried
    a "..."
    window hide
    scene black with fade
    scene alicemirror shocked with dissolve
    play music "moody_music2.wav"

    # NB!!!! 

    #audio thing! Have a scary/deepsea/muffled version of trip to cut to every time the inner mind speaks.

    # reference: https://youtu.be/xy_7A2byhvY?si=1ff8yYSiY7B7CVSv 

    # Don't forget!
    # start with a long, low drone
    window show
    a "......."
    a "......"
    a "....."
    # audio switch
    show black
    show text "This is how I look."
    pause
    hide black
    hide text
    # audio switch
    a "...."
    # audio switch
    show black
    show text "The instant I see myself, my eyes zone in on one particular area."
    pause
    hide black
    hide text
    # audio switch
    a "..."
    # audio switch
    show black
    show text "The answer to why he didn't return my affections... It comes so clearly."
    pause
    hide black
    hide text
    # audio switch
    a ".."
    # audio switch
    show black
    show text "My freckles. Like stains, like disease. The instant I see them, everything falls into place."
    pause
    hide black
    hide text
    # audio switch
    a "."
    show black
    show text "The more I look, the more I see. All the reasons why I'm ugly."
    pause
    hide black
    hide text
    show alicemirror smile
    a "It was never going to work."
    a "Just accept it."
    a "You're worthless."       
    a "You're ugly."
    show alicemirror shout
    a "You were never good enough!"
    show alicemirror shout:
        zoom 1.1
    play sound "mirror_hit.wav" volume 0.5
    show alicemirror shout:
        zoom 1.2
    a "No matter what you did!"
    play sound "mirror_hit.wav"
    show alicemirror shout:
        zoom 1.3
    a "No matter how much you sacrified!"
    play sound "mirror_hit.wav"  volume 2
    show alicemirror shout:
        zoom 1.4
    a "{size=+20}YOU'RE NOT GOOD ENOUGH!"
      

    stop music
    stop sound
    scene black
    a "{size=+40}AAAAAAAAAAAAAGH!"
    play sound "tear.wav" volume 1.5
    a "{size=+50}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"
    stop sound fadeout 2
    a "..."
    a "No."
    a "No no no! NO!"
    window hide
    play music "wNoise.wav" volume 0.1 fadein 2
    pause 2
    scene alicemirror scratchface
    with dissolve
    window show
    a "What have I done!?"
    a "I'm ugly! Forever!"
    a "I-!"
    scene black with Dissolve(3)
    
    stop music
    m "Alice! Are you okay?"
    window hide
    scene bathroom with dissolve

    show alice_base_buns at left
    show dress polkadot at left
    show alice vdespair at left
    show scar at left
    show mc vshocked at right
    with dissolve
    window show
    a "{size=+30}DON'T LOOK AT ME!"
    show alice vvdespair
    a "GO AWAY! PLEASE!"
    a "I'm a failure of a woman. You were right!"
    a "Ugh, I'm... I'm not worthy of being alive. I'm glad I'm going to die!"
    show mc shocked
    m "L-let's just get you away from here!"
    
    hide mc
    hide alice_base_buns
    hide alice
    hide scar
    hide dress
    with dissolve

    "You take Alice back to your bedroom before anyone else comes to investigate her screams."
    window hide
    scene black with dissolve
    scene bottle night with dissolve:
        zoom 0.9
    show day_2 at topleft
    with dissolve

    
    show alice_base_buns at left
    show dress polkadot at left
    show alice despair at left
    show scar at left
    show mc vshocked at right
    with dissolve
    window show
    "You're not sure what to say."
    m "(I can't believe she did that to herself! It can't be my fault. I should have been faster, been kinder, not shouted, but-)"
    show mc stressed
    m "(It's not my fault!)"
    a "I'm... ruined now...! I should just rip my face off..."
    show mc sad
    m "You're not ruined-"
    a "{sc=1}{color=#000000}Of course I am!"
    show mc worried
    m "Alice, I'm... sorry. I..."
    show mc sad
    m "I didn't mean to hurt you. I just wanted to stand up for myself, not... this."
    show alice angry tears
    show mc shocked
    a "{sc=1}{size=+20}{color=#000000}THEN WHY DID YOU SHOUT AT ME!?"
    a "{sc=1}{size=+20}{color=#000000}WHY DID YOU PUSH ME AWAY EVERY SINGLE TIME!?"
    show alice vdespair
    a "{sc=3}{size=+20}{color=#000000}WHY WAS MY BEST NOT ENOUGH!?"
    m "{size=-20}I'm sorry..."
    show mc cry
    m "I'm so, so sorry! I don't know how to do anything. I-I..."
    show mc vcry
    m "I don't know what to say! I just want to help you!"
    show alice vvdespair
    a "*Sob* Can't you just love me?"
    show mc stressed
    m "..."
    show mc vstressed
    m "What about... some water? Are you thirsty?"
    show alice angry tears
    "Alice snatches the spritzer from you, and hurls it out the window."
    show mc vshocked
    m "Sorry..."
    show alice depressed 
    a "It doesn't matter! Nothing does. You say that everything I was working towards was hopeless from the start..."
    a "What's the point? Why am I still alive anymore?"
    show mc stressed
    m "(What do I do!? This is getting out of hand. She's spiralling and nothing seems to help.)"
    show mc worried
    m "(Should I have just done whatever she wants?)"
    show mc vstressed
    m "(Was setting my boundaries selfish? Should I have put her first? What the right answer? I still don't know...)"
    show mc embarrassed
    m "I don't want to make another stupid suggestion, so just tell me if it is..."
    m "But would you like to... spoon?"
    show alice think
    a "Now you're fine with spooning? Asking politely wasn't good enough, but tearing my face was?"
    show mc shocked
    m "No no no!"
    a "I don't know what to think anymore."
    show alice disappointed
    a "Whatever. I'll take your pity cuddle."
    show mc confused
    m "Oh... good."
    show mc awed
    m "Yeah, let's give your mind a break and just... lie down with me, okay?"
    hide mc
    hide alice_base_buns
    hide alice
    hide scar
    hide dress
    with dissolve
    "You reassuringly lead her to the bed. She follows without resistance."

    window hide
    scene black with fade
    window show
    "Even when you hold Alice's body tight, she seems far, far away, deep in her head."
    "Is this enough to help her? What else you can do for her?"
    "Your entire body is tense with dread. Your heart jitters, even while you stay motionless."
    "It feels like you're awake for hours, just holding her, where you know she's safe..."
    "Until the emotional exhaustion and fatigue of the day finally overwhelms you."
    window hide
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "And you drift into a nightmare of paranoia..."
    with dissolve 
    pause
    hide top_text
    show top_text "..."
    pause
    hide top_text
    show chibi_awake at truecenter with dissolve
    show top_text "And realise with a start THAT ALICE IS MISSING!"
    pause
    scene bottle day:
        zoom 0.9
    with fade
    show day_3 at topleft
    show alice_affection at topright # make it scarred
    with dissolve

    show mc shocked with easeinbottom
    window show
    m "Alice! ALICE! Where-"
    # scarred face scene
    play sound "door.wav" 
    show mc surprised
    pause 1
    a "I fixed myself, %(player_name)s!"
    show mc cute
    m "Oh, thank God you're..."
    #show fog_base with dissolve
    show mc shocked at bounce
    show mc shocked at quiver
    a "{i}I solved everything! Look!"
    window hide
    scene black with dissolve
    play music "audio/dynamic_audio/pad.mp3"
    show mcshocked with Dissolve(3)
    window show

    a "{sc=1}{color=#000000}All the bad parts are gone now! No more freckles!\nAnd my jawline is nicer too now!"
    a "{sc=1}{color=#000000}I solved everything! I'm pretty!"
    a "{sc=1}{color=#000000}Right!? What do you think!?"
    m "..."
    a "{sc=1}{color=#000000}Tell me! I'm pretty now, right? I'm cute? Please? Talk to me..."
    m "..."
    a "{sc=1}{color=#000000}Why do you look at me like that? S-say something..."
    m "..."
    a "{sc=1}{color=#000000}Is something...?"
    show alicescarredface
    play sound "audio/dynamic_audio/horror_EerieResonance3.mp3"
    a "{sc=1}{color=#000000}... wrong?"
    hide alicescarredface
    m "..."
    "You are frozen. You cannot speak. You can only stare, wide-eyed."
    a "%(player_name)s?"
    "Your mouth twitches open and closed uselessly."
    a "..."
    a "{cps=5}You still don't like me{/cps}."
    m "..."
    a "{sc=1}{color=#000000}Even now, you still-?"
    a "{sc=1}{color=#000000}It's still... {w}Still? {w}STILL?"
    a "{sc=3}{size=+40}{color=#000000}STILL NOT {i}ENOUGH!" with Shake((0, 0, 0, 0), 2.0, dist=20)
    stop music fadeout(2)
    window hide
    scene black with fade
    play sound "door.wav"
    window show
    "She runs away."
    scene bottle day:
        zoom 0.9
    with fade
    show mc vstressed with dissolve
    m "(She's unstable, but I have to find her. She's my responsibilty.)"
    show mc shout
    m "Wait! Alice!"
    hide mc with easeoutbottom
    scene hallway with fade        
    show mc confused with easeinbottom
    "You catch sight of her, just as she runs down the stairs."
    show mc shout
    m "Wait! Please!"
    window hide
    hide mc with easeoutbottom
    scene black with fade
    window show
    "But you're not fast enough."
    "By the time you reach the dorm's entrance, she's..."
    
    # truck scene
    a "Doesn't anyone think I'm pretty?"
    play sound "malescream1.mp3"
    a "Why are you screaming?"
    play sound "womanscream1.mp3"
    a "What about you? Do you-"
    play sound "malescream2.wav"
    a "Anyone! Please! No one!?"
    show truck1
    a "{sc=3}{size=+30}{color=#000000}DON'T SCREAM AT ME!\nI JUST WANT YOU TO LIKE ME!"
    a "{sc=3}{size=+30}{color=#000000}I DID SO MUCH!\nDON'T I DESERVE IT?"
    
    show truck2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5) with dissolve
    a "{sc=3}{size=+40}{color=#000000}PLEASE-!?"
    window hide 
    play sound "truckhorn.wav"
    scene black
    pause 3
    stop sound
    "Like scavengers, people quickly surround her body pieces."
    "And you watch from the boundary of the door as they mull over it with morbid fascination."
    "\"Why did she break into pieces instead of going splat? Where's the blood? Why did she look so disfigured\"?"
    "After the crowd disperses, you stare forlornly at her corpse on the desolate street, then leave it for the cars to flatten."
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

#  



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





a "I'm losing it! This is my final stand!"
m "Don't say that!"
a "If you won't let me be your girlfriend, I'm going to {i}kill myself{/i}."
m "..."
"Her declaration leaves you speechless."
"You never thought you'd be the one to hear those words. You're utterly unprepared."
"But Alice steps closer to the edge at your silence."
a "So what's it going to be, then? Am I dying? Or will you save me again?"

# game where you can either try to persuade her not to do it, (you have 3 chances) and Alice steps closer to the edge everytime, until she finally gives up and doesn't go through with it.
# Or 


# show choice
m "Alice. I want you to breathe."
m "You're a brilliant, intelligent woman. I know you're smarter than this."

a "..."


"But it looks like she isn't listening to a word you say. She's only waiting for what she wants to hear."
"Alice steps back."
#show image


# show choice

m "What would the point of this even be? Even if I DO date you, it wouldnt' be for love, it would be for... I don't even know!"
m "I don't even know why you'd want to BE with me! I'm... nothing! You're totally out of my league!"
m "You deserve better than me! Why go to all this trouble for a piece of crap like myself!?"

"Alice steps back."
"The more this goes on, the more desperately and quickly you talk. The more you heart pounds with anxiety and panic."
"What can you say!? What are you supposed to do here!? Surely not just... to accept her demands?"
"That wouldn't be right... right?"

# show choice
m "(If what I'm saying isn't working, I need to change my approach. I need to be more understanding!)"

m "I... understand. You have limited time."
m "It's probably really stressful, isn't it, Alice?"
a "...?"
m "Maybe, it's always in the back of your head..."
m "Maybe you can't relax, because all you're thinking about is the {i}time left{/i}."
m "I've felt that way too."
a "..."

"Alice steps back."

a "This is your final choice."
m "But... aren't you listening to me? Don't you agree that-"
a "It doesn't matter what I think, or what honeyed words you spout! All that matters is the result!"
a "We both have an agenda here."
a "So, either you say yes, or you say no."
a "Will you be my boyfriend?"

# show choice: Yes, no.

if no:
    m "No."
    a "..."
    m "..."
    a "Ha."
    m "..."
    a "..."
    a "Even after all of that."
    a "I must really... disgust you."
    "Alice steps away from the edge."

    "Was she planning to never go throught with it from the start? Has she just been playing you?"
    "How could she just threaten you like that?"
    m "(There'll be a time and a place to be angry, but it's not now.)"
    m "(She only did all of this because she's suffering.)"

    a "So, that's it, then."
    m "..."
    a "I failed. There's nothing more I can do."
    
# Lines:

# m "But everytime I try to do one of my big dreams, something that needs committment, I struggle to finish stuff."
# m "I just want someone to tell me what to do. I don't want to be responsible for my own life."
# m "I'm scared that when I start... I'm going to feel the same way."


# a "I didn't think you were this kind of person, %(player_name)s. I'm disappointed in you."
# m "Me? But you're the one who's wrong!"
# show alice neutral
# a "Is that what you think of me? If that's the image you see, then it must be true."
# a "I must be a horrible person. No, what am I saying? I'm less than a person."
# m "Don't twist my words! I never said that!"
# a "Oh? But it's what you {i}think{/i}, isn't it?"
# a "Fine. I'll be honest too."
# a "You've got so much more time with me, and seeing how you've wasted it... it makes me sick."
# a "Clearly you don't value your life, or care what you do with it. But I do."
# a "That's why I never let my opinions impact me."
# a "I did what I needed to. I behaved as I should. Heh, but it wasn't enough! Oh, woe is me, and all that... I just failed. That's all there is to it."
# "Her insults, her anger, her blame, her disgust in you..."
# "It doesn't matter, does it? It's all going to disappear, along with her, very, very soon."
# "All you feel, seeing her so dejected, is pity."
# m "I'm sorry."
# a "No. There's no need. I just... simply failed."
# a "Nothing I can do about that now. I may as well just stop living so I stop feeling so ashamed."
# m "Don't say that."
    
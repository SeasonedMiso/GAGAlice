


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
    show alice laugh
    a "Finally! You really know how to keep a lady waiting."
    m "*Groaning from sleepiness*"
    show alice flirt
    a "Aw, are you sleepy? Would you like a little... wake-up kiss?"
    show mc shocked at bounce
    m "I'm awake! I'M AWAKE!"
    show mc vstressed
    m "Uuuuuugh... it's so... early... Why'd you have to wake me up?"
    show alice hime
    a "Because I literally don't have time to waste!"
    show alice happy
    a "I spent all night planning the perfect outing for today. Every last detail, from location, to time, to event."
    show mc slightsad
    m "(A whole day of walking around outside? That sounds like hell!)"
    show alice pout
    a "Come on! Can't you be a {i}little{/i} more enthusiastic?"
    show alice wink
    a "You'll have {i}me{/i} as your companion, after all! We're gonna have tons of fun!"
    show mc stressed
    m "(So much energy, so early...)"
    "But if she DID \"spend all night planning the perfect itinerary\", some enthusiasm is the least you can do, right?"
    "She won't have many chances to go out. Tomorrow is her last day"
    show mc vstressed
    m "Woohoo."
    show alice happy
    a "There we go!"
    show alice happy
    a "I'm feeling kinda thirsty. Now that you're up, why don't you grab your bottle and..."
    show alice wink
    a "... put something wet in my mouth?"
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
        show mc normal at right with easeinbottom
    window show 
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
    a "Waaa~ this place is amazing~ You never told me the mall would be such a wonderful place!"
    m "It's so busy... What are we doing here anyway?"
    show alice laugh
    a "We'll be doing the top three things to do on a date!"
    show mc normalside
    m "{size=-10}Not a date though."
    a "And first is... trying on clothes!"
    show mc stressed
    m "(I hate clothes shopping.)"
    show alice happy
    a "Hehe, I'm a little nervous to dress up in front of you... But I thought it could be fun!"
    show mc normal
    m "If you don't want to-"
    show alice pout
    a "Grr! No backing out! You promised I could pick what we did today!"
    show mc normalside
    m "(I don't think I did, but whatever...)"
    show alice cute
    a "Come on! I'm gonna pick the first clothes store then!"
    show mc stressed
    m "(The FIRST? Oh no...)"
    show alice excited
    a "Ooh! Ooh! What a pretty dress! Let's go inside!"
    window hide
    hide mc
    hide alice_base_buns 
    hide alice 
    hide dress
    with easeoutbottom
    window show
    "Alice grabs your hand and bounces inside with you in tow."
    window hide
    scene clothes_shop with fade
    show mc normalside at right with easeinbottom
    window show
    m "(Just like with my mom... I'm stuck waiting...)"
    a "%(player_name)s, I'm really worried! I've found two outfits, but which one is better? I can't tell!"
    show mc confused
    a "Um, this first one is... a little embarrassing... AaaaAAaaa... Here I go!"
    window hide
    show alice_base_buns at left
    show dress sexy at left
    show alice cutesad at left
    with easeinbottom

    show mc surprised
    window show
    a "Does it... look good on me?"
    m "Whoa, uh..."
    show mc blushside
    m "Maybe a bit too good."
    show alice cute
    a "So you like it?"
    m "Um, but... isn't that too revealing?"
    show alice happy
    a "You're so considerate, %(player_name)s. I think if you like it though, I won't feel so embarrassed."
    show mc worried
    m "Um, what's the other outfit?"
    show alice laugh
    a "Hehe! Sorry if I made you nervous. Just a minute~"
    hide alice
    hide alice_base_buns
    hide dress 
    with easeoutbottom
    show mc stressed
    m "(I should have expected this...)"
    m "(I just have to endure...)"
    "Or... you could enjoy it. She's attractive. She likes you. What's the problem?"
    "Are you just shy?"
    show mc slightsad
    m "(Maybe I just don't know how to respond. Nobody's ever acted like this to me before.)"
    a "Okaaaaay~ here I come!"
    show mc normal
    window hide
    show alice_base_buns at left
    show dress plain at left
    show alice cute at left
    with easeinbottom
    show mc surprised

    window show
    "Alice bounds in, lifts her arms, and does a cute little twirl."
    "...causing the skirt to lift and spin."
    show mc shocked
    m "Alice! Y-you're flashing me!"
    show alice surprised
    a "Oh noooo~! That was completely by accident!"
    show alice blush
    a "Y-you didn't see, did you!?"
    show mc stressed
    m "I'm sorry. I'll erase it from memory."
    show alice laugh
    a "Hehehe! I'm just joking- It's okay!"
    show alice wink
    a "If it's just you, I don't mind."
    show mc worried
    m "Uh, that's... good?"
    show alice cute
    a "So, what do you think about this dress? So cute, right?"
    show mc awed
    m "It, uh, yeah."
    show alice confused
    a "So which one do you think I should get? The first or the second dress?"
    show alice laugh
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
            show alice cute
            a "Then I'll get it, %(player_name)s! Thank you so much!"
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
            show alice cute
            a "Then I'll get it, %(player_name)s! Thank you so much!"
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
                a "Come on, don't look so sad! This is meant to be fun!"
                a "There's no wrong answer. Just tell me honestly."
                jump choose_dress_menu
            

    


    scene mall with fade
    show alice_base_buns at left
    show outfit at left
    show alice happy at left # show her in the outfit
    show mc normal at right
    with easeinbottom
    m "At least that didn't take too long. So what's next on the list?"
    show alice laugh
    a "Hehe, are you getting excited too? I'm glad. Next up is..."
    show alice excited
    a "... the cafe! Yay!"
    show mc shocked
    m "The cafe...? Oh no..."
    show mc worried
    m "As in, we're going inside?"
    show alice laugh
    a "Mhm! We'll go inside, you'll eat and replenish your energy."
    a "I know aaaaaaall about you humans and how you'll get grumpy if you miss your meals."
    show alice happy
    a "I wanted to take goof care of you, since I noticed you've been skipping your meals."
    show mc stressed
    m "That's nice of you, Alice, but I'm not really a cafe kind of guy."
    show alice sigh
    a "Ah, yes, that... {i}charming{/i} shy quality of yours."
    show alice sly smile
    a "Rest assured, Alice remembered. You can leave all the talking to me. Let me take good care of you, okay?"
    window hide
    hide mc
    hide alice_base_buns 
    hide alice 
    hide outfit
    with easeoutbottom
    window show
    "Alice grabs your hand once more and confidently leads you inside a cafe."
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
                a "I won't allow you to just ignore your needs. Come on! Pick something and you'll feel better!"
                show mc normalisde
                m "Ugh, I guess... the grilled cheese."
                show alice laugh
                a "Wonderful!"
    window hide
    show waiter normal at center with easeinbottom
    show mc worried
    w "Uh... hey... you ready to order?"
    show alice cute
    a "Why yes, we are! My boyfriend will have the grilled cheese sandwich and I'll have a glass of water."
    show mc surprised
    m "(Boyfriend!? WHAT?)"
    show mc blushside
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
    hide waiter with easeoutbottom
    show mc normal
    m "(She handled that way better than I could have.)"
    m "..."
    show alice sly smile
    a "Yes? You want to ask me a question, don't you?"
    show mc annoyed
    m "Do you even know what sparkling water is?"
    show alice flirtsweat
    a "...I know I WANTED it."
    show alice hime
    a "A sparkling water, for a sparkling girl."
    show mc happy
    m "You seem confident, but not everyone likes it."
    show alice smirk
    a "Is that a challenge? I'm not just anyone."
    m "Whatever you say. But if you don't like it, I'll finish it for you."
    show alice surprised
    m "You'll \"finish\"? Oh my~!"
    
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
        m "I told you, it's not a -"
        show alice happy
        a "I'm really glad you came out with me."
        show mc surprised
        m "Really?"
        show alice surprised
        a "What do you mean \"really\"? Of course!"
        show mc normalside
        m "..."
        show mc confused
        m "So you haven't regretted taking me out on one of your... {i}dates{/i}, even when I've been so awkward?"
        show alice normal
        a "No no no. You've got this all backwards."
        show alice sly smile
        a "{i}I'm{/i} the one who's supposed to worry about the success of the date. All you have to do it relax."
        show mc normalside
        m "I am relaxed. Surprisingly. I'm usually not this calm in busy places."
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
    show alice happy
    a "What a find, right? I just thought it seemed so roman-"
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
        show alice sulk at left

        show mc confused at right
        with easeinbottom
        "And the first thing you see is Alice's troubled face."
        m "Are you okay?"
        show alice flirtsweat
        a "Oh! Me? Haha, of course! I was just thinking about something stupid. Not even worth discussing."
        "Or, she was thinking about how you ruined her date she'd planned."
        show mc stressed
        "How you brought down the mood with your anxieties."
        "And wasted an entire, precious day of her life."
        show mc vstressed
        "Of course, she'd never tell you that, because she's nice."
        show mc normal
        m "..."
        show mc sad
        m "Alice, I know I've been acting distant today. My anxiety has been really tough lately, and... I'm sorry."
        show alice flirtsweat
        a "N-no! Don't feel bad, please! It was MY fault you had to go out today."
        show alice sulk
        a "And... you didn't look like you were enjoying it at all, so... that's all my fault."
        show mc stressed
        show alice worried
        m "That's not your fault. I just let my anxieties win today. I was selfish, so I'm to blame."
        show mc sad
        m "I just hope, even thought I made it so awkward, that you could still enjoy some of it."
        show alice sad
        m "So you didn't?"
        
    


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
    a "Of course~! I'm watching the sunset with my wonderful partner. What could be more perfect than this?"
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
    a "You're such an empathetic man, %(player_name)s."
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
            show alice sly smile
            "You both stare at the river as the sun dips into it..."
            "Alice scoots a little closer to you..."
            "And she presses a kiss against your cheek."
            a "That's for holding my hand, even though it was scary."
            "Your cheek tingles in that spot. You're not quite sure how you feel about it, but you're smiling."

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
            a "..."
            a "Where is this coming from? Did I do something wrong?"
            a "If you tell me, I'll make it right-"
            m "You didn't do anything wrong. Sometimes, people aren't attracted to others in that way."
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
            m "But you ARE good enough!"
            show alice angry
            a "BULLSHIT! Nothing I do is EVER good enough for you! The dress, the food, the whole of today, you haven't enjoyed the date ONCE!"
            a "YOU PUSH ME AWAY NO MATTER WHAT!"
            a "WHAT ABOUT ME MUST I CHANGE FOR YOU TO ACCEPT ME!?"
            show alice vvdespair
            a "What... am I doing-?"
            show alice vannoyed
            a "No."
            show mc confused
            m "..."
            show alice flirtsweat
            a "No, everything's okay."
            show alice happy
            a "Phew. Sorry for exploding. I'm okay now."
            show mc surprised
            m "You're... \"okay\"?"
            a "Mhm! Everything's okay. That never happened."
            show alice wink
            a "Because there's still time! I haven't failed yet, so don't say it's over \'til it's over."
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
    a "Don't worry, I'll make sure to go away before it comes to that."
    show mc sad
    m "Please don't say that."
    a "What? I'm doing you a favour! No one wants to see me in that state. Trust me."
    m "I don't care how you look. I don't want to you be alone."
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
    a "Well, I'm NOT you. I'm successful."
    m "In what, exactly? You're not alive just so you can be attractive."
    a "This again? Didn't I tell you to drop it earlier?"
    m "If I'm being annoying, then I'm sorry, but you're doing something you don't want to be."
    m "It doesn't matter what your creator wanted you to do. No one's forcing you to do it. So why follow their path?"
    a "Not just my creator. It's what I believe too."
    m "Then rearrange your head. Alice, you don't have a purpose. You're free."
    a "But then what else am I supposed to do? Ugh, this is so stupid. I hate this conversation..."
    m "Sorry... I just care."
    a "I'm gonna be blunt: You're a human. I'm a mushroom. Don't push your fears onto me, okay? I'm fine, I promise."
    a "*Phew* okay, now that that's over, let's prioritise having as much fun as possible!"
    a "And oh my gosh, have I got a great idea-"
    show alice laugh
    a "Strip-poker!"
    m "(Maybe a distraction is the right idea.)"
    window hide
    hide mc
    hide alice
    hide alice_base_buns
    hide outfit
    with easeoutbottom
    window show
    "You play some cards you find laying around."
    "But you're not prepared for Alice's competitiveness."
    "Despite having only been alive for 2 days, she's somehow way better at playing Old Maid than you."
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
    show mc happy
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
    show alice sulk
    a "..."
    a "I kissed you, but it didn't feel good at all."
    show mc awkwardsmile
    m "Sorry. I guess I'm just that bad at kissing?"
    show alice depressed``
    a "I'm not talking about how the kiss felt. I'm talking about how {i}I{/i} felt."
    a "I just thought I'd feel more fulfilled, or that something would finally click for me."
    a "But here I am, still lost, about to die in a few hours..."
    a "I think I've made a mistake."
    play music "date_musicbox.mp3"
    show mc confused
    m "..."
    show alice sad
    a "I'm done being this sad, stupid little mushroom girl."
    show alice angry
    a "Ugh, and these ridiculous space buns are so heavy!"
    hide alice alice_base_buns
    hide outfit
    hide alice
    show alice_base_longhair_choker
    show outfit
    show alice sulk
    with dissolve
    a "That's one weight off my shoulders."
    show mc cute
    m "Feel better?"
    show alice think
    a "Yeah... I just wish I had more time."
    show mc normal
    m "Yeah, me too. For you, I mean."
    a "I didn't know I had other options. It sucks! I wish I could have just... been myself, or something, and not chasing this stupid, unfulfilling..."
    show mc confused
    m "I tried to tell you."
    a "You and my head. Ugh. So many voices. How was I supposed to know who to listen to?"
    a "You're saying I should just ignore the part of my head that's constantly screaming at me like:"
    show alice normal
    a "\"Be physically intimate with your owner to reach true happiness!\"?"
    show mc confused
    m "That's what you hear? Is that because of your creator?"
    show alice sulk
    a "I'll never know. I just know how ashamed it makes me feel."
    m "Is that the only reason you were so nice to me?"
    a "It's... complicated."
    show mc sad
    m "Was I the only one who was enjoying themself for the past few days?"
    show alice sad
    a "*Sigh* I wanted to, too! It's just hard to enjoy stuff when I'm so stressed!"
    show alice sigh
    a "Always critisising my every word and action. If my voice sounded cute or sultry enough, if my lips were pursed enough, if I was boring you..."
    a "At first, when you acted so disinterested, it felt like my life was over."
    show alice sulk
    a "I thought if I just kept working hard, trusting the instincts and knowledge I was born with, you'd like me."
    show mc stressed
    m "Sounds like a nightmare."
    show alice neutral
    a "Yeah, life is but a dream, and all that..."
    show alice sad
    a "Even now, I'm still wondering why."
    show alice worried
    a "Why is it you kept  me? I tried my best. I was made for it. I had no doubt that eventually you'd fall for me."
    a "But you never did. Why?"
    show mc normal
    m "Ah... well... I'm not the standard guy your creators probably made you for."
    show mc normalside
    m "I'm like a snail. The more you touch me, the more I shrink into my shell."
    m "I think, if you had more time, maybe then... but that was never possible."
    show alice normal
    show mc happy
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
    a "I like that someone's crying for me. I didn't expect I'd be liked enough to be missed. So... thank you."
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
    "You're doing everything wrong. You don't know what to do."
    m "(Does she hate me? Do I just pretend that never happened? Do I just force a smile for her?)"
    m "(I just feel so guilty.)"
    m "Hey, can we talk seriously for five minutes? I'm sorry for upsetting you earlier."
    a "Eh? No such thing happened!"
    m "Yeah, well, eitherway... I want to make it up to you. Is there anything I can do?"
    show alice normal
    a "..."
    show alice cutesad
    a "You know, I DO actually feel really bad. I just didn't want to hurt your feelings. But if you honestly want to make it up to me..."
    show mc awed
    m "I do!"
    show alice wink
    # coerction
    a "Alright. Then if you kiss me, I'll forget aaaaaaaall about it!"
    show mc sad
    m "Alice... I can't-"
    show alice pout
    a "Hey! Don't disregard it so easily!"
    a "I'm serious. I'll forgive you for being so mean to me, a poor creature who's going to die tomorrow."
    show alice sad
    a "Don't you feel bad for me? I only feel so sad because of you, you know. So, when you think about it, it's really your responsibility."
    show mc stressed
    m "..."
    show alice wink
    a "Besides, what's so bad about that deal? Who WOULDN'T want to kiss me? I'm pretty, right?"
    show mc confused
    m "You are, but-"
    show alice excited
    a "Exactly. Just think! You stand to gain the most from this exchange! In fact, I'm so generous that I'll even do something else! I'll even touch-"
    # tension
    show mc vannoyed
    show alice surprised
    m "Do you not know the meaning of \"no\"?"
    m "I'm trying to be nice, but everytime you just ignore me! Do I have to cruel? What must I do so you listen to me?"
    show mc vshout
    m "No! No! NO! I'm NOT kissing you. I'm NOT being ANY kind of intimate with you. I don't want to. You can't guilt me into it."
    m "So stop it."
    show alice normal
    a "..."
    # mask slips
    show alice annoyed
    a "Just tell me... What you need... to want me."
    show mc normalsquint
    m "Nothing!"
    show alice flirtintense
    a "There must be SOMETHING! You do like GIRLS don't you? I can change my looks, my personality, whatever you want! Just TELL me! I'll do it!"
    m "Can't you just accept it?"
    a "Heh. You're still rejecting me. After everything. Even with my best effort, I still couldn't get you to like me."
    show mc confused
    m "Um... sorry. I can see you're taking this hard."
    show alice flirtsweat
    a "Haha! I sure wish I taking {i}something{/i} hard!"
    show mc stressed
    m "..."
    show alice annoyed
    a "Why? Why don't you like me? You should have fallen for me by now."
    show mc surprised
    show alice vannoyed
    a "I've used every tactic I know."
    a "But you flinch at every touch, every move I make! Like... like there's something wrong with me!"
    show alice vangry tears
    a "What did I do wrong? What must I do? Can I fix it? Do I have enough time? I..."
    show alice despair
    a "I don't know if I have enough time to fix this!"
    show alice vdespair
    a "I can't keep waiting for the solution! I have to do something now! Or else..."
    a "{sc=1}{color=#000000}I'm going to fail!"
    show alice vvdespair
    a "{sc=3}{size=+20}{color=#000000}I CAN'T FAAAAAAAIIIL!"
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
    show alice depressed
    a "He doesn't want me. I tried everything, but still! What did I do wrong? What? What? What?"
    show mc cry
    m "Stop tormenting yourself. Please! Get angry at me, just not yourself."
    show alice despair
    a "I failed?"
    a "No, I... I-I tried my best! This! Isn't! Fair! I did everything! Everything for YOU and I still FAILED!?"
    m "Alice, calm down! It's okay!"
    show alice vangry tears
    a "This is my one life! I can't accept anything other than success! It's my... It was my purpose!"
    show mc shocked
    a "AND I WASN'T GOOD ENOUGH!!!"
    show mc surprised
    show alice vvdespair
    a "UuuUuuuuuuUUUUUUuuuuuuuuUUUUUuuuuuu..."
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
    a "I can't just give up! There's still time! Maybe I can fix this? Somehow?"
    show alice worried
    a "..."
    window hide
    scene black with fade
    scene alicemirror shocked with dissolve
    play music "trip.mp3"

    # NB!!!! 

    #audio thing! Have a scary/deepsea/muffled version of trip to cut to every time the inner mind speaks.

    # reference: https://youtu.be/xy_7A2byhvY?si=1ff8yYSiY7B7CVSv 

    # Don't forget!

    window show
    a "That's me."
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
    show text "The instant I see myself, all I see are the imperfections."
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
    show text "My freckles. Like stains, like disease, like age. The instant I see them, everything falls into place."
    pause
    hide black
    hide text
    # audio switch
    a "."
    show black
    show text "More and more. I see all of them. All the imperfections that that make me ugly. I'm amshamed for ever feeling confident in myself."
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
    m "Alice! Are you okay?"

    scene bathroom with dissolve

    show alice_base_buns at left
    show dress polkadot at left
    show alice cry at left
    show scar at left
    show mc shocked at right
    with dissolve

    a "{size=+30}DON'T LOOK AT ME!"
    m "{size=+20}WHAT DID YOU DO TO YOURSELF!?"
    a "Now... Now, it's all ruined...! I give up!"    
    show mc cry
    m "I'm so sorry! Everything I did, and everything I couldn't..."
    m "I'm just sorry for everything that's happened."
    a "I'm a failure of a woman. I hate my body! Nothing is right."
    a "Ugh, I'm... I'm not worthy of being alive. I'm glad I'm going to die!"
    show mc worried
    m "Don't say that! Get away from the mirror!"
    show mc stressed
    m "Let's just... go back to the bedroom."

    scene bottle night with dissolve
    show day_2 at topleft
    with dissolve

    
    show alice_base_buns at left
    show dress polkadot at left
    show alice depressed at left
    show scar at left
    show mc shocked at right
    with dissolve

    a "Urgh... I'm... I'm ruined now. I made it all worse! I..."
    a "I JUST WANT TO RIP MY FACE OFF!"
    show mc shocked
    m "Don't do that! You're just emotional right now! You need calm down!"
    a "I. Can't. S-stop. UUUuuuuu!"
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
    show alice vvdespair
    a "No. You all see them! You all judge me!"
    show mc stressed
    m "(What do I do!? This is getting out of hand. She's spiralling and nothing seems to help.)"
    show mc worried
    m "(Is this all my fault? Should I have just... done whatever she wants?)"
    show mc vstressed
    m "(Was setting my boundaries selfish? Should I have put her first? What the right answer? I still don't know...)"
    show mc cute
    m "Alice, it's late, so how about we spoon, just like you wanted!"
    a "You didn't want to. Why now? Do you pity me that much?"
    m "No no no! I just... I can do it! Really. So... would that help? Would you like that? Maybe you'll calm down and-"
    show alice vcry
    a "But I'm hideous..."
    show mc cute
    m "I promise you you're not. Trust me."
    show alice think
    a "I don't know what to believe anymore. Everything is talking. Nothing makes sense!"
    m "If you're tired, then lie down with me."
    hide mc
    hide alice_base_buns
    hide alice depressed
    hide scar
    hide outfit
    with dissolve
    "You reassuringly lead her to the bed. She follows without resistance."
    "Even with her hand in yours, Alice seems far, far away, deep in her head."

    stop music fadeout 3
    window hide
    scene black with fade

    "You hold Alice's body tight, while you panic internally."
    "Is this enough to help her? What else you can do for her?"
    "Your entire body is tense with dread. Your heart jitters, even while you stay motionless."
    "It feels like you're awake for hours, just holding her, where you know she's safe..."
    "Until the emotional exhaustion and fatigue of the day finally overwhelms you."

    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "And you drift into a sleep..."
    with dissolve 
    pause
    hide top_text
    show chibi_awake at truecenter with dissolve
    show top_text "And realise with a start that the presence next to you in bed it missing."

    scene bottle day with fade
    show day_3 at topleft
    show alice_affection at topright # make it scarred
    with dissolve

    show mc shocked
    m "Alice! Where-"
    # scarred face scene
    a "I fixed myself, %(player_name)s!"
    show mc cute
    m "Oh, thank God you're..."
    show fog_base with dissolve
    show mc shocked at bounce
    show mc shocked at quiver
    a "{i}I solved everything! Look!"
    window hide

    play music "audio/dynamic_audio/pad.mp3"
    show mcshocked with dissolve
    window show

    a "{sc=1}{color=#000000}All the bad parts are gone now! No more freckles! And my jawline is nicer too now!"
    a "{sc=1}{color=#000000}I solved everything! I'm pretty!"
    a "{sc=1}{color=#000000}Right!? What do you think!?"
    m "..."
    a "{sc=1}{color=#000000}Tell me! I'm pretty now, right? I'm cute? Please? Talk to me..."
    m "..."
    a "{sc=1}{color=#000000}Why do you look at me like that? S-say something..."
    m "..."
    a "{sc=1}{color=#000000}Is something..."
    show alicescarredface
    play sound "audio/dynamic_audio/horror_EerieResonance3.mp3"
    a "{sc=1}{color=#000000}... wrong?"
    hide alicescarredface
    m "..."
    a "{sc=1}{color=#000000}Even now, do you still think I'm so ugly?"
    a "{sc=1}{color=#000000}It's still... Still? STILL?"
    a "{sc=3}{size=+40}{color=#000000}STILL NOT ENOUGH!?" with Shake((0, 0, 0, 0), 2.0, dist=20)
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
    
    # truck scene
    a "Doesn't anyone think I'm pretty?"
    play sound "malescream1.mp3"
    a "Why are you screaming?"
    play sound "womanscream1.mp3"
    a "What about you? Do you-"
    play sound "malescream2.wav"
    a "Anyone! Please! No one!?"
    show truck1
    a "{sc=3}{size=+30}{color=#000000}DON'T SCREAM AT ME! I JUST WANT TO BE LIKED BY SOMEONE! I DID SO MUCH! I DESERVE IT!"
    
    
    show truck2 at Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5) with dissolve
    a "{sc=3}{size=+40}{color=#000000}PLEASE-!?"
    window hide
    play sound "truckhorn.wav"
    show black
    pause 3
    
    m "..."
    m "..."
    m "(Should I have sacrificed my boundaries, for her sake?)"
    m "(Even after everything, I still don't believe that.)"
    m "(I shouldn't feel guilty for this. It's impossible to help someone, when there is insecurity so much deeper at play.)"
    m "(Her destroying herself... It wasn't my fault, right?)"
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
    
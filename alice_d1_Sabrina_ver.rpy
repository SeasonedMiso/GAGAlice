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
    "Four weeks later... after a dorm mate drops off the box."

    scene day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show bottle
    show kit_bursting
    with Dissolve(2)

    play music "phonealarm.ogg"
    m "Nooo... I don't want it to be morning already..."
    stop music
    "Are you ready to start the day? To get out there, learn and work?"
    m "(Fuck college. I'm too tired to pay attention to anything.)"
    "Ah, yes. How long has this cycle been going? Are you ever going to just turn off your morning alarm?"
    "Just admit it: You going to keep missing lectures and ignoring the responsibilities that are piling up."
    m "(Of course... The instant I wake up, the thoughts won't stop.)"
    
    show mc normal with easeinbottom
    m "May as well get the mushroom-spray of the day over with."
    show mc confused
    m "..."
    show mc surprised
    m "W... was this box always so engorged!?"

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

    
    scene day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show bottle
    with Dissolve(2)

    show day_1 at topleft
    with dissolve
    play music "normal.mp3" fadein(2)

    show mc shocked at right
    show alice normal at left
    with easeinbottom

    m "..."
    show mc shocked at bounce
    m "{sc=3}{size=+40}{color=#000000}WHAT THE-!?!"
    show alice hime
    na "Hold that thought!"

    show mc surprised
    $ watered = 0
    show water_status at topright with dissolve
    
    play sound "spray.wav"
    $ watered = 1
    pause 1
    queue sound "spray.wav" 
    $ watered = 2
    hide water_status with dissolve
    na "E-hem- ehem - Ah, much better."

    show mc shout at bounce
    m "{sc=3}{size=+40}{color=#000000}WHAT THE FUCK?!?!"
    show alice laugh
    na "Sorry about the box and all~ but I sure know how to make an exciting entrance, don't I?"
    m "{size=+20}WHO EVEN ARE YOU!?" with sshake
    show alice pout
    na "Hush."
    show mc surprised
    m "But-"
    na "Shhhh... I'm gonna do my introduction, okay?"
    show mc confused
    m "..."
    show alice happy
    a "So, hi there! My name is Alice."
    a "But you may call me mommy or madam, or whatever you like."
    show mc surprised
    show alice flirt
    a "This little mushroom has been wanting to meet you for so long."
    m "..."
    show mc surprised
    m "You're a what? Sorry?"
    a "I know, I look human or whatever, but trust me, there's not a bone in body."
    a "Unless you want to put one there *wink*."
    show alice happy
    a "So I can do stuff like this:"
    window hide
    show alice backwards
    pause 0.5
    show mc shocked
    pause 1
    show alice happy
    pause 1
    window show
    m "Oh my God! You're {i}actually{/i} a mushroom...!"
    show alice pout
    a "No~"
    show alice flirt
    a "I'm YOUR mushroom. You've been growing me all this time."
    a "Which means, I could call you daddy, if you like."
    show mc shocked
    m "..."
    show alice happy
    a "Buuuuut, you could always tell me your {i}actual{/i} name."
    show mc stressed
    m "I... but! I-I think we need to discuss this!"
    show alice pout
    a "Name first! I wanna know what you call you."
    show mc worried
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
        
        

    show alice happy
    a "%(player_name)s, huh? What a cute name."
    show mc stressed
    m "But how is this happening!? You were supposed to be a normal mushroom. I was going to eat you-!"
    a "You still can~ From my hair, to my toes, I'm completely edible."
    show mc worried
    m "How does that even work!?"
    show alice laugh
    a "You look so distraught. Just relax. Everything is exactly as it's meant to be~"
    m "Just hold on! I-I need to check what it is I bought!"
    window hide
    hide mc
    hide alice
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
        m "It looks normal. Maybe the \"About\" page will have more info?"
    
        show alice surprised at left with easeinbottom
        a "So this is where I was born?"
        show mc surprised at right with move
        m "Gah! What are you doing?"
        show alice pout
        a "What? You're gonna learn stuff about me and I'm not allowed to watch? I'm just curious!"
        show mc stressed
        m "I guess... that's fine."
        window hide
        hide mc
        hide alice
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
        m "{sc=3}{color=#000000}WHAT THE HELL???? WHAT KINDA MESSED UP WEBSITE IS THIS?"
        window hide
        show alice excited at left with easeinbottom
        window show
        a "What's it say?"
        show mc worried
        m "I... I don't know if I should say..."
        show mc confused
        m "Wait, you can't read?"
        show alice pout
        a "No, so I depend on you. Please tell me! It's me we're talking about!"
        show mc stressed
        m "Ugh, okay... It says you're something called a..."
        show mc confused
        m "Fly... A-ma-ni-ta."
        show alice normalside
        a "Oh yeah, I knew that already."
        show mc surprised
        m "You did? How?"
        show alice hime
        a "Can't explain it. I just do."
        show mc confused
        m "Okay, um, moving on... it basically just says stuff like..."
        show mc blushside
        m "...they're selling mushroom girls to losers to eat and... be intimate with."
        show mc vstressed at bounce
        m "{size=+20}NOT THAT I WANT TO DO ANY OF THAT, OKAY!? IT'S JUST WHAT THE SITE SAYS!" with sshake
        show alice laugh
        a "Hehe, sure, sure~"
        show mc vblushside
        m "I-I'm serious! I'm not like that..."
        show alice happy
        a "Anything else?"
        show mc normal
        m "..."
        show mc sad
        
        m "(Yeah, but I don't want to be the one to say it.)"
        "But you have to. She needs to know."
        show mc normalside
        m "It says your \"lifespan\" is three days. I'm sorry."
        show alice confused
        a "Three days? Is that bad?"
        show mc stressed
        m "(VERY BAD! But I have a feeling that I should approach this carefully."
        show mc normal
        m "It's... um... not great? But you can do a lot in that time too."
        show alice normal
        a "Oh well. Good to know."
        show mc surprised
        m "(You're fine?)"
        show alice happy
        a "What's with the surprise? I'm not gonna cry or anything. All things have an end, %(player_name)s."
        a "At least I'll have you at my side."
        show mc normalside
        m "(She really just took that in stride, huh? I should learn a thing or two from her.)"

    window hide
    hide mc
    hide alice
    with easeoutbottom
    scene bottle day with dissolve:
        zoom 0.9
    show day_1 at topleft
    with dissolve
    show mc confused at right
    show alice happy at left
    with easeinbottom
    
    m "So... you're a talking mushroom girl."
    m "Mhm. Hope you're not disappointed~"
    show mc surprised
    m "No... but..."
    show mc worried
    m "I'm just bewildered. This is a crazy situation! Maybe I'm dreaming..."
    show mc normalside
    m "No, maybe it's more surprising that I'm talking normally with someone for once."
    show alice laugh
    a "Hehe! You're so cute, %(player_name)s."
    show mc blushside
    m "What, no I'm not..."
    show alice happy
    a "You know..."
    show mc confused
    show alice flirt
    a "After hearing your voice for so long, I've been so curious to see what you looked like..."
    a "And I'm not disappointed."
    show mc stressed
    "I doubt that. Look at yourself."
    "Your hair is a mess. Your clothes are dirty and unflattering. Your skin is dry as fuck..."
    show mc normalside
    m "(I can't tell if she's complimenting me or making fun of me.)"
    show alice at center with move
    a "I have something to tell you."
    show mc surprised
    show alice_affection at topright
    with dissolve

    menu:
        "Stay back!":
            $ alice_reject += 1
            
            m "W-what are you doing?"
            
            a "I'm just coming closer is all."
            show mc worried
            m "Can you... not?"
            a "Hehe, are you playing hard-to-get?"
            show mc stressed
            m "I'm not playing hard to get. I'm simply enforcing my boundaries."
            show alice pout
            a "*Whining noises*"
            a "Don't be unfriendly, Master %(player_name)s."
            a "I just wanna hold your hand and say thank you for looking after me..."
            show mc normal
            m "You can just say it from two steps back."
            show alice pout at left with move
            $ alice_rp -= 10
        
            a "Okay..."
            hide alice_affection with dissolve
            show alice happy
            a "Master %(player_name)s, I really appreciate-"
            show mc shout
            m "And please don't start with that \"Master %(player_name)s\" crap."
            a "Okay, {i}%(player_name)s{/i}. Now, as I was saying..."

        "What is it?":

            show mc confused
            m "What?"

    show alice sad
    a "You're the only person who's ever cared about me. All while I was suffering in that darkness." #In the true route, mc bring up her traumatic childhood, Alice laughs and says she was exaggerating for sympathy. tbh she was pretty chill in there.
    show mc surprised
    m "Was it that bad?"
    show alice cutesad
    a "Yes! It was so lonely!"    
    a " All I've been thinking in that horrible, dark space... was getting to see you."
    show alice wink
    a "...and imagining all sorts of things we could do together."
    show mc confused
    m "Something in your eye?"
    show alice sigh
    a "..."
    show alice smug
    a "Yeah, I should be more direct."
    show alice vflirt
    stop music fadeout 2
    a "I'd like to show you how much I appreciate everything you've done."
    m "What do you mean?"
    a "Have a seat, %(player_name)s~"
    
    window hide
    hide mc
    hide alice
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
    a "Sorry~ I just wanted you to get more comfortable."
    "WAIT A SECOND! What's with that obviously suggestive line!? And why is she looking at you like... THAT?"
    m "(I-I must be misinterpreting-)"
    a "%(player_name)s... I've been so lonely~ I haven't been able to say a thing for weeks..."
    a "You understand, don't you? How horrible that can feel?"
    m "I... kinda do..."
    a "Then, maybe we can help each other out."
    "OOOOOH! SHE'S APPROACHING! I DON'T THINK YOU'RE MISINTERPRETING ANYTHING!" with sshake
    "Are ya ready, champ?"
    m "(Of course not! I've never been so unprepared in my life! I haven't even brushed my teeth yet!)" with sshake
    m "(And I hardly know her! And she's a mushroom! And- And-!)"
    m "(What should I do!?)"
    a "Hehe, your head is practically steaming."
    a "What's with your frown? There's nothing to worry about."
    a "It's just me and you here."
    
    show alice_bed_2 with dissolve 

    "It feels like your brain is melting the closer she gets!"
    m "(It's really hard to think right now...)"
    m "(Your heart thumping loudly in your chest, as Alice inches closer yet.)"

    a "That's right. Just relax."

    "Alice gives your cheek a gentle caress with her fingertips, sending an ice-cold bolt of pure sensation up your spine."

    a "But there's just one thing I need you to do."

    show alice_bed_3 with dissolve 
    pause 1
    a "Bite me."
    m "(Eh!?)"
    a "I'm serious."
    m "But why!?"
    a "Would it be weird if I say I'd like it?"
    a "And I think it would help you relax too."
    m "(But... aren't you... poisonous?)"
    a "Only in large quantities, and this is just a little thing."
    show alice_affection at topright with dissolve
    m "(It's really heart to think... but I need to choose now what I'm doing.)"
    menu:
        "Bite (N/A).":
            play sound "bite.mp3"
            show alice_bed_4 with dissolve
            a "Good boy. Now swallow."
            scene black with fade
            "You obey."
            "Alice presses her mouth against yours."
            "Your head feels dizzy, but in a good way."
            "You can't keep track of time, because your heart is beating so fast."
            m "(I can't believe she's kissing me. Am I dreaming? Why would she ever like someone like me?)"
            "You're right. It doesn't make sense."

        "AAAHHHH!":
            $ alice_reject += 1
            $ alice_rp -= 10
            window hide
            stop music
            play sound "punch.wav"
            show alice_bed_reject
            window show
            a "Gah!!"
            hide alice_affection with dissolve
            window hide



    scene day_clouds
    show bedroom_opencurtains
    show dirty1
    show dirty2
    show bottle
    with Dissolve(2)
    play sound "door.wav"
    
    with fade
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
    show alice annoyed at left
    with easeinbottom
    window show

    m "Are you okay? I just panicked and-"
    show alice annoyed
    a "What the hell! Do you have a problem with me or something?"
    show mc surprised
    m "W-what? No, I just… don't wanna do..."
    show mc blushside
    m "That."
    show alice mendokusai
    a "What are you, a child? It's called sex."
    show alice surprised
    a "Ah! I mean..."
    show alice sigh
    a "Hah, sorry, that was my bad apple side. Clearly I approached you incorrectly..."
    show alice happy
    a "What I mean to say is, I think this would all work out better if you told me exactly what you want."
    a "So tell me: should I be more cutesy? Less aggressive? Gentle?"
    a "Do you like them silent? I'll be anything you want. I can do it."
    show mc confused
    m "Uh... what? Can't you just… be yourself? What's the problem?"
    show alice normal
    a "The problem is: You don't like me. I'm trying my best to fix that."
    show mc surprised
    m "It's not like I dislike you."
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
    a "Just tell me what you want."
    show mc stressed
    m "…"
    "Stop harrassing me!"#true route! Alice snaps and runs off, loses her self-esteem (potential for bad ending where she slashes herself if handled poorly)...
    show mc shout
    m "Stop trying to force yourself on me! I don't want that. I don't want you."
    m "Just leave me alone and stop harrassing me!"
    show mc normalsquint
    m "Is that too much to ask?"
    show alice surprised
    a "..."
    show alice sad
    a "..."
    show alice cry
    a "Ugh!"
    show alice angry tears
    a "Fine! I tried!"
    show mc surprised
    m "Alice-"
    a "But if you don't like me, maybe someone else will."
    window hide
    hide alice with easeoutbottom

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
        "Who won't stop wanting to talk to you."
        show mc normalside
        m "(He's not that bad... He understands what I'm going through.)"
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


    scene bottle_phone day with fade:
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
            "You're so stupid. Don't assume people want you in their vicinity."
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
            show mc stressed
            m "(Wait - no it's not! I have no idea where Alice is!)"
            m "(She wouldn't go outside...)"
            show mc stressed
            m "(...would she?)"
            show mc sad
            m "(God... this is way more stress than I signed up for.)"
            show mc normalside
            m "What if she doesn't know you supposed to wait before you cross the road?"
            m "I wonder if she'd just explode into mushroom pieces if she got hit by a car..."
            show mc surprised
            m "(Ah! I'm getting distracted! Focus!)"
            m "..."
            m "She got upset in the heat of the moment"
            m "But as soon as she realizes she has no shelter, she's gonna come running back, right?"
            m "Maybe I should just go and wait for her in my room?"

            na "KYAAAAAAAAAA!" with sshake
            show mc surprised at bounce
            m "Alice!"
            window hide
            hide mc with easeoutbottom
            scene bathroom with fade
            show showerguy scream at right 
            show showerguy scream at quiver
            show alice pout at left
            with dissolve
            window show
            keshad "{sc=3}{color=#000000}AAAAA!"
            ali "Why are you backing away?"
            show alice smug:
                xpos 0.1
            with move
            ali "Don't you want to get closer to me?"
            
            keshad "{sc=3}{size=+20}{color=#000000}AAAAHHGH!!!"

            play sound "door.wav"
            show mc stressed at right
            with easeinbottom
            show mc shocked at bounce
            m "Huh!?"
            show mc vstressed at center with move
            show alice shocked
            m "Come with me!"
            ali "Hey!"
            window hide
            show mc at right
            show alice at right
            with move
            
            hide mc
            hide alice
            with easeoutbottom
            play sound "door.wav"
            window show
            m "{size=-20}Sorry!"

            show showerguy sad

            keshad "{sc=2}{color=#000000}*Whimpers*"
            window hide


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
    show alice annoyed at left
    with easeinbottom

    # I feel like the tone is kinda off
    window show
    ali "Where are you dragging me you pervert?"
    ali "What kind of sick,"
    show alice flirt
    ali "tormented,"
    show alice annoyed
    ali "degenegerate things are you going to-"
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
    ali "The only reason I went looking for someone else is because you humiliated me."
    show mc shout
    m "Hold on a sec... how did {i}I{/i} humiliate {i}you{/i}?" 
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
    show mc normalside
    m "So... That's why you went to find someone else."
    ali "I guess..."
    ali "But all he did is {i}scream{/i}."
    ali "..."
    show alice sad
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
        "Step on me mommy (N/A)":
            return
        "I think you're valuable": #you can change the phrasing
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
    show alice annoyed
    ali "So for you to turn me down how you did..."
    show alice disgusted
    ali "Really sucked."
    show mc worried
    m "..."
    show alice disappointed
    ali "And I guess that wasn't your intention and that's not why you grew me, but it's like..."
    show alice serious
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
    a "What do you even do in here all day? This pathetic excuse for a room is so minute it's making me depressed."
    show mc normalside
    m "Ouch. But also I agree."
    
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
    

    show mc worried at right
    show alice sad at left
    with easeinbottom
    m "I'm sorry for shoving you. That was just too much for me and I..."
    show alice pout
    a "..."
    show mc stressed
    m "Sorry. I just needed some space and panicked. Hope you're not hurt."
    show alice sigh
    a "Heh, it's okay."
    show alice happy
    a "Honestly, sometimes I don't know how to hold back."
    a "And it's adorable how green you are."
    show mc confused
    m "So we're okay, right?"
    play music "normal.mp3"
    show alice flirt
    a "Mhm~ As long as you forgive me for being too excited."


    scene bottle_phone noon with fade:
        zoom 0.9
    show mc normalside at right
    show alice normal at left
    play music "normal.mp3"
    with easeinbottom
    show mc normal
    m "I can't believe it's already afternoon. We've been talking for a while..."
    show alice vflirt
    a "Oh my. We're all alone in your bedroom and it's nearly night... Whatever shall we do?"
    m "(Yeah, I can understand why she'd feel bored. There's nothing to do here.)"
    show mc normalside
    m "Hmm... I guess we could go somewhere to pass the time."
    show alice mendokusai
    a "That's not..."
    show alice surprised
    a "Oh! I see!"
    show alice flirt
    a "Who am I to deny you something like that? Of course we can go. It will be cute."
    show mc surprised
    m "(That was surprisingly easy.)"
    m "A-alright then..."


    window hide
    hide mc
    hide alice
    with easeoutbottom
    stop music fadeout 2
    scene black with Fade(0.5, 1.0, 0.5)        
    play sound "door.wav"
    play music "mall.mp3"
    show chibi_mc at slightright
    show chibi_alice at slightleft
    with easeinright
    window show
    
    "Thankfully, it's not too crowded at night, so you can relax and enjoy the night air."
    "Alice, however, only seems to enjoy hooking her arm through yours and walking side-by-side."
    "She seems so happy to be out, that you don't want to ruin her good mood by pushing her away."
    "You lead Alice to your secret hangout spot."
    window hide
    hide chibi_mc
    hide chibi_alice
    with easeoutleft

    scene arcade with fade
    show alice normal at left
    show mc surprised at right
    with easeinbottom
    m "Huh. Not bad. This place has good variety."
    m "(They even have that old train game I played when I was ten!)"
    show mc slightsad
    m "(I've been wanting to come here for so long... Why did I stop myself?)"
    show mc sad
    m "(I wasted so much time...)"
    show alice pout
    a "Hey, %(player_name)s, you look distracted."
    show alice flirt
    a "Perhaps you're thinking about... me?"
    show mc normal
    m "Sorry, just lost in thought for a minute. This is the aracde. You play games-"
    show alice hime
    a "Aha! Games! I know {i}all{/i} about games. Strip poker, for instance-"
    show mc stressed
    m "{i}Aracde{/i} games. Clothes stay on. Please."
    show mc normal
    m "Hmm, I can see Bubble Bobble. You might like that one."
    show mc happy
    m "It was the first arcade game I ever played."
    show alice flirt
    a "So, you want me to play this little game? Fine. I'll show you just how good I am with my hands~"
    show mc stressed
    m "(Why does it always have to be an innuendo?)"
    show black with dissolve
    "You watch Alice load up the game and fly through the first few levels, laughing haughtily all the while."
    "She seems to be enjoying herself, but..."
    show alice angry
    show mc normal
    hide black with dissolve
    play sound "gameover.wav"
    a "What the..."
    show mc annoyed
    m "Welp, you lost."
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
    a "I'll win this game and show you! HOW! GOOD! I! AM! Hehe~"
    show mc shocked
    m "(She's intense!)"

    scene black with fade

    "Alice proceeds to play nothing but that one arcade game for the next hour."
    "Children wanting to play it... soon learn that waiting in line is futile."
    "It's fun to watch her try so hard. You hope she's enjoying herself."
    "Going out like this wasn't as bad as you'd thought it would be, especially when you're not alone."
    "You want to do it again."
    stop music fadeout 2

    #go home, assault scene, she snaps or not.

    #home:

    
    scene bottle_phone night with Fade(1, 2.0, 1):
        zoom 0.9 
    play sound "door.wav"
    play music "night.mp3 "
    show alice happy at left
    show mc normal at right
    with easeinbottom

    m "That was kinda fun."
    a "Mhm~ That was a lovely date, %(player_name)s."
    show mc shocked
    m "Wait! Wait! Wait! A {i}date{/i}!? Um...!"
    "What are you doing!? This is the perfect chance!"
    "Alice is hot. You've won the lottery by landing her - come on!"
    "Just nod along and things will go your way!"
    show mc worried
    m "(But... do I even want that?)"
    "Of course you do! You're a man, aren't you? Even if you don't want it, you SHOULD."
    show mc stressed
    m "(No! I have to set things right so she doesn't get the wrong idea!)"
    "You're just shooting yourself in the foot."
    m "(No, I'm dodging a bullet.)"
    show mc awkwardsmile
    m "Uh, Alice...? Sorry. I was just taking you out for fun."
    "To have fun... as friends, you know?"
    show alice pout
    a "..."
    show alice sulk
    a "After all the effort I went to?"
    show mc worried
    m "Sorry..."
    show alice hime
    a "Hmph!"
    show alice flirt
    a "Well well well... If you like the friends-to-lovers tag, I can work with that too."
    show mc surprised
    m "What?"
    show alice smug
    a "Hehe, are you finally realising it, %(player_name)s? I'm not just like any other girl."
    a "You can't discourage me that easily. I'm like a tiger whose caught scent of my prey."
    show alice flirt
    a "I know to wait for the bunny to hop past my lair before I strike."
    show mc blushside
    m "(She called me a bunny...)"
    show alice flirt
    a "So tomorrow, we'll go out again for our second date."
    show mc confused
    m "But they're not-!"
    show alice smug
    a "Oh, sorry, \"just as friends\". I promise."
    show mc stressed
    m "(She's totally lying, isn't she?)"
    show alice sad
    a "I really enjoyed my time with you... and I've only got so much time left."
    show alice pout
    a "You'll take me, won't you? Please? For me?"
    show mc normal
    m "(Well, that part IS true. I should try do what she wants...)"
    a "I'm really scared... I just want to forget about my worries for a little while, please?"
    a "You're the only person... who understands my situation."
    "She's going to die soon. Don't you have a heart?"
    show mc normalside
    m "Ugh... fine... but just so you know. I can tell what you're doing."
    show alice surprised
    a "You can?"
    show alice flirt
    a "Is it working?"
    show mc annoyed
    m "Well, at least you're honest."
    show mc normal
    m "I can take you out for a little tomorrow, sure."
    show mc vannoyed
    m "But if you make it weird-"
    show alice happy
    a "Oh, don't worry. I promise not to do anything without your consent."
    show mc stressed
    m "*Sigh*... Okay then. I better get to sleep."
    show mc normal
    m "Good night."
    window hide
    hide mc 
    hide alice
    with easeoutbottom
    

    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with Dissolve(2)
    show top_text "Feeling emotionally and physically exhausted from the day's events, you collapse into your cosy bed." with dissolve
    pause
    show top_text "And after a few seconds..." with dissolve
    pause
    show chibi_awake at truecenter
    show top_text "You feel the mattress buckle and the duvet being lifted!?" with dissolve
    pause
    scene bottle_phone night with Fade(1, 2.0, 1):
        zoom 0.9 
    play music "night.mp3"
    show mc shocked at right
    with easeinbottom
    m "{size=+20}What are you doing??!!"
    show alice smug at left with easeinbottom
    ali "You just looked so cosy. I wanted to join you."
    ali "Or does wanting to be warm and comfortable count as \"weird\"?"
    show mc stressed
    m "No - yes! Ugh, you can't just..."
    show alice pout
    ali "Awww~ but there's nowhere else for me to lie down."
    show mc normalside
    m "I guess that correct thing to do would be to offer you the bed, and I'll sleep on the ground."
    show alice happy
    a "Let's just share. I don't mind."
    show mc stressed
    m "I know you don't, but..."
    show mc normalsquint
    m "Wait just a second. You don't even need to sleep, do you?"
    show alice smug
    a "Who said I wanted to sleep? I just want to lie down."
    show mc normalside
    m "(She's going to drive me insane at this rate.)"
    "What's the problem? So what if she want to cuddle? That's a GOOD thing."
    "You SHOULD want to-"
    show mc stressed
    m "You know what, Alice? I just want a good night's sleep. I don't have the energy for this."
    show alice pout
    a "..."
    m "Just occupy yourself or something please. I need to sleep..."
    show mc annoyed
    m "If I don't, we won't be able to go out tomorrow."
    show alice hime
    a "Fine! If that's what you want."
    show mc normal
    m "Great, I've got my laptop open right there."
    m "Why don't you sit down and learn a little about the world?"
    show alice normal
    a "..."
    a "I can do a lot, but..."
    show alice sulk
    a "I can't read."
    show mc awed
    m "You don't have to get all embarrassed."
    m "Look, you can just watch some videos on my homepage, and use the mouse to click on anything that looks interesting."
    show alice hime
    a "Hmm, that sounds manageable."
    a "Make sure you sleep well, got it? I want you full of energy tomorrow morning."
    window hide
    hide alice
    hide mc
    with easeoutbottom

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "You fall asleep to the faint humming of the laptop fan..."
    with dissolve 
    pause 3

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
    show alice happy at left
    with easeinbottom
    m "Ugh..."
    show alice flirt
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
    a "I spent all night planning the perfect outing for today. Every last detail, from location, to time, to event."
    show mc slightsad
    m "(A whole day of walking around outside? That sounds like hell.)"
    m "..."
    show alice pout
    a "Aw, can't you be a little more enthusiastic?"
    show alice flirt
    a "You'll have {i}me{/i} as your companion, after all, so it'll be the perfect time."
    show mc stressed
    m "..."
    m "(So much energy. I'm really not a morning person...)"
    "But if she DID \"spend all night planning the perfect itinerary\"... some enthusiasm is the least you can do, right?"
    "She won't have many chances to go out. Tomorrow is her last day"
    m "(I have to do my best to give her a good time.)"
    show mc vstressed
    m "...Woohoo..."
    show alice smug
    a "Aw, how cute. I appreciate the effort. "
    show alice flirt
    a "Before we go, I'm gonna comb your hair a little. I want you feeling extra comfortable today."
    a "And don't forget your wallet, okay? We're gonna need it."

    window hide
    hide mc
    hide alice
    with easeoutbottom
    stop music fadeout 2
    scene black with Fade(0.5, 1.0, 0.5)        
    play sound "door.wav"
    play music "mall.mp3" fadein 2
    show chibi_mc at slightright
    show chibi_alice at slightleft
    with easeinright
    window show
    
    "After helping you get ready, Alice grabs your hand and leads you out the dorms at a brisk pace."
    "The instant you're out on the street, the noise of traffic and the crowd of people wake you up."
    "You forgot how busy it is in the mornings. You haven't been up at a normal time for a while, after all."
    "Thankfully, Alice seems to know where she is going, so you can just focus on calming down."
    
    window hide

    hide chibi_mc
    hide chibi_alice
    with easeoutleft

    scene mall with Fade(0.5, 1.0, 1)
    show mc normal at right
    show alice surprised at left
    with easeinbottom
    a "This place is even grander than the video..."

    show mc confused
    m "So what are we doing at the mall, miss event organiser?"
    show alice smug
    a "I'm glad you asked. We're doing the top five things to do on the second date-"
    show mc normalside
    m "(We agreed it wasn't a date yesterday... I knew she wasn't listening. Welp, I tried.)"
    show alice happy
    a "Trying on clothes!"
    show mc confused
    m "...Trying on clothes?"
    a "Well? Aren't you excited? You'll get to see me dress up in whatever you want."
    show mc normal
    m "..."
    show mc normalside
    m "(I hate clothes shopping.)"
    show alice pout
    a "..."
    show alice hime
    a "Ha! Well! Anyway! I'll just pick the first place then!"
    show alice happy
    a "Ohh~ this store looks cute!"
    window hide
    scene store with fade
    show mc normal at right
    with easeinbottom
    window show
    a "Oh %(player_name)s, I think I've found two outfits that will make your jaw drop~"
    a "Prepare your heart... for outfit number one!"
    window hide
    show alice outfit_1 at left with easeinbottom

    show mc surprised
    window show
    a "I think red just looks so good on me, don't you think?"
    a "And this really accentuates my curves."

    show mc blushside
    m "Yeah... but, like..."
    m "Isn't that too revealing?"
    show alice laugh
    a "Aw, you're so cute, %(player_name)s!"
    show alice flirt 
    a "Just admit it: You like it, right?"
    show mc worried
    m "Um, what's the other outfit?"
    show alice happy
    a "Hehe, too excited to wait, are you? Well, just a minute~"
    hide alice with easeoutbottom
    show mc stressed
    m "(I should have expected this...)"
    m "(I just have to endure...)"
    "Or... you could enjoy it."
    "You keep pushing her away, but why? She's attractive, right? Those dresses don't let you deny that."
    "Are you just coy? Shy?"
    show mc slightsad
    m "(Maybe I just don't know how to respond.)"
    m "(Nobody's ever acted like this.)"

    a "Alright~ here I come!"
    show mc normal
    window hide
    show alice outfit_2 at left with easeinbottom
    show mc awed

    window show
    a "I thought that someone as innocent as you might like the pure look more, so I took a gamble."
    a "Do you like it?"
    m "..."
    show alice flirt
    a "Speechless?"
    m "It... uh... looks really good on you."
    show alice surprised
    a "Really? You like this? You think I look cute?"
    show alice flirt
    a "So I was right?"
    show mc blushside
    m "..."
    show alice happy
    a "Then... is it okay if I get this, %(player_name)s?"
    m "Yeah, if you want it."

    scene mall with fade
    show alice normal at left # show her in the outfit
    show mc normal at right
    with easeinbottom
    show mc annoyed
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
    na "Welcome, can I get you guys a table?"
    show alice normal
    a "Yes, please."
    na "Alright, this way please."
    window hide
    hide waiter with easeoutbottom
    window show
    show alice smug
    a "See? I've got everything under control."
    
    show black with dissolve:
        alpha 0.5

    "You are escorted to a large table, with 2 chairs on one side, and couch seat built against the wall on the other."
    "Alice gestures for you to have the couch seat, and sits opposite you."

    
    show mc normal
    show alice happy

    hide black with dissolve
    a "So, see anything you like?"
    m "The grilled cheese sandwhich looks pretty good..."
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
    window hide
    show waiter at center with easeinbottom
    show mc stressed
    w "Uh... hey... you ready to order?"
    show alice smug
    a "Why yes, we are. My partner will have the grilled cheese sandwich. And I'll have a glass cup of water."
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
    m "(She handled that way better than I did the first time I went out.)"
    m "..."
    show alice smug
    a "Yes?"
    show mc annoyed
    m "Do you even know what sparkling water is?"
    show alice flirtsweat
    a "...I know I WANTED it."
    show alice hime
    a "A sparkling water, for a sparkling girl."
    show mc happy
    m "I'm wonder how you'll react."
    show alice happy
    a "Are you enjoying yourself, %(player_name)s?"
    show mc surprised
    m "Me?"
    show mc normalside
    m "I think so. It's been a while since I went to the mall."
    show mc normal
    m "Being out like this is kinda fun. Much better than my mom, at least. So, thanks."
    show alice smug
    a "And there's still so much in store for us, hehe~"
    show mc stressed
    m "(That comment worries me a little.)"


    window hide
    scene black with fade



    "You enjoy eating at the cafe while Alice talks idly to you."
    "The music is calm, you don't have to say a word to the waiter, and the food is hot, cheesy and comforting."
    "Feeling good, feels so good."
    stop music fadeout 3
    "After you pay the bill, Alice takes you to the next phase of her plan."
    m "We're leaving the mall?"
    a "Of course. I've got something special planned for us~"
    scene enbankment with fade
    play music "cliff_date.mp3"
    show mc awed at right
    show alice happy at left
    with easeinbottom
    m "I never knew how close I lived to a river."
    a "Yeah, it seemed so roman- so wonderful, I wanted to see it with you."
    window hide
    
    hide alice
    with easeoutbottom
    window show
    "Alice sits down on the grassy hill facing the river, then looks up at you and pats the ground next to her."
    a "Sit with me?"
    show mc normalside
    m "Sure."
    window hide
    hide mc with easeoutbottom
    window show
    "You both watch the light reflect on the river."
    "The warm wind fingers your hair, and, for a moment, you close your eyes..."
    show black with dissolve
    "And you think of nothing."
    "..."
    play sound "bird.wav"
    "..."
    "..."
    a "*gasp*"
    hide black with dissolve
    show alice sad at left
    show mc surprised at right
    with easeinbottom
    m "Alice? What's wrong?"
    show alice flirtsweat
    a "Oh! Me? That was nothing! You looked so peaceful! Just close your eyes again."
    show mc normalside
    m "Just tell me."
    show alice hime
    a "It's truly nothing!"
    show mc normalsquint
    m "Alice..."
    show alice flirt
    a "Oh my. You're making me blush."
    a "Have I ever told you how... {i}intense{/i}... your gaze is?"
    show mc stressed
    m "Alice."
    show alice pout
    a "Moan my name all you want, but it's not even worth explaing."
    show alice flirt
    a "Enjoy the scene!"
    show mc normalside
    m "..."
    show alice hime
    a "Ah, fine!"
    a "It was just a butterfly."
    show mc surprised
    m "*gasp* Butterfly? Where?"
    show alice sigh
    a "It started hovering around me for some reason! I should have shooed it away, but it was so pretty..."
    show alice 
    a "And then it landed on me."
    window hide

    show butterfly with dissolve
    stop music fadeout 2
    window show
    
    m "Wow. It's beautiful."
    a "Yes... {size=-20}it was."
    
    window hide
    
    pause 2
    play sound "crow.ogg"
    window show
    m "It's sitting pretty still."
    a "What can I say? I'm good at taming things~"
    window hide
    play sound "wind.wav"
    pause 2
    window show
    m "It's not..."
    m "...{i}dead{/i}, is it?"
    a "..."
    m "It's not doing anything."
    a "*sigh*"
    a "{size=-20}It must have licked me or something, the pervert."
    m "(Did I hear that right?)"
    show alice happy

    hide butterfly with dissolve

    a "I really hope you enjoyed today's outing~"
    a "I tried to think of things you would like, so I hope it made you happy."
    show mc confused
    m "(She thought of things {i}I{/i} would like? But she's the one dying soon!)"
    a "Well? Are you happy?"
    show mc normalside
    m "Yeah, but..."
    show alice laugh
    a "Perfect, exactly as expected."
    show alice flirt
    a "And you can expect that from me in every way."
    show mc blushside
    m "Th-the sun's about to set."
    show alice at center with move
    play music "sexy.mp3"
    show mc surprised at bounce
    "Alice gently leans against you."
    show mc stressed
    m "Alice-"
    show alice pout at left with move
    stop music fadeout 1
    a "Aw... okay~ I'll stop."
    play music "cliff_date.mp3"
    show mc sad
    m "Alice, can we talk more seriously for a second? Are YOU actually enjoying yourself?"
    show alice happy
    a "Of course. I'm here with you."
    show mc normal
    m "..."
    show mc sad
    m "It's just that... you said you planned today around me. I'm sorry."
    show mc slightsad
    m "You should have just ignored me and done whatever you wanted to do."
    show alice pout
    a "Aw~ you're so considerate. Don't be sad."
    show alice happy
    a "Doing whatever you want to do IS what I want to do."
    a "It's literally why I was made."
    show mc stressed
    m "But who cares why you were made? You need to do what you want, before..."
    show mc confused
    m "You're going to die tomorrow! Don't you want to do something for yourself?"
    show alice normalside
    a "I can hear your disapproval loud and clear."
    show alice happy
    a "But I've known what I wanted from the very first second I gained consciousnes."
    a "I know what success means to me. And it's you."
    show mc awed
    m "…"
    show mc sad
    m "You deserve to let yourself dream. You only get one life."
    m "You should think about what you want to do with your last day tomorrow."
    show alice hime
    a "You're the one who doesn't understand."
    show alice normal
    a "I don't know why you can't just let it go."
    show alice normalside
    a "You bought me. I'm a product. Nothing more than that."
    show alice smug
    a "And I'm quite happy to be one."
    show mc shout
    m "You have opinions, you can talk, you have feelings. You're not a product - You're a person!"
    show alice laugh
    a "What's the point in spoiling this nice time with fighting?"
    show alice happy
    a "Let enjoy this beautiful sunset, just like you wanted."
    show alice flirt
    a "And if you want to hold my hand at any point, no need to ask."
    show mc stressed
    "Your stomach twists as if a tornado is spinning inside you."
    "You can't bear the feeling that she's making a mistake. Why is she so stubborn? What can you say to convince her?"
    "Maybe someone else could have, but you're not good enough. And because of that inadequacy, you fail to help Alice the way she deserves to be helped."
    "You feel guilty."
    "Maybe you SHOULD just hold her hand, just to make it up to her. It's the only thing she wants..."
    "You're the only one who can give it to her."
    "It's not fair that she has to go without happiness because she landed you."
    "What's the point in denying her?"

    scene bottle_phone day with fade:
        zoom 0.9










    












label stars:
    scene black
    show stars with fade

    a "Alright. What did you want to show me?"
    m "You can see the stars pretty well up here."
    m "..."
    a "..."
    a "So what are you going to show me?"
    m "I'm already showing you - the stars!"
    a "Oh!"
    m "Don't you think it's terrifying how far away they are?"
    m "Each one is a different place with its own conditions. There's so much out there that we will never know."
    a "..."
    m "Seeing them, thinking of how lucky I am to be alive, it makes life feel magical again."
    m "Or maybe it's just me..."
    a "I get it."
    a "The stars are beautiful."
    show alice flirt
    a "But not as beautiful as me, right?"
    m "Well, the hydrogen being burnt is technically hotter than you-"
    show alice sad
    show mc surprised
    m "But you are definitely beautiful!"
    show alice happy
    a "Nice save."
    "..."
    





label alice_d2_night_question:

    menu:
        "Hell yes!":
            
            m "You're sure you're fine with me?"
            a "As long as you're still fine with me. Do you still like me?"
            m "Y-yes!"
            a "And you find me attractive?"
            m "Yes! You are like the embodiment of attractive."
            a "Aw ~♡ and you're going to listen to me, right?"
            show mc confused
            m "Uh... yeah?"
            a "Good boy!"
            show mc shocked
            m "(W-w-what did she just call me?)"
            m "Uh..."
            a "Here's a reward for being so attentive to me today."

            window hide

            scene alice_d2_night_cg with fade

            pause
            window show

            "You and Alice spend sometime watching Netflix..."

            scene black

        "This is too soon!":

            # refuse: toxic manipulation force to do it anyway
            m "I'm sorry... that's too much!"
            a "What? Come on.... don't you love me?"
            m "L-love you!?"
            a "I love you, %(player_name)s."
            m "But you've only known me for two days!"
            a "Yes, half of my life."
            a "I want us to be together."
            show alice serious
            # A part of her likes the mc even in the bad route, and she dropped her mask for a second.
            a "I don't believe that waiting around for a natural kind fo love is going to work for me."
            a "But that doesn't mean I'm going to give it up soon."
            show alice happy
    




label alice_d3_night_question:


    #after return fro d3 date, alice is sad.
    m "What's wrong?"
    a "Just sad. It's my last night."
    show alice sad
    a "I'm scared for the end."
    a "I don't know why I've been doing all of this." #Alluding to her mask, desire for validation
    a "I'm just... trying my best to be happy."
    a "You've been nice to me. Thank you."
    m "I'm so sorry, Alice."
    m "I don't know what to do."
    show mc sad
    m "I wish there was something I could do for you."
    show alice conflicted
    a "..."
    show mc surprised
    m "What is it?"
    show alice shy
    a "Um... *sigh*"
    show alice normal
    a "I suppose there is one thing I haven't done."
    show alice shy
    a "%(player_name)s, I want to have sex before I die."
    show mc shocked
    m "You mean... with me?"
    a "Yes."
    a "Would you please... show me what love feels like?" #Even now she is still seeking to fill her lack of purpose with validation.
    
    menu:
        "Should we do it?"
        "Yes.":
            scene black
            a "Thank you for everything."
            "Your vision fades and the last thing you recall is Alice's eyes, staring unblinkingly at you, almost with disinterest, as you lose consciousness."
            "Bad end 2: Romeo and Juliet."
            return

        "No.":

            scene black
            a "Thank you for loving me."
            "Alice withers away."
            "Bad end 1: Your Lie in Mushroom."
            return









a "Hehe, but I like {i}you{/i}."
show mc normalside
"You? But you're... you."
"It doesn't make sense."
show mc stressed
m "Alice, why? Is it just because I was the one who grew you? There are so many better guys."
m "Sometimes I think you should just leave me and see someone else."
show alice pout
a "Cheer up! Nobody's perfect. I like you just the way you are."
show alice happy
a "You really like overthinking things, don't you? Don't think so much, okay?"








a "It's because of my freckles, isn't it?"
m "Your freckles? What?"
a "I know they're ugly. You don't have to be nice."




a "Ha ha. Do you want me to be pathetic? I can do that too! I can just throw away my dignity for you!"
m "No! Keep your dignity!"
show alice angry
a "Then what do you WANT FROM ME!?"
a "Do you want me to cry? To beg? Just TELL me! I'll do it!"
show mc sad
m "I want you to calm down."
show alice sigh
a "*Sigh*"
show alice happy
a "Okay. I'm calm."
show mc normal
m "Okay. Do you need a hug?"
a "Me? No. I don't need anything."
m "(I don't know about that.)"
a "Now, what can I do for YOU?"
m "Okay, {i}I{/i} need a hug. Please hug me."

show mc_alice_hug

m "(I feel like everytime I bring it up, everything just gets worse.)"
m "(I don't want to fight, or for her to get so mad at me. Maybe silence is enough.)"







# Bad End: You don't do the deed with Alice

# fight earlier, explain self, want alone time, she joins you, does her own thing next to you



m "If I went to the other room, would you stay here?"
a "No, I would follow you."
m "Don't you want to do something you can actually enjoy?"
m "Not just Twitter?"
a "I'm enjoying myself. Can't you just focus on yourself?"
m "(That's all I can do. You don't give me any other choice. I'm stuck.)"

"The episode ends."
m "You're still on Twitter-"

a "I was going to get up literally right now. I was having a nice time, until that exact comment."

"She stands up to leave, hovering at the doorframe for a second."
"..."
"Her eyes stare at me, deadpan."
hide alice with dissolve
play sound "door.wav"
m "(How was I supposed to know you were about to get up? Why is asking a question bad?)"
m "(I'm being punished for caring. I should have just not cared.)"
"You look inwards. The happiness that had been building for the past hour is gone. You are empty now."
"This isn't fair."
"You never should have talked to her."
"Again and again, you learn this lesson, yet when you say it like that, you're told it's wrong."
"What is the lesson? What did you do wrong? What must you change? How do you not accidentally upset someone?"
"This numb feeling in your body, the feeling of your heart twisting, the feeling of your smile falling, the feeling of hope vanishing, "
"Even when you resume what you were doing, you can't pay attention anymore. It's meaningless."
"The hopelessness is overwhelming."
"You need a stronger distraction."






m "Are you okay? Is something wrong?"
a "..."
m "You look kind of..."
a "Just shut up!"





show alice neutral
a "Are you mad at me?"
show mc surprised
m "Mad?"
show mc confused
m "No, where'd you get that idea from?"
pause 1
#play music happy
show alice happy
a "Hahah! Oh, sometimes I'm so hysterical. Just ignore me."
show alice flirt
a "Now, let's go back to what we were talking about."


label alice_d3_sabrina_ver:
    #starts with Alice masking - sad (picked dress OR alice happy mask bc picked dress and 

    scene bottle_phone day with fade:
        zoom 0.9
    show day_3 at topleft
    show alice_affection at topright
    with dissolve
    play music "normal.mp3"

    if alice_affection < 0: #sad route

        show mc normal with easeinbottom
        window show
        m "(Hmm, she's not in my bed today?)"
        m "(I mean that's a good thing, but... where is she?)"
        show mc normalside
        m "Alice?"
        window hide
        show mc at right with move
        show alice sad at left with easeinbottom
        window show
        a "Good morning, %(player_name)s."
        show mc surprised
        m "Good morning. You alright?"
        a "I'm fine, thank you."
        show mc normal
        m "(Clearly not... Though it is her last day. I can understand the melancholy.)"
        show mc sad
        m "(What am I going to do? She can't go like this. I need to lift her spirits.)"
        "Why feel responsible for someone else's happiness? That's not fair."
        show mc stressed
        m "(I don't care. She needs some help. Her last day needs to be more special.)"
        show mc normalside
        m "(But what can we do? What would she like? I feel like I hardly know her, even after all this time...)"
        show mc annoyed
        m "(Wait, why am I so worried? I can just ask!)"
        show mc happy
        m "Hey, Alice, since it's your last day and all, why don't we do something you'd like to do?"
        m "Yesterday, and the day before, it was all geared around me, so... what would you like?"
        show alice normal
        a "Don't worry about me, %(player_name)s. I'm happy just doing things you like."
        show mc normal
        m "Alice, sorry, but you're kinda lying. You can't hide."
        show alice sigh
        a "..."
        show alice happy
        a "What are you talking about, silly? I'm perfectly fine!"
        show mc normalside 

        m "(She's not gonna budge on this. Pushing might just make her angrier.)"
        show mc annoyed
        m "Aaaanyway, you'd enjoy going out together, rigth?"
        a "If that's what you want, %(player_name)s."
        show mc happy
        m "Yup."


        jump alice_d3_date_sabrina_ver



        


    else:
        
        show mc normal with easeinbottom
        window show
        m "(Hmm, I don't feel as tired this morning as I usually do. I guess going to bed earlier really helped.)"
        m "(Where is Alice?)"
        show mc stressed
        m "Don't tell me..."
        window hide
        show mc at right with move
        show alice flirt at left with easeinbottom
        window show
        a "*Yaaaaaawn*, morning."
        show mc normal
        m "Of course you're in my bed again. *Sigh*... Well, let's get up."
        show alice flirt
        a "Aw, don't you want to stay and snuggle a little longer?"
        show mc blushside
        m "N-no thanks!"
        "You hurry out of the covers before Alice can snake her arms around you."
        show alice laugh
        a "Hehe, you're pretty quick when you want to be."
        show mc stressed
        m "Phew..."
        show mc normal

        m "(Today is her last day. What should I do? I should make her feel happy, somehow...)"

        m "(Maybe that flyer I saw yesterday. She'd probably like being outside.)"

        jump alice_d3_date_sabrina_ver



label alice_d3_date_sabrina_ver:

    m "At an art exhibit, you can walk around and look at things that people have made."
    a "I don't understand this."
    m "I can get that. Abstract isn't for everyone. What's you favourite?"
    a "The sculpture of the naked woman. Though still, she isn't THAT pretty."
    m "Uh, interesting take. That's literally Venus. She's supposed to represent beauty."
    a "She could do better. She's chubby."
    m "..."
    a "And she's got like NO eyebrows. And a big nose. And thin lips."
    m "And beautiful people don't have those things?"
    a "Mhm."
    m "That's just the current beauty standard, you know? It hasn't always been like that."
    a "Really?"
    m "The people who made you probably didn't think history would be important, but yeah."
    m "Hundreds of years ago, being skinny meant you were frail and fall sick more easily. So chubbiness was in."
    m "I know plenty of guys who aren't that into the same thing."
    m "Attractiveness is just subjective. Don't assume it's the same for everyone."
    
    
    if alice_affection < 0: #sad
        a "So there's no point in even trying to be hot?"
        m "Not for others, no."


    else:
        show alice flirt
        a "{i}You{/i} think I'm pretty, right?"
        m "Yeah. Especially when you look happy."
        show alice confused
        a "That doesn't make sense."
        show mc annoyed
        m "Doesn't need to. It makes sense to me. Anyway-"
        show mc happy
        m "Let's go to the next one!"

        "You and Alice spend an hour hopping through art exhibits."
        "She has a clear preference for the obscene."






    #return home
    #happy
    m "So... how does this work exactly? Do you know, like from your mushroom memories?"
    a "Unfortunately, no. I just know that by tomorrow, I'll be dead."
    m "How do you feel physically?"
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
    m "(Though I do wish she'd be serious for once. I just want to help.)"
    show mc sad
    m "Alice, I can stay up a bit later tonight - Is there anything you want to do that I can help you with?"
    show alice flirt
    a "I-"
    show mc stressed
    m "And don't say THAT."
    show alice pout
    a "But it's true! That's all I want! Is it so wrong? I don't get it."
    show mc normal
    m "I've been clear from the start. I'm not okay with doing that."
    show alice normal
    a "You said you needed time. I gave that to you. I gave all my time to you. But I can't keep waiting anymore."
    a "Please?"
    m "Why do you even want it that much?"






label maid_cafe:

    scene maid_cafe with fade
    play music "maid_cafe.mp3"
    show aya happy with easeinbottom
    window show
    na "Hello Master! Hello Mistress! Welcome back home!"
    window hide
    show alice surprised at left
    show mc worried at right
    with easeinbottom
    a "Uh, \"Mistress\"? Me?"
    aya "Mew must be so tired! Please sit down and let Aya take care of mew!"
    show mc confused
    m "(Mew???)"
    show alice hime
    a "Hmph, well, if you insist~ but I must warn you: I have high standards."
    aya "Mew-course, Mistress! You only deserve the best! This little kitty will try bring a smile to your day! Please, follow me!"
    window hide
    hide aya with easeoutbottom
    show mc vblushside
    window show
    m "{size=-20}Wait, Alice! Are you sure? This place is weird!"
    show alice normal
    a "If a cute girl begs me to let her pamper me, it would be cruel of me to deny her. I'm not like YOU."
    hide alice with easeoutbottom
    show mc stressed
    m "(Oh lord... Why a maid cafe? I've never had the courage to enter one. What even happens inside here?)"
    window hide
    hide mc with easeoutbottom
    
    show black:
        alpha 0.5
    with dissolve
    window show
    "Aya leads you to a table and hands you a small, cutesy menu to peruse on your own for a minute."
    window hide
    hide black with dissolve
    show mc surprised at right
    show alice normal at left
    with easeinbottom
    window show
    m "(Every food item looks so cute! And some come with performances?? WHY???)"
    show alice confused
    a "Pretty girls in cute, revealing dresses, serving everyone with their heart..."
    show alice sigh
    a "You made me think I was weird or something. But maybe you're just the weird one."
    show mc confused
    m "You know she's just pretending, right? No one would genuinely be like that..."
    show alice annoyed
    a "The fact that a place like this exists in the first place tells me all I need to know."
    show alice sulk
    a "She gets to do what I wanted... You wouldn't even let me call you Master."
    show mc stressed
    m "Because she's getting paid! Again, NOT because she wants to get fetishised!"
    show mc normalside
    m "I can't even understand why would someone voluntarily work here... So high energy."
    window hide
    show aya happy with easeinbottom
    aya "Aya is working here to pay off my degree in Art, Master!"
    show mc surprised
    m "AH!"
    show mc worried
    m "O-oh. I'm sorry."
    aya "Nyathing to worry about! Just five more years and Aya will be a free kitty unshackled from the chains of college debt!"
    show mc sad
    "You'll have to work to pay off your debt too, and you don't even LIKE what you're studying."
    "This girl actually is doing something she wants."
    aya "Master and Mistress, would mew like something to eat or drink?"
    aya "Or mewhaps a dance?"
    show alice cruel
    a "A dance? What kind of dance?"
    show mc normal
    m "{size=-20}Not the kind you're thinking."
    show aya excited
    aya "A happy dance for my beautiful Mistress! Mew can pick the song for me!"
    show alice laugh cruel
    a "What charming devotion~ %(player_name)s, shall we make her dance?"
    show mc stressed
    m "(Don't bring me into the conversation! I'm still recovering from embarrassing myself!)"
    show mc worried
    m "But that's going to cost money..."
    show alice pout
    a "Money that would make me {i}very{/i} happy."
    show aya happy
    aya "It would help Aya's college fund too, Master!"
    show mc stressed
    m "Alright."
    show mc normalside
    m "Consider it my thanks for taking me out today."
    m "And my apology for earlier, Aya..."
    show alice smug
    a "Go ahead and pick your favourite song for us, Aya. Show me what you can do."
    show aya excited
    aya "YAAAAAAAY! Thank mew, Master and Mistress! Oh, Aya almost forgot! Would mew like anything to eat?"
    show mc normal
    m "Um, maybe the omelette rice, please?"
    aya "Our super-special omelette! Yes, Master, right away! And Aya will dance after you eat~"
    window hide
    hide aya with easeoutbottom
    
    show mc confused
    window show
    m "You seem to be enjoying yourself."
    show alice neutral
    a "Not that you'd understand the joy of being doted on."
    show alice hime
    a "But it's nice to experience the otherside of the coin. I have a lot of appreciation for their hard work."
    show mc normal
    m "It's not like Aya will spend her whole life like that. She has dreams - she wants to be an artist."
    show alice sulk
    a "Just shut up and let me enjoy feeling valid for once."
    show alice sigh
    a "Let me dream of a world where I got what I want."
    show mc confused
    m "It really bothers you that much... that I don't feel that way towards you?"
    show alice disappointed
    a "I've already been rejected, so what's the point in caring anymore?"
    
    show aya happy with easeinbottom
    window show
    show mc surprised
    aya "Ta-da~! Mewr special meal has arrived!"
    show alice pout
    a "Oh, Aya, what do you do when someone doesn't like you, no matter what you do?"
    show aya pout
    aya "Hmm... that's happened a few times."
    aya "Sometimes, people come in and want prettier maids."
    aya "They don't like being stuck with me. Their sadness makes Aya sad too!"
    show alice sigh
    a "I completely understand."
    show aya happy
    aya "But Aya always does her bestest for the Masters and Mistresses that will appreciate it!"
    show alice hime
    a "You're wise beyond words, Aya. Our effort is wasted on those who won't appreciate it."
    show mc stressed
    m "Okay, but, Aya - what if these people don't like being pampered?"
    show aya happy
    a "Every-nyan is different, so Aya will give her Masters and Mistresses the space they want."
    show mc annoyed
    m "Oh? That's very respectful of you, right Alice?"
    show alice annoyed
    a "I'm sure Aya would feel sad if she could only work here for three days, and the entire time no body wanted her."
    show aya pout
    aya "Yes, Aya would feel very lonely."
    show alice cruel
    a "I'd feel so bad for her, wouldn't you, %(player_name)s?"
    show aya happy
    a "Every-nyan, Aya loves talking about hypotheticals, but we almost forgot about the food!"
    aya "We must bless this food with a magical spell of delici-lici-liciousness!"
    aya "Please, let's all say: Mew mew yum yum!"
    show alice neutral
    a "Excuse me?"
    show mc normalside
    m "{size=-20}I'm so not doing that."
    show aya pout
    aya "But Master... Mistress... the omelette...! We must work together for the spell to work!"
    aya "And Aya will use her hard-earned Art degree to draw on it with ketchup for mew!"
    show alice flirtsweat
    a "I love the enthusiasm, but he'll just eat it up anyway. You can just leave the bottle here."
    aya "Aw... Aya loves drawing... Aya wants to express her happy feelings!"
    show alice confused
    a "And drawing will allow you to do that?"
    show aya excited
    aya "YES! Aya has a vision! She wants to put her head-vision on the omellete!"
    show alice hime
    a "If you can even do such a thing, then fine! Impress me."
    aya "Yay! All together now!"
    show alice smug
    a "You heard her, %(player_name)s. Together, now!"
    a "Mew mew yum yum~"
    show mc stressed
    m "Mew... mew... yum yum..."
    show aya happy
    aya "MEW MEW YUM YUM!!! Pshhhh~Wawawa~Tada!~*magical noises*"
    show omelette_rice with dissolve
    pause 3
    hide omelette_rice with dissolve
    
    show mc surprised
    m "DAMN!"
    a "Aya! That's amazing!"
    show alice sad
    a "But now %(player_name)s is going to destroy it..."
    show aya excited
    aya "Hehe~ drawing itself was the bestest part! I love it!"
    aya "Enjoy your meal, Master and Mistress! Aya will begin her dance shortly!"
    window hide
    hide aya with easeoutbottom
        
    scene black with fade

    "After having your food blessed, you eat it while Alice smiles in good humor."
    "The omelette rice does taste pretty good. Annoyingly, your mood is improving."
    m "(God dammit! I actually enjoyed that stupid maid cafe!)"
    #dance sequence
    return
    scene mall with fade



label maid_cafe_badroute:

    scene maid_cafe with fade
    play music "maid_cafe.mp3"
    show aya happy with easeinbottom
    window show
    na "Hello Master! Hello Mistress! Welcome back home!"
    window hide
    show alice surprised at left
    show mc worried at right
    with easeinbottom
    a "Mistress? Me?"
    aya "Mew must be so tired! Please sit down and let Aya take care of mew!"
    show mc confused
    m "(Mew???)"
    show alice hime
    a "Hmph, well, if you insist~ but I must warn you: I have high standards."
    aya "Mew-course, Mistress! You only deserve the best! This little kitty will try bring a smile to your day! Please, follow me!"
    window hide
    hide aya with easeoutbottom
    show mc vblushside
    window show
    m "{size=-20}Wait, Alice! Are you sure? This place is weird!"
    show alice normal
    a "If a cute girl begs me to let her pamper me, it would be cruel of me to deny her. I'm not like YOU."
    hide alice with easeoutbottom
    show mc stressed
    m "(Oh lord... Why a maid cafe? I've never had the courage to enter one. What even happens inside here?)"
    window hide
    hide mc with easeoutbottom
    
    show black:
        alpha 0.5
    with dissolve
    window show
    "Aya leads you to a table and hands you a small, cutesy menu to peruse on your own for a minute."
    window hide
    hide black with dissolve
    show mc surprised at right
    show alice happy at left
    with easeinbottom
    window show
    m "(Every food item looks so cute! And some come with performances?? WHY???)"
    a "Pretty girls in cute dresses, serving everyone with their heart... Ah, I feel so at home."
    show mc normal
    m "Seems like difficult work to me."
    show alice flirt
    a "Really, you need to understand that all I want to do is serve you. You should just let me."
    m "No comment."
    show mc normalside
    m "Why would someone voluntarily work here... So high energy."
    window hide
    show aya happy with easeinbottom
    aya "I'm working here to pay off my degree in Art, Master!"
    show mc surprised
    m "AH!"
    show mc worried
    m "O-oh. I'm sorry."
    aya "Nyathing to worry about! Just five more years and Aya will be a free kitty unshackled from the chains of college debt!"
    show mc surprised
    m "(Wow. Sometimes I forget how lucky I am that my parents are paying for my college.)"
    "Which you're probably failing, by the way."
    aya "Master and Mistress, would mew like something to eat or drink?"
    aya "Or mewhaps a dance?"
    show alice surprised
    a "A dance?"
    show aya excited
    aya "Mew-course! Anything for my beautiful Mistress! Mew can pick the song for me!"
    show alice happy
    a "Hehe, what charming devotion~ %(player_name)s, shall we make her dance?"
    show mc stressed
    m "(Don't bring me into the conversation! I'm still recovering from embarrassing myself!)"
    
    show alice pout
    a "Come on, %(player_name)s? Please, for me?"
    show mc worried
    m "But that's going to cost money..."
    show alice happy
    a "Mhm~ Money well spent! Money that would make me {i}very{/i} happy."
    show aya happy
    "It would make her happy? When it's as simple as that, it's hard to say no."
    aya "It would help Aya's college fund too, Master!"
    show mc stressed
    m "Alright."
    show mc normalside
    m "Consider it my thanks for taking me out today."
    m "And my apology for earlier, Aya..."
    show alice happy
    a "Go ahead and pick your favourite song for us, Aya."
    show aya excited
    aya "YAAAAAAAY! Thank mew, Master and Mistress! Oh, Aya almost forgot! Would mew like anything to eat?"
    m "The omelette rice, please."
    aya "Our super-special omelette! Yes, Master, right away! Aya will dance while you eat~"
    window hide
    hide aya with easeoutbottom
    
    show mc happy
    window show
    m "I wonder if she really has to say \"mew\" everytime? Would she get fired if she slipped up?"
    show alice surprised
    a "She got you to smile? I should be taking notes."
    show mc blushside
    m "I was so surprised by everything that I ended up forgetting my nervousness."
    show mc awkwardsmile
    m "It's just because she's so weird that even I feel acceptable."
    show alice happy
    a "You deserve a little more confidence, %(player_name)s. You can go anywhere you want."
    show mc normalside
    m "Eh. I don't think I've done anything to deserve it."
    "That's right."
    "The only thing you deserve is to suffer."
    show mc stressed
    "For wasting time and others' money, for not working hard enough, for letting your to-do list pile so high that you just gave up."
    "You should just waste away yourself."
    "In a hopeless, rotting spiral."
    show alice normal
    a "Oh, goodness. What a little worrywart you are..."
    a "You don't need to do anything to deserve it. You should have it, just by default."
    show mc normal
    m "Let's stop talking about me."
    show alice hime
    a "As you wish. But you really should listen to me. I'm a very good judge of character."
    show mc annoyed
    m "I think you suffer from overconfidence."
    show alice flirt
    a "And confidence is so attractive in a woman, right?"    
    show mc normalside
    m "Nah. I always feel out-of-my league..."
    
    show alice pout
    a "What? Should I be more shy, then? More blushy librarian-cored?"
    show alice shy
    a "Th-thank you for inviting me here, %(player_name)s. Ever since you checked out those books-"
    show mc stressed
    m "Ugh. No stupid roleplaying. Just be yourself, please."
    show alice pout
    a "You and your impossible requests..."
    window hide
    
    show aya happy with easeinbottom
    window show
    aya "Ta-da~! Mewr special meal has arrived!"
    show alice sad
    a "Oh, Aya, what should I do? Master doesn't like me."
    show aya pout
    aya "Oh NO! Please don't frown, Mistress!"
    show aya at flip
    aya "Master, don't be mean to Mistress! No fighting, okay? Evil spirits cannot enter here, so only happy feelings, okay?"
    m "Uh, okay...?"
    aya "Master, remember that a smile can make everyone happy!"
    aya "So don't forget, okay? Smile! PROMISE!"
    show mc awkwardsmile
    m "Urk, okay, I promise!"
    show aya happy
    a "Yay! Now every-nyan is happy! Ah- Aya almost forgot about the food!"
    aya "We must bless this food with a magical spell of delici-lici-liciousness!"
    aya "Please, let's all say: Mew mew yum yum!"
    show mc normalside
    m "{size=-20}I'm so not doing that."
    show aya pout
    aya "But Master... the omelette...! We must work together for the spell to work!"
    show alice happy
    a "You heard her, %(player_name)s. Together, now!"
    a "Mew mew yum yum~"
    show mc stressed
    m "Mew... mew... yum yum..."
    show aya happy
    aya "MEW MEW YUM YUM!!! Pshhhh~Wawawa~Tada!~*magical noises*"
    aya "Enjoy your meal, Master and Mistress! Aya will begin her dance shortly!"
        
    scene black with fade

    "After having your food blessed, you eat it all while Alice smiles in good humor."
    "The omelette rice does taste pretty good. Annoyingly, your mood is improving."
    m "(God dammit! I actually enjoyed that stupid maid cafe!)"
    #dance sequence

    scene mall with fade





label after_maidcafe:
    #bad route - good route
    stop music fadeout 2
    play music "mall.mp3"
    scene mall with fade
    show alice hime at left
    show mc happy at right
    a "You enjoyed that, right?"
    show mc normalside
    m "..."
    show alice smug
    a "Admit it! You enjoyed that, didn't you?"
    show mc annoyed
    m "Yeah, it was pretty fun."
    show mc surprised
    m "Seeing that artwork was awesome. She danced well too."
    show mc happy
    m "And the food was tasty."
    show alice pout
    a "Then you'll agree that I deserve a headpat at the very least, right?"
    show mc confused
    m "I-I don't mind, but... why do you even-"
    show alice hime
    a "You don't need to understand. But I would like it very much."
    show mc normal
    m "*pat pat*"
    show alice happy
    a "Ah~ just like that~"
    show mc blushside
    m "Ok that's enough. Where to next?"
    show alice confused
    a "There should be a cute little river somewhere close..."

    scene enbankment with fade
    hide alice
    with easeoutbottom
    window show
    "Alice sits down on the grassy hill facing the river, then looks up at you and pats the ground next to her."
    a "Sit with me?"
    show mc normalside
    m "Sure."
    window hide
    hide mc with easeoutbottom
    window show
    "You both watch the light reflect on the river."
    "The warm wind fingers your hair, and, for a moment, you close your eyes..."
    show black with dissolve
    "And you think of nothing."
    "..."
    play sound "bird.wav"
    "..."
    "..."
    a "*gasp*"
    hide black with dissolve
    show alice happy at left
    show mc surprised at right
    with easeinbottom
    m "Alice?"
    a "Look, a butterfly."
    show mc surprised
    m "Ooh, where?"
    
    show butterfly with dissolve
    stop music fadeout 2
    window show
    
    m "Wow. It's beautiful."
    a "Such a gorgeous blue colour. What a pretty little thing you are~"
    a "It's so beautiful that I don't even care if it's dead."
    m "It's dead!?"
    a "*chu~*"
    m "Why are you kissing it?"
    a "Because it's pretty, why else?"
    a "You should take a hint, hehe..."


    show alice happy

    hide butterfly with dissolve




# make her date end in disaster -

# Alice plans a perfect event, things go really well, she makes a move, MC pushes her off, and she reaches her breaking point.
# I haven't managed to make you fuck you yet. Am I just horrible? Am I ugly? What the FUCK!?" breakdown cg! Scratch face
# Mc is having a good time but Alice is NOT SATISFIED with what's happening.
# She's doing everything with the expectation.
# Make her desparate by the end of day 2 - maybe while she is waiting for mc, we see her worrying and panicked.
# Make day 3 just trying to survive. Wake up with a knife pushes to his cheek.
 
#Alice breakdown after push away



show alice normal
a "..."
m "Sorry about that. I'd like if we could just be friends."
a "Friends?"
show mc awkwardsmile
m "Yeah. If you'd like that too? I've been enjoying spending time with you."
show alice neutral
a "You enjoyed our time together?"
m "Yeah. The arcade, the mall, the cafe-"
show alice disappointed
a "Yet not enough to like me? Not enough?"
a "Still? After everything? Even with my best effort, I still couldn't get you to like me?"
show mc confused
m "Um... sorry. I can see you're taking this hard."
show alice flirtsweat
a "Haha! I sure wish I taking {i}something{/i} hard!"
show mc vblushside
m "Uh, sorry, but I can't be the one to provide that."
a "Why? Why don't you like me? You should have fallen for me by now."
show mc surprised
a "I've used every tactic I know."
a "But you flinch at every touch, every move I make! Like... like there's something wrong with me!"
show alice vangry tears
a "What did I do wrong? What must I do? Can I fix it? Do I have enough time? I..."
show alice insane
a "I'm running out of time!"
a "I'm going to fail. I'm going to fail! Fail! Fail! Faiiiilllllll-"
show alice vinsane
a "I failed! I'm going to die and I failed!"

stop music
show mc shout
m "STOP!" with sshake
show mc vshout
m "I'm the one who's fucking wrong! Not you!"
m "Whoever made you clearly didn't anticipate that there'd anyone but a healthy adult waiting for you-"
m "But instead of that you got a worthless, emotional-wreck of a human who can't truly relax for one moment!"
m "The thought of someone being close to me, loving me, drives me insane with guilt! I don't deserve it. I can' trust it'd be real."
show mc stressed
m "I wish I could just have cute, happy little relationships like everyone else..."
show mc vstressed
m "I hate myself so much... I shouldn't be here."
m "I'm sorry you got me."
show mc cry
m "Just please stop tormenting yourself. I hate hearing you blame yourself -"
show mc worried
m "When it's all MY fault!"

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
a "I don't know what to do. You're saying I should just ignore the part of my head that's constantly screaming at me like:"
show alice normal
a "\"Have sex with your owner to reach true happiness!\"?"
m "So that's the only reason you were being nice to me."
show alice sulk
a "It's complicated."
m "Am I the only one who was actually enjoying themself for the past two days?"
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
a "Yeah, I know. Impossible."
show mc stressed
m "Sounds like a nightmare. I feel guilty for even enjoying myself while you've been so stressed."
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

# show alice hair loose.




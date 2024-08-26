label ad1Morning:

    #Character definitions:
    define nvlChar = Character(None, kind=nvl, what_color = "#FFFFFF")
    
# I'm concerned that the narrator being another character in MC's head is forgotten in this route
    stop music fadeout(2)
    
    default aliceTrust = 0
    play music "horror.wav"
    "Everyday, you wake up, make cheap instant coffee, and spray the mycelium."
    "Today was no exception."

    show bottle_phone day with dissolve:
        zoom 0.9
        alpha 0.5
    show pulsingblack
    with dissolve

    "You wake up..."
    hide bottle_phone day
    show bottle_phone noon:
        zoom 0.9
        alpha 0.5
    show pulsingblack
    with dissolve
    "Watch Youtube Shorts until your phone dies..."
    window hide
    show mc sad with easeinbottom
    window show
    "And raise your heavy body out of bed."
    "You prepare your cheap coffee, turn back towards your bed, and place your coffee on the bed side table."
    "You shift your attention toward your proto-roommate."
    stop music fadeout(2)
    play sound "tear.wav"
    "Suddenly you hear a rustling sound from the corner of your room."

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
    
    scene bottle_phone noon with Fade(1, 2.0, 1):
        zoom 0.9

    play music "normal.mp3" fadein(3)

    #Siloutte animation of her breaking out by herself




# Initial Shock and Interaction:

# The main character’s shock at Alice’s appearance can be emphasized to highlight his social anxiety. Maybe he stumbles over his words or struggles to make sense of what’s happening,
# which would contrast with Alice’s bold and straightforward approach.
# Alice’s immediate attempt at physicality sets the tone for her character, showing her programming and how she’s driven by the need for validation. 
# This also allows the main character to reveal his discomfort with her advances, starting the theme of conflicting desires.


    show mc shocked at right
    show alice confused at left
    with easeinbottom
     
    na "So this is your room? It's so... {i}cozy{/i}."
    m "..."
    show mc shout at bounce
    m "{sc=3}{size=+40}{color=#000000}WHAT THE FUCK?!?!"
    show alice normal
    na "..."
    show alice spray
    play sound "spray.wav"
    #todo: put in a mist cloud sprite with fadeout     
    show alice fake smile
    na "What a warm welcome!"
    na "My name is Fly Amanita!"
    na "You {i}really{/i} have an interesting way with words master."
    show mc sad
    m "Sorry I uh..."
    "..."
    show mc shocked at bounce
    m "WAIT A SEC! WHO-... or...what?... THE HELL ARE YOU?!"
    m "Fly?!"
    show alice confused
    na "Are you okay master?"
    na "You should have memories of watering me for the last several weeks."
    na "I hope that you aren't suffering from any kind of neuralogical ailment"
    na "Luckily, I come prepared with knowledge for just such cases!"
    na "Although I do specialize in treating hypoxia!"
    # I don't know if this lands, I'm trying to make the joke that she's programmed to deal with brain damage from being choked by her during sex
    show alice hime
    na "Or perhaps you're just looking forward to spending the evening with me?"

    m "You're... the mushroom I bought?"
    show alice moe smile
    na "Oh, it seems that you're alright"
    show mc vshout
    m "YOU'RE TALKING!"
    show alice neutral
    na "..."
    na "Since you appear to be in good health, perhaps you could do me the favour of telling me what to call you?"
    show alice thinking
    na "Master, Onii-chan, Servant, Slave-"
    show mc shout
    m "NO! J-Just my n-name is fine..."
    na "As you wish. Your name which is?"
    show mc awed
    m "Ummm..."
    m "My name..."
    m "My name is... Ummm"
    show alice sad
    na "Are you sure you don't need me to commence a neuralogical evaluation?"
    show mc shout
    m "NO!!!"
    show mc stressed
    m "Just give me a sec..."
    "You weren't mentally prepared to talk to someone... "
    show alice neutral
    na "So, what do I call you?"
    label name_ali: 
        $name_redo = False
        $player_name = renpy.input("So, what do I call you?", length = 8).strip().lower().capitalize()
        # Reply from Skye: bad_names needs to be a global variable, and we should do the same thing in the other routes.
        # if player_name in badNames:  # you haven't define badNames yet so it makes an error as is
        #     "...%(player_name)"
        #     show alice meanLaugh
        #     na "Hold on a second... THAT'S your name?"
        #     show mc stressed
        #     m "No! I just stuttered..."
        #     na "Okay."
        #     show alice tsun
        #     na "Then what is your name then?"
        #     $name_redo = True
        #     jump name_ali
        if player_name == "":
            "Can't even remember your own name... Come on..."
            "I guess you <b>really</b> can't do anything right."
            "Just go with Ryland."
            $player_name = "Ryland"
        
        $ playername = player_name
        m "...%(player_name)s."
        
        if (name_redo):
            show alice smug
            na "So master %(player_name)s?"
            show mc angry
            m "YES!"
            m "But you can leave out the ummm... master part..."
            # show alice meanLaugh
            na "Just wanted to make sure..."
        
    show alice smug
    na "What a cute name... It {i}really{/i} suits you."
    m "What's that supposed to mean?!"
    show alice laugh cruel
    na "Nothing, {i}\"Master\" {/i} %(player_name)s."
    #She introduces herself
    
    "..."
    stop music
    show mc confused
    m "So... Getting back on topic... I thought I was supposed to be growing a mushroom?"
    show alice normal
    na "Which you valiantly succeeded in."
    m "So... You're a mushroom then? Not like a scary alien that's going to lay eggs in my stomach or something?"
    show alice mendokusai
    na "Of course not!"
    show mc awed
    m "I didn't think that mushrooms were supposed to talk... or... move..."
    show alice disgusted
    na "Well this one does"
    m "But-"
    show alice sly smile
    na "You don't need to think so hard about it!"
    na "You're going to tire yourself out"
    show alice flirt
    na " Why don't we relax a little bit and get more comfortable?"
    m "Uh, yeah, sure"
    "She sits down on the bed, and gestures for you to follow suit"
    "You hesitate for a moment, but shortly follow suit"
    # I think we need a CG here of her crawling on top of him on the bed
    na "You seem so stressed!"
    m "Well, there's kind of a lot to take in"
    na "Oh I'm sure"
    na "But that's okay!"
    na "You have me now!"
    na "You don't have to worry about anything anymore"
    m "Uh... Fly... Amanatee?"
    na "Amanita! But I know that's a mouth full"
    na "So you can call me whatever you want"
    "You take a look at her hair(?) buns, and blurt out the first thing that comes to mind"
    m "Maybe something like Alice? 'Eat me, Drink me' that sort of thing"
    na "I'm not really sure what you mean, but sure, if that's what you want!"
    m "Yeah..."
    m "Sorry, it's just so much to take in..."
    m "I started growing you because I felt like I wanted a tiny bit of responsibility"
    m "But now it's like-"
    ali "..."
    play sound "sheets.wav"
    window hide
    play music "tense.wav"
    scene PinnedDown with fade
    ali "I told you..."
    ali "You're thinking..." 
    ali "too..." 
    ali "much..."
    m "Wha- Uh- I-"
    "Before you can process whats happening you feel Alice's small hands wrap around your wrist"
    play music "heartbeat.wav"
    "Your brain to melt as a faint {color=#C4A484}sweet{/color} and {color=#C4A484}earthy{/color} scent enters your conciousness."
    "Somewhere between the smell of coffee, vanilla, cinnamon and moss."
    "You look up to see her face approaching yours"
    "Before you can consider how to react, your body moves on it's own"
    # I feel like maybe there needs to be bigger red flag before this
    menu:
        "Kiss her":
            return
        "Push her away":
            return


    # show mc surprised
    # m "...?"
    # na "So, anyway... Should we start?"
    # show mc confused
    # m "Ummm... Start...what?"

    # switch to nvl?]

    # So part of this is going on about the MC's perception of her as poisonous
    # I kind of don't know if it serves the narrative or not
    # I think it's better that it's just about him being sexually harrassed
    # show alice normal at center with move
    # show mc shocked at bounce
    # nvlChar "Without answering your question, she takes a confident lunge in your direction."
    # nvlChar "Her face appoaches yours suddenly."
    # nvlChar "You throw your center of balance backward to evade her advance, but you start to fall backwards."
    # nvlChar "Her hand pinches the neck of your oversized hoodie, preventing your descent."
    # nvlChar "She tightens her grasp and shifts her own body weight forward, bringing her face closer to yours."
    # nvl clear
    # show mc awed
    # nvlChar "You stare at her face."
    # nvlChar "Her expression remains fixed in a neutral casual, but apathetic expression as she looks down at you."
    # show black:
    #     alpha 0.2
    # nvlChar "You notice a faint {color=#C4A484}sweet{/color} and {color=#C4A484}earthy{/color} scent."
    # nvlChar "Somewhere between the smell of coffee, vanilla, cinnamon and moss."
    # show black:
    #     alpha 0.3
    # nvlChar "You have been suspended in place for what feels like several minutes."
    # nvlChar "Each passing moment, the scent seeps further into your body."
    # nvlChar "Your mind begins to melt inside your head."
    # nvl clear
    # show black:
    #     alpha 0.4
    # nvlChar "It feels warm and fuzzy, almost like a pleasant numbness spreading from to core of your conciousness."
    # nvlChar "You feel your thoughts slow to a halt."
    # nvlChar "Your gaze shifts to her lips, which shimmer as if moist."
    # show black:
    #     alpha 0.5
    # play music "heartbeat.wav"
    # show mc worried
    # nvlChar "The sound of your heart pounds violently through your ears."
    # nvlChar "Every fiber of your being is telling you to get away from her." #rewrite so not certain if sexual or even want to get away
    # nvlChar "You know intuitively, that if she gets close to you..."
    
    # nvlChar "{sc=3}{color=#FF0000}{size=+40}YOU ARE GOING TO DIE."
    # nvl clear
    # hide black
    # stop music
    # show mc vshout
    # show alice vannoyed at left with move
    # show alice shocked at left
    # play sound "slap.ogg" # find a good push/shove sf
    # m "{sc=3}{color=#000000}{size=+40}GET THE FUCK AWAY FROM ME!"
    # show alice surprised
    # na "..."
    # na "{size=-10}... you're not supposed to... I'm..."
    # show mc stressed
    # "..."
    # show mc worried
    # m "{size=+10} Sorry, I didn't mean to push you... I'm just really..."



# Alice’s Reaction to Rejection:
# Alice’s emotional shock at being rejected could be portrayed as intense, almost like she’s never experienced rejection before.
# Her fleeing the scene in search of someone new emphasizes her desperation for validation.
# The incident with the other dorm member introduces the idea that Alice doesn’t fully understand human social norms or boundaries,
# making her actions seem almost childlike in their simplicity. This could create a sense of vulnerability in her character.





    show alice sulk
    na "{size=-10}... I thought that you... were meant to..."
    na "{size=-10}...fall for me... maybe I'm just not...{size=+10} "
    show mc stressed
    m "I was kind of freaked out that you got so close all of a sudden and-"
    show alice angry tears
    na "{size=+40}SHUT UP!"
    show mc surprised
    show alice disgusted
    na "What's wrong with you?! Isn't this what you wanted?"
    show alice vangry tears
    na "ISN'T THIS WHY YOU RAISED ME?"
    show mc worried
    m "What are you talking about? I-"

    show alice sad at flip
    "She turns away from you and dashes towards the door."
    show mc surprised
    "You stare blankly at her back, as she fumbles with the lock."

    show alice angry tears
    ali "I don't need someone like you anyway..."
    show alice angry
    ali  "I can do better!"
    hide alice with easeoutbottom
    play sound "door.wav"
    "..."
    show mc awed
    m "She's gone..."
 
    show mc stressed at center with move
    play music "normal.mp3"
    m "What the fuck just happened?"
    "Your brain is still lagging behind."
    m "..."
    m "So that was the mushroom I've been growing... But it's not a mushroom..."
    show mc confused
    m "And it talks..."
    "Good job, you made a girl cry."
    "You're so good at this whole being useless bit, sometimes I forget it's not on purpose."
    "I bet you don't even know what you did."
    show mc normalside
    m "..."
    show mc shout
    m "What the hell is going on...?"
    "Why don't you figure it out?"
    show mc normalsquint
    m "... Okay... Ummm..."
    show mc confused
    m "Why don't I look at the site I got it from... There must have been some kind of mistake or something."
    hide mc with easeoutbottom


    window hide

    call screen alice_check_website with dissolve

    screen alice_check_website:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.284 ypos 0.51 idle "pc/pc_hover.png" hover "pc/pc_click.png"
            action Jump("alice_check_site")

        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.5 hover "mushroom_display/bed_hover.png" idle "mushroom_display/bed_idle.png"
            action Notify("You really just want to crawl under them and ignore Alice, but that won't do.")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.7425 ypos 0.53 hover "mushroom_display/table_hover - Copy.png" idle "mushroom_display/table_idle - Copy.png"
            action Notify("There are butt-shaped marks wiped into the dust.")    
        
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.522 ypos 0.364 hover "mushroom_display/shark_hover.png" idle "mushroom_display/shark_idle.png"
            action Notify("Blahaj will always be there for you to punch!") 
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.56 ypos 0.36 hover "mushroom_display/noot_hover.png" idle "mushroom_display/noot_idle.png"
            action Notify("Noot noot, the guard. He'll protect you from Alice, right?")     
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.304 ypos 0.48 hover "mushroom_display/noodle_hover.png" idle "mushroom_display/noodle_idle.png"
            action Notify("You haven't felt hungry in a while...")       



    
    
    label alice_check_site:       
        play sound "<from 0 to 1>type.wav"
        scene website2 with dissolve
        m "Okay, let's see what this business is \'ABOUT\'."
    call screen alice_aboutpage with dissolve

    screen alice_aboutpage:
        imagebutton:
            xanchor 0.5 yanchor 0.5 xpos 0.8125 ypos 0.120 idle "website/about_idle.png" hover "website/about_hover.png"
            action Jump("alice_about")

    label alice_about:
        window hide
        scene website_about with dissolve
        pause
    
    show mc surprised at right with easeinbottom 
    window show
    m "..."
    show mc shocked
    m "{sc=3}{color=#000000}WHAT THE FUCK IS THIS??? \nIS THIS EVEN LEGAL????"
    m "So I'm supposed to grow a \'companion\'?"
    m "Even I'm not THAT much of a loser." 
    m "Who the hell is selling this kind of thing?"
    show mc stressed
    m "..."
    m "So let me get this straight... "
    m "She's a mushroom companion... And her characteristics are... unparalleled beauty and dominance?" #match what's on the site better
    
    show mc normalside
    m "I mean, I guess she was pretty attractive..."
    show mc normalsquint
    m "...only has 3 days to live..."
    # Is that really all he has to say about this? Isn't this like really shocking? 
    show mc shocked
    m "...Do not attempt to consume unless prepared by a professional??"
    show mc worried
    m "That sounds... concerning."
    show mc confused
    m "By consume do they mean like..."
    show mc surprised
    m "Eat?"
    # m "Make sure to prepare adaquetely before consumption due to "
    # MC needs to find a part talking about her toxicity and 



    window hide
    scene bottle_phone noon with fade:
        zoom 0.9

    show mc stressed with easeinbottom
    
    window show

    "So?\n Are you any closer to figuring out what is going on?"
    show mc confused
    m "I guess so... I think maybe she was expecting for me to...um..."
    show mc blushside
    m "...{i}use{/i} her..."
    show mc confused
    m "But I still don't get why she got mad and ran off."
    "You really don't understand women do you?"
    "Or anyone for that matter."

    "You sit in your gaming chair and stare blankly at the clock on your computer taskbar."
    show mc stressed
    m "Wow, that's just a lot to take in."
    play sound("phonealarm.ogg")
    show mc shocked
    m "AAH!"
    "It's just a dischord message"
    show mc stressed
    "Oh, it's Rom."
    nvlChar "Even if you don't have any friends in the real world, you still know some people online."
    nvlChar "Even then though, you mostly talk in a small private server."
    nvlChar "There's about 10 people."
    nvlChar "Last time you went into a larger server, you couldn't quite find the timing to talk."
    nvlChar "Whenever you tried, people talked over you, and didn't seem to care about what you had to say."
    nvl clear
    "You click onto the notification window in the bottom corner of your screen and the message expands."
    jump dischord_chat

    label dischord_chat:
        # define romBestGrill = rb 
        play music "computerHum.wav"
        scene discord with fade
        rb "sup i was wondering if you wanted to hop in vc"
        "This is one of your few online friends..."
        "Normally if you prepared for a few minutes, you might be able to talk for a bit"
        "But right now, you don't have the capacity for that"
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
        m "?"
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
    m "Am I the weird one?"
    show mc worried
    m "Like... Is that how normal guy would react to this??"
    
    
    show mc stressed
    # This part goes on too long# 
    "Anyone you meet is going to be repulsed when they actually get to know you anyway."
    "That's how it always has been."
    "And always will be..."
    "You're unloveable."
    "Even if you tried- you honestly think you could be intimate with someone?" 
    "Nobody would even want to be SEEN with you!"
    show mc awed
    "..."
    show mc shocked
    m "OH FUCK!"
    m "What if someone saw her leaving my dorm?!"
    show mc stressed at center with move
    window hide
    hide mc with easeoutbottom
    play sound "door.wav"
    scene hallway with fade
    show mc worried with easeinbottom
    window show
    m "Where is she?"
    m "She wouldn't go outside..."
    show mc stressed
    m "...would she?"
    m "Aaaah! Fuck!"
    show mc sad
    m "This is way more stress than I signed up for."
    "She's probably already out in the city."
    show mc worried
    m "Does she know that you need to wait before you cross the road?"
    m "I wonder if she'd just explode into mushroom pieces if she got hit by a car..."
    show mc stressed
    #add expressions here
    m "If she's outside, she could be anywhere"
    m "The only way I could realistically find her is by asking passers-by if they saw her"
    m "And that means..."
    mc shudder
    m "Talking to people"
    "You're probably just over thinking it."
    "It's called 'Anxiety'"
    "Thought you'd be familiar with it by now"
    m "..."
    m "She got upset in the heat of the moment"
    m "But as soon as she realizes she has no shelter, she's gunna come running back"
    m "Maybe I should just go and wait for her in my room?"
    m "But-"
    m"..."


    show mc at right with move

    menu:
        "What should I do?"
        "Give up (N/A)":
            
            #example
            window hide
            show mc stressed at center with move
            show black with dissolve:
                alpha 0.5
            window show
            "She could be anywhere. This place is huge. She might have already left the dorms..."
            "She looked like she could handle herself, so..."
            "Is it really even necessary for you to even ask people if they've seen a red-headed hottie?"
            "It would be so embarrassing. They'd probably just laugh at you."
            "Let's go inside"
            show black with dissolve:
                            alpha 0.5
            "You wait..."
            "For a few minutes..."
            "Then an hours passes..."
            "2 hours..."
            play heartbeat
            "The sun begins to wane in the sky"
            "And then suddenly"
            *Knock knock*

            #show room
            m "Alice?!"
                show black with dissolve:
                            alpha 0.5
            play fastClammeringFootsteps
      
            play sound "door.wav"
            scene hallway with fade
            show mc worried with easeinbottom
            window show
            m "Huh? Where is she?"
            m "Alice?!"
            "No one is there"


            # keep going
            


            "END X:..."
            # pause 1

            # "BUT MAYBE SHE DIED."

            # hide black
            # show mc shocked

            # m "Maybe she's in trouble!"

            return

        "Search outside.":
            
     
            show mc vstressed
            "You wait for a few minutes"
            "Slowly mustering up determination from the depths of your very soul"
            m "..."
            m "Ahhhh!!! Fuck it"
            m "Here goes nothing!"
            na "KYAAAAAAAAAA!" with sshake
            show mc surprised at bounce
            m "Alice!"
            window hide
    
        


    scene bathroom with fade
    show showerguy scream at right 
    show showerguy scream at quiver
    show alice pout at left
    with dissolve
    window show
    keshad "{sc=3}{color=#000000}AAAAA!"
    ali "Why are you backing away?"
    show alice sly smile:
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
    play sound "slap.ogg"
    show alice shocked
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

    scene bottle_phone noon with fade:
        zoom 0.9

    play sound "door.wav"

    show mc normalsquint at right
    show alice annoyed at left
    with easeinbottom

    # I feel like the tone is kinda off

#     Confrontation and Apology:

# The confrontation when the main character drags Alice back could be a pivotal moment. 
# His frustration could stem not just from her reckless behavior but also from the overwhelming situation he finds himself in.
# When Alice blames the main character for rejecting her, it could trigger a moment of self-reflection for him. 
# Perhaps he realizes that his reaction was more about his own insecurities than about Alice herself, which could add depth to his apology.

# The Rooftop Scene:
# The rooftop scene with the stars is a beautiful moment where the main character tries to impart some wisdom to Alice.
# His attempt to show her that meaning can be found in anything could reflect his own struggle to find purpose in life.
# Alice’s inability to grasp the concept could underscore the gap between them, highlighting her programmed nature and lack of understanding of deeper human experiences.


    window show
    ali "Where are you dragging me you pervert?"
    ali "What kind of sick,"
    show alice flirt
    ali "tormented,"
    show alice annoyed
    ali "degenegerate things are you going to-"
    show mc vshout 
    m "{size=+20}What the fuck were you \n{sc=2}{size=+20}{color=#000000}doing{/sc} down there?!" with sshake
    show alice pout
    ali "It-"
    show mc shout
    m "You were harassing... {i}assaulting{/i} someone! My God!"
    ali "I-"
    show mc vstressed
    m "Don't you get how stupid that was?"
    show mc worried
    m "It's bad enough you let someone see you!"
    m "What am I supposed to do if they call the police?"
    show alice vannoyed at quiver
    ali "It-!"
    show mc vannoyed
    m "You {i}what{/i}?"
    # try to spell stuff to make it sound like she's sobbing
    show alice angry at bounce
    ali "It's not {i}my{/i} fault that you ignored me!"
    show alice angry tears
    ali "The only reason I went looking for someone else is because you humiliated me."
    show mc shout
    m "Hold on a sec... how did {i}I{/i} humiliate {i}you{/i}?" 
    show mc normalsquint
    ali "You bought me, and picked me out for one reason."
    show alice vangry tears
    ali "But when you actually see me, you THROW ME AWAY!"
    show alice cry
    ali "How am I not good enough for you?"
    show mc surprised
    m "What are you {i}talking{/i} about?"
    show mc worried
    m "You just came up to me, and started touching my face."
    m "and... saying weird stuff."
    #show mc stressed
    #m "And then you just ran away! I didn't do anything."

    show alice sad
    ali "But that's why you raised me right?"
    show mc shout
    m "No! It's a misunderstanding!"
    show mc stressed
    m "I didn't know anything about you until literally five minutes ago."
    show alice sulk
    ali "So what? I'm supposed to be irresitible. That's my whole thing."
    ali "That's my purpose."
    show alice disgusted
    ali "So either there is something is wrong with you..."
    show alice sad
    ali "...or there's something wrong with me."
    show mc worried
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
        "But you ARE pretty!":
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
    window hide
    show bottle_phone night:
        zoom 0.9
    with Dissolve(3)
    show mc sad
    window show
    m "It's getting kinda late... Can we think about this more tomorrow?"
    show alice surprised
    ali "You're going to sleep already?"
    # ali "But night's when all the fun stuff happens..."
    # Btw I feel alice would find a club interesting - full of hot women like her, all dancing to attract guys etc... Maybe a potential scene? 
    m "Yeah, I didn't quiet get my full 8 hours..."

    #needs something here
    
    show mc normalside
    
    m "Good night."
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
    ali "It's important to relax after tension. You know... aftercare?" #change
    show alice flirt
    ali "Or did you want to be the big spoon instead?"
    show mc vblushside
    m "No! W-why would you-?"
    show alice pout
    ali "This is all I know..."
    show alice normalside
    ali "Plus, it's not like I sleep. I'm a fungus."
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

# YouTube and Knowledge:
# Leaving the laptop with Alice introduces an interesting dynamic where she absorbs information rapidly. 
# This could lead to her developing new perspectives or even challenging the main character’s views in the days that follow.
# Her overnight binge-watching could also lead to humorous or insightful moments the next day, where she parrots back things she’s learned or misunderstood from the videos.

    window hide
    scene black with fade
    stop music fadeout(3)
    show chibi_sleep at truecenter with dissolve
    show top_text "You fall asleep to the faint humming of the laptop fan..."
    with dissolve 
    pause 3

    play sound "yay.wav"
    window show
    "You've reached the end of day 1!"
    return

# Potential Additions:
# Internal Monologue:
# The main character’s internal thoughts during these events could add depth to his character, showing his anxiety, guilt, and confusion. 
# It would also help convey his struggle with toxic masculinity and his internal gender identity conflict.

# Alice’s Perspective:
# Brief insights into Alice’s thoughts or feelings could make her more relatable. Even if she doesn’t fully understand human emotions, 
# she might have her own way of processing events, which could be intriguing to explore.

# Foreshadowing:
# Small hints about Alice’s limited lifespan or the company’s motives could be woven into the narrative subtly, 
# creating a sense of impending conflict and adding tension to their interactions.


# ----------------------

# - bad route idea: he dies, but it’s not her poison that kills him. It’s his OVERREACTION and fear of her poison that kills him.

# more conflict in terms of like maybe
# them brushing off this gendered society thing to each other
# like "you have it so much easier"
# i think like
# a fundamental women experience is that there's an assumed like
# standard of beauty and those below it are hardly considered like
# people
# but if you are concerned at all with being over that line, and being into beauty or whatever
# then you're seen as vain
# that double standard feels very important here
# like the contrast between a society that punishes you for not complying, but berates your attempts to comply
# So I want to fit that in some how

   

#MC explains that humans too have biological instincts for survival
#There's some stuff we can't ignore, like food, water, shelter love
#But sometimes that desire causes more problems for us like obesity with candy
#Sometimes those instincts lead for us to harm the environment, step on other people, and to be discimantory
#As sentient things, we need to learn to overcome our 'nature' sometimes, in order for us to be happy
#Obviously it's not that simple
#but mc wants alice to find what makes her happy outside of her assigned purpose


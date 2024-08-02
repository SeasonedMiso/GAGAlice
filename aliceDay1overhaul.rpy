
THIS DAY NEEDS MAJOR TWEAKS
-Alice = valley girl not ojousama
-Make it clear that alice's trauma is the expectation that she's sexually desireable
-make the conflict make sense and natural
-Make the resolution make sense, but leave them as like acquaintances, not friends



##Check all the comments and non spoken lines from ori
label: ad1Morning
    stop music fadeout(2)
    show black with fade
    
    $aliceTrust = 0
    
    "Everyday, you woke up, made cheap instant coffee, and sprayed the mycelium "
    "Today was no exception"
    "You wake up..."
    "Watch Youtube Shorts until your phone dies..."
    "And raise your heavy body out of bed."
    "You prepare your cheap instant coffee, turn back towards your bed, and place your coffee on the bed side table."
    "You shift your attention toward your proto-roommate"
    "Suddenly you hear a rustling sound from the corner of your room "
       #Siloutte animation of her breaking out by herself
    show mc shocked at right with move
    show alice tsun at left 
    na "So this is your room? Smaller than I hoped for but I guess this will work."
    m "..."
    m "WHAT THE FUCK?!?!"
    na "..."
    "The girl that emerged from your mushroom box unapologetically grabs the spray bottle on the table beside her"
    "She pulls the trigger and a cloud of mist appears in front of her"
    "She steps slowly through it and towards me"
    
    show alice tsun annoyed
    na "Warm fucking welcome..."
    na "You /really/ have a way with words."

    show mc sad
    m "I'm sorry..."
    "..."
    show mc shocked
    m "WAIT A SEC! WHO-... or...what?... THE HELL ARE YOU?!"
    show alice sad
    na "That's tragic..."
    na "I hoped my client would be like mentally all there or whatever"
    na "But I guess I just have that effect on people."    

    show alice despair
    na "Actually tragic..."
    m "You're... the mushroom I bought?"
    na "And you aren't brain damaged?"

    show mc angry
    m "THAT'S MY LINE!!!"
    m "YOU'RE TALKING!"
    show alice neutral
    na "..."
    na "Well since your brain is functioning to _some_ level, maybe you could tell me what to call you?"
    show mc awed
    m "Ummm... My name..."
    show alice sad
    na "My bad, I should have picked something easier for you right?"

    show mc angry
    m "NO!!!"
    show mc sad
    m "Just give me a sec..."
    "You weren't mentally prepared to need to talk to someone... "
    show alice neutral
    na "So, what do I call you?"
    label name_ali: 
        $name_redo = False
        $playername = renpy.input("So, what do I call you?", length = 8).strip().lower().capitalize()
        if playername in badNames:
            "...%(player_name)"
            show alice meanLaugh
            na "Hold on a second... THAT'S your name?"
            show mc stressed
            m "No! I just stuttered..."
            na "Okay."
            show alice tsun
            na "Then what is your name then?"
            $name_redo = True
            jump name_ali
        if playername = "":
            "Can't even remember your own name... Come on..."
            "I guess you <b>really</b> can't do anything right."
            "Just go with Finn."
            $playername = "Finn"
        m "...%(player_name)s."
        show alice smug
        if (name_redo):
            na "Are you sure this time?"
            show mc angry
            m "YES!"
            show alice meanLaugh
            na "Just wanted to make sure..."
        show alice smug
        na "What an cute name... I guess it suits someone like you."
        m "What's that supposed to mean?!"
        show alice meanLaugh
        na "What ever you want."
        "...'
        stop music
        
        m "So... Getting back on topic... I thought I was supposed to be growing a mushroom?"
        na "Well, I guess you were able to succeed in {i}something{/i} at least."
        m "So... You're a mushroom then? Not like a scary alien that's going to lay eggs in my stomach or something?"
        na "What are you talking about?"
        "I didn't think that mushrooms were supposed to talk... or... be animate..."
        na "You seem to REALLY like asking about stupid shit"
        na "How about you stop thinking so hard, and we get more comfortable?"
        "She protudes the aura of a queen sitting on a throne."
        
        na "..."
        na "So, anyway... Should we start?"
        m "Ummm... Start...what?"

# switch to nvl?]

# So part of this is going on about the MC's perception of her as poisonous
# I kind of don't know if it serves the narrative or not
# I think it's better that it's just about him being sexually harrassed
        "Without answering your question, she takes a confident lunge in your direction"
        "Her face appoaches yours suddenly"
        "You throw your center of balance backward to evade her advance, but you start to fall backwards"
        "Her hand pinches the neck of your oversized hoodie, preventing your descent"
        "She tightens her grasp and shifts her own body weight forward, bringing her face closer to yours."
        "You stare at her face"
        "Her expression remains fixed in a neutral casual, but apathetic expression as she looks down at you."
        
        "You notice a faint sweet, and somewhat earthy scent"
        "Somewhere between the smell of coffee, vanilla, cinnamon and moss"
        "You have been suspended in place for what feels like several minutes"
        "Each passing moment, the scent seeps further into your body"
        "Your mind begins to melt inside your head"
        "It feels warm and fuzzy, almost like a pleasant numbness spreading from to core of your conciousness"
        "You feel your thoughts slow to a halt"
        "Your gaze shifts to her lips, which shimmer as if moist"
        "The sound of your heart pounds violently through your ears"
        "Every fiber of your being is telling you to get away from her"
        "You know intuitively, that if she gets close to you..."
        "YOU ARE GOING TO DIE"
        
        show mc stressed
        m "...!"
        m "GET THE FUCK AWAY FROM ME!!"
        show alice shock
        na "..."
        na "{size=-10}... you're not supposed to... i'm..."
        "..."
        m "{size=+10} Sorry, I didn't mean to yell... I'm just really..."
        "You trail off after noticing that she contiues to mumble to herself."
        "She's clearly not listening"
        na "{size=-10}... i thought that you... were meant to..."
        "lose.. reason... maybe i'm just not...{size=+10} "
        m "Hey, I'm trying to apologize but I need you to listen."
        m "I was kind of freaked out that you got so close all of a sudden and-"
        na "SHUT UP!"
        "She suddenly snaps at you"
        "Her face twists with rage and pain"
        na "What's wrong with you?! Isn't this what you wanted?"
        na "ISN'T THIS WHY YOU RAISED ME?"
        m "What are you talking about I-"

        show alice sad
        "She turns away from you and dashes towards the door."
        "You stare blankly at her back, as she fumbles with the lock."


        ali "I don't need someone like you anyway..."
        ali  "I can do better!"
        "..."
        m "She's gone..."
        "Your line of sight slowly drops towards the floor as you hang your head"
        "You notice several shimmering drops of clear liquid on the wooden flooring."
    
        show mc stressed at center
        play music normal
        m "What the fuck just happened?"
        "Your brain is still lagging behind."
        m "..."
        m "So that was the mushroom I've been growing... But it's not a mushroom..."
        show mc tired
        m "And it talks..."
        show mc stressed
        "Good job, you made a girl cry"
        "You're so good at this whole being useless bit, sometimes I forget it's not on purpose"
        "I bet you don't even know what you did"
        m "..."
        m "What the hell is going on..."
        "Why don't you figure it out?"
        m "... Okay... Ummm..."
        m "Why don't I look at the site I got it from... There must have been some kind of mistake or something."

        m "Okay let's see what this buisness is 'ABOUT'"
        m "WHAT THE FUCK IS THIS??? IS THIS EVEN LEGAL????"
        m "So I'm supposed to grow a companion?"
        m "Even I'm not THAT much of a loser." 
        "Who the hell is selling this kind of thing? And who is buying it?"
        m "..."
        m "So let me get this straight... "
        m "She's a mushroom companion... And her characteristics are... Unparalleled beauty and dominance?"

        m "I mean, I guess she was pretty attractive, but I wasn't really paying attention to that."
        m "...only has 3 days to live..."
        # Is that really all he has to say about this? Isn't this like really shocking? 
        
        "So? Are you any closer to figuring out what is going on?"
        
        m "I guess so... I think maybe she was expecting for me to... ummm "
        m "{i}use{/i} her..."
        m "But I still don't get why she got mad and ran off"
        "You really don't understand women do you?"
        "Or anyone else for that matter"
        "You sit in your gaming chair and stare blankly at the clock on your computer taskbar"
        m "Wow, that's just a lot to take in"
        play sound('message_notify.wav')
        show mc shocked
        m "AAH!"
        "It's just a dischord message"
        "Oh it's Rom "
        "Even if you don't have any friends in the real world, you still know some people online."
        "Even then though, you mostly talk in a small private server"
        "There's about 10 people"
        "Last time you went into a larger server, you couldn't quite find the timing to talk"
        "Whenever you tried, people talked over you, and didn't seem to care about what you had to say"
        "You click onto the notification window in the bottom corner of your screen and the message expands"
        label dischord_chat:
            define romBestGrill = rb
            play music computerHum

            rb "sup i was wondering if you wanted to hop in vc"
            "this is one of my few online friends..."
            "Normally if you internally prepared for a few minutes, you might be able to talk for a bit"
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
            "you think about if you should tell him about what just transpired"
            m "you probably won't believe me so..."
            rb "don't be like that"
            m "fine"
            m "You know I told you I was growing mushrooms... Well this is where I ordered them from and ummm "
            m "It bloomed today... into a girl"
            rb "lmao nice nice"
            m "and then umm "
            m "She got all close to me and then ran off crying..."
            rb "wait, did you make this site? I didn't know you could make websites"
            rb "it looks so professional"
            rb "how many hours did it take"
            m "?"
            rb "like for a joke it's based"
            m "I can't code, and it's real."
            rb "wait like real real>"
            m "yeah"
            rb "emoji upside down smile"
            rb "lmao wtf"
            rb "let me order one real quick"
            rb "I wonder if I can get it to cosplay Rom "
        m "What? Is he not listening to me?"
            m "are you for real?"
            rb "like was she hot? I've always wanted a girlfriend that can become my waifu"
            m "I'm being serious, she's like a living being... She talks and moves and everything"
            rb "sounds like I don't need my onahole anymore"
        m "What the fuck?"
            m "I'm sorry, I think i've gotta go"
            rb "don't have too much fun"

        "You close the window, and turn away from your computer screen."
        show mc stressed
        m "Am I the weird one?"
        m "Like... Is that how I'm supposed to act?"
        m "Is that how guys are supposed to think about girls?"
        m "Like... Is this sort of buisness just like... normal?"
        "
        "You're just afraid"

        "Anybody who gets to know you is going to be repulsed when they actually get to know you anyway."
        "That's how it always has been"
        "And always will be..."

        m "Tch, just remembered something I was trying to forget"
        "You're unloveable"
        "Even if you tried: you honestly think that YOU could play the role of boyfriend to someone" 
        "Nobody would even want to be seen with you"
        "..."
        m "OH FUCK!"
        "You spring out of your chair."
        m "What if someone saw her leaving my dorm?!"

        m "I need to find her, and make sure no one sees her" 

        "You walk over to the door and walk through it into the corridor."
        "You look towards both ends of the passage, but no one is there."
        
        Choice: Where go???

    #go out to the enterance
    #mental preparation, scared of going out to look
    #hear a scream
    #Run towards location (shower)
    #KYAAA! it's shadow person
    #She closing in about to try to get closer to him
    #You grab her in the nick of time
    #pull her back to your room
    change scene to main gate
    m "Fuck... There's no sight of her anywhere"
    m "She wouldn't go outside..."
    m "Would she?"
    m "Aaaah! Fuck!"
    m "This is way more stress than I signed up for"
    "She's probably already out in the city"
    "I wonder if she knows that you need to wait to cross the road"
    "That would be an interesting ambulance call"

    m "Ahhhh!!! Damn it... Maybe I should just..."

    Choice "Head back to room to wait for her to come back" "Go outside"
    Go outside:
    m "I can't just give up"
    m "She could be in trouble"
    m "Fuck it! Here goes nothing"
    "As you place your hand on the front door of the dormitory entrance"
    na "KYAAAAAAAAAA!"
    m "Alice!!"
    
    scene transition to black 
    transitoin to kitchen
    transition to bathroom
    keShad "AAAAA"
    ali "Why are you backing away from me?"
    ali "Don't you want to get closer to me?"
    keShad "AAAAHHGH"

    show mc sprite approaching alice
    Slap sound effect
    then dragging her off screen

    fade to black

    dragging her into your room

    # I feel like the tone is kinda off

    ali "Where are you dragging me you pervert?"
    ali "What kind of sick,"
    ali "tormented"
    ali "degenegerate things are you going to-"
    m "What the fuck were you doing down there?!"
    ali "It-"
    m "You were harassing... assaulting someone"
    ali "I-"
    m "Don't you get how stupid you are?"
    m "It's bad enough you let someone see you"
    m "What am I supposed to do if they call the police?"
    ali "It-"
    m "You what?"
    # try to spell stuff to make it sound like she's sobbing

    ali "It's not my fault that you ignored me!"
    ali "The only reason I went looking for someone else is because you humiliated me"
    m "Hold on a sec... I how did I humiliate you?"
    ali "You bought me, and picked me out for one reason"
    ali "But when you actually see me, you throw me away"
    ali "How am I not good enough for you?"
    m "What are you talking about?"
    m "I you just came up to me, and started touching my face"
    m "and... saying weird stuff"
    ali "But that's why you raised me right?"
    m "No! It's a misunderstanding"
    m "I didn't know anything about you until literally a few hours ago"
    ali "So what?"
    ali "I'm supposed to be irresitible"
    ali "That's my whole thing"
    ali "That's why I'm valueble"
    # I feel like this is too introspecive
    ali "So there's either there's something wrong with me, or something wrong with you"
    m "So... That's why you went to find someone else"
    ali "I guess..."
    ali "But all he did is scream"
    ali "..."
    ali "Is there something wrong with how I turned out?"
    ali "Maybe it's my face or..."
    #Choice: It's okay ; I think you're valueble ; step on me mommy; 
    #You're valueble
    m "You're incredibly pretty"
    m "So much that anyone would be jealous"
    m "..."
    m "Especially compared to someone so plain like me"
    ali "Oh yeah, self depreciation always makes people feel better"
    m "Anyway, I was just trying to say that..."
    m "I don't think that's what makes you valueble"
    ali ""
    m "..."

    
    







 #you yell at her for attempting to assault a random person
    #Also that if people see you in here, it will cause problems for you
    #She starts crying and says it's you fault for not giving her attention
    #She explains that it hurt her because she's supposed to be attractive and alluring
    #And so it makes her feel like a failure





# mc checks website. shocked that she  only lives for 3 days.
# she’s like “I know, and I have to spend it with YOU.”

# He also sees that she’s poisonous and freaks out. Alice is annoyed by his reaction and hints at this hatred/fear towards her being unjustified and unfair. 
# “You think they’re going to kill their customer base? They thrive on repeat customers.”

# She’s a bit sad/angry. “Relax. i won’t do anything anyway. I can tell I’m not wanted.”

# - bad route idea: he dies, but it’s not her poison that kills him. It’s his OVERREACTION and fear of her poison that kills him.

# Tension again. He wants to clear the air a bit. suggests goes to rooftop. He talks excitedly about the stars. She’s like “Okay I guess. i don’t really see the point.” He describes how people can find meaning in the stars. she SUBTLY goes from making fun of it and calling it stupid to warming up to it.

# Back at room. When he gets in to sleep, she starts to pull back the cover and climb in bc she assumed that’s what she was supposed to do.

# She demands he gives her something to do while he sleeps. “What, you expect me to just wait?”
# mc says he guesses she can just go on her laptop.


# Bad end where alice disfigures her face to look prettier






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







#as a mushroom, she doesn't have memories or a sense of personal identity


 
   
    
    #as a mushroom, she doesn't have memories or a sense of personal identity
	#She does have instinct and the information in her DNA
	#In that DNA there's a clear purpose, be desireable, be pretty
	#If she isn't those things, she has no sense of meaning
	#That's why she wants for him to look at her
	#To use her
	#So that she can feel like it was worth it.
	#Not because she likes him, or wants to do the act as itself, but because she wants the validation it implies.
    
    #MC explains that humans too have biological instincts for survival
	#There's some stuff we can't ignore, like food, water, shelter love
	#But sometimes that desire causes more problems for us like obesity with candy
	#Sometimes those instincts lead for us to harm the environment, step on other people, and to be discimantory
	#As sentient things, we need to learn to overcome our 'nature' sometimes, in order for us to be happy
	#Obviously it's not that simple
	#but mc wants alice to find what makes her happy outside of her assigned purpose
	

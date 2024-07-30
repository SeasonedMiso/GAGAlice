
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
<<<<<<< HEAD
    na "So this is your room? Smaller than I hoped for but I guess this will work."
=======
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
    m "..."
    m "WHAT THE FUCK?!?!"
    na "..."
    "The girl that emerged from your mushroom box unapologetically grabs the spray bottle on the table beside her"
    "She pulls the trigger and a cloud of mist appears in front of her"
    "She steps slowly through it and towards me"
    
    show alice tsun annoyed
<<<<<<< HEAD
    na "Warm fucking welcome..."
    na "You /really/ have a way with words."
=======

>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8

    show mc sad
    m "I'm sorry..."
    "..."
    show mc shocked
    m "WAIT A SEC! WHO-... or...what?... THE HELL ARE YOU?!"
    show alice sad
<<<<<<< HEAD
    na "That's tragic..."
    na "I hoped my client would be like mentally all there or whatever"
    na "But I guess I just have that effect on people."    
=======
    #I think the word she chooses to use here to address him such as client, parent, guardian, is really important! come back here later
    na "That's tragic... I hoped my client would be like mentally all there or whatever"
    #make this line more PC
    na "But I guess I just have that effect on people."    
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8

<<<<<<< HEAD
=======
    #na "How pitiful... I would have hoped that my client would be able to perform basic congnitive tasks"
    #na "But I suppose the surreal allure of my visage is beyond your comprehension"
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
    show alice despair
    na "Actually tragic..."
    m "You're... the mushroom I bought?"
<<<<<<< HEAD
    na "And you aren't brain damaged?"
=======
    na "So you aren't brain damaged?"
    #This is actually good foreshadowing for her toxicity
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8

<<<<<<< HEAD
=======
    #na "It seems you have something resmebling sentience... Well Done."
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
    show mc angry
    m "THAT'S MY LINE!!!"
    m "YOU'RE TALKING!"
    show alice neutral
<<<<<<< HEAD
    na "..."
    na "Well since your brain is functioning to _some_ level, maybe you could tell me what to call you?"
=======
    na "..."
    #na "Seeing as your brain is functioning to _some_ degree, perhaps you could tell me your name?"
    na "Well since your brain is functioning to _some_ level, maybe you could tell me what to call you?"
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
    show mc awed
    m "Ummm... My name..."
    show alice sad
<<<<<<< HEAD
    na "My bad, I should have picked something easier for you right?"

=======
    na "My bad, I should have picked something easier for you right?"
    #The scene is like: She thinks that maybe you've been poisoned by her already, but she's phrasing it so it's like
    #her look sare the reason why you are cognitively impared
    #She's kind of making fun of you
    #But mc is just nervous
    #Don't actually know if I like this convo, maybe rewrite
    
    
    #na "Forgive me, I should have chosen a less challenging display of intelligence."
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
    show mc angry
    m "NO!!!"
    show mc sad
    m "Just give me a sec..."
    "You weren't mentally prepared to need to talk to someone... "
    show alice neutral
<<<<<<< HEAD
    na "So, what do I call you?"
=======
    na "So, what do I call you?"
    #name input

>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
    label name_ali: 
        $name_redo = False
        $playername = renpy.input("So, what do I call you?", length = 8).strip().lower().capitalize()
        if playername in badNames:
            "...%(player_name)"
            show alice meanLaugh
<<<<<<< HEAD
            na "Hold on a second... THAT'S your name?"
=======
            #like aqua from konosuba or uminekoBeatrice
            na "Hold on a second... THAT'S your name?"
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
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
<<<<<<< HEAD
        na "You seem to REALLY like asking about stupid shit"
        na "How about you stop thinking so hard, and we get more comfortable?"
=======
        na "You seem to REALLY like asking about stupid shit"
        #na "You really seem to enjoy asking meaningless questions."
        na "How about you stop thinking so hard, and we get more comfortable?"
        #na "Why don't you stop thinking about hard stuff, and relax a little bit?"
        "She lowers herself down onto the corner of the bed and leans back slightly, crossing one leg ontop of the other.'        
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
        "She protudes the aura of a queen sitting on a throne."
        
<<<<<<< HEAD
        na "..."
        na "So, anyway... Should we start?"
=======
        #here she tries to get you to stop asking questions, and come over to her
        #instead of these lines I think it should be more like she's getting fed up with her advances not working.


        na "..."
        na "So, anyway... Should we start?"
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
        m "Ummm... Start...what?"

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
<<<<<<< HEAD
        na "..."
        na "{size=-10}... you're not supposed to... i'm..."
=======
        "You look back up at the girl, whose face is frozen with shock" 
        na "..."
        "Slowly, her expression darkens, and her bottom lip begins to tremble, as she turns her face downwards"
        na "{size=-10}... you're not supposed to... i'm..."
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
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
<<<<<<< HEAD
    
=======
        #is it even wood in the cg?


	
	#She tries once again to reinitiate
	#But this time mc is more vocal/aggresive, and it shocks her
    #choice: horrible turn down, passive let her do whatever, let her down nicely
	na "...So... You don't want me?"      
        m "?"
        na "That's not what's supposed to happen..."
        na "I'm supposed to entice anyone to abandon reason."
        na "But you..." 
        m "I'm trying to tell you I-"
        show alice shoutTears
        na "SHUT UP!"
        show mc shocked
        m "..."
        show alice crying
        na "..."
        na "{size=-8}What's wrong with me...{size=+8}"
        hide alice with easeoutbottom
        "Before you can open my mouth, she turns towards the door"
        "She swiftly turns the door knob and runs out"
        "You hear her sobbing echo through the dormitory passage, and then fade into the distance"
        #maybe you only learn her name on the rooftop?
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
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
        #too obvious, rewrite to be more subtle
        #i feel like this interaction maybe needs more impact?
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
        #what is he afraid of? just that he will be noticed? Why is being with a girl a negative thing?
        m "I need to find her, and make sure no one sees her" 

        "You walk over to the door and walk through it into the corridor."
        "You look towards both ends of the passage, but no one is there."
        
        Choice: Where go???


<<<<<<< HEAD
=======
    #choice: Go back to your room and wait for her to come back (forget about her)
        #Go look outside
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8


<<<<<<< HEAD


then goes to look
not sure where to look = anxious. hypes self up to go outside and search
hears a girlish squeal
runs to bathroom
he thinks it’s alice’s screaming, but once inside she’s like wtf it was him not me - points to neighbour showering.
neighbour is a eldritch blob (on the friendlier/shocked side with dyed hair). in funny jojo pose covering parts and very scared.
brief argument where alice chastises mc on being too scared to do her.


mc grabs alice and takes back to room
argument: she blames him for her actions. angry tear up. “What am I supposed to do? you’re an asshole and how else am i going to get that affection.”
he is still annoyed and awkward and flustered but apologises to get bed to feel better since she’s crying a bit. especially since inner thoughts guilt him.
she brushes off his tenderness
“Oh whatever.”
this irks him and he’s like “Fine if you’re not ready to hear it.”

However they agree to disagree.
mc checks website. shocked that she  only lives for 3 days.
she’s like “I know, and I have to spend it with YOU.”

He also sees that she’s poisonous and freaks out. Alice is annoyed by his reaction and hints at this hatred/fear towards her being unjustified and unfair. “You think they’re going to kill their customer base? They thrive on repeat customers.”

She’s a bit sad/angry. “Relax. i won’t do anything anyway. I can tell I’m not wanted.”

- bad route idea: he dies, but it’s not her poison that kills him. It’s his OVERREACTION and fear of her poison that kills him.

Tension again. He wants to clear the air a bit. suggests goes to rooftop. He talks excitedly about the stars. She’s like “Okay I guess. i don’t really see the point.” He describes how people can find meaning in the stars. she SUBTLY goes from making fun of it and calling it stupid to warming up to it.

Back at room. When he gets in to sleep, she starts to pull back the cover and climb in bc she assumed that’s what she was supposed to do.

She demands he gives her something to do while he sleeps. “What, you expect me to just wait?”
mc says he guesses she can just go on her laptop.


Bad end where alice disfigures her face to look prettier


#as a mushroom, she doesn't have memories or a sense of personal identity


    #go out to the enterance
    #mental preparation, scared of going out to look
    #hear a scream
    #Run towards location (shower)
    #KYAAA! it's shadow person
    #She closing in about to try to get closer to him
    #You grab her in the nick of time
    #pull her back to your room
    #you yell at her for attempting to assault a random person
    #Also that if people see you in here, it will cause problems for you
    #She starts crying and says it's you fault for not giving her attention
    #She explains that it hurt her because she's supposed to be attractive and alluring
    #And so it makes her feel like a failure
    
    #as a mushroom, she doesn't have memories or a sense of personal identity
=======
    #go out to the enterance
    #mental preparation, scared of going out to look
    #hear a scream
    #Run towards location (shower)
    #KYAAA! it's shadow person
    #She closing in about to try to get closer to him
    #You grab her in the nick of time
    #pull her back to your room
    #you yell at her for attempting to assault a random person
    #Also that if people see you in here, it will cause problems for you
    #She starts crying and says it's you fault for not giving her attention
    #She explains that it hurt her because she's supposed to be attractive and alluring
    #And so it makes her feel like a failure
    
    #as a mushroom, she doesn't have memories or a sense of personal identity
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
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
	
<<<<<<< HEAD
=======
	#She looks at the vastness of the city and feels like there's more possibility than she could have imagined
	#Maybe even she can try to find some kind of meaning in life 
	#Everything in life is meaningless, so we get to pick whats meaningful for ourselves.
	#She acts dismissive but smiles faintly at you and feels a little better
	#it's important here that she's not in as much as a state, but that she's not completely over it: just enough to make it possible for the 2 of you to get along
>>>>>>> b459953adb52acc51cdd679c0da4e005bc6e2ce8
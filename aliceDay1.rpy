
#feel like it's not funny enough, prob needs more humour

#na is unknown speaker
#[make character beeps dif for Alice and Button]


THIS DAY NEEDS MAJOR TWEAKS
-Alice = valley girl not ojousama
-Make it clear that alice's trauma is the expectation that she's sexually desireable
-make the conflict make sense and natural
-Make the resolution make sense, but leave them as like acquaintances, not friends

label: ad1Morning
    stop music fadeout(2)
    show black with fade
    
    #variables
    $aliceTrust = 0
    #keep original script up to "{size=-8}"
    
    #TODO: add normal morning thing here


    "Everyday, you woke up, made cheap instant coffee, and sprayed the mycelium "
    "Today was no exception"
    "You wake up..."
    "Watch Youtube Shorts until your phone dies..."
    "And raise your heavy body out of bed."
    "You prepare your cheap instant coffee, turn back towards your bed, and place your coffee on the bed side table."
    "You shift your attention toward your proto-roommate"
    #fix 
    "Suddenly you hear a rustling sound from the corner of your room "
    #Siloutte animation of her breaking out by herself
    show mc shocked at right with move
    show alice tsun at left 
    #First line is super important so come back later
    #Make it more impactful, pretending to be something you're not
    na"So this is your room? Smaller than I hoped for but I guess this will work."
    m "..."
    m "WHAT THE FUCK?!?!"
    na"..."
    "The girl that emerged from your mushroom box unapologetically grabs the spray bottle on the table beside her"
    "She pulls the trigger and a cloud of mist appears in front of her"
    "She steps slowly through it and towards me"
    
    #staring down at you cruelly
    show alice tsun annoyed
    na"Warm fucking welcome... You /really/ have a way with words."

    #gets reflexively small and subby
    show mc sad
    m "I'm sorry..."
    "..."
    show mc shocked
    m "WAIT A SEC! WHO-... or...what?... THE HELL ARE YOU?!"
    show alice sad
    #I think the word she chooses to use here to address him such as client, parent, guardian, is really important! come back here later
    na"That's tragic... I hoped my client would be like mentally all there or whatever"
    #make this line more PC
    na"But I guess I just have that effect on people."    

    #na"How pitiful... I would have hoped that my client would be able to perform basic congnitive tasks"
    #na"But I suppose the surreal allure of my visage is beyond your comprehension"
    show alice despair
    na"Actually tragic..."
    m "You're... the mushroom I bought?"
    na"So you aren't brain damaged?"
    #This is actually good foreshadowing for her toxicity

    #na"It seems you have something resmebling sentience... Well Done."
    show mc angry
    m "THAT'S MY LINE!!!"
    m "YOU'RE TALKING!"
    show alice neutral
    na"..."
    #na"Seeing as your brain is functioning to _some_ degree, perhaps you could tell me your name?"
    na"Well since your brain is functioning to _some_ level, maybe you could tell me what to call you?"
    show mc awed
    m "Ummm... My name..."
    show alice sad
    na"My bad, I should have picked something easier for you right?"
    #The scene is like: She thinks that maybe you've been poisoned by her already, but she's phrasing it so it's like
    #her look sare the reason why you are cognitively impared
    #She's kind of making fun of you
    #But mc is just nervous
    #Don't actually know if I like this convo, maybe rewrite
    
    
    #na"Forgive me, I should have chosen a less challenging display of intelligence."
    show mc angry
    m "NO!!!"
    show mc sad
    m "Just give me a sec..."
    "You weren't mentally prepared to need to talk to someone... "
    show alice neutral
    na"So, what do I call you?"
    #name input

    label name_ali: 
        $name_redo = False
        $playername = renpy.input("So, what do I call you?", length = 8).strip().lower().capitalize()
        #make an array of bad cases and check if the name is in the array
        if playername in badNames:
            "...%(player_name)"
            show alice meanLaugh
            #like aqua from konosuba or uminekoBeatrice
            na"Hold on a second... THAT'S your name?"
            show mc stressed
            m "No! I just stuttered..."
            na"Okay."
            show alice tsun
            na"Then what is your name then?"
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
            na"Are you sure this time?"
            show mc angry
            m "YES!"
            show alice meanLaugh
            na"Just wanted to make sure..."
        show alice smug
        na"What an cute name... I guess it suits someone like you."
        m "What's that supposed to mean?!"
        show alice meanLaugh
        na"What ever you want."
        "...'
        stop music
        
        #Mc tries to get answers from her, while she subtlely tries to get closer to him
        #show that mac is still panicing
        #she brushes off your questions, while implying you should be paying more attention to her.
        #Maybe mc tries to ask her name but she blows him off.


        m "So... Getting back on topic... I thought I was supposed to be growing a mushroom?"
        na"Well, I guess you were able to succeed in {i}something{/i} at least."
        m "So... You're a mushroom then? Not like a scary alien that's going to lay eggs in my stomach or something?"
        na"What are you talking about?"
        "I didn't think that mushrooms were supposed to talk... or... be animate..."
        na"You seem to REALLY like asking about stupid shit"
        #na"You really seem to enjoy asking meaningless questions."
        na"How about you stop thinking so hard, and we get more comfortable?"
        #na"Why don't you stop thinking about hard stuff, and relax a little bit?"
        "She lowers herself down onto the corner of the bed and leans back slightly, crossing one leg ontop of the other.'        
        "She protudes the aura of a queen sitting on a throne."
        
        #here she tries to get you to stop asking questions, and come over to her
        #instead of these lines I think it should be more like she's getting fed up with her advances not working.


        na"..."
        na"So, anyway... Should we start?"
        m "Ummm... Start...what?"
#------------------------------------------

        #i kind of picture the boxcutter scene from bakemonogatari here
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
        #maybe you lightly get away from her, regain your composture, and then only, do you have the panic response when she takes another step towards you.
        "The sound of your heart pounds violently through your ears"
        "Every fiber of your being is telling you to get away from her"
        "You know intuitively, that if she gets close to you..."
        "YOU ARE GOING TO DIE"
        
        show mc stressed
        m "...!"
        "You snap to your senses and push her by her shoulders away from you"
        m "GET THE FUCK AWAY FROM ME!!"
        "You're unable to control your emotions, as adrenaline courses through your brain"
        show alice shock
        "You look back up at the girl, whose face is frozen with shock" 
        na"..."
        "Slowly, her expression darkens, and her bottom lip begins to tremble, as she turns her face downwards"
        na"{size=-10}... you're not supposed to... i'm..."
        "..."
        #choice: apologize, yell at her (be more subtle than that)
        m "{size=+10} Sorry, I didn't mean to yell... I'm just really..."
        "You trail off after noticing that she contiues to mumble to herself."
        "She's clearly not listening"
        na"{size=-10}... i thought that you... were meant to..."
        "lose.. reason... maybe i'm just not...{size=+10} "
        m "Hey, I'm trying to apologize but I need you to listen."
        m "I was kind of freaked out that you got so close all of a sudden and-"
        na"SHUT UP!"
        "She suddenly snaps at you"
        "Her face twists with rage and pain"
        na"What's wrong with you?! Isn't this what you wanted?"
        na"ISN'T THIS WHY YOU RAISED ME?"
        m "What are you talking about I-"

        show alice sad
        "She turns away from you and dashes towards the door."
        #I don't think she would be able to operate a lock, so maybe have a reason from earlier as to why the door is already open
        "You stare blankly at her back, as she fumbles with the lock."
        "..."
        m "She's gone..."
        "Your line of sight slowly drops towards the floor as you hang your head"
        "You notice several shimmering drops of clear liquid on the wooden flooring."
        #is it even wood in the cg?


	
	#She tries once again to reinitiate
	#But this time mc is more vocal/aggresive, and it shocks her
    #choice: horrible turn down, passive let her do whatever, let her down nicely
	na"...So... You don't want me?"      
        m "?"
        na"That's not what's supposed to happen..."
        na"I'm supposed to entice anyone to abandon reason."
        na"But you..." 
        m "I'm trying to tell you I-"
        show alice shoutTears
        na"SHUT UP!"
        show mc shocked
        m "..."
        show alice crying
        na"..."
        na"{size=-8}What's wrong with me...{size=+8}"
        hide alice with easeoutbottom
        "Before you can open my mouth, she turns towards the door"
        "She swiftly turns the door knob and runs out"
        "You hear her sobbing echo through the dormitory passage, and then fade into the distance"
        #maybe you only learn her name on the rooftop?
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
        #show room, new dialogue for blahaj etc
        #click pc
        m "Okay let's see what this buisness is 'ABOUT'"
        m "WHAT THE FUCK IS THIS??? IS THIS EVEN LEGAL????"
        m "So I'm supposed to grow a companion?"
        m "Even I'm not THAT much of a loser." 
        "Who the hell is selling this kind of thing? And who is buying it?"
        m "..."
        m "So let me get this straight... "
        m "She's a mushroom companion... And her characteristics are... Unparalleled beauty and dominance?"
        #maybe change this from dominance to confidence

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
        #actually show interface here
        label dischord_chat:
            #what's mc's username
            define romBestGrill = rb
            play music computerHum
            #notification sounds? typing sounds?
            #maybe user types anything like emily is away?

            rb"sup i was wondering if you wanted to hop in vc"
            "this is one of my few online friends..."
            "Normally if you internally prepared for a few minutes, you might be able to talk for a bit"
            "But right now, you don't have the capacity for that"
            m "Sorry, kinda busy rn... can you type?"
            rb"np i was just bored and your always online so..."
            m "ouch"
            #anime crying gif from rb
            rb"are u eeping soon? little eep moder?"
            m "i just got up"
            rb"o"
            rb"your sleep finally looped back to humanity"
            rb"vampirism cured"
            m "i guess"
            rb"are you okay, you don't usually respond so short"
            m "yeah i'm fine... it's just"
            m "idk"
            rb"did something happen?"
            "you think about if you should tell him about what just transpired"
            #here show the time stamp go forward 2 minutes
            m "you probably won't believe me so..."
            rb #sends gif
            rb"don't be like that"
            m "fine"
            #attach link to website
            m "You know I told you I was growing mushrooms... Well this is where I ordered them from and ummm "
            m "It bloomed today... into a girl"
            rb"lmao nice nice"
            m "and then umm "
            m "She got all close to me and then ran off crying..."
            rb"wait, did you make this site? I didn't know you could make websites"
            rb"it looks so professional"
            rb"how many hours did it take"
            m "?"
            rb"like for a joke it's based"
            m "I can't code, and it's real."
            rb"wait like real real>"
            m "yeah"
            rb"emoji upside down smile"
            rb"lmao wtf"
            rb"let me order one real quick"
            rb"I wonder if I can get it to cosplay Rom "
        m "What? Is he not listening to me?"
            m "are you for real?"
            rb"like was she hot? I've always wanted a girlfriend that can become my waifu"
            m "I'm being serious, she's like a living being... She talks and moves and everything"
            rb"sounds like I don't need my onahole anymore"
        m "What the fuck?"
            m "I'm sorry, I think i've gotta go"
            rb"don't have too much fun"
            rb#winky emoji... maybe all of the emojis are his waifu

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
        "Even if you tried: you hoesntly think that YOU could play the role of boyfriend to someone" 
        "Nobody would even want to be seen with you"
        "..."
        m "OH FUCK!"
        "You spring out of your chair."
        m "What if someone saw her leaving my dorm?!"
        #what is he afraid of? just that he will be noticed? Why is being with a girl a negative thing?
        m "I need to find her, and make sure no one sees her" 

        "You walk over to the door and walk through it into the corridor."
        "You look towards both ends of the passage, but no one is there."
        
        #TODO:add a bit where he's feeling scared to go outside
        #the only times he goes outside is to buy a new cardboard box of instant ramen
        #salt contents are bad :c

        #Choice: Look on roof, look in cafeteria, Forget about her

        label: checkRoof
        "You turn toward the staircase leading to the roof."
        "There's a small chain barring access, but you easily step over it"
       


        #why would the player know to check on the roof?
        
        #maybe the player was told that this mushroom likes high places 

        play sound footstepsEchoingStairs
        scene rooftop afternoon
        play music wind

	
        "You walk up the narrow set of stairs and arrive onto the roof of your dormitory building."
        "From here, you can look out at the university campus that you haven't explored since your first semester of classes."
        "Ivy grows on the walls to either side of a large stairset, that climbs from the bottom of the campus, towards the ceremonial hall"
        "You remember sitting there during your initial orientation and listening to long speeches about how you as the youth of the world"
        "Are here to learn the skills necessary to make the world a better place."
        "..."
	"Sometimes you think about how when you graduate, you will feel like it was truely a waste:"
	"That you spent so much of your youth so close to such incredible architecure;"
	"And so many other people trying their best to make their dreams come true."
	"..."

    #it feels like her chacter development goes too fast, and that too much is said and not told.
    #move some of this convo to day 2, as she still needs to be toxic in day 2 as well.

	#find her on the rooftop
	"You look around and see "
	#Tears/swollen eyes, but calmer
	#She starts she conversation in a sad tone
	#as a mushroom, she doesn't have memories or a sense of personal identity
	#She does have instinct and the information in her DNA
	#In that DNA there's a clear purpose, be desireable, be pretty
	#If she isn't those things, she has no sense of meaning
	#That's why she wants for him to look at her
	#To use her
	#So that she can feel like it was worth it.
	#Not because she likes him, or wants to do the act as itself, but because she wants the validation it implies.
    
    #this makes the mc blushy and panic even more internally

 	#MC explains that humans too have biological instincts for survival
	#There's some stuff we can't ignore, like food, water, shelter love
	#But sometimes that desire causes more problems for us like obesity with candy
	#Sometimes those instincts lead for us to harm the environment, step on other people, and to be discimantory
	#As sentient things, we need to learn to overcome our 'nature' sometimes, in order for us to be happy
	#Obviously it's not that simple
	#but mc wants alice to find what makes her happy outside of her assigned purpose
	
	#She looks at the vastness of the city and feels like there's more possibility than she could have imagined
	#Maybe even she can try to find some kind of meaning in life 
	#Everything in life is meaningless, so we get to pick whats meaningful for ourselves.
	#She smiles faintly at you and feels a little better
	#it's important here that she's not in as much as a state, but that she's not completely over it: just enough to make it possible for the 2 of you to get along

	#You walk back down to the room with her
	#You decide what to call her
	
	#it's evening now
    #you ask her how she wants to spend the rest of the evening

    #i don't know what she wants to do, decide this

    #you say that you're getting a little sleepy, and she gives an offer to 'spend the night with her" again
    #you decline
    #after spending some time with her you decide to sleep









#--------------------------------


#try her telling her name here, vs earlier



#[with button route think of the silloutes and how much personality came through that... How would she be posed for that?]

#intial talk with Alice
#"will you submit to me?" 
#if yes bad end? maybe no choice at all the first time
#choice gives you either trust++ if you deal well, or neutral if not
#[from which point should the actual submission end branch off]
#from here we can begin to hint at her scent etc being mind-altering
#alice is taken aback by you not giving her attention, and runs off

#in this panic you decide to take a moment to cool off, let her calm down
# you decide to check website and see the website to understand whats going on
#you see that you have a discord notification, you reply to friend and tell himm your situation
#he's confused why you aren't taking this oppertunity

#you find her on the roof
#try to understand why she got mad
#open up a little towards her too
#go back to room together

#you suggest that you do something together?

#sleep





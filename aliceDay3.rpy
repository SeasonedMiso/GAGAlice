
# Day 3: 
# Alice has been working extremely hard and obsessively on her song for the entire night.

# MC goes out to get a new set of strings for her, but on the way back gets a call from his father. His father is a narcissist. 
# His father has loaned him a card, which he uses to give allowence for food etc, instead of giving him his own card. 
# He got a phone notification when they purchased the hoodie, and therefore was able to see that they were shopping at a women's clothing store. 
# Initially the MC thinks he's going to see through and know he bought it from himself, but the dad instead assumes his son has a girlfriend and bought it for her,
# and says things like "Of course, you probably have several of them at the same time, like I did at your age", 
# where the father is projecting his own toxic masculine attitudes on to the MC, because he thinks that is what 'normal' is.  
# He also needs to lie about academic and social performance


# Father’s Call:
# The interaction with the main character’s father is a key moment that showcases the toxic expectations placed on him. 
# The father’s assumptions and comments reveal the generational cycle of toxic masculinity, further intensifying the main character’s internal conflict.
# The call adds to the weight of the main character’s emotional burden, making the subsequent fight with Alice more impactful. 
# It could also reinforce his feelings of isolation and the pressure to conform to societal norms.

# Imported from day 2

   #start some really bad beginner guitar experimenting
   "I guess that's my obligations for the day over..."
   "Let's check if there's any new meme compilations"
   stop music
   show mc awed
   "..."
   "3 missed calls from dad"
   "You haven't talk to him in almost a month"
   show mc stressed
   "Fuck"
   "Should I text him an excuse for why I can't talk now?"
   "Or should I call him now?"

   menu:
      "What should I do?"
      "Make an excuse(N/A).":
         "..."
      "Call him back.":
         show mc stressed
         m "Hey, uh... I need to go make a phone call."
         jump day2PhoneCall


label day2PhoneCall:
   scene black with fade
   play music "wind.wav"
   "You climb up to the roof and tap the call button"
   scene rooftop with fade
   play sound "phonecall.mp3"
   "Ring..."
   "ring..."
   "...ring..."
   stop sound
   dad "Hello?"
   show mc stressed
   m "Hey dad... How's it going?"
   # I think maybe it's better that he opens with like "Hope you aren't partying too much"
   # I haven't heard about your grades but you're staying on top of it right?
   # That's the agreement, You get As, and I pay for your internet, food, utilities
   # If not, you're an adult... You're old enough to figure something out
   dad "Well I was doing pretty good"
   dad "I went down to the shop to see how the work on my car is going"
   dad "I was just talking to the mechanic about what kind of engine to import"
   dad "And then... I got a notification from the card I gave you"
   show mc worried
   m "*gulp*"
   dad "And I saw you've been doing some {i}clothes shopping{/i}"
   show mc surprised
   m "Uh... yeah"
   show mc worried
   m "So it's come to this..."
   m "I can expl-"
   dad "You finally have a girlfriend?"
   show mc confused
   m "Huh?!"
   dad "I mean that's the only thing I can think of"
   dad "You're not one of {i}those{/i} people to go buying stuff from women's stores for yourself"
   m "..."
   show mc awkwardsmile
   m "Uh, yeah, haha..."
   m"... Of course not"
   dad "So you're going to introduce me sometime right?"
   m "uhh"
   dad "I looked through all your social media looking to see if I could find her, but I didn't see anything, seeing how you never post"
   dad "You don't have any accounts I don't know about do you?"
   show mc slightsad
   m "Uh no..."
   dad "Good."
   show mc sad
   m "Is that it?"
   dad "Yeah, I'm going to get back to making my moonshine"
   dad "You remember I showed you the distillation rig I built right?"
   m "Uh yeah... Have fun!"
   dad "Will do, {i}son{/i}."
   dad "Later"
   stop music fadeout 3
   scene black with fade
   jump day2DeepTalk





# In terms of the timing its too sudden and too much emotions... Doesn't feel earned

# Maybe this entire thing should be scraped as it's not really relevant to her character arc

# Butterfly Incident:
# The butterfly scene is a powerful moment that symbolizes Alice’s internal conflict and the pain she causes unintentionally. 
# It humanizes her and shows her vulnerability, making her more relatable and tragic.
# The main character’s reassurance that she’ll always have him and the squirrels creates a bond between them, 
# showing that he’s starting to see past her toxic exterior to the person she is inside.
 

#Also the contents need to change a lot

   # scene butterfly with fade
   # #Here I think it's important to have a cg? I don't want to just write a huge monologue, but it's that or a picture
   # "You stop behind a still alice, crouching down on the grass."
   # "Her hand is outstretched but motionless, and a blue object lies on her extended index finger"
   # "A butterfly"
   # "The butterfly that moments ago fluttered about in the shallow breeze so freely"
   # "Laying peacefully still on her fingertip"
   # play sound "wind.wav"
   # "..."
   # "..."
   # "The butterfly remains motionless"
   # "..."
   # "The moment stretches on for longer that you feel comfortable"
   # "You want to say something... Anything... But you feel like there's an unspoken weight in the air"
   # "You hear alice's taut vocal cords produce a strained sound as she exhales deeply"
   # "Not quite a voice, but still communicating to you a signal"
   # "Something's not right"
   # "She exhales again"
   # "This time the flow of breath carries with it a small whimper"
   # "You step closer towards her"
   # "And look more carefully at her hand"
   # "The butterfly remains transfixed"
   # "..."
   # "It reminds you of the preserved butterflies pinned up around your university department"
   # "Beautiful, yet devoid of life"
   # "And then you realize"
   # "The butterfly is dead"
   # "You look down at her face"
   # "Two wet streams trace her cheeks down to her chin as she bites her lip"
   # "Staring at the thing that used to be a butterfly"
   # "She's the reason it died."
   # m "..."
   # "You don't know what to say"
   # "You think for a moment"
   # "'What's the matter... It's just a butterfly'... No..."
   # "'Why are you crying?'... You can't think of anything that doesn't sound insincere"
   # "..."
   # "You open your mouth in an attempt to muster up something to say"
   # ali "You know..."
   # m "?!"
   # play music "sad.wav"
   # ali "When people see a mushroom with spots like me... What do you think they think?"
   # m "Ummm... I uh... I think ummm like"
   # ali "Death... Toxicity... Poison... Hysteria"
   # ali "But you know... I'm not even that toxic"
   # ali "How many people do you think die from eating fly amanita?"
   # m "..."
   # ali "NOT A SINGLE PERSON IN THE LAST HUNDRED YEARS!"
   # ali "But still... That's what you all think of me"
   # ali "All anyone ever thinks about me"
   # ali "..."
   # ali "But you know... The worst part is..."
   # ali "Their fears aren't unwarranted"
   # ali "I kill the things around me"
   # ali "You know, they used to crush us up and mix us into milk to kill flies wanting to drink it"
   # ali "That's where the 'Fly' part of the name comes from "
   # ali "Isn't that weird if you think about it for a second?"
   # ali "If we are so scary, why would you mix it into the milk you drink?"
   # ali "I don't get it..."
   # ali "I don't understand anything"
   # ali "But I don't want to be something that causes suffering and death to everything around me"
   # ali "But that's how you all see me"
   # ali "By default"
   # ali "And there's nothing I can say that will change the way you all see me"
   # ali "I don't want to be like this!!!"
   # "Alice's voice slowly turns from words into incoherrent sobs"
   # m "..."
   # m "You know... ummm "
   # m "I'm not going to pretend I know everything about you..."
   # m "Or that I can talk for all human's or whatever"
   # m "But... I think I read a study about like... Japanese squirrels? I think?"
   # m "That were able to eat you guys. No problem..."
   # m "And so... I guess I was just thinking like"
   # m "Maybe it's not so black and white? That sure, maybe some people get the wrong idea, and think you're more of a threat than you really are"
   # m "But at least me... I think you're not that scary."
   # m "When we first met, I think maybe I was like what you said"
   # m "You did kind of freak me out"
   # m "But I sort of wasn't expecting the whole... You know? Living mushroom thing?"
   # m "And everything else"
   # m "So I'm sorry about that"
   # m "But right now... I think you're just like any other girl"
   # m "And I know maybe my opinion doesn't mean that much"
   # m "But I guess I wanted to say if you're feeling isolated"
   # m "I just wanted you to to know that..."
   # m "You have me... and..."
   # m " The squirrels I guess"
   # ali "..."
   # show butterfly_smile
   # #show alice smile cry
   # ali "That's so... stupid!"
   # m "I'm sorry..."
   # ali "And like... how would you know what a normal girl is like anyway"
   # m "I-"
   # ali "Hahahaha"
   # m "?"
   # ali "..."
   # ali "I'm sorry"
   # ali "I guess I got a little melodramatic"
   # m "It's okay"
   # scene black with fade
   # "She gets up and you keep starting walking again slowly"
   # "The sun has almost completely set"
   # jump day2WayHome


#I'm worried that it's weird that there's 2 big emotional freak outs in one day... It's important that each one resolves a different feeling



# After the conversation the MC feels depressive, and the weight of his parents expectations of him. 
# When he gets home he is in a bad mood, which leads to him bottling it up while alice is practicing loudly.
# Alice is also acting incredibly stressed, and is being incredibly perfectionist, playing the same lines over and over again until they are perfect, 
# and being incredibly short and snappy with the main character, because she wants to win and be perfect. She can't 'afford the time to talk to him"
# He eventually snaps and yells at her which leads to her fighting with him. He reveals that he is really jealous of her, 
# and that it intimidates him that she's now better with one day of practice than he has ever been at anything in his life. 
# That he feels conflicted because he wants to help her but feels like she's also being self centered, and is focusing too much on perfection. 
# That she's gone from trying to get external validation from one source, just to change it for another. 

# The fight is supposed to be the main emotional climax of the route.
# Ideally they make up and both end up with a healthier outlook as a result of the fight. 
# He realizes that he's just making excuses and that he's just jealous that she's doing what he's always want to, and she realizes that it's okay to not be perfect, 
# and just to let what happens happen. She plays at the event but makes a couple mistakes, and ends up not winning, 
# In fact, maybe she even drops her pick, or embaressing herself and needing to start over or something. But she goes throurgh it with a smile, 
# because she just wants to know that she did something meaningful. 


# Maybe the lyrics of the song reflect how she feels about the main character which adds more catharsis to the fight that they had earlier, 
# where although she looked like she cared more about the song than spending time with him in her last day, 
# it's because she wanted to properly communicate how she felt towards him. The main character and her go home, for him to slit her throat, 
# and properly prepare her to eat without toxins, knowing that she has no regrets, and that the MC now has a new outlook on life,
# and is going to try to become the version of himself he wants to be, free from what anyone else thinks of him




# Alice’s Obsession:
# Alice’s obsessive behavior and perfectionism reflect her desperation to achieve something meaningful before her time runs out.
# Her snapping at the main character shows the strain she’s under, and her focus on perfection echoes her previous need for external validation.
# This scene also highlights the difference in how they cope with stress—Alice by throwing herself into her work, and the main character by bottling up his emotions.

label day2DeepTalk:
   "You go back downstairs to your room."

   play music "night.mp3"
   
   
   show bottle night with Dissolve(2):
      zoom 0.9
   
   show alice serious at left
   with dissolve 
   play sound "door.wav"
   
   "Alice is sitting there and has already figure out some basic chord progression kind of stuff"
   show mc normal at right with easeinbottom
   m "..."
   ali "*focused silence*"
   show mc normalside
   m "Looks like you're having fun"
   ali "Yeah... I feel like I'm starting to get the hang of this"
   show mc slightsad
   m "That must be nice."
   show alice annoyed
   ali "Hey, are you angry or something? Did I do something?"
   show mc stressed
   m "No... It's whatever, just go back to your noodling."
   show alice normal
   ali "If that's what you want then fine..."
   "she plays but it gets more aggresive and she pauses every once in a while."
   "..."
   show mc vstressed
   "she keeps playing and you just sit there..."
   "It boils up..."
   "Until you just can't take it anymore."



#    The Fight:
# The fight serves as the emotional heart of the route, where both characters lay bare their insecurities. 
# The main character’s jealousy and frustration are understandable, and his outburst is a natural progression of the pressure he’s been under.
# Alice’s reaction could reveal her own fears of inadequacy, despite her apparent confidence. 
# The fight forces both characters to confront their flaws and the ways they’ve been avoiding their deeper issues.
# The reconciliation should feel earned, with both characters acknowledging their mistakes and growing from the experience. 
# This could be a moment where they find common ground in their struggles, leading to mutual understanding and support.


# 1. Miscommunication and Resentment:
# Alice's Frustration: 
#   Alice is laser-focused on perfecting her song, seeing it as her only chance to prove her worth. She’s been practicing obsessively, 
#   tuning out the main character and snapping at him whenever he tries to talk.

# MC’s Resentment: 
#   The main character has been bottling up his own feelings, feeling neglected and overshadowed by Alice’s sudden talent. He feels inadequate, 
#   as if her rapid progress is a slap in the face to his own struggles with creativity.

# The Trigger: 
#   The main character might try to offer some advice or suggest she take a break, only for Alice to dismiss him curtly. 
#   This dismissiveness could be the straw that breaks the camel's back, leading to an outburst where he accuses her of being self-centered and of seeking validation just like before,
#   only now through music.

# 2. Jealousy and Self-Worth:
# MC’s Envy: 
#   The main character could explode in anger, confessing that he’s jealous of how quickly she’s excelled at something he’s always wanted to do.
#   He feels like a failure in comparison, and Alice’s focus on perfection makes him feel even worse.

# Alice’s Counterattack: 
#   Alice, feeling attacked, might lash out by accusing him of not understanding how much pressure she’s under. She might say something like,
#   “At least I’m doing something! You’re too scared to even try.”

# The Climax: 
#   This could escalate to a moment where the main character questions why Alice even cares about this competition. 
#   He might accuse her of just replacing one form of validation with another, hitting her deepest insecurity.

# 3. Revealing Deep Fears:
#   Alice’s Fear: 
#     During the fight, Alice could reveal that she’s terrified of dying without having done anything meaningful. 
#     She might admit that the reason she’s pushing so hard is that she’s scared of being forgotten, of being just another product.
    
#   MC’s Confession:
#     In turn, the main character could confess that he’s scared of never amounting to anything, of being a disappointment to his parents and to himself.
#     He might admit that he envies Alice because she’s living the kind of bold, fearless life he’s always wanted, even if it’s only for a few days.
    
#   Resolution: 
#     This mutual confession could lead to a moment of understanding where they both realize they’re projecting their fears onto each other. 
#     The fight could end with them both calming down, realizing that they’re not so different after all.

# 4. The Breaking Point:
# Alice’s Perfectionism:
#   Alice’s obsession with perfection could be driving her to the point of exhaustion. The main character could try to intervene,
#   telling her that it’s okay to make mistakes, only for Alice to snap back that she doesn’t have time for mistakes.

# MC’s Breaking Point: 
#   The main character, feeling like he’s losing her to this obsession, could finally break and yell that she’s going to burn herself out, 
#   just like he did with his own dreams. He might accuse her of throwing away the time they have left together for something that doesn’t even matter.

# Alice’s Realization: 
#   This could lead to a moment where Alice realizes that in her pursuit of perfection, she’s been neglecting the one person who has shown her genuine care.
#   This realization could be the turning point that helps her see that she doesn’t need to be perfect to be loved.

# 5. A Fight for Each Other:
#   MC’s Fear of Losing Her: 
#     The main character, driven by the fear of losing Alice, could lash out, telling her that she’s wasting the little time they have left on 
#     something that won’t change anything. He might confess that he’s terrified of her dying without them really connecting.

#   Alice’s Retort: 
#     Alice, feeling cornered, might fire back that she doesn’t want to just be “another pretty thing” to him, that she needs to do something that’s hers,
#     something that matters, even if it’s just for a moment.
 
#   Emotional Release: 
#     The fight could escalate until they’re both shouting, only to end with them collapsing into each other, realizing that they’re both scared, 
#     both trying to find something meaningful in a world that feels overwhelming and unfair. 
#     This could be the moment they both realize they’ve been fighting for each other all along,
#     and that their connection is what truly matters.




   show mc vshout
   m "Are you going to keep playing all night? How am I supposed to relax like this?"
   show alice angry
   ali "Huh? What's up with you? I've literally done nothing and you're being super passive aggressive for no reason."
   show mc shout
   m "It's not for no reason! I go through all the effort to set up all this stuff for you, and you..."
   show alice serious
   ali "And I what?"
   ali "Have fun and use it?"
   show alice annoyed
   ali "Sorry for existing I guess."


   #choice as to whether to fully give into it or whether to take a step back
   #[I think all of the decisions need to be subtle, not GOOD CHOICE or BAD CHOICE]
   #She's on the verge of tears, and you take a step back

   #choice 1 "I'm jealous of you"
   #choice 2 "You're so selfish"
   show mc vannoyed
   
   m "You don't get it..."
   m "You just start learning guitar on a whim."
   show mc sulk
   m "And you're already better than I've ever been at anything."
   m "In literally the span of hours."
   show mc stressed
   m "What the fuck am I supposed to do?"
   m "I'm not good enough for my parents."
   m "And I'm not good enough for myself."
   show mc slightsad
   m "I'm a fucking loser, and yet I tell my self I'll learn to draw."
   m "Or learn an instrument."
   show mc shout
   m "Or fucking anything."
   show mc sad
   m "I just want to like myself."

   m "But even then..."
   m "I know it will never be enough"
   show mc slightsad
   m "I'm never going to be enough for my parents"
   m "Because all they want me to be is the person they THINK I am"
   show mc vannoyed
   m "But I CAN'T be that person!!"
   m "I've never been that person..."
   show alice neutral
   ali "..."
   show mc normalside
   m "They think I'm a straight A student, with lots of friends."
   m "My dad is making up fantasies of me having a girlfriend and living up to how he was in college"

   m "I don't even know what he would do if he found out"
   show mc cynical
   m "Who I {i}actually{/i} am"
   show mc stressed
   m "That I'm on the verge of flunking out"
   m "That I have no friends"
   m "That I'm not like him..."

   # nuance of disgust
   show mc sulk
   m "I just feel like..."
   m "Time keeps moving..."
   m "And I'm still alone... Here... In my room."
   m "But I can't stay in college for ever."
   m "I'm going to drop out or scrape through."
   m "And then I'm going to work doing some crappy deskjob I hate, until I get old..."
   m "And then I die."

   ali "..."
   show alice sulk
   ali "You know.. It's kind of funny"
   show mc normal
   m "?"
   ali "How when it was me wanting attention"
   ali "You could rationalize all the reasons why I was being stupid for wanting that"
   ali "But you..."
   show alice normal
   ali "You're the exact same."
   show alice disgusted
   ali "Get over yourself."
   ali "You're drowning in your own tears about only having another 60 years left to accomplish something."
   show alice sulk
   ali "How do you think I feel?"
   ali "I have one more day"
   ali "..."
   show mc sad
   m "I'm sorry..."
   show alice normalside
   ali "It's okay..."
   ali "I haven't spent that much time with you."
   ali "Or you know, being alive."
   show alice serious
   ali "But I think maybe, you're waiting for an excuse."
   show mc confused
   m "What do you mean?"
   
   ali "You took me to a whole bunch of places and showed me a bunch of stuff."
   show alice confused
   ali "and at first I thought it was meaningless."
   show alice normal
   ali "But I realized that nothing matters except what is important to you."
   
   ali "Latte art is just making pictures in cow boob juice."
   ali "And video games are just what depressed people do to avoid dealing with real life."
   # Too much
   ali "But even then."
   show alice serious
   ali "Those are things that bring meaning to people."
   ali "Every single thing you could be interested in."
   ali "has so much depth when you actually look into it."
   ali "Every rabbit hole runs so deep."
   show alice normalside
   ali "And I guess what I'm trying to say is"
   show alice sad
   ali "You can't wait for someone else to give you permission to act" 
   ali "To do what you want with your life"
   show mc worried
   m "But what if it doesn't work out?"
   show alice sigh
   ali "Well then you're back where you started."
   ali "And you can find another reason to live"
   ali "Humans are good at that"
   show alice happy
   ali "So I guess in the meantime, all you can do is find a waste of time that feels special to you"
   #maybe try to fit in a bit about like: I'm just scared even if I sacrifice everything, that ill still feel as broken and fucked up as i did before
   # I'm worried this reads as preechy and goes against do don't say


#    Post-Fight Reflection:
# After the fight, a quiet moment of reflection for both characters could serve as a turning point, where they each realize the impact they’ve had on one another. 
# This could lead to a deeper emotional connection before Alice’s final performance.

# Resolution Ideas:
 
#   A Quiet Apology: After the fight, they might sit in silence, both emotionally drained, before one of them quietly apologizes. 
# This could lead to a tender moment where they both acknowledge their fears and insecurities.
#   A Song for Him: Alice might reveal that the song she’s been working on is actually about the main character, a way to express her feelings for him. 
# This could add an extra layer of emotion to her performance the next day.
#   Letting Go: The fight could end with them both realizing that it’s okay to let go of perfection, to accept that their time together doesn’t have to be perfect to be meaningful. 
# This could set the stage for Alice’s final performance, where she embraces imperfection and the beauty of the moment.

   show mc awed
   m "..."
   m "...Thanks..."
   show alice sly smile
   ali "Don't mention it"
   show mc normalside
   m "I guess... I think you're right..."
   show mc stressed
   m "I don't really know what I'm going to do yet but... I think I'm going to stop thinking about everything I want to do."
   m "Everything I want to be."
   show mc sad
   m "And just pick something and see where it takes me."
   show alice happy
   ali "Well as long as you're having fun, right?"
   show mc normal
   m "... I think I'm kind tired after going out today"
   m "Kind of a bit past my threshold for humans interaction"
   show alice normal
   ali "You going to go to bed?"
   
   m "Yeah I think so..."
   show mc awed
   m "Do you mind switching to headphones?"
   ali "Sure"

   scene black with fade  
   window hide
   stop music fadeout(3)
   show chibi_sleep at truecenter with dissolve
   show top_text "You crawl into bed and fall asleep to the dull sound of unamplified guitar sounds" with dissolve 
   pause 3


   play sound "yay.wav"
   "END!!!"


/////////////

Alice’s Performance:
Alice’s performance is a culmination of her journey. The mistakes she makes, and how she handles them, symbolize her acceptance of imperfection and her growth as a character.
The song’s lyrics could be a powerful way for Alice to express her feelings towards the main character, showing that her focus on the song was,
in fact, a way to connect with him on a deeper level.
Her decision to smile through the performance, despite the errors, underscores the theme of finding meaning in the process rather than the outcome. 
This could resonate with the main character, helping him see the value in his own efforts, regardless of external validation.

Final Scene:
The final scene, where the main character prepares Alice for consumption, is both poignant and symbolic. It’s a moment of acceptance and closure,
as both characters come to terms with their respective journeys.
The act of consuming Alice could be seen as the main character internalizing the lessons she’s taught him, 
carrying her memory and the meaning of their time together forward in his life.
This ending reinforces the themes of mortality, self-acceptance, and breaking free from societal expectations. 
The main character’s newfound resolve to live authentically could be a bittersweet yet hopeful conclusion to the route.

////



label:day3Morning
#wake up
#she's been playing guitar the whole night on a guitar with old strings (missing a string). You feel sorry for her, but impressed at her drive.

#have an internal dialogue of how you are jealous, but at the same time, you've never even tried that hard, so maybe you don't even have the kenri to feel that way

#you decide to take her to a guitar store to buy new strings
#[here i think the bg music when she's practicing should be the song she's writing, but at various levels of playing: think wa2]
label:day3GuitarStore
#she's wowed by just how many types of guitars there are
#she find's a more pro-ish gutiar that she thinks really suits you (or that she really wants)
#maybe have a scene where you talk to the worker there (maybe he's a friend of the neighbour,  and the neighbour reccomended this place)
#you buy new strings and go back home
label:day3WayHome
#you end up becoming a little depressed and standoffish, but this time she asks you whats wrong
#you explain that you had always wanted to be creative but never had a spark, maybe waiting from a push from someone else

#you try apologize for how you acted yesterday
#choice as to whether to fully give into it or whether to take a step back
#She's on the verge of tears, and you take a step back

#jealous of how in a matter of hours, she got better than you were able to get (half-assedly), and so it makes you feel even more useless. 
#maybe i'm only trying to nurture your creativeness because I wish someone had done the same for me

#she gets upset: I only have a few days to live, yet you have years. I just want to try to find some sort of meaning while i'm here
#[i think try to maybe build that part of her character: in contrast to buttons attitude towards death, hers is more like: I want to be immortalized through creation]

#maybe this should go into day 2

#alice kind of represents the ego, with validation being a huge part of her character, and this results in her attitude towards death
#put this in earlier days too

label:day3Restring
#you tune up the guitar strings for her and are suprised by just how good she sounds
#she explains as a mushroom she has connection with ancient wisdom, and so for her it was very intuitive, 
#and she was able to learn super fast
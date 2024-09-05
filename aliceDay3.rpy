
# Day 3: 
# Alice has been working extremely hard and obsessively on her song for the entire night.

# MC goes out to get a new set of strings for her, but on the way back gets a call from his father. His father is a narcissist. 
   
   #Wake up to alice with bloodshot eyes, shes been grinding all night
   #You call out to her but she ignores you at first
   #You pull off her headphones off her
   #She says gm but needs to keep grinding
   #choice: Insist she takes a break to come with


label day3Morning:
"You wake up to the rhythm of dull strumming."
m "Damn you're still going?"
ali "..."
m "Hello? Good morning~"
ali "..."
"She seems to be completely ingulfed in the guitar world."
"She can't hear you."
"You slowly get out of bed and walk towards the kettle to make some coffee."
"While the kettle boils you look over to her and watch her play."
"You can't hear her that well from the growling of the water being heated."
"Her movements look a lot more confident that you remember last night"
"But when you look at her face you see her eyes are bloodshot."
"You walk over to her and tap her shoulder gently."
m "..."
"No response"
"You bring your hand up to the top of her head and begin to lift the headphones upwards."
ali "EEK! Wha-"
m "Good morning!"
ali "Jeez, don't scare me like that"
m "Haha, sorry about that."
m "Looks like you've been going the whole night?"
ali "Yeah but I'm behind on time."
ali "There's no way I'm going to win at this rate."
#Maybe it would be funny if she forgets she hasn't practiced singing, so and the concert she doesn't realize and that's what her big failure is
m "Take it easy, you still have lots of time."
m "And besides, it's not about the outcome, it's about the experience."
ali "Yeah, right, sure."
"She turns back to the paper she's been taking notes on and resumes her practice."
"You look at the notes, but it looks like no music notation you've ever seen before."
m "Hey, how did you learn how to read music?"
ali "What do you mean?"
m "Like your notes, they must be some kind of thing you learned right?"
ali "Nah, I just drew stuff to help me remember what part of the song go where."
"You look closer at the page and it's full of abstract interconnecting shapes."
m "Uhh, I have no idea what i'm looking at."
ali "That's okay, just as long as I know."
"You hear the kettle click and walk over to it."
screen trans 
# maybe slurping sound
m "Okay I'm alive now"
ali "*strum* *strum*"
m "Are you ready to go to the guitar store?"
ali '*pickedy* *pick*'
"She can't hear you again"
"You walk over to her and slowly wade your hand in front of her vision"
ali "Whaaat~"
m "Do you wanna go get strings or not?"
ali "Ughhh, do I have to?"
m "If you can do with out them then I guess not."
ali "..."
ali "Can't you just go for me? I'm running out of time and I still have so much to do"
m "I think you should take a break, you've been grinding for like 12 hours straight"
ali "Nooooo~"
ali "I don't have time to go!"
m ("Damn what should I do?")
choice:let her keep grinding, 
   -Take her along with you


#wake up
#she's been playing guitar the whole night on a guitar with old strings (missing a string). You feel sorry for her, but impressed at her drive.

#have an internal dialogue of how you are jealous, but at the same time, you've never even tried that hard, so maybe you don't even have the kenri to feel that way

#you decide to take her to a guitar store to buy new strings
#[here i think the bg music when she's practicing should be the song she's writing, but at various levels of playing: think wa2]





label day3Store:



   #Go to store
   #Look at the instrument store 
   #she looks at an one and cant take her eye off
   #you could maybe afford it if you used most of your money 
   #but shes going to die tonight (could buy and return but scam?)
   #you leave the store and on the way back (by the river bed) and your dad calls 
  
#   The music store scene is a little empty. The part with the expensive guitar that she likes works, but it needs more. 
#   One idea is that perhaps she sees someone else playing guitar and is hit by a wave of insecurity, watching how good and easily this guy is just playing around,
#   and her fear of the concert + being compared to other performers, and self-doubt increases. Maybe all she tells mc is that she's feeling nervous for tonight.
#   He could respond with empathy (from his experiences of stage fright and social anxiety) and that he'll be there cheering her on = makes her smile and they 
#   have a cute little bonding moment.
  
  






---------------------------------------------------






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



   #You tell her to go on ahead
   #She sits down and looks at flowers and the butterflies
   


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





#You arrive back and she goes back to songing
   # It's fine for the first few hours, but now it's evening and she's been dismissive towards you
   #You try offer to help but shes stubbornly grinding
   #Eventually you snap and get angry, its her last day
   # You tell her like "I'm trying to be supportive! Don't you get how hard this is for me? You've accomplished more than I ever have and you're only few hours deep! 
   #This is the last time we have together and you're just wasting it" all that stuff


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


#   For "The snapping point", I think his self-doubt about how quickly she's improved at guitar could be better portrayed:
#   instead of saying it all from the POV of why this is hard for him (which is too obviously self-focused + annoys me), 
#   he can phrase it as a frustrated encouragment, trying to get her to see why everything is okay and she can stop stressing and be proud of all she has done instead.
#   For example, "Why are you so upset/stressed/afraid? Stop putting yourself down - don't you know how much I look up to you? You've worked so hard, you've learned so much,
#   and what I can sounds better than anything I could do. You've accomplished more than I ever have!" 
#   This way MC's self-hate is more backhanded AND it shows how their relationship has grown to the point that
#   he is genuinely worried about her and wants her to see how HE sees her.




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
   ...#maybe try to fit in a bit about like: I'm just scared even if I sacrifice everything, that ill still feel as broken and fucked up as i did before
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




  
   #she gets upset and walks out with the guitar to work alone
   #You take some time to calm down, and go find her
   #Shes on the roof, and shes not playing guitar, instead shes holding a dead butterfly
   #She's crying 
   # opens up to you now because she trusts you
   #You listen. She talks about how the butterfly reminds her of herself
   #And now shes very aware that shes just wanting validation in a different way
   #Self doubt sets in
   #She's scared that shes wasted the small bit of time she has with you
   #But she just wanted to accomplish something
   #This is the only chance she has to fee like her life was able to accomplish something
   #MC defuses it by pointing out that the validation doesnt need to be what she focuses on,
   #She picked this because she saw something in it that resonated with her, and as long as she had fun, that's all that matters
   #hes there to help
   #He helps her refine the song with what ever feedback he can give
   #They go to the event
   #Kellin is there and is afraid to see alice at first, but eventually he chills out around her
   #Her time comes to play 
   #She goes up and (trips, or drops pick, or mic howls really bad, or guitar jack cuts out)
   #She smiles and make a joke of it into the mic, and the audience laughs with her
   #The lyrics are using butterfly metaphor and about how she feels about life, and the mc
   #She doesn't win the competion
   # Kellin comes up to her and he shows her respect and asks her about the song
   Post-concert, for some bittersweetness and dramatic irony, Kellin could go over the top about how well Alice did, and how much potential she has if she keeps on going + he wants to make future plans with her and begs her to join his band. Alice and MC know she can't, but how they navigate that convo could be interesting, and can help lead to the somber tone of the "one last conversation" on the way home. 
   # You and her go home together and have one last conversation on the way home
   # She tells you there might be a way to cook her without dying
   # It ends with you thinking about what you want to do with your life, about how maybe you'll go and get that guitar, or take kellin up on playing in a band with him
   # But no matter what happens, you're going to start from trying to like yourself first

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



#[here i think the bg music when she's practicing should be the song she's writing, but at various levels of playing: think wa2]
label day3Morning:


   scene black with dissolve
   scene bottle day:
      zoom 0.9
   with Dissolve(2)
   show day_3 at topleft
   show alice_affection at topright
   with dissolve
   window show
   "You wake up to the rhythm of dull strumming."
   show mc surprised
   show hoodie
   with easeinbottom
   m "Damn, you're still going?"
   ali "..."
   show mc confused
   m "Hello? Good morning?"
   "..."
   "She can't hear you. She seems to be completely engulfed in the guitar world."
   "Slowly, you get out of bed and walk towards the kettle to make some coffee."
   show mc normalside
   "While the water boils, you scrutinise her playing."
   "You can't much over the rumbling of hot water, but her movements look significantly more confident than last night."
   "However, when you scan her face, you notice how  bloodshot her eyes are."
   "You step towards her and tap her shoulder gently."
   show mc at right
   show hoodie at right
   with move
   show mc awed
   m "Hey."
   "No response."
   show mc normal
   "You bring your hand up to the top of her head and lift up the headphones."
   show alice_base_longhair at left
   show alice shocked at left
   show dress true at left
   with dissolve
   ali "EEK! Wha-"
   show mc happy
   m "Good morning!"
   show alice pout
   ali "Jeez, don't scare me like that."
   show mc annoyed
   m "Haha, sorry about that."
   show mc normal
   m "Looks like you've been going the whole night?"
   show alice sad
   ali "But I'm still behind on time."
   ali "There's no way I'm going to win at this rate."
   show mc awed
   m "Take it easy. You still have lots of time. The show's only at night."
   show mc cute
   m "And besides, it's not about the outcome. It's about the experience."
   show alice sulk
   ali "Yeah. Right. Sure."
   show mc normal
   hide alice
   hide dress
   hide alice_base_longhair
   with dissolve
   "She turns back to the paper she's been taking notes on and resumes her practice."
   show mc awed
   "You look at the notes. They're completely unrecognisable. Nothing like the standard music notation you've seen."
   show mc confused
   m "Hey, how did you learn how to read music?"
   show alice_base_longhair at left
   show alice neutral at left
   show dress true at left
   with dissolve
   ali "What do you mean?"
   m "Like your notes... They must be some kind of thing you learned right?"
   show alice normalside
   ali "Nah, I just drew stuff to help me remember what part of the song go where."
   show mc normalsquint
   "You look closer at the page full of abstract, interconnecting shapes."
   m "Uhh, I have no idea what i'm looking at."
   ali "That's okay, just as long as I know."
   "You think for a moment, but the more you do, the more confused you become"
   m "I'm so confused... Like I had my doubts when you started talking about doing music in the first place"
   m "But how on earth are you like... Doing any of this?"
   ali "I... Don't really know..."
   ali "It's kind of like how I knew about some stuff when I was born..."
   ali "But kind of different?"
   ali "That stuff was all facts and details."
   ali "This all feels a lot more nebulous and abstract..."
   ali "Like something that wasn't programmed in me, but more like, something I just..."
   m "...I see..."
   m "I guess if I had to make a guess based on what I know about mushrooms, then maybe some psychedellic higher wisdom stuff is involved""
   ali "Yeah, maybe!"
   "She quickly turns back and starts practicing again."
   "She doesn't seem anywhere near as interested in contemplating this as you are"
   hide alice with dissolve
   show mc normal
   "You hear the kettle click and walk over to it."
   "You can't help but be impressed by her."
   show mc slightsad
   "But you also feel a bit..."
   window hide
   show black with dissolve
   play sound "sip.wav"
   pause 3
   show mc happy
   hide black with dissolve
   
   window show
   m "Okay, I'm alive now."
   ali "*strum* *strum*"
   show mc normal
   m "Ready to go to the guitar store?"
   ali '*pickedy* *pick*'
   show mc normalside
   "She can't hear you again."
   "You walk over to her and slowly wave your hand in front of her vision."
   show alice_base_longhair at left
   show dress true at left
   show alice mendokusai at left
   with dissolve
   ali "Whaaat~"
   show mc confused
   m "Do you wanna go get strings or not?"
   show alice sulk
   ali "Ughhh, do I have to?"
   show mc normalside
   m "If you can do with out them then I guess not."
   ali "..."
   show alice sad
   ali "Can't you just go for me? I'm running out of time and I still have so much to do."
   show mc slightsad
   m "A-alone? I... guess I could try, but..."
   m "(But Alice looks stressed. Should she really keep pushing herself so hard?)"
   show mc stressed
   m "(Is she really going to make her entire last day about a competition she won't even win?)"
   m "(It doesn't feel right.)"
   show mc confused
   m "I think you should take a break. You've been grinding for like 12 hours straight."
   show alice vannoyed
   ali "I don't have time to go with you!"
   menu:
      "Should you just leave her alone? It's hard to ignore the uneasy feeling in the pit of your stomach."
      "Let her grind (N/A).":
         "Skye must still write this part."
         return
      "Make her take a break.":
         show mc slightsad
         m "I'm worried about you. You've been working non-stop for the entire night."
         show mc sad
         m "And taking a break helps you work even better. So, please, come with me."
         show alice sad
         a "But... I don't have time!"
         show mc cute
         m "You do! It won't take long, and it'll clear your head. Trust me. It's the best choice."
         show alice sulk
         ali "Fine then! Let's just get it over with." #Orginal seemed too bratty instead of her being genuinely worried/stressed.
         window hide
         hide mc
         hide hoodie
         hide alice
         hide alice_base_longhair
         hide dress
         with easeoutbottom
         scene black with Fade(0.5, 1.0, 0.5)
         play sound "door.wav"
         play music "mall.mp3" fadein 2
         show chibi_mc at slightright
         show chibi_alice at slightleft
         with easeinright
         window show
         #What do they talk about on the way?
         "Alice trailing behind you, you walk to the music store."
         "She's silent. Every now and then you glance over your shoulder, worried that she got lost somewhere along the way."
         "But she's always right behind you."
         "Walking lazily, yet somewhat annoyed."
         window hide
         hide chibi_mc
         hide chibi_alice
         with easeoutleft
         jump day3Store

label day3Store:
   #play sound shop bells
   scene music_store with Dissolve(2)
   show alice_base_longhair at left
   show dress true at left
   show alice shocked at left
   show mc normal at right
   show hoodie at right
   window show
   ali "!"
   show alice excited
   ali "Woah, this place is crazy!"
   show mc happy
   m "Yeah... There's all sorts of stuff."
   #Maybe drag this out and make it more like "why does that one have a birth defect?"
   show alice confused
   ali "Why is there like... a conjoined twin guitar?"
   show mc annoyed
   m "I have no idea."
   show mc happy
   m "I'm going to go get the strings. You can have a look around in the meanwhile."
   m "(And hopefully being surrounded by all these guitars will cheer you up.)"
   #Maybe it's better that she points it out only afterwards?
   show alice surprised
   ali "You're going to talk to a stranger? All by yourself?"
   show mc vshocked
   m "..."
   show mc worried
   m "(Damn, I didn't think that far! But then again, I managed to talk to Kellin by myself.)"
   show mc stressed
   m "(And I don't want to bother Alice. She needs to relax right now.)"
   show mc awkwardsmile
   m "I'll be fine. Probably..."
   show alice sly smile
   ali "If you say so."
   window hide

   hide mc normal
   hide hoodie
   with dissolve

   show black with dissolve
   pause 0.5
   play sound "cash_register.mp3"
   pause 0.5
   show alice normalside
   hide black with dissolve
   show mc vstressed at right
   show hoodie at right
   with dissolve
   window show
   m "Ugh... That went a-about as expected."
   show alice smirk
   ali "So you pissed yourself and the staff had to clean it up in front of you?"
   show mc annoyed
   "You hold up the string packet triumphantly."
   m "There, I did it! See! I c-can do it if I try!"
   show alice sigh
   ali "Your voice is still trembling though..."
   show mc normalside
   m "Since we're here we might as well have a proper look around."
   show alice normal
   show mc happy
   m "Did you know you can try out guitars with an amp on the second floor?"
   show alice normalside
   ali "It's fine, I should go home and practice anyway."
   show mc confused
   m "We came out all this way. You may as well try some different ones and see if there are any you like."
   show mc cute
   m "And you can play what you've been working on here."
   show alice confused
   ali "That is a good point..."
   hide alice_base_longhair
   hide dress true
   hide alice shocked
   hide mc normal
   hide hoodie
   with dissolve
   "Alice tries out a few guitars while you watch."
   #maybe you take the phone call here and she's still on the guitar when you get back
   "Although she plays on multiple different ones, it's never for more than a few seconds, before she unplugs it and puts it back on the hanger."
   "Until..."
   show alice_base_longhair
   show alice surprised
   show dress true
   with dissolve
   ali "This one is different."
   m "Really? Isn't it exactly the same as that other one you were just playing? Just a different colour?"
   show alice pout
   ali "But it feels completely different!"
   m "If you say so..."
   hide alice
   hide alice_base_longhair
   hide dress
   with dissolve
   "After a few minutes pass, she eventually unplugs it and tries a couple others."
   "However it's obvious that none of them interest her as much."
   show mc normal
   show hoodie
   with dissolve
   "You glance at the price of the one she was eyeballing."
   "\"Fender Custom Shop 2022 Fall Event LTD 1960 Telecaster Journeyman Relic Aged Magenta Sparkle\"."
   "And the price is..."
   show mc vshocked at bounce
   show hoodie at bounce
   m "..."
   "If you bought it, you would be eating instant noodles every day for the next 2 months."
   "Which isn't any different than how you live anyway."
   show mc stressed
   "But, she's only has today left."
   m "(Maybe I could return it tomorrow and get a refund.)"
   show mc sad
   m "Alice, we should probably get going"
   show mc at right with move

   show alice sad at left with easeinbottom
   ali "...Okay..."
   "She takes a last look at that guitar, and slowly gets up."
   "As she does a young boy with 2 older adults (probably his parents) takes a seat at the amp on the other side of the floor"
   "He plugs in the guitar his parents place on his lap for him to try and..."
   stop sound
   play sound "guitar_shred.wav"
   show mc surprised
   show alice shocked
   ali "!"
   m "Damn. Kids these days are crazy huh?"
   show alice cutesad
   ali "..."
   #"You see her scrunch up her brow and turn her gaze towards the floor" #Too much description when her sprite will show it.
   show mc normal
   m "Let's go. You've got a lot of work to do right?"
   ali "Yeah..."
   window hide
   stop music fadeout 2
   scene black with Dissolve(1)
   play sound "<from 0 to 1>shop_bell.wav"
   pause 1
   scene enbankment with Dissolve(1)
   show alice_base_longhair at left
   show dress true at left
   show alice sad at left
   show mc normal at right
   show hoodie at right
   with easeinbottom
   window show
   "It happens while you're walking along the river with Alice by your side."
   "You're heading back to your dorms, when suddenly-"
   stop sound
   play music "ringtone.ogg"
   show alice shocked at bounce
   show dress at bounce
   show alice_base_longhair at bounce
   show mc shocked at bounce
   show hoodie at bounce
   m "{sc=5}{color=#000000}{size=+80}Oh shit!"
   "You're not used to the sound of your own ringtone? That says it all."
   show alice confused
   a "What's that?"
   show mc surprised
   show alice normal
   m "Dad?"
   show mc stressed
   m "Ugh... Why now? I'm not in the mood."
   show mc normalside
   # make it more clear why he doesn't want to pickup
   default declineDad = False
   menu:
      
      m "I could just message him some excuse, or..."
      "Tell him you'll call tomorrow.":
         $ declineDad = True
         show mc normal
         stop music
         "You decline his call, then quickly send a message to your father:"
         "\"Hi Dad. Sorry, I'm out at the moment. Can I please call you tomorrow?\""
         show mc awkwardsmile
         m "It's sorted. We can continue now."
         show alice sly smile
         a "So that was your father?"
         show mc slightsad
         m "Mm."
         show alice normal
         a "You don't seem to like him-"
         play music "ringtone.ogg"
         show alice surprised at bounce
         show dress at bounce
         show alice_base_longhair at bounce
         show mc shocked at bounce
         show hoodie at bounce
         a "?"
         show mc stressed
         m "Please don't do this."
         stop music
         "Again, you decline your dad's call, and send a follow up:"
         "\"Sorry, I am really busy. Is it important?\""
         show mc normalsquint
         "You stare at the screen, but he doesn't read it."
         show alice sly smile
         a "Don't get along, I take it?"
         "You don't answer."
         "Because you're waiting, and on the inside of your head, is a countdown:"
         m "(Three... two... one...)"
         play music "ringtone.ogg"
         show alice surprised
         show mc vstressed
         m "..."
         show mc shout
         m "{sc=5}{color=#000000}{size=+20}Why are you like this!?"
         m "Why do I always have to-"
         show mc sigh
         m "..."
         show mc sad
         m "Sorry Alice. Could you please wait for five minutes?"
         show alice sly smile
         a "Sure. Try not to explode."
         hide alice
         hide alice_base_longhair
         hide dress 
         with dissolve
         "Giving you a little pat on the shoulder, Alice leaves you to sit on a bench." #Already established they're by the riverbank
         "And, with a deep breath to steel your nerves, you answer the call."
         jump day2PhoneCall
         

      "Accept the call.":
         show mc stressed
         m "Hey, uh... I need to go take this."
         show alice sulk
         a "Sure."
         hide alice
         hide alice_base_longhair
         hide dress 
         with dissolve
         "Alice nods curtly and sits on a nearby bench." #Already established they're by the riverbank
         "But you're too preoccupied by the imminent event to feel guilty."
         "Heart racing with trepidation, you answer the call."
         jump day2PhoneCall

label day2PhoneCall:
   stop music
   stop sound
   play sound "windgust.wav"
   play music "wind.wav"
   if declineDad: #Because he's annoyed now, he's even more cruel and abusive
      dad "So you decided to answer me now?"
      m "I sent you a message-"
      dad "Well, since you have time to talk, I just wanted to let you know..."
      show mc 
      dad "... that I got a little message from the bank that you'd used my card today."
      show mc worried
      m "*Gulp*"
      dad "Been doing some shopping with my money, eh? What did you get?"
      show mc embarrassed
      m "A hoodie."
      dad "Yes, I see that you went to Hoodie Emporium. You've got enough of those damn things if you ask me."
      show mc stressed
      m "(I didn't.)"
      dad "And what did you get in the women's store?"
      show mc vshocked
      m "..."
      dad "..."
      show mc worried
      m "(Shit. Shit. I'm taking too long to respond! He's going to think I did something I shouldn't have.)"
      m "I-it was for a friend."
      dad "That's a lot of money you're spending on a {i}friend{/i}, %(player_name)s."
      dad "Are you sure you haven't got a girlfriend you're not telling me about?"
      show mc shout
      m "No! We only met two days ago."
      dad "Hmm..."
      show mc slightsad
      m "Was that all you wanted to ask?"
      dad "What's the rush? Oh, are you out with your lady friend?"
      m "...Yes."
      dad "Aha. Give her lots of compliments. Just nod when she talks and nod like her every word is the fucking word of God."
      dad "You'll get there in no time. Later."
   else:
      dad "Hello?"
      show mc stressed
      m "Hey dad... How's it going?"
      dad "Well, I was doing pretty good."
      dad "I went down to the shop to see how the work on my car is going."
      dad "I was just talking to the mechanic about what kind of engine to import."
      dad "And then... I got a notification from the card I gave you."
      show mc worried
      m "*gulp*"
      dad "And I saw you've been doing some {i}clothes shopping{/i}."
      show mc surprised
      m "Uh... yeah."
      show mc worried
      m "So it's come to this..."
      m "I can expl-"
      dad "You finally got yourself a girlfriend?"
      show mc confused
      m "Huh?!"
      dad "I mean that's the only thing I can think of."
      dad "You're not one of {i}those{/i} people to go buying stuff from women's stores for yourself."
      m "..."
      show mc awkwardsmile
      m "Uh, yeah, haha..."
      m"... Of course not."
      dad "When I was your age, I was plowing through some pusssy! I get it. Just as long as you keep up with your studies."
      dad "So you're going to introduce me sometime right?"
      m "Uhh."
      dad "I looked through all your social media looking to see if I could find her, but I didn't see anything, seeing how you never post."
      dad "You don't have any accounts I don't know about do you?"
      show mc slightsad
      m "Uh no..."
      dad "Good."
      show mc sad
      m "Is that it?"
      dad "Yeah, I'm going to get back to making my moonshine."
      dad "You remember I showed you the distillation rig I built right?"
      m "Uh yeah... Have fun!"
      dad "Will do, {i}son{/i}."
      dad "Later."

stop music fadeout 3
show mc sigh
"You end the call, throw back you head, and shake out all the disgusting things you just heard him say from your head."
show mc sad
"Then you look for Alice."
show mc at right 
show hoodie at right
with move
show alice_base_longhair at left
show alice sulk at left
show dress true at left
with dissolve 
"She's kneeling beside some flowers on the grass, watching a butterfly perched on a white daisy."
show alice surprised
a "So? How was it?"
show mc awkwardsmile
m "It was fine. Sorry for the delay. We can go now."
show alice normal
ali "Are you okay? You seem kinda off."
show mc normalside
m "Yeah, it's nothing."
show alice pout
ali "If you say so..."
#"Alice slowly stands up and you resume your walk back home."
window hide

jump preFightDay3

#   For "The snapping point", I think his self-doubt about how quickly she's improved at guitar could be better portrayed:
#   instead of saying it all from the POV of why this is hard for him (which is too obviously self-focused + annoys me),
#   he can phrase it as a frustrated encouragment, trying to get her to see why everything is okay and she can stop stressing and be proud of all she has done instead.
#   For example, "Why are you so upset/stressed/afraid? Stop putting yourself down - don't you know how much I look up to you? You've worked so hard, you've learned so much,
#   and what I can sounds better than anything I could do. You've accomplished more than I ever have!"
#   This way MC's self-hate is more backhanded AND it shows how their relationship has grown to the point that
#   he is genuinely worried about her and wants her to see how HE sees her.

label preFightDay3:
   scene black with fade
   scene bottle noon:
      zoom 0.9
   with Dissolve(2)
   show day_3 at topleft
   show alice_affection at topright
   with dissolve
   play sound "door.wav"
   play music "night.mp3" 
   show mc sad at right
   show hoodie at right
   show alice_base_longhair at left
   show dress true at left
   show alice serious at left
   with easeinbottom
   
   hide alice
   hide alice_base_longhair
   hide dress
   with dissolve
   show mc confused
   window show
   # show her rushing back thorugh door as you get back
   m "Damn, you really aren't wasting a second, huh?"
   show mc at center
   show hoodie at center
   with move
   show mc stressed
   m "*Sigh*"
   show mc normalside
   "Alice doesn't bother to reply as she sits on the chair on hefts to guitar onto her lap."
   "It seems she wants to be left alone, and that just proves how unimportant you are to her right now."
   "She only cares about herself."
   show mc slightsad
   m "(Which she {i}should{/i} be doing. It's her last day. I shouldn't try to take up so much of her precious time.)"
   m "(But it would have been nice to hang out together.)"
   show mc stressed
   m "..."
   show mc normal
   m "I may as well read some manga. We still have a couple hours before the show stars."
   window hide
   scene black with dissolve
   window show

   "The first hour is fine enough..."
   "You can't focus on reading, over the sound of the same guitar phrases repeated over and over..."
   "...But it's fine....."
   "......Another hour rolls by......."
   "...........And she hasn't so much as looked in your direction............."
   stop music fadeout 6
   m "..."
   "Another hour..."
   play sound "guitar_note.wav"
   "The sound of the guitar drills its way further into your brain."
   play sound "<from 0 to 1>guitar_note.wav" loop
   "Echoing though your skull and ears."
   play sound "guitar_note.wav" noloop
   hide mc
   "A wave of nausea swirls in your stomach, rising quickly to your throat. You swallow, fists clenched to keep it in."
   "Your heart isn't calming down. It's only getting faster."
   show mc stressed
   show hoodie
   with dissolve
   "Panicked, you realise you're suddenly standing."
   "And you notice with pain that Alice doesn't notice."
   "She's so focused."
   "You can't be here right now... with her..."
   show mc vstressed
   "Your stomach feels like you've swallowed a brick."
   "The same phrase fades in and out of your head, ebbing with the chords of guitar, over and over again."
   window hide
   pause 1

   # Pulsing text: ---


   show text "Shut up." with dissolve
   pause
   hide text
   show text "{size=+10}Shut up."
   with dissolve
   pause
   hide text
   show text "{size=+30}Shut up."
   with dissolve
   pause
   hide text
   show text "{size=+60}Shut up."
   with dissolve
   pause
   hide text
   show text "{size=+100}Shut up."
   with dissolve
   pause
   hide text
   show text "{size=+400}Shut up."
   with dissolve
   pause

   hide text
   scene bottle noon:
      zoom 0.9
   show day_3 at topleft
   show alice_affection at topright
   show mc vstressed
   show hoodie
   with dissolve
   window show



   # # ---
   # "\"Shut up\""
   # "You've been annoyed since the call earlier."
   # "But you thought you could put on a smile for her"
   # "On her last day"
   # hide black with dissolve
   # show mc vannoyed
   # "You look over to her"
   # "She's staring at the fretboard"
   # m "..."
   # show mc at quiver
   # "You don't know what's going to come out, but it's already coming out before you can brace yourself-"
   # window hide
   # show black

   # show text "Say something!"
   # $ renpy.pause ()
   # show text "Anything!"
   # $ renpy.pause ()
   # 
   # m "..."
   # show mc stressed
   # m "Hey, do you mind like... Taking a break? For my sanity?"


   #Trying a faster approach because I think you've already built tension and the above is redundant and explaining too much

   #---
   show mc vshout
   m "{sc=5}{color=#000000}{size=+80}CAN YOU JUST-!"
   show mc sigh
   m "Please... take a break?"
   #---

   "..."
   
   show mc confused at bounce
   show hoodie at bounce
   m "Hey! Can you even hear me?"
   "..."
   show mc vannoyed
   "You walk over to her and-"
   window hide
   play sound "unplug_guitar.wav"
   stop music
   show alice_base_longhair at left
   show dress true at left
   show alice shocked at left
   with easeinbottom
   show mc vshout
   window show
   m "{size=+20}Stop it already! You've been playing the whole day!"
   m "I want to support you, but I just can't take it anymore!"
   show alice serious
   ali "Hey, what the hell? I'm busy!"
   show mc stressed
   m "I go through all the effort to set up all this stuff for you, and you..."
   show alice disappointed
   ali "And I what? Use it?"
   # show alice annoyed
   # ali "Sorry for existing I guess."  #I don't like this line
   show mc vannoyed
   m "You don't get it. "
   m "This is our last day together and you're just wasting it on {i}this{/i}."
   show mc vstressed
   m "Who cares if you win or not? Why do you care so much about this stupid competition!?"
   m "None of this shit matters!"
   m "Wasn't the whole point of this to not please anyone else?"
   show mc confused
   m "But you're just-"
   show mc awed
   "You suddenly realise how bitter the words you're spewing are."
   "They taste bad. You don't like what you're saying, but you're already said most of it."
   "And as if you can't defy the momentum, you finish your horrid sentence."
   show mc embarrassed
   m "...going from an insecurity that was imposed on you, to one you chose."
   show alice neutral
   ali "..."
   show alice vannoyed
   ali "..."
   show alice cry
   ali "..."
   window hide
   hide alice
   hide alice_base_longhair
   hide dress 
   with easeoutbottom
   play sound "door.wav"
   # Forced wait for 3 seconds so like . wait . wait ."
   # but her expression changes
   #"Clutching the guitar towards her chest, Alice stands up, and walks towards the door." #Too much explaining. To keep with the style of the story, I'm removing redundant ones
   show mc sad
   m "..."
   # ali "Somewhere I can focus without you"
   show mc at center with move
   
   # m "She's gone..."
   # show mc normal
   # m "..."
   show mc vstressed
   m "What's wrong with me?"
   m "I have to find her."
   default looked_river = False
   default looked_mall = False
   menu:
      "Where do I look?"
      "The mall.":
         #"..."
         scene mall with fade
         $ looked_mall = True
      "The river bank.":
         #"..."
         scene enbankment with fade
         $ looked_river = True
   # ORder doesn't matter but gives scenery to go past as you have the internal dialogue
   play music "trip.mp3"
   # switch nvl?
   "Haha, you did it again!"
   "If there was a prize for making girls cry, you would be a shoe in {i}the dis-noble {/i}prize"
   "This is how it always is though. "
   "Every friendship, acquintance, classmate or crush... Without fail, you'll always find the best way to push all of them away from you."
   "But, honestly, did you really expect anything different this time?"
   "No. In fact, I can say this without a shadow of doubt:"
   "In every alternate universe, you make Alice cry and run away from you."
   "You can't help but judge her for how she lives her life."

   m "I don't see her anywhere. Where else could she be?"
   menu:
      "Where else do I look?"
      "The mall." if looked_mall == False:
         scene mall with fade
         #"..."
      "The river bank." if looked_river == False:
         scene enbankment with fade
         #"..."

   "All of this \"helping her\", trying to grant her last wishes..."
   "You're just pretending to be a good person. If it was true, you wouldn't be so alone in the first place."
   "You were jealous of Alice from the very beginning."
   "The way that she could say what she really felt, or..."
   "... how she could do more than you've ever accomplished in less than a fraction of the time you've been alive."
   "How does she know who she is so easily? In your whole life, you {i}still{/i} don't know who you are."
   # ("How she dressed, or how she looked"?)
   # "That's how you really feel!"
   "But that's okay! She's be gone soon, and then you'll forget everything, and our usual life will return."
   "Just you and I, forever..."
   window hide
   show mc slightsad
   show hoodie
   with dissolve
   window show
   m "..."
   "Besides, why do you care so much about some bitch that's going to die in a few hours anyway?"
   show mc shout
   m "I'm not like that!"
   m "I'm not who you-"
   show mc normal
   m "Who I think I am..."
   show mc sad
   m "Where are you, Alice?"
   # Show running out into the hall
   show mc stressed
   "You think back to the first night where Alice ran off by herself..."
   # m "..."
   # m "I think I know where she is"
   window hide
   #scene trans
   #play sound foodsteps and heartbeat
   scene hallway with fade
   pause
   scene rooftop with fade
   show alice_base_longhair at left
   show alice think at left
   show dress true at left
   with dissolve
   play sound "door.wav"
   show mc pant at right
   show hoodie at right
   with easeinbottom
   window show
   m "Alice!"
   jump rooftop_reworked

label rooftop_reworked:
   # he goes up to roof sweaty
   # starts trying to apologise  
   m "Alice, I- *pant* I-"
   show mc sad
   m "I wanna say that I'm-"

   # is interrupted by alice somberly talking at him about butterfly
   ali "Since we went out yesterday, I've been thinking a lot about butterflies."
   show mc awed
   m "..."
   "You look down at her sitting on the floor, and notice a large red butterfly on her fingertip."
   show alice sulk
   ali "At first, when we went to the cafe, I was really surprised when the waiter brought me that butterfly art."
   # ali "And I thought about what it might mean."
   ali "I could be overthinking it, and he went off of vibes but..."
   ali "Maybe there was a reason that he chose that." #Changed above because you used maybe here already
   ali "So I thought really hard about it, and after you went to sleep, I took a break from practicing to do a little research."
   show alice normal
   ali "And I realised butterflies aren't that different from me."
   show alice sadsmile
   ali "We're both pretty, but short-lasting."
   ali "Once we leave our cacoons, we've only got a few days to explore the world, or to leave any sort of lasting legacy." 
   show alice think
   ali "Just to have any proof that we existed at all."
   ali "And I-" # The original sentence wasn't necessary. It's already evident in the following sentences they remind her of her own life.
   show alice cutesad
   ali "I want my life to mean {i}something{/i}." #Something. Anything. Is a bit overdone in media
   ali "Not just be a pretty butterfly that's gone with the wind. I want to be make some kind of legacy."
   # ali "But I'm still scared..."
   # show alice worried
   # ali "I'm scared that no matter what I do, even if I could change the entire world, it wouldn't change how I feel."
   show alice depressed
   ali "I'm sorry for pushing you away."
   show mc sad
   m "You don't need to-"
   a "If I had more time, I-"
   show mc shout
   m "Please don't apologise! I'm sorry. I was just... I don't know."
   show alice worried
   # ali "It's just hard!"  
   # ali "The time we have is limited, and in the moment, it's easy to tell yourself that what you're focused on is the most important thing in the world." # I'm struggling to understand this senstence. I think it's too vague.
   # ali "To feel like I accomplished something! But I didn't want to push you away."
   # ali "I should have treasured the time I have with you more..." # What? I thought she regrets that she pushed him away, but understands why it's necessary given her limited time. I don't see why she think she didn't treasure the time with him. 
   # show mc 
   # m "You know."
   # m "I don't think you picked music because you wanted to be the best, or win the competition..."
   # show mc cute
   # m "I think it's because you saw something that spoke to you"
   # m "And maybe that's all that matters..."
   # m "But even so..."

   # m "You've been playing guitar for a couple of hours, and-"
   # "She's already better at it than you've ever been at anything."
   # show mc cute
   # m "I don't think you realise how amazing you are."
   # show mc normalside
   # m "I was thinking about how I lashed out earlier and..."
   show mc slightsad
   m "I was just jealous. You're really good at guitar, and..."
   show alice shocked
   a "Jealous of me? Why!?"
   show mc stressed
   m "I have so much time compared to you, but I still haven't accomplished a thing."
   m "There's so much I want to do, but I never commit to anything past a few days."

   # show mc stressed
   # m "I just wanted to spend a bit more time with you before you..."

   # I think it's important that he says this at some point but the timing feels bad here
   # m "Damn I'm fucking pathetic..."
   # m "I have so much time compared to you, but I still haven't accomplished a thing."
   # show mc slightsad
   # m "I tell my self I'll learn to draw."
   # m "Or learn an instrument."
   # show mc shout
   # m "Or fucking anything."
   show mc sulk
   m "I'm still just wasting time everyday telling myself it will all work itself out, without putting in actual effort."
   # m "That tomorrow, someone will push me towards living the life I want to..."
   # m "For an excuse..."
   m "Because people will judge me for what I like."
   # Unused stuff to pull from

      # ali "Well then you're back where you started."
      # ali "And you can find another reason to live"
      # ali "Humans are good at that"
      # show alice happy
      # ali "So I guess in the meantime, all you can do is find a waste of time that feels special to you"
      # ...
   show alice disappointed
   a "That's stupid. Just do what you want."
   show mc vstressed
   m "I know it's stupid! I realise that whenever I see you being passionate about guitar with all your energy."
   # m "I just want to like myself."
   # m "But even then..."
   # m "I know it will never be enough"
   # m "Even if I tried to like myself it wouldn't be enough for my parents"
   # show mc slightsad
   # m "Because all they want me to be is the person they THINK I am"
   # show mc vannoyed
   # m "But I CAN'T be that person!!"
   # m "I've never been that person..."
   # show alice normal
   # ali "..."
   show alice normal
   m "I KNOW I might be making the biggest mistake of my life by thinking of what I'm supposed to do, instead of what I want to do, but-"
   m "My parents think I'm a straight A student, with lots of friends. Ha!"
   m "My dad is making up fantasies of me having a girlfriend and living up to how he was in college."
   m "I don't even know what he would do if he found out who I {i}actually{/i} am."
   show mc sigh
   m "That I'm on the verge of flunking out."
   m "That I have no friends."
   m "That I'm completely different to him..."
   show mc sulk
   m "I just feel like time keeps moving, and I'm still alone... In my room."
   m "And after college, I'm going to work doing some crappy deskjob I hate, until I get old and die."
   show mc sad
   m "I'm sorry. I came to apologize and I just ended up talking at you."
   show alice sigh
   ali "Same here. At least we're even now." # I wanted her to acknowledge a bit of what he said.
   show alice happy
   ali "I don't know why, but I feel a lot calm after saying everything."
   show alice think
   ali "I think, not matter how much time I spend on it, my legacy song isn't going to be perfect."
   show alice vannoyed
   a "I'm just going to do my best, whatever that ends up being."
   show mc slightsad
   m "I wish I could help you."
   # ali "Or enough..."
   # ali "Just existing, and experiencing..."
   show alice smirk
   a "..."
   show mc vannoyed
   m "What are you scheming now?"
   show alice hime
   # ali "Hey..."
   # ali "I know it doesn't make up for earlier but..."
   ali "Well, I was wondering if maybe..."
   show alice wink
   show mc awed
   ali "... you'd wanna help me with the finishing touches of my song?"
   show mc confused
   m "But it's YOUR song!"
   show alice tsun
   a "Does that mean I'm not allowed help? And this is the only way I can actually finish on time, so..."
   show alice smirk
   a "You don't get a choice!"

   window hide
   #show mc embaressed
   stop music fadeout 2
   scene black with dissolve
   window show
   "For the next two hours, you give critique and help Alice polish up her song's pacing and cutting out overly-ambitious scopes." # placeholder text for pacing
   "It's fun, and the time pressure forces both of you to focus." # placeholder text for pacing
   "As the night emerges, you and Alice pack up and walk to the venue." # placeholder text for pacing
   window hide
   jump preshow
label preshow:
   play music "mall.mp3"
   scene music_club with Dissolve(2)
   show mc happy at right
   show hoodie at right
   show alice_base_longhair at left
   show dress true at left
   show alice worried at left
   with easeinbottom
   window show
   m "Okay, we made it in time!"
   ali "..."
   show mc awed
   m "Now just to sign up over here and-"
   ali "Can we go home?"
   show mc shocked
   m "Huh!? But we... you just spent all day finishing the song!"
   show alice sad
   ali "I've changed my mind. I don't... think I can do this."
   show mc confused
   m "Don't be ridiculous! You've worked so hard!"
   ali "But-"
   show mc happy
   m "Hey, you've got this!"
   show mc annoyed
   m "And even if you mess up, at least you commited and did something most people will never do in their lives."
   show alice sigh
   ali "Okay..."
   show alice serious
   ali "Fuck it. Let's do this."
   "Alice snatches the pen with great enthusiasm and vigor and-"
   show mc vannoyed
   ali "..."
   show alice blush
   ali "Can you sign up for me?"
   show mc confused
   m "Huh? Why?"
   show alice disappointed
   ali "I can't write, remember?"
   show mc normalside
   m "Oh yeah, forgot about that."
   "*Skribble Skrabble*"
   show mc happy
   m "Done. Now, we wait."
   window hide
   hide alice
   hide alice_base_longhair
   hide dress
   
   with dissolve
   show kellin happy at left
   with easeinbottom
   #kel "And then you should have seen her face when-"
   show kellin vhappy
   show mc vshocked
   window show
   kel "%(player_name)s? Whaaaaaaat?"
   kel "You should have told me you were gunna come down here! This is like my stomping ground!"
   kel "I've gotta introduce you to-"
   show alice_base_longhair at left
   show alice normal at left
   show dress true at left
   with easeinbottom
   show kellin shocked at bounce
   kel "!"
   show kellin at right with move
   show kellin shocked at flip
   show mc surprised at center
   show hoodie at center
   with move
   kel "It's her!"
   show alice shocked
   a "It's you!"
   show mc confused
   m "...?"
   show kellin awkward at flip
   kel "I'm sorry, I gotta go, %(player_name)s! I'll catch you later."
   hide kellin with dissolve
   show alice vannoyed
   show mc at right
   show hoodie at right
   with move
   m "What was that? Why did he recognize you?"
   show alice normalside
   ali "You remember how when we first met..."
   ali "... I ran away to the shower room?"
   show mc shocked
   m "Wait! HE'S the guy from back then?!"
   show alice sigh
   ali "Yeah."
   show mc stressed
   m "Holy shit, that's so awkward. I've gotta apologize to him later."
   #m "Anyway let's head inside..."
   window hide
   hide mc
   hide hoodie
   hide alice
   hide alice_base_longhair
   hide dress
   with dissolve
   jump aliceDay3Show

label aliceDay3Show:
   window show
   "You wait nervously with Alice in the venue, surrounded by several groups merrily drinking and laughing."
   "And then the lights dim, the sound of merriment hushes, and all eyes focus through the darkness to the spotlit stage."
   "As the first performance starts, you notice how Alice stares at the stage, fully immersed in the moment."
   # "Something with no place in reality, but on Youtube or TV."
   # "Real people who practiced and whose legs were shaking as they sung."
   window hide
   show alice_base_longhair at left
   show dress true at left
   show alice cutesad at left
   show mc awed at right
   show hoodie at right
   with dissolve
   window show
   m "Hey, you you should get backstage soon."
   show alice sad
   ali "Mm..."
   show mc normal
   m "Hey, just one thing before you go."
   show alice worried
   show mc happy
   m "No matter how it goes, I'm really proud of you."
   show alice blushside
   ali "Thanks..."
   show alice happy
   ali "I gotta go!"
   window hide
   hide alice
   hide alice_base_longhair
   hide dress
   with easeoutbottom
   scene music_stage with dissolve
   stop music fadeout 3
   window show
   announcer "Okay ladies, gentlemen, and those in between~"
   announcer "Next up I want you all to give a warm welcome to..."
   announcer "... Alice!"
   show alice_base_longhair
   show alice flirtsweat
   show dress true
   with dissolve
   ali "Uh, hi there~"
   announcer "Is there anything you want to say to the crowd before you start?"

# Unused stuff to pull from
      # ali "You took me to a whole bunch of places and showed me a bunch of stuff."
   # show alice confused
   # ali "and at first I thought it was meaningless."
   # show alice normal
   # ali "But I realized that nothing matters except what is important to you."

   # ali "Latte art is just making pictures in cow boob juice."
   # ali "And video games are just what depressed people do to avoid dealing with real life."
   # # Too much
   # ali "But even then."
   # show alice serious
   # ali "Those are things that bring meaning to people."
   # ali "Every single thing you could be interested in."
   # ali "has so much depth when you actually look into it."
   # ali "Every rabbit hole runs so deep."
   # show alice normalside
   # ali "And I guess what I'm trying to say is"
   # show alice sad
   # ali "You can't wait for someone else to give you permission to act"
   show alice surprised
   ali "I uh- haven't really prepared anything..."
   show alice cutesad
   a "But..."
   ali "I guess the last few day have been a really chaotic time for me."
   show alice think
   ali "There where times I felt like everything was meaningless, but I had someone with me to help me through that."
   show alice happy
   ali "And I wouldn't be up here without them."
   show alice normal
   ali "This song is called \"Metamorphisis\"."
   #play song fail

   # Maybe using dynamic audio and vamps to get the song to progress as the user clicks?
   "Alice starts playing the melody I have heard so many times by now."
   "But this time, seeing her up on the stage, it felt different."
   "Knowing how much she put into it to get here..."
   "She opens her mouth to start singing and-"
   show alice shocked
   "Her voice awkwardly pops out and cracks part way through the second word."
   "Her hands freeze. An awkward silence runs across the room."
   "..."
   show alice normal
   "Then, her eyes scan the audience... and stop on me."
   show alice flirtsweat
   ali "I guess I focused so much on the guitar that I forgot to practice singing! Hahaha!"
   show alice sigh
   ali "Let's try that again."
   "She starts the song again from the beginning, but this time, when the verse starts..."
   show alice sly smile
   ali "*first lyric line*"
   "She talks over the music as if casually chatting to herself."
   ali "*lyrics*..."
   show alice happy
   # Lyrics go here ->
   play sound "yay.wav"
   announcer "Let's give it up one more time for Alice! Next up, we have..."
   window hide
   jump post_show

label post_show:
   scene alley with fade
   window show
   m "Alice!"
   window hide
   show alice_base_longhair at left
   show alice cutesad at left
   show dress true at left
   with easeinbottom
   "You see her walk out from the backstage door, but waiting there for her is-"
   show kellin happy at right
   show kellin at flip
   with dissolve
   kel "Hey Alice!"
   show alice shocked
   ali "!?"
   m "(Oh no! I have to get between them before-)"
   show kellin awkward
   kel "I'm so sorry!"
   show alice surprised
   kel "At first I hated you, because of what happened the other day."
   show kellin shocked
   kel "But after hearing your song, I completely understand now!"
   show kellin vhappy
   kel "It must have been some weird misunderstanding right?!"
   show alice flirtsweat
   ali "Ah..."
   kel "You were so good! I really loved the way you did the (input technical aspects from the actual song)."
   #show mc awed at right
   m "Hey guys..."
   #show mc normal
   kel "%(player_name)s! I thought you were going to use that guitar to learn for yourself!"
   kel "Why didn't you tell me?"
   #show mc worried
   m "Sorry. I probably got distracted by all the talking and forgot."
   show kellin happy
   kel "If you'd told me it was for a girl with such small hands, I would have lent you a guitar with a smaller neck!"
   kel "I bet it was hard to play!"
   show alice surprised
   ali "Wait you're the neighbour we're borrowing from!?"
   #show mc normalside
   show alice laugh
   ali "Thank you so much! I wouldn't have been able to do this tonight if you hadn't lent-"
   show kellin normal
   kel "If you wanna say thanks, I know the perfect way."
   #show mc confused
   #m "You don't mean..."
   kel "You'll have to pay by..."
   show alice sad
   ali "*gulp*"
   show kellin vhappy
   kel "Letting me take a group Polaroid of us!"
   show alice confused
   ali "A what?"
   # show mc surprised
   # m "Wooooah... It's one of those old cameras. Where did you get it?"
   show kellin happy
   kel "A polaroid! I ordered it second-hand online for super cheap! Hahaha!"
   show kellin vhappy
   kel "Ready or not! Cheese!"

   play sound "polaroid.wav"
   show white with dissolve
   show alice shocked
   hide white with dissolve

   show kellin happy
   kel "Nice. I'll see you guys inside."
   hide kellin with dissolve
   m "Hey."
   show mc happy at right
   show hoodie at right
   with dissolve
   m "Are you okay? The flash must have been pretty suprising, huh?"
   show alice normalside
   ali "Yeah... I'm fine...I was just-"

   #play sound notice
   # Maybe kellins friend should rush from inside to let them know
   announcer "Okay, it's time to announce today's winner!"
   show alice shocked
   a "The winner!?"
   show mc shocked
   m "We have to get back inside!"
   scene music_stage with fade
   show alice_base_longhair at left
   show dress true at left
   show alice worried at left
   #show kellin normal at left
   show mc awed at right
   show hoodie at right
   with dissolve
   announcer "And today's winner..."
   announcer "Who will have the luxury of recording a single at (insert funny names) studios for completely free!"
   announcer "IS~"
   ali "..."
   announcer "..."
   announcer "{sc=3}{color=#000000}{size=+80}VICIOUS FISH!!!"

   play sound "yay.wav"
   play music "mall.mp3"
   show mc sad
   m "Alice, I'm so-"
   show alice laugh
   ali "Heheh! Such a weird band name!"
   show mc confused
   m "Are you okay?"
   show alice sly smile
   ali "Yeah? What, you thought I was gonna cry if I lost?"
   show alice neutral
   ali "Plus what am I going do with the prize of recording a single after I'm gone?"
   #show mc awed
   #show alice surprised
   kel "Are you going somewhere?"
   hide mc
   hide hoodie
   with dissolve
   show kellin awkward at right
   show kellin at flip
   with dissolve
   show alice think
   # show mc normal
   ali "Uh... yeah. I'm going abroad."
   show kellin vhappy
   kel "Oh that's awesome! But kinda a shame."
   show kellin happy
   kel "We were just missing a rhythm guitarist and I was gunna ask if you could fill in..."
   kel "ANYWAY! When are you leaving?"
   show alice normalside
   ali "Tonight..."
   show kellin shocked
   kel "Oh, that's CRAZY!"
   show kellin normal
   kel "Do you need a ride to the airport? My friend has a big car, so we could-"
   show alice flirtsweat
   ali "No, thanks, it's okay!"
   show alice normal
   ali "Anyways! It's getting pretty late..."
   ali "We should head back so I can get ready."
   show kellin awkward
   kel "Aw, I was hoping we could talk about music!"
   show alice happy
   ali "I'm sure we'll get that chance next time."
   show kellin happy
   kel "Yeah, I'm looking forward to it!"
   show kellin normal
   kel "Oh yeah. It should be ready by now."
   show alice surprised
   ali "Huh? This is..."
   show kellin happy
   kel "It's the photo I took earlier!"
   kel "You should have it. It'll be something nice for you to remember us by."
   show alice cutesad
   ali "Wow, this is so pretty. Is it really okay if-"
   show kellin vhappy
   kel "Of course! I bought it for this sort of thing anyway!"
   kel "Anyway, I'll go. Sorry to stop you from going home."
   show alice sly smile
   ali "No it's okay! Thank you for everything. I hope you enjoy the rest of your night."
   kel "Yeah, you too! Stay safe!"
   hide kellin with dissolve
   show mc happy at right
   show hoodie at right
   with dissolve
   m "Don't worry. I'll look after her. Ready to go, Alice?"
   show alice laugh
   a "Yeah."
   window hide
   stop music fadeout 2
   scene black with dissolve
   jump aliceDay3WayBackHome

label aliceDay3WayBackHome:
   window show
   "The two of you walk back towards your dormitory in silence."
   "Until Alice's pace grinds to a halt."
   window hide
   scene outside_dorm with fade
   play music "trip.mp3"
   show mc awed at right
   show hoodie at right
   with easeinbottom
   window show
   m "Hey, are you okay?"
   show alice_base_longhair at left
   show alice sad at left
   show dress true at left
   with easeinbottom
   ali "Yeah... I mean... I don't know. It's just that it's all over."
   ali "I'm supposed to feel okay now, like this life was enough. I accomplished something and made memories, but..."
   show alice think
   ali "Even still... This is it huh?"
   show mc cute
   m "There's still time! Maybe we can find a way for you to live \'til tommorow-"
   show alice serious
   show mc awed
   ali "Stop."
   ali "I know that it's time."
   show alice sulk
   ali "I can feel it."
   show alice vannoyed
   m "..."
   show alice sly smile
   ali "Tonight was fun."
   ali "Kellin was really nice. He seems to really loves music."
   show mc normalside
   m "Yeah, and he didn't even ask if we are dating or anything."
   show alice sigh
   ali "Why's that the first thing you say?"
   show mc awkwardsmile
   m "I don't know."
   show mc slightsad
   m "He's just not like some other people I know."
   show alice normal
   "Alice starts walking again, this time much slower, as if hoping to elongate the trip back."
   show alice sulk
   ali "Don't you wish you'd reached out to him earlier?"
   show mc normalside
   m "Yes, but..."
   m "I don't think I could have. Even now..."
   show mc worried
   m "It's still scary to know that if I say the wrong thing he might never want to talk to me again."
   show alice disappointed
   ali "Stop being so dramatic! Not everything is life or death..."
   show alice laugh
   ali "Unless you're me, that is! Haha!"
   show alice sly smile
   ali "But even if you mess up a little, I think you could just apologize."
   show mc stressed
   m "Maybe it is that simple."
   show mc slightsad
   m "Hey, I wanted to say..."
   m "About the song you wrote."
   show mc cute
   m "Thanks. It means a lot."
   show alice shocked
   ali "What are you talking about!?"
   show alice flirtsweat
   ali "Those l-lyrics didn't mean anything, idiot!"
   show mc confused
   m "They didn't?"
   show alice tsun
   ali "Don't get me wrong! I just made them up to go with the melody!"
   show mc surprised
   m "Real tsundere!?"
   show alice pout
   ali "Huh? What does that mean?"
   show mc annoyed
   m "Nothing."
   show mc happy
   m "You really worked hard for today, and I'm really proud of you."
   show alice blush
   a "You already said that. But... thanks."
   a "..."
   m "..."
   # show alice think
   # ali "Hey... I just thought you should know..."
   # show mc normal
   # ali "Even though I'm poisonous..."
   # ali "There's a way you can prepare me so that I'm edible"
   # ali "And even if you screw up a little, no one had died eating from eating a fly aminitas in over a hundred years."
   # m "Eat you?"
   # m "What?"
   # m "Why-
   # m "Why would I do something like that?"
   # ali "I want you to... It's the last "
   # show alice normal
   # ali "I really appreciate what you did for me."
   # ali "Even though it was hard at first."
   # show alice happy
   show alice blushside
   ali "I'm glad things turned out this way."
   show mc cute
   m "Me too."
   show alice sad
   ali "I'm... going to go for a walk tonight."
   ali "By myself."
   show mc confused
   ali "So don't come looking for me."
   show mc shocked
   m "But I want to be with you when-"
   show alice serious
   ali "Please. I want for you to remember me for the time we spent together, not for how I left."
   show mc awed
   m "..."
   show mc sad
   m "Okay."
   show alice sulk
   ali "Sorry."
   show alice sadsmile
   ali "Or rather, thank you."
   window hide
   stop music fadeout 2

   jump aliceDay3Goodbyes

label aliceDay3Goodbyes:
   scene black with fade
   scene bottle night:
      zoom 0.9
   with Dissolve(2)
   play music "night.mp3"

   show day_3 at topleft
   show alice_affection at topright
   with dissolve

   play sound "door.wav"
   show alice_base_longhair at left
   show alice sigh at left
   show dress true at left
   show mc sad at right
   show hoodie at right
   with easeinbottom
   window show
   ali "Home sweet home! Aaah, I'm so tired..."
   m "I bet..."
   show mc vstressed
   "You stand there, uselessly frozen, unsure what to say."
   "You're not equipped for dealing with serious situations like this."
   show alice normal
   ali "Do you want to watch a movie or something?"
   show mc surprised
   m "A movie? But-"
   show alice confused
   ali "Do you like comedy or are you into something like horror?"
   show mc confused
   m "Comedy, but-"
   show alice normalside
   ali "Yeah, that tracks..."
   show mc slightsad
   m "Are you sure you are fine with just watching a movie?"
   m "Isn't there anything else you'd rather do?"
   show alice normal
   ali "..."
   show alice sly smile
   ali "I just want normal."
   ali "That's already special enough for me."
   show mc confused
   m "If you're sure..."
   window hide   
   show black with dissolve
   window show
   "You watch a random romantic comedy movie on your laptop, together on your bed."
   "She laughs at the stupid jokes, and tears up for the climax."
   "You watch her every reaction, feeling the urgency to scrape for memories with increasing dread."
   "And before you know it..."
   window hide
   stop music fadeout 2
   show mc stressed
   show alice laugh
   hide black with dissolve
   m "I guess it's over."
   ali "Yeah. That kind of sucked, hahaha."
   show mc cute
   m "Well, you seemed to be enjoying it."
   show alice sly smile
   ali "Yeah I did. No thanks to you constantly staring at me."
   show mc blushside
   m "Sorry. I just don't want to miss anything."
   "..."
   show alice normal
   ali "Hey..."
   show mc normal
   ali "It's kinda getting late."
   show mc slightsad
   m "..."
   show alice normalside
   ali "I should probably head out for my... walk."
   show mc stressed
   m "..."
   show mc sad
   m "So I guess... This is..."
   show alice think
   ali "Yeah. This is it."
   "Alice stands up from the bed and hovers around the door."
   show alice sigh
   ali "I don't really know what I'm supposed to say here."
   show alice normalside
   ali "I could do a long speech about everything I've learned with you."
   show alice sly smile
   ali "But I think it's better if I do this..."
   window hide
   show alice_kiss with Dissolve(2)
   play music "date_musicbox.mp3"
   pause 1
   window show
   ali "You've got a lot of life left."
   ali "So enjoy it enough for both of us"
   ali "Okay?"
   m "Okay..."
   "Your lip starts trembling and tears gather your eyes."
   m "I-I-I-"
   ali "It's okay..."
   window hide
   pause 1
   show mc cry
   show alice sadsmile
   hide alice_kiss with dissolve
   window show
   #"She opens the door and steps into the entrance."

   ali "Have a good life."
   ali "I'll miss you..."
   ali "Where ever it is I'm going."
   window hide
   hide alice_base_longhair
   hide alice
   hide dress
   with easeoutbottom
   play sound "door.wav"
   #"She turns away and closes the door firmly behind her."
   show mc vcry
   window show
   m "Alice..."
   window hide
   stop music fadeout 3
   scene black with Dissolve(2)
   jump aliceDay3Epilogue
#  Choice where you can chase after her?


label aliceDay3Epilogue:
   play music "dynamic_audio/clock.mp3" fadein(2)
   show text "You're having your favourite dream."
   $ renpy.pause ()
   show text "In it, you're with your friends."
   $ renpy.pause ()
   show text "You look around and see them smiling. You hear their jokes and laughing."
   $ renpy.pause ()
   show text "You feel calm. You think nothing."
   $ renpy.pause ()
   show text "You simply exist together. How wonderful."
   $ renpy.pause ()
   show text "The heavy burden of your worries disappear."
   $ renpy.pause ()
   show text "All the things you've cried over in the past don't matter anymore."
   $ renpy.pause ()
   show text "Even your failures."
   $ renpy.pause ()
   show text "At first, you were terrified of this dream, but now..."
   $ renpy.pause ()
   hide text with dissolve
   show polaroid with dissolve
   pause
   show polaroid2 with dissolve
   pause
   show polaroid3 with dissolve
   window show
   scene black with fade
   window show
   "Alice True End."
   window show
   pause


   # "fade out to a cg of the mc's room with the guitar alice wanted, the polaroid they all took together"
   # "as well as 2 more of MC with kellin and kellin's friend, playing in a band together"

   #shot of mcs room with the polaroids on the wall. Guitar on a guitar stand. Cleaner and more managed room. more personality and hobbies
   #Blue pills (estrogen) on top of their desk, and longer hair in the polaroids.

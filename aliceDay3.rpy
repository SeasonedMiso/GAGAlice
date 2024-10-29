#[here i think the bg music when she's practicing should be the song she's writing, but at various levels of playing: think wa2]
label day3Morning:


   scene black with fade
   scene day_clouds
   show bedroom_opencurtains
   show dirty1
   show dirty2
   show bottle
   with Dissolve(2)
   window show
   show day_3 at topleft
   show alice_affection at topright
   with dissolve
   "You wake up to the rhythm of dull strumming."
   show mc surprised with easeinbottom
   m "?"
   m "Damn you're still going?"
   ali "..."
   show mc normal
   m "Hello? Good morning..."
   ali "..."
   "She seems to be completely ingulfed in the guitar world."
   "She can't hear you."
   show mc at left with move
   "You slowly get out of bed and walk towards the kettle to make some coffee."
   show mc normalside
   "While the kettle boils you look over to her and watch her play."
   "You can't hear her that well over the rumbling of water being heated."
   "Her movements look a lot more confident that you remember last night"
   "But when you look at her face you see her eyes are bloodshot."
   "You walk over to her and tap her shoulder gently."
   show mc at right with move
   show mc awed
   m "Hey."
   show mc normalside
   "No response"
   show mc normal
   "You bring your hand up to the top of her head and begin to lift the headphones upwards."
   show alice surprised at left with easeinbottom
   show mc at right with move
   ali "EEK! Wha-"
   show mc happy
   m "Good morning!"
   show alice pout
   ali "Jeez, don't scare me like that"
   show mc annoyed
   m "Haha, sorry about that."
   show mc normal
   m "Looks like you've been going the whole night?"
   show alice sad
   ali "Yeah but I'm behind on time."
   ali "There's no way I'm going to win at this rate."
   show mc awed
   m "Take it easy, you still have lots of time."
   m "And besides, it's not about the outcome, it's about the experience."
   show alice sulk
   ali "Yeah, right, sure."
   hide alice with dissolve
   "She turns back to the paper she's been taking notes on and resumes her practice."
   show mc normal
   "You look at the notes, but it looks like no music notation you've ever seen before."
   show mc confused
   m "Hey, how did you learn how to read music?"
   show alice confused at left with dissolve
   ali "What do you mean?"
   m "Like your notes, they must be some kind of thing you learned right?"
   show alice normalside
   ali "Nah, I just drew stuff to help me remember what part of the song go where."
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
   m "I guess if I had to make a guess based on what I know about dotted mushrooms, then maybe some psychedellic higher wisdom stuff is involved""
   ali "Yeah, maybe!"
   "She quickly turns back and starts practicing again."
   "She doesn't seem anywhere near as interested in contemplating this as you are"
   hide alice with dissolve
   show mc normal
   "You hear the kettle click and walk over to it."
   "You can't help but be impressed by her"
   "But you also feel a bit..."
   "..."
   show black with dissolve
   "play coffee"
   hide black with dissolve
   #Maybe leave this just as an incomplete sentence
   #screen trans
   # maybe slurping sound
   show mc annoyed
   m "Okay, I'm alive now."
   ali "*strum* *strum*"
   show mc normalsquint
   m "Are you ready to go to the guitar store?"
   ali '*pickedy* *pick*'
   "She can't hear you again"
   "You walk over to her and slowly wave your hand in front of her vision"
   show alice mendokusai at left with dissolve
   ali "Whaaat~"
   m "Do you wanna go get strings or not?"
   ali "Ughhh, do I have to?"
   show mc normal
   m "If you can do with out them then I guess not."
   ali "..."
   show alice sad
   ali "Can't you just go for me? I'm running out of time and I still have so much to do."
   show mc worried
   m "A-alone? I... guess I could try, but..."
   m "(But Alice looks stressed. Should she really keep pushing herself so hard?)"
   show mc stressed
   m "(she is going to make her entire last day about a competition she won't even win?)"
   m "(It doesn't feel right.)"
   show mc confused
   m "I think you should take a break, you've been grinding for like 12 hours straight."
   show alice pout
   ali "Nooooo~"
   ali "I don't have time to go with you!"
   menu:
      "Should you just leave her alone? It's hard to ignore the uneasy feeling in the pit of your stomach."
      "Let her grind (N/A).":
         "Skye must still write this part."
         return
      "Make her take a break.":
         show mc worried
         m "Hey, I'm kind of worried about you"
         m "You've been grinding non-stop for the entire night"
         show mc sad
         m "Please, come with me."
         show alice sulk
         ali "Ugh, fine~"
         window hide
         hide mc
         hide alice
         with easeoutbottom
         scene black with Fade(0.5, 1.0, 0.5)
         play sound "door.wav"
         play music "mall.mp3" fadein 2
         show chibi_mc at slightright
         show chibi_alice at slightleft
         with easeinright
         window show
         #What do they talk about on the way?
         "The two of you walk together towards the music store."
         "You walk a little ahead of her, and she follows your back"
         "You get worried that she's lost sight of you, or got lost somewhere along the way"
         "So you check over your shoulder every few minutes, but she's always right behind you"
         "Walking lazily, yet somewhat annoyed."
         jump day3Store

label day3Store:
   #play sound shop bells
   scene music_store with dissolve
   show alice shocked at left
   show mc normal at right
   ali "!"
   show alice awe
   ali "Woah, this place is crazy."

   m "Yeah... There's all sorts of stuff"
   #Maybe drag this out and make it more like "why does that one have a birth defect?"
   show alice confused
   ali "Why is there like... a conjoined twin guitar?"
   show mc stressed
   m "I have no idea."
   show mc normalside
   m "I'm going to go get the strings."
   m "You can have a look around in the meanwhile if you want"
   #Maybe it's better that she points it out only afterwards?
   ali "Are you sure you can talk to a stranger all by yourself?"
   show mc surprised
   m "..."
   show mc worried
   m "(Damn, I didn't think that far...)"
   m "It'll be fine. Probably..."
   show alice neutral
   ali "If you say so."
   show black with dissolve
   #insert awkward purchasing
   hide black with dissolve
   show mc vstressed
   m "Ugh... That went a-about as expected"
   show alice smirk
   ali "So you pissed yourself and the staff had to clean it up in front of you?"
   show mc annoyed
   "You hold up the string packet triumphantly"
   m "There, I did it! See! I c-can do it if I try!"
   show alice sigh
   ali "Your voice is still trembling though..."
   show mc stressed
   m "Whatever!"
   show mc normal
   m "Since we're here we might as well have a proper look around."
   show mc surprised
   m "Look, there's a second floor where you can try guitars out with an amp"
   show alice normalside
   ali "It's fine, I should go home and practice anyway..."
   show mc confused
   m "We came out all this way, you might as well try some different ones and see if there's any you like."
   show mc happy
   m "Plus, you can always try play what you've been working on here"
   show alice sulk
   ali "I guess you're right..."
   hide mc
   hide alice
   with easeoutbottom
   "You leave alice to try out some guitars while you watch"
   #maybe you take the phone call here and she's still on the guitar when you get back
   "She tries out a couple of different ones, but never for more than a couple seconds, before she unplugs it, it puts it up on the hanger"
   "Until..."
   show alice surprised at center with easeinbottom
   ali "This one is... different?"
   m "Really? It just looks like a different color to that other one you were just playing to me."
   show alice pout
   ali "But it feels completely different!"
   m "If you say so..."
   hide alice with easeoutbottom
   "After a few minutes pass she eventually unplugs it, and tries a couple others"
   "But it's obvious that none of them interest her as much"
   show mc normal at center with easeinbottom
   "You take a look at the price of the one she was eyeballing"
   "Fender Custom Shop 2022 Fall Event LTD 1960 Telecaster Journeyman Relic Aged Magenta Sparkle"
   "And the price is..."
   show mc shocked at bounce
   m "!"
   "If you bought it, you would be eating instant noodles every day for the next 2 months"
   "Which I guess isn't any different than how you live anyway"
   show mc stressed
   "But, she's only has today left..."
   "Maybe if I returned it after tomorrow and got a refund?"
   show mc vstressed
   "... Nah, that's way too scummy"
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
   show alice shocked at bounce
   ali "!"
   m "Damn kids these days are crazy huh?"
   show alice cutesad
   ali "..."
   "You see her scrunch up her brow and turn her gaze towards the floor"
   show mc normal
   m "Let's go, you've got a lot of work to do right?"
   ali "Yeah..."
   stop music fadeout 2
   window hide
   scene black with fade
   scene enbankment with fade
   show mc normal at right
   show alice sad at left
   "The 2 of you walk along the river bank towards your dorm"
   "When suddenly- "
   stop sound
   play music "heaven.mp3"
   show alice surprised at bounce
   show mc shocked at bounce
   m "Oh shit!"
   "You're not used to the sound of your ringtone"
   show alice normalside
   show mc surprised
   m "Dad..."
   show mc stressed
   m "Ugh..."
   show mc normalside
   m "I could just message him some excuse and let it ring out..."
   # make it more clear why he doesn't want to pickup
   m "Or..."

   menu:
      "What should I do?"
      "Make an excuse(N/A).":
         "..."
         return
      "Accept the call.":
         show mc stressed
         m "Hey, uh... I need to go take this."
         hide alice with dissolve
         "Alice nods and sits on a near by bench along the riverbank"
         show mc at center with move
         jump day2PhoneCall

label day2PhoneCall:

   stop music
   stop sound
   play sound "windgust.wav"
   play music "wind.wav"

   dad "Hello?"
   show mc stressed
   m "Hey dad... How's it going?"
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
   dad "You finally got yourself a girlfriend?"
   show mc confused
   m "Huh?!"
   dad "I mean that's the only thing I can think of."
   dad "You're not one of {i}those{/i} people to go buying stuff from women's stores for yourself"
   m "..."
   show mc awkwardsmile
   m "Uh, yeah, haha..."
   m"... Of course not"
   dad "When I was your age, I was plowing through some pusssy! I get it. Just as long as you keep up with your studies."
   dad "So you're going to introduce me sometime right?"
   m "Uhh."
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
   m "..."
   show mc at right with move
   show alice sad at left with dissolve
   "You turn back to find Alice"
   "To find her kneeling beside some flowers on the grass"
   "She's watching a butterfly perched on a white daisy."
   show alice normal
   m "Hey, sorry about that... Let's go"
   show alice worried
   ali "Are you okay? You seem kinda off."
   show mc normalside
   m "Yeah, it's nothing..."
   show alice normalside
   ali "Okay... If you say so..."
   "She stands up slowly and you resume your walk back home."
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
   scene afternoon_clouds
   show bedroom_opencurtains:
      matrixcolor TintMatrix("#f4ca9a")
   show dirty1:
      matrixcolor TintMatrix("#f4ca9a")
   show dirty2:
      matrixcolor TintMatrix("#f4ca9a")
   show bottle:
      matrixcolor TintMatrix("#f4ca9a")
   with Dissolve(2)
   show day_3 at topleft
   show alice_affection at topright
   with dissolve
   play sound "door.wav"
   play music "night.mp3"
   show mc normal at right
   show alice serious at left
   with easeinbottom
   a "!"
   hide alice with easeoutbottom
   show mc surprised
   # show her rushing back thorugh door as you get back
   m "Damn you really aren't wasting a second huh?"
   ali "..."
   show mc stressed at center with move
   m "*Sigh*"
   m "We still have a couple hours, since the show is only in the evening"
   m "I guess I'll try read some manga on my phone or something"
   window hide
   show black with dissolve
   window show
   "The first hour is fine enough..."
   "You can't focus on reading, over the sound of the same guitar phrases repeated over and over"
   "But it's fine..."
   "Another hour rolls by..."
   # Tense is inconsistent
   "And she hasn't so much as looked in your direction."
   stop music fadeout 6

   m "..."
   "Another hour..."
   play sound "guitar_note.wav"
   "The sound of the guitar drills its way further into your brain."
   play sound "<from 0 to 1>guitar_note.wav" loop
   "Echoing though your skull and through your ears"
   play sound "guitar_note.wav" noloop
   hide mc
   show mc stressed with dissolve
   "A wave of nausea hits you."

   "You stand up, suddenly feeling restless"
   "You don't know exactly why"
   "But you don't want to be here right now"
   "You can't be here right now"
   "With her..."
   "It's her last day... but she hasn't even spoken a word to you"
   "After all you've done for her"
   show mc vstressed
   "Your stomach feels like you've swallowed a brick"
   "You say it over and over in your head"
   #"..."
   "\"Shut the fuck up\""
   #"..."
   "You've been annoyed since the call earlier"
   "But you thought you could put on a smile for her"
   "On her last day"
   hide black with dissolve
   show mc vannoyed
   "You look over to her"
   "She's staring at the fretboard"
   m "..."
   show mc at quiver
   "You don't know what's going to come out, but you brace yourself"
   window hide
   show black

   show text "Say something!"
   $ renpy.pause ()
   show text "Anything!"
   $ renpy.pause ()
   hide text
   hide black
   window show
   m "..."
   show mc stressed
   m "Hey, do you mind like... Taking a break? For my sanity?"
   ali "..."
   hide mc
   show mc shout at center
   show mc at bounce
   m "Hey I'm talking to you!"
   ali "..."
   show mc vannoyed
   "You walk over to her and..."
   play sound "unplug_guitar.wav"
   show alice shocked at left
   show mc at right with move
   show mc vshout
   m "Stop it already! You've been playing the whole day!"
   ali "!"
   m "I'm trying to support you here, but I just can't take it anymore"
   show alice annoyed
   ali "Hey what the fuck? I'm busy!"
   show mc vshout
   m "I go through all the effort to set up all this stuff for you, and you..."
   show alice serious
   ali "And I what?"
   ali "Use it?"
   show alice annoyed
   ali "Sorry for existing I guess."
   show mc vannoyed
   m "You don't get it..."
   m "This is our last day together and you're just wasting it on this"
   m "Who cares if you win or not? Why do you care so much about this stupid competition?!"
   show mc stressed
   m "None of this shit matters!"
   m "I thought the whole point of this was to not try to please anyone else"
   m "But you're just going from an insecurity that was imposed on you to one you chose"
   ali "..."
   show alice sulk
   ali "..."
   show mc confused
   ali "..."
   # Forced wait for 3 seconds so like . wait . wait ."
   # but her expression changes
   "Clutching the guitar towards her chest, Alice stands up, and walks towards the door."
   show mc normalsquint
   m "Where are you going?!"
   ali "..."
   # ali "Somewhere I can focus without you"
   hide alice with easeoutbottom
   play sound "door.wav"
   show mc surprised
   m "!"
   show mc at center with move
   m "She's gone..."
   show mc normal
   m "..."
   show mc vstressed
   m "Fuck..."
   m "What's wrong with me?"

   m "I've gotta go find her"
   default looked_river = False
   default looked_mall = False
   menu:
      "Where do I look?"
      "The mall":
         #"..."
         scene mall with fade
         $ looked_mall = True
      "The river bank":
         #"..."
         scene enbankment with fade
         $ looked_river = True
   # ORder doesn't matter but gives scenery to go past as you have the internal dialogue
   play music "trip.mp3"
   # switch nvl?
   "Hey... You did it again!"
   "If there was a prize for making girls cry, you would be a shoe in"
   "The dis-noble prize"
   "This is how it always is though"
   "Every friendship or acquintance"
   "Every classmate and every crush"
   "Without fail, you always find the best way to push all of them away from you"
   "But honestly..."
   "Did you really expect anything different?"
   "No... In fact..."
   "I can say without a shadow of doubt..."
   "This is what you wanted to happen."

   m "I don't see her anywhere..."
   m "Fuck where else could she be?"
   menu:
      "Where else do I look?"
      "The mall" if looked_mall == False:
         scene mall with fade
         #"..."
      "The river bank" if looked_river == False:
         scene enbankment with fade
         #"..."

   "All of this 'helping her' and 'trying to grant her last wishes'"
   "You're just trying to convince yourself that you are a good person"
   "But if that were true you wouldn't be so alone in the first place"
   "You were jealous of her from the very beginning"
   "The way that she could say what she really felt"
   "How she could do more than you've ever accomplished in less than a fraction of a percent of the time you've been alive"
   "How she knows who she is..."
   # ("How she dressed, or how she looked"?)
   "That's how you really feel!"
   "But that's okay!"
   "We are happier this way!"
   "Just you and I..."
   "Forever..."
   m "..."
   "Besides, why do you care so much-"
   m "I-"
   "About some bitch who is going to die in a few hours anyway?"
   m "I'm not like that!"
   m "I'm not who you-"
   m "Who I think I am..."
   m "I've got to go find her..."
   # Show running out into the hall
   m "Fuck she could be anywhere..."
   m "Where would she go in a time like this?"
   "You think back to the first night where Alice ran off by herself"
   "How she felt then"
   m "..."
   m "I think I know where she is"
   window hide
   #scene trans
   #play sound foodsteps and heartbeat
   scene hallway with fade
   pause
   scene rooftop with fade
   show alice cutesad at left with dissolve
   play sound "door.wav"
   show mc surprised at right with easeinbottom
   window show
   m "Alice!"
   jump rooftop_reworked

label rooftop_reworked:
   # he goes up to roof sweaty
   # starts trying to apologise

   m "Alice!"
   show mc confused
   m "I- *pant* I- "
   m "I wanna say that I'm-"

   # is interrupted by alice somberly talking at him about butterfly
   show alice sad
   ali "You know..."
   ali "Since we went out yesterday..."
   ali "I've been thinking a lot about butterflies..."
   show mc awed
   m "?"
   "You look down at her sitting on the floor, and notice a large red butterfly on her fingertip"
   show alice think
   ali "When we went to the cafe... At first I was really surprised when the waiter brought me that butterfly art"
   ali "And I thought about what it might mean"
   ali "Maybe I'm just overthinking it, and he just went of of vibes but..."
   ali "Maybe there was a reason that he chose that."
   show alice sulk
   ali "And so I thought really hard about it..."
   ali "And after you went to sleep, I took a break from practicing to do a little research"
   show alice normal
   ali "You know... Butterflies aren't that different to me..."
   show alice sadsmile
   ali "They're really pretty..."
   ali "But it doesn't last that long..."
   ali "After they come out of their cacoon, they only have X days to live..."
   ali "To breed and be attractive enough to breed and to leave any sort of lasting legacy"
   show alice think
   ali "To have any proof that they existed at all..."
   ali "So I see myself in them"
   show alice sad
   ali "And they made me think a lot about myself..."
   ali "My life..."
   show alice cutesad
   ali "I want my life to mean something... Anything..."
   ali "To be remembered as a person that did something"
   ali "And not just a pretty butterfly that's gone with the wind"
   ali "But I'm still scared..."
   show alice worried
   ali "I'm scared that no matter what I do"
   ali "Even if I could change the entire world"
   ali "It wouldn't change that I feel like I do"
   show alice serious
   ali "So I'm sorry"
   ali "I'm sorry for losing sight of you, and for pushing you away"
   show alice sad
   ali "It's just hard you know..."
   ali "The time we have is limited, and in the moment, it's easy to tell yourself that what you're focused on is the most important thing in the world"
   ali "I just have this one chance..."
   show alice cry
   ali "To feel like I accomplished something"
   ali "But I didn't want to push you away"
   ali "I should have treasured the time I have with you more..."
   show alice think
   ali "This butterfly over here..."
   ali "It's dead..."
   ali "Because of me..."

   ali "I just wanted to touch it, so when it flew over to me"
   show alice sadsmile
   ali "But I'm toxic..."

   #ali "You know the fly in fly aminita comes from the fact that they used to use us to kill flies by putting us in milk"
   show alice cry
   ali "It's like... Why do I have to be like this?"
   ali "Why do I hurt everyone around me just by existing?"
   ali "I just *sob*"
   show mc confused
   m "You know..."
   m "I don't think you picked music because you wanted to be the best, or win the competition..."
   show mc cute
   m "I think it's because you saw something that spoke to you"
   m "And maybe that's all that matters..."
   m "But even so..."
   show mc normal
   m "You've been playing guitar for a couple of hours..."
   show mc annoyed
   m "And you're already better at it than I've ever been at anything"
   show mc cute
   m "You're amazing, and I don't think you know how much you are..."
   show mc normalside
   m "I was thinking about how I lashed out earlier and..."
   show mc sad
   m "I think... I'm jealous of you"
   m "Of your talent"
   m "Of your looks"
   m "Of everything about you"
   m "And I know maybe it's selfish for me to say that but"
   show mc stressed
   m "I just wanted to spend a bit more time with you before you..."

   # I think it's important that he says this at some point but the timing feels bad here
   show mc worried
   show alice worried
   m "Damn I'm fucking pathetic..."
   m "I have so much time compared to you, but I still haven't accomplished a thing."
   show mc slightsad
   m "I tell my self I'll learn to draw."
   m "Or learn an instrument."
   show mc shout
   m "Or fucking anything."
   m "But I'm still just wasting time everyday"
   m "Telling myself it will all work itself out"
   m "That tomorrow, someone will push me towards living the life I want to..."
   m "For an excuse..."
   m "I'm just scared it won't work out, or people will judge me..."
   # Unused stuff to pull from

      # ali "Well then you're back where you started."
      # ali "And you can find another reason to live"
      # ali "Humans are good at that"
      # show alice happy
      # ali "So I guess in the meantime, all you can do is find a waste of time that feels special to you"
      # ...
   show mc sad
   m "I just want to like myself."
   m "But even then..."
   m "I know it will never be enough"
   m "Even if I tried to like myself it wouldn't be enough for my parents"
   show mc slightsad
   m "Because all they want me to be is the person they THINK I am"
   show mc vannoyed
   m "But I CAN'T be that person!!"
   m "I've never been that person..."
   show alice normal
   ali "..."

   show mc normalside
   m "They think I'm a straight A student, with lots of friends."
   m "My dad is making up fantasies of me having a girlfriend and living up to how he was in college"
   m "I don't even know what he would do if he found out"
   show mc normal
   m "Who I {i}actually{/i} am"
   show mc stressed
   m "That I'm on the verge of flunking out"
   m "That I have no friends"
   m "That I'm not like him..."
   show mc sulk
   m "I just feel like..."
   m "Time keeps moving..."
   m "And I'm still alone... Here... In my room."
   m "But I can't stay in college for ever."
   m "I'm going to drop out or scrape through."
   m "And then I'm going to work doing some crappy deskjob I hate, until I get old..."
   m "And then I die."
   show mc sad
   m "I'm sorry, I came to apologize and I just ended up talking at you..."
   show alice sulk
   ali "No, it's okay"
   show alice normal
   ali "I feel like now we both understand each other a little bit better"
   ali "I guess... Maybe it's okay if I..."
   show alice sadsmile
   ali "...if I'm not perfect"
   show mc confused
   ali "Or enough..."
   ali "Just existing, and experiencing..."
   show alice normal
   ali "Hey..."
   ali "I know it doesn't make up for earlier but..."
   ali "I still want to do this show, and I was just wondering if maybe"
   show alice happy
   ali "You'd wanna help me with the finishing touches?"
   show mc surprised
   m "!"
   #show mc embaressed
   m "Uh, yeah... No problem"
   stop music fadeout 2


   jump preshow
label preshow:
   play music "mall.mp3"
   scene music_club with fade
   show mc normal at right
   show alice worried at left
   with easeinbottom

   m "Okay, we're here"
   ali "..."
   m "Now just to sign up over here and-"
   ali "Can we go home?"
   m "Huh?!"
   show alice sad
   ali "I've changed my mind..."
   ali "I don't think I can..."
   show mc confused
   m "Don't be ridiculous! You've worked so hard!"
   ali "But-"
   show mc happy
   m "Hey, you've got this"
   m "And even if you fuck up... At least you commited and did something most people will never do in their lives"
   show alice sigh
   ali "Okay..."
   show alice normal
   ali "Fuck it..."
   "She takes the pen in her hand with great enthusiasm and vigor and-"
   ali "..."
   ali "Can you sign up for me?"
   show mc confused
   m "Huh? Why?"
   show alice disappointed
   ali "I can't write remember?"
   show mc normalside
   m "Oh yeah... Forgot about that..."
   "*Skribble Skrabble*"
   m "There we go... Now just to go inside and wait until you've gotta go backstage."
   hide alice with dissolve
   show kellin happy at left
   with easeinbottom
   #kel "And then you should have seen her face when-"
   show kellin vhappy
   show mc shocked
   kel "(MC name)? What the hell!"
   kel "You should have told me you were gunna come down here!"
   kel "This is like my stomping ground!"
   kel "I've gotta introduce you to-"
   show alice normal at left with easeinbottom
   show kellin shocked at bounce
   kel "!"
   show kellin at right with move
   show kellin shocked at flip
   show mc surprised at center with move
   kel "It's her!"
   show alice confused
   show mc confused
   m "?"
   show kellin awkward at flip
   kel "I'm sorry, I gotta go..."
   kel "I'll catch you later..."
   hide kellin with dissolve
   show alice sad
   show mc at right with move
   ali "..."
   m "What the fuck was that?"
   m "Why did he recognize you?"
   ali "You remember how when we first met..."
   ali "And I ran away to the shower room?"
   m "..."
   show mc shocked
   m "Wait! HE was the guy from back then?!"
   ali "Yeah..."
   show mc stressed
   m "Holy shit, that's so awkward..."
   m "I've gotta apologize to him later"
   show mc normalside
   #m "Anyway let's head inside..."
   window hide
   hide mc
   hide alice
   with easeoutbottom
   jump aliceDay3Show

label aliceDay3Show:
   window show
   "You wait with Alice nervously in the venue"
   "You see several groups happily drinking beer and laughing"
   "The first couple of performers come out and the atmosphere of the place changes"
   "You watch them together"
   "But you can't help but feel like you are watching 'A performance'"
   "Something you see on youtube or TV"
   "It doesn't feel real"
   "Real people who practiced and whose legs were shaking as they sung"
   "Until"
   show alice cutesad at left with dissolve
   ali "I think it's time..."
   show mc awed at right with dissolve
   m "Oh yeah! You should get backstage"
   ali "..."
   show mc normal
   m "Hey! Just one thing before you go"
   m "..."
   show mc annoyed
   m "I just want to remind you that no matter how it goes"
   m "That I'm really proud of you"
   show alice normalside
   ali "Thanks... I-"
   ali "I gotta go!"
   hide alice with easeoutbottom
   "And with that she turned her back and started walking towards the stage door"
   scene music_stage with dissolve
   stop music fadeout 3

   announcer "Okay ladies and gentlemen, and those in between..."
   announcer "Next up I want you all to give a warm welcome to~"
   announcer "Alice!"
   show alice flirtsweat with dissolve
   ali "Uh- Hi there..."
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
   show alice confused
   ali "I uh- haven't really prepared anything but uh..."
   show alice think
   ali "I guess the last few day have been a really chaotic time for me..."
   ali "There where times I felt like everything was meaningless, but I had someone with me to help me through that"
   ali "And I wouldn't be up here with out them."
   show alice normal
   ali "This song is called \"Metamorphisis\"."
   #play song fail

   # Maybe using dynamic audio and vamps to get the song to progress as the user clicks?
   "Alice starts playing the melodies I had heard so many times at this point"
   "But this time it felt different"
   "Knowing how much she put into it to get here..."
   "She opens her mouth to start singing and-"
   "Her voice awkwardly pops out and cracks part way through the second word"
   show alice shocked
   "Panic runs across her face and her hands freeze"
   "An awkward silence runs across the room"
   "..."
   "Then, she looks through the audience"
   "Until her eyes land on me"
   show alice cute
   ali "I guess I focused so much on the guitar that I forgot to practice singing!"
   ali "Hahaha..."
   show alice sigh
   ali "Let's try that again!"
   "She starts the song again from the beginning, but this time, when the verse starts"
   ali "*first lyric line*"
   "She talks over the music as if talking to herself"
   ali "*lyrics*..."
   # Lyrics go here ->
   play sound "yay.wav"
   show alice happy
   "She looks up to me and smiles"
   announcer "Let's give it up one more time for Alice!"
   announcer "Okay! Next up we have..."
   jump post_show

label post_show:
   scene alley with fade
   m "Alice!"
   show alice cutesad at center with easeinbottom
   "You see her walk out from the backstage door, but waiting there for her is-"
   show kellin happy at left
   with dissolve
   kel "Hey Alice!"
   show alice shocked at flip
   ali "?!"
   "You walk over to try to get between them but before you get there-"
   show kellin awkward
   kel "I'm so sorry!"
   ali "?!"
   kel "At first I hated you, because of what happened the other day."
   show kellin shocked
   kel "But after hearing you song!"
   kel "I completely understand now!"
   show kellin vhappy
   kel "It must have been some weird misunderstanding right?!"
   ali "Ah... Ummmm"
   kel "You were so good! I really loved the way you did the- (Here put in technical aspects from the actual song)"
   show mc awed at right
   m "Alice!"
   kel "(mc name)! I thought you were going to use that guitar to learn for yourself!"
   kel "Why didn't you tell me that-"
   show mc worried
   m "Yeah, I'm sorry. I should have told you that-"
   kel "If you told me it was for a girl with such small hands, I would have lent you a guitar with a smaller neck!"
   kel "I bet it was hard to play!"
   show alice surprised at flip
   ali "Wait you're the neighbour we're borrowing from?!"
   m "Yeah..."
   show alice laugh
   ali "Thank you so much! I wouldn't have been able to do this tonight if you didn't-"
   show kellin normal
   kel "If you wanna say thanks, I know the perfect way..."
   show mc confused
   m "You don't mean..."
   kel "You'll have to pay by..."
   show alice normalside
   ali "*gulp*"
   show kellin vhappy
   kel "Letting me take a group Polaroid of us!"
   show alice surprised
   ali "Huh?"
   show mc surprised
   m "Woah it's one of those old cameras..."
   m "Where did you get that?"
   show kellin happy
   kel "I ordered it second hand online for super cheap! Hahaha"
   show kellin vhappy
   kel "Ready or not! Cheese!"

   play sound "polaroid.wav"
   show white with dissolve
   hide white with dissolve

   show alice shocked at bounce
   ali "!"
   show mc cute
   m "Are you okay? The flash must have been pretty suprising huh?"
   show alice normalside
   ali "Yeah... I'm fine...I was just-"

   #play sound notice
   # Maybe kellins friend should rush from inside to let them know
   announcer "Okay, it's time to announce today's winner!"
   show mc shocked
   m "We should hurry back inside!"
   scene music_stage with fade

   show alice surprised at center
   show kellin normal at left
   show mc awed at right
   with dissolve

   announcer "And!"
   announcer "Today's winner!"
   announcer "Who will have the luxury of recording a single at (insert funny names) studios for completely free!"
   announcer "IS~"
   ali "*gulp*"
   announcer "..."
   announcer "VICIOUS FISH!!!"

   play sound "yay.wav"
   play music "mall.mp3"
   show mc sad
   m "Alice, I'm so-"
   show alice laugh
   ali "Heheh, such a weird band name."
   show mc confused
   m "?!"
   m "Are you okay?"
   show alice cruel
   ali "Yeah? What you thought I was gunna cry if I lost?"
   show alice neutral
   ali "Plus what am I gunna do with the prize of recording a single after I'm gone?"
   show kellin awkward
   kel "Are you going somewhere?"
   show mc worried
   m "?!"
   show alice think
   show mc normal
   ali "Uh... Yeah... I'm going abroad."
   show kellin vhappy
   kel "Oh that's awesome! But kinda a shame..."
   show kellin happy
   kel "We were just missing a rhythm guitarist and I was gunna ask if you could fill in..."
   kel "ANYWAY!"
   kel "When are you leaving?"
   show alice normalside
   ali "..."
   ali "Tonight..."
   show kellin shocked
   kel "Oh that's crazy!"
   show kellin normal
   kel "Do you need a ride to the airport?"
   kel "My friend has a big car, so we could-"
   show alice flirtsweat
   ali "No it's okay!"
   show alice normal
   ali "Thanks for offering."
   ali "Anyways! It's getting pretty late..."
   ali "We should head back so I can get ready"
   show kellin awkward
   kel "Aww, I was hoping we could talk about music!"
   show alice happy
   ali "I'm sure we'll get that chance next time..."
   show kellin happy
   kel "Yeah, I'm looking forward to it!"
   kel "Oh yeah... It should be ready by now."
   show alice surprised
   ali "Huh? This is..."
   kel "This is the photo I took earlier!"
   kel "I thought it might be something nice for you to remember us by..."
   show alice cutesad
   ali "Wow, this is so pretty... Is it really okay if-"
   show kellin vhappy
   kel "Of course! I bought it for this sort of thing anyway!"
   kel "Anyway, sorry to stop you from going home."
   show alice happy
   ali "No it's okay! Thanks."
   ali "You enjoy the rest of the night!"
   kel "Yeah you too- stay safe!"
   show mc happy
   m "We will do. I'll look after her!"
   #m+ali "Later~"
   scene black with fade
   stop music fadeout 2
   jump aliceDay3WayBackHome

label aliceDay3WayBackHome:
   "The two of you walk back towards your dormitory."
   "You walk together in silence until you reach the road leading up to your dormitory."
   "Alice's pace grinds to a halt."

   scene outside_dorm with fade
   play music "trip.mp3"
   ali "..."
   show mc awed at right with easeinbottom
   m "Hey, are you okay?"
   show alice sad at left with easeinbottom
   ali "Yeah... I mean..."
   ali "I don't know."
   ali "It's just that it's all over you know..."
   ali "I know I'm supposed to feel okay now"
   ali "Like this life was enough like this"
   ali "And like... I do feel like I accomplished something"
   ali "And make memories with you..."
   show alice think
   ali "But even still... This is it huh..."
   show mc cute
   m "We still have time! Maybe if we wait til tommorow we'll find that you-"
   show alice serious
   ali "Stop."
   ali "I know that it's time"
   show alice cutesad
   ali "I can feel it."
   show alice sad
   m "..."
   show alice happy
   ali "Tonight was fun!"
   ali "Kellin was really nice... He seemed like he really loves music."
   show mc normalside
   m "Yeah... And he didn't even ask if we are dating or anything."
   show alice smug
   ali "Haha, why's that the first thing you say?"
   show mc awkwardsmile
   m "I don't know."
   show mc slightsad
   m "I guess he's just not like some other people I know."
   show alice normal
   ali "Hmm~"

   "She starts walking again slowly and you follow her pace"
   ali "Don't you wish you'd reached out to him earlier?"
   show mc normal
   m "..."
   show mc normalside
   m "I don't think I could have... Even now..."
   show mc worried
   m "It's still scary to know that if I say the wrong thing he might never want to talk to me again"
   show alice disappointed
   ali "Stop being so dramatic!"
   ali "Not everything is life or death..."
   show alice laugh
   ali "Unless your me that is! Haha"
   show alice happy
   ali "But even if you fuck up a little, I think you could just apologize"
   show mc stressed
   m "Maybe..."
   m "Hey, I wanted to say..."
   m "About the song you wrote."
   show mc awed
   m "Thanks..."
   m "It meant a lot..."
   show alice shocked
   ali "What are you talking about!"
   show alice flirtsweat
   ali "Those l-lyrics didn't mean anything!"
   ali "Idiot!"
   show mc confused
   m "?!"
   show alice hime
   ali "Don't get me wrong!"
   ali "I just made them up to go with the melody!"
   show mc surprised
   m "Real Tsundere?!"
   show alice neutral
   ali "Huh? What does that mean?"
   show mc annoyed
   m "Nothing..."
   show mc happy
   m "You really worked hard for today, and I'm really proud of you"
   show alice think
   ali "...Thanks."

   ali "Hey... I just thought you should know..."
   show mc normal
   # ali "Even though I'm poisonous..."
   # ali "There's a way you can prepare me so that I'm edible"
   # ali "And even if you screw up a little, no one had died eating from eating a fly aminitas in over a hundred years."
   # m "Eat you?"
   # m "What?"
   # m "Why-
   # m "Why would I do something like that?"
   # ali "I want you to... It's the last "
   show alice normal
   ali "I really appreciate what you did for me."
   ali "Even though it was hard at first."
   show alice happy
   show mc blushside
   ali "I'm glad that this is the way things turned out."
   show alice sad
   ali "..."
   ali "I'm going to go for a walk tonight."
   ali "By myself."
   ali "So don't come looking for me."
   show mc shocked
   m "But I want to be with you when-"
   show alice serious
   ali "Please. I want for you to remember me for the time we spent together."
   ali "Not for how I left"
   show mc awed
   m "..."
   show mc sad
   m "Okay."
   show alice sulk
   ali "...Sorry... Or I guess"
   show alice normal
   ali "Thank you"
   stop music fadeout 2

   jump aliceDay3Goodbyes

label aliceDay3Goodbyes:
   scene black with fade
   scene night_clouds
   show bedroom_opencurtains:
      matrixcolor TintMatrix("#6F6FBB")
   show dirty1:
      matrixcolor TintMatrix("#6F6FBB")
   show dirty2:
      matrixcolor TintMatrix("#6F6FBB")
   show bottle:
      matrixcolor TintMatrix("#6F6FBB")
   with Dissolve(2)
   play music "night.mp3"

   show day_3 at topleft
   show alice_affection at topright
   with dissolve

   play sound "door.wav"
   show alice sigh at left
   show mc sad at right
   with easeinbottom

   ali "Home sweet home!"
   ali "Aaah! I'm so tired..."
   m "I bet..."
   m "..."
   show mc vstressed
   "You stand there for a few moments not knowing what to say..."
   "You don't feel equiped for dealing with situations like this."
   show alice normal
   ali "Do you want to watch a movie or something?"
   show mc surprised
   m "Huh?"
   ali "Do you like comedy or are you into something like horror?"
   show mc confused
   m "Comedy but..."
   show alice normalside
   ali "Yeah, that tracks..."
   m "Are you sure you are fine with just watching a movie?"
   m "Isn't there anything else you'd rather do?"
   show alice normal
   ali "..."
   ali "No..."
   show alice happy
   ali "I just want normal..."
   ali "That's already special enough for me."
   show mc slightsad
   m "If you're sure..."


   show black with dissolve

   "You watch a random romantic comedy movie from Netflix together on your bed."
   "She laughs at the stupid jokes, and tears up for the climax."
   "And before you know it..."
   stop music fadeout 2
   show mc stressed
   show alice laugh
   hide black with dissolve
   m "Ahhh... I guess it's over."
   ali "Yeah. That kind of sucked hahaha..."
   show mc cute
   m "Well you seemed to be enjoying it"
   show alice happy
   ali "Yeah I did. Thanks to you..."
#  Insert more dialog here
   show alice normal
   ali "Hey..."
   show mc normal
   ali "It's kinda getting late..."
   show alice normalside
   ali "I should probably head out for my... walk..."
   show mc slightsad
   m "..."
   show mc sad
   m "So I guess... This is..."
   show alice sad
   ali "Yeah... This is it."
   "She stands up and hovers around the general vicinity of the door"
   show alice sigh
   ali "I don't really know what I'm supposed to say here"
   show alice normalside
   ali "I could do a long speech about everything I've learned with you..."
   show alice happy
   ali "But I think it's better if I do this."
   window hide

   show alice_kiss with dissolve
   play music "date_musicbox.mp3"
   pause 1
   window show
   ali "You've got a lot of life left."
   ali "So enjoy it enough for both of us"
   ali "Okay?"
   m "Yeah..."
   "Your lip starts trembling as tears well in your eyes"
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

   hide alice with easeoutbottom
   play sound "door.wav"
   #"She turns away and closes the door firmly behind her."
   show mc vcry
   window show
   m "Alice..."
   show mc
   m "..."
   stop music fadeout 3
   window hide
   scene black with fade
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

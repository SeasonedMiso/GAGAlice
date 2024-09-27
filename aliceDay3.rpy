#[here i think the bg music when she's practicing should be the song she's writing, but at various levels of playing: think wa2]
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
"You can't hear her that well over the rumbling of water being heated."
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
"You can't help but be impressed by her"
"But you also feel a bit..."
"..."
#Maybe leave this just as an incomplete sentence
screen trans
# maybe slurping sound
m "Okay I'm alive now"
ali "*strum* *strum*"
m "Are you ready to go to the guitar store?"
ali '*pickedy* *pick*'
"She can't hear you again"
"You walk over to her and slowly wave your hand in front of her vision"
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
m "Hey, I'm kind of worried about you"
m "You've been grinding non-stop for the entire night"
m "Please, come with me"
ali "Ugh, fine~"
 scene trans

#What do they talk about on the way?
"The two of you walk together towards the music store."
"You walk a little ahead of her, and she follows your back"
"You get worried that she's lost sight of you, or got lost somewhere along the way"
"So you check over your shoulder every few minutes, but she's always right behind you"
"Walking lazily, yet somewhat annoyed."

label day3Store:
play sound shop bells
scene mall with fade
ali "!"
ali "Woah this place is crazy"
m "Yeah... There's all sorts of stuff"
#Maybe drag this out and make it more like "why does that one have a birth defect?"
ali "Why is there like... a conjoined twin guitar?"
m "I have no idea."
m "I'm going to go get the strings"
m "You can have a look around in the meanwhile if you want"
#Maybe it's better that she points it out only afterwards?
ali "Are you sure you can talk to a strager all by yourself?"
m ("Damn, I didn't think that far...")
m "It'll be fine! Probably..."
ali "If you say so."
 screen trans
 #insert awkward purchasing
 screen trans
m "Ugh... That went a-about as expected"
ali "So you pissed yourself and the staff had to clean it up in front of you?"
"You hold up the string packet triumphantly"
m "There, I did it! See! I c-can do it if I try!"
ali "Your voice is still trembling though..."
m "Whatever!"
m "Since we're here we might as well have a proper look around"
m "Look, there's a second floor where you can try them out with an amp"
ali "It's fine, I should go home and practice anyway..."
m "Look, we came out all this way, you might as well try some different guitars and see if theres any you like"
m "Plus, you can always try play what you've been working on here"
ali "I guess you're right..."
 screen trans
"You leave alice to try out some guitars while you watch"
#maybe you take the phone call here and she's still on the guitar when you get back
"She tries out a couple of different ones, but never for more than a couple seconds, before she unplugs it, it puts it up on the hanger"
"Until..."
ali "This one is... different?"
m "Really? It just looks like a different color to that other one you were just playing to me."
ali "But it feels completely different!"
m "If you say so..."
"After a few minutes pass she eventually unplugs it, and tries a couple others"
"But it's obvious that none of them interest her as much"
"You take a look at the price of the one she was eyeballing"
"Fender Custom Shop 2022 Fall Event LTD 1960 Telecaster Journeyman Relic Aged Magenta Sparkle"
"And the price is..."
m "!"
m "..."
"If you bought it, you would be eating instant noodles every day for the next 2 months"
"Which I guess isn't any different than how you live anyway"
"But, she's only has today left..."
"Maybe if I returned it after tomorrow and got a refund?"
"... Nah, that's way too scummy"
m "Okay, we should probably get going"
ali "...Okay..."
"She takes a last look at that guitar, and slowly gets up."
"As she does a young boy with 2 older adults (probably his parents) takes a seat at the amp on the other side of the floor"
"He plugs in the guitar his parents place on his lap for him to try and..."
play sound shred
ali "!"
m "Damn kids these days are crazy huh?"
ali "..."
"You see her scrunch up her brow and turn her gaze towards the floor"
m "Let's go, you've got a lot of work to do right?"
ali "Yeah..."
scene trans
"The 2 of you walk along the river bank towards your dorm"
"When suddenly- "
play sound rintone
m "Oh shit!"
"You're not used to the sound of your ringtone"
m "Dad..."
m "Ugh..."
m "I could just message him some excuse and let it ring out..."
# make it more clear why he doesn't want to pickup
m "Or...?"

   menu:
      "What should I do?"
      "Make an excuse(N/A).":
         "..."
      "Accept the call.":
         show mc stressed
         m "Hey, uh... I need to go make a phone call."
         "Alice nods and sits on a near by bench along the riverbank"
         jump day2PhoneCall

label day2PhoneCall:
   scene black with fade
   play music "wind.wav"
   "You tap the accept call button"
   stop sound
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
   m "..."
   "You turn back to find Alice"
   "To find her kneeling beside some flowers on the grass"
   "She's watching a butterfly perched on a white daisy."
   m "Hey, sorry about that... Let's go"
   ali "Are you okay? You seem kinda off."
   m "Yeah, it's nothing..."
   ali "Okay... If you say so..."
   "She stands up slowly and you resume your walk back home"

#   For "The snapping point", I think his self-doubt about how quickly she's improved at guitar could be better portrayed:
#   instead of saying it all from the POV of why this is hard for him (which is too obviously self-focused + annoys me),
#   he can phrase it as a frustrated encouragment, trying to get her to see why everything is okay and she can stop stressing and be proud of all she has done instead.
#   For example, "Why are you so upset/stressed/afraid? Stop putting yourself down - don't you know how much I look up to you? You've worked so hard, you've learned so much,
#   and what I can sounds better than anything I could do. You've accomplished more than I ever have!"
#   This way MC's self-hate is more backhanded AND it shows how their relationship has grown to the point that
#   he is genuinely worried about her and wants her to see how HE sees her.

preFightDay3:
   # show her rushing back thorugh door as you get back
   m "Damn you really aren't wasting a second huh?"
   ali "..."
   m "*Sigh*"
   m "We still have a couple hours, since the show is only in the evening"
   m "I guess I'll try read some manga on my phone or something"
   scene trans
   "The first hour was fine enough..."
   "You couldn't focus super on reading over the sound of the same guitar phrases repeated over and over"
   "But it was fine..."
   "Another hour rolled by"
   # Tense is inconsistent
   "And she hasn't so much as looked in your direction"
   m "..."
   "Another hour..."
   "The sound of the guitar drills its way further into your brain"
   "Echoing though your skull and through your ears"
   "A wave of nausea hits you"
   "You stand up, suddenly feeling restless"
   "You don't know exactly why"
   "But you don't want to be here right now"
   "You can't be here right now"
   "With her..."
   "It's her last day... but she hasn't even spoken a word to you"
   "After all you've done for her"
   "Your stomach feels like you've swallowed a brick"
   "You say it over and over in your head"
   "..."
   "'Shut the fuck up'"
   "..."
   "You've been annoyed since the call earlier"
   "But you thought you could put on a smile for her"
   "On her last day"
   "You look over to her"
   "She's staring at the fretboard"
   m "..."
   "You don't know what's going to come out, but you brace yourself"
   "To say something..."
   "Anything..."
   m "..."
   m "Hey, do you mind like... Taking a break? For my sanity?"
   ali "..."
   m "Hey I'm talking to you!"
   ali "..."
   "You walk over to her and..."
   play sound guitar unplugged
   m "Stop it already! You've been playing the whole day!"
   ali "!"
   m "I'm trying to support you here, but I just can't take it anymore"
   ali "Hey what the fuck? I'm busy!"
   show mc shout
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
   m "None of this shit matters!"
   m "I thought the whole point of this was to not try to please anyone else"
   m "But you're just going from an insecurity that was imposed on you to one you chose"

   ali "..."
   # Forced wait for 3 seconds so like . wait . wait ."
   # but her expression changes
      "She stands up clutching the guitar towards her chest"
   "And starts to walk towards the door"
   m "Where are you going?!"
   ali "..."
   "..."
   # ali "Somewhere I can focus without you"
   m "!"
   ali "..."
   show sprite disappear
   m "She's gone..."
   m "..."
   m "Fuck..."
   m "What's wrong with me?"

   m "I've gotta go find her"
   option 1: The mall
   option 2: The river bank
   # ORder doesn't matter but gives scenery to go past as you have the internal dialogue
   scene trans
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
   choice :
      option 1: The mall
      option 2: The river bank
      (thing you already chose is disabled)

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
   scene trans
   show black
   play sound foodsteps and heartbeat
   m "()"
   show hallway
   m "()"
   scene trans
   show scene rooftop cg with alice crying guitar and butterfly
   play sound creaking door bursting open
   m "Alice!"

Rooftop reworked:
# he goes up to roof sweaty
# starts trying to apologise

m "Alice!"
m "I- *pant* I- "
m "I wanna say that I'm-"

# is interrupted by alice somberly talking at him about butterfly
ali "You know..."
ali "Since we went out yesterday..."
ali "I've been thinking a lot about butterflies..."
m "?"
"You look down at her sitting on the floor, and notice a large red butterfly on her fingertip"
ali "When we went to the cafe... At first I was really surprised when the waiter brought me that butterfly art"
ali "And I thought about what it might mean"
ali "Maybe I'm just overthinking it, and he just went of of vibes but..."
ali "Maybe there was a reason that he chose that."
ali "And so I thought really hard about it..."
ali "And after you went to sleep, I took a break from practicing to do a little research"
ali "You know... Butterflies aren't that different to me..."
ali "They're really pretty..."
ali "But it doesn't last that long..."
ali "After they come out of their cacoon, they only have X days to live..."
ali "To breed and be attractive enough to breed and to leave any sort of lasting legacy"
ali "To have any proof that they existed at all..."
ali "So I see myself in them"

ali "And they made me think a lot about myself..."
ali "My life..."

ali "I want my life to mean something... Anything..."
ali "To be remembered as a person that did something"
ali "And not just a pretty butterfly that's gone with the wind"

ali "But I'm still scared..."
ali "I'm scared that no matter what I do"
ali "Even if I could change the entire world"
ali "It wouldn't change that I feel like I do"

ali "So I wanna say I'm sorry"
ali "I'm sorry for losing sight of you, and for pushing you away"
ali "It's just hard you know..."
ali "The time we have is limited, and in the moment, it's easy to tell yourself that what you're focused on is the most important thing in the world"
ali "I just have this one chance..."
ali "To feel like I accomplished something"
ali "But I didn't want to push you away"
ali "I should have treasured the time I have with you more..."

ali "This butterfly over here..."
ali "It's dead..."
ali "Because of me..."
ali "I just wanted to touch it so when it flew over to me"
ali "I was really happy..."
ali "But I'm toxic..."
ali "You know the fly in fly aminita comes from the fact that they used to use us to kill flies by putting us in milk"
ali "It's like... Why do I have to be like this?"
ali "Why do I hurt those around me just by existing?"
ali "I just *sob*"

m "You know..."
m "I don't think you picked music because you wanted to be the best, or win the competition..."
m "I think it's because you saw something that spoke to you"
m "And maybe that's all that matters..."
m "But even so..."
m "You've been playing guitar for a couple of hours..."
m "And you're already better at it than I've ever been at anything"
m "You're amazing, and I don't think you know how much you are..."
m "I was thinking about how I lashed out earlier and..."
m "I think... I'm jealous of you"
m "Of your talent"
m "Of your looks"
m "Of everything about you"
m "And I know maybe it's selfish for me to say that but"
m "I just wanted to spend a bit more time with you before you..."

# I think it's important that he says this at some point but the timing feels bad here
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
show mc sulk
m "I just feel like..."
m "Time keeps moving..."
m "And I'm still alone... Here... In my room."
m "But I can't stay in college for ever."
m "I'm going to drop out or scrape through."
m "And then I'm going to work doing some crappy deskjob I hate, until I get old..."
m "And then I die."
m "I'm sorry, I came to apologize and I just ended up talking at you..."
ali "No, it's okay"
ali "I feel like now we both understand each other a little bit better"
ali "I guess... Maybe it's okay if I..."
ali "I'm not perfect"
ali "Or enough..."
ali "Just existing, and experiencing..."
ali "Hey..."
ali "I know it doesn't make up for earlier but..."
ali "I still want to do this show, and I was just wondering if maybe"
ali "You'd wanna help me with the finishing touches?"
m "!"
show mc embaressed
m "Uh, yeah... No problem"

scene trans
label preshow:
show bg concert hall outside
m "Okay, we're here"
ali "..."
m "Now just to sign up over here and-"
ali "Can we go home?"
m "Huh?!"
ali "I've changed my mind..."
ali "I don't think I can..."
m "Don't be ridiculous! You've worked so hard!"
ali "But-"
m "Hey, you've got this"
m "And even if you fuck up... At least you commited and did something most people will never do in their lives"
ali "Okay..."
ali "Fuck it..."
"She takes the pen in her hand with great enthusiasm and vigor and-"
ali "..."
ali "Can you sign up for me?"
m "Huh? Why?"
ali "I can't write remember?"
m "Oh yeah... Forgot about that..."
"*Skribble Skrabble*"
m "There we go... Now just to go inside and wait until you've gotta go backstage."

enter kellin and shadow friend
kel "And then you should have seen her face when-"
kel "(MC name)? What the hell!"
kel "You should have told me you were gunna come down here!"
kel "This is like my stomping ground!"
kel "I've gotta introduce you to-"
show alice from right
kel "!"
kel gets behind mc and uses him as a barrier from alice\
kel "It's her!"
m "?"
kel "I'm sorry, I gotta go..."
kel "I'll catch you later..."
ali "..."
m "What the fuck was that?"
m "Why did he recognize you?"
ali "You remember how when we first met..."
ali "And I ran away to the shower room?"
m "..."
m "Wait! HE was the guy from back then?!"
ali "Yeah..."
show mc depressed
m "Holy shit, that's so awkward..."
m "I've gotta apologize to him later"
m "Anyway let's head inside..."

label aliceDay3Show:
"You wait with Alice nervously in the venue"
"You see several groups happily drinking beer and laughing"
"The first couple of performers come out and the atmosphere of the place changes"
"You watch them together"
"But you can't help but feel like you are watching 'A performance'"
"Something you see on youtube or TV"
"It doesn't feel real"
"Real people who practiced and whose legs were shaking as they sung"
"Until"
ali "I think it's time..."
m "Oh yeah! You should get backstage"
ali "..."
m "Hey! Just one thing before you go"
m "..."
m "I just want to remind you that no matter how it goes"
m "That I'm really proud of you"
ali "Thanks... I-"
ali "I gotta go!"
"And with that she turned her back and started walking towards the stage door"
scene trans

announcer "Okay ladies and gentlemen, and those in between..."
announcer "Next up I want you all to give a warm welcome to~"
announcer "Alice!"
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

   ali "I uh- haven't really prepared anything but uh..."
   ali "I guess the last few day have been a really chaotic time for me..."
   ali "There where times I felt like everything was meaningless, but I had someone with me to help me through that"
   ali "And I wouldn't be up here with out them."
   ali "This song is called 'Metamorphisis'"
   play song fail

   # Maybe using dynamic audio and vamps to get the song to progress as the user clicks?
   "Alice starts playing the melodies I had heard so many times at this point"
   "But this time it felt different"
   "Knowing how much she put into it to get here..."
   "She opens her mouth to start singing and-"
   "Her voice awkwardly pops out and cracks part way through the second word"
   "Panic runs across her face and her hands freeze"
   "An awkward silence runs across the room"
   "..."
   "Then, she looks through the audience"
   "Until her eyes land on me"
   show little smile
   ali "I guess I focused so much on the guitar that I forgot to practice singing!"
   ali "Hahaha..."
   ali "Let's try that again!"
   "She starts the song again from the beginning, but this time, when the verse starts"
   ali "*first lyric line*"
   "She talks over the music as if talking to herself"
   ali "*lyrics*..."
   # Lyrics go here ->
   play sound applause
   "She looks up to me and smiles"
   announcer "Let's give it up one more time for Alice!"
   announcer "Okay! Next up we have..."
   scene trans

label post-show:
show outside venue
m "Alice!"
"You see her walk out from the backstage door, but waiting there for her is-"
kel "Hey Alice!"
ali "?!"
"You walk over to try to get between them but before you get there-"
kel "I'm so sorry!"
ali "?!"
kel "At first I hated you, because of what happened the other day."
kel "But after hearing you song!"
kel "I completely understand now!"
kel "It must have been some weird misunderstanding right?!"
ali "Ah... Ummmm"
kel "You were so good! I really loved the way you did the- (Here put in technical aspects from the actual song)"
m "Alice!"
kel "(mc name)! I thought you were going to use that guitar to learn for yourself!"
kel "Why didn't you tell me that-"
m "Yeah, I'm sorry. I should have told you that-"
kel "If you told me it was for a girl with such small hands, I would have lent you a guitar with a smaller neck!"
kel "I bet it was hard to play!"
ali "Wait you're the neighbour we're borrowing from?!"
show mc embaressed
m "Yeah..."
ali "Thank you so much! I wouldn't have been able to do this tonight if you didn't-"
kel "If you wanna say thanks, I know the perfect way..."
m "You don't mean..."
kel "You'll have to pay by...
ali "*gulp*""
kel "Letting me take a group Polaroid of us!"
ali "Huh?"
m "Woah it's one of those old cameras..."
m "Where did you get that?"
kel "I ordered it second hand online for super cheap! Hahaha"
kel "Ready or not! Cheese!"
play sound camera shutter
ali "!"
play sound photo printing
m "Are you okay? The flash must have been pretty suprising huh?"
ali "Yeah... I'm fine...I was just-'

play sound notice
# Maybe kellins friend should rush from inside to let them know
announcer "Okay it's time to announce today's winner!"
m "We should hurry back inside!"
scene trans
announcer "And!"
announcer "Today's winner!"
announcer "Who will have the luxury of recording a single at (insert funny names) studios for completely free!
announcer "IS~"
ali "*gulp*"
announcer "..."
announcer "VICIOUS FISH!!!"
m "Alice, I'm so-"
show ali smile
ali "Heheh, such a weird band name"
m "?!"
m "Are you okay?"
ali "Yeah? What you thought I was gunna cry if I lost?"
ali "Plus what am I gunna do with the prize of recording a single after I'm gone?"
kel "Are you going somewhere?"
m "?!"
ali "Uh... Yeah... I'm going abroad"
kel "Oh that's awesome! But kinda a shame..."
kel "We were just missing a rhythm guitarist and I was gunna ask if you could fill in..."
kel "ANYWAY!"
kel "When are you leaving?"
ali "..."
ali "Tonight..."
kel "Oh that's crazy!"
kel "Do you need a ride to the airport?"
kel "My friend has a big car, so we could-"
ali "No it's okay!"
ali "Thanks for offering."
ali "Anyways! It's getting pretty late..."
ali "We should head back so I can get ready"
kel "Aww, I was hoping we could talk about music!"
ali "I'm sure we'll get that chance next time..."
kel "Yeah, I'm looking forward to it!"
kel "Oh yeah... It should be ready now"
ali "Huh? This is..."
kel "This is the photo I took earlier!"
kel "I thought it might be something nice for you to remember us by..."
ali "Wow, this is so pretty... Is it really okay if-"
kel "Of course! I bought it for this sort of thing anyway!"
kel "Anyway, sorry to stop you from going home."
ali "No it's okay! Thanks."
ali "You all enjoy the rest of the night!"
kel "Yeah you two stay safe!"
m "We will do, I'll look after her!"
m+ali "Later~"
scene trans

label aliceDay3WayBackHome:
"The two of you walk back towards your dormitory"
"You walk together in silence until you reach the road leading up to your dormitory"
"Alice's pace grinds to a halt"
ali "..."
m "Hey, are you okay?"
ali "Yeah... I mean..."
ali "I don't know."
ali "It's just that it's all over you know..."
ali "I know I'm supposed to feel okay now"
ali "Like this life was enough like this"
ali "And like... I do feel like I accomplished something"
ali "And make memories with you..."
ali "But even still... This is it huh..."
m "We still have time! Maybe if we wait til tommorow we'll find that you-"
ali "Stop."
ali "I know that it's time"
ali "I can feel it."
m "..."
ali "Tonight was fun!"
ali "Kellin was really nice... He seemed like he really loves music."
m "Yeah... And he didn't even ask if we are dating or anything."
ali "Haha, why's that the first thing you say?"
m "I don't know."
m "I guess he's just not like some other people I know."
ali "Hmm~"
"She starts walking again slowly and you follow her pace"
ali "Don't you wish you'd reached out to him earlier?"
m "..."
m "I don't think I could have... Even now..."
m "It's still scary to know that if I say the wrong thing he might never want to talk to me again"
ali "Stop being so dramatic!"
ali "Not everything is life or death..."
ali "Unless your me that is! Haha"
ali "But even if you fuck up a little, I think you could just apologize"
m "Maybe..."
m "Hey, I wanted to say..."
m "About the song you wrote."
m "Thanks..."
m "It meant a lot..."
show alice embaressed
ali "What are you talking about!"
ali "Those l-lyrics didn't mean anything!"
ali "Idiot!"
m "?!"
ali "Don't get me wrong!"
ali "I just made them up to go with the melody!"
m "Real Tsundere?!"
ali "Huh? What does that mean?"
m "Nothing..."
m "You really worked hard for today, and I'm really proud of you"
ali "...Thanks."

ali "Hey... I just thought you should know..."
# ali "Even though I'm poisonous..."
# ali "There's a way you can prepare me so that I'm edible"
# ali "And even if you screw up a little, no one had died eating from eating a fly aminitas in over a hundred years."
# m "Eat you?"
# m "What?"
# m "Why-
# m "Why would I do something like that?"
# ali "I want you to... It's the last "

ali "I really appreciate what you did for me."
ali "Even though it was hard at first"
ali "I'm glad that this is the way things turned out"
ali "..."
ali "I'm going to go for a walk tonight"
ali "By myself"
ali "So don't come looking for me"
m "But I want to be with you when-"
ali "Please. I want for you to remember me for the time we spent together"
ali "Not for how I left"
m "..."
m "Okay."
ali "...Sorry... Or I guess"
ali "Thank you"
scene trans

label aliceDay3Goodbyes:
    show scene mc room
   #  This scene is 
    ali "Home sweet home!"
    ali "Aaah! I'm so tired..."
    m "I bet..."
    m "..."
    "You stand there for a few moments not knowing what to say..."
    "You don't feel equiped for dealing with situations like this."
    ali "Do you want to watch a movie or something?"
    m "Huh?"
    ali "Do you like comedy or are you into something like horror?"
    m "Comedy but..."
    ali "Yeah, that tracks..."
    m "Are you sure you are fine with just watching a movie?"
    m "Isn't there anything else you'd rather do?"
    ali "..."
    ali "No..."
    ali "I just want normal..."
    ali "That's already special enough for me."
    m "If you're sure..."
    scene trans
    "You watch a random romantic comedy movie from Netflix together on your bed."
    "She laughs at the stupid jokes, and tears up for the climax"
    "And before you know it..."
    scene trans
    m "Ahhh... I guess it's over."
    ali "Yeah. That kind of sucked hahaha..."
    m "Well you seemed to be enjoying it"
    ali "Yeah I did. Thanks to you..."
   #  Insert more dialog here
    ali "Hey...
    ali "It's kinda getting late..."
    ali "I should probably head out for my... walk..."
    m "..."
    m "So I guess... This is..."
    ali "Yeah... This is it."
    "She stands up and waits stands closer to the general vicinity of the door"
    ali "I don't really know what I'm supposed to say here"
    ali "I could do a long speech about everything I've learned with you..."
    ali "But I think it's better if I do this."
    show cg of her kissing mcs cheek or forehead
    ali "You've got a lot of life left."
    ali "So enjoy it enough for both of us"
    ali "Okay?"
    m "Yeah..."
    "Your lip starts trembling as tears start to well in your eyes"
    m "I-I-I"
    ali "It's okay..."
    "She opens the door and steps into the enterance"
    ali "Have a good life"
    ali "I'll miss you (player name)..."
    ali "Where ever it is I'm going."
    "She turns away and closes the door firmly behind her"
    m "Alice..."
    m "..."
    scene trans
   #  Choice where you can chase after her?


label aliceDay3Epilogue:
   play music "dynamic_audio/clock.mp3" fadein(2)
    show text "You're having your favourite dream."
    $ renpy.pause ()
    show text "In it, you're with your friends."
    $ renpy.pause ()
    show text "You look around and see them smiling. You hear their jokes and laughing.
    $ renpy.pause ()
    show text "You feel calm. You think nothing."
    $ renpy.pause ()
    show text "You simply exist together. How wonderful."
    $ renpy.pause ()
    show text "The heavy burden of your worries disappear." 
    $ renpy.pause ()
    show text "All the things you've cried over in the past don't matter anymore."
    $ renpy.pause ()
    show text "Even your {sc=1}failures{/sc}."
    $ renpy.pause ()
    show text "At first, you were terrified of this dream, but now...

    fade out to a cg of the mc's room with the guitar alice wanted, the polaroid they all took together
    as well as 2 more of MC with kellin and kellin's friend, playing in a band together

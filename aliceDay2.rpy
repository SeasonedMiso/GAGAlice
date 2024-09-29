# #aim for 1700-2000 lines across all endings

# label day2Morning:

#    # variables for Alice:
#    default arcadeWent = False
   

#    $ alice_rp = 0


#    #It's very important that alice has fun making fun of mc, in a sadistic way, but almost like nagatoro
#    #It starts cruel, but gradually starts to reveal that at her core she really cares about him

#    #If you can replace narration with dialogue, go back and do it! 


#    #wake up
#    #she waters herself

#    #if trust == 0 then she's mopey, so make sure enough chances to get it to be > 1
#    #talk to her

#    show bedroom_day with fade:
#       zoom 0.9
      
#    show mc stressed at right
#    show alice pout at left
#    with easeinbottom

#    play music "normal.mp3"

#    ali "So are you going to just keep lying there, or...?"
#    show mc normal
#    "You open your eyes to see Alice looking down on you"
#    ali "You've been lying there for a while now... Aren't you bored?"
#    show mc vannoyed
#    m "Don't you know what sleep is?"
#    ali "Yeah, but you're only supposed to do that for 8 hours..."
#    show alice disappointed
#    ali "At night time." # might be better to say "... and at night"
#    show mc normal
#    "You look over to your table, and pick up your phone"
#    "It's dead. Not like anyone ever messages you anyway."

#    m "What time is it?"
#    show alice normalside
#    ali "Well you've been out for like... 12 hours"
#    show mc confused
#    m "Oh, so it's probably like 1pm or so?"
#    m "What's the issue?"
#    show alice disappointed

#    ali "You're such a waste of space"
#    ali "I'm honestly impressed you had time to remember to water me between sleeping the day away and listening to people on youtube tell you what cartoons are worth watching"

#    m "How do you know what youtube is?"
#    #Elongate
#    #Or just change it to say videos?
   
#    m "...I was also... writing stories..."
#    show alice laugh
#    # make sure this makes sense in context
#    ali "You didn't even TRY to deny it"
   
#    ali "I bet you didn't even finish a single chapter"
#    show mc humiliated
#    m "..."
#    show alice laugh cruel
#    ali "See?"


# #This part needs to be changed:
# #it's not that she's perceptive, it's that you aren't used to someone else voicing negative thoughts about you


#    "It's like she's reading your mind"
#    "She puts to words the things you think about yourself before the thought is even fully formed"
#    # shes better at hating you than you ever could be. 
#    # the one thing you were good at and you have been outclassed
#    "It's like she sees right through you"
#    m "..."
#    "You turn your head down towards the messy duvet you're sitting on to avoid her gaze"
#    #she says one more mean thing here,  insulting your aethstetic and clothes 
#    #realizes that you're crying and is kinda shocked, then tries to make you feel better (softens up)
#    show alice normal
#    ali "Ummm... If you want I could help you... you know?"
#    ali "Look less like your mom picks out your clothes from the bargain bin"
#    m "Is that supposed to be an apology?" #  "Is that supposed to be an make me feel better?"
#    ali "Whatever, do you want my help or not?"

#    #maybe need to explain that although she's only a day old, she has instinct for only few things:
#    #Fashion/beauty, the need to be desired, knowledge on her species, as well as arts 
#    #(although the company programming tries to make her forget about that part)
#    #maybe try to develop that motif a bit about like, her needing to fight her programming
#    show mc normalside
#    "You pause for a moment to think about the offer"
#    "You would need to go outside"
#    "Where \"people\" are"
#    m "Ummm...Not really"
#    show alice shocked
#    #Like GAN face here with sound effect, let it be sort of slapstick
#    ali "but... I..."
#    ali "..."
#    show alice angry tears
#    ali "Fine, what ever, die alone virgin, see if I give a fuck"
#    show mc shocked at bounce
#    m "!"
#    m "No wait, it's fine! We can go! Wherever, Whatever you want"
#    show alice excited
#    ali "Really?"
#    show mc confused
#    m "..."
#    ali "..." # tsundere alice sprite
#    show alice hime
#    ali "Hmph, fine, if you wanna go so bad, I guess I have no choice then..."
#    show mc normalside
#    m "{size-10} that was easy"
#    show alice normal
#    ali "{size=+10} Did you say something?"
#    show mc stressed
#    m "No! Let's just go."
#    window hide
#    hide mc
#    hide alice
#    with easeoutbottom
#    stop music fadeout 2
#    scene black with Fade(0.5, 1.0, 0.5)        
#    play sound "door.wav"
#    play music "mall.mp3" fadein 2
#    show chibi_mc at slightright
#    show chibi_alice at slightleft
#    with easeinright
#    window show

#    #Develop this conflict
#    #You didn't want to fight and you feel sorry for her since she's going to die soon anyway  
#    "You try not to think about the other students seeing you leave the dorm with a girl."
#    #talk a little more about the traveling process and getting to the mall
#    window hide

#    hide chibi_mc
#    hide chibi_alice
#    with easeoutleft

#    jump day2date

# label day2date:
#    scene mall with Fade(0.5, 1.0, 1)
#    show mc normal at right
#    show alice surprised at left
#    with easeinbottom
#    ali "Woah, what is this place?"
#    show mc normalside
#    m "I've only heard rumours, but I believe this place is called a \'mall\'."
#    show alice awe
#    ali "A \"mall\"..."
#    ali "Why would you stay inside all day when there's such vibrant places like this so close by?"
#    show mc worried
#    m "Well... It's loud and there's lot's of people..."
#    show alice confused
#    ali "Hmm? For such a stupid reason? I don't get that"
#    ali "Anyway, now that we're here, let's try and find some stuff to gaslight people into thinking you're not a loser"
#    show mc confused
#    m "How do you know what gaslighting is?"
#    show alice sly smile
#    ali "Does anyone REALLY know what it is?"
#    m "Yes?"
#    jump clothes
#    # menu:
#    #    "You notice Alice looking at a clothes store..."
#    #    "Offer to go.":
#    #       jump clothes
# #Maybe move this scene to after the date scene
# #Make it a choice of "Where you see her looking"
# #And make it requirement for true end

# #todo:make this scene more subtle
# label clothes:
#    show alice normalside
#    ali "Whatever, what about that place over there?"
#    m "You mean the men's attire store?"
#    show mc normal
#    m "Do you think I look like I have the money for a suit and tie?"
#    show alice smug
#    ali "Even if you did, it's not like it would /suit/ you anyway"
#    show mc annoyed
#    m "Hehe-"
#    "You almost give in and laugh at her joke"
#    "A joke at your expense"
#    "You know she's right"
#    show alice normal
#    ali "So how about you give me something to work with?"
#    ali "Makes it easier to at least know what we are going for"
#    show mc normalside
#    m "I guess I like grey-scale stuff that's not too flashy"
#    show alice cruel 
#    ali "So what we came all this way so that you can keep trying to blend in with the shadows?"
#    ali "Come on, you must like at least some /real/ colors"
#    show mc blushside
#    m "... I kinda... don't hate pastel stuff..."
#    show alice laugh
#    ali "Heeeh? That's unexpected. Didn't think you were the type for cute stuff like that"
#    #ali "Want me to pick you out a skirt too? I bet I can find one that will /really/ suit you"
#    show mc embarrassed
#    m "What!? Pastels aren't cute, they're cool..."
#    ali "You don't need to play stupid, I saw your wallpaper on your big screen thing"
#    #Show like a cute kirby-ish wallpaper on the pc during the discord scene
#    m "!"
#    m "..."
#    "She's got you there"
#    ali "Besides, how is it creepy? I'm serious, I think you'd look really cute~"
#    show mc vstressed
#    m "Stop fucking with me..."
#    show alice serious
#    ali "I'm not"
#    m "There's no way you actually mean that..."
#    show mc worried
#    m "Besides, I already can't deal with people..."
#    m "How am I supposed to handle them if they stare at me"
#    m "I just want to fade into the background"
#    "In your room... Forever"
#    # a room that isnt his and is temporary
#    show alice neutral
#    ali "Really?"
#    m "..."
#    show alice annoyed
#    ali "I'm going to die soon... I don't have much time left..."
#    ali "And you have some more... But even then"
#    show alice 
#    ali "Your time is limited."
#    show alice sad
#    ali "Don't you feel like it's a waste? Of youth? Of life?"
#    ali "I think you're just scared."
#    ali "Me too..."
#    ali "But can you honestly tell me that you /want/ things to carry on like they are?"
#    show mc awed
#    m "..."
#    show alice laugh cruel
#    ali "So..."
#    ali"..."
#    ali"Let's get you some cute clothes!"
#    show mc vvannoyed
#    m "That's where you were going with this?!?!?"
#    ali "So that's a no then?"

# menu:
#    "We can take a look I guess":
#       jump mallPastel
#    "Not in a million years, no way (N/A)":
#       "Skye must still write this part..."

# label mallPastel:
#    $ alice_rp+=10
#    show black with dissolve
#    "..."
   
#    #cut to the mall later, with mc wearing a slightly oversized pastel pink hoodie
#    # :3 insignia?
#    show mc pink embarrassed
#    show alice smug
   
#    hide black with dissolve
#    m "..."
#    show mc pink embarrassed desperate
#    #make sure it's not obvious that they are trans, make it like they are a guy who's ashamed of having a feminine side
#    #because of it bringing more attention to him and that going against the status quo
#    #she acutally thinks it suits him, and is trying to help him give less of a fuck
#    # but is also teasing him by picking on the obvious discomfort he feels about this 

#    m "EVERYONE'S LOOKING AT ME!"
#    ali "So? Let them."

#    m "Easy for you to say..."
#    ali "What was that?"
#    m "Easy for you to say when you could even make rags work!!!" # change this line X3
#    show alice flirt
#    ali "You really think so?"

#    m "That's not my point! I just mean like..."
#    m "I'm not like you. It's better for everyone else that I just stay out of sight."
#    show alice annoyed 
#    ali "Stop saying stupid shit. If I hear one more thing from you I'll take that as a personal insult."
#    m "Huh? Why what does what I say about myself have to do with you?"
#    show alice vannoyed
#    ali "I picked out those clothes, and my sense is absolute."
#    show alice angry
#    ali "So shut the fuck up and enjoy the attention."
#    m "..."
#    m "I-"
#    ali "What did I just say?!"
#    m "Sorry..."
#    show alice laugh
#    ali "You really are cute."
#    show mc pink embarrassed
#    show black with dissolve:
#       alpha 0.5
#    "You don't really know how to feel..."
#    "You can't help but feel scared."
#    "Scared of judgement."
#    "Memories of the kids you went to elementary school with flash into your mind's eye."
#    "Of little comments your parents made."
#    "When you stepped out of line."
#    "Not for being rude, or malicious."
#    "But for being curious."
#    "..."
#    "You like cute anime."
#    "You like playing games where you talk to little animals people, and go fishing."
#    "You know you like this hoodie."
#    "But is it {i}really{/i} okay?"
#    "For someone like you to wear this?"
#    "Up until now, it's always been participating in this stuff as an observer..."
#    "Out of sight."
#    hide black with dissolve
#    show alice disappointed
#    ali "It's just a waste you wouldn't try on the good stuff."
#    show alice laugh
#    ali "I picked you out the cutest thigh-highs and everything."
#    ali "The little cat paw prints on the sole were adorable."
#    m "I bought this - can't you just leave it?!"

#    show alice happy
#    ali "Jokes aside, I think that it really suits you and I can tell you like it too."
#    m "..."
#    show alice normalside
#    ali "It's just a shame you want to hide away under all that fabric."
#    ali "Wouldn't hurt you to show us some skin."
#    show mc embarrassed tears
#    show alice hime
#    ali "But I guess fruiting bodies don't sprout in a day, and that suits you pretty good as is."
#    m "Who is supposed to know about fruiting bodies?! You're lucky I'm a biology major..."
#    ali "Anyways, it's still pretty early and we are here already so let's go somewhere else."
#    show mc confused
#    m "Like where?"
#    show alice confused
#    ali "Hmmm... I don't know..."
#    show mc normal
#    m "Do you have any hobbies or whatever?"
#    show alice cruel
#    ali "Oh yeah, I {i}love{/i} to crochet on the weekends after finishing at the office~"
#    show alice mendokusai
#    ali "I'm a mushroom that was born literally a day ago, why the fuck would I have hobbies?"
#    show mc stressed
#    m "...Sorry..."
#    show alice normal
#    ali "Whatever... So, where are we going?"

#    #Maybe add a bit here about being thirsty so the cafe is a neccessary event
#    "You've haven't been to the mall since you were in elementary school."
#    "Let alone with a {i}girl{/i}."
#    show mc normalside
#    "Where would she want to go?"
#    jump aliceDay2DateLocation

# label aliceDay2DateLocation:

#    menu:
#       "Quickly get this over with.":
#          jump cafeDate
#       "Show her something you like.":
#          if alice_rp >= 10:
#             jump arcadeDate

#          "You think about taking her to somewhere you would want to go."
#          "But then you look over at her, and see her impatiently tapping her foot."
#          "You don't want to drag this out any longer than it needs to be."
#          jump aliceDay2DateLocation

#    # choice: [Quickly get this over with, Show her something you like]
#    # >Show her something you like
#    #    if(trust)>x:
#    #       jump arcadeDate
      
      



# #move to day 1 maybe
# label arcadeDate:
#    show mc normal
#    m "I think I saw a sign for an arcade back there"
#    show alice confused
#    ali "An arcade?"
#    m "We could go and I could maybe try show you how to play some video games."
#    show alice disappointed
#    ali "Are you for real right now?"
#    show mc confused
#    m "You want to find stuff you're interested in right?"
#    show mc annoyed
#    m "How do you know you don't like it if you don't give it a go?"
#    show alice pout
#    ali "..."
#    show alice mendokusai
#    ali "...FINE~"
#    scene arcade with fade
#    show mc surprised at right
#    show alice disappointed at left
#    with easeinbottom
#    #black scene


#    #Change this so alice has an appropriate amount of knowledge about this stuff
#    $ arcadeWent = True
#    m "Woah, look at this place! They have so many retro titles!"
#    show alice normalside
#    ali "Isn't that like a nice way of saying they're charging 25 cents for games that have been out of date for like 30 years?"
#    show alice confused
#    ali "Can't you play these on your computer anyway?"
#    show mc normalside
#    m "I guess I could set up a MAME emulator on RetroArch, but-"
#    show alice annoyed
#    ali "Are you listening to yourself right now?"
#    ali "I have no fucking clue what you're talking about."
#    show mc awed
#    m "I just meant like, we could use my pc..."
#    show mc normalside
#    m "but then we're really comprimising on the authenticity of the experience."
#    show alice smug
#    ali "The experience of being in a run down shit hole?"
#    show mc surprised
#    m "Woah! They have that weird train game?"
#    show mc happy
#    m "It's a weird Japan-only game where you play as a train conductor and like, there's train levers, and-"
#    show alice neutral
#    ali "You're really making this whole gaming thing so SO cool."
#    show mc normal
#    m "Well there's a whole bunch of other games too."
#    m "What kind of thing do you think you might like?"

#    show alice confused
#    ali "I don't know... What about that one over there?"
#    show alice happy
#    ali "Those little dinosaur things are kinda cute~"
#    show mc happy
#    m "Oh bubble bobble?"
#    m "I haven't played that game since I was a kid."
#    m "Lemme get some tokens..."

#    #interlude
#    show black with dissolve
#    "You show Alice how to move, blow bubbles, and capture monsters."
#    "She quickly grasps the basics and is able to beat the first level without any issues."
#    "However, after only a few levels, the difficulty begins to increase dramamtically, and before more than a few minutes have passed..."
#    show alice annoyed
#    hide black with fade
   
#    ali "Game Over? What the fuck is this shit?"
#    show mc annoyed
#    m "In these kind of games you only get a few lives, and if you use them all up, you need to pay more to keep playing."
#    show mc happy
#    m "Do you want to keep playing this?"
#    show alice sulk
#    ali "What's the point? What do I {i}get{/i} if I keep playing?"
#    show mc awed
#    m "Well... The satisfaction of having gotten further, and accomplishing something that not many people have done?"
#    show alice annoyed
#    ali "That's fucking stupid."
#    ali "Who cares if you are the best in the world at playing stupid children's games?"
#    show mc normal
#    m "..."
#    show mc sulk
#    m "It's not stupid to me..."
#    m "...or lots of other people."

#    m "These games represent memories of our childhoods."
#    m "Friendships."
#    show mc normalside
#    m "Although looking around here, you might not get it but..."
#    m "There are all sorts of games."
#    m "Games about guns, games about fishing, games about defusing bombs."
#    show mc stressed
#    m "Games about just talking to people."
#    m "Games that give you a new outlook to look at the world..."
#    show alice neutral
#    ali "..."
#    show mc awed
#    m "Games to play by yourself, games to pass the controller back and forth..."
#    m "Games that let you meet new people."
#    m "I think that for me, it helps to feel connected to something bigger."
#    m "The community of people brought together by having this small thing in common."
#    show mc normalside
#    m "I just thought it would be cool if you would be able to find something like that too."
#    show alice pout
#    ali "..."
#    show alice sulk
#    ali "I guess..."
#    show alice normalside
#    ali "I'm sorry okay?"
#    ali "I shouldn't have called it stupid."
#    show alice normal
#    ali "But even so, I don't really think this is for me."
#    ali "Maybe if I had more time to find one that speaks to me."

#    ali "But right now, I want to find something else."
#    show mc slightsad
#    m "..."
#    m "Okay... let's try find something else."
#    m "How about..."
#    #obv need different dialogue path if it's not the first option
#    #Choice
#    jump cafeDate


# label cafeDate:
#    scene mall with fade
#    show mc normal at right
#    show alice normal at left
#    with easeinbottom
#    "You walk past a small cafe. It looks relatively empty, despite how busy the rest of the mall is."
#    "The tile floor and decor look clean and without wear."
#    "This place is probably new."
   
#    m "Do you want to go inside and get something to drink?"
#    show alice neutral
#    ali "... As long as I have my water spray, I'm fine. I don't really get that whole animal thing of 'eating' in order to sustain yourself."
#    show mc normalside
#    m "Well, there are plenty of reasons to eat and drink stuff, even if it's not purely for sustanance."
#    m "Lots of people eat and drink stuff purely for enjoyment."
#    m "Going out for food is something a lot of people do as a way of seeing new places, and experiencing new things with people."
#    m "Making memories, that sort of stuff."
#    show alice sly smile
#    ali "When was the last time you went out to eat with someone?"
#    show mc stressed
#    m "..."
#    show alice cruel
#    ali "Figures."
#    show mc normal
#    m "Anyway, I still need to do that whole animal 'eating, drinking' thing"
#    show alice hime
#    ali "I don't get it... But like, whatever, if you're so adamant about this whole thing and it's {i}sooo{/i} important to you, I guess I'll give it a go."
#    window hide
#    #screen transition
#    stop music fadeout 2
#    scene mallcafe with fade
#    play music "mallcafe.mp3"
#    show mc normal at right
#    show alice normal at left
#    with easeinbottom
#    "A young waitor is sitting at a desk by the storefront, flicking a pencil around notebook propped up at the corner of the desk at an angle."
#    "He looks up, notices us, and turns his gaze back to the paper, continuing as he was for a few more seconds before slowly getting up out of his seat."

#    na "Welcome, can I get you guys a table?"
#    show mc worried
#    m "..."
#    ali "..."
#    m "..."
#    na "...Ummm... Are you okay?"
#    show mc vstressed
#    m "yEahh, umm I... uhHh.... 2 please?"
#    na "Sure, right this way."
#    show alice disappointed
#    ali "God, I forgot you can't talk to anybody except for your stuffed animals."
#    show mc worried
#    m "I didn't think entering a store would mean talking to someone."
#    show alice mendokusai
#    ali "I'm a mushroom with no knowledge of the world except for the small amount of info I was biologically programmed to know."
#    ali "But even /I/ know that's how this works."

#    show black with dissolve:
#       alpha 0.5

#    "You are escorted to a large table, with 2 chairs on one side, and couch seat built against the wall on the other."
#    "Alice swiftly slips onto the couch chair, without saying anything"
#    #She picked the more comfortable choice without second thought
#    hide black with dissolve
#    show mc normal
#    show alice normal
#    m "..."
#    ali "..."
#    m "..."
#    show alice confused
#    ali "So... When does this get interesting?"
#    show mc normalside
#    m "Well, after the waiter comes back we can tell them what we want to order."
#    m "And then we wait for it to be prepared."
#    m "Eat."
#    m "Then pay for our order and leave."
#    show alice disgusted
#    ali "So it's just waiting for food, eating and then you leave? And this makes memories how?"
#    ali "And you guys have to do this like..."
#    ali "3 times a day?"
#    show mc worried
#    m "Yeah, but there's still like... Ummm... You know? It's different when you go somewhere to do it."
#    show alice normalside
#    ali "If you're so desperate for a change of scenery while eating, then can't you just like, eat in the shower or something?"

#    na"Are you guys ready to order?"
#    show mc shocked at bounce
#    "Damn, he snuck up on me... We still haven't decided!"

#    #maybe try do like tumblr cry text where it's like "I sorRi; I jsut cant't' doo it"
#    show mc stressed
#    m "ummm... Uhh, just one... sec; pleaSe"
#    show mc shocked
#    m "Alice, We've got to decide! Have a look at the menu!"

#    #screen transition
#    show cafe_menu at truecenter with easeinbottom
#    play sound "page.wav"
#    #Are there any foods that mushrooms can't break down/ mould doesn't grow, that might be on a menu?
#    show alice annoyed
#    ali "What the hell am I going to do with a toasted cheese sandwich?"
#    show mc sad
#    m "Come on, please just pretend to TRY to enjoy yourself."
#    show alice laugh
#    ali "OMG I'm am so excited to order 2 pieces of bread, with fermented cow mammary extract melted between! I'm actually quivering in ancipation to put it in my mouth, digest it and then wait for 8 hours, and then-"

#    m "Please! Just... like... Come on, how about this? This one looks kind of cool? Right?"
#    show alice annoyed
#    ali "Latte art? Like a drawing of coffee? And you eat the paper?"
#    show mc normalside
#    m "No, they ummm... Make like an image ontop of the coffee by pouring the coffee into the foamed milk so it makes a picture"
#    show alice sly smile
#    ali "You guys really love drinking stuff from cow boob's huh? Is it like a sex-thing or..."
#    show mc stressed
#    m "No!"
#    show alice confused
#    ali "So lemme get this stragiht? Somebody like, puts in the effort to make some kind of drawing out of foam, and then you just... drink it?"
#    show mc normal
#    m "Yeah."
#    show alice sigh
#    ali "I've have never heard of something."
#    ali "So"
#    show alice disgusted
#    ali "fucking stupid in my life."
#    show mc slightsad
#    m "You've been alive for like 24 hours."
#    show alice annoyed
#    ali "THE POINT IS! Why would you make something that's just going to get destroyed a few minutes later? What's the point?"

#    #Kind of a metaphor for life, especially with it being as short as it is

#    m "Okay so if it's so stupid, then what ARE you going to order then"
#    ali "..."
#    ali "Fine, you've peaked my interest, let's see what this is about"

#    hide cafe_menu with easeoutbottom
#    play sound "page.wav"
#    #screen trans
#    na "So are you guys ready to place your order now?"
#    show mc worried
#    m "...Umm. I, umm. could I please...2... uhh."
#    show mc stressed
#    "You give up and point towards the listing for latte art in the menu."
#    "The waiter bends over to look and the item you're pointing at, and after spending a second registering, his expression instantly changes as if suddenly jolted awake"
#    na "Two latte arts right? Coming right up!"
#    "He energetically snatches the menus of from the table, and practically skips away from the table."

#    #scene trans
#    "..."

#    na "Sorry to keep you waiting!"
#    show alice vannoyed
#    show mc normal
#    "Barely 5 minutes had past since the order was placed, the waiter arrives back balancing a tray in one hand."
#    "He carefully places the tray down onto the table and without missing a beat, begins to explain the items." 
#    na "Over here for you I thought you might like something cute and uplifting to freshen up the bags under your eyes."
#    "He places a coffee cup in front of you with a detailed illustration of a small rabbit running through a flower garden."
#    na "And for you, I thought you might like this [...]."
#    #What does he see in her that inspires him to draw something that says something about her?
#    show alice surprised
#    ali "Huh... wow... You made this for me? Even though I'm going to drink this in front of you, and undo all of your effort... Why?"

#    #maybe it would be cool if alice is like "drawing, that sounds easy", she's able to do it well mechanically, but the waiter points out that there's not message behind her art
#    #that's the differnece between AI and people etc

#    na "Well, this is my dad's place. It's not doing too well, so he's making me help out"
#    na "Not really how I want to spend my time out of class, but I don't have a choice"
#    na "I'm studying to become an artist, and well... This is the only part of my job that I get do something worth while"
#    show alice sulk
#    ali "I see... I still doesn't explain the whole like, spending so much effort on something I'm going to destroy 2 seconds later."
#    na "It's sort of a shame, but like... All art has an expiry date. Whether it's the pigment in oil paintings decaying, pencil fading, or art galleries going up in flames"
#    na "Even cave paintings from thousands of years ago are going to be destroyed eventually"
#    na "Nothing lasts forever, and well..."
#    na "I like trying to make observations about what kind of people order from here, and try to make something just for them "
#    na "Art is like... How do I say it... Taking something abstract like, a thought, or a feeling... Sometimes just a funny vibe, or sometimes something really important"
#    na "The kind of stuff that inspires revolutions or changes lives"
#    na "It's a way of taking that message and trying your hardest to get someone else to feel the same way as you"
#    na "When words can't"
#    na "So I guess it's like... It doesn't matter if my art lasts a second or thousand years, as long as I can try to share that feeling with someone" 
#    show alice neutral
#    ali "..."
#    na "Sorry, I guess I talked a bit too much... Anyways, I hope you enjoy your coffee"
#    "He walks back to his station at the front, and picks up his pencil again"
#    "Alice looks down into her cup for a few seconds as if thinking deeply about something"
#    "And then suddenly picks up the cup and presses it to her lips"
#    show alice disgusted
#    ali "Bleghhh... What the fuck is this? It's like... creamed dirt water..."
#    show alice awe
#    ali "Ah!... But wait that after taste... This tastes kind of like my mycelium."
#    show mc awed
#    m "Yeah, well I threw in a couple of coffee grounds into where you were growing, since I read online it's good for mushroom growth"
#    show alice normalside
#    ali "I see..."
#    "She reluctantly takes a second taste of her coffee."
#    "Occasionally looking deeply into the depths of cup."
#    "Maybe you should say something to her:"
#    menu:
#       "Did you enjoy that?":
#          jump aboutCoffee
#       "Talk about world(N/A).":
#          "..."
#       "Stay quiet(N/A).":
#          "..."
#    #Choice: [Did you enjoy that?,  About how much you know about the world, Stay quiet]
# label aboutCoffee:
#    show mc normal
#    m "How's your coffee?"
#    ali "Hmm... It's okay... I think maybe I understand why people go out to eat a bit better."
#    "You sense that she wants to say something else."
#    show mc confused
#    m "Yeah, and why's that."
#    show alice sulk
#    ali "I guess... I just have some stuff to think about... About me... About... You know..."
#    "She gulps and seems slightly stressed."
#    show alice hime
#    ali "But anyway, the taste was nostalgic and I think maybe... I don't hate coffee."
#    show mc happy
#    m "That's great to hear."
#    m "You seemed like you were thinking pretty hard looking into the mug. What were you thinking about?"

#    if arcadeWent:
#       jump coffeeTalkArcade
#    show alice sulk
#    ali "Nothing much..."
#    show mc normalside
#    "You can tell she's not telling the full story."
#    "But you don't want to push her too hard."
#    show mc normal
#    m "Okay, just as long as you enjoyed it"
#    ali "Yeah..."
#    jump leaveCafe


# #fork if you went to arcade first and max trust
# label coffeeTalkArcade:
#    show alice normalside
#    ali "You know..."
#    ali "I was just thinking back to that dinosaur game in the arcade."
#    show mc confused
#    m "Yeah, bubble bobble."
#    m "What about it?"
#    show alice sulk
#    ali "Yeah... Just like... In that game right, if you fuck up and get yourself killed, you can come back if you get a 1up, or waste your rent money."
#    show mc annoyed
#    m "Yeah, but like, I wouldn't reccomend that strategy tbh."
#    ali "Sure, but like..."
#    ali "We don't get anything like that do we?"
#    show alice pout
#    ali "In real life"
#    show mc surprised
#    m "..."
#    ali "There's no amount of power or money, no one is important enough to get around the game over screen."
#    ali "And even if you beat the game, it's over..."
#    show alice pout
#    ali "And so I feel like... What do you do when there's no point?"
#    ali "With a game like that you can brag to your friends, or... not get a girlfriend."
#    show alice depressed
#    ali "But with life it's just like... Why even bother?"
#    ali "At first, I just followed my instincts and tried to get you to pay attention to me."
#    ali "Not because you were special, or because I liked you, even knew you."
#    ali "But because that's what I felt would make me feel like I am worth something."
#    show alice sulk
#    ali "I don't know it's... stupid... Sorry, I just..."
#    ali "Maybe what you said last night... and what the cow boob artist said..." 
#    show alice confused
#    ali "Maybe there is something more to life than just using others to prove to yourself you're worth something."
#    ali "So I wanted to say that..."
#    show mc awed
#    m "..."
#    show alice normalside
#    ali "Yesterday I didn't need to shout like that or whatever."
#    show mc confused
#    m "...wow... I uh... that's nice?"
#    show alice annoyed
#    ali "What!?"
#    show mc surprised
#    m "No! I mean, sorry that was just sudden so I don't really know what to say."
#    show alice sulk
#    ali "Agghh, I shouldn't have said anything to you."
#    show mc stressed
#    "You're so stupid..."
#    "Even when you luck into doing something nice, and helping someone, you have to fuck it up at the last second."
#    "She's probably already seen through the pretty words you said yesterday as made up bullshit."
#    "Be real: YOU said it, so there's not way that you're right."
#    "You're so!"
   
#    ali "..."

#    "FUCKING"
#    show alice pout
#    ali "..."

#    "STUP-"
#    show alice blush
#    ali "Thank you for taking me here."
#    $ alice_rp += 10

#    show mc surprised

#    m "Ummm... Yeah, That's okay..."
#    ali "..."
#    show alice normal
#    ali "You look suprised."
#    show mc blushside
#    m "Yeah I uh... Didn't really expect you to say that."
#    show alice sigh
#    ali "Me either."
#    show alice normal
#    ali "But I think that I'm starting to change"
#    ali "I don't know what it is but."
#    show alice confused
#    ali "I just feel like when I was born, I had a very certain idea of how this life was supposed to go."
#    show alice sad
#    ali "You were going to be all over me, and I was going to feel good about that."
#    ali "Because that was proof that I succeeded in my purpose."
#    show alice smug
#    ali "But you were too much of a little bitch to do anything and made me cry."
#    show mc sad
#    m "I'm sorry, you know that I didn't mean it like that, I'm just-"
#    show alice happy

#    ali "I know, don't worry about it."
#    show alice pout
#    ali "It's just at the time that was kinda a shock you know..."
#    ali "Like I had just been told that I'm not cut out for my purpose."
#    ali "I'm just too ugly, too annoying, too whatever."
#    show alice depressed
#    ali "And that's not a great feeling."
#    ali "And for a while, I didn't really know what to do with myself."
#    ali "And being with you..."
#    show alice sulk
#    ali "Was painful..."
#    show alice annoyed
#    ali "Do you know what it's like to be with someone you want to like you?"
#    ali "How painful it is to know that the reason they didn't like you isn't something you did?"
#    ali "But just like... the way you are?"
#    show alice sigh
#    ali "And so I guess that's where I was for a while..."
#    show alice sulk
#    ali "And now I... I don't know."
#    ali "I feel like, maybe I can find something else worth living for."
#    ali "Even if it's only for another day."
#    show alice blush
#    ali "And I wouldn't have that without you."
#    show mc surprised
#    m "I didn't do anything special."
#    show mc awkwardsmile
#    m "I just said whatever words popped into my mind."
#    m "Anyone could do that."
   
#    ali "Yeah, but you did."
#    show mc awed
#    m "..."
#    show mc normalside 
#    m "Whatever."
#    show alice confused
#    ali "So while we are talking like this... I was curious if there was anything you wanted to know about me"
#    show mc confused
#    m "Like what kind of thing?"
#    show alice cruel
#    ali "I dunno? Like you know... My 3 sizes, the color of my underwear. You know, normal stuff?"
#    show mc stressed at bounce
#    m "Who taught you what normal is?!"

#    show alice sulk
#    ali "I guess I was just born knowing all kinds of stuff."
#    ali "Like ways to make people feel good, how to tie people up, that sort of stuff."
#    show mc vstressed at bounce
#    m "WHY IS IT ALL SEX?!?!"
#    show alice confused
#    ali "Hmmm... Now that you mention it, a lot of it is related to sex."
#    show mc confused
#    m "?"
   
#    ali "Like, I have some other information that I was just born knowing"
#    ali "Like uhhh.... I know a bit about mushrooms, and like... I guess some of the stuff is more abstract."

#    ali "Like when I was born I just KNEW that if I behaved a certain way, that you would like it."
#    show alice pout
#    ali "But it didn't go the way I assumed it would."
#    m "So you mean like... You had like... Instincts about specific information? Like genetic memories?"
#    show alice neutral
#    ali "I don't know what the fuck you're talking about but uh, yeah sure, why not?"
#    show mc normal
#    m "What I mean is, that you like woke up and knew how to speak perfect English, and all of that other stuff."
#    show mc normalside
#    m "I didn't really think about it too hard after the shock of ummm... You like... Being alive and everything."
#    show alice cry
#    ali "What, you'd rather I was dead?"
#    show mc vvannoyed
#    m "No I- Actually no, I'm not gunna take the bait this time."
#    show alice smug
#    ali "Awww, but it worked before."
#    show mc awed
#    m "I was just trying to say that there needs to be a reason you know all of this stuff?"
#    show alice confused
#    ali "Yeah well... Didn't you like buy me off of the internet from some sketchy darkweb site or something?"
#    show mc stressed
#    m "IT WASN'T THE DARKWEB-"
#    show mc normalside
#    m "But yeah, I guess I wouldn't put it past that site to do something like that"
#    m "I guess everything you knew makes sense for the purpose of what you were being sold for"
#    m "So maybe they like, embedded that information into your DNA to streamline the user experience of ummm "
#    show alice neutral
#    ali "I'm right here you know"
#    show mc awkwardsmile
#    m "Sorry, I phrased that sorta weird"
#    show alice normal
#    ali "I think you might be onto something though..."
#    show alice normalside
#    ali "It is kind of weird that I know over 200 sex postions, but didn't know what a mall is huh?"
#    show mc shocked
#    m "There are that many?!"
#    show alice smug
#    ali "Way to reveal your power level wand master"
#    show mc sulk
#    m "I just think it's really fucked up"
#    m "How they programmed you to be the ideal product for them to profit off of"
#    show alice confused
#    ali "Yeah, I guess... But..."
   
#    ali "Are you guys really all that different?"
#    show mc confused
#    m "Huh?"
#    ali "I mean... Think about it right?"
#    show alice normal
#    ali "If you look around at every one here, they were all raised by parents, who taught them what was right and wrong"
#    ali "And then sent them to a school to learn stuff the government wants them to know for like a billion years"
#    ali "If you're born with one set of bits, you get given toys to simulate child rearing"
#    ali "And if you have the other, you're supposed to be like a firefighting astronaut football player or something"
#    show mc vannoyed
#    m "What were you watching on my computer last night?"
#    #Put in a bit in night of day 1 about her watching stuff on his computer because she's bored while he sleeps
#    show alice hime
#    ali "ANYWAYS! You know what I mean right... It's easy for you to point at me and say I'm fucked up, but from where I'm sitting"
#    show alice serious
#    ali "None of you guys seem that different"
#    show mc normal
#    m "..."
#    show alice confused
#    ali "I guess I just wanted to know like... How do you know your values are you own?"
#    ali "Like are you living for yourself? Or to feel like you're winning in some game you've been conditioned to think is important?"
#    #way too on the nose, rewrite to soften
#    show mc confused
#    m "I... I don't-"
#    show alice laugh
#    ali "Anyways, lets order some cake! After trying that coffee, I kind of want to see if the other stuff is any good"
#    m "Uhh... Yeah..."
#    jump leaveCafe


# label leaveCafe:
#    stop music fadeout 3
#    scene mall with fade
#    play music "mall.mp3"
#    "After you paid the bill, you walked through the mall towards the exit"

#    scene enbankment with fade
#    show mc awed at right
#    show alice happy at left
#    with easeinbottom
#    m "It's not too often I get to walk outside in the sunset."
#    ali "Yeah sure... \"in the sunset\""
#    m "Yeah... Maybe I should do it more"
#    ali "Maybe you should! It's really pretty!"
#    show mc confused
#    m "Why do you seem like you're having more fun on the embankment going back home, than when we were actually at the mall"
#    ali "The mall was fun... But this is nice too"
#    m "..."
#    show alice surprised
#    ali "!"
#    m "What?"
#    show alice awe
#    ali "Look! Over there!"
#    m "Huh?"
#    ali "It's a butterfly!"
#    hide alice with easeoutright

#    show mc surprised
   
#    m "Huh? Wait!"

#    scene black with fade
#    stop music fadeout 3
#    m "Don't just run off like that! You had me worried for a sec, when I lost sight of-"
#    ali "..."

#    scene butterfly with fade
#    #Here I think it's important to have a cg? I don't want to just write a huge monologue, but it's that or a picture
#    "You stop behind a still alice, crouching down on the grass."
#    "Her hand is outstretched but motionless, and a blue object lies on her extended index finger"
#    "A butterfly"
#    "The butterfly that moments ago fluttered about in the shallow breeze so freely"
#    "Laying peacefully still on her fingertip"
#    play sound "wind.wav"
#    "..."
#    "..."
#    "The butterfly remains motionless"
#    "..."
#    "The moment stretches on for longer that you feel comfortable"
#    "You want to say something... Anything... But you feel like there's an unspoken weight in the air"
#    "You hear alice's taut vocal cords produce a strained sound as she exhales deeply"
#    "Not quite a voice, but still communicating to you a signal"
#    "Something's not right"
#    "She exhales again"
#    "This time the flow of breath carries with it a small whimper"
#    "You step closer towards her"
#    "And look more carefully at her hand"
#    "The butterfly remains transfixed"
#    "..."
#    "It reminds you of the preserved butterflies pinned up around your enotmology lab."
#    "Beautiful, yet devoid of life"
#    "And then you realize"
#    "The butterfly is dead"
#    "You look down at her face"
#    "Two wet streams trace her cheeks down to her chin as she bites her lip"
#    "Staring at the thing that used to be a butterfly"
#    m "..."
#    "You don't know what to say"
#    "You think for a moment"
#    "'What's the matter... It's just a butterfly'... No..."
#    "'Why are you crying?'... You can't think of anything that doesn't sound insincere"
#    "..."
#    "You open your mouth in an attempt to muster up something to say"
#    ali "You know..."
#    m "?!"
#    play music "sad.wav"
#    ali "When people see a mushroom with spots like me... What do you think they think?"
#    m "Ummm... I uh... I think ummm like"
#    ali "Death... Toxicity... Poison... Hysteria"
#    ali "But you know... I'm not even that toxic"
#    ali "How many people do you think die from eating fly amanita?"
#    m "..."
#    ali "NOT A SINGLE PERSON IN THE LAST HUNDRED YEARS!"
#    ali "But still... That's what you all think of me"
#    ali "All anyone ever thinks about me"
#    ali "..."
#    ali "But you know... The worst part is..."
#    ali "Their fears aren't unwarranted"
#    ali "I kill the things around me"
#    ali "You know, they used to crush us up and mix us into milk to kill flies wanting to drink it"
#    ali "That's where the 'Fly' part of the name comes from "
#    ali "Isn't that weird if you think about it for a second?"
#    ali "If we are so scary, why would you mix it into the milk you drink?"
#    ali "I don't get it..."
#    ali "I don't understand anything"
#    ali "But I don't want to be something that causes suffering and death to everything around me"
#    ali "But that's how you all see me"
#    ali "By default"
#    ali "And there's nothing I can say that will change the way you all see me"
#    ali "I don't want to be like this!!!"
#    "Alice's voice slowly turns from words into incoherrent sobs"
#    m "..."
#    m "You know... ummm "
#    m "I'm not going to pretend I know everything about you..."
#    m "Or that I can talk for all human's or whatever"
#    m "But... I think I read a study about like... Japanese squirrels? I think?"
#    m "That were able to eat you guys. No problem..."
#    m "And so... I guess I was just thinking like"
#    m "Maybe it's not so black and white? That sure, maybe some people get the wrong idea, and think you're more of a threat than you really are"
#    m "But at least me... I think you're not that scary."
#    m "When we first met, I think maybe I was like what you said"
#    m "You did kind of freak me out"
#    m "But I sort of wasn't expecting the whole... You know? Living mushroom thing?"
#    m "And everything else"
#    m "So I'm sorry about that"
#    m "But right now... I think you're just like any other girl"
#    m "And I know maybe my opinion doesn't mean that much"
#    m "But I guess I wanted to say if you're feeling alone..."
#    m "I just wanted you to to know that..."
#    m "You have me... and..."
#    m " The squirrels I guess"
#    ali "..."
#    show butterfly_smile
#    #show alice smile cry
#    ali "That's so... stupid!"
#    m "I'm sorry..."
#    ali "And like... how would you know what a normal girl is like anyway"
#    m "I-"
#    ali "Hahahaha"
#    m "?"
#    ali "..."
#    ali "I'm sorry"
#    ali "I guess I got a little melodramatic"
#    m "It's okay"
#    scene black with fade
#    "She gets up and you keep starting walking again slowly"
#    "The sun has almost completely set"
#    jump day2WayHome

# label day2WayHome:
#    #Here is the original idea for the scene/ Feel like I didn't add everything I wanted to
#    #--------->
#    #choice whether to get her to open up adds a point to trust
#    #if trust is high enough
#    #she explains about her toxicity, and the danger she poses to those around her (people) in high doses
#    #at first she didn't have the tools to think about it, but she's starting to feel insecure about being perceived as dangerous

#    #here its important to talk about her lifespan as a mushroom too, whether or not she's edible etc.
#     #she discusses her view on death: i don't care about dying, as long as while i live i have some kind of meaning. I want to be loved.

#     #[maybe she has some kind of internal conflict where she's afraid of getting close to people because she's literally poisonous]
#     #but is it fine as long as she doesn't care about them? so she's scared of trusting someone, because her poison will hurt them
#     #and push them away, so its easier she doesn't even try
#     #or that she only uses them for sex, validation, then throws them away
# ##########################


# "You walk with Alice through along the embankment until you reach the outskirts of the city center"
# "Its hussle and bussle has died down partly due to distance from the crowds, and partly due to the day turning to evening"
# "However..."
# play music "date.wav"
# show alice normal at left
# show mc normal at right
# with easeinbottom
# ali "Hey do you hear something?"
# m "Hmm?"
# m "..."
# m "Yeah, I guess now that you mention it"
# hide alice with easeoutright
# m "Huh? Hold on slow down!!"

# #transition to alley way
# scene alley with fade
# show alice normal at left
# show mc pant at right
# with easeinbottom
# ali "The sound is coming from down here"
# m "*Huff* *huff*... Please... Don't... Run..."
# ali "What is this place"
# m "This- *cough*"
# show alice disappointed
# ali "Damn, you need to work on cardio"
# m "This place looks like a live music venue"
# m "If you go down those stairs, there's people listening to a band or something probably"
# ali "Hmmm..."
# m "See, there's a poster for an event on here"
# #MAKE THE NAME OF THE EVENT SOMETHING FUNNY#
# show alice normal
# ali "#name of the event#?"
# show mc normal
# m "Yeah, it's probably like a rock music thing from the vibes of the poster, and the little I can hear"
# ali "Rock music?"
# m "Yeah it's like... I don't really get it, but I think it's a kind of music where people sing about like..."
# m "Being really angry at your ex-girlfriend..."
# show mc normalside
# m "Or like... Killing people? Or like... Maybe it's about dying yourself?"
# m "I don't know... I feel like I have lots of conflicting ideas about it"
# m "But either way, it's generally more intense music that deals with more heavy topics"
# ali "That sounds kinda interesting"
# ali "I feel like human's usually avoid interacting with the more ugly parts of being alive"
# ali "But it sounds like some people go out of their way to think about it"
# m "Yeah. Some people like to escape from their problems, and others like to think about them all day"
# m "I guess human's are weird"
# ali "I'm guessing that what you listen to is more in the 'escaping from life' catergory"
# m "..."
# m "I've heard a little bit of this sort of music"
# m "Through my bedroom wall"
# ali "So your neighbour is into this sort of stuff"
# m "Yeah, I think he plays guitar too from the sound of it. He's pretty good too"
# ali "So that means you have connections with an insider?"
# m "What? I don't even know what he looks like. So talking to him is out of the question"
# ali "You've been living there for ages, and you don't even know what you neighbour looks like?"
# m "Nope"
# ali "..."
# m "..."
# show alice sly smile
# ali "..."
# show mc normalsquint
# m "Oh no, what are you thinking"
# ali "Hey, I was just thinking about how much I wanna learn guitar"
# ali "And well"
# ali "You're my only option"
# show mc stressed
# m "No way"
# show alice cry
# ali "*sob* How could you say that!"
# ali "To a cute innocent girl with only so many more hours left on the clock"
# m "..."

# #Choice: Give in to her, No means no
# menu:
   
#    "No means no.(N/A)":
#       "..."
#    "Give in.":
#       #Give in to her
#       ali "*sob* Ignore the last wishes of a petite, dying, defenseless-"
#       m "Fuck you... Fine!"
#       m "I'll go ask"
#       show alice excited
#       ali "Really!?"
#       m "Wait, you're actually excited?"
#       m "I thought this was just a way to make me suffer"
#       show alice pout
#       ali "Why are you so mean to me"
#       ali "Such an abuser"
#       m "Why do you have an interest in this all of a sudden though?"
#       show mc confused
#       m "Like I've spent the whole day showing you a bunch of stuff, and you didn't seem very excited about anything else"
#       show alice normal
#       ali "I've been thinking about it the whole day"
#       ali "At first I kinda of didn't understand why people care about stuff"
#       ali "like drawings, or food or video games"
#       ali "But thanks to everything you showed me, I think I started to get a better idea of why"
#       ali "And then I was kind of hoping something would just leap out to me"
#       ali "But I don't think life works like that"
#       ali "I think instead of waiting for a lightning bolt to strike down and give some kinda of divine intervention"
#       ali "You gotta just like"
#       ali "Do whatever seems fun"
#       ali "And I kinda can't keep waiting."
#       ali "I don't have that sort of time"
#       ali "..."
#       ali "So I'm gunna go with this!"
#       m "..."
#       show mc slightsad
#       #he's not sad here because of talking to neighbour, but because he's jealous about her attitude
#       m "I'll see what I can do."
#       stop music fadeout 2
#       jump Day2Neighbour


# #choice whether to get the courage to talk to neighbour
# #how does alice respond if you don't do it

# #how does mc deal with needing to concur the anxiety to knock.
# label Day2Neighbour:
#    scene black with fade
#    "You get back to your place, and lead Alice inside."
#    "You place your things on your table and then go out the door you just came from."
#    scene hallway with fade
#    show mc normal with easeinbottom
#    m "Okay... It's not that scary... It's just talking to a person."
#    show mc worried
#    m "A person that you have never seen before."
#    m "Who could be a serial killer, or... a scientologist or something"
#    m "But probably not!"
#    show mc stressed
#    m "... Hopefully"
#    m "Just gotta knock at that door..."
#    m "Just a little rap-a-tap-tap..."
#    show mc vstressed at bounce
#    m "FUCK!!!"
#    show mc sad
#    m "Why is this so hard?!!"
#    show mc stressed
#    m "You know fuck it, I don't think I can-"
#    play sound "door.wav"
#    show kellin at left with easeinbottom
#    na "Uhh, are you okay?"
#    play music "normal.mp3"
#    show mc shocked at bounce
#    pause 1
#    show mc shocked at right with move
#    m "AAH! ummm, Yeah, I was just!... Uh, you know... Ummm..."
#    na "Did you need something? I heard mumbling and feet shuffling outside so?"
#    # make text very small
#    show mc worried
#    m "Uhh yeah, so I was kinda of ummm, sent here to ask a favour, but like I don't even know you, or like said my name and I"
#    na "Slow down, just take it easy"
#    #what to make his name? Maybe like Kellin, or Ryland or something
#    kel "First off, hi, I'm Kellin. I don't think I've met you before? Do you stay in the dorms?"
#    #here add that he recognizes you from yesterday
#    m "Uhhh... Yeah, next door actually..."
#    kel "Woah! So your the one that's been here the whole time! I tried to leave a package for you the other day but!"
#    m "Yeah I'm not too great at talking to people... Or waking up" 
#    m "Sorry about that"
#    kel "No, it's okay, you're probably a really good listener!"
#    kel "Damn we've been next-door room buddies for like... How long now?"
#    m "Uhhh... Like 2 years"
#    kel "Woah that long already? Good times..."
#    kel "By the way, I still don't know your name"
#    m "Oh it's player name"
#    kel "Nice to meet you!"
#    kel "So what do you need?"
#    m "Uh, I've just heard you playing guitar and listening to music and stuff through the walls and ummm "
#    kel "OH! I'm so sorry, I must have been blasting it too loud! I'll try be careful from now on!"
#    m "No, uh-"
#    kel "It's okay you don't have to be polite!"
#    kel "I'm so sorry, I should have been using headphones to being with"

#    #Maybe it would be funny if he keeps going on about it to the point of crying but mc isn't able to interject properly
#    #i think that's a good dynamic, like he just talks a lot and comes to his own conclusions, and the mc can't correct that
#    #But then how do you end the exchange, and move to the next point?
#    #I like the idea of him being super ADHD but very like　　マイペース

#    #He's basically an embodiment of the hyper fixation element of autism, so showing of the positives of it 
#    #compared to the anxiety and social awkwardness of mc
#    show mc stressed
#    m "No, you're fine, that's not it"
#    m "I was just wondering if uhhh... Damn I guess I don't know you well enough to ask anything"
#    kel "You don't have to say anything... I know why you're here!"

#    #Alternative progression: You nervously being trying to ask
#    #he ends up getting over the toply worried expecting that you are going to tell him about someone being murdered on the floor or something
#    #his assumption about the situation is that something bad MUST have happened, because he's picking up how stressed you are

#    kel "I see right through you... To your soul!"
#    show mc shocked
#    m "!?"
#    kel "I accept your proposal"
#    m "Huh?"
#    kel "So if I'm doing guitar... Maybe backing vocals, then what are you going to be doing?"
#    kel "Don't tell me! You have the vibes of a bassist!"
#    kel "But if you were, then I would have heard you through the wall"
#    kel "So you must be a drummer! You must go to like a practice studio right!"
#    kel "It's so inconvinient to be a drummer living in a communal space right!"
#    kel "So when is our first practice session? Do you have any songs done yet?"
#    show mc worried
#    m "I don't uh... Know how to play drums"
#    kel "You're so humble! That's such a good quality in a band member!"
#    m "No like, literally I've never picked up a drum stick"
#    kel "Oh so then what do you play?"
#    kel "Wait don't tell me... Kalimb-"
#    m "I can't play anything"
#    kel "WOAH, so you're fresh blood! That's so exciting"
#    show mc sad
#    m "Yeah, I guess you could say that"

#    m "(Damn, he's so nice, but I'm already so exausted from this conversation.)"
#    show mc stressed
#    m "I know we've never talked before"
#    m "And this is a big ask..."
#    show mc worried
#    m "but I was wondering if..."
#    m "I could ummm..."
#    kel "Sure, I'll get it ready"
#    show mc shocked
#    m "I haven't even asked yet!"
#    kel "What are you talking about? I told you! I get you!"
#    kel "You don't need to say anything to me! Our brains are connected on the same wavelength!"
#    show mc worried
#    m "Uhh... yeah... sure..."
#    kel "Come inside!" 
#    m "...Okay..." 

#    scene neighbour_bedroom with fade:
#       zoom 0.9
#    play sound "door.wav"
#    show mc awed at right
#    show kellin at left
#    with easeinbottom
#    m "Woah this place is really... something"
#    kel "I guess? Isn't it normal?"
   
#    m "Uh, if this is normal, then I think your reference point is kinda busted"
#    kel "So this is what you wanted right?"
#    kel "I have a couple guitars, but this is the only one that's not in a weird tuning right now"
#    show mc confused
#    m "Tuning? uhh"
#    kel "Most guitars are tuned in fourths starting from E, with the exception of the major third between the G and B strings"
#    kel "But recently I've been really into this emo tuning that's tuned to like an A major chord with a D in the bass"
#    kel "I also have an 8 string over here that's tuned-"
#    m "So guitars have strings... I think? and ummm emo?"
#    #maybe do the emo copypasta?
#    kel "I haven't changed the strings on this one for a while so if this is okay then"
#    show mc worried
#    m "Are you sure it's okay, Kellin?"
#    kel "Yeah, I don't really use it either way..."
#    kel "Oh you probably want this too"
#    kel "And this and..."
#    stop music fadeout 2
#    scene black with fade


#    show bottle night with Dissolve(2):
#       zoom 0.9
#    play music "night.mp3"
#    show alice normal at left
#    with dissolve 
#    play sound "door.wav"
#    show mc stressed at right with easeinbottom
#    #mc with guitar in soft bag on back and arms fulled with stuff
#    show alice surprised
#    ali "Woah, you got it! Thanks but..."
#    ali "I thought you were just getting a guitar, what's all that"
#    m "A tuner, an overdrive, compressor and delay pedal, a practice amp-"
#    ali "That's-"
#    m "-headphones, a box of picks, 2 instructional dvds-"
#    show alice neutral
#    ali "Uh-"
#    m "-3 live dvds, 8 cds..."
#    m "And one vinyl"
#    ali "Geez"
#    show mc normal
#    m "I managed to turn down the record player"
#    "I guess we're lucky you have such a supportive neighbour"
#    show mc normalside
#    m "yeah... But I can't help the feeling that maybe I'm doing him a favour by giving him someone new to rant at"

# label day2GuitarSetup: 
#    show alice excited
#    ali "So can we set it up? Please!?"
#    show alice hime
#    ali "...I mean, if you're free right now that is."
#    show mc normal
#    m "Uh yeah, lemme just try to figure out how to get it in tune."
#    show alice happy
#    ali "That's fine, I can do it."
#    show mc confused
#    m "Are you sure?"
#    show alice laugh
#    ali "Just pass it here!"
#    # string tuning sound
#    "*Snap!*"
#    # string snaps
#    show alice shocked
#    show mc sad
#    ali "Eek!"
#    show mc stressed
#    m "I mean, he did say that it needs a new set of strings..."
#    show alice sad
#    ali "Uwa, what do we do, should we call the police?"
#    ali "They'll know what to do right?"
#    show mc normal
#    m "We can just get a new set tomorrow. It's too late now"
#    m "For now we'll just have to make do with those"
#    show alice pout
#    ali "...I guess..."
#    #start some really bad beginner guitar experimenting
#    "I guess that's my obligations for the day over..."
#    "Let's check if there's any new meme compilations"
#    stop music
#    show mc awed
#    "..."
#    "3 missed calls from dad"
#    "You haven't talk to him in almost a month"
#    show mc stressed
#    "Fuck"
#    "Should I text him an excuse for why I can't talk now?"
#    "Or should I call him now?"

#    menu:
#       "What should I do?"
#       "Make an excuse(N/A).":
#          "..."
#       "Call him back.":
#          show mc stressed
#          m "Hey, uh... I need to go make a phone call."
#          jump day2PhoneCall
# #choice -> call back?
# #if call back trust++ - Why?

# label day2PhoneCall:
#    scene black with fade
#    play music "wind.wav"
#    "You climb up to the roof and tap the call button"
#    scene rooftop with fade
#    play sound "phonecall.mp3"
#    "Ring..."
#    "ring..."
#    "...ring..."
#    stop sound
#    dad "Hello?"
#    show mc stressed
#    m "Hey dad... How's it going?"
#    # I think maybe it's better that he opens with like "Hope you aren't partying too much"
#    # I haven't heard about your grades but you're staying on top of it right?
#    # That's the agreement, You get As, and I pay for your internet, food, utilities
#    # If not, you're an adult... You're old enough to figure something out
#    dad "Well it was doing pretty good"
#    dad "I went down to the shop to see how the work on my car is going"
#    dad "I was just talking to the mechanic about what kind of engine to import"
#    dad "And then... I got a notification from the card I gave you"
#    show mc worried
#    m "*gulp*"
#    dad "And I saw you've been doing some {i}clothes shopping{/i}"
#    show mc surprised
#    m "Uh... yeah"
#    show mc worried
#    m "So it's come to this..."
#    m "I can expl-"
#    dad "You finally have a girlfriend?"
#    show mc confused
#    m "Huh?!"
#    dad "I mean that's the only thing I can think of"
#    dad "You're not one of {i}those{/i} people to go buying stuff from women's stores for yourself"
#    m "..."
#    show mc awkwardsmile
#    m "Uh, yeah, haha..."
#    m"... Of course not"
#    dad "So you're going to introduce me sometime right?"
#    m "uhh"
#    dad "I looked through all your social media looking to see if I could find her, but I didn't see anything, seeing how you never post"
#    dad "You don't have any accounts I don't know about do you?"
#    show mc slightsad
#    m "Uh no..."
#    dad "Good."
#    show mc sad
#    m "Is that it?"
#    dad "Yeah, I'm going to get back to making my moonshine"
#    dad "You remember I showed you the distillation rig I built right?"
#    m "Uh yeah... Have fun!"
#    dad "Will do, {i}son{/i}."
#    dad "Later"
#    stop music fadeout 3
#    scene black with fade
#    jump day2DeepTalk

# label day2DeepTalk:
#    "You go back downstairs to your room."

#    play music "night.mp3"
   
   
#    show bottle night with Dissolve(2):
#       zoom 0.9
   
#    show alice serious at left
#    with dissolve 
#    play sound "door.wav"
   
#    "Alice is sitting there and has already figure out some basic chord progression kind of stuff"
#    show mc normal at right with easeinbottom
#    m "..."
#    ali "*focused silence*"
#    show mc normalside
#    m "Looks like you're having fun"
#    ali "Yeah... I feel like I'm starting to get the hang of this"
#    show mc slightsad
#    m "That must be nice."
#    show alice annoyed
#    ali "Hey, are you angry or something? Did I do something?"
#    show mc stressed
#    m "No... It's whatever, just go back to your noodling."
#    show alice normal
#    ali "If that's what you want then fine..."
#    "she plays but it gets more aggresive and she pauses every once in a while."
#    "..."
#    show mc vstressed
#    "she keeps playing and you just sit there..."
#    "It boils up..."
#    "Until you just can't take it anymore."
#    show mc vshout
#    m "Are you going to keep playing all night? How am I supposed to relax like this?"
#    show alice angry
#    ali "Huh? What's up with you? I've literally done nothing and you're being super passive aggressive for no reason."
#    show mc shout
#    m "It's not for no reason! I go through all the effort to setup all this stuff for you, and you..."
#    show alice serious
#    ali "And I what?"
#    ali "Have fun and use it?"
#    show alice annoyed
#    ali "Sorry for existing I guess."


#    #choice as to whether to fully give into it or whether to take a step back
#    #[I think all of the decisions need to be subtle, not GOOD CHOICE or BAD CHOICE]
#    #She's on the verge of tears, and you take a step back

#    #choice 1 "I'm jealous of you"
#    #choice 2 "You're so selfish"
#    show mc vannoyed
   
#    m "You don't get it..."
#    m "You just start learning guitar on a whim."
#    show mc sulk
#    m "And you're already better than I've ever been at anything."
#    m "In literally the span of hours."
#    show mc stressed
#    m "What the fuck am I supposed to do?"
#    m "I'm not good enough for my parents."
#    m "And I'm not good enough for myself."
#    show mc slightsad
#    m "I'm a fucking loser, and yet I tell my self I'll learn to draw."
#    m "Or learn an instrument."
#    show mc shout
#    m "Or fucking anything."
#    show mc sad
#    m "I just want to like myself."

#    m "But even then..."
#    m "I know it will never be enough"
#    show mc slightsad
#    m "I'm never going to be enough for my parents"
#    m "Because all they want me to be is the person they THINK I am"
#    show mc vannoyed
#    m "But I CAN'T be that person!!"
#    m "I've never been that person..."
#    show alice neutral
#    ali "..."
#    show mc normalside
#    m "They think I'm a straight A student, with lots of friends."
#    m "My dad is making up fantasies of me having a girlfriend and living up to how he was in college"

#    m "I don't even know what he would do if he found out"
#    show mc cynical
#    m "Who I {i}actually{/i} am"
#    show mc stressed
#    m "That I'm on the verge of flunking out"
#    m "That I have no friends"
#    m "That I'm not like him..."

#    # nuance of disgust
#    show mc sulk
#    m "I just feel like..."
#    m "Time keeps moving..."
#    m "And I'm still alone... Here... In my room."
#    m "But I can't stay in college for ever."
#    m "I'm going to drop out or scrape through."
#    m "And then I'm going to work doing some crappy deskjob I hate, until I get old..."
#    m "And then I die."

#    ali "..."
#    show alice sulk
#    ali "You know.. It's kind of funny"
#    show mc normal
#    m "?"
#    ali "How when it was me wanting attention"
#    ali "You could rationalize all the reasons why I was being stupid for wanting that"
#    ali "But you..."
#    show alice normal
#    ali "You're the exact same."
#    show alice disgusted
#    ali "Get over yourself."
#    ali "You're drowning in your own tears about only having another 60 years left to accomplish something."
#    show alice sulk
#    ali "How do you think I feel?"
#    ali "I have one more day"
#    ali "..."
#    show mc sad
#    m "I'm sorry..."
#    show alice normalside
#    ali "It's okay..."
#    ali "I haven't spent that much time with you."
#    ali "Or you know, being alive."
#    show alice serious
#    ali "But I think maybe, you're waiting for an excuse."
#    show mc confused
#    m "What do you mean?"
   
#    ali "You took me to a whole bunch of places and showed me a bunch of stuff."
#    show alice confused
#    ali "and at first I thought it was meaningless."
#    show alice normal
#    ali "But I realized that nothing matters except what is important to you."
   
#    ali "Latte art is just making pictures in cow boob juice."
#    ali "And video games are just what depressed people do to avoid dealing with real life."
#    # Too much
#    ali "But even then."
#    show alice serious
#    ali "Those are things that bring meaning to people."
#    ali "Every single thing you could be interested in."
#    ali "has so much depth when you actually look into it."
#    ali "Every rabbit hole runs so deep."
#    show alice normalside
#    ali "And I guess what I'm trying to say is"
#    show alice sad
#    ali "You can't wait for someone else to give you permission to act" 
#    ali "To do what you want with your life"
#    show mc worried
#    m "But what if it doesn't work out?"
#    show alice sigh
#    ali "Well then you're back where you started."
#    ali "And you can find another reason to live"
#    ali "Humans are good at that"
#    show alice happy
#    ali "So I guess in the meanwhile, all you can do is find a waste of time that feels special to you"

#    # I'm worried this reads as preechy and goes against do don't say
#    show mc awed
#    m "...Thanks"
#    show alice sly smile
#    ali "Don't mention it"
#    show mc normalside
#    m "I guess... I think you're right..."
#    show mc stressed
#    m "I don't really know what I'm going to do yet but... I think I'm going to stop thinking about everything I want to do."
#    m "Everything I want to be."
#    show mc sad
#    m "And just pick something and see where it takes me."
#    show alice happy
#    ali "Well as long as you're having fun right"
#    show mc normal
#    m "... I think I'm kind tired after going out today"
#    m "Kind of a bit past my threshold for exposure to humans"
#    show alice normal
#    ali "You going to go to bed?"
   
#    m "Yeah I think so..."
#    show mc awed
#    m "Do you mind switching to headphones?"
#    ali "Sure"

#    scene black with fade  
#    window hide
#    stop music fadeout(3)
#    show chibi_sleep at truecenter with dissolve
#    show top_text "You crawl into bed and fall asleep to the dull sound of unamplified guitar sounds" with dissolve 
#    pause 3


#    play sound "yay.wav"
#    "END!!!"


# #defuse by doing something together, show her music on youtube?  maybe you show her a little bit before, and then something after?
# #You make a promise that tomorrow you would go to a music store and buy a new set of strings

# #contrast of how the 2 of them argue

# #Alice: short and cold and precise when she's argueing, but when she's really hurt, will also do insults she doesn't mean. More petty. Tends to run away, when like this.
# #MC:bottles up, tries not to express, but if he panics, he word vomits, with internal stuff leaking out. Sometimes he deflects and blames others. Focuses on what-ifs, over thinker.

# #FOCUS:You can't live for conditional love: pretending to be something you're not, when you only live one.














# Skye ver September edit below - edited by Sabrina
























#aim for 1700-2000 lines across all endings

label day2Morning:

   # variables for Alice:
   default arcadeWent = True


   


   #It's very important that alice has fun making fun of mc, in a sadistic way, but almost like nagatoro
   #It starts cruel, but gradually starts to reveal that at her core she really cares about him


   #wake up
   #she waters herself

   #if trust == 0 then she's mopey, so make sure enough chances to get it to be > 1
   #talk to her



   # (Shes left hunderds of tabs open on your laptop)

   scene day_clouds
   show bedroom_opencurtains
   show dirty1
   show dirty2
   show bottle

   show mc stressed at right
   show alice pout at left
   with easeinbottom

   play music "normal.mp3"

   ali "So are you going to just keep lying there, or...?"
   show mc normal
   "You open your eyes to see Alice looking down on you"
   ali "You've been lying there for a while now... Aren't you bored?"
   show mc vannoyed
   m "Don't you know what sleep is?"
   ali "Yeah, but you're only supposed to do that for 8 hours..."
   show alice disappointed
   ali "At night time." # might be better to say "... and at night"
   show mc normal
   "You look over to your table, and pick up your phone"
   "It's dead. Not like anyone ever messages you anyway."

   m "What time is it?"
   show alice normalside
   ali "Well you've been out for like... 12 hours"
   show mc confused
   m "Oh, so it's probably like 1pm or so?"
   m "What's the issue?"
   show alice disappointed

   ali "You're such a waste of space"
   ali "I'm honestly impressed you had time to remember to water me between sleeping the day away and listening to people on YouTube tell you what cartoons are worth watching"

   m "How do you know what YouTube is?"
   #Elongate
   #Or just change it to say videos?

   m "...I was also... writing stories..."
   show alice laugh
   # make sure this makes sense in context
   ali "You didn't even TRY to deny it"

   ali "I bet you didn't even finish a single chapter"
   show mc humiliated
   m "..."
   show alice laugh cruel
   ali "See?"


#This part needs to be changed:
#it's not that she's perceptive, it's that you aren't used to someone else voicing negative thoughts about you


   "It's like she's reading your mind"
   "She puts to words the things you think about yourself before the thought is even fully formed"
   # shes better at hating you than you ever could be.
   # the one thing you were good at and you have been outclassed
   "It's like she sees right through you"
   m "..."
   "You turn your head down towards the messy duvet you're sitting on to avoid her gaze"
   #she says one more mean thing here, insulting your aethstetic and clothes
   #realizes that you're crying and is kinda shocked, then tries to make you feel better (softens up)
   show alice normal
   ali "Ummm... If you want I could help you... you know?"
   ali "Look less like your mom picks out your clothes from the bargain bin"

#    Alice wants to try go to the mall to experiment with finding a new way to express herself the only way that she knows how: through her appearance.
# The MC tries to use this as an opportunity to expose her to new things: and maybe find something for her to find meaning in.

   m "Is that supposed to be an apology?" #  "Is that supposed to be an make me feel better?"
   ali "Whatever, do you want my help or not?"

   #maybe need to explain that although she's only a day old, she has instinct for only few things:
   #Fashion/beauty, the need to be desired, knowledge on her species, as well as arts
   #(although the company programming tries to make her forget about that part)
   #maybe try to develop that motif a bit about like, her needing to fight her programming
   show mc normalside
   "You pause for a moment to think about the offer"
   "You would need to go outside"
   "Where \"people\" are"
   m "Ummm...Not really"


    # I think maybe it makes more sense that it's the mc trying to get alice to go out with him, not the other way around. She gets roped into it by the prospect of clothing


   show alice shocked
   #Like GAN face here with sound effect, let it be sort of slapstick
   ali "but... I..."
   ali "..."
   show alice angry tears
   ali "Fine, whatever! Die alone virgin! See if I care!"
   show mc shocked at bounce
   m "!"
   m "No wait, it's fine! We can go! Wherever- Whatever you want"
   show alice excited
   ali "Really?"
   show mc confused
   m "..."
   ali "..." # tsundere alice sprite
   show alice hime
   ali "Hmph, fine, if you wanna go so bad, I guess I have no choice then..."
   show mc normalside
   m "{size=-10}That was easy"
   show alice normal
   ali "{size=+10} Did you say something?"
   show mc stressed
   m "No! Let's just go."
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

   #Develop this conflict
   #You didn't want to fight and you feel sorry for her since she's going to die soon anyway
   "You try not to think about the thought of other students seeing you leave the dorm together with a girl"
   #talk a little more about the traveling process and getting to the mall
   window hide

   hide chibi_mc
   hide chibi_alice
   with easeoutleft

   jump day2date

label day2date:
#    The mall setting serves as a perfect backdrop for Alice’s exploration of self-expression. Her desire to use appearance as a form of validation reflects her programming,
# while the main character’s attempts to show her deeper forms of meaning create an interesting contrast.
# The arcade scene highlights Alice’s lack of understanding of human activities.
# The main character’s explanation of video games as a form of connection and self-improvement could be a moment where Alice starts to see value in things beyond physical appearance.

   scene mall with Fade(0.5, 1.0, 1)
   show mc normal at right
   show alice surprised at left
   with easeinbottom
   ali "Woah, what is this place?"
   show mc normalside
   m "I've only heard rumours, but I believe this place is called a \'mall\'."
   show alice awe
   ali "A \"mall\"..."
   ali "Why would you stay inside all day when there are such vibrant places like this so close by?"
   show mc worried
   m "Well... It's loud and there's lot's of people..."
   show alice confused
   ali "Hmm? That's such a stupid reason? I don't get it."
   ali "Anyway, now that we're here, let's try and find some stuff to gaslight people into thinking you're not a loser"
   show mc confused
   m "How do you know what gaslighting is?"
   show alice sly smile
   ali "Does anyone REALLY know what it is?"
   m "Yes?"
   jump clothes
   # menu:
   #    "You notice Alice looking at a clothes store..."
   #    "Offer to go.":
   #       jump clothes
#Maybe move this scene to after the date scene
#Make it a choice of "Where you see her looking"
#And make it requirement for true end

#todo:make this scene more subtle ali "Anyways, it's still pretty early and we are here already so let's go somewhere else."
   show mc confused
   m "Like where?"
   show alice confused
   ali "Hmmm... I don't know..."
   show mc normal
   m "Do you have any hobbies or whatever?"
   show alice cruel
   ali "Oh yeah, I {i}love{/i} to crochet on the weekends after finishing at the office~"
   show alice mendokusai
   ali "I'm a mushroom that was born literally a day ago, why the fuck would I have hobbies?"
   show mc stressed
   m "...Sorry..."
   show alice normal
   ali "Whatever... So, where are we going?"

   #Maybe add a bit here about being thirsty so the cafe is a neccessary event
   "You've haven't been to the mall since you were in elementary school."
   "Let alone with a {i}girl{/i}."
   show mc normalside
   "Where would she want to go?"
   jump aliceDay2DateLocation

label aliceDay2DateLocation:

   menu:
      "Quickly get this over with.":
         jump cafeDate
      "Show her something you like.":
         if alice_rp >= 10:
            jump arcadeDate

         "You think about taking her to somewhere you would want to go."
         "But then you look over at her, and see her impatiently tapping her foot."
         "You don't want to drag this out any longer than it needs to be."
         jump aliceDay2DateLocation

   # choice: [Quickly get this over with, Show her something you like]
   # >Show her something you like
   #    if(trust)>x:
   #       jump arcadeDate




# while out, she makes comments here and there that show her interest in
# creating and having a sense of identity/srtle.
# eg. “If I made this game, I’d make the characters cuter or something.”
# /“Could you draw X on this latter instead?”

#move to day 1 maybe
#label arcadeDate:

#    The arcade scene highlights Alice’s lack of understanding of human activities.
# The main character’s explanation of video games as a form of connection and self-improvement could be a moment where Alice starts to see value in things beyond physical appearance.

   # show mc normal
   # m "I think I saw a sign for an arcade back there"
   # show alice confused
   # ali "An arcade?"
   # m "We could go and I could maybe try show you how to play some video games."
   # show alice disappointed
   # ali "Are you for real right now?"
   # show mc confused
   # m "You want to find stuff you're interested in right?"
   # show mc annoyed
   # m "How do you know you don't like it if you don't give it a go?"
   # show alice pout
   # ali "..."
   # show alice mendokusai
   # ali "...FINE~"
   # scene arcade with fade
   # show mc surprised at right
   # show alice disappointed at left
   # with easeinbottom
   # #black scene


   # #Change this so alice has an appropriate amount of knowledge about this stuff
   # $ arcadeWent = True
   # m "Woah, look at this place! They have so many retro titles!"
   # show alice normalside
   # ali "Isn't that like a nice way of saying they're charging a dollar for games that have been out of date for like 30 years?"
   # show alice confused
   # ali "Can't you play these on your computer anyway?"
   # show mc normalside
   # m "I guess I could set up a MAME emulator on RetroArch, but-"
   # show alice annoyed
   # ali "Are you listening to yourself right now?"
   # ali "I have no fucking clue what you're talking about."
   # show mc awed
   # m "I just meant like, we could use my PC..."
   # show mc normalside
   # m "but then we're really compromising on the authenticity of the experience."
   # show alice smug
   # ali "The experience of being in a run down shit hole?"
   # show mc surprised
   # m "Woah! They have that weird train game?"
   # show mc happy
   # m "It's a weird Japan-only game where you play as a train conductor and like, there's train levers, and-"
   # show alice neutral
   # ali "You're really making this whole gaming thing so SO cool."
   # show mc normal
   # m "Well there's a whole bunch of other games too."
   # m "What kind of thing do you think you might like?"

   # show alice confused
   # ali "I don't know... What about that one over there?"
   # show alice happy
   # ali "Those little dinosaur things are kinda cute~"
   # show mc happy
   # m "Oh Bubble Bobble?"
   # m "I haven't played that game since I was a kid."
   # m "Lemme get some tokens..."

   # #interlude
   # show black with dissolve
   # "You show Alice how to move, blow bubbles, and capture monsters."
   # "She quickly grasps the basics and is able to beat the first level without any issues."
   # "However, after only a few levels, the difficulty begins to increase dramatically, and before more than a few minutes have passed..."
   # show alice annoyed
   # hide black with fade

   # ali "Game Over? What the fuck is this shit?"
   # show mc annoyed
   # m "In these kind of games you only get a few lives, and if you use them all up, you need to pay more to keep playing."
   # show mc happy
   # m "Do you want to keep playing this?"
   # show alice sulk
   # ali "What's the point? What do I {i}get{/i} if I keep playing?"
   # show mc awed
   # m "Well... The satisfaction of having gotten further, and accomplishing something that not many people have done?"
   # show alice annoyed
   # ali "That's stupid."
   # ali "Who cares if you are the best in the world at playing stupid children's games?"
   # show mc normal
   # m "..."
   # show mc sulk
   # m "It's not stupid to me..."
   # m "...or lots of other people."

   # m "These games represent memories of our childhoods."
   # m "Friendships."
   # show mc normalside
   # m "Although looking around here, you might not get it but..."
   # m "There are all sorts of games."
   # m "Games about guns, games about fishing, games about defusing bombs."
   # show mc stressed
   # m "Games about just talking to people."
   # m "Games that give you a new outlook on the world..."
   # show alice neutral
   # ali "..."
   # show mc awed
   # m "Games to play by yourself, games to pass the controller back and forth..."
   # m "Games that let you meet new people."
   # m "I think that for me, it helps to feel connected to something bigger."
   # m "The community of people brought together by having this small thing in common."
   # show mc normalside
   # m "I just thought it would be cool if you would be able to find something like that too."
   # show alice pout
   # ali "..."
   # show alice sulk
   # ali "I guess..."
   # show alice normalside
   # ali "I'm sorry okay?"
   # ali "I shouldn't have called it stupid."
   # show alice normal
   # ali "But even so, I don't really think this is for me."
   # ali "Maybe if I had more time to find one that speaks to me."
   # ali "But right now, I want to find something else."
   # show mc slightsad
   # m "..."
   # m "Okay... let's try and find something else."
   # m "How about..."
   # #obv need different dialogue path if it's not the first option
   # #Choice
   # jump cafeDate


label cafeDate:
# The latte art scene offers a poignant lesson about the impermanence of art and the importance of the process rather than the outcome.
# This could subtly parallel Alice’s own fleeting existence and her search for meaning within it.
# The barista’s philosophy on art could resonate with Alice, planting the seeds for her eventual embrace of music as a form of expression,
# even if she doesn’t fully grasp it yet.
   # scene mall with fade
   # show mc normal at right
   # show alice normal at left
   # with easeinbottom
   "You walk past a small cafe. It looks relatively empty, despite how busy the rest of the mall is."
   "The tile-floor and decor look clean and without wear."
   "This place is probably new."

   m "Do you wanna go inside and get something to drink?"
   show alice neutral
   ali "...As long as I have my water spray, I'm fine. I don't really get that whole animal thing of 'eating' in order to 'sustain' yourself."
   show mc normalside
   m "Well, there are plenty of reasons to eat and drink stuff, even if it's not purely for sustenance."
   m "Lots of people eat and drink stuff purely for enjoyment."
   m "Going out for food is something a lot of people do as a way of seeing new places and experiencing new things with people."
   m "Making memories, that sort of stuff."
   show alice sly smile
   ali "When was the last time you went out to eat with someone?"
   show mc stressed
   m "..."
   show alice cruel
   ali "Figures."
   show mc normal
   m "Anyway, I still need to do that whole animal 'eating, drinking' thing"
   show alice hime
   ali "I don't get it... But like, whatever, if you're so adamant about this whole thing and it's {i}sooo{/i} important to you, I guess I'll give it a go."
   window hide
   #screen transition
   stop music fadeout 2
   scene mallcafe with fade
   play music "mallcafe.mp3"
   show mc normal at right
   show alice normal at left
   with easeinbottom
   "A young waiter is sitting at a desk by the storefront, flicking a pencil around a notebook propped up at the corner of the desk at an angle."
   "He looks up, notices us, and turns his gaze back to the paper, continuing as he was for a few more seconds before slowly getting up out of his seat."
   na "Welcome, can I get you guys a table?"
   show mc worried
   m "..."
   ali "..."
   m "..."
   na "...Ummm... Are you okay?"
   show mc vstressed
   m "yEahh, umm I... uhHh.... 2 please?"
   ali "Uh, I don't think we need 2 tables, unless you wanna sit by yourself"
   m "No, I meant like... Uhhh... Just the 1 table for the 2 of us..."
   na "*Giggles* Sure, right this way."
   show alice disappointed
   ali "God, I forgot you can't talk to anybody except for your stuffed animals."
   show mc worried
   m "I didn't think entering a store would mean talking to someone."
   show alice mendokusai
   ali "I'm a mushroom with no knowledge of the world except for the small amount of info I was biologically programmed to know."
   ali "But even /I/ know that's how this works."

   show black with dissolve:
      alpha 0.5
   "You are escorted to a large table, with 2 chairs on one side, and a couch seat against the wall on the other."
   "Alice swiftly slides onto the couch chair, without a word"
   #She picked the more comfortable choice without second thought
   hide black with dissolve
   show mc normal
   show alice normal
   m "..."
   ali "..."
   m "..."
   show alice confused
   ali "So... When does this get interesting?"
   show mc normalside
   m "Well, after the waiter comes back we can tell them what we want to order."
   m "And then we wait for it to be prepared."
   m "Eat."
   m "Then pay for our order and leave."
   show alice disgusted
   ali "So it's just waiting for food, eating and then you leave? And this makes memories how?"
   ali "And you guys have to do this like..."
   ali "3 times a day?"
   show mc worried
   m "Yeah, but there's still like... Ummm... You know? It's different when you go somewhere to do it."
   show alice normalside
   ali "If you're so desperate for a change of scenery while eating, then can't you just like, eat in the shower or something?"

   na"Are you guys ready to order?"
   show mc shocked at bounce
   "Damn, he snuck up on me... We still haven't decided!"

   #maybe try do like tumblr cry text where it's like "I sorRi; I jsut cant't' doo it"
   show mc stressed
   m "ummm... Uhh, just one... sec; pleaSe"
   show mc shocked
   m "Alice, We've got to decide! Have a look at the menu!"

   #screen transition
   show cafe_menu at truecenter with easeinbottom
   play sound "page.wav"
   #Are there any foods that mushrooms can't break down/ mould doesn't grow, that might be on a menu?
   show alice annoyed
   ali "What the hell am I going to do with a toasted cheese sandwich?"
   show mc sad
   m "Come on, please just pretend to TRY to enjoy yourself."
   show alice laugh
   ali "OMG I'm so excited to order 2 pieces of bread, with fermented cow mammary extract melted between!"
   ali"I'm actually quivering in anticipation to put it in my mouth, digest it and then wait for 8 hours, and then-"

   m "Please! Just... like... Come on, how about this? This one looks kind of cool? Right?"
   show alice annoyed
   ali "Latte art? Like a drawing of coffee? And you eat the paper?"
   show mc normalside
   m "No, they ummm... Make like an image on top of the coffee by pouring the foamed milk into the coffee so it makes a picture"
   show alice sly smile
   ali "You guys really love drinking stuff from cow boob's huh? Is it like a sex thing or..."
   show mc stressed
   m "No!"
   show alice confused
   ali "So lemme get this straight? Somebody like, puts in the effort to make some kind of drawing out of foam, and then you just... drink it?"
   show mc normal
   m "Yeah."
   show alice sigh
   ali "I have never heard of something-"
   ali "So-"
   show alice disgusted
   ali "Stupid in my life."
   show mc slightsad
   m "You've been alive for like 24 hours."
   show alice annoyed
   ali "THE POINT IS!"
   ali "Why would you make something that's just going to get destroyed a few minutes later? What's the point?"

   #Kind of a metaphor for life, especially with it being as short as it is

   m "Okay so if it's so stupid, then what ARE you going to order then"
   ali "..."
   ali "Fine, you've piqued my interest, let's see what this is about"

   hide cafe_menu with easeoutbottom
   play sound "page.wav"
   #screen trans
   na "So are you guys ready to place your order now?"
   show mc worried
   m "...Umm. I, umm. could I please...2... uhh."
   show mc stressed
   "You give up and point towards the listing for latte art in the menu."
   "The waiter bends over to look at the item you're pointing at, and after spending a second processing, his expression suddenly changes as if suddenly jolted awake"
   na "Two latte arts right? Coming right up!"
   "He energetically snatches the menus off from the table, and practically skips away."

   #scene trans
   "..."

   na "Sorry to keep you waiting!"
   show alice vannoyed
   show mc normal
   "Barely 5 minutes had passed since the order was placed, the waiter returns balancing a tray in one hand."
   "He carefully places the tray down onto the table and without missing a beat, begins to explain the items."
   na "Over here, for you, I thought you might like something cute and uplifting to freshen up the bags under your eyes."
   "He places a coffee cup in front of you with a detailed illustration of a small rabbit running through a flower garden."
   na "And for you, I thought you might like this butterfly."

   #She relates to it because butterflies are only alive for mating, but they mean so much more
   #So she relates to them

   #When she kills it, she's more like, I killed it before it even fulfilled it's task
   #So it opens up more doubt into why she is pursuing anything anyway
   #But gives MC an oppurtunity to reassure her and take the pressure off
   #Also means that the good end requires having gone to the cafe and done all the date stuff
   #I think this is the kikkake to save her from the perfectionist end?

   # ask chat gpt at work
   #What does he see in her that inspires him to draw something that says something about her?
   show alice surprised
   ali "Huh... wow... You made this for me? Even though I'm going to drink this in front of you, and undo all of your effort... Why?"

   #maybe it would be cool if alice is like "drawing, that sounds easy", she's able to do it well mechanically, but the waiter points out that there's not message behind her art
   #that's the differnece between AI and people etc

   na "Well, this is my dad's place. It's not doing too well, so he's making me help out"
   na "Not really how I want to spend my time out of class, but I don't have a choice"
   na "I'm studying to become an artist, and well... This is the only part of my job that I get do something worth while"
   show alice sulk
   ali "I see... I still doesn't explain the whole like, spending so much effort on something I'm going to destroy 2 seconds later."
   na "It's sort of a shame, but like... All art has an expiry date. Whether it's the pigment in oil paintings decaying, pencil fading, or art galleries going up in flames"
   na "Even cave paintings from thousands of years ago are going to be destroyed eventually"
   na "Nothing lasts forever, and well..."
   na "I like trying to make observations about what kind of people order from here, and try to make something just for them "
   na "Art is like... How do I say it... Taking something abstract like, a thought, or a feeling... Sometimes just a funny vibe, or sometimes something really important"
   na "The kind of stuff that inspires revolutions or changes lives"
   na "It's a way of taking that message and trying your hardest to get someone else to feel the same way as you"
   na "When words can't"
   na "So I guess it's like... It doesn't matter if my art lasts a second or thousand years, as long as I can try to share that feeling with someone"
   show alice neutral
   ali "..."
   na "Sorry, I guess I talked a bit too much... Anyways, I hope you enjoy your coffee"
   "He walks back to his station at the front, and picks up his pencil again"
   "Alice looks down into her cup for a few seconds as if thinking deeply about something"
   "And then suddenly picks up the cup and presses it to her lips"
   show alice disgusted
   ali "Bleghhh... What the fuck is this? It's like... creamed dirt water..."
   show alice awe
   ali "Ah!... But wait that aftertaste... This tastes kind of like my mycelium."
   show mc awed
   m "Yeah, well I threw in a some coffee grounds into where you were growing, since I read online it's good for mushroom growth"
   show alice normalside
   ali "I see..."
   "She reluctantly takes a second taste of her coffee."
   "Occasionally looking deeply into the depths of cup."
   "Maybe you should say something to her:"
   menu:
      "Did you enjoy that?":
         jump aboutCoffee
      "Talk about world(N/A).":
         "..."
      "Stay quiet(N/A).":
         "..."
   #Choice: [Did you enjoy that?,  About how much you know about the world, Stay quiet]
label aboutCoffee:
   show mc normal
   m "How's your coffee?"
   ali "Hmm... It's okay... I think maybe I understand why people go out to eat a bit better."
   "You sense that she wants to say something else."
   show mc confused
   m "Yeah, and why's that."
   show alice sulk
   ali "I guess... I just have some stuff to think about... About me... About... You know..."
   "She gulps and seems slightly stressed."
   show alice hime
   ali "But anyway, the taste was nostalgic and I think maybe... I don't hate coffee."
   show mc happy
   m "That's great to hear."
   m "You seemed like you were thinking pretty hard looking into the mug. What were you thinking about?"

   if arcadeWent:
      jump coffeeTalkArcade
   show alice sulk
   ali "Nothing much..."
   show mc normalside
   "You can tell she's not telling the full story."
   "But you don't want to push her too hard."
   show mc normal
   m "Okay, just as long as you enjoyed it"
   ali "Yeah..."
   jump leaveCafe


#fork if you went to arcade first and max trust
label coffeeTalkArcade:
   show alice normalside
   ali "You know..."
   ali "I was just thinking back to that dinosaur game in the arcade."
   show mc confused
   m "Yeah, Bubble Bobble."
   m "What about it?"
   show alice sulk
   ali "Yeah... Just like... In that game right, if you fuck up and get yourself killed, you can come back if you get a 1up, or waste your rent money."
   show mc annoyed
   m "Yeah, but like, I wouldn't recommend that strategy to be honest."
   ali "Sure, but like..."
   ali "We don't get anything like that do we?"
   show alice pout
   ali "In real life"
   show mc surprised
   m "..."
   ali "There's no amount of power or money, no one is important enough to get around the game over screen."
   ali "And even if you beat the game, it's over..."
   show alice pout
   ali "And so I feel like... What do you do when there's no point?"
   ali "With games like that, you can brag to your friends, or... repel every girl in a 5km radius."
   show alice depressed
   ali "But with life it's just like... Why even bother?"
   ali "At first, I just followed my instincts and tried to get you to pay attention to me."
   ali "Not because you were special, or because I liked you, or even knew you."
   ali "But because that's what I felt would make me feel like I am worth something."
   show alice sulk
   ali "I don't know it's... stupid... Sorry, I just..."
   ali "Maybe what you said last night... and what the cow boob artist said..."
   show alice confused
   ali "Maybe there is something more to life than just using others to prove to yourself you're worth something."
   ali "So I wanted to say that..."
   show mc awed
   m "..."
   show alice normalside
   ali "Yesterday I didn't need to shout like that or whatever."
   show mc confused
   m "...wow... I uh... that's nice?"
   show alice normal
   a "..."
   show alice disgusted
   ali "That's... \"nice\"?"
   show mc surprised
   m "No! I mean, sorry that was just sudden so I don't really know what to say."
   show alice sulk
   ali "Agghh, I shouldn't have said anything to you."
   show mc stressed
   "You're so stupid..."
   "Even when you luck into doing something nice, and helping someone, you have to fuck it up at the last second."
   "She's probably already seen through the pretty words you said yesterday as made up bullshit."
   "Be real: YOU said it, so there's no way that you're right."
   "You're SO-"

   ali "..."

   "FUCKING-"
   show alice pout
   ali "..."

   "STUP-"
   #change music to heartfelt
   show alice blush
   ali "Thank you for taking me here."
   $ alice_rp += 10

   show mc surprised
   m "!"
   m "Ummm... Yeah, That's okay..."
   ali "..."
   show alice normal
   ali "You look suprised."
   show mc blushside
   m "Yeah I uh... didn't really expect you to say that."
   show alice sigh
   ali "Me neither."
   show alice normal
   # ali "But I think that I'm starting to change"
   ali "I don't know what it is but."
   show alice confused
   ali "I just feel like when I was born, I had a certain idea of how this life was supposed to go."
   show alice sad
   ali "You were going to be all over me, and I was going to feel good about that."
   ali "Because that was proof that I was good enough."
   show alice smirk
   ali "But you were too much of a little bitch to do anything and made me cry."
   show mc sad
   m "I'm sorry, you know that I didn't mean it like that, I just-"
   show alice happy

   ali "I know, don't worry about it."
   show alice pout
   ali "It's just at the time that was kind of a shock, you know?"
   ali "Like I had just been told that I'm not cut out for my purpose."
   ali "I'm just too ugly, too annoying, too whatever."
   show alice depressed
   ali "And that's not a great feeling."
   ali "And for a while, I didn't really know what to do with myself."
   ali "And being around you..."
   show alice sulk
   ali "Was painful..."
   show alice annoyed
   ali "Do you know what it's like to be around someone you want to like you?"
   ali "How painful it is to know that the reason they don't like you isn't something you did?"
   ali "But just like... the way you are?"
   show alice sigh
   ali "And so I guess that's where I was for a while..."
   show alice sulk
   ali "And now I... I don't know."
   ali "I feel like, maybe I can find something else worth living for."
   ali "Even if it's only for another day."
   show alice blush
   ali "And I wouldn't have that without you."
   show mc surprised
   m "I didn't do anything special."
   show mc awkwardsmile
   m "I just said whatever words popped into my mind."
   m "Anyone could do that."
   ali "Yeah, but {i}you{/i} did."
   #blushies
   show mc awed
   m "..."
   show mc normalside
   #this is him hiding his embaressment
   m "Whatever."
   show alice confused
   ali "So while we are talking like this... I was curious if there was anything you wanted to know about me"
   show mc confused
   m "Like what kind of thing?"
   show alice cruel
   ali "I dunno? Like you know... My 3 sizes, the color of my underwear. You know, normal stuff?"
   show mc stressed at bounce
   m "Who taught you what normal is?!"

   show alice sulk
   ali "I guess I was just born knowing all kinds of stuff."
   ali "Like ways to make people feel good, how to tie people up, that sort of stuff."
   show mc vstressed at bounce
   m "WHY IS IT ALL SEX?!?!"
   show alice confused
   ali "Hmmm... Now that you mention it, a lot of it is related to sex."
   show mc confused
   m "?"

   ali "Like, I have some other information that I was just born knowing"
   ali "Like uhhh.... I know a bit about mushrooms, and like... I guess some of the stuff is more abstract."

   ali "Like when I was born I just KNEW that if I behaved a certain way, that you would like it."
   show alice pout
   ali "But it didn't go the way I assumed it would."
   m "So you mean like... You had like... instincts about specific information? Like genetic memories?"
   show alice neutral
   ali "I don't know what you're talking about but uh, yeah sure, why not?"
   show mc normal
   m "What I mean is, that you like woke up and knew how to speak perfect English, and all of that other stuff."
   show mc normalside
   m "I didn't really think about it too hard after the shock of ummm... You like... Being alive and everything."
   show alice cry
   ali "What, you'd rather I was dead?"
   show mc vvannoyed
   m "No I- Actually no, I'm not gonna take the bait this time."
   show alice smug
   ali "Awww, but it worked before."
   show mc awed
   m "I was just trying to say that there needs to be a reason you know all of this stuff?"
   show alice confused
   ali "Yeah well... Didn't you like, buy me off of the internet from some sketchy darkweb site or something?"
   show mc stressed
   m "IT WASN'T THE DARKWEB-"
   show mc normalside
   m "But yeah, I guess I wouldn't put it past that site to do something like that"
   m "I guess everything you knew makes sense for the purpose of what you were being sold for"
   m "So maybe they like, embedded that information into your DNA to streamline the user experience of ummm "
   show alice neutral
   ali "I'm right here you know"
   show mc awkwardsmile
   m "Sorry, I phrased that sorta weird"
   show alice normal
   ali "I think you might be onto something though..."
   show alice normalside
   ali "It is kind of weird that I know over 200 sex postions, but didn't know what a mall is, huh?"
   show mc shocked
   m "There are that many?!"
   show alice smug
   ali "Way to reveal your power level, 'wand master'"
   show mc sulk
   m "I just think it's really fucked up"
   m "How they programmed you to be the ideal product for them to profit off of"
   show alice confused
   ali "Yeah, I guess... But..."

   ali "Are you guys really all that different?"
   show mc confused
   m "Huh?"
   ali "I mean... Think about it right?"
   show alice normal
   ali "If you look around at every one here, they were all raised by parents, who taught them what was right and wrong"
   ali "And then sent them to a school to learn stuff the government wants them to know for like, a billion years"
   ali "If you're born with one set of bits, you get given toys to simulate child rearing"
   ali "And if you have the other, you're supposed to be like a firefighting astronaut football player or something"
   show mc vannoyed
   m "What were you watching on my computer last night?"
   show alice hime
   ali "ANYWAYS! You know what I mean right... It's easy for you to point at me and say I'm fucked up, but from where I'm sitting"
   show alice serious
   ali "None of you guys seem that different"
   show mc normal
   m "..."
   show alice confused
   ali "I guess I just wanted to know like... How do you know your values are you own?"
   ali "Like are you living for yourself? Or to feel like you're winning in some game you've been conditioned to think is important?"
   #way too on the nose, rewrite to soften
   show mc confused
   m "I... I don't-"
   show alice laugh
   ali "Anyways, lets order some cake! After trying that coffee, I kind of want to see if the other stuff is any good"
   m "Uhh... Yeah..."
   jump leaveCafe


label clothes:
#    The scene where Alice notices the main character’s interest in the pastel pink hoodie is a lovely touch.
# It reveals her growing awareness of his internal struggles and offers a moment of connection between them.
# Her playful teasing and encouragement for him to try on the hoodie show that she’s beginning to understand and care for him on a deeper level.
# This scene subtly hints at the main character’s gender identity issues, adding another layer to his character.

   show alice normalside
   ali "Whatever, what about that place over there?"
   m "You mean the men's attire store?"
   show mc normal
   m "Do you think I look like I have the money for a suit and tie?"
   show alice smug
   ali "Even if you did, it's not like it would /suit/ you anyway"
   show mc annoyed
   m "Hehe-"
   "You almost give in and laugh at her joke"
   "A joke at your expense"
   "You know she's right"
   show alice normal
   ali "So how about you give me something to work with?"
   ali "Makes it easier to at least know what we are going for"
   show mc normalside
   m "I guess I like grey-scale stuff that's not too flashy"
   show alice cruel
   ali "So what we came all this way so that you can keep trying to blend in with the shadows?"
   ali "Come on, you must like at least some /real/ colors"
   show mc blushside
   m "... I kinda... don't hate pastel stuff..."
   show alice laugh
   ali "Heeeh? That's unexpected. Didn't think you were the type for cute stuff like that"
   ali "Want me to pick you out a skirt too? I bet I can find one that will /really/ suit you"
   show mc embarrassed
   m "What?! Why does lik- not hating pastels make me a creep like that?!"
   ali "You don't need to play stupid, I saw your wallpaper on your big screen thing"
   #Show like a cute kirby-ish wallpaper on the pc during the discord scene
   m "!"
   m "..."
   "She's got you there"
   ali "Besides, how is it creepy? I'm serious, I think you'd look really cute~"
   show mc vstressed
   m "Stop fucking with me..."
   show alice serious
   ali "I'm not"
   m "There's no way you actually mean that..."
   show mc worried
   m "Besides, I already can't deal with people..."
   m "How am I supposed to handle them if they stare at me"
   m "I just want to fade into the background"
   "In your room... Forever"
   # a room that isnt his and is temporary
   show alice neutral
   ali "Really?"
   m "..."
   show alice annoyed
   ali "I'm going to die soon... I don't have much time left..."
   ali "And you have some more... But even then"
   show alice
   ali "Your time is limited."
   show alice sad
   ali "Don't you feel like it's a waste? Of youth? Of life?"
   ali "I think you're just scared."
   ali "Me too..."
   ali "But can you honestly tell me that you /want/ things to carry on like they are?"
   show mc awed
   m "..."
   show alice laugh cruel
   ali "So..."
   ali"..."
   ali"Let's get you some cute clothes!"
   show mc vvannoyed
   m "That's where you were going with this?!?!?"
   ali "So that's a no then?"

menu:
   "We can take a look I guess":
      jump mallPastel
   "Not in a million years, no way (N/A)":
      "Skye must still write this part..."

label mallPastel:
   $ alice_rp+=10
   show black with dissolve
   "..."

   #cut to the mall later, with mc wearing a slightly oversized pastel pink hoodie
   # :3 insignia?
   show mc pink embarrassed
   show alice smug

   hide black with dissolve
   m "..."
   show mc pink embarrassed desperate
   #make sure it's not obvious that they are trans, make it like they are a guy who's ashamed of having a feminine side
   #because of it bringing more attention to him and that going against the status quo
   #she acutally thinks it suits him, and is trying to help him give less of a fuck
   # but is also teasing him by picking on the obvious discomfort he feels about this

   m "EVERYONE'S LOOKING AT ME!"
   ali "So? Let them."
   m "Easy for you to say..."
   ali "What was that?"
   m "Easy for you to say when you look good in anything!!!"
   show alice flirt
   ali "You really think so?"
   m "That's not my point! I just mean like..."
   m "I'm not like you. It's better for everyone else that I just stay out of sight."
   show alice annoyed
   ali "Stop saying stupid shit. If I hear one more thing from you I'll take that as a personal insult."
   m "Huh? Why what does what I say about myself have to do with you?"
   show alice vannoyed
   ali "I picked out those clothes, and my taste is absolute."
   show alice angry
   ali "So shut the fuck up and enjoy the attention."
   m "..."
   m "I-"
   ali "What did I just say?!"
   m "Sorry..."
   show alice laugh
   ali "You really {i}are{/i} cute."
   show mc pink embarrassed
   show black with dissolve:
      alpha 0.5
   "You don't really know how to feel..."
   "You can't help but feel scared."
   "Scared of judgement."
   "Memories of the kids you went to elementary school with flash into your mind's eye."
   "Of little comments your parents made."
   "When you stepped out of line."
   "Not for being rude, or malicious."
   "But for being curious."
   "..."
   "You like cute anime."
   "You like playing games where you talk to little animal people, and go fishing."
   "You know you like this hoodie."
   "But is it {i}really{/i} okay?"
   "For someone like {i}you{/i} to wear this?"
   "Up until now, it's always been participating in this stuff as an observer..."
   "Out of sight."
   hide black with dissolve
   show alice disappointed
   ali "It's just a shame you wouldn't try on the good stuff."
   show alice laugh
   ali "I picked out the cutest thigh-highs and everything for you."
   ali "The little cat paw prints on the sole were adorable."
   m "I bought this - can't you just leave it?!"

   show alice happy
   ali "Jokes aside, I think that it really suits you and I can tell you like it too."
   m "..."
   show alice normalside
   ali "It's just a shame you want to hide away under all that fabric."
   ali "Wouldn't hurt you to show us some skin."
   show mc embarrassed tears
   show alice hime
   ali "But I guess fruiting bodies don't sprout in a day, and that suits you pretty good as is."
   m "Who is supposed to know about fruiting bodies?! You're lucky I'm a biology major..."
   show alice normal
   ali "Anyway, pick the next place for us, will you?"
   show mc confused
   m "Like where?"
   show alice confused
   ali "Hmmm... I don't know..."
   show mc normal
   m "Do you have any hobbies or whatever?"
   show alice cruel
   ali "Oh yeah, I {i}love{/i} to crochet on the weekends after finishing at the office~"
   show alice mendokusai
   ali "I'm a mushroom that was born literally a day ago, why the fuck would I have hobbies?"
   show mc stressed
   m "...Sorry..."
   show alice normal
   ali "Whatever... So, where are we going?"

   jump cafeDate

label leaveCafe:
   stop music fadeout 3
   scene mall with fade
   play music "mall.mp3"
   "After you paid the bill, you walked through the mall towards the exit"

   scene enbankment with fade
   show mc awed at right
   show alice happy at left
   with easeinbottom
   m "It's not too often I get to walk outside in the sunset."
   show alice normalside
   ali "Yeah sure... \"in the sunset\""
   m "Yeah... Maybe I should do it more."
   show alice happy
   ali "Maybe you should! It's really pretty!"
   show mc confused
   m "Why do you seem like you're having more fun on the embankment going back home, than when we were actually at the mall"
   ali "The mall was fun... But this is nice too"
   jump day2WayHome

   show alice surprised
   ali "!"
   m "What?"
   show alice awe
   ali "Look! Over there!"
   m "Huh?"
   ali "It's a butterfly!"
   hide alice with easeoutright

   show mc surprised

   m "Huh? Wait!"

   scene black with fade
   stop music fadeout 3
   m "Don't just run off like that! You had me worried for a sec, when I lost sight of-"
   ali "..."


#Introduce the butterfly here, but it just takes her to the live house
label day2WayHome:
   #Here is the original idea for the scene/ Feel like I didn't add everything I wanted to
   #--------->
   #choice whether to get her to open up adds a point to trust
   #if trust is high enough
   #she explains about her toxicity, and the danger she poses to those around her (people) in high doses
   #at first she didn't have the tools to think about it, but she's starting to feel insecure about being perceived as dangerous

   #here its important to talk about her lifespan as a mushroom too, whether or not she's edible etc.
    #she discusses her view on death: i don't care about dying, as long as while i live i have some kind of meaning. I want to be loved.

    #[maybe she has some kind of internal conflict where she's afraid of getting close to people because she's literally poisonous]
    #but is it fine as long as she doesn't care about them? so she's scared of trusting someone, because her poison will hurt them
    #and push them away, so its easier she doesn't even try
    #or that she only uses them for sex, validation, then throws them away
##########################


"You walk with Alice through along the embankment until you reach the outskirts of the city center"
"Its hustle and bustle has died down partly due to distance from the crowds, and partly due to the day turning to evening"
"However..."
play music "date.wav"
show alice surprised
with easeinbottom
ali "Hey do you hear something?"
show mc normalside
m "Hmm?"
m "..."
show mc normal
m "Yeah, I guess now that you mention it."
hide alice with easeoutright
show mc surprised
m "Huh? Hold on slow down!!"

# Music Decision:
# Alice’s decision to embrace heavy music as her form of expression is a bold and fitting choice.
# It aligns with her desire to confront her mortality and make the most of her limited time.
# Her determination to write a song and perform in the open mic competition adds urgency and direction to the story.
# It gives her a concrete goal to work towards, which could drive the narrative forward.

#transition to alley way
scene alley with fade
show alice normal at left
show mc pant at right
with easeinbottom
ali "The sound is coming from down here"
m "*Huff* *huff*... Please... Don't... Run..."
ali "What is this place"
m "This- *cough*"
show alice disappointed
ali "Damn, you need to work on cardio"
m "This place looks like a live music venue"
m "If you go down those stairs, there's people listening to a band or something probably"
ali "Hmmm..."
m "See, there's a poster for an event on here"
#MAKE THE NAME OF THE EVENT SOMETHING FUNNY#
#todo: needs to be a competition
show alice normal
ali "Bandemonium?"
show mc normal
m "Yeah, it's probably like a rock music competition thing from the vibes of the poster, and the little I can hear"
ali "Rock music?"
m "Yeah it's like... I don't really get it, but I think it's a kind of music where people sing about like..."
m "Being really angry at your ex-girlfriend..."
show mc normalside
m "Or like... Killing people? Or like... yourself?"
m "I don't know... I feel like I have lots of conflicting ideas about it"
m "But either way, it's generally more intense music that deals with heavier topics"
#Maybe she should be more like WTF?
ali "That sounds kinda interesting"
ali "I feel like humans usually avoid interacting with the more ugly parts of being alive"
ali "But it sounds like some people go out of their way to think about it"
m "Yeah. Some people like to escape from their problems, and others like to think about them all day"
m "I guess humans are weird"
ali "I'm guessing you listen to the more of the 'escapism' category"
m "..."
m "I've heard a little bit of this sort of music"
m "Through my bedroom wall"
ali "So your neighbour is into this sort of stuff"
m "Yeah, I think he plays guitar too from the sound of it. He's pretty good"
# ali "So how long have you guys been dating?"
ali "So that means you have connections with an insider?"
m "What? I don't even know what he looks like. So talking to him is out of the question"
ali "You've been living there for ages, and you don't even know what you neighbour looks like?"
m "Nope"
ali "..."
m "..."
show alice sly smile
ali "..."
show mc normalsquint
m "Oh no, what are you thinking"
ali "Hey, I was just thinking about how much I wanna learn guitar"
ali "And well"
ali "You're my only option"
show mc stressed
m "No way"
show alice cry
ali "*sob* How could you say that!"
ali "To a cute innocent girl with only so many more hours left on the clock"
m "..."

#Choice: Give in to her, No means no
menu:
   "No means no.(N/A)":
      "..."
   "Give in.":
      #Give in to her
      ali "*sob* Ignore the last wishes of a petite, dying, defenseless-"
      m "Fuck you... Fine!"
      m "I'll go ask"
      # He needs to be like "but you only have one day, how tf are you gunna do the thing" alsom lampshade that she has like higher power shroom creative intuition
      show alice excited
      ali "Really!?"
      m "Wait, you're actually excited?"
      m "I thought this was just a way to make me suffer"
      show alice pout
      ali "Why are you so mean to me"
      ali "Such an abuser"
      m "You only have today and tommorrow left. How do you play to learn a whole instrument?"
      ali "I'll make it work out."
      m "HOW'RE YOU SO COCKY?!"
      ali "Tehe!"
      m "..."
      m "Why do you have an interest in this all of a sudden though?"
      show mc confused
      m "Like I've spent the whole day showing you a bunch of stuff, and you didn't seem very excited about anything else"
      show alice normal
      ali "I've been thinking about it the whole day"
      ali "At first I kinda of didn't understand why people care about stuff"
      ali "like drawings, or food or video games"
      ali "But thanks to everything you showed me, I think I started to get a better idea of why"
      ali "And then I was kind of hoping something would just leap out to me"
      ali "But I don't think life works like that"
      ali "I think instead of waiting for a lightning bolt to strike down and give some kinda of divine intervention"
      ali "You gotta just like"
      ali "Do whatever seems fun"
      ali "And I kinda can't keep waiting."
      ali "I don't have that sort of time"
      ali "..."
      ali "So I'm gunna go with this!"
      m "..."
      show mc slightsad
      #he's not sad here because of talking to neighbour, but because he's jealous about her attitude
      m "I'll see what I can do."
      stop music fadeout 2
      jump Day2Neighbour


#choice whether to get the courage to talk to neighbour
#how does alice respond if you don't do it
label Day2Neighbour:
   scene black with fade
   "You get back to your place, and lead Alice inside."
   "You place your things on your table and then go out the door you just came from."
   scene hallway with fade
   show mc normal with easeinbottom
   m "Okay... It's not that scary... It's just talking to a person."
   show mc worried
   m "A person that you have never seen before."
   m "Who could be a serial killer, or... a mormon or something"
   m "But probably not!"
   show mc stressed
   m "... Hopefully"
   m "Just gotta knock at that door..."
   m "Just a little rap-a-tap-tap..."
   show mc vstressed at bounce
   m "FUCK!!!"
   show mc sad
   m "Why is this so hard?!!"
   show mc stressed
   m "You know fuck it, I don't think I can-"
   play sound "door.wav"
   show kellin normal at left with easeinbottom
   na "Uhh, are you okay?"
   play music "normal.mp3"
   show mc shocked at bounce
   pause 1
   show mc shocked at right with move
   m "AAH! ummm, Yeah, I was just!... Uh, you know... Ummm..."
   na "Did you need something? I heard mumbling and feet shuffling outside so?"
   # make text very small
   show mc worried
   m "Uhh yeah, so I was kinda of ummm, sent here to ask a favor, but like I don't even know you, or like said my name and I"
   na "Slow down, just take it easy"
   show kellin happy
   kel "First off, hi, I'm Kellin. I don't think I've met you before? Do you stay in the dorms?"
   m "Uhhh... Yeah, next door actually..."
   show kellin shocked
   kel "Woah! So your the one that's been here the whole time! I tried to leave a package for you the other day but!"
   show mc stressed
   m "Yeah I'm not too great at talking to people... Or waking up"
   m "Sorry about that"
   show kellin happy
   kel "No, it's okay, you're probably a really good listener!"
   kel "Damn we've been next-door room buddies for like... How long now?"
   m "Uhhh... Like 2 years"
   kel "Woah that long already? Good times..."
   kel "By the way, I still don't know your name"
   m "Oh it's player name"
   kel "Nice to meet you!"
   show kellin normal
   kel "So what do you need?"
   m "Uh, I've just heard you playing guitar and listening to music and stuff through the walls and ummm "
   show kellin shocked
   kel "OH! I'm so sorry, I must have been blasting it too loud! I'll try be careful from now on!"
   m "No, uh-"
   show kellin awkward
   kel "It's okay you don't have to be polite!"
   kel "I'm so sorry, I should have been using headphones to being with"

   show mc normalside
   m "No, you're fine, that's not it"
   show kellin normal
   m "I was just wondering if uhhh... Damn I guess I don't know you well enough to ask anything"
   show kellin happy
   kel "You don't have to say anything... I know why you're here!"

   #Alternative progression: You nervously being trying to ask
   #he ends up getting over the toply worried expecting that you are going to tell him about someone being murdered on the floor or something
   #his assumption about the situation is that something bad MUST have happened, because he's picking up how stressed you are
   show kellin vhappy
   kel "I see right through you... To your soul!"
   show mc shocked
   m "!?"
   kel "I accept your proposal"
   show mc surprised
   m "Huh?"
   show kellin happy
   kel "So if I'm doing guitar... Maybe backing vocals, then what are you going to be doing?"
   kel "Don't tell me! You have the vibes of a bassist!"
   kel "But if you were, then I would have heard you through the wall"
   kel "So you must be a drummer! You must go to like a practice studio right!"
   kel "It's so inconvinient to be a drummer living in a communal space right!"
   kel "So when is our first practice session? Do you have any songs done yet?"
   show mc worried
   m "I don't uh... Know how to play drums"
   show kellin vhappy
   kel "You're so humble! That's such a good quality in a band member!"
   show mc stressed
   m "No like, literally I've never picked up a drum stick"
   show kellin normal
   kel "Oh so then what do you play?"
   show kellin happy
   kel "Wait don't tell me... Kalimb-"
   show mc normalsquint
   m "I can't play anything"
   show kellin vhappy
   kel "WOAH, fresh blood! That's so exciting!"
   show mc sad
   m "Yeah, I guess you could say that."
   
   m "(Damn, he's so nice, but I'm already so exausted from this conversation.)"
   show mc stressed
   
   m "I know we've never talked before"
   show kellin normal
   m "And this is a big ask..."
   show mc worried
   m "but I was wondering if..."
   m "I could ummm..."
   show kellin happy
   kel "Sure, I'll get it ready"
   show mc shocked
   m "I haven't even asked yet!"
   show kellin vhappy
   kel "What are you talking about? I told you! I get you!"
   kel "You don't need to say anything to me! Our brains are connected on the same wavelength!"
   show mc worried
   m "Uhh... yeah... sure..."
   show kellin happy
   kel "Come inside!"
   m "...Okay..."

   scene neighbour_bedroom with fade:
      zoom 0.9
   play sound "door.wav"
   show mc awed at right
   show kellin normal at left
   with easeinbottom
   m "Woah this place is really... something"
   kel "I guess? Isn't it normal?"

   m "Uh, if this is normal, then I think your reference point is kinda busted"
   kel "So this is what you wanted right?"
   kel "I have a couple guitars, but this is the only one that's not in a weird tuning right now"
   show mc confused
   m "Tuning? uhh"
   show kellin happy
   kel "Most guitars are tuned in fourths starting from E, with the exception of the major third between the G and B strings"
   show kellin vhappy
   kel "But recently I've been really into this emo tuning that's tuned to like an A major chord with a D in the bass"
   kel "I also have an 8 string over here that's tuned-"
   m "So guitars have strings... I think? and ummm emo?"
   #maybe do the emo copypasta?
   show kellin happy
   kel "I haven't changed the strings on this one for a while so if this is okay then"
   show mc worried
   m "Are you sure it's okay?"
   m "ummmm..."
   m "K-Kel?"
   show kellin vhappy
   kel "Yeah, I don't really use it either way..."
   show kellin normal
   kel "Oh you probably want this too"
   kel "And this and..."
   stop music fadeout 2
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
   show day_2 at topleft
   show alice_affection at topright
   with dissolve

   play music "night.mp3"
   show alice normal at left
   with dissolve
   play sound "door.wav"
   show mc stressed at right with easeinbottom
   #mc with guitar in soft bag on back and arms fulled with stuff
   show alice surprised
   ali "Woah, you got it! Thanks but..."
   ali "I thought you were just getting a guitar, what's all that"
   m "A tuner, an overdrive, compressor and delay pedal, a practice amp-"
   ali "That's-"
   m "-headphones, a box of picks, 2 instructional dvds-"
   show alice neutral
   ali "Uh-"
   m "-3 live dvds, 8 cds..."
   m "And one vinyl"
   ali "Geez"
   show mc normal
   m "I managed to turn down the record player"
   ali "Then why did you take the vinyl?"
   "I guess we're lucky you have such a supportive neighbour"
   show mc annoyed
   m "I can't help the feeling that maybe I'm doing him a favor by giving him someone new to rant at."
   jump day2GuitarSetup

label day2GuitarSetup:
#    Guitar Practice:
# The guitar scene reinforces the theme of resilience. Despite the broken string, Alice’s quick progress on the instrument reflects her innate abilities and determination.
# The main character’s willingness to ask his neighbor for the guitar, despite his social anxiety, shows his growing commitment to helping Alice.
# This small victory for him could be a significant moment in his own journey.

   show alice excited
   ali "So can we set it up? Please!?"
   show alice hime
   ali "...I mean, if you're free right now that is."
   show mc normal
   m "Uh yeah, lemme just try to figure out how to get it in tune."
   show alice happy
   ali "That's fine, I can do it."
   show mc confused
   m "Are you sure?"
   show alice laugh
   ali "Just pass it here!"
   # string tuning sound
   "*{size=+20}Snap!*"
   # string snaps
   show alice shocked
   show mc sad
   ali "Eek!"
   show mc stressed
   m "I mean, he did say that it needs a new set of strings..."
   show alice sad
   ali "Uwa, what do we do, should we call the police?"
   ali "They'll know what to do right?"
   show mc normal
   m "We can just buy a new wire tomorrow."
   m "For now, you'll just have to make do with those."
   show alice pout
   ali "...I guess..."
   hide alice with dissolve
   play sound "guitar_flick.wav"
   "Alice sits on your chair, guitar in hand, and you watch for a few seconds as she clusily plucks the remaing five strings."
   "What's the point? What is possibly hoping to achieve in just a day?"
   scene black with fade
   "You don't say it, but..."
   "You wouldn't be surprised if she's given up by the time you wake up."
   window hide
   window hide
   stop music fadeout(3)
   show chibi_sleep at truecenter with dissolve
   show top_text "Emotionally and physically exhausted, you let those simple guitar notes carry you to sleep."
   with dissolve 
   pause 3

   jump day3Morning

# todo: add new ending to the day

# Potential Additions:
# Internal Struggles:
# The main character’s internal dialogue could delve into his mixed feelings about encouraging Alice to find meaning, knowing her time is limited.
# This could add a layer of bittersweet tension to their interactions.
# Alice’s thoughts while practicing the guitar could reveal her growing sense of purpose, mixed with the knowledge that she’s running out of time.

# Foreshadowing and Symbolism:
# The butterfly’s death could foreshadow the challenges Alice will face in the competition and her own mortality.
# It could also symbolize the fragile nature of the connections she’s forming with the main character.
# The pastel pink hoodie could become a recurring symbol of the main character’s suppressed identity, perhaps reappearing in later scenes as he becomes more comfortable with himself.




#choice -> call back?
#if call back trust++ - Why?



#defuse by doing something together, show her music on YouTube?  maybe you show her a little bit before, and then something after?
#You make a promise that tomorrow you would go to a music store and buy a new set of strings

#contrast of how the 2 of them argue

#Alice: short and cold and precise when she's argueing, but when she's really hurt, will also do insults she doesn't mean. More petty. Tends to run away, when like this.
#MC:bottles up, tries not to express, but if he panics, he word vomits, with internal stuff leaking out. Sometimes he deflects and blames others. Focuses on what-ifs, over thinker.

#FOCUS:You can't live for conditional love: pretending to be something you're not, when you only live one.
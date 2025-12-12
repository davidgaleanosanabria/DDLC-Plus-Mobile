define wipe_intro = ImageDissolve("images/side_stories/menu/wiperight.png", 8, ramplen=96)
transform sm_intro_fade:
    truecenter
    alpha 0
    linear 3.0 alpha 1

label sm1:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    $ pause(1)
    play music intro
    $ pause(0.5)
    show bg residential_day with Dissolve(3)
    $ pause(3)
    show bg corridor with Dissolve(3)
    $ pause(3)
    show bg pstairwell with Dissolve(3)
    $ pause(3)
    show bg pclub_morning as pclub1 zorder 1 at sm_intro_fade with Dissolve(0.05)
    show bg pclub_sm_intro as pclub2 zorder 2 at truecenter with wipe_intro
    $ unlock("bg_class3")
    show bg pclub_sm_intro
    hide pclub1
    hide pclub2

    S m 4b f11
    m "Okay, everyone!"
    m "The Literature Club is starting."
    m "Let's all have a seat and take attendance, okay?"
    m "..."
    m 1r "Ugh..."
    m "I miss Debate Club..."
    m "Who knew it would be so difficult to start a new club?"
    m 1p "I feel worse with every day that passes without anyone coming in..."
    m "I'm really starting to lose confidence."
    H m
    "Monika is the only member of the Literature Club."
    "In the days that have passed, all of her efforts to recruit new members have been fruitless."
    S m 1g f11
    m "Am I going about this wrong?"
    "Monika glances at one of her fliers."
    "The headline is: \"Do you like literature?\""
    m "Maybe nobody is into literature enough to pick it over their other club interests..."
    m 1r "I can't just rely on people liking literature."
    m "I need to sell them on a vision! A vision."
    m 1g "But what kind of vision...?"
    H m
    "Monika rests her head on her desk, deep in thought."
    "But before she realizes it, the recent nights of staying up too late start to catch up to her."
    "It's so quiet, and the noise of the air conditioner is soothing..."
    stop music fadeout 6.0
    scene black
    with Dissolve(4)
    $ pause(2)
    $ s_name = "???"
    s "Um..."
    s "Hello...?"
    show bg club_day
    S s 1b t11
    show black zorder 2:
        alpha 1
        linear 1.5 alpha 0.85
        1
        linear 0.25 alpha 0
    $ pause (3)
    hide black
    $ unlock("bgm_peachypie")
    play music p2
    $ s_name = "Sayori"
    "Suddenly, a voice causes Monika to snap awake."
    S s 1b t21
    S m 1l f22
    m "Oh...oh my gosh! I'm so sorry! I never do this!"
    s 1q "Hehe. Is this the Napping Club?"
    m 1n "No, this is..."
    "Monika pauses, suddenly embarrassed to admit that this is, in fact, the Literature Club."
    m "This is the Literature Club..."
    s 4x "Yay! I thought I got it wrong for a sec..."
    m 2e "I'm super sorry...it was like, so unprofessional of me to do that."
    s 1x "Don't apologize! I do that all the time!"
    m 2m "Oh..."
    s 1b "Um...did I miss the club meeting? Where is everybody?"
    m 4n "Well, about that..."
    m "...This is everybody."
    s 1c "Really? Just you?"
    m 1d "But...we're getting more members! I'm working really hard on it!"
    s 1i "Hold on a sec."
    s "If it's just you..."
    m "..."
    s 4r "That means I get to be Vice President!!"
    m 1d "Wait...Vice President?"
    m 2m "Um...what are your qualifications?"
    s 1a "Well, I'm better at napping than you."
    s 1x "...Maybe I should be President!"
    m 1f "Now you're just making fun of me!"
    s 2g "Oh...I'm sorry..."
    m 1d "Um...what was your name?"
    s 1a "Sayori."
    m 2r "Okay. Sayori..."
    m 2d "I've been trying really, really hard on this club."
    m "I know you caught me at a weird time, but..."
    m 2p "It's really disheartening to not be taken seriously, you know?"
    m "I care so much about this."
    m "I just want to find other people who do too."
    s 1h "Oh no..."
    s "I'm so sorry..."
    s "I do care. I promise."
    s 1l "I have a hard time being serious, that's all..."
    s 1k "I didn't mean for it to hurt you."
    s 1l "And I was joking about the Vice President thing too. I would make a terrible Vice President..."
    m 2e "I mean, I'm sure that..."
    "Monika tries to say something reassuring, but it's difficult when she still doesn't know much about Sayori."
    m 2f "...I'm sorry that this isn't like, a real club yet."
    m "Would you still be interested in joining after I found a few more members, at least?"
    s 1b "Well, no..."
    s 2a "I want to join now!"
    m 1d "Really??"
    s 4x "Yeah! It sounds like a lot of fun!"
    s "Besides, I can tell how hard you've been working."
    s 1a "You're doing something amazing and you should be proud of it, you know?"
    s "So let me help you turn something stressful into something fun."
    s 1d "If nothing else, I'm good at that, so..."
    m 2j "Ahaha."
    m 2a "Honestly, how could I possibly say no to that?"
    m "That's really sweet of you, Sayori."
    m "Oh...I'm Monika, by the way."
    s 1q "Monika!"
    s "That's such a cool name!"
    m 2n "Oh, now you're just trying to cheer me up..."
    s 1x "But you're smiling!"
    m 2a "Well, I didn't say it didn't work."
    "Monika glances at the flier on her desk and realizes that her name is already written on it."
    s 1a "So what do we do first?"
    m 1a "Well..."
    m "It's getting pretty late, isn't it?"
    m "We can go home and try to come up with some new ideas to recruit club members."
    s 2q "I can do that!"
    m 2a "Cool!"
    m "And I think I need to put some more thought into my vision for the club."
    m 1r "You know, like...a mission."
    s 1q "My mission is to make everyone happy."
    m 1j "Ahaha."
    m 1a "Yeah, something like that. I need to think about it."
    s 2a "Hey, do you like hugs?"
    m 1d "...I guess so?"
    H s
    H m
    "Sayori suddenly pulls Monika into a friendly hug, then lets go."
    S s 1a f21
    s 1a "Some people can just really use a hug sometimes."
    s "Besides..."
    "Sayori whispers loudly."
    s 4r "Hug energy is what keeps me at my best!"
    S m 1a f22
    m 2k "Ahaha, hug energy?"
    "Monika laughs."
    "Although Sayori is very different from her, Monika feels her spirits lifted."
    "Maybe it's just because she finally found another club member."
    "But..."
    m 2a "Well, I'm looking forward to tomorrow, then."
    m "It'll be fun."
    s 1x "Yeah! I'm excited!"
    s "I'm gonna think really hard tonight about how to get more people."
    m "Yeah, me too."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    jump sm2

label sm2:
    scene bg corridor
    with dissolve_scene_full
    play music p2

    "A day passes, and the time comes for the Literature Club - Monika and Sayori - to reconvene."
    "As President, Monika ensures that she's the first to arrive to the clubroom."
    "But she finds herself waiting longer than expected for Sayori."
    scene bg club_day with wipeleft
    S m 2f f11
    m "It's been 10 minutes already..."
    m "Maybe Sayori changed her mind about joining?"
    m 2r "No... That can't be. She was so excited yesterday."
    m 2f "But I'm getting kind of worried..."
    "Suddenly, Sayori comes bounding through the door."
    "In her hand, she's holding a sheet of paper."
    S s 4m f21
    S m 2d t22
    s "Sorry I'm late! I'm here!"
    m 1a "It's okay. Welcome back."
    s 4x "Aaaaand..."
    "Sayori spins over to Monika and deposits the sheet onto Monika's desk."
    m 1d "Oh, what's this?"
    $ unlock("take_my_hand")
    call showpoem (poem_ps1, music=False)
    m 2b "Hey, this is really good!"
    m "You wrote this, Sayori?"
    s 1q "Of course!"
    s 1b "Wait..."
    s 4m "Wait, no! That's the wrong side of the paper!"
    m 1d "Huh?"
    s 4p "I wasn't ready to share that yet, I'm so embarrassed..."
    "Monika flips over the paper. Written on the other side is a list of ideas for recruiting new club members."
    m 2a "Ohh! So this is what you meant to show me."
    m "But I'm curious now...do you write poetry often?"
    s 1b "I do! But..."
    s 1l "I'm sure I'm not anywhere near as good at it as you are."
    m 2j "Ahaha. Really?"
    m 1l "I'm actually terrible at writing poetry..."
    m "I've never written anything I was happy with."
    m 1n "Like, I always read it again a week after I write it, and I'm like..."
    m "'Wow, this is so stupid.'"
    m 1m "I dunno..."
    m "It's like the dramatic version of me doesn't agree with the person I want myself to be...or something like that."
    s 2d "Aww..."
    s "You should have more confidence in yourself!"
    s 2a "You're the Literature Club President!"
    m 2j "Ahaha...I guess you're not wrong there."
    m 2a "I need to like, set a good example or whatever."
    m 2a "Hmm...you know, I can envision the club doing something like that..."
    s 1b "Doing what?"
    m "You know...like sharing poems we write, and stuff like that."
    s 4x "Oh! Yeah!"
    s "I would love that!"
    s 1a "It's such a good way to learn about other people, you know?"
    s "It's like, we have so many emotions that we can't express to other people, usually..."
    s "But you can when it's in a poem, right?"
    m 1b "Yeah!"
    m "I think that's helping me form a more cohesive vision for the club."
    m 1a "So I'm glad you showed me...well, even though it was by accident."
    s 1q "Me too!"
    s 1a "I felt embarrassed at first, but now it feels kind of good that someone else read it."
    s 1x "I'll try to show you more of them in the future!"
    m 1b "I'd love that."
    m 1e "Oh jeez, I'm getting distracted..."
    m 1a "Do you want to go over this recruitment brainstorm together?"
    s 2q "My brain stormed so hard!"
    s 2n "It was like a brain hurricane."
    s 1o "My brain is a natural disaster."
    m 2k "Ahahahaha!"
    m "Sayori, that's terrible."
    S s 1a t21
    m 2a "Anyway, let's take a look at the list..."
    m "..."
    m 1m "...'Make cupcakes'."
    s 1l "I was hungry..."
    s 2c "But it's a good idea!"
    s "Isn't it?"
    m 2q "Um..."
    m "Let me think about this..."
    m 2d "I mean... When would we have the chance to give people cupcakes?"
    s 1x "You know, like when they come into the club!"
    s "What if we said we had free cupcakes on the fliers?"
    m 1g "I'm, like...kinda worried that would bring in the wrong kinds of people, you know?"
    s 1b "Wrong kinds?"
    m 1m "People would come just for the cupcakes and then leave..."
    s 1h "Aw, nobody would do that!"
    s "That would be mean!"
    m 1d "But you know, I want to find people who are really into literature!"
    m "Even if they don't know it yet."
    m 1a "Let's see, the next thing on the list..."
    m "'Hunt for people reading books'."
    m 1d "I don't think I get it..."
    s 1a "Like, going around the school and finding people who are reading books, you know?"
    s "Like in the morning, or during lunch..."
    s 4x "And we'd tell them to check out the Literature Club!"
    m 2d "Well, the problem with that is like..."
    m "Wouldn't most people reading books just be doing it for an assignment or something?"
    m "How would we know if they're just reading for fun?"
    s 1l "Um...well, we could ask them..."
    s "But then we'd be bothering people who are trying to do schoolwork..."
    s "I didn't think about that part, I'm sorry..."
    m 2a "Hey, don't apologize."
    m "You're coming up with a lot more things than I can."
    m 2d "Oh, your next idea is to hand out fliers, rather than just put them up on the wall."
    m 2a "I'd definitely like to start doing that."
    s 4q "I'm useful!"
    m 2k "Ahaha. I never said you weren't."
    m 1d "I just need to think...what would we tell people when handing them out?"
    m 2d "I don't want to just be like...'Join the Literature Club!'"
    m 2a "Let's figure out how we can better engage people."
    s 1c "What if you told them about the club activities and stuff?"
    m 1d "What club activities?"
    m 1e "Yeah, I guess it's supposed to be my job to come up with that, right?"
    m "A vision for the club."
    m 1r "Okay, Sayori, pretend you're a normal person for a second..."
    m 1l "Wait! I didn't mean it like that!"
    s 1r "Ahaha!"
    m 2a "You know, like a random passerby who's getting a flier."
    m "How would you react to the idea of a Literature Club?"
    s 2i "Hmm..."
    s "Probably like..."
    s 5d "Literature is stuuupid."
    s "I'm joining the Anime Club."
    m 1n "What the heck...?"
    s 4r "Ahaha! Sorry, I was just thinking of a friend of mine."
    m 1e "Okay, what if I said that we, like...do group reading and discuss it together?"
    s 1l "I would probably nap through that..."
    m 1d "That's you, Sayori."
    s 2h "Yeah, but that doesn't really sound fun to most people anyway!"
    s "We need to really catch their interest, you know?"
    m 1g "Ugh..."
    m "This sucks. Why is this so hard?"
    s 1g "Monika..."
    s "Don't be sad..."
    m 1d "What do you like about literature, Sayori?"
    s 1b "Me?"
    s 1a "Well, kind of what I said about the poem earlier..."
    s 2a "I think it gives you the chance to express yourself."
    s "Like, express yourself in ways you can't normally do, when you're just doing your normal day and talking to your friends."
    s 2d "I mean, we all have so many thoughts and feelings that we just...don't get to share, you know?"
    s "It's, like..."
    s 1d "...Intimate."
    m 2e "Yeah..."
    m "How do we get that across to people?"
    m 4b "We could be like...'Express your true self!'"
    s 4r "'Be intimate with us!'"
    m 4n "Okay, that's kind of..."
    s 1q "Ehehe, I'm just kidding."
    s 4m "...Oh my gosh!"
    m 1d "What? What is it?"
    s "I forgot all of my things in my classroom!"
    s 4l "I must have gotten too excited and rushed here, silly me..."
    m 2d "Rushed? But weren't--"
    m 2e "Ah, never mind... Did you want to get your stuff, then?"
    s 1h "I'll forget if I don't do it now!"
    m 2j "Ahaha. Well, I'll wait for you, then."
    s 1x "Okay, it'll only take a second!"
    H s
    H m
    "Sayori dashes out of the room, leaving Monika momentarily alone."
    "Monika sighs and starts jotting her thoughts on a sheet of paper."
    S m 1i f11
    m "Express yourself..."
    m "Be who you want to be..."
    m "Make new friends..."
    m "..."
    m "Discover...a new you."
    m "Discover your heart."
    m 1r "No..."
    m 1h "Write your heart out."
    m 1q "No..."
    m 1i "Write into your heart."
    m "Write the way into your heart."
    m 2r "...Join the Literature Club. ...Write the way into your heart."
    m "..."
    m 2m "Wow, that's lame..."
    S m 2m t22
    S s 1a f21
    s 4m "Monika!!"
    m 1d "Ah!"
    m "You startled me!"
    s "Sorry!"
    s "But it's something important!"
    s "On the way to my classroom...there was a girl reading a book!"
    m 2d "Reading a book?"
    s 4c "Let's hurry and recruit her!"
    m 2i "Wait...are you sure she's not just doing homework?"
    s "I could tell she was really into it!"
    m 2m "Um..."
    m "Well, I guess we could...take a look..."
    H s
    H m
    "Monika grabs one of her fliers and stands up from her desk."
    "Then the two depart the classroom, with Sayori leading the way."

    scene bg corridor
    with wipeleft_scene

    S s 4r f21
    s "This way!"
    S m 2e f22
    m "You don't have to run..."
    "Sayori leads Monika over to a particular classroom, then lowers her voice to a whisper."
    s 3o "See, in here!"
    "Monika peers through the window."
    "Sure enough, there's a girl sitting alone, intently reading a book."
    m 1m "I feel like a creep doing this..."
    s 1x "You should go inside and talk to her!"
    m 1g "Me?"
    s 1h "You're the President! And I would probably scare her away..."
    m 1r "Okay...fine, I'll do it."
    "Monika takes a deep breath, then timidly enters the classroom."

    scene bg corridor
    with wipeleft_scene

    S s 1a f21
    s "That was fast!"
    S m 1p f22
    m "Oh my gosh, I'm so embarrassed..."
    s 1g "Why? What happened?"
    m 2n "Um..."
    m "Well, I entered the classroom, and she didn't even look up from her book..."
    m 4n "So I kind of just...left the flier on her desk, and then walked out."
    s 1r "Ahaha!"
    s 1a "That's kind of cute."
    m 2o "..."
    s 2x "But I'm sure she'll see it and want to join the club!"
    m 2e "I hope so..."
    m "...Shall we head back now?"
    H s
    H m
    "The two head back to the clubroom, Sayori feeling rather accomplished, and Monika still feeling a bit embarrassed by the encounter."
    $ unlock("bgm_mysongyournote")
    play music p1 fadeout 2.0
    scene bg club_day
    with wipeleft_scene

    "Upon returning, Monika and Sayori resume their strategy meeting."
    "They discuss various different kinds of recruitment tactics, from professional to silly."
    "After going through Sayori's list, and with Monika coming up with ideas of her own, the two end in a better spot than from where they began."
    S m 2a f22
    m "Well, I would say today was pretty productive, wasn't it?"
    S s 1x f21
    s 1a "Yeah!"
    s "I think we're starting to make progress."
    s 4q "I can't wait to get some new members~"
    s 1c "Hey, what's this?"
    "Sayori peers at the sheet of paper Monika was jotting on earlier."
    m 1e "Oh! Don't mind that..."
    m "I was just thinking to myself."
    s 1b "Join the Literature Club..."
    s "Write the way...into your heart?"
    s 4q "That's so cute!"
    m 1l "Ahaha..."
    m "I thought it was a little overdramatic."
    s 1d "But..."
    "Sayori pauses and thinks for a moment."
    s "You know..."
    s "I don't think you give yourself enough credit."
    m 1d "What? What do you mean?"
    s "Like..."
    s "I dunno, I feel like I can tell from talking to you today."
    s "It seems like you're always afraid of doing something wrong."
    m 2m "Yeah, but..."
    s 1a "Would you call yourself a perfectionist?"
    m 1q "..."
    m 1d "...Yeah."
    m "Yeah, I definitely am."
    m 2e "I mean...I always have an idea in my head of how I want things to go."
    m "And it's like, I can't accept anything less than that."
    m 2a "But I think in the end, it helps me try my hardest at everything...so I don't think it's that bad."
    m "Like with this club, we have such an opportunity to make it into exactly how we envision it."
    m 2i "But it feels like we only have one shot at it."
    m "So...I'm just really afraid of it deviating from that. The vision."
    s 2b "What's the vision?"
    m 1d "It's..."
    "Monika pauses to think, then shakes her head to herself."
    "She sighs."
    m 1r "I don't know."
    m "I just want everyone to..."
    m 1q "..."
    "Monika trails off."
    S s 2a t21
    "Smiling, Sayori taps her finger against the sheet of paper."
    "\"Write the way into your heart.\""
    s 2d "I think what you're trying to do..."
    s "...is to make the club that {i}you{/i} need the most, out of anyone."
    s 1a "Well, you're the one who knows yourself best, of course."
    s "But...I'm here to help you."
    S m 2e t22
    "Monika returns Sayori's smile."
    m "It's sort of amazing, how kind you are."
    m "We're really gonna make this the best club ever."
    H m
    H s
    "Sayori nods, and the two remain silent for a moment, lost in thought."
    "The only sound is the steady whisper of the air conditioner."
    "And the only movement is the afternoon sunlight, trickling its way in and out of the moving clouds."
    "Sayori breaks the moment with a big yawn."
    S m 2a f22
    m "Time to go home?"
    S s 1a f21
    s "You tell me. You're the President."
    m 2b "Ahaha."
    m 4b "In that case, today's meeting is officially over."
    m "I look forward to tomorrow."
    s 1q "Me too!"
    "Sayori beams and grabs her things."
    m 1a "You can go on ahead, I need a few minutes still."
    s 1c "Oh, I can wait!"
    m "That's alright, I just want some alone time."
    s 2a "Hmm, in that case..."
    "Sayori waves enthusiastically at Monika."
    s 2q "Good luck."
    H s
    H m
    $ unlock("bgm_dusk")
    play music p7a fadeout 2.0
    "Monika smiles and waves in return as Sayori spins her way out of the clubroom."
    "All alone, she sighs to herself and takes a minute to zone out."
    "She wasn't prepared for the self-reflection encouraged by Sayori, but she decides it was something she probably needed right about now."
    S m 2i f11
    m "The club that I need the most?"
    m 2r "I don't get it..."
    m 2i "I just wanted to start a club with more passion."
    m "Something that I could use to help lead people to happiness."
    m 2e "Literature is the key to that."
    m "Because it's the window to the real person inside of us."
    m "Underneath the person who's forced to always smile and blend in."
    m 1q "The person who's forced to be..."
    m 1o "...Perfect."
    $ pause(2)
    m 1d "...Hm?"
    "Monika suddenly notices a folder on the floor by her desk."
    m "Did Sayori leave this behind?"
    m "I hope it doesn't have her homework in it..."
    "Worried, Monika opens the folder to check."
    m "Poems..."
    "It's a folder of poems."
    $ unlock("become_the_flower")
    call showpoem (poem_ps2, music=False)

    m 1p "What the...?"
    m 1g "Wait..."
    m "Sayori...?"

    $ unlock("sm_part2")
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause(2.0)
    jump desktop_from_side_stories

label sm3:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg corridor
    with dissolve_scene
    play music p7b

    "Another day passes in a flash, and it's already time for the next club meeting."
    "Although Monika should have come up with a plan for today's club tasks, she hasn't been able to shake her guilt and anxiety after reading Sayori's poem."

    scene bg club_day with wipeleft
    S m 1r f11
    m "I'm so stupid..."
    m "How did I let myself be the center of attention?"
    m 1g "Sayori is going through these kinds of feelings, and I'm letting her comfort me instead of the other way around..."
    m 1p "What kind of Club President does that?"
    m "This whole time, I didn't think to ask about her own feelings."
    m "So much for the stupid vision..."
    H m
    "Sayori enters the clubroom with her usual smile."
    "But upon seeing the downcast Monika, her smile quickly fades into an expression of concern."
    S s 1g f21
    s "Monika...?"
    s "Is everything okay?"
    S m 1g f22
    m "..."
    m "...I'm really sorry."
    m "I'm such a terrible friend."
    s 2h "Huh??"
    s "What...are you talking about?"
    s "You're an amazing friend!"
    "Monika shakes her head."
    m 1r "I made this all about myself..."
    m "Even you said so yesterday."
    m 1i "You told me that I'm trying to make the club that I need the most, right?"
    m "But..."
    m 1o "My problems...are so...trivial...compared to yours."
    "Sayori responds quietly."
    s 1g "What are you talking about...?"
    "But as she says that, her face darkens."
    "Through the silence, Sayori mutters her realization."
    s 1k "...I left my folder here..."
    "Monika stares blankly ahead, unable to come up with a response."
    s "...I wasn't ready to share those."
    s "Now you're worrying about me...I don't want that."
    m 1g "But why?"
    m "...We're friends, right?"
    "Wordlessly, Sayori nods."
    m "Friends look out for each other."
    m "I want to be here for you as much as you're here for me."
    "Another long moment passes in silence."
    "The air is incredibly heavy."
    $ pause(2)
    s 1i "This is different."
    s "It wasn't just about you yesterday--it was about the club."
    s "Besides..."
    s 1k "Things were so happy yesterday."
    s "You don't need to do this all of a sudden."
    s "I don't want it."
    s 1h "I like happy."
    s "So..."
    s "If you do this..."
    s 1k "Then you're...just being selfish."
    m 1o "..."
    H s
    H m
    "Monika massages her forehead, struggling through the frustration of such a paradox."
    "It's understandable that Sayori isn't ready to share certain things."
    "But...as unfair as it is for Monika to pry, it's also painful for Monika to force herself to ignore the needs of her friend."
    S m 1p f22
    m "I'm sorry I looked."
    m "I disrespected your privacy."
    S s 1k f21
    s "No...I don't blame you for looking."
    s "You would have at least needed to check if it was mine."
    m 1r "Yeah..."
    "Monika takes a deep breath."
    $ pause(2)
    m 1i "...Okay."
    m "I understand that you don't want me to worry."
    m "And I think I'll be able to put this aside, so that we can move on."
    m 1d "But...can you promise me something?"
    s 1b "Promise you what?"
    "Monika pauses to collect her thoughts."
    $ pause(2)
    m 2i "...This is the Literature Club."
    m "It's a place where people can express themselves in the ways that life normally doesn't allow them to."
    m 2r "That's the vision."
    m 2i "In fact, it's our vision."
    m 2m "Write the way into your heart...or whatever."
    m 2d "So...I just want you to promise me that you'll remember that too."
    m "It doesn't have to be right now...but I want to be here for you when you need it."
    m 2e "I want us to be ourselves like that."
    S s 1d t21
    "Sayori smiles gently."
    s "I'll promise if you promise."
    S m 1a t22
    "Unable to help it, Monika returns Sayori's smile."
    m "I promise."
    s 1a "Me too."
    H s
    H m
    "As the conversation closes, the mood in the room is lifted."
    "With that behind them, it's time to proceed with the club activities."
    play music p1 fadeout 2.0
    S m 2a f22
    m "So..."
    m "Wanna teach me about poetry?"
    S s 4m f21
    s "Huh??"
    s 4h "But...what about recruitment?"
    m 2a "It's fine... We have plenty of time for that."
    m "But right now, I feel like I want to do this."
    m "I mean, I do have to fulfill my end of the promise...you know?"
    s 1q "Ehehe."
    s 1a "There's no way I could say no to that."
    s 1l "Just don't expect much..."
    s "I do a lot of writing, but it's not like I'm a scholar or anything."
    m 2a "That's fine."
    m "I think I just need like, some motivation..."
    m 2e "I never know where to start when it comes to writing poems."
    s 1x "Starting isn't so hard!"
    s "You kinda just need to write down your feelings, and see where it takes you."
    m 1g "Yeah, but...that wouldn't come out any good."
    s 1c "It's not supposed to."
    s 1q "You're gonna have to fight your perfectionist mind on this one. Ehehe."
    s 1x "You can just start by writing your feelings, and...see what kinds of things it makes you think of."
    s "And then you can turn your feelings into a little story."
    m 1q "Hmm..."
    s 2a "You can get your feelings down first, and then make it sound pretty later."
    s 2b "It's like...it's not like building a railroad, where you go from one end to the other."
    s 2a "It's more like a collage, where you find all the things you want to put in, and then you arrange them in a pretty way."
    s "At least, that's how I do it...it's not like it's the only way."
    s "But it's a really good way to not get stuck right at the beginning."
    m 1d "I understand..."
    m 1e "Yeah...I always get so caught up in how it sounds that I forget about what's actually important."
    "Monika pulls out a pen and paper to start writing on."
    m 1i "'Stop being a perfectionist'..."
    m "'You idiot.'"
    m 1j "Ahaha, I'm just kidding."
    "Monika scribbles out \"You idiot\" after she writes it down."
    s 1c "No, keep it!"
    m 1a "What, why?"
    m "Are you calling me an idiot?"
    s 1h "Of course not!"
    s "But...the point is that you're not supposed to police your feelings, right?"
    s 1a "Be as dramatic as you want."
    m 1l "Ahaha. But I was just..."
    m "Well...yeah."
    "Underneath the scribble, Monika rewrites \"You idiot\". She stares at the paper."
    "Her words stare back at her."
    m 1n "It's kind of funny how I wrote down what I'm mad at myself for...and then I did that exact thing anyway."
    m "This is really gonna take some getting used to."
    s 2a "I believe in you."
    m 1e "Thanks...I do too."
    m 1d "Me, I mean."
    m 1a "But also you, of course."
    s 1q "Ehehe."
    H s
    H m
    "Monika continues the exercise, jotting down her thoughts."
    "It's surprisingly quite a struggle to write without overthinking it."
    "But after a while, with Sayori's guidance and encouragement, Monika's sheet of paper begins to look fairly lively, peppered with all of her random thoughts."
    S m 1a f22
    m 1r "Phew..."
    "Monika looks up and down at her sheet."
    m 1m "Gosh, I feel...so tense, looking at this."
    m "I hate it."
    m 1a "But it's also kind of liberating."
    S s 1a f21
    s "Mhm."
    s "I can tell how hard you're trying. It makes me happy."
    s 1x "I think you'll be good at writing poems."
    m 2k "Ahaha. Don't give me too much credit."
    m 2a "I'd have to try really, really hard at it..."
    m "But...I think it's something that I'll enjoy doing."
    m "With you."
    S s 1q t21
    "Sayori beams."
    m 2d "I'll stop here, but we still have time..."
    m 2a "Let's try to work on a new flier for the club."
    m "I won't be so picky about the language."
    s 4x "Yay! Let's do it!"
    H s
    H m
    "Monika and Sayori proceed with their work."
    "With each passing day, the two of them become more confident in the club."
    "Not simply from their recruitment planning...but from their vision, as well."
    "As their bond strengthens, so does the essence of the Literature Club."
    "Finally, they begin to truly feel it's only a matter of time before they find more members..."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    jump sm4

label sm4:

    scene bg corridor
    with dissolve_scene_full

    play music p7a
    "Another day passes."
    "As usual, Monika is the first one to the clubroom."
    "With her is a printout of the revised Literature Club flier, complete with all the new ideas Monika and Sayori came up with."
    scene bg club_day with wipeleft
    S m 1r f11
    m "If only this was the flier we gave to that one reading girl the other day..."
    m "It's so much more attractive than the old one."
    m 1i "But..."
    "The new catchphrase is featured clearly in the center of the flier:"
    "\"Write the way into your heart!\""
    "Surely, common sense would say that one writes {i}from{/i} the heart, not {i}into{/i} the heart."
    "But the message being delivered is that one can use writing to discover themselves."
    "Hopefully--Monika and Sayori had thought--that it would be enough to garner some curiosity from students."
    $ show_content_warning("Written poetic exploration of destruction and self-destruction, with imagery of violence and loss. Includes metaphors involving murder and allusions to suicidal ideation.")
    m 1p "Why do I feel so tense looking at this?"
    "Monika thinks back to the previous meeting, when she performed the writing exercise."
    m "Was I always this bad at expressing myself?"
    m "...How am I supposed to be President if I can't even demonstrate what the club is supposed to be about?"
    H m
    "The Literature Club is truly beginning to take form."
    "But with that, the weight on Monika's shoulders only becomes heavier."
    "Debate Club was always about rigid structure--formulating airtight points and counterpoints, and delivering them with conviction."
    "It was about the person on the {i}outside{/i}."
    "That's why Monika was so good at it--it existed entirely within her realm of comfort."
    S m 1p f11
    m "It's...suffocating."
    m 1r "I need to break through this mental wall."
    m 1i "I need to learn to express myself...for real."
    H m
    "Monika pulls out a sheet of paper and grabs her pen."
    "She presses the tip of the pen firmly against the paper."
    $ pause(2)
    "...But her hand doesn't move."
    "Instead, a tiny blot of ink collects around the tip of her pen."
    "Monika lifts her pen and stares at the little blotch."
    "For some reason, she feels compelled to run her finger across it."
    "As she does so, the black ink smears across the paper, ruining Monika's canvas."
    m 1i "Ugh..."
    "Out of spite for herself, Monika presses her pen down once again, letting the ink collect."
    "She creates a second smear on the paper."
    m "Come on, Monika."
    m "Just move your hand!"
    "Monika writes."
    call showpoem (poem_pm1, music=False, paper="bg/poem_pm1.png")
    m "..."
    "Monika slides the paper away from her and puts her head down on the desk."
    scene black with Dissolve(2)
    $ pause(2)
    "The air conditioner seems louder today."
    $ pause(2)
    s "I'm here."
    m "Hi."
    "Monika hears Sayori approach her desk, then stop for a second, probably reading the piece of paper."
    "Then, she sits down in the adjacent desk."
    s "Bad day?"
    m "Mhm."
    $ pause(2)
    s "Me too."
    scene bg club_day with Dissolve(2)
    S m 1d f22
    m "You too?"
    $ pause(2)
    S s 1d f21
    s "The new flier looks so good."
    s "You've been working so hard."
    s "On the club...but also something else, I think."
    $ pause(2)
    m 1p "...I can't do it."
    m "I'm sorry."
    m "It's so hard to just...be vulnerable."
    s "Mm."
    H s
    H m
    "Sayori takes the sheet of paper from Monika's desk."
    "She writes something down, then stares at it for a while."
    $ pause(2)
    S s 1k f21
    s "Can I trust you?"
    S m 2d f22
    m "Of course."
    m "You can trust me with anything."
    H s
    H m
    "Sayori gazes at Monika with sadness in her eyes."
    "Understanding the signal, Monika takes the paper from Sayori's desk and reads it."
    stop music fadeout 2.0
    $ pause(2)
    call showpoem (poem_ps3, music=False, paper="bg/poem_pm1.png")

    play music p7c
    S m 1a f22
    m 1g "Sayori..."
    S s 1k f21
    s "..."
    s "This is really...really...hard for me."
    "Her voice shakes."
    s 1t "So if I can do it..."
    s "...Then you can, too."
    s "Because..."
    s "You're like a million times better than me."
    m 2m "That's completely not true."
    "Sayori takes a deep breath, trying to steady herself."
    $ pause(2)
    s 1l "That's something about me that I've never told anyone before."
    s "Even now...my head is, like...screaming at me to stop."
    m 1g "Wait! You don't...you don't have to force yourself!"
    m "I mean, just because of the promise yesterday..."
    s 1i "I want to."
    s "It just...feels right."
    s 1k "I mean...maybe it's part of the reason I came to this club in the first place."
    $ pause(2)
    s 1i "This is the Literature Club."
    s "I trust you. More than I'm scared."
    H s
    H m
    "At those words, Monika stands up."
    "Sayori must have taken days to work up the courage for this."
    "Were Monika's own futile--but genuine--efforts actually the push that Sayori needed?"
    "Sayori's deliberate breaths can be heard over the air conditioner."
    "As she prepares herself to continue, Monika waits in gentle silence."
    $ pause(2)
    S s 1k f21
    s "I have this...problem...where I get really upset when people worry too much about me."
    s "I can't control it..."
    s 1d "It's like...why waste your energy worrying about me when you can just be happy instead?"
    s "So I never tell anyone about these kinds of thoughts that I have."
    s 1k "It's so much easier to just smile and help everyone else be happy."
    S m 1g f22
    m "But that's..."
    "Terrible."
    "That's what Monika wants to say, but she stops herself in fear of saying the wrong thing."
    s 1d "It's just that if everyone knew about it...they wouldn't treat me the same anymore."
    s "Like whenever I'm not smiling, everyone would worry about me and ask me what's wrong."
    s 1k "I know that...because it used to be like that."
    "Sayori pauses, seeming to recall something in the past."
    s 1g "I just want everyone to be happy."
    s "That's the most important thing to me."
    s 1k "And...letting people look inside my head doesn't bring happiness to anyone."
    "Sayori pauses again, her solemn expression making her look almost like an entirely different person."
    m 1g "How did you find the courage to tell me this?"
    m "You're not...worried that I'll be one of those people too?"
    s 1g "I am worried."
    s "Part of me really hates myself for doing this."
    s 1d "But another part of me...I think, just felt like it would be different this time."
    s "Whenever we talk about what the club is supposed to mean, I kept feeling like it was right for me to do."
    s 1l "Especially after you've been trying so hard to express yourself, too."
    s "It just...made me feel like I could say it in confidence, and our friendship doesn't have to change."
    s 1t "Ahaha."
    s "It's so silly...the club is only two people, but it already means this much to me."
    scene black with Dissolve(1)
    "Monika feels a tightening sensation in her heart."
    "A feeling of connection as Sayori's emotions radiate between them."
    m "Me too."
    m "I was...so lost until you showed up."
    m "You're so brave, Sayori. You're so strong and brave. I don't even compare."
    "Monika steps forward."
    m "But...if nothing else, I can at least offer you some hug energy."
    m "If you'd like."
    $ unlock("bgm_hugenergy")
    play music p9 fadeout 2.0
    $ unlock("sm_exclusive")
    scene sm_base with Dissolve(2.0)
    "Wordlessly, and without a smile, Sayori rests her forehead on Monika's shoulder."
    "Through their contact, Monika can almost feel the torrent of thoughts swimming in Sayori's head."
    "And in this moment, enchanted by the air of the club..."
    "Monika realizes that of all the days that have passed, this is the one where she really, really hopes that nobody new walks through the door."
    "She speaks softly."
    show sm_m1:
        alpha 0
        linear 0.5 alpha 1
    show sm_m2:
        alpha 0
        linear 0.5 alpha 1
    m "You're like...the sweetest girl I've ever met."
    m "You can say anything. I'll never judge you."
    m "I promise."
    "Sayori's breath begins to quiver."
    "She takes several deep breaths, trying as hard as she can to start speaking, to say the things she never once dared to say out loud."
    "Finally, she speaks in a choked voice."
    show sm_m2:
        alpha 1
        linear 0.5 alpha 0
    show sm_s2:
        alpha 0
        linear 0.5 alpha 1
    show sm_s4 zorder 3:
        alpha 0
        linear 0.5 alpha 1
    s "I'm...so worthless."
    s "I'm worthless and everyone would be better off without me."
    show sm_s5 zorder 3:
        alpha 0
        linear 0.5 alpha 1
    "She suppresses a sob as a tear falls down her cheek."
    show sm_s3:
        alpha 0
        linear 0.5 alpha 1
    s "I'm just...an inconvenience to everyone."
    s "I'm not good at anything, and it just feels like everyone just has to put up with me, and I hate it. I hate it."
    "The more Sayori speaks, the more she fails to control her voice, falling victim to the overwhelming sadness clutching at her throat and chest."
    show sm_s1:
        alpha 0
        linear 0.5 alpha 1
    s "I don't want to have these thoughts. I want them to go away. And now I'm making you put up with me and I just want to die!"
    show sm_m1:
        alpha 1
        linear 0.5 alpha 0
    "As soon as Sayori loses her composure, Monika becomes determined to keep her own."
    "She only wants to be what Sayori needs right now."
    "So, she won't let any sadness show."
    "Her voice comes through as soft and gentle."
    show sm_m1:
        alpha 0
        linear 0.5 alpha 1
    show sm_m2:
        alpha 0
        linear 0.5 alpha 1
    m "This isn't putting up with you."
    m "It's just being your friend."
    show sm_s1:
        alpha 1
        linear 0.5 alpha 0
    "Monika offers a few words of comfort."
    "But she knows--Sayori said it herself--that the thoughts Sayori experiences are ones that don't belong."
    "And Monika can't magically make them go away."
    "The most she can do is help Sayori battle them, like any good friend would do."
    show sm_m1:
        alpha 1
        linear 0.5 alpha 0
    m "You have so much value."
    m "To me, and your other friends, too."
    m "This club wouldn't have been the same without you."
    m "I really, really mean that."
    show sm_m1:
        alpha 0
        linear 0.5 alpha 1
    m "You coming here was the best thing that could have happened."
    m "Even if we never got any other members...I would still be happy."
    m "That's what you brought here."
    m "You brought us a vision...and you also brought happiness."
    show sm_m1:
        alpha 1
        linear 0.5 alpha 0
    m "And that's your favorite thing to do...right?"
    "Sayori doesn't respond, but Monika feels her gently nod."
    "No more words are needed between them."
    scene black with Dissolve(2.0)
    "The two share their embrace for a while longer, Monika letting Sayori take as much time as she needs."
    "Once her breathing steadies and her sniffles fully cease, Sayori lifts her head and wipes her eyes."
    play music p1 fadeout 2.0
    scene bg club_day with Dissolve(2.0)
    S s 1l f21
    s "I guess I needed that."
    s "Some days are harder than others."
    S m 1e f22
    m "Well, I'm here whenever you need me."
    m "But any other time...I'll make sure that things are the way they usually are."
    m "If that's what makes you happy."
    s 1d "Mhm."
    s "Thanks."
    s 1q "You're the best."
    m 2a "No, you are."
    "The two exchange smiles."
    m 2d "You know...I'm sorry to bring this up all of a sudden, but...have you considered talking to a professional?"
    "Sayori nods."
    s 1l "It's scary."
    s "Since it's already so hard to tell people..."
    m 2e "Yeah."
    m "Well...of course it will always be your choice, but if you're ever looking to find the courage for it, I can do my best to help you."
    s 1d "Thanks."
    s "I think it helps knowing that you would."
    "Sayori suddenly yawns and stretches."
    s 4p "Wow, that made me tired!"
    s "And hungry..."
    m 1j "Ahaha."
    m 1a "Well, I won't make you do any work today if you're not up for it."
    s 1b "No, I want to!"
    s 1a "I mean...I can say that it's definitely one thing that makes me happy."
    S m 1j t22
    "Monika smiles."
    s 2l "...But I might want to get a snack first."
    H s
    H m
    "All of a sudden, the sound of the door causes the two of them to turn their heads."
    "The door opens halfway, then stops. A face peeks inside."
    "A face that seems familiar..."

    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    pause(2.0)
    $ unlock("sidestory1")
    $ plus_persistent.side_stories_read[0] = True
    jump desktop_from_side_stories
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

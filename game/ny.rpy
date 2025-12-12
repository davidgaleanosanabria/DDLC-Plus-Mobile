label ny1:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg corridor with Dissolve(2)


    "It's only been one day since Yuri's letter was delivered to Natsuki, with Monika's help."
    "Because Yuri chose not to attend the club meeting that day, she and Natsuki haven't faced each other since."
    "Although it's only lunchtime, Yuri finds herself anxiously counting the hours until she will need to face the outcome of her efforts - whether good or bad."
    "And because the passing by of students was making her feel even more anxious, Yuri picked out the most secluded spot she could find to spend her lunch."
    stop music fadeout 2.0
    scene bg pstairwell
    $ unlock("bg_stairwell")
    show yuri 1l at t11
    with wipeleft
    "Because this staircase is under maintenance, no student would have any reason for coming here."
    "It's such a relaxing feeling to have a moment of solitude in the middle of a frantic school day--"
    $ unlock("bgm_dusk")
    play music p7b
    S y 1l t22
    S n 1p f21
    n "--!"
    S y 3n f22
    y "Eep--"
    n 5q "...What are you doing here?"
    y 3o "Um--"
    y "I-I just--"
    "Yuri grips her book with enough force to wrinkle the pages beneath the pressure of her thumbs."
    y 3l "Well--what are {i}you{/i} doing here?"
    n 5s "..."
    n 5q "I just...came to get a drink from the vending machine."
    n 5w "The other one is out of the drink I like."
    H n
    H y
    "Yuri notices Natsuki fidgeting with a few coins between her fingers."
    "She nods, avoiding eye contact."
    "Natsuki, also looking away, shuffles over to the vending machine."
    "It's so quiet that every one of her movements seems to reverberate through the entire stairwell."
    "After far too long, she finally receives her beverage, which she then fidgets with in place of the coins."
    "It's some kind of iced tea."
    "But instead of leaving right away, Natsuki just stands in place. She glances all around her."
    S n 5q f21
    n "It's like, way too quiet back here...it's creepy."
    n 5p "I mean--"
    n 42c "That's--not what I meant, really. I mean...it's totally cool that it's your thing, or whatever...like, I can see how it suits you, so..."
    n 1h "Not--because I think you're creepy or something! I didn't mean that either!"
    n 5u "You know, I'm just gonna stop talking. That seems like a good idea."
    S y 3n f22
    y 4b "It's okay."
    y "Everything...is okay."
    H n
    H y
    "Yuri finds herself attempting some words of comfort after hearing Natsuki stammer herself into dejection."
    "Seemingly in response, Natsuki approaches the base of the staircase and hesitantly sits herself down near Yuri."
    S n 4s f21
    n "Well, I can leave if you want."
    H n
    "Yuri shakes her head."
    "Natsuki twists the cap off her drink and takes a sip."
    $ pause(2)
    "Despite receiving Yuri's general permission, Natsuki doesn't say anything more."
    "Yuri continues to read, or at least pretends to."
    scene black with Dissolve(2)
    "And the two just sit there for a long time."
    "The tension seems to fade a little bit as time passes."
    "Even without any words, this seems to mean at least something--though it's not clear what that may be."
    scene bg pstairwell with Dissolve(2)
    "Lunch ends more quickly than expected."
    "Natsuki is the first to stand up, with her empty drink bottle."
    S y 3e t22
    S n 5h f21
    n "Are you coming today?"
    n "To the club."
    "Yuri nods."
    n 12a "I'm sorry for...being so awkward."
    n 12b "I'm really bad at talking about...this stuff."
    n "I just can't, for some reason. I don't know why."
    n 4q "But I want to. Eventually."
    S y 3v f22
    y "There's no rush."
    y "I promise."
    n "...Thanks."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ pause(1)

    jump ny2

label ny2:
    scene bg pstairwell with Dissolve(2)
    play music p7a
    "It's the next day."
    "Natsuki appears from around the corner and steps up to the vending machine, glancing at Yuri as she does so."
    "Today, she seems to be holding some kind of book as well."
    $ unlock("bgm_strawberrypeppermint")
    play music p3 fadeout 2.0
    S n 1c f21
    n "Oh, you're here again."
    S n 4w f21
    n "...Well, I just came here to read this. Because there aren't any people around here."
    S y 1a f22
    y 2e "Oh? I thought you didn't like how quiet it was?"
    n 4t "Well...I don't. But there's no people here."
    y 2g "I see."
    H n
    H y
    "Natsuki sits down."
    "The mood feels much different today than it did yesterday."
    "After yesterday's lunch and the club meeting that followed, Natsuki and Yuri are beginning to feel more relaxed around each other again."
    "Although Yuri's letter is still lingering in the back of Natsuki's mind, she continues to detour around it."
    S y 2v f22
    y "But it's okay that I'm here?"
    S n 5c f21
    n "Yeah, I don't care."
    n "I mostly just don't feel like dealing with the crap I get from my friends about it."
    n 5t "Especially since like...they all just assumed I stopped reading manga after I joined the Literature Club."
    n 5q "Not that I'm trying to hide it from them, exactly..."
    n 4x "But I just don't want it to come up again {i}now{/i} after I've waited so long for this new volume to come out. Literally months at this point."
    y 1f "You don't have other friends who are into manga?"
    n 3c "Not unless online friends count."
    n "And Sayori, but that's different 'cause she's not exactly {i}into{/i} it, she just likes it, you know what I mean?"
    y 1m "Mhm."
    n 4c "Honestly, you're lucky that the books you're into at least just look like books, so you don't have to feel like everyone is constantly judging you by what you're reading."
    y 3l "That would be so awful..."
    y "Especially since I already hate attention so much."
    n 5c "Well, it's a good thing I have thick skin, I guess."
    n 5a "By the way, I would totally recommend finding some friends online if you haven't already. If you're like me and have no one to share your hobbies with."
    y 2a "Oh, I have online friends."
    y 2u "Since middle school, actually. I was especially desperate back then."
    y "It's...somewhat embarrassing to reminisce about those days."
    y 2w "Sometimes I feel like the me from a few years ago would have benefited from a good smack across the face..."
    n 4c "Oh, whatever. We were all just stupid kids back then anyway."
    n 4t "Some of the fanfics I wrote...thank god I used a pseudonym."
    n 4y "But I liked it at the time. I got a lot of fulfillment out of it."
    n 4a "And plus, I can look back and say with confidence that I've become a better person since then."
    n "So I don't think I would change anything."
    y 3v "I wonder if a few years from now, we'll think the same thing about our current selves...?"
    n 5z "Ahaha! Probably."
    y 3t "That doesn't make you uncomfortable?"
    n 5d "No, of course not! I don't care what other people think of me. Especially someone who doesn't even exist yet."
    y 4b "Mm..."
    n 3a "Alright, here--"
    H n
    "Natsuki raises her hand to her face and forcefully slaps her own cheek."
    S n 3y f21
    n "That's me from the future coming to terms with me right now."
    n 3s "Also, ow. I didn't mean to do it that hard."
    H n
    H y
    "Yuri doesn't seem to react."
    "But then, to Natsuki's surprise, Yuri shyly looks the other way before lifting her arm and doing the same thing to herself, loudly smacking her cheek."
    S y 4e t11
    "She turns red and stares into her lap, but is unable to hide a smile, as though it was a really funny joke."
    S y 4e t22
    S n 5a f21
    n "Oh, that's what I'm talking about. I didn't know you had it in you."
    y 3o "I...I don't. I don't even know why I did that."
    y "Maybe I thought it would be funny."
    y 3v "--Sorry, I keep distracting you..."
    y 4b "You said you were looking forward to reading, but I keep going on about all this nonsense."
    y "I'll let you get to your reading."
    n 1q "Oh...right."
    $ pause(2)
    n 1t "...Yeah, I guess I'll do that, then."
    H n
    H y
    "The conversation ends quickly, and Natsuki opens her book."
    scene black with Dissolve(2)
    "The two read silently for the remainder of the lunch hour."
    "But the whole time, Yuri feels distracted by a twist of regret over having so abruptly forced the end of their conversation."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ pause(1)

    jump ny3

label ny3:
    scene bg pstairwell with Dissolve(2)
    $ unlock("bgm_lavendermist")
    play music p4
    S y 2f f22
    y "You're back."
    S n 3q f21
    n "Yeah, I'm here to lay low again."
    "Another day has passed."
    "During lunchtime, Natsuki finds herself having wandered to the stairwell once more."
    n 3c "Hey, did you buy that?"
    "Natsuki quickly notices a bottle of iced tea on the staircase where she normally sits."
    S y 4b t22
    "Yuri nods, avoiding eye contact."
    n 5q "What, like for me?"
    n "But you didn't know I was coming here today. What if I didn't show up?"
    y 4d "Well--"
    y 4c "I just--I mean, I would have drank it myself, I guess..."
    y "It was a stupid thing to do."
    n 5m "No, it--it wasn't {i}stupid{/i}."
    n 5u "I just thought--"
    n 12b "...Never mind."
    n "What I meant to say is thank you."
    n "And that it's a really nice gesture."
    y 4b "It's...it's okay if you don't feel that way..."
    n 42c "I do!"
    n "It was the other things that I didn't mean."
    n 1n "I swear. Please believe me."
    y 3v "Mm..."
    "Yuri pauses, then nods."
    y 3l "Talking...is hard. I get it wrong a lot too."
    y "So I believe you."
    H n
    H y
    "Natsuki exhales in relief."
    "She then sits down next to Yuri and takes the drink."
    "Knowing Yuri, she was probably overthinking it so much that Natsuki's tepid response filled her with self-doubt."
    S n 5q f21
    n "...I'll do something nice for you next time."
    S y 3v f22
    y "Please, don't feel obligated--"
    n 5w "I want to!"
    n "I wanna do nice things too."
    y 4b "...Okay."
    y "Thank you."
    n 5s "You can thank me after I figure out how to do something nice."
    y 3u "I'll do it then, too."
    "Natsuki sighs."
    y 3e "Hm?"
    n 5q "Nothing..."
    n "It just reminds me how I haven't been getting along with my friends lately..."
    y 3f "Is that why you've been coming here?"
    n 5g "Well, no, not exactly..."
    n "I haven't been avoiding them on purpose or anything."
    n 4q "There are just...other things I'd rather be doing during lunch lately."
    n 4c "I like being around them when we're all just having fun, but they also just can't take anything seriously."
    n 5q "So when I'm...I dunno, feeling serious...then their attitudes just really get on my nerves."
    n 5s "It's only gotten worse ever since I joined the Literature Club."
    y 2f "How come?"
    n 5q "I don't know."
    n 5t "I feel like I used to be really good with just putting up with it. Because it would be so stupid to cause drama over a joke I didn't like or something."
    n 5s "But I just...have a hard time doing that lately."
    n 42c "But it's my fault for being overly sensitive. If I have a problem, I'm not gonna demand for everyone around me to change!"
    y 3v "But..."
    n 1s "Yeah, I know."
    n "Monika and Sayori really don't agree with that kind of thing."
    n 4b "But they're not in my position, so it's easy for them to say that you should just communicate your feelings, or whatever."
    n 5w "It's not like {i}my{/i} friend group does that kind of thing! I would just be making an embarrassment of myself."
    n 5s "...Sorry, none of this has anything to do with you. I don't know why I'm talking about it."
    y 2t "It's okay..."
    y "I like listening."
    n 4c "What? Listening to other people's problems?"
    y 3m "Yes."
    n 5z "Ahaha! That's weird."
    y 3g "..."
    n 5q "...Sorry."
    y 3t "I just...like learning about people."
    y "Do you think it's weird?"
    n 1t "N-No! That's not weird! I probably just misunderstood, so..."
    n 1q "I dunno...does that mean I should keep going?"
    y 3v "If you'd like..."
    n "Okay..."
    n 5i "Well, I don't know what to talk about now."
    y 2f "What are some things that you like about your friends?"
    n 4k "A lot of things!"
    n 4j "I mean, they're really fun to hang out with, like after school and on the weekends..."
    n "And they really like my baking..."
    n 3d "And it's fun to complain about school together."
    n 3j "They make me laugh a lot. And we have a lot of good memories and inside jokes."
    y 3v "Oh..."
    y "I'm bad at a lot of those things."
    n 3c "...So?"
    y 4a "Are those all things that are important to you?"
    n 5c "Well...kind of, but they're not things I need to get out of {i}everybody{/i}."
    n "Everyone in the club is really different from that, but I'm still friends with them too."
    y 2f "Well, Sayori really likes your baking."
    y "And she makes you laugh."
    y 2j "...And she complains a lot."
    n "That doesn't mean she's anything like my other friends."
    y 1h "Well unlike them, she's a nice person who cares about your feelings."
    n 1f "Excuse me?"
    n 1e "How about you don't talk that way about my friends that you don't know anything about?"
    "Natsuki stands up."
    y 3n "No, wait--"
    y 3o "I'm sorry! I didn't mean it!"
    y "I didn't want to say something bad."
    y 4c "Please don't leave..."
    n 42b "..."
    "Natsuki sighs and shakes her head."
    n 42c "...It's fine."
    n "As long as you understand that you can't just judge people like that."
    y 4b "I'm sorry."
    "Natsuki sits back down."
    n 5s "You can't just compare friends like that and like...measure who's better than who. Everyone's different."
    y 3v "I'm sorry."
    y "I just..."
    y 4b "..."
    y "I just...don't like people who want to hurt you."
    n "..."
    H n
    H y
    "A moment of silence stretches between them."
    play music p7b fadeout 2.0
    $ pause(2)
    S n 3h f21
    n "They don't want to hurt me."
    n 3q "We just like to tease each other about stupid things. It's fun."
    S y 3h f22
    y "I don't like that."
    n 3h "Well, that's why I'm friends with them and you're not."
    y "You like it?"
    n 5s "..."
    n 5q "...Just don't worry so much about me."
    n 12a "It's not worth it."
    y 3v "I'm sorry."
    y "I wish I knew how to help with social conflicts."
    y 3l "Like how Monika can."
    y "She's good at these things."
    S y 3f t22
    n 5h "Not really."
    n 5q "Also, I don't always want help. Sometimes it's just stuff I have to deal with myself."
    n 5w "That's what Monika and Sayori never seem to understand."
    n 5t "Sometimes all you do is look at them wrong and they're all like 'Aw, what's wrong? Is everything okay?'"
    n 42c "I just wanna mind my own business sometimes! And decide myself if I want to talk about things."
    n 42a "The only one who understands that is you."
    n 42b "So you really shouldn't be so hard on yourself. You're not...as bad as you think."
    y 3v "Oh...you don't need to reassure me or anything..."
    n 5q "I mean that."
    n 5t "Plus, it makes sense that someone who doesn't talk a lot would make a good listener."
    $ pause(2)
    y 3u "Thank you."
    y "You're...also nice."
    n 5u "..."
    $ pause(2)
    n "It's really hard for me."
    n "It doesn't come naturally at all."
    n 5q "It's so weird because I always thought of myself as someone who can just say whatever's on my mind."
    n "But I feel like that only works when I'm annoyed, or upset, or I want to say something mean."
    n 1x "Why am I like that?"
    n 1s "You don't have to answer that, I'm just talking to myself."
    S y 1e t22
    "Yuri nods and remains silent."
    "Natsuki notices her fidgeting with the pages of her book."
    n 3c "How come you like reading so much?"
    y 2h "Oh, um..."
    y 2f "Well, a lot of reasons."
    y 3m "But...I just get sucked into it so easily."
    y "It's so immersive. Like I want to be a part of it."
    y 1h "I think...there are a lot of things about people in real life that make me feel uncomfortable and frustrated."
    y "Especially when it comes to following social conventions. And group interactions."
    y 1l "I just...don't really understand it, and I have no real desire to participate."
    y 1i "But it's different with books. It feels like I always want to be around the characters."
    y "I feel such a strong emotional connection with them in ways that I've never felt with real people."
    y 1m "So...in that way, it can sometimes feel more real than real life."
    n 1c "Really?"
    n "It's that hard for you to be around people? Like...all the time?"
    y 1g "Mm...fairly often. Especially in group settings."
    y 3w "When people are making all kinds of conversation, and saying jokes, and all of that...I don't know what to do, and I just disengage."
    n 3m "Oh..."
    n "That doesn't get lonely?"
    y 3v "I don't think so."
    y 3u "I can still enjoy spending time with people one on one. And I have online friends too, of course."
    $ pause(2)
    n 5q "Do you ever...do you ever wish that you could be friends with the characters in your books?"
    y 3l "All the time."
    y 3w "Sometimes so badly that it makes my heart ache."
    n 5u "Yeah..."
    n "Me too."
    y 3t "Really...?"
    n 12a "Mhm."
    n "A lot."
    $ pause(2)
    n "Like...more than anything."
    H n
    H y
    "After Natsuki mutters that, silence fills the stairwell once more."
    "But it's a mutual silence."
    "One full of understanding."
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    $ unlock("ny_part2")
    jump desktop_from_side_stories

label ny4:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    scene bg pstairwell with Dissolve(2)

    $ show_content_warning("Discussion of self-hate and the experience of intense social anxiety.")

    $ unlock("bgm_mysongyournote")
    play music p1

    S n 3k f21
    n "Hey."
    S y 1a f22
    y "Oh, hello."
    y "I almost thought you weren't coming today."
    n 3c "Yeah, well..."
    H n
    H y
    "Lunch is already more than halfway over."
    "Natsuki had typically been meeting Yuri in the stairwell much earlier, since it had been a good way of dodging her friends when she didn't feel like seeing them."
    "Today, she's holding a large plastic container in both hands."
    S n 3c f21
    n "I ran into my friends, so I hung out with them for a while."
    S y 1f f22
    y "Is that so?"
    n "Yeah."
    n 3a "I was in a good mood today, so I figured I should. I hadn't seen them in a while. Which I had to come up with an excuse for, but I expected that."
    n 3k "Plus, I have way more of these than I know what to do with, so I figured I would share with them too..."
    "As she sits down, Natsuki opens the lid of her container."
    y 2a "You made cupcakes."
    n 5d "You know it."
    n "It's been a while at this point, so...I figured it was about time again."
    n 5a "You can take one if you want."
    H n
    H y
    "Yuri takes a cupcake and carefully twirls it between her fingers."
    "It's brown, with dark green frosting immaculately shaped into a floral pattern and topped with some kind of glittery powder."
    S y 2m f22
    y "How pretty."
    y 2i "I just ate, so I may not be able to finish it..."
    y 2f "Are they for the club?"
    S n 4k f21
    n "Yeah, I guess so."
    n "I didn't really think about it, I just made them."
    y 2a "Ah...I just thought that because green is Monika's favorite color, right?"
    n 4t "Well--yeah, but that's not really..."
    "Yuri takes a small bite."
    y 2f "...This is green tea flavored."
    n 4s "..."
    y 1c "I love green tea."
    n 5y "Oh--do you?"
    n "It was just a random idea I wanted to try, so..."
    y 3d "Ahaha."
    n 5n "Don't laugh at me..."
    y 3o "I'm...I'm not."
    y 3u "I just felt happy."
    n 5q "Oh...sorry."
    n "Usually when--"
    n 42c "...Never mind. What I mean is that I'm glad."
    n 12a "Sorry for saying dumb things again."
    n "I just wanted to do something nice."
    n "And this is something I happen to be good at."
    n 3t "And I do know that you like them. From past experience."
    y 3n "Mm--"
    H n
    H y
    "Yuri turns red, recalling the time she treated herself rather generously to Natsuki's cupcakes."
    "Ironically, her mouth is too full of cupcake for her to stammer an excuse, so she just settles for a disapproving look."
    S y 1f f22
    y "How did you get into baking?"
    S n 3k f21
    n "Oh, well...I dunno. It kinda just always appealed to me."
    n 3y "Well, a few years ago, I read this one manga with a lot of baking, so I got like super into it for a while. I was probably making stuff almost every day."
    n 3j "But it's something that I always knew I liked anyway. It's like...baking is like art, but when you get good at it, it gets more delicious too."
    y 2j "I'm struggling to imagine myself putting my heart into something so artistic, knowing that it would just be eaten afterwards."
    n 3z "Ahaha. Yeah, maybe you're too practical for it."
    y 3u "I think I prefer to be on the receiving end."
    n 4d "Thats my other favorite part about it."
    n "It's something I can do that makes a lot of people happy. Like, unconditionally."
    n 4a "Everyone is always so thankful, and in that moment you get to be like the bringer of joy."
    n 5k "I dunno. It just makes me feel..."
    y 3f "Valued?"
    n 5c "...Yeah. I guess that."
    y 1a "So you were able to make up with your friends today?"
    n 3k "Hm? There wasn't really anything to make up with them about. We weren't fighting or anything."
    y 2f "You weren't...?"
    y 2h "Maybe I misunderstood..."
    n 5g "It only turns into a fight if I lose my cool. And that's just unnecessary drama. It only makes things worse."
    y 2t "So...they're not going to stop?"
    n 5q "I mean, it only happens sometimes anyway."
    n 42c "It's just the way they are. I'm the only one who ever has a problem with it."
    n "It's not worth it."
    n 5t "Especially since I have somewhere to go now when I don't feel like hanging out with them."
    y 2h "Oh..."
    y "I see."
    play music p7c fadeout 2.0
    "The cupcake's empty foil wrapper audibly crinkles as Yuri clenches a fist."
    y 2l "I'm glad that the situation is resolved."
    y 2h "And that you don't have to...avoid them anymore."
    n 5q "...Yeah."
    n "Me too."
    $ pause(2)
    n 5t "...And I don't have to bother you during your alone time anymore."
    n "I'm sure you have a lot of reading to catch up on."
    y 4b "...Yeah."
    $ pause(2)
    n 12a "I know that...that cupcakes are basically nothing compared to all the stuff you've done for me."
    n "But it's the best I can do."
    n "So you can have the rest of them."
    H n
    H y
    "Natsuki grabs the box and slides it over to Yuri's feet."
    "Yuri stares at the box."
    "Then, she shakes her head and slides them back."
    S y 3l f22
    y "You should save them for your other friends."
    S n 1h f21
    n "But--"
    n 1n "I made them for you."
    "Natsuki's voice whines as she protests."
    y "I know."
    y 3a "And I liked them very much. Exactly as you thought."
    y 3m "You succeeded."
    y 3l "...But I know you care about making your other friends happy, too."
    y 3h "And if this is the way you know how to make that happen...then I'm not going to take it from you."
    n 12c "No! They were for making {i}you{/i} happy!"
    y 3r "{i}You{/i} make me happy!"
    y "You're worth more than cupcakes to some people."
    y 2h "That's why they...want to spend time with you."
    y 4b "And be your friend."
    $ unlock("bgm_piecebypiece")
    play music p8 fadeout 2.0
    H n
    H y
    "Without warning, tears pour from Natsuki's eyes."
    "She pulls her knees to her chest and starts sobbing into her arms."
    S y 3n f22
    y "Natsuki--"
    S n 12f f21
    n "I'm such a bad person--!"
    y 3o "U-Um--"
    "Yuri stammers, feeling panicked."
    y "I didn't mean to say something bad..."
    "Natsuki shakes her head and wipes her eyes."
    n 12g "You didn't."
    n "I just--"
    "Natsuki tries to choke back her sobs, but struggles to speak through them."
    n 12f "I just really hate myself sometimes."
    n "And it feels so wrong when you say those nice things to me."
    n "Like I don't deserve it."
    y 3t "I'm sorry..."
    n 12i "No, I am."
    n "I'm so difficult."
    n 12f "And I can't--think of even a single thing about myself that somebody would like."
    y "..."
    n 12i "And I hated myself for bothering you during lunch."
    n "I just thought it was--my chance to be a good person, like to be nice and do the things you wrote about in the letter."
    n 12h "I knew if I tried in the club, Sayori and Monika would be super annoying and make a huge deal out of it."
    y "You know..."
    y "I think a lot of those negative things too, about myself."
    y 3w "I never felt like a good person. I always...scrutinize everything I say, and later I feel like I said all the wrong things."
    y 3h "And I just spend so much time thinking about myself. Hating myself. And feeling like everyone else must hate me, too."
    y 3l "So...I understand some of that through my own experience."
    y 3v "And that's why I wanted to write the letter and express my feelings."
    y "It...pained me to see those things in someone else that I saw in myself."
    n 12f "..."
    H n
    H y
    "Natsuki sniffles. Yuri rustles through her bag and pulls out some tissues, then hands them to Natsuki."
    S y 1f f22
    y "Monika told me that it takes a good person to reflect on these things."
    y 1m "The desire to improve yourself. That makes you a good person. So don't worry so much."
    y 3v "Also...there are things about you that...people would like, so..."
    $ pause(2)
    S n 12g f21
    n "...Like what?"
    y 3t "..."
    y 3v "Like..."
    y "Like how you're fun for people to be around."
    y "And you're not shy. And you know how to make people laugh."
    y "And you're very passionate about things, and you know how to take the lead."
    y "And you care a lot about other people."
    y 4b "And just...a lot of things..."
    n "Oh..."
    $ pause(2)
    n 5u "Well, now you're making me feel really embarrassed."
    y 3o "Well--you're the one who asked!"
    y 3v "And don't you think {i}I{/i} feel embarrassed?"
    "Natsuki tries to hide a smile. Then, she sighs as it fades again."
    n 1q "Every time I come here, I always think it's the last time, but then I keep coming back for some reason."
    y 3t "Is that...bad?"
    n 5s "..."
    n "Just really confusing."
    n 4q "I mean, my friends and I go way back. So ditching them all the time feels like...I dunno."
    y 3f "Feels like what?"
    "Natsuki's voice gets quiet."
    n 12a "...Maybe I'm scared that they'll get mad at me."
    y 4b "Mm..."
    n "I really don't know what to do."
    "She pauses. Yuri stares into the distance, tracing her eyes along the patterns of the floor tiles while she thinks to herself."
    y 4a "What would you do, hypothetically, if your friends were happy for you instead of mad at you?"
    n 5c "Happy for what?"
    y 3h "Happy that your new club is making you happy."
    n 5u "Well--"
    n 42c "That's just...not a fair hypothetical."
    "Natsuki says that, but with little confidence in her voice."
    n 42a "I always...told myself that I don't rely on the approval of others to be happy."
    n "And I still feel that way, but..."
    n 12b "I'm spending time with people who put me down whenever I don't have their approval."
    n "That's probably what's making me feel so confused."
    n 5s "Because...I'm threatened out of the things that {i}should{/i} make me happy."
    n "So no matter what, it's like I have to be unhappy to be happy."
    n 5x "It's making my head hurt."
    y 3t "That must make it...really difficult to feel comfortable with yourself."
    y "Being made to feel like you're wrong just for being the person you are."
    n 5u "..."
    n "It really...goes against everything I believe in, doesn't it?"
    n "It goes against the kind of person I want to be."
    n 12c "I'm fed up with it."
    n "I'm fed up with a lot of things."
    "Natsuki presses her palms into her forehead and shakes her head."
    n 12a "I know what's best for me, but I keep convincing myself out of it."
    n 12b "It's so much easier to be comfortably unhappy than it is to do something so scary."
    y 1e "To do what?"
    n 12a "You know..."
    n "To end it."
    y 3f "...With them?"
    "Natsuki nods."
    y 3i "I didn't think you were actively considering that as an option."
    n 5q "I wasn't, until recently."
    n "It's just one of those things where, like..."
    n 4c "It's been a certain way for so long that you just get used to it."
    n 5c "Like...so much of you has gone into it. So much that it feels like that's just how your life is."
    S y 3l t22
    n 5q "And throwing it away is like throwing away such a big part of your life."
    n 5u "It makes me feel sick to think about."
    "Natsuki sighs."
    n "It's...just really scary. It's terrifying."
    y 2t "What are you scared of?"
    n "I don't know...a lot of things."
    n "Like being alone."
    n "Not having anyone to talk to or hang out with."
    n "Not being able to replace what I have with them."
    n "And I don't want them to hate me."
    n "And I'm scared they'll hurt me for going against them."
    y 3t "Physically?"
    n 1h "Not physically!"
    n 1q "But..."
    "Yuri clenches her fists."
    y 3l "Natsuki."
    n 1h "What?"
    y "If anyone even thinks to cause you harm..."
    $ pause(2)
    y 3h "...I will unleash hell upon them."
    S n 5z t21
    "Natsuki snorts in laughter."
    y 3n "Don't laugh at me!"
    n "Ahaha. Sorry, I was just--"
    n 5t "I liked that."
    n "That's all."
    y 3g "Oh..."
    y "Well, I meant it."
    n 3j "I know you did."
    "Natsuki gives Yuri an endearing look."
    n "I needed it."
    y 4b "Mm..."
    "As the conversation lapses, Natsuki again slides her box of cupcakes over to Yuri."
    n 3c "Just take them, okay?"
    n 3q "I don't...I don't want other people to have them anymore."
    y 3t "...Are you sure?"
    "Natsuki nods."
    n "I'm sure."
    y 1m "I will, then."
    y "I'll enjoy them."
    H n
    H y
    "Natsuki looks away, but a feeling of warmth spreads through her."
    "She holds onto that feeling, knowing it will give her courage."
    stop music fadeout 2.0
    scene black with Dissolve(2)
    $ pause(1)

    jump ny5

label ny5:
    scene bg pstairwell with Dissolve(2)
    $ show_content_warning("Dialogue depictions of emotional distress, anxiety, panic attacks, and fear of rejection. Features a character's self-harm ideation of desiring to hit one's own head, and descriptions of the physiological symptoms of a panic attack, including rapid breathing and sobbing.")
    play music p1
    S y 1a f22
    y "Ah, you're here first today."
    S n 3s f21
    n "Mhm."
    y "And you brought reading material."
    n "Mhm."
    H n
    H y
    "Natsuki is sitting in her usual spot, this time holding a volume of manga while her lunch sits beside her."
    "Yuri sits down as well and opens her own book."
    S n 3q f21
    n "It sucks when a good series has to come to an end."
    n "Like it's such a big part of your life, and then one day there's just nothing left."
    n "It makes you feel so empty."
    S y 1h f22
    y "Unfortunately, I'm about to experience that myself. I'm on the last book of this series."
    n 3c "That sucks."
    y 2i "But...there's also something satisfying about letting a story conclude. I don't know if I'd want it to go on forever."
    n 5q "Maybe."
    n "But there are some things that I wish could."
    y 2f "On the other hand, have you ever read something that overstayed its welcome?"
    n 5t "Yeah, definitely."
    n 4t "I can think of at least one thing I've read that got pretty unbearable like halfway through, and the ending really sucked."
    n 5r "So...it sucks when something good has to end, but it also sucks when they just keep inventing more plot until you don't like it anymore."
    n "I guess it sucks either way."
    y 2l "Mhm."
    y "Well, that's the nature of all things. They come to an end."
    H n
    H y
    "The two fall silent."
    "They slowly eat while making their way through their respective reading material."
    "Except Natsuki doesn't seem to be touching her food at all."
    S n 3k f21
    n "...You don't go out during the weekends, right?"
    S y 1h f22
    y "...Excuse me?"
    n "Like, with friends. At the mall, or downtown, or whatever."
    y 1k "I'm not a total shut-in, you know."
    n 3t "Oh...my bad for making assumptions."
    y 2f "Well...I'm sure I go out less often than other people. Like you, and the others in the club."
    y 2j "I don't really meet with friends and arbitrarily spend time like that."
    y "I'm usually meeting with my board game group."
    n 5c "Board game group...?"
    y 3q "It...doesn't matter. It's just more nerdy stuff."
    y 3f "Why do you ask, anyway?"
    n 1t "I was just curious! I just realized that I couldn't picture it, so...I was just curious."
    play music p7a fadeout 2.0
    "Yuri looks at Natsuki and realizes that she's shaking."
    n 4u "Don't look at me like that."
    y 4b "Sorry..."
    "Natsuki pulls her knees into her chest and puts her head down."
    n 12d "I can't take this."
    y 3n "Did I...do something?"
    "Yuri gets flustered, her mind racing over what she may have said or done."
    n "I did."
    n "I ended it."
    n "I texted them earlier, telling them."
    n "And then I just blocked them because I'm so afraid of their responses."
    n "And now it feels like I'm dying inside."
    y 3t "Oh..."
    y "That's..."
    $ pause(2)
    y 3v "...I'm sorry."
    scene black with Dissolve(1)
    "Totally unsure of what to do, Yuri can barely find any words of support to offer."
    "Meanwhile, the sound of Natsuki's unusually hard breathing fills the air."
    "Then, she speaks again, barely above a whisper."
    play music p7c fadeout 2.0
    n "...Help me."
    n "I feel sick and I want to hit my head against things."
    n "Please help. I can't take this."
    y "--You may be having a panic attack."
    "With that realization, Yuri's demeanor suddenly changes."
    y "I--I have experience with this. So I'll help you through it. Okay?"
    "Natsuki meekly nods through her rapid breath, head still buried in her knees."
    "Yuri slides herself over to Natsuki and sits on the step behind her."
    "Then, she puts her hands on Natsuki's shoulders."
    y "Can you feel my hands?"
    "Natsuki nods. Her shaking becomes much more apparent through Yuri's sense of touch."
    "Yuri keeps her voice low and gentle."
    y "You're safe right now. You're in a good and safe place, where nothing can hurt you."
    "Natsuki nods once more. Although Yuri is only touching Natsuki's shoulders, she can practically feel her racing pulse through the base of her neck."
    y "We'll do a breathing exercise together. All you have to do is listen to my breaths and breathe along with me."
    y "Let's breathe in now."
    "Yuri takes a deep, slow breath."
    "Beneath her hands, she feels Natsuki's shoulders rise as Natsuki takes a breath of her own, trying to mimic Yuri."
    "They exhale together, although Natsuki's breath shakes on the way out."
    y "That's good. Let's keep going."
    "Yuri breathes in once more, and Natsuki joins her."
    "They continue like that for a few more cycles while Yuri closely monitors."
    "Eventually, Yuri feels Natsuki rest more of her weight into Yuri's palms."
    y "Let's focus on the physical world."
    y "All you have to do is focus on the feeling of your breaths going in and out."
    y "And the weight of my hands on your shoulders."
    y "You're in a safe and comfortable physical space."
    scene black
    $ pause(2)
    scene bg pstairwell with Dissolve(2)
    "Minutes pass in silence."
    "By now, the worst of it has passed, but Yuri is determined not to move away until Natsuki prompts her to."
    "Meanwhile, Natsuki has lifted her head off her knees, and her breathing has mostly steadied."
    "Then, she takes a final deep breath and slowly pulls herself to her feet, causing Yuri to let go."
    "She stretches her arms."
    S n 12a f21
    n "I'm sorry. I didn't mean to freak out."
    n "I don't know what my deal is."
    S y 3t f22
    y "You don't have to apologize."
    y "This must be enormously stressful for you."
    n "Is that going to keep happening?"
    y 3h "It...it may, or it may not."
    y 3i "We can take measures to help prevent it in the future. But I think it will naturally get better over time."
    H n
    H y
    "Natsuki motions to sit back down again, so Yuri moves over."
    "Yuri turns away to pick up her open book from the dusty floor, which she had hastily set down earlier. She brushes the dust off the cover."
    S n 12b f21
    n "I...don't think I could have gotten through that alone."
    $ pause(2)
    S y 4b f22
    y "...You're not alone."
    "Feeling shy again, Yuri speaks into her own lap."
    $ pause(2)
    y "From now on."
    y "You don't have to do anything alone."
    scene black with Dissolve(2)
    "As she says that, Yuri tenses up."
    "It's rare for her to so openly share her thoughts."
    "But something about Natsuki--of all people--makes it feel so much more natural to do so."
    "Perhaps because like Yuri, Natsuki is so timid and uncertain of herself."
    "Natsuki does such a good job at hiding it that it's taken a long time for Yuri to finally realize it."
    "And because of that, Yuri is able to deliver the reassurance that she herself would have wanted."
    "Demonstrating that you deserve the love of others."
    "If you can accept that for the first time, then perhaps you can begin the tumultuous journey of learning to love yourself."
    $ unlock("bgm_hugenergy")
    play music p9 fadeout 2.0
    $ unlock("ny_exclusive")
    scene ny_base
    show ny_y5 zorder 2:
        alpha 1
    show ny_y6 zorder 3:
        alpha 1
    with Dissolve(2.0)
    $ pause(2)
    show ny_n1:
        alpha 0
        linear 0.5 alpha 1
    n "Do you really mean that?"
    n "You're probably gonna regret saying that, if you do."
    show ny_y5:
        alpha 1
        linear 0.5 alpha 0
    y "How so?"
    show ny_n2:
        alpha 0
        linear 0.5 alpha 1
    show ny_n5:
        alpha 0
        linear 0.5 alpha 1
    show ny_n1:
        alpha 1
        linear 0.5 alpha 0
    n "Because."
    n "I'm probably gonna have a lot of free time during the weekends, from now on."
    n "So you're giving me permission to be as annoying as I want and drag you around to a lot of places."
    y "I see."
    show ny_n6:
        alpha 0
        linear 0.5 alpha 1
    show ny_n5:
        alpha 1
        linear 0.5 alpha 0
    n "But you already said it, so you can't take it back now."
    show ny_y6:
        alpha 1
        linear 0.5 alpha 0
    show ny_y2:
        alpha 0
        linear 0.5 alpha 1
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    y "Ah..."
    y "Well, I suppose I have no choice but to accept that responsibility, then."
    show ny_n2:
        alpha 1
        linear 0.5 alpha 0
    n "Mhm."
    $ pause(2)
    show ny_n2:
        alpha 0
        linear 0.5 alpha 1
    show ny_n7:
        alpha 0
        linear 0.5 alpha 1
    show ny_n6:
        alpha 1
        linear 0.5 alpha 0
    n "I know a good ice cream place."
    show ny_y4:
        alpha 1
        linear 0.5 alpha 0
    y "Oh?"
    y "That means you'll finally figure out my favorite ice cream flavor."
    n "Huh?"
    n "What are you talking about?"
    show ny_y3:
        alpha 0
        linear 0.5 alpha 1
    show ny_y2:
        alpha 1
        linear 0.5 alpha 0
    y "Oh, you don't remember?"
    y "The first day that you came to the club...you guessed everyone's favorite ice cream flavor, but for me you said you had no idea."
    n "Seriously?"
    n "I don't remember that at all."
    show ny_n7:
        alpha 1
        linear 0.5 alpha 0
    show ny_n5:
        alpha 0
        linear 0.5 alpha 1
    n "...Oh wait, yes I do. I said it was probably green tea."
    show ny_y3:
        alpha 1
        linear 0.5 alpha 0
    show ny_y2:
        alpha 0
        linear 0.5 alpha 1
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    "Yuri shakes her head."
    y "It's a good guess, but my favorite is usually to get chocolate and raspberry together."
    show ny_n5:
        alpha 1
        linear 0.5 alpha 0
    show ny_n2:
        alpha 1
        linear 0.5 alpha 0
    show ny_n3:
        alpha 0
        linear 0.5 alpha 1
    n "Chocolate and raspberry?"
    n "How fancy."
    show ny_y4:
        alpha 1
        linear 0.5 alpha 0
    y "How is that fancy?"
    n "Oh, I dunno."
    n "I feel like I should have guessed something like that."
    show ny_y2:
        alpha 1
        linear 0.5 alpha 0
    show ny_y3:
        alpha 0
        linear 0.5 alpha 1
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    show ny_y6 zorder 3:
        alpha 0
        linear 0.5 alpha 1
    y "Well..."
    y "Maybe next time I'll try chocolate and strawberry."
    show ny_n7:
        alpha 0
        linear 0.5 alpha 1
    n "Hey, strawberry is my favorite!"
    show ny_y4:
        alpha 1
        linear 0.5 alpha 0
    show ny_y3:
        alpha 1
        linear 0.5 alpha 0
    show ny_y2:
        alpha 0
        linear 0.5 alpha 1
    y "Hmm."
    y "What a coincidence."
    $ pause(2)
    show ny_n7:
        alpha 1
        linear 0.5 alpha 0
    show ny_n5:
        alpha 0
        linear 0.5 alpha 1
    n "I think...it helps to have something to look forward to."
    show ny_n3:
        alpha 1
        linear 0.5 alpha 0
    n "I still have the sick feeling in my stomach."
    n "But it's easier now to convince myself that I did the right thing."
    show ny_y6:
        alpha 1
        linear 0.5 alpha 0
    show ny_y2:
        alpha 1
        linear 0.5 alpha 0
    y "Is there anything better I could be doing?"
    show ny_n5:
        alpha 1
        linear 0.5 alpha 0
    show ny_n4:
        alpha 0
        linear 0.5 alpha 1
    show ny_n1:
        alpha 0
        linear 0.5 alpha 1
    n "Not that I know of."
    n "There's nothing that will make this easy for me."
    n "And you already did more than I thought anyone could."
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    show ny_y6 zorder 3:
        alpha 0
        linear 0.5 alpha 1
    y "Mm..."
    show ny_n4:
        alpha 1
        linear 0.5 alpha 0
    show ny_n5:
        alpha 0
        linear 0.5 alpha 1
    n "Come to think of it, we never talked about the letter you wrote..."
    n "But I feel like we're way past that at this point...I don't even know what to talk about."
    show ny_n5:
        alpha 1
        linear 0.5 alpha 0
    show ny_n6:
        alpha 0
        linear 0.5 alpha 1
    n "Except that I think it...helped me understand my needs a little bit better."
    n "The way I like to be treated."
    n "And the kinds of friends that I want to have."
    show ny_n1:
        alpha 1
        linear 0.5 alpha 0
    n "That's why I wanted to start coming here in the first place. Even though I was so scared of causing more problems."
    show ny_y6:
        alpha 1
        linear 0.5 alpha 0
    show ny_y4:
        alpha 1
        linear 0.5 alpha 0
    show ny_y3:
        alpha 0
        linear 0.5 alpha 1
    y "I thought...I thought it was a coincidence that you ran into me here initially?"
    show ny_n6:
        alpha 1
        linear 0.5 alpha 0
    show ny_n5:
        alpha 0
        linear 0.5 alpha 1
    show ny_n3:
        alpha 0
        linear 0.5 alpha 1
    n "Oh--Ah--"
    n "Well, not...exactly..."
    y "What do you mean?"
    n "Nothing."
    $ pause(2)
    show ny_n5:
        alpha 1
        linear 0.5 alpha 0
    show ny_n3:
        alpha 1
        linear 0.5 alpha 0
    show ny_n6:
        alpha 0
        linear 0.5 alpha 1
    show ny_n2:
        alpha 0
        linear 0.5 alpha 1
    n "I...I may have tracked you down first."
    n "With the help of Sayori."
    show ny_y3:
        alpha 1
        linear 0.5 alpha 0
    show ny_y1:
        alpha 0
        linear 0.5 alpha 1
    y "That's--"
    y "But you said--"
    show ny_n6:
        alpha 1
        linear 0.5 alpha 0
    show ny_n2:
        alpha 1
        linear 0.5 alpha 0
    show ny_n4:
        alpha 0
        linear 0.5 alpha 1
    show ny_n1:
        alpha 0
        linear 0.5 alpha 1
    n "I was shy, okay?"
    n "I wasn't ready to like..."
    n "...Whatever, you know what I'm saying."
    show ny_y1:
        alpha 1
        linear 0.5 alpha 0
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    show ny_y6 zorder 3:
        alpha 0
        linear 0.5 alpha 1
    y "Well..."
    y "I guess...I'm glad that you worked up the courage."
    y "Even if it was in your own way."
    show ny_y6:
        alpha 1
        linear 0.5 alpha 0
    show ny_y4:
        alpha 1
        linear 0.5 alpha 0
    y "I can tell that you've been making a lot of difficult decisions."
    y "It's brave. And it will make things better in the long run."
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    show ny_y2:
        alpha 0
        linear 0.5 alpha 1
    y "I think anyone would be proud of you for it."
    show ny_n1:
        alpha 1
        linear 0.5 alpha 0
    show ny_n4:
        alpha 1
        linear 0.5 alpha 0
    show ny_n2:
        alpha 0
        linear 0.5 alpha 1
    show ny_n7:
        alpha 0
        linear 0.5 alpha 1
    n "Anyone?"
    $ pause(2)
    n "...You mean, like you?"
    $ pause(2)
    show ny_y4:
        alpha 1
        linear 0.5 alpha 0
    show ny_y2:
        alpha 1
        linear 0.5 alpha 0
    show ny_y5:
        alpha 0
        linear 0.5 alpha 1
    show ny_y6 zorder 3:
        alpha 0
        linear 0.5 alpha 1
    y "...Yes."
    y "Like me."
    $ pause(2)
    show ny_n2:
        alpha 1
        linear 0.5 alpha 0
    show ny_n7:
        alpha 1
        linear 0.5 alpha 0
    show ny_n3:
        alpha 0
        linear 0.5 alpha 1
    show ny_n4:
        alpha 0
        linear 0.5 alpha 1
    n "You know, I could get used to this."
    show ny_y5:
        alpha 1
        linear 0.5 alpha 0
    show ny_y3:
        alpha 0
        linear 0.5 alpha 1
    y "As long as...as long as you don't tease me too much."
    n "Fine."
    n "Just a little, then."
    $ pause(2)
    show ny_y4:
        alpha 0
        linear 0.5 alpha 1
    y "That's fine."
    $ pause(2)
    show ny_y6:
        alpha 1
        linear 0.5 alpha 0
    y "I know how uncertain everything feels to you right now..."
    show ny_y3:
        alpha 1
        linear 0.5 alpha 0
    show ny_y2:
        alpha 0
        linear 0.5 alpha 1
    y "...But I really do think that good things are in store. Those are my honest feelings."
    show ny_n4:
        alpha 1
        linear 0.5 alpha 0
    show ny_n6:
        alpha 0
        linear 0.5 alpha 1
    n "Thanks."
    n "It feels nice to be reassured."
    scene black with Dissolve(2)
    "The two girls continue their conversation through the remainder of lunch."
    "But a new feeling hangs in the air--a feeling of greater certainty in their path forward."
    "In just a few hours, there will be another Literature Club meeting, where the four club members will happily spend time together."
    "Each of them, all with their own special qualities, have something unique that they can deliver to one another."
    "Through friendship and literature, the club members will continue to grow and find new happiness together."
    "The end of each chapter is the start of the next."
    "Yuri thinks to herself."
    "Since she's about to finish her long-running series, it would be best to have a new book lined up."
    "Perhaps this weekend would be a good time to visit the bookstore."
    $ pause(2)
    "Together."
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    $ unlock("sidestory6")
    $ plus_persistent.side_stories_read[5] = True
    jump desktop_from_side_stories
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

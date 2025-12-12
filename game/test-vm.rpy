




init python:
    def create_glitch_text(text_length, available_glyphs):
        glitch = ""
        for i in range(text_length):
            if random.randint(0, 9) > 4:
                glitch += random.choice(available_glyphs)
            else:
                glitch += " "
        return glitch


default line_length = 60

default characters_per_second = 60

default dot_delay = 0.3

default glyphs = "ÇüéâäàåçêëèïîìÄÅæÆôöòûùÿÖÜ¢£¥₧ƒáíóúñÑªº¿⌐¬½¼¡«»┤╡╢╖╕╣║╗╜╝╜╛┐└┴┬├─┼╞╟╚╔╩╦╠═╬╧╨╤╥╙╘╒╓╫╪┘┌▌▐┌αßΓπΣσµτΦΘΩδ∞φε∩≡±≥≤⌠⌡"
default cursor = "█"

default quotes_array = [
    "circular, with the focal point in the center.",
    "ventilation ducts in the basement. Also needed are airtight containers which can serve as both storage and dispensary of the ether.",
    "indicates only 80% or less of nutrients and medical supplements are needed to keep the body alive, compared to the non-amputated control.",
    "material resistant to Third Eye penetration. Electromagnetic",
    "are speculated to improve Third Eye potency by puberty. The new",
    "meditation of some sort. We do not",
    "outer and inner cylindrical shells' openings on opposite sides, such that they will rotate to create an entrance.",
    "meters in diameter, so that a 0.5-meter gap between each body will",
    "during birth, or the full trimester? The effects",
    "who don't have a Third Eye struggle to understand what current science cannot tell them. I am disregarding",
    "name implies death, but of what? Only the material self. Our mission to become free of the material self is",
    "of the Nexus extends beyond any comprehension of the material world.",
    "The only prison is our material world. The gate",
    "They speak to me. They instructed me to",
    "emotional impulse over rationality. By the",
    "of which disassociation is a symptom. Conditioning",
    "all have functional reproductive systems, then we could produce new, potent children with incredible efficiency, and sudden death would be a less",
    "tests focusing on each of these emotional responses to determine which",
    "All your base are belong to us.",
    "gradual changes to the Scripture class curriculum to incorporate",
    "By age five, children testing above the threshold will be transferred to Wing A, while all",
    "Male and infertile children can still be trained for specialized",
    "list of which rooms will need doors and windows renovated to accommodate the projected increase in",
    "nutrition? During child development,",
    "but my Third Eye shows me two of them. I can't make sense of",
    "will ascend and bring salvation to all. May the Third Eye",
    "two Guardian Angels, condemned to blindness, who seek a guiding light in their eternal prison.",
    "should seek purpose. Purpose ignites a will to live, a will to suffer for",
    "beyond the eyes of the public. Decades of favorable reputation",
    "are my children. The opportunity",
    "The key to opening a powerful channel lies in eroding the tether between",
    "have died so that those most worthy will be able to ascend.",
    "voltage is appropriate for immobilization without risking permanent damage.",
    "absolute genius and has made incredible contributions to Project Libitina, despite having no Third",
    "have given him the title 'Guardian' to reflect",
    "Emotions are the dials and switches that override rational thought and can be fine-tuned to exert a great deal of control upon",
    "At nine months each, a total of thirty-six would reach peak efficiency, with about one week per",
    "has become an increasingly scientific endeavor thanks to",
    "may actually produce tiny, but detectable, physical distortions in the area surrounding them. We might consider",
    "adulthood to receive professional training in",
    "number of specialized professions we will need to staff, such as additional nurses and reproductive",
    "Eye is open and measure any notable difference in response to danger, pain, food, and sexual stimulus.",
    "Opening the Third Eye creates a deep-brain channel which causes sentient characteristics such as consciousness and free thought to",
    "Love for us, the collective, triumphs over love for the individual. So a degree of sacrifice",
    "is far stronger during collective sessions, which makes me believe the Nexus will have incredible",
    "Is the increased potency from proximity to others a temporary effect, or does it have a lasting impact on the strength of their Third Eye?",
    "I lied. It's actually hot.",
    "children are generally obedient, but with the introduction of more unpleasant activities we should consider",
    "sourcing our medication. If they are also able to supply",
    "can only assume that even obstacles or failures are all a part of the great plan, even if beyond my comprehension.",
    "an Angel in mortal skin. She will walk the path to Ascension, and we will follow.",
    "The observable changes in physical appearance, however small, already prove this to be more than the usual spiritual nonsense.",
    "like dogs, genetically molded by humans and unconditionally loyal in exchange for food and shelter.",
    "distanced from the religion which the Academy was once known to practice. Religion requires faith; this is undeniable truth.",
    "insisted on upgrading the computer systems, going on about backups and protecting data. Nobody touches my personal \"data\".",
    "54,42,15         2:14"]

transform bios_top_right_center:
    anchor (0,0)
    pos (200,44)

label test_vm:


    play music bios_buzz

    show bios_layer at bios_glow_shader
    scene black onlayer bios


    $ bios_output = "Initializing..."
    show bios_output_text "[bios_output]" + _(cursor) onlayer bios at bios_top_right_center
    pause(0.5)
    $ bios_output += _("\nConnecting.")
    show bios_output_text "[bios_output]" + _(cursor)

    $ dot_step = 0
    $ dot_amount = renpy.random.randint(2, 8)
    while dot_step < dot_amount:
        pause(dot_delay)
        $ bios_output += "."
        show bios_output_text "[bios_output]" + _(cursor)
        $ dot_step += 1
    pause(dot_delay)
    $ bios_output += _(" Connected\n")
    show bios_output_text "[bios_output]" + _(cursor)
    pause(1.0)
    $ bios_output += _("Attempting to decode binary data...\n")
    show bios_output_text "[bios_output]" + _(cursor)
    pause(0.5)



    $ quote = quotes_array[renpy.random.randint(0, len(quotes_array) - 1)];

    $ glitch_text = create_glitch_text(renpy.random.randint(600, 900) - len(quote), glyphs)

    $ insert_location = random.randint(5, len(glitch_text) - 5)
    $ full_glitch_text = glitch_text[:insert_location] + quote + glitch_text[insert_location:]


    $ iterator = 0
    while iterator < len(full_glitch_text):

        if iterator < len(full_glitch_text) - 1:
            $ full_glitch_text = full_glitch_text[:iterator] + _("\n") + full_glitch_text[iterator:]

        $ iterator += line_length


    $ bios_output += "\n"
    $ iterator = 0
    while iterator < len(full_glitch_text):
        $ bios_output += full_glitch_text[iterator]


        if renpy.random.randint(0, 10) < 3:
            show bios_output_text "[bios_output]" + _(cursor)
            if renpy.random.randint(0, 40) < 2:
                pause(1.0)
            else:
                pause(1.0 / renpy.random.randint(characters_per_second / 10.0, characters_per_second))
        $ iterator += 1

    show bios_output_text "[bios_output]" + _(cursor)
    pause(1.5)
    $ bios_output += _("\n\nConnection lost")
    show bios_output_text "[bios_output]" + _(cursor)

    call screen test_vm_wait_for_click

screen test_vm_wait_for_click:
    modal True

    dismiss action [Hide(), Jump("return_from_test_vm")]
    frame:
        area (0,0,1.0,1.0)
        background Solid("#00000000")

label return_from_test_vm:
    hide bios_layer
    stop music
    $ desktop_window_animation_multi = 1
    jump desktop_from_side_stories
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

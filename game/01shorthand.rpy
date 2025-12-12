




















python early:
    import re

    def shorthand_parse_show(lexer):
        
        
        text = lexer.rest().split()
        if len(text) != 3:
            return None
        who = text[0]
        expression = text[1]
        trans = text[2]
        return (who, expression, trans)

    def shorthand_execute_show(parsed):
        (who, expression, trans) = parsed
        character = eval(who)
        
        zorder = 3 if re.fullmatch(r'f[0-4][0-4]', trans[0]) else 2
        name = character.image_tag
        renpy.show(f'{name} {expression}', at_list=[eval(trans)], zorder=zorder)
        return

    def shorthand_predict_show(parsed):
        return [renpy.get_registered_image(f'{who} {expression}')]

    def shorthand_lint_show(parsed):
        if parsed == None:
            renpy.error("Incorrectly-formatted shorthand statement.")
            return
        (who, expression, trans) = parsed
        if type(getattr(store, who, None)) != renpy.character.ADVCharacter:
            renpy.error(f"Invalid character: {who}")
        return

    def shorthand_parse_hide(lexer):
        text = lexer.rest().split()
        if len(text) != 1:
            return None
        return text[0]

    def shorthand_execute_hide(parsed):
        who = parsed
        character = eval(who)
        name = character.image_tag
        renpy.show(name, at_list=[thide], zorder=1)
        renpy.hide(name)
        return

    def shorthand_lint_hide(parsed):
        if parsed == None:
            renpy.error("Incorrectly-formatted shorthand statement.")
            return
        who = parsed
        if type(getattr(store, who, None)) != renpy.character.ADVCharacter:
            renpy.error(f"Invalid character: {who}")
        return

    renpy.register_statement(
    name='S',
    parse=shorthand_parse_show,
    execute=shorthand_execute_show,
    predict=shorthand_predict_show,
    lint=shorthand_lint_show
)
    renpy.register_statement(
    name='H',
    parse=shorthand_parse_hide,
    execute=shorthand_execute_hide,
    lint=shorthand_lint_hide
)
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

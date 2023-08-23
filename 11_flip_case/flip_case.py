def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    phrase = phrase.replace(to_swap, "*")
    if to_swap.islower():
        phrase = phrase.replace(to_swap.upper(), to_swap)
        phrase = phrase.replace("*", to_swap.upper())
    else:
        phrase = phrase.replace(to_swap.casefold(), to_swap.upper())
        phrase = phrase.replace("*", to_swap.casefold())

    return phrase
    

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    formatted_phrase = phrase.casefold().replace(" ", "")
    phrase_list = list(formatted_phrase)
    reversed_phrase_list = phrase_list.copy()
    reversed_phrase_list.reverse()
    return phrase_list == reversed_phrase_list


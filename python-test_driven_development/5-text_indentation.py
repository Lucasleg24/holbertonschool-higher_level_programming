#!/usr/bin/python3

"""
contain the function
"""


def text_indentation(text):

    """
    function for add indentation
    text: contain the string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text.strip() == "":
        return
    punctuation = {'.', '?', ':'}
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in punctuation:
            result += '\n\n'
        i += 1
    print(result.strip())

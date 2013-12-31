# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def gruppercase(value):
    """Correctly uppercases all Gr characters in a string"""

    grletters = [u'α', u'β', u'γ', u'δ', u'ε', u'ζ', u'η', u'θ', u'ι', u'κ', u'λ', u'μ', u'ν', u'ξ', u'ο', u'π', u'ρ', u'σ', u'τ', u'υ', u'φ', u'χ', u'ψ', u'ω']
    grletters_accent = [u'ά', u'έ', u'ή', u'ί', u'ό', u'ύ', u'ώ']
    grletters_upper_accent = [u'Ά', u'Έ', u'Ή', u'Ί', u'Ό', u'Ύ', u'Ώ']
    grletters_upper_solvents = [u'ϊ', u'ϋ']
    grletters_other = [u'ς']

    grletters_to_uppercase = [u'Α', u'Β', u'Γ', u'Δ', u'Ε', u'Ζ', u'Η', u'Θ', u'Ι', u'Κ', u'Λ', u'Μ', u'Ν', u'Ξ', u'Ο', u'Π', u'Ρ', u'Σ', u'Τ', u'Υ', u'Φ', u'Χ', u'Ψ', u'Ω']
    grletters_accent_to_uppercase = [u'Α', u'Ε', u'Η', u'Ι', u'Ο', u'Υ', u'Ω']
    grletters_upper_accent_to_uppercase = [u'Α', u'Ε', u'Η', u'Ι', u'Ο', u'Υ', u'Ω']
    grletters_upper_solvents_to_uppercase = [u'Ι', u'Υ']
    grletters_other_to_uppercase = [u'Σ']

    grlowercase = grletters + grletters_accent + grletters_upper_accent + grletters_upper_solvents + grletters_other
    gruppercase = grletters_to_uppercase + grletters_accent_to_uppercase + grletters_upper_accent_to_uppercase + grletters_upper_solvents_to_uppercase + grletters_other_to_uppercase
    grkeys = dict(zip(grlowercase, gruppercase))

    import re
    pattern = "|".join(grkeys.keys())
    return re.sub(pattern, lambda m: grkeys[m.group()], value.upper())
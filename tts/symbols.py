""" from https://github.com/keithito/tacotron """

_pad        = '_'
#_punctuation = '!\'(),.:;? '
_punctuation = '!",.:;? '
_special = '-'
#_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters)

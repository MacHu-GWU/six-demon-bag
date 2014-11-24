##encoding=utf8

import pyperclip

text = 'yes'
pyperclip.copy(text) # only support ascii code
print pyperclip.paste() # copy something in clipboard
#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword.
#        mcb.pyw <keyword> - Loads keyword to clipboard.
#        mcb.pyw list - Lods ll keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: Save clipboard content.

#TODO: List keywords and load content.

mcbShelf.close()
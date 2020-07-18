# Hope I'm doing this right. 
# Here's a dumb little piece of code I made that allows you to play a sound in Jupyter Notebook any time your cell returns an error.


from IPython.display import Audio , display

def play_sound(self, etype, value, tb, tb_offset=None):
    
    self.showtraceback((etype, value, tb), tb_offset=tb_offset)
    display(Audio("PATH/TO/FILE.mp3", autoplay=True))
    
get_ipython().set_custom_exc((Exception,), play_sound)


# If you want to play the sound from a URL you can change display(Audio("PATH/TO/FILE.mp3", autoplay=True)) to:
#   display(Audio(url = "URL", autoplay=True))

# I'm using Exception to play a sound on ANY error..you can be more specific, ZeroDivisionError, TypeError, etc.

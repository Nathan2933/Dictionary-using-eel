import eel
import json
from difflib import get_close_matches
from tkinter import messagebox
eel.init('web')
@eel.expose
def meanin(theword):
   data=json.load(open("data.json"))
   word=theword
   word=word.lower()
   if word in data:
      meaning=data[word]
      for item in meaning:
         eel.addText(u'\u2022'+item+'\n')
   elif len(get_close_matches(word,data.keys()))>0:
      close_match=get_close_matches(word,data.keys())[0]
      eel.alerting(close_match)
   else:
      eel.wde("The word doesn't exist.Please verify.")
@eel.expose
def meaning2(word2):
   data=json.load(open("data.json"))
   word=word2.lower()
   meaning=data[word]
   for item in meaning:
      eel.addText(u'\u2022'+item+'\n')
eel.start('index.html',size=(810,523))

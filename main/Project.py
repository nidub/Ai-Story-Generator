from transformers import pipeline
import re

#get_ipython().events.register('pre_run_cell', set_css)
def func (e,g):
  story_generator1 = pipeline("text-generation", "pranavpsv/gpt2-genre-story-generator")
  
  stringToPass="<BOS>"+g+e
  #print(stringToPass)
  #story = story_generator1("<BOS> <superhero> Batman", max_length= 200) 
  story = story_generator1(stringToPass, max_length= 400) 
  #print(story[0]["generated_text"])

  mod_story=story[0]["generated_text"]
  #mod_story='<BOS> <superhero> Batman: "The Killing Joke" Part 1 Batman and Robin try a daring crime of which Wayne has been unable to take credit. The Joker kidnaps his mother, Madame Penelope, and forces Robin to flee to a tower in Manhattan called the White House. However, Batman fights a pack of murderous, bat-like zombies. One of them is the Joker and escapes with a special gas that can generate electricity, and Batman and Robin use it to burn up the tower. It burns Gotham and eventually kills several million people, including the Presidents family.In an alternate timeline, Robin runs into the Joker and finds him at the White House. As Batman and Robin enter the building, Joker attacks, Batman disarms him and saves the White House. However, he escapes and tells the Joker about his plan to eliminate Batman.The Joker then takes Batman, Robin and several other villains on a truck ride into the White House. Batman and Robin have an argument. Afterwards, a large'
  x=re.search("[<].*[>]",mod_story)
  #print(x.group())

  mod_story=mod_story.replace(x.group(),'')

  #print(mod_story)
  return(mod_story)

# [<].*[>]
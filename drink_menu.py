def drink_menu(person):
  """Asks the pirate what their taste preferences are and maps them to a drink selection"""
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
  }
preferences= {}
for flavor in questions:
  invalid_input = False
  value = flavor
  while invalid_input == False:
    flavor = raw_input(questions[flavor]+ ", answer Yes or No: ")
    if flavor == "Yes" or flavor == "No":
      if flavor == "No":
        preferences[value] = False
      else:
        preferences[value] = True
      invalid_input = True
    else:
      print "You entered an invalid response, please try again."

      
def drink_maker(preferences):
  import random
  """Asks the pirate what their taste preferences are and maps them to a drink selection"""
  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
  }
  ing_li =[]
  for flavor in preferences:
    if preferences[flavor] == True:
      choice = ingredients[flavor]
      selection = random.choice(choice)
      ing_li.append(selection)
  return ing_li
if __name__ == '__main__':
    drink_menu("James")
    drink_maker(preferences)

  
  
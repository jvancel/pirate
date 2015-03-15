def drink_menu(person):
  """Asks the pirate what their taste preferences are and maps them to a drink selection"""
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
  }
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
  }
flav_li_bool = []
for flavor in questions:
  invalid_input = False
  while invalid_input == False:
    flavor = raw_input(questions[flavor]+ ", answer Yes or No: ")
    if flavor == "Yes" or flavor == "No":
      if flavor == "No":
        flav_li.append(False)
      else:
        flav_li.append(True)
      invalid_input = True
    else:
      print "You entered an invalid response, please try again."
print flav_li

    
  
  
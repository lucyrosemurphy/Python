import re

#User enters a password and the password viability is checked under several criteria

def passwordViability():
  
	while True:
    criteriaMet = 0
    
    print ('Enter a password')                              #Adds a label
		password = str(input('Password:'))                      #User Input for Password
    
		if 6 <= len(password) < 16:                             #Mandates password Length
		    criteriaMet += 1
    else:
		  print ('The password must be between 6 and 15 characters.')
      continue
      
    if re.search(r'[#$@]', password):
      criteriaMet += 1
    else:
      print ("How could you forget about the special characters, I mean after all they are special. Try adding at least one of these symbols to your password (@#$)")
      continue
      
    if re.search(r'[A-Z]', password):
      criteriaMet += 1
    else:
      print ("Every great password needs an at least one uppercase letter.")
      continue
      
    if re.search(r'[a-z]', password):
        criteriaMet += 1
    else:
      print ("Heyyy... dont forget about the little guys, every good password needs at least one lowercase letter")
      continue
        
    if re.search(r'[0-9]', password):
      criteriaMet += 1
    else:
      print ("don't neglect the top of your keyboard. Every good password needs at least one number (0-9).")
      continue
      
     if criteriaMet >= 5:
      print ("You did it, now that is a fantastic password!")
     else:
      print ("Hey, something seems to have gone wrong. Make sure you have met these criteria: \n" +
             "- Password must be between 6 and 15 characters long \n" +
             "- Don't forget your special characters (they are a bit narsasistic, hense their name, and don't like to be excluded)" +
             ". Special characters include: #$@ \n" +
             "- INCLUDE AT LEAST ONE CAPITAL LETTER \n" +
             "- include at least one lower case letter \n" +
             "- Dont neglet the top of your key board. Dont be shy, add a number 0-9 \n")
 
passwordViability()

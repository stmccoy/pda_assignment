### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    #need a colon after else
    else
      return False
   
#should be def not dif
#should have a comma between card1 and card2 
  dif highest_card(self, card1 card2):
  #needs indent for if
  if card1.value > card2.value:
    return card
#should be return card1, not card. 
  else:
    return card2
  

#needs to be indented 
def cards_total(self, cards):
  #total should be assigned a value. Probably 0 if you're adding up card total
  total
  for card in cards:
    total += card.value
    #cannot add a string to an int or float, so depending on how you defined total you'd have to convert it to a string. 
    #return statement would stop for loop on first cycle which could mess up test
    return "You have a total of" + total
  
```

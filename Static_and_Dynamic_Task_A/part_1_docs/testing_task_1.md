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
    if card.value = 1: # needs to be == 1
      return True
    else # colon needed after else
      return False
   

  dif highest_card(self, card1 card2): #dif should be def, comma missing between parameters: (self, card1, card2)
  if card1.value > card2.value:
    return card #should be return card1
  else:
    return card2
  


def cards_total(self, cards):
  total # should be set to 0
  for card in cards:
    total += card.value
    return "You have a total of" + total
  #return statement needs to be a formatted string:
    #return (f"You have a total of {total}")
```

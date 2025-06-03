There are a variety of parameters with which you can analyze cards. Parameters are specific with "-p" or "--parameter". Currently, only one parameter can be specified at a time.


### Syntax
- The typical syntax for a parameter looks "{attribute1}2{attribute2}". This indicates that 2 attributes are being ratio'd or examined relative to eachother
- Usually "attribute2" is the converted mana cost of a card
- For instance, the parameter "pow2cmc" computes the ratio of each card's power to it's convered mana cost, then sorts the given list of cards in descending order by that ratio
    - A 3/1 creature that costs 1 mana would  have a "pow2cmc" ratio of 3.0

### Parameters
Supported parameters are listed below
- pow2cmc: sorts cards by the highest power-to-converted mana cost-ratio
- tou2cmc: sorts cards by the highest toughness-to-converted mana cost-ratio
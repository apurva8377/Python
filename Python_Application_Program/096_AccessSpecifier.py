##################################################################################################################
#
#  Program Name : 096_AccessSpecifier.py
#  Discription  : All variables
#  Author       : Apurva Vilas Shinde
#  Date         : 17/05/2026
#
##################################################################################################################

class Demo:
    def __init__(self):
        self.No1 = 10         # public
        self._No2 = 20        # protected
        self.__No3 = 30       # private

obj = Demo()
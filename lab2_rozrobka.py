import random
e=''
while e!='q':

    class Card(object):
        def __init__(self):
            self.suit = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
            self.mydeck = []
            self.cardind = []
            for value in range(0, 52):
                r = str(value % 13)
                cost=int(r)
                if r == '11':
                    cost=r
                    r = 'V'
                if r == '12':
                    cost=r
                    r = 'Q'
                if r == '0':
                    cost=r
                    r = 'K'
                index = int((value / 13) % 13)
                self.mydeck.append((r, self.suit[index], cost))

        def shuffle(self):
            nextcard = self.mydeck.pop(random.randint(0, len(self.mydeck) - 1))
            return nextcard

        def deck(self):
            c = Card()
            for i in range(0, 52):
                self.cardind.append(c.shuffle())

        def view(self):
            print('Pyramid: ')
            print(60 * ' ', self.cardind[0])
            print(50 * ' ', self.cardind[1:3])
            print(40 * ' ', self.cardind[4:7])
            print(30 * ' ', self.cardind[7:11])
            print(20 * ' ', self.cardind[11:16])
            print(10 * ' ', self.cardind[16:22])
            print(self.cardind[23:30])
            print(' ')
            print(' ')
            print("Deck of help: ")
            print(self.cardind[30:])
    print(60*' ', 'Card game [Pyramid]: ')
    print(' ')
    c = Card()
    c.deck()
    c.view()

    e=str(input('Enter-restart, q+enter-exit'))
if e=='q':
    exit()

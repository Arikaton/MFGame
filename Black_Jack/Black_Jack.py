from random import shuffle

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_v(self):
        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)


class Hand(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_v(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_v()
            if card.get_rank() == "A":
                aces += 1

        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "%s's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand Value: " + str(self.get_v())
        return text


class Deck(object):
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r, s) for r in ranks for s in suits]
        shuffle(self.cards)

    def deal_cards(self):
        return self.cards.pop()


def new_game(money):
    d = Deck()
    player_hand = Hand('Player')
    dealer_hand = Hand('Dealer')
    player_hand.add_card(d.deal_cards())
    player_hand.add_card(d.deal_cards())
    dealer_hand.add_card(d.deal_cards())
    print(dealer_hand)
    print("="*20)
    print(player_hand)
    in_game = True
    while player_hand.get_v() < 21:
        ans = input("Hit or stand? (h/s) \n")
        if ans == 'h':
            player_hand.add_card(d.deal_cards())
            print(player_hand)
            if player_hand.get_v()>21:
                print("You Loose")
                money -=5
                in_game = False
                break
        elif ans=='s':
            print("You stand")
            break
        else:
            print("Error")
    print('='*20)
    if in_game:
        while dealer_hand.get_v() < 17:
            dealer_hand.add_card(d.deal_cards())
            print(dealer_hand)
            if dealer_hand.get_v() > 21:
                print("Dealer bust")
                money+=5
                in_game = False
    if in_game:
        if player_hand.get_v()>dealer_hand.get_v():
            print("You win")
            money+=5
        else:
            print("Dealer win")
            money-=5
    return money


if __name__ == '__main__':
    money = int(input())
    print("You have %d$" % money)
    while money>0:
        money = new_game(money)
        print("You have %d$\n" % money)
    print("\nYou spent all your money!")




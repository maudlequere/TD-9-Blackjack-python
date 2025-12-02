import random
#Variables globales

cash = 200
bet = 0
quit_game=False


#fonction init_cards => 52 cartes mélangées

def init_cards():
    lst_cards = ['As ♥','As ♦','As ♣','As ♠','2 ♥','2 ♦','2 ♣','2 ♠','3 ♥','3 ♦','3 ♣','3 ♠','4 ♥','4 ♦','4 ♣','4 ♠','5 ♥','5 ♦','5 ♣','5 ♠','6 ♥','6 ♦','6 ♣','6 ♠','7 ♥','7 ♦','7 ♣','7 ♠','8 ♥','8 ♦','8 ♣','8 ♠','9 ♥','9 ♦','9 ♣','9 ♠','10 ♥','10 ♦','10 ♣','10 ♠','Valet ♥','Valet ♦','Valet ♣','Valet ♠','Dame ♥','Dame ♦','Dame ♣','Dame ♠','Roi ♥','Roi ♦','Roi ♣','Roi ♠']
    random.shuffle(lst_cards)
    return lst_cards

# print(init_cards())

#fonction draw => retourne la première carte du paquet et lst_cards mis à jour

def draw(lst_cards):
    card = 0
    while card <1:
        # print(lst_cards[card])
        first_card=lst_cards[card]
        del lst_cards[card]
        card = 1
    return [first_card,lst_cards]

# print(draw(['4 ♦', '6 ♣', '4 ♥', 'Valet ♠', 'As ♥', '8 ♥', 'As ♣', '2 ♦', '5 ♣', 'Roi ♥', 'Dame ♦', '4 ♠', '9 ♠', '7 ♥', 'Valet ♥', 'As ♦', '6 ♦', '3 ♣', '7 ♣', 'Dame ♣', '8 ♠', '2 ♣', 'Dame ♥', '3 ♦', '4 ♣', '8 ♦', '5 ♥', '7 ♦', '6 ♠', '6 ♥', 'Dame ♠', '8 ♣', 'Roi ♣', '7 ♠', '3 ♥', '5 ♦', 'As ♠', '9 ♥', '3 ♠', '9 ♣', 'Roi ♠', '5 ♠', '9 ♦', 'Valet ♣', 'Valet ♦', '2 ♥', '2 ♠']))

#fonction get_value_cards => cumules valeurs cartes (prise en compte règles du jeu)
def get_value_cards(liste_cartes):

    somme = 0
    lst_ace =[]

    for e in liste_cartes:
        valeur_chiffre=['2 ♥','2 ♦','2 ♣','2 ♠','3 ♥','3 ♦','3 ♣','3 ♠','4 ♥','4 ♦','4 ♣','4 ♠','5 ♥','5 ♦','5 ♣','5 ♠','6 ♥','6 ♦','6 ♣','6 ♠','7 ♥','7 ♦','7 ♣','7 ♠','8 ♥','8 ♦','8 ♣','8 ♠','9 ♥','9 ♦','9 ♣','9 ♠','10 ♥','10 ♦','10 ♣','10 ♠']
        valeur_tete=['Valet ♥','Valet ♦','Valet ♣','Valet ♠','Dame ♥','Dame ♦','Dame ♣','Dame ♠','Roi ♥','Roi ♦','Roi ♣','Roi ♠']

        if e in valeur_chiffre:
            somme = somme + int(e[0])
        
        elif e in valeur_tete:
            somme = somme + 10  
        
        else :
            lst_ace.append(e)

    e = 0
    if len(lst_ace)!=0:
        while e < len(lst_ace) :
            e = e + 1 
            if somme <=10 :
                somme = somme + 11
            else :
                somme = somme + 1
            
    return somme

# print(get_value_cards(['2 ♣','2 ♠','3 ♥','3 ♦']))
# print(get_value_cards(['Valet ♥','Valet ♦','Valet ♣','Valet ♠','Dame ♥','Dame ♦']))
# print(get_value_cards(['2 ♣','2 ♠','3 ♥','As ♥']))
# print(get_value_cards(['As ♥','Valet ♥','Valet ♦']))
# print(get_value_cards(['Valet ♥','Valet ♦','As ♥']))

#fonction display_card => cartes ainsi que la valeur cumulée

def display_card(statut,lst_cards_player,value_player):
    espace =" "
    return f"{statut} {espace.join(lst_cards_player)} ({get_value_cards(lst_cards_player)})"

# print(display_card("Joueur",['2 ♣','2 ♠','3 ♥','As ♥'],['2 ♣','2 ♠','3 ♥','As ♥']))

#fonction to_bet => nombre de dollars restant maj en fonction de la mise et la mise

def to_bet(dollars_restant):

    mise = 0
    while mise > dollars_restant or mise <20:
        while True :
            try :
                mise = int(input("Entrez la valeur que vous souhaitez miser : \n"))
                break
            except ValueError:
                print("Oups la valeur n'est pas valide, entrez à nouveau une mise (en chiffres) :\n")
        
    dollars_restant = dollars_restant - mise
    
    return [dollars_restant,mise]

# print(to_bet(50))

#Jeu du blackjack

dollars_restant = 200
croupier = "Croupier"
joueur = "Joueur"

jouer = input("Voulez-vous jouer ? Répondre par oui ou non. \n")

while jouer.lower() != "oui" and jouer.lower() != "non" :
        jouer = input("Erreur, répondez par oui ou non. Voulez-vous jouer ? \n")


while dollars_restant >= 20 and jouer.lower()=="oui" :

    # Mise en jeu

    jeu = init_cards()
    mise = to_bet(dollars_restant)

    lst_card_dealer = []
    carte_pioche = draw(jeu)[0]
    lst_card_dealer.append(carte_pioche)
    value_dealer = get_value_cards(lst_card_dealer)
    print(f"{display_card(croupier,lst_card_dealer,value_dealer)}\n")


    winner_player = False

    # Tour du joueur

    lst_card_player = []
    carte_pioche = draw(jeu)[0]
    lst_card_player.append(carte_pioche)
    value_player = get_value_cards(lst_card_player)
    print(f"{display_card(joueur,lst_card_player,value_player)} \n")

    piocher = input("Voulez vous piocher une autre carte ? Répondre par oui ou non. \n")

    while piocher.lower() != "oui" and piocher.lower() != "non" :
           piocher = input("Voulez vous piocher une autre carte ? Répondre par oui ou non. \n")

    while piocher.lower() == "oui" :

        carte_pioche = draw(jeu)[0]
        lst_card_player.append(carte_pioche)
        value_player = get_value_cards(lst_card_player)
        
        if value_player > 21:
            break

        print(f"{display_card(joueur,lst_card_player,value_player)} \n")
        piocher = input("Voulez vous piocher une autre carte ? Répondre par oui ou non. \n")

    print(f"{display_card(croupier,lst_card_dealer,value_dealer)}\n")
    print(f"{display_card(joueur,lst_card_player,value_player)} \n")

    # Tour du croupier

    while value_dealer<value_player and value_player<=21 and value_dealer<21:
        carte_pioche = draw(jeu)[0]
        lst_card_dealer.append(carte_pioche)
        value_dealer = get_value_cards(lst_card_dealer)

    if value_dealer > 21:
            winner_player = True

    print(f"{display_card(croupier,lst_card_dealer,value_dealer)}\n")

    # Remise en jeu possible ?
    
    if winner_player == False and value_dealer != value_player:
        print("Vous avez perdu ! \n")
        print(f"Vous aviez {dollars_restant}$ .Votre mise était de {mise[1]}$. \n" )
        dollars_restant = dollars_restant - mise[1]

    elif winner_player == True  and value_dealer != value_player:
        print("Vous avez gagné ! \n")
        print(f"Vous aviez {dollars_restant}$.Votre mise était de {mise[1]}$. \n" )
        dollars_restant = dollars_restant + mise[1]*2

    elif value_dealer == value_player:
        print("Egalité")
        dollars_restant = dollars_restant

    print(f"Alors la somme qu'il vous reste est de {dollars_restant}$ \n" )

    jouer = input("Voulez-vous continuer de jouer ? Répondre par oui ou non. \n")
    while jouer.lower() != "oui" and jouer.lower() != "non" :
        jouer = input("Erreur, répondez par oui ou non. Voulez-vous jouer ? \n")

    if jouer.lower()=="oui" and dollars_restant<20 :
        print("Vous n'avez plus assez d'argent pour continuer, dommage !")

print("Merci, au revoir et à bientôt")
    
    







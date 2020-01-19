# -*- coding: utf-8 -*-
"""
# Author: Ricardo Cousins (cousinsr@oregonstate.edu)
# Course: OSU CS 362, Winter 2020
# Assignment: Assignment 2
# Assignment specification: https://oregonstate.instructure.com/courses/1750847/assignments/7761137?module_item_id=19203443
# Last modified: 19 January 2020

Original creation date time: Tue Oct 13 15:42:42 2015
Original author: tfleck
"""

import Dominion
import random
from collections import defaultdict

# Obtain the number of victory cards to use in the game.
# This function does not validate that input player_names has a valid structure (an array of strings).
def GetNumVictoryCards(player_names, threePlusPlayerVictoryCardCount = 12, twoPlayerVictoryCardCount = 8):
    # If there are more than 2 players in the game, there should be 12 victory cards.
    # Otherwise, for 2 players there should be 8 victory cards.
    if len(player_names) > 2:
        return threePlusPlayerVictoryCardCount
    else:
        return twoPlayerVictoryCardCount

# Obtain the number of curse cards to use in the game.
# This function does not validate that each input has a valid structure
# (an array of strings and an integer respectively).
def GetNumCurseCards(player_names, curseCardIncrementAfterFirstPlayer = 10):
    return (-1 * curseCardIncrementAfterFirstPlayer) + curseCardIncrementAfterFirstPlayer * len(player_names)

# Create a dictionary of Kingdom cards.
# This function does not validate that each input is an integer.
def GetBoxes(nV, actionCardSupply = 10):
    # Define box
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()]*actionCardSupply
    box["Smithy"] = [Dominion.Smithy()]*actionCardSupply
    box["Laboratory"] = [Dominion.Laboratory()]*actionCardSupply
    box["Village"] = [Dominion.Village()]*actionCardSupply
    box["Festival"] = [Dominion.Festival()]*actionCardSupply
    box["Market"] = [Dominion.Market()]*actionCardSupply
    box["Chancellor"] = [Dominion.Chancellor()]*actionCardSupply
    box["Workshop"] = [Dominion.Workshop()]*actionCardSupply
    box["Moneylender"] = [Dominion.Moneylender()]*actionCardSupply
    box["Chapel"] = [Dominion.Chapel()]*actionCardSupply
    box["Cellar"] = [Dominion.Cellar()]*actionCardSupply
    box["Remodel"] = [Dominion.Remodel()]*actionCardSupply
    box["Adventurer"] = [Dominion.Adventurer()]*actionCardSupply
    box["Feast"] = [Dominion.Feast()]*actionCardSupply
    box["Mine"] = [Dominion.Mine()]*actionCardSupply
    box["Library"] = [Dominion.Library()]*actionCardSupply
    box["Gardens"] = [Dominion.Gardens()]*nV
    box["Moat"] = [Dominion.Moat()]*actionCardSupply
    box["Council Room"] = [Dominion.Council_Room()]*actionCardSupply
    box["Witch"] = [Dominion.Witch()]*actionCardSupply
    box["Bureaucrat"] = [Dominion.Bureaucrat()]*actionCardSupply
    box["Militia"] = [Dominion.Militia()]*actionCardSupply
    box["Spy"] = [Dominion.Spy()]*actionCardSupply
    box["Thief"] = [Dominion.Thief()]*actionCardSupply
    box["Throne Room"] = [Dominion.Throne_Room()]*actionCardSupply
    return box

# Create a dictionary for printing the buying power cost of each card in the game.
# Note that there is no programmatic connection between the buying power costs listed below and the actual buying power
# costs specified in Dominion.py.
def GetSupplyOrder():
    supply_order = {0: ['Curse', 'Copper'],
                    2: ['Estate', 'Cellar', 'Chapel', 'Moat'],
                    3: ['Silver', 'Chancellor', 'Village', 'Woodcutter', 'Workshop'],
                    4: ['Gardens', 'Bureaucrat', 'Feast', 'Militia', 'Moneylender', 'Remodel', 'Smithy', 'Spy', 'Thief', 'Throne Room'],
                    5: ['Duchy', 'Market', 'Council Room', 'Festival', 'Laboratory', 'Library', 'Mine', 'Witch'],
                    6: ['Gold', 'Adventurer'],
                    8: ['Province']}
    return supply_order

# Pick the specified number of Kingdom cards types from the box to be in the game's supply.
# This function does not validate if box and numKingdomCards have valid structure (dictionary and integer respectively).
def GetGameSupplyKingdomCards(box, numKingdomCards = 10):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    randomNumKingdomCards = boxlist[:numKingdomCards]
    return defaultdict(list, [(k, box[k]) for k in randomNumKingdomCards])


# Add default supply cards to the game's supply.
# This function does not validate that inputs have valid structure
# (integer, integer, array of strings, and dictionary respectively).
def GetGameSupplyDefaultSupplyCards(nV, nC, player_names, supply):
    supply["Copper"] = [Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"] = [Dominion.Silver()]*40
    supply["Gold"] = [Dominion.Gold()]*30
    supply["Estate"] = [Dominion.Estate()]*nV
    supply["Duchy"] = [Dominion.Duchy()]*nV
    supply["Province"] = [Dominion.Province()]*nV
    supply["Curse"] = [Dominion.Curse()]*nC

# Construct the Player objects.
# This function does not validate that the input is an array of strings.
def GetPlayerObjects(player_names):
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

# Run the Dominion game.
# This function does not validate that inputs have valid structure
# (dictionary, dictionary, and array of Player objects respectively).
def RunGame(supply_order, supply, players):
    # Initialize the trash.
    trash = []
    # Play the game.
    turn = 0
    while not Dominion.gameover(supply):
        turn += 1
        print("\r")
        for value in supply_order:
            print(value)
            for stack in supply_order[value]:
                if stack in supply:
                    print(stack, len(supply[stack]))
        print("\r")
        for player in players:
            print(player.name, player.calcpoints())
        print("\rStart of turn " + str(turn))
        for player in players:
            if not Dominion.gameover(supply):
                print("\r")
                player.turn(players, supply, trash)

# Calculate the final scores of the Dominion game players and determine who won.
# This function does not validate that the input is an array of Player objects.
def DetermineGameWinners(players):
    dcs = Dominion.cardsummaries(players)
    vp = dcs.loc['VICTORY POINTS']
    vpmax = vp.max()
    winners = []
    for i in vp.index:
        if vp.loc[i] == vpmax:
            winners.append(i)
    if len(winners) > 1:
        winstring = ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0], 'wins!'])

    print("\nGAME OVER!!!\n" + winstring + "\n")
    print(dcs)

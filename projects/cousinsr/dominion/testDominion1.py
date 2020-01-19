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

import testUtility

# Get the player names.
player_names = ["Rico", "*Lord Vader"]

# Get the number of victory cards and curse cards.
numVictoryCards = testUtility.GetNumVictoryCards(player_names, 12, 1)
numCurseCards = testUtility.GetNumCurseCards(player_names)

# Define the box of Kingdom cards.
box = testUtility.GetBoxes(numVictoryCards)

# Create a dictionary for printing the buying power cost of each card in the game.
supply_order = testUtility.GetSupplyOrder()

# Pick 10 Kingdom cards from box to be in the game's supply.
supply = testUtility.GetGameSupplyKingdomCards(box)

# Add default supply cards to the game's supply.
testUtility.GetGameSupplyDefaultSupplyCards(numVictoryCards, numCurseCards, player_names, supply)

# Construct the Player objects.
players = testUtility.GetPlayerObjects(player_names)

# Play the Dominion game.
testUtility.RunGame(supply_order, supply, players)

# Calculate the final scores of the Dominion game players and determine who won.
testUtility.DetermineGameWinners(players)

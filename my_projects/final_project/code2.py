#!/usr/bin/env python
"""Alexandra | Mad Libs"""

from reportlab.pdfgen import canvas

def main():
    # Get input from the user
    adjective = input("Enter a adjective: ")
    adjective2 = input("Enter a adjective: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    plural_noun = input("Enter a plural noun: ")
    game = input("Enter a name of a game: ")
    plural_noun2 = input("Enter a plural noun: ")
    ing_verb = input("Enter a verb ending in -ing: ")
    ing_verb2 = input("Enter a verb ending in -ing: ")
    plural_noun3 = input("Enter a plural noun: ")
    ing_verb3 = input("Enter a verb ending in -ing: ")
    noun3 = input("Enter a noun: ")
    plant = input("Enter a name of a plant: ")
    body_part = input("Enter the name of a body part: ")
    place = input("Enter a name of a place: ")
    ing_verb4 = input("Enter a verb ending in -ing: ")
    adjective3 = input("Enter a adjective: ")
    number = input("Enter a number: ")
    plural_noun4 = input("Enter a plural noun: ")

    # Create the Mad Libs story
    story = ("A vacation is when you take a trip to some " + adjective + " place with your " +
             adjective2 + " family. Usually you go to some place that is near a/an " + noun + " or up on a/an "+
             noun2 + ". A good vacation place is one where you can ride " + plural_noun + " or play " + game +
             " or go hunting for " + plural_noun2 + ". I like to spend my time "+ ing_verb + " or " + ing_verb2 +
             ". When parents go on a vacation, they spend their time eating three "+ plural_noun3 +
             " a day, and fathers play golf, and mothers sit around " + ing_verb3 +
             ". Last summer, my little brother fell in a/an " + noun3 + " and got poison " + plant +
             " all over his " + body_part + ". My family is going to go to the " + place +
             ", and I will practice " + ing_verb4 +
             ". Parents need vacations more than kids because parents are always very " +
             adjective3 + " and because they have to work " + number +
             " hours every day all year making enough " + plural_noun4 + " to pay for the vacation.")

    # Display story 
    print(story)

    # Create a PDF file
    c = canvas.Canvas("mad_libs.pdf")
    text = c.beginText()
    text.setTextOrigin(50, 700)
    text.setFont("Helvetica", 12)
    text.textLines(story)
    c.drawText(text)
    c.showPage()
    c.save()

if __name__ == "__main__":
    main()

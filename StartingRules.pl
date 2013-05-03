% starting knowledge base
female(scarlett).
female(white).
female(peacock).
male(mustard).
male(plum).
male(green).
adjacent(study, hall).
adjacent(study, library).

adjacent(hall, study).
adjacent(hall, lounge).

adjacent(lounge, hall).
adjacent(lounge, dining).

adjacent(dining, lounge).
adjacent(dining, kitchen).

adjacent(kitchen, dining).
adjacent(kitchen, ball).

adjacent(ball, kitchen).
adjacent(ball, conservatory).

adjacent(conservatory, billiard).
adjacent(conservatory, ball).

adjacent(billiard, conservatory).
adjacent(billiard, library).

adjacent(library, billiard).
adjacent(library, study).

murderer(mustard) :- weapon(dagger); weapon(rope); weapon(leadpipe);
                    weapon(candlestick); weapon(wrench).
murderer(green) :- weapon(leadpipe); weapon(wrench).

murderer(peacock) :- weapon(dagger); weapon(leadpipe); weapon(candlestick); 
                    weapon(wrench); weapon(revolver).

adjacent(R, Q) :- murderer(X), female(X), startingroom(R), room(Q).

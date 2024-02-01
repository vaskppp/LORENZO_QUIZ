# Déclarez les personnages utilisés dans le jeu.
define l = Character("Lorenzo", color="#c8ffc8")
define dissolve_slow = Dissolve(2.0)
# Le jeu commence ici
label youdied:
    hide Screen
    play sound youdiedaudio
    show died  with dissolve_slow
    return
label victoire:
    hide Screen
    l"GG"
    return 

label start:

    show lorenzor at left with dissolve
    l "Bienvenue sur le LORENZO QUIZZ"

    jump question1

label question1:
    hide quiz
    show lapini at right with move
    l "Tu dois bien répondre à la question qui va suivre"
    show lapin
    l "Quel est cet animal ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Chien":
            $ player_response = "Chien"
        "Viande":
            $ player_response = "Viande"
        "Lapin":
            $ player_response = "Lapin"

    if player_response == "Viande":
        jump q2
    else:
        jump youdied

label q2:
    label question2:
        hide lapin
        show lorenzor  with  pixellate
        l"Bravo tu as réussis la première question"
        $ player_response = None  # Variable pour stocker la réponse du joueur
        $ player_response= renpy.input("Combien font 1+1 ?")


        if player_response == "11":
            jump q3
        else:
            jump  youdied

    return


label q3:
    show lorenzor at right with move
    hide lorenzor with dissolve
    l "Quel Accessoire m'irai le mieux ?"
    show chap1 at left
    show thug at right
    $ player_response = None  # Variable pour stocker la réponse du joueur
    menu:
        "Chapeau Magicien":
            $ player_response = "Magicien"

        "Lunettes Thug":
            $ player_response = "Thug"


    if player_response == "Magicien":
        jump c5
    else:
        jump l5

label c5:
    show sorcier
    hide chap1
    hide thug
    show lorenzorc at right with dissolve
    l"Je suis un Magicien ?"
    menu:
        "Oui":
            jump q5
        "Non":
            jump youdied

label l5:
    show thuglife
    hide chap1
    hide thug
    show lorenzorl at right with dissolve
    $ player_response = None
    l"Je suis un Thug ?"
    menu:
        "Oui":
            jump q5
        "Non":
            jump youdied


label q5:
    hide sorcier
    hide thuglife
    show ocean with pixellate
    l "Quel est l'océan le plus grand du monde ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Océan Atlantique":
            $ player_response = "Atlantique"
        "Océan Pacifique":
            $ player_response = "Pacifique"
        "Océan Indien":
            $ player_response = "Indien"

    if player_response == "Pacifique":
        jump q6
    else:
        jump youdied
label q6:
    hide lorenzorc with dissolve
    hide lorenzorl with dissolve
    hide ocean
    show lorenzor at left with move
    show paris with pixellate

    l "Quel est le nom de la capitale de la France ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Paris":
            $ player_response = "Paris"
        "Londres":
            $ player_response = "Londres"
        "Berlin":
            $ player_response = "Berlin"

    if player_response == "Paris":
        jump q7
    else:
        jump youdied

label q7:
    show lorenzor at right with move
    hide paris with dissolve
    show solaire with dissolve
    l "Quelle est la plus grande planète du système solaire ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Jupiter":
            $ player_response = "Jupiter"
        "Saturne":
            $ player_response = "Saturne"
        "Neptune":
            $ player_response = "Neptune"

    if player_response == "Jupiter":
        jump q8
    else:
        jump youdied
label q8:
    show lorenzor at left with move
    hide solaire with dissolve
    show terre with dissolve
    l "Combien de continents y a-t-il sur la Terre ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Cinq":
            $ player_response = "Cinq"
        "Six":
            $ player_response = "Six"
        "Sept":
            $ player_response = "Sept"

    if player_response == "Sept":
        jump q9
    else:
        jump youdied

label q9:
    hide lorenzor with dissolve
    hide terre with pixellate
    show felin with pixellate
    l "Quel est l'animal terrestre le plus rapide ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Guepard":
            $ player_response = "Guepard"
        "Lion":
            $ player_response = "Lion"
        "Leopard":
            $ player_response = "Leopard"

    if player_response == "Guepard":
        jump q10
    else:
        jump youdied

label q10:
    hide felin
    show lorenzor at right with move
    hide lorenzor with dissolve
    l "Qui a peint la Joconde ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur
    show joconde
    menu:
        "Leonard de Vinci":
            $ player_response = "Leonard de Vinci"
        "Pablo Picasso":
            $ player_response = "Pablo Picasso"
        "Vincent van Gogh":
            $ player_response = "Vincent van Gogh"

    if player_response == "Leonard de Vinci":
        jump q11
    else:
        jump youdied

label q11:
    
    hide joconde
    show lorenzor at right with move
    hide lorenzor with dissolve
    show australie
    l "Quelle est la capitale de l'Australie ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Sydney":
            $ player_response = "Sydney"
        "Melbourne":
            $ player_response = "Melbourne"
        "Canberra":
            $ player_response = "Canberra"

    if player_response == "Canberra":
        jump q12
    else:
        jump youdied
label q12:
    hide australie
    show cheval
    show lorenzor at right with move
    l "Quelle est la couleur du cheval blanc d'Henri IV ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Blanc":
            $ player_response = "Blanc"
        "Noir":
            $ player_response = "Noir"
        "Gris":
            $ player_response = "Gris"

    if player_response == "Blanc":
        jump q13
    else:
        jump youdied

label q13:
    hide lorenzor with dissolve
    hide cheval
    show lorenzor at right with move
    show petitprince
    l "Qui a écrit 'Le Petit Prince' ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Antoine de Saint-Exupéry":
            $ player_response = "Antoine de Saint-Exupéry"
        "Marcel Proust":
            $ player_response = "Marcel Proust"
        "Victor Hugo":
            $ player_response = "Victor Hugo"

    if player_response == "Antoine de Saint-Exupéry":
        jump q14
    else:
        jump youdied

label q14:
    hide lorenzor with dissolve
    hide petitprince
    show desert with ease
    l "Quel est le plus grand désert du monde ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Le Sahara":
            $ player_response = "Le Sahara"
        "Le désert de Gobi":
            $ player_response = "Le désert de Gobi"
        "Le désert d'Atacama":
            $ player_response = "Le désert d'Atacama"

    if player_response == "Le Sahara":
        jump q15
    else:
        jump youdied

label q15:
    hide desert with dissolve
    show romeo with dissolve
    l "Qui est l'auteur de la pièce de théâtre 'Roméo et Juliette' ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "William Shakespeare":
            $ player_response = "William Shakespeare"
        "Molière":
            $ player_response = "Molière"
        "Victor Hugo":
            $ player_response = "Victor Hugo"

    if player_response == "William Shakespeare":
        jump q17
    else:
        jump youdied
label q17:
    show decouverte with dissolve
    hide romeo with dissolve
    l "Qui a découvert l'Amérique ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Christophe Colomb":
            $ player_response = "Christophe Colomb"
        "Vasco de Gama":
            $ player_response = "Vasco de Gama"
        "Amerigo Vespucci":
            $ player_response = "Amerigo Vespucci"

    if player_response == "Christophe Colomb":
        jump q18
    else:
        jump youdied

label q18:
    hide decouverte with dissolve
    show lorenzor at right with pixellate
    show hamlet with pixellate
    l "Qui a écrit 'Hamlet' ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "William Shakespeare":
            $ player_response = "William Shakespeare"
        "Charles Dickens":
            $ player_response = "Charles Dickens"
        "Jane Austen":
            $ player_response = "Jane Austen"

    if player_response == "William Shakespeare":
        jump q19
    else:
        jump youdied

label q19:
    hide hamlet with pixellate
    show berlin with dissolve
    l "Quelle est la capitale de l'Allemagne ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Berlin":
            $ player_response = "Berlin"
        "Munich":
            $ player_response = "Munich"
        "Francfort":
            $ player_response = "Francfort"

    if player_response == "Berlin":
        jump q20
    else:
        jump youdied

label q20:
    hide berlin
    show fleuve
    l "Quel est le plus grand fleuve du monde ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Nil":
            $ player_response = "Nil"
        "Amazone":
            $ player_response = "Amazone"
        "Mississippi":
            $ player_response = "Mississippi"

    if player_response == "Amazone":
        jump q21
    else:
        jump youdied

label q21:
    hide fleuven
    show math
    show lorenzor at right with dissolve
    hide lorenzor with fade
    l "Mode Génie des Maths activé"
    l "Quel est le résultat de l'intégrale de e^x par rapport à x de 0 à 1 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "e - 1":
            $ player_response = "e - 1"
        "e + 1":
            $ player_response = "e + 1"
        "e":
            $ player_response = "e"
        "e^2":
            $ player_response = "e^2"
        "e - 2":
            $ player_response = "e - 2"

    if player_response == "e":
        jump q22
    else:
        jump youdied

label q22:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quel est le résultat de la série géométrique infinie : 1 + 1/2 + 1/4 + 1/8 + ... ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "2":
            $ player_response = "2"
        "3":
            $ player_response = "3"
        "4":
            $ player_response = "4"
        "1/2":
            $ player_response = "1/2"
        "Infini":
            $ player_response = "Infini"

    if player_response == "2":
        jump q23
    else:
        jump youdied

label q23:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quelle est la valeur de pi à 5 décimales près ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "3,14159":
            $ player_response = "3,14159"
        "3,14150":
            $ player_response = "3,14150"
        "3,14169":
            $ player_response = "3,14169"
        "3,14140":
            $ player_response = "3,14140"
        "3,14145":
            $ player_response = "3,14145"

    if player_response == "3,14159":
        jump q24
    else:
        jump youdied

label q24:
    show lorenzor at right with dissolve
    hide lorenzor with moveout
    l "Si x = 2^3 et y = 3^2, quelle est la valeur de x^y ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "512":
            $ player_response = "512"
        "64":
            $ player_response = "64"
        "256":
            $ player_response = "256"
        "128":
            $ player_response = "128"
        "1024":
            $ player_response = "1024"

    if player_response == "64":
        jump q25
    else:
        jump youdied

label q25:
    hide math
    show lorenzor at right with dissolve
    hide lorenzor with fade
    show histoire 
    l "Quelle bataille a mis fin à l'empire napoléonien en Europe en 1815 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Bataille de Leipzig":
            $ player_response = "Bataille de Leipzig"
        "Bataille de Waterloo":
            $ player_response = "Bataille de Waterloo"
        "Bataille de Trafalgar":
            $ player_response = "Bataille de Trafalgar"
        "Bataille d'Austerlitz":
            $ player_response = "Bataille d'Austerlitz"

    if player_response == "Bataille de Waterloo":
        jump q26
    else:
        jump youdied

label q26:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quel traité a mis fin à la Première Guerre mondiale en 1919 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Traité de Versailles":
            $ player_response = "Traité de Versailles"
        "Traité de Trianon":
            $ player_response = "Traité de Trianon"
        "Traité de Saint-Germain-en-Laye":
            $ player_response = "Traité de Saint-Germain-en-Laye"
        "Traité de Sèvres":
            $ player_response = "Traité de Sèvres"

    if player_response == "Traité de Versailles":
        jump q27
    else:
        jump youdied

label q27:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quelle est la date de la bataille de Stalingrad pendant la Seconde Guerre mondiale ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "1942":
            $ player_response = "1942"
        "1943":
            $ player_response = "1943"
        "1944":
            $ player_response = "1944"
        "1945":
            $ player_response = "1945"

    if player_response == "1942":
        jump q28
    else:
        jump youdied

label q28:
    show lorenzor at right with dissolve
    hide lorenzor with dissolve_slow
    l "Quel empereur romain a construit le mur d'Hadrien en Grande-Bretagne ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Auguste":
            $ player_response = "Auguste"
        "Trajan":
            $ player_response = "Trajan"
        "Hadrien":
            $ player_response = "Hadrien"
        "Marc Aurèle":
            $ player_response = "Marc Aurèle"

    if player_response == "Hadrien":
        jump q29
    else:
        jump youdied

label q29:
    show lorenzor at right with dissolve
    hide lorenzor with dissolve
    l "Quel roi d'Angleterre a signé la Magna Carta en 1215 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Richard Cœur de Lion":
            $ player_response = "Richard Cœur de Lion"
        "Jean Sans Terre":
            $ player_response = "Jean Sans Terre"
        "Henri II":
            $ player_response = "Henri II"
        "Édouard III":
            $ player_response = "Édouard III"

    if player_response == "Jean Sans Terre":
        jump q30
    else:
        jump youdied

label q30:
    hide histoire
    show lorenzor at right with dissolve
    hide lorenzor with dissolve
    show chine with dissolve
    l "Quelle dynastie a marqué la Chine vers l'année -2000 avant notre ère ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Dynastie Xia":
            $ player_response = "Dynastie Xia"
        "Dynastie Shang":
            $ player_response = "Dynastie Shang"
        "Dynastie Zhou":
            $ player_response = "Dynastie Zhou"
        "Dynastie Qin":
            $ player_response = "Dynastie Qin"
        "Dynastie Han":
            $ player_response = "Dynastie Han"
        "Dynastie Tang":
            $ player_response = "Dynastie Tang"
        "Dynastie Song":
            $ player_response = "Dynastie Song"
        "Dynastie Yuan":
            $ player_response = "Dynastie Yuan"

    if player_response == "Dynastie Shang":
        jump q31
    else:
        jump youdied


label q31:
    hide chine
    show rome with pixellate
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quel empereur romain a construit le Colisée de Rome vers l'an 70-80 après J.-C. ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Néron":
            $ player_response = "Néron"
        "Trajan":
            $ player_response = "Trajan"
        "Auguste":
            $ player_response = "Auguste"
        "Titus":
            $ player_response = "Titus"
        "Hadrien":
            $ player_response = "Hadrien"
        "Caligula":
            $ player_response = "Caligula"
        "Vespasien":
            $ player_response = "Vespasien"
        "Marc Aurèle":
            $ player_response = "Marc Aurèle"

    if player_response == "Vespasien":
        jump q32
    else:
        jump youdied

label q32:
    show lorenzor at right with dissolve
    hide lorenzor with dissolve
    l "Quelle bataille a marqué la fin de la guerre de Cent Ans entre la France et l'Angleterre ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Bataille de Castillon (1453)":
            $ player_response = "Bataille de Castillon (1453)"
        "Bataille de Crécy (1346)":
            $ player_response = "Bataille de Crécy (1346)"
        "Bataille d'Azincourt (1415)":
            $ player_response = "Bataille d'Azincourt (1415)"
        "Bataille de Poitiers (1356)":
            $ player_response = "Bataille de Poitiers (1356)"
        "Bataille de Bouvines (1214)":
            $ player_response = "Bataille de Bouvines (1214)"
        "Bataille de Patay (1429)":
            $ player_response = "Bataille de Patay (1429)"
        "Bataille de Formigny (1450)":
            $ player_response = "Bataille de Formigny (1450)"
        "Bataille de Verneuil (1424)":
            $ player_response = "Bataille de Verneuil (1424)"

    if player_response == "Bataille de Castillon (1453)":
        jump q33
    else:
        jump youdied

label q33:
    show lorenzor at right with dissolve
    hide lorenzor with fade
    l "Quel événement a marqué la fin de la Guerre froide en Europe en 1989 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Chute du mur de Berlin":
            $ player_response = "Chute du mur de Berlin"
        "Réunification de l'Allemagne":
            $ player_response = "Réunification de l'Allemagne"
        "Dislocation de l'Union soviétique":
            $ player_response = "Dislocation de l'Union soviétique"
        "Signature du traité START":
            $ player_response = "Signature du traité START"
        "Révolution de velours en Tchécoslovaquie":
            $ player_response = "Révolution de velours en Tchécoslovaquie"
        "Élection de Boris Eltsine":
            $ player_response = "Élection de Boris Eltsine"
        "Création de l'OTAN":
            $ player_response = "Création de l'OTAN"
        "Chute du rideau de fer":
            $ player_response = "Chute du rideau de fer"

    if player_response == "Chute du mur de Berlin":
        jump q34
    else:
        jump youdied

label q34:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quelle bataille a marqué la fin de la Guerre de Sécession aux États-Unis en 1865 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Bataille d'Antietam":
            $ player_response = "Bataille d'Antietam"
        "Bataille de Gettysburg":
            $ player_response = "Bataille de Gettysburg"
        "Bataille de Vicksburg":
            $ player_response = "Bataille de Vicksburg"
        "Bataille de Bull Run (Première bataille)":
            $ player_response = "Bataille de Bull Run (Première bataille)"
        "Bataille de Shiloh":
            $ player_response = "Bataille de Shiloh"
        "Bataille de Fort Sumter":
            $ player_response = "Bataille de Fort Sumter"
        "Bataille de Spotsylvania Court House":
            $ player_response = "Bataille de Spotsylvania Court House"
        "Bataille de Cold Harbor":
            $ player_response = "Bataille de Cold Harbor"

    if player_response == "Bataille d'Appomattox Court House":
        jump q35
    else:
        jump youdied

label q35:
    show lorenzor at right with dissolve
    hide lorenzor with dissolve
    l "Qui était le Premier Ministre du Royaume-Uni au début de la Première Guerre mondiale en 1914 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Herbert Henry Asquith":
            $ player_response = "Herbert Henry Asquith"
        "David Lloyd George":
            $ player_response = "David Lloyd George"
        "Arthur Balfour":
            $ player_response = "Arthur Balfour"
        "Winston Churchill":
            $ player_response = "Winston Churchill"
        "Stanley Baldwin":
            $ player_response = "Stanley Baldwin"
        "Neville Chamberlain":
            $ player_response = "Neville Chamberlain"
        "Clement Attlee":
            $ player_response = "Clement Attlee"
        "Anthony Eden":
            $ player_response = "Anthony Eden"

    if player_response == "Herbert Henry Asquith":
        jump q36
    else:
        jump youdied

label q36:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Qui a dirigé la France pendant la Révolution française de 1789 à 1799 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Louis XVI":
            $ player_response = "Louis XVI"
        "Napoléon Bonaparte":
            $ player_response = "Napoléon Bonaparte"
        "Louis XVIII":
            $ player_response = "Louis XVIII"
        "Louis-Philippe":
            $ player_response = "Louis-Philippe"
        "Georges Danton":
            $ player_response = "Georges Danton"
        "Jean-Paul Marat":
            $ player_response = "Jean-Paul Marat"
        "Robespierre":
            $ player_response = "Robespierre"
        "Jacques Necker":
            $ player_response = "Jacques Necker"

    if player_response == "Napoléon Bonaparte":
        jump q37
    else:
        jump youdied
    
label q37:
    show lorenzor at right with dissolve
    hide lorenzor with fade
    l "Quel empereur romain a construit le Colisée de Rome ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Auguste":
            $ player_response = "Auguste"
        "Caligula":
            $ player_response = "Caligula"
        "Néron":
            $ player_response = "Néron"
        "Vespasien":
            $ player_response = "Vespasien"
        "Titus":
            $ player_response = "Titus"
        "Domitien":
            $ player_response = "Domitien"
        "Hadrien":
            $ player_response = "Hadrien"
        "Antonin le Pieux":
            $ player_response = "Antonin le Pieux"
        "Marc Aurèle":
            $ player_response = "Marc Aurèle"
        "Commode":
            $ player_response = "Commode"

    if player_response == "Vespasien":
        jump q38
    else:
        jump youdied

label q38:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quel explorateur portugais a découvert le passage maritime vers l'Inde en contournant le cap de Bonne-Espérance en 1498 ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Vasco de Gama":
            $ player_response = "Vasco de Gama"
        "Christophe Colomb":
            $ player_response = "Christophe Colomb"
        "Ferdinand Magellan":
            $ player_response = "Ferdinand Magellan"
        "Amerigo Vespucci":
            $ player_response = "Amerigo Vespucci"
        "Marco Polo":
            $ player_response = "Marco Polo"
        "Juan Sebastián Elcano":
            $ player_response = "Juan Sebastián Elcano"
        "James Cook":
            $ player_response = "James Cook"
        "Hernán Cortés":
            $ player_response = "Hernán Cortés"
        "Francisco Pizarro":
            $ player_response = "Francisco Pizarro"
        "John Cabot":
            $ player_response = "John Cabot"

    if player_response == "Vasco de Gama":
        jump q39
    else:
        jump youdied

label q39:
    show lorenzor at right with dissolve
    hide lorenzor with dissolve
    l "Qui a été le premier président des États-Unis ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "George Washington":
            $ player_response = "George Washington"
        "Thomas Jefferson":
            $ player_response = "Thomas Jefferson"
        "John Adams":
            $ player_response = "John Adams"
        "James Madison":
            $ player_response = "James Madison"
        "Abraham Lincoln":
            $ player_response = "Abraham Lincoln"
        "Andrew Jackson":
            $ player_response = "Andrew Jackson"
        "Theodore Roosevelt":
            $ player_response = "Theodore Roosevelt"
        "John F. Kennedy":
            $ player_response = "John F. Kennedy"
        "Ronald Reagan":
            $ player_response = "Ronald Reagan"
        "Barack Obama":
            $ player_response = "Barack Obama"

    if player_response == "George Washington":
        jump q40
    else:
        jump youdied

label q40:
    show lorenzor at right with dissolve
    hide lorenzor with moveout
    l "Quel roi de France a été guillotiné pendant la Révolution française ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Louis XVI":
            $ player_response = "Louis XVI"
        "Louis XV":
            $ player_response = "Louis XV"
        "Louis XIV":
            $ player_response = "Louis XIV"
        "Louis XIII":
            $ player_response = "Louis XIII"
        "Louis XVII":
            $ player_response = "Louis XVII"
        "Louis XVIII":
            $ player_response = "Louis XVIII"
        "Louis Philippe Ier":
            $ player_response = "Louis Philippe Ier"
        "Charles X":
            $ player_response = "Charles X"
        "Napoléon Ier":
            $ player_response = "Napoléon Ier"
        "Henri IV":
            $ player_response = "Henri IV"

    if player_response == "Louis XVI":
        jump q41
    else:
        jump youdied

label q41:
    show lorenzor at right with dissolve
    hide lorenzor with pixellate
    l "Quelle est l'étoile la plus proche de la Terre ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Le Soleil":
            $ player_response = "Le Soleil"
        "Proxima Centauri":
            $ player_response = "Proxima Centauri"
        "Alpha Centauri":
            $ player_response = "Alpha Centauri"
        "Sirius":
            $ player_response = "Sirius"
        "Bételgeuse":
            $ player_response = "Bételgeuse"
        "Pollux":
            $ player_response = "Pollux"
        "Rigel":
            $ player_response = "Rigel"
        "Arcturus":
            $ player_response = "Arcturus"
        "Véga":
            $ player_response = "Véga"
        "Deneb":
            $ player_response = "Deneb"

    if player_response == "Le Soleil":
        jump q42
    else:
        jump youdied

label q42:
    show lorenzor at right with dissolve
    hide lorenzor with dissolve
    l "Quelle est la plus grande lune de Jupiter ?"
    $ player_response = None  # Variable pour stocker la réponse du joueur

    menu:
        "Ganymède":
            $ player_response = "Ganymède"
        "Io":
            $ player_response = "Io"
        "Callisto":
            $ player_response = "Callisto"
        "Europe":
            $ player_response = "Europe"
        "Titan":
            $ player_response = "Titan"
        "Titan":
            $ player_response = "Titan"
        "Triton":
            $ player_response = "Triton"
        "Lune":
            $ player_response = "Lune"
        "Phobos":
            $ player_response = "Phobos"
        "Déimos":
            $ player_response = "Déimos"

    if player_response == "Ganymède":
        jump victoire
    else:
        jump youdied

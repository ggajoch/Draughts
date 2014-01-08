Draughts
========

Automatic draughts player


Wykorzystanie języka Python z biblioteką OpenCV oraz lego NXT w celu zbudowania automatu do gry w warcaby.

Abstrakt:
Zbudowanie automarycznego robota do gry w warcaby.
Komputer powinien wykrywać pionki na planszy do warcabów, analizować ruchy, rozstrzygać o ich poprawności a następnie odpowiedzieć na ruch gracza (przestawić pionki na szachownicy).


Założenia projektu:
wykorzystanie kamery wbudowanej w telefon z androidem w celu rozpoznania pionków na szachownicy,
zbudowanie suwnicy oraz mechanizmu przesuwającego pionki za pomocą lego NXT,
transmisja danych pomiędzy NXT i komputerem za pomocą bluetooth
zaimplementowanie algorytmu do gry w warcaby

Technologie:
język python z biblioteką OpenCV - rozpoznawanie obrazu, analiza, algorytm do grania w warcaby, komunikacja z Lego NXT w celu przesłania koordynatów pionków do przesunięcia,
oprogramowanie NXT w języku NXC (Not eXactly C) sterujące silnikami - przesuwające pionki.



backlog:

Modules:
 - Image - board recognition
 - Game backend - draughts play algorithm
 - NXT backend - low level functions to communicate with NXT brick
 - NXT middleend - high level functions moving plotter
 - FrontEnd - GUI showing user stats, board, moves etc.
 - Main - connect everything, main algorithm of the game, run GUI etc.

Physical Device:
 - Mostly done, based on Lego NXT + train +steel rods to hold main frame of device.

Image  - done:
 - camera connection - done/improve - (MJPEG stream to frontend)
 - piece recognition - done
 - piece color recognition - done
 - board interface to other modules - done

Game backend - done:
 - Board and move normalisation classes - done
 - board position recognition and analysis - done
 - heuristic function to analyse board position - done/constant improve
 - heuristic algorithm (alfa-beta) choosing best possible move - done

NXT backend:
 - establish connection with NXT (bluetooth) - done
 - send coordinates - done
 - take piece, move, put it down - [todo]
 - optional - read press key to determine end of human move move

NXT middleEnd:
 - interface connecting low level functions from NXT backend and Main program

FrontEnd:
 - determine technology - PyQt ?
 - design interface
 - implement buttons, fields
 - connect to Game backend and NXT middleEnd to direct move plotter over board.

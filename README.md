# BATTLESHIPS

## Battleships is a fun and interactive game played against the computer. It runs in the Code institute mock terminal on [Heroku](https://www.heroku.com/github-students).

## The aim of the game is to try and discover the computers "battleships" before the computer discovers yours. More information on this classic game can be found [here](https://en.wikipedia.org/wiki/Battleship_(game)).

### [Here, you can view the live project.](https://mary-battleships-93db79c894ca.herokuapp.com/)

![Screenshot of project](amiresponsive.png)

### How to play

To begin, the player is asked to input their name. They are then invited to place their "Battleships" on the board, by inputting the row and column placement for each ship.

The conputer then places their battleships, which is randomly generated.

The game then commences, with a display of the players board and a dummy board for the computer, to ensure their ships remain hidden.

The player can see where their ships are, indicated with an initial, but cannot see where the computer ships are.

The player is then invited to guess the row and column of the computers ship. If they guess incorrectly, the position guessed is marked with a "*". If it's a hit, the position is marked with an "X".

The player and computer take it in turns to try to sink eachothers battleships.

The winner is the first to successfully sink the other players battleships.

### Features

#### Existing Features:
* Random Board generation for computers board
  * The player can not see where the computers ships are.
* Play against the computer
* Maintains scores
* Accepts user input
* Input validation and error checking

#### Future Features
* Have ships vary in size

### Testing

I have manually tested this project with these methods:
* I have passed my code through the pep8 linter and confirmed there are no bugs.
* I have given invalid inputs to chect the errors are working and displaying the correct error messages.
* I have tested in my local terminal and in the Heroku terminal.

#### Bugs

Solved Bugs:

* Upon deployment, I discovered that I had not correctly made a while statement to show an error message when the wrong input was given when player guesses a row and column. I fixed this by adding a while statement to display correct error message to player.

* Upon passing my code through the pep8 linter, I discovered that there were a few problems relating to indentation and white spaces. I have throughly been through my code and edited this where nessessary. 

Remaining bugs:

* No known bugs remaining.

### Validator testing
* Pep8
  * No errors were returned from pep8online.com


### Deployment

This project was deployed using Code Institute mock terminal for Heroku.
* Steps for deployment
  * Fork or clone this repository.
  * Create a new Heroku App.
  * Set the buildbacks to Python and NodeJS in that order.
  * Link the Heroku app to the repository.
  * Click on Deploy.

### Credits
* Code Institute for the deployment terminal
* Wikipedia for the details of the battleships game
* Support from the Code Institute slack community
* advice from [Stack Overflow](https://stackoverflow.com/)



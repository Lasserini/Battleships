<h1 align="center">Battleship Commander</h1>

<h2 align="center"><img src="https://github.com/Lasserini/Battleships/blob/main/readme_images/battleships_readme_image.png"></h2>

This game is a Python terminal game, build during a Diploma in Software Development at Code Institute. Its the third porfolio project out of five and is build in Python.
The game runs in Code Institute's mock terminal on Heroku.

The goal of the game is to sink all the computers ships before you run out of ammunition. Best of luck!

[Try the live version of the game here:](https://battleship-commander.herokuapp.com/)

## 1. How to Play
- First the game prompts the players for whether they would like a short, medium or long game.
- The program then creates a gameboard with some hidden ships.
- To win you must sink all the hidden ships.
- If you run out of ammunition, then the game is lost.
- Type coordinates into the terminal so select where you want to shoot.
- The game provides visual and textual feedback on whether your shot hit or missed.
- Keep shooting until the game reaches its conclusion.

## 2. User Experience (UX)

### 2.1 Project introduction
A quick game experience based upon the classic Battleships game. Here you are playing 1 player was a computer generated board of hidden ships.
Sink them all before its too late.

### 2.2 Project goals
- Create a Battleship game using Python.
- Make the gameplay loop run smoothly.
- Allow the user to adjust game lenght.

### 2.3 Target audience
The website is aimed at people who enjoy quick games, its intended to be lighthearted enough to provide a fun experience.

### 2.4 User Stories
- As a user I want to play a quick game.
- As a user I want to adjust the duration of the game.
- As a user I want to easily understand what happens after I enter coordinates
- As a user I want to know if my inputs are incorrect

### 2.5 Owner Stories
- As an owner I want to ensure invalid inputs are handled gracefully
- As an owner I want to deliver an engaging gameplay experience
- As an owner I want to publish a functional minigame

## 3. Features
### 3.1 Current Features
*   Random Board Generation 
    - Ships are placed randomly on the gameboard.
    - Ships can have varying random lenghts.
    - Ships remain hidden from the player until they take a hit.

<img src="https://github.com/Lasserini/Battleships/blob/main/readme_images/game_board.png">

*   Custom game lenght
    - Player imput dictates whether a short, medium or long game is run.
    - The factors that change are grid size, number of ships and amount of ammunition.

<img src="https://github.com/Lasserini/Battleships/blob/main/readme_images/select_game_lenght.png">

*   Imput validation
    - Must enter coordinates inside the gameboard(grid).
    - Prevents entering the same guess more than once.
    - Ensures the correct format for guesses is being used.

    <img src="https://github.com/Lasserini/Battleships/blob/main/readme_images/error_two.png">

    <img src="https://github.com/Lasserini/Battleships/blob/main/readme_images/error_one.png">

*   User feedback
    - Provides both visual and textual feedback to player shots.
    - Ensures the user is able to understand whats going on at all times.
    
### 3.2 Potential ideas for more features
- Stronger control of how many ships of each size is produced.
- Difficulty settings (fx more/less ammunition etc.)
- Sea Mines (a 1spot trap with some negative consequence to the player)

## 4. Technologies Used

### 4.1 Languages Used

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### 4.2 Programs Used

1. [Gitpod](https://gitpod.io/)
    - Gitpod was used to develop the website.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git. And to host the project.
1. [Heruku:](https://www.heroku.com/)
    - Used to create a live version of the project.
1. [Am I Responsive:](http://ami.responsivedesign.is/)
    - Used for README image.
1. [PEP8 Python Validator](https://pep8online.com/)
    - Used to validate Python code.

### 4.3 Libraries & Frameworks Used
- Used Random to help randomly place ships.

## 65 Testing
### 5.1 Solved Bugs
- The grid printed was out of line with the numbers below.
    - Added : to the letter printing to push content into place.
    - Added sidebonus is a slightly easier to read gameboard.
- The while loop in setup_game wasn't working as intended.
    - Tried a myriad on unsuccesful things.
    - At the end I found the error, I was +=1 the wrong variable which was causing all sorts of issues.
- Recieved incorrect error message when shots got a hit.
    - Corrected some incorrect Legend usage in the error checking functions.
- Program was breaking when given unexpected player input for lenght setting.
    - Added a range check and a ValueError exception.
    - Ensures the user won't break the game, and will be able to select desired game lenght.

### 5.2 Remaining Bugs
- Typing a single input to coordinates breaks the game.

### 5.3 Validator Testing
The code passes through the PEP8 Validator without issues.

<img src="https://github.com/Lasserini/Battleships/blob/main/readme_images/pep8_battleship_validation.png">

### 5.3 Testing User Stories
- As a user I want to play a quick game.
    - Upon clicking the link, I need to select 1 option then the game starts.
- As a user I want to adjust the duration of the game.
    - The opening screen provides 3 options for game duration.
- As a user I want to easily understand what happens after I enter coordinates
    - After selecting correct coordinates, the game prints several lines that explains what happened.
    - The game also updates the visual gameboard, to provide visual confirmation to the user.
- As a user I want to know if my inputs are incorrect
    - When something incorrect is entered, the game informs me of the problem and attempts to help fix it.

### 5.4 Testing Owner Stories
- As an owner I want to ensure invalid inputs are handled gracefully
    - The program handles most invaled inputs gracefully, and helps the user back on track.
- As an owner I want to deliver an engaging gameplay experience
    - The game features some flavour text, attempting to bring a little story to life.
- As an owner I want to publish a functional minigame
    - The game works as intended.


## 6. Deployment
The project was deployed using Code Institute's mock terminal for Heroku.

*   Steps for deployment   
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy


## 7. Credits

### Code inspiration
- Throughtout the project I have drawn inspiration from a tutorial Battleshild video from [CS Students:](https://www.youtube.com/watch?v=MgJBgnsDcF0)
- The basic structuring of the programme & the board+ship generation functions is build upon the concepts explained in the video.

### Content
-   All content was written by the developer.


### Acknowledgements

- [W3Schools:](https://www.w3schools.com/) for being a great place to find helpful answers.

- Code Institute for the deployment terminal.
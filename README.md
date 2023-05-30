# Tic-Tac-Toe Python

This project implements an Intelligent Strategy Manager (ISM) for a tic-tac-toe game. It uses a reinforcement learning (RL) algorithm for the AI Player to learn and strategize the game moves. It also includes a graphical user interface (GUI) using Tkinter for visualizing the game board and blob animations.

## Files included in this repository:

- Game.py: Main game logic and ISM controller.

- Player.py: Defines the AI Player and its behavior such as choosing actions and updating parameters.

- RL.py: Contains the implementation of the Reinforcement Learning (RL) model for the AI Player.

- gui.py: Graphical user interface for the game board.

- b.py: Contains code for blob animations.

## Dependencies

- Python 3.6+
- NumPy
- TensorFlow
- Tkinter
- PIL (Python Imaging Library)

## Usage

To run the application, you need to execute the GUI file:

```bash
python gui.py
```

## File Descriptions

- **Game.py**: This file contains the class `ISM` which is the main game logic and the controller for the Intelligent Strategy Manager. It has methods to print the board, get the game state, update the game state, train the RL model, calculate game performance, and check win conditions.

- **Player.py**: This file contains the class `Player` which implements the game player. The Player can be either a user or an AI. If it's an AI, it uses a reinforcement learning strategy to choose its actions. 

- **RL.py**: This file contains the class `RL` which implements a basic reinforcement learning model using a neural network. This RL model is used by the AI player to learn the game and make decisions.

- **b.py**: This file contains the class `Blob` which is used to create animated blob objects on the game board. The blobs move in a left and right motion.

- **gui.py**: This file contains the game's graphical user interface implemented with Tkinter. It displays the game board and allows users to interact with the game.

## Contributing

Feel free to fork this project, add your improvements and then propose them through a pull request.

## License

This project is released under the MIT License.

## Contact

Please, if you have any question or advice, feel free to open an issue. We will be glad to hear from you.

# Anni_Assesment_game
PYTHON COMMAND LINE GAME
GitHub Link : hƩps://github.com/Reddygopalkrishna/Anni_Assesment_game
Rabbit and Carrot Game
This is a simple text-based game where the player controls a rabbit that must collect carrots
and reach rabbit holes to win.
How to Play
- Use the 'w', 'a', 's', and 'd' keys to move the rabbit.
- Press 'p' to pick up a carrot if the rabbit is on a carrot Ɵle.
- Navigate the rabbit to the rabbit holes to win.
- You can also press 'Enter' to see the opƟmal soluƟon to the game.
- Press 'q' to quit the game.
Code ExplanaƟon
Constants
- `RABBIT`, `CARROT`, `RABBIT_HOLE`, `PATHWAY_STONE`, and `HOLDING_CARROT`
represent different elements in the game grid.
Movements
- `MOVES` is a list of possible movements for the rabbit: leŌ, right, up, and down.
GeneraƟng the Map
- `generate_map` creates a random game map with a rabbit, carrots, and rabbit holes. It
places these elements randomly on the grid.
Displaying the Grid
- `display_grid` is used to render and display the game grid to the user in the console.
CalculaƟng ManhaƩan Distance
- `manhaƩan_distance` calculates the ManhaƩan distance between two points on the grid,
which is used in pathfinding algorithms.
Finding Shortest Path
- `find_shortest_path` employs the A* algorithm to find the shortest path between two
points on the game grid. This algorithm is crucial for determining opƟmal moves for the
rabbit.
Playing the Game
- `play_game` handles the main gameplay logic. It allows the user to control the rabbit's
movements, pick up carrots, and reach rabbit holes to win the game.
Showing the SoluƟon
- The `show_soluƟon` funcƟon is an extra feature that demonstrates the opƟmal soluƟon to
the game using a path-finding algorithm. It visualizes the rabbit's path to success.
By following these explanaƟons, you can understand the various components and mechanics
of the Rabbit and Carrot Game. 

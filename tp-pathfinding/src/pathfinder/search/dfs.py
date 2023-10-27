from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        #explored[node.state] = True
        
        # Creo frontier utilzando una pila
        frontier = StackFrontier()
        
        # Agrego el nodo a la frontier
        frontier.add(node)

        while True:
        
            if frontier.is_empty():
                return NoSolution(explored)
            
            node = frontier.remove()

            # Verifico si el nodo es el estado objetivo
            if node.state == grid.end:
                return Solution(node, explored)

            if node.state not in explored.keys():
                explored[node.state] = True

                # Exploro los neighbors
                neighbours = grid.get_neighbours(node.state)

                for action in neighbours.keys():
                    new_state = neighbours[action]
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = action

                    if new_node not in explored:
                        frontier.add(new_node)

        return NoSolution(explored)        
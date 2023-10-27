from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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
        explored[node.state] = True
        
        # Verifico si el nodo es el estado objetivo
        if node.state == grid.end:
            return Solution(node, explored)
        
        # Creo frontier utilzando una cola
        frontier = QueueFrontier()
        
        # Agrego el nodo a la frontier
        frontier.add(node)

        while True:
        
            if frontier.is_empty():
                return NoSolution(explored)
            
            node = frontier.remove()

            explored[node.state] = True
            
            # Exploro los neighbours
            neighbours = grid.get_neighbours(node.state)

            for action in neighbours.keys():
                new_state = neighbours[action]
                new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                new_node.parent = node
                new_node.action = action
            
                if new_node.state == grid.end:
                    return Solution(new_node, explored)

                if new_node.state not in explored:
                # Marco el nuevo estado como ya explorado
                    explored[new_node.state] = True
                # Agrego el nuevo nodo a la frontier para seguir buscando
                    frontier.add(new_node)

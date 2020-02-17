
from mcts_node import MCTSNode
from random import choice
from math import sqrt, log

num_nodes = 1000
explore_faction = 2.

def traverse_nodes(node, board, state, identity):
    """ Traverses the tree until the end criterion are met.

    Args:
        node:       A tree node from which the search is traversing.
        board:      The game setup.
        state:      The state of the game.
        identity:   The bot's identity, either 'red' or 'blue'.

    Returns:        A node from which the next stage of the search can proceed.

    """
    current_node = node
  #  print("current_node.children length:       ", len(current_node.child_nodes))
    while len(current_node.child_nodes) != 0:
        if len(current_node.untried_actions) > 0:
            return current_node
        current_node = best_ucb(node,board,state,identity)
        print("current_node found")
    return current_node
    


def expand_leaf(node, board, state):
    """ Adds a new leaf to the tree by creating a new child node for the given node.

    Args:
        node:   The node for which a child will be added.
        board:  The game setup.
        state:  The state of the game.

    Returns:    The added child node.

    """
    pass
    # Hint: return new_node


def rollout(board, state):
    """ Given the state of the game, the rollout plays out the remainder randomly.

    Args:
        board:  The game setup.
        state:  The state of the game.

    """
    pass


def backpropagate(node, won):
    """ Navigates the tree from a leaf node to the root, updating the win and visit count of each node along the path.

    Args:
        node:   A leaf node.
        won:    An indicator of whether the bot won or lost the game.

    """
    pass


def think(board, state):
    """ Performs MCTS by sampling games and calling the appropriate functions to construct the game tree.

    Args:
        board:  The game setup.
        state:  The state of the game.

    Returns:    The action to be taken.

    """
    identity_of_bot = board.current_player(state)
    root_node = MCTSNode(parent=None, parent_action=None, action_list=board.legal_actions(state))
    print("wode haiziL:  ", len(root_node.child_nodes))
    print("-----------------------------------------------------")

    for step in range(num_nodes):
        # Copy the game for sampling a playthrough
        sampled_game = state

        # Start at root
        node = root_node
       # print(" root的childrenß", len(node.child_nodes))

        # Do MCTS - This is all you!
        node = traverse_nodes(node,board,sampled_game,identity_of_bot)
       # print(" 我是childnode：", node.child_nodes)
    # Return an action, typically the most frequently used action (from the root) or the action with the best
    # estimated win rate.
    return choice(board.legal_actions(state))
    # make a best choice with maxium ucb values
    def best_ucb(node,board,state,identity):
        print("best_ucb")
        # a dictionary to store ucb values for children
        ucbs = {}
        for child in node.child_nodes.value():
            #check identity
            win_rate = child.wins/child.visits if identity == board.current_player(state) else 1 - child.wins/child.visits 
            ucbs[child] = win_rate + explore_faction * sqrt(log(child.parent)/child.visits)
        best_child = max(ucbs, key = ucbs.get)
        return best_child

   #     pass
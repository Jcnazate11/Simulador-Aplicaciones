from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Algoritmo de poda alpha-beta
def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.get_children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.get_children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children else []

    def is_terminal(self):
        return not self.children

    def get_children(self):
        return self.children

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json
    root = Node(data['value'], [Node(child['value'], [Node(gc['value']) for gc in child['children']]) for child in data['children']])
    result = alpha_beta_pruning(root, data['depth'], float('-inf'), float('inf'), True)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

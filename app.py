from flask import Flask, render_template, request, jsonify
import ast
from models.code_simplifier import CodeSimplifier

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simplify', methods=['POST'])
def simplify_code():
    data = request.get_json()
    code = data.get('code')

    simplified_code = simplify_python_code(code)
    return jsonify({'simplified_code': simplified_code})

def simplify_python_code(code):
    tree = ast.parse(code)
    simplified_tree = CodeSimplifier().visit(tree)
    ast.fix_missing_locations(simplified_tree)
    return ast.unparse(simplified_tree)

if __name__ == "__main__":
    app.run(debug=True)

import ast

class CodeSimplifier(ast.NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node.value, ast.BinOp):
            if isinstance(node.value.op, ast.Add) and isinstance(node.value.right, ast.Constant) and node.value.right.value == 0:
                return None  # Remove assignment (a = a + 0)
            if isinstance(node.value.op, ast.Mult) and isinstance(node.value.right, ast.Constant) and node.value.right.value == 1:
                node.value = node.value.left  # Simplify x = y * 1 to x = y
        return node

    def visit_If(self, node):
        if isinstance(node.test, ast.Constant):
            if node.test.value:  # if True:
                return node.body  # Keep only body
            else:  # if False:
                return None  # Remove the block
        return node

    def visit_Expr(self, node):
        if isinstance(node.value, ast.BinOp):
            if isinstance(node.value.left, ast.Name) and isinstance(node.value.right, ast.Name):
                if node.value.left.id == node.value.right.id:  # x = x
                    return None  # Remove
        return node

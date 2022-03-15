# https://stackoverflow.com/questions/5910703/how-to-get-all-methods-of-a-python-class-with-given-decorator


from functools import wraps
def g_flag(func):
    @wraps(func)
    def wrap_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrap_func


@g_flag
def f(a: str, b, c = 123, d: dict = {}):
    print('hi')


# 方法1： inspect解析源码
def parse_source(func):
    import inspect
    # 获取参数信息
    # sig = inspect.signature(f)
    # parm = sig.parameters
    # print(parm)

    # 获取源码
    src_lines = inspect.getsourcelines(f)
    print(src_lines)


# 方法2： ast + inpsect
def find_decorator(func):
    # ast: 抽象语法树
    import ast, inspect
    res = {}
    def visit_FunctionDef(node):
        # 获取参数，或其它
        # print(dir(node))
        # print('##', node.args.args)
        # print('##', [ast.dump(e) for e in node.args.args])
        # 获取装饰器
        res[node.name] = [ast.dump(e) for e in node.decorator_list]
    V = ast.NodeVisitor()
    V.visit_FunctionDef = visit_FunctionDef
    V.visit(compile(inspect.getsource(func), '?', 'exec', ast.PyCF_ONLY_AST))
    return res


parse_source(f)
print('------')
print(find_decorator(f))


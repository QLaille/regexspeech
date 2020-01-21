import get_speech
import build_ast
import json
import os
from grako.util import asjson
from grako import parse

dir_path = os.path.dirname(os.path.realpath(__file__))

jsons = build_ast.get_json_files()

tokens, nodes, funcs = build_ast.group_json_by_keys(jsons)

ast = build_ast.build_ast(tokens, nodes)

#text = get_speech.get_speech()

request = 'match a single character of a b c end of match'

resp = parse(ast, request)

json_ast = asjson(resp)

print(json.dumps(json_ast, indent=2))

regex = '/'
for token in json_ast:
	key, value = list(token.items())[0]
	expr = funcs[key]
	regex += eval(expr, {'__builtins__': {'tokens': token[key][0],'str':str}})
regex += '/'
print(regex)


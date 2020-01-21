import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

import pprint
import json
import os

def get_json_files():
	array = []
	for file in os.listdir(dir_path + '/tokens/'):
		with open(dir_path + '/tokens/' + file, 'r') as f:
			array.append(json.load(f))
	return (array)

def group_json_by_keys(jsons):
	ast_tokens = []
	ast_nodes = {}
	ast_nodes_funcs = {}
	for json in jsons:
		ast_tokens.append(json['token_name'])
		ast_nodes[json['token_name']] = json['token_ast']
		ast_nodes_funcs[json['token_name']] = json['token_fct']
	return ast_tokens, ast_nodes, ast_nodes_funcs

def build_ast(tokens, nodes):
	ast = "@@grammar::VoiceRegex\nstart =  request $;\nrequest = 'match' @+:common { 'and' @+:common }* 'end of match';\n"
	ast += 'common = \n'
	for name in tokens:
		ast += '| ' + name + "\n"
	ast += ';\n'
	for node in nodes:
		ast += nodes[node] + "\n"
	ast += "character_range = letter 'dash' letter;\ncharacters = { letter }+ ;\ncharacter = letter ;letter = /[a-z]\s/;\n"
	return (ast)

dir_path = os.path.dirname(os.path.realpath(__file__))

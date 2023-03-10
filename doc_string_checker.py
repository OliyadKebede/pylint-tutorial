from pylint.checkers import BaseTokenChecker
from pylint.interfaces import IAstroidChecker , ITokenChecker
import tokenize

class TripleDoubleStringChecker(BaseTokenChecker):
    __implements__ =  ( IAstroidChecker , ITokenChecker )
    name = 'invalid-module-string-quote'
    msgs = {
            'C1111' : (
                'Invalid string quote ',
                'invalid-module-string-quote',
                'Used when the string quote character does not match the'
                'value triple double string'
                ),
            }
    _string_tokens = {}

    def process_tokens( self , tokens):
        for (tok_type, token, (start_row , _), _, _) in tokens:
            if tok_type == tokenize.STRING:
                token_text = token.strip('"').strip("'")
                self._string_tokens[token_text] = ( token , start_row )

    def visit_module(self, node):
        self._check_docstring(node)

    def visit_classdef(self, node):
        self._check_docstring(node)

    def visit_functiondef(self, node):
        self._check_docstring(node)

    def _check_docstring( self , node):

        if node.doc in self._string_tokens:
            token , row = self._string_tokens[node.doc]
            if not token.startswith('"""'):
                self.add_message('invalid-module-string-quote', line = row )
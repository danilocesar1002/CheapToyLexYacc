from mylexer import Lexer

class Parser:
    def __init__(self, rules):
        self.lexer = Lexer(rules["tokens"])

        self.currentToken = None
        self.lookAhead = None
    
    def advanceTokens(self):
        self.currentToken = self.lookAhead
        self.lookAhead = self.lexer.nextToken()
    
    def parse(self, expr):
        pass # TODO

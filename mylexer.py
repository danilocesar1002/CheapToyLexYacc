from re_to_nfa import (
    AbstractLexer,
    NFAUnionFromREs,
    Token
)

class Lexer(AbstractLexer):
    def __init__(self, tokens):
        super().__init__(tokens)
        
        self.nfa = NFAUnionFromREs(self.tokens)
        
    def nextToken(self):
        if self.currentChar == None:
            return Token(
                "EOF",
                ""
            )
        stringStart = self.index - 1
        stringEnd = None
        acceptingState = None
        
        states = self.nfa.epsilonClosure([self.nfa.initial])

        while states != []:
            states = self.nfa.epsilonClosure(self.nfa.move(states, self.currentChar))
            
            accepting = [state for state in states if state in self.nfa.accepting]
            if len(accepting) > 0:
                acceptingState = min(accepting)
                stringEnd = self.index
            
            self.nextChar()
        
        if acceptingState == None:
            
            if stringStart == self.index - 1:
                stringEnd = self.index
            else:
                stringEnd = self.index - 1
            
            res = Token(
                "ILLEGAL",
                self.str[stringStart : stringEnd]
            )
        else:
            self.index = stringEnd
            self.nextChar()
            res = Token(
                self.nfa.accepting[acceptingState],
                self.str[stringStart : stringEnd]
            )

        return res

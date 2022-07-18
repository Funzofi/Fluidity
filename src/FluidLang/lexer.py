from token import Token
import tokens

class Lexer(object):
    def __init__(self, source):
        self.source = source
        self._tokens = []

    @property
    def tokens(self):
        if len(self._tokens) == 0:
            for char in self.source:
                if char in tokens.operator.keys():
                    self._tokens.append(Token("OPERATOR", tokens.operator[char]))
                elif char in tokens.alphabet.keys():
                    self._tokens.append(Token("ALPHABET", tokens.alphabet[char]))
                elif char in tokens.number.keys():
                    self._tokens.append(Token("NUMBER", tokens.number[char]))
                elif char in tokens.keyword.keys():
                    self._tokens.append(Token("KEYWORD", tokens.keyword[char]))
                elif char in tokens.symbol.keys():
                    self._tokens.append(Token("SYMBOL", tokens.symbol[char]))
                elif char == '\n':
                    self._tokens.append(Token("NEWLINE", char))
                elif char == ' ':
                    self._tokens.append(Token("WHITESPACE", char))
                elif char == '\t':
                    self._tokens.append(Token("TAB", char))
                else:
                    self._tokens.append(Token("UNKNOWN", char))
        
        return self._tokens
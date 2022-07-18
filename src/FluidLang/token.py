class Token(object):
    def __init__(self, tokentype, value):
        self.token_type = tokentype
        self.value = value

    def __str__(self):
        return 'Token({}, {})'.format(self.token_type, self.value, self.line, self.col)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.token_type == other.token_type and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)
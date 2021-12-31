class test:
    def __init__(self):
        self.word = 'word'
        self._protect_word = 'protect'
        self.__private_word = 'private'
    def getPrivate(self):
        return self.__private_word
    def getProtect(self):
        return self._protect_word

t = test()
print(t.word)
print(t._protect_word)
print(t.getPrivate())
print(t.__private_word)

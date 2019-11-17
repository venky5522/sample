class SeeMee:
    def youcanseemee(self):
        return "you can see mee"
    def __youcantseemee(self):
        return "you cant see mee"
p = SeeMee()
print(p.youcanseemee())
print(p._SeeMee__youcantseemee())
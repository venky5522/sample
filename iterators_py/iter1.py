class my_number:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x = self.a
        self.a+=1
        return x
p = my_number()
it =iter(p)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
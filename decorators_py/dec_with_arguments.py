def retry(n):
    print("Decorator to perform retries")
    def inside(fn):
        def inner():
            for i in range(n):
                fn()
        return inner
    return inside
@retry(5)
def hello():
    print("decorated function")
hello()







import sys
def test_splat(car = "audi", yearsold = 20):
    """document string"""
    print(f"{car} and {yearsold}")


if __name__ == "__main__":
    dict_per = {
        "yearsold": 19,
        "car": "mers"
    }
    person = ["David"]
    print(test_splat.__doc__)
    # print(**dict_per)
    a = ['mot', 'hai', 'ba', 'chin']
    b = ['nam', 'sau', 'bay', 'tam']
    c = {}
    for i, j in zip(a, b):
        c[i] = j
    print(c)

    for i in dir(sys):
        print(i)
    class Myclass:
        """this is document"""
        i = 123
        def f(self):
            print('my self')
    x = Myclass()
    print(type(Myclass.f))
    print(type(x.f))
    # print(type(help('modules')))
    wordnum = 5
    for k in range(1, wordnum + 1):
        print(k)
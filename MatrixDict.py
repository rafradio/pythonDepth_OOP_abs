from Matrix import BaseDict

class MatrixDict(BaseDict):
    """Матрица имеет следующий вид: """

    def __init__(self, rows=None, columns=None, digits=None, myArr=None):
        self.rows, self.columns, self.digits = rows, columns, digits
        self.myArr = []
        # self.__doc__ = "Матрица имеет следующий вид"
        if myArr: 
            self.myArr = myArr
        else:      
            self.create()
        super().__init__(self.myArr, rows = rows, columns = columns)
        # print(self.__getitem__((2,2)))

    def create(self):
        for i in range(self.rows):
            self.myArr += [(i+1, j+1, self.digits) for j in range(self.columns)]

    def __add__(*matrices):
        addFunc = lambda a, b: a + b
        c = []
        for i in range(matrices[0].rows):
            c += [*[(i+1, j+1, addFunc(*[m[i+1, j+1] for m in matrices])) for j in range(matrices[0].columns)]]
            # for j in range(matrices[0].columns):
            #     c.append((i+1, j+1, addFunc(*[m[i+1, j+1] for m in matrices])))

        return MatrixDict(matrices[0].rows, matrices[0].columns, 0, c)
    
    def __mul__(self, other):
        c = []
        for i in range(self.rows):
            for j in range(other.columns):
                v = 0
                for elm in range(other.rows):
                    v += self[i+1, elm+1] * other[elm+1, j+1]
                c.append((i+1, j+1, v))
        return MatrixDict(self.rows, other.columns, 0, c)

    
    def __str__(self):
        txt = self.__doc__ + '\n'
        return txt + super().__str__()

     
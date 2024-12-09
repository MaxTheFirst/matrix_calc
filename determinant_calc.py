import numpy


class DeterminantCalc():
    @staticmethod
    def get_matrix_minor(array, i, j):
        return numpy.delete(numpy.delete(array, i, axis=0), j, axis=1)

    @staticmethod
    def get_determinat33(array: numpy.ndarray):
        if len(array) != 3 or len(array[0]) != 3:
            raise Exception("Shape is illegal!")
        for i in range(3):
            minor = DeterminantCalc.get_matrix_minor(array, 0, i)
            yield (
                array[0][i],
                minor,
                numpy.linalg.det(minor)
            )

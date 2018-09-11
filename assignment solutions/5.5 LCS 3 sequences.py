# python3
import numpy
                                    
def LCS3(s1, s2, s3, n1, n2, n3):
    """ Finds the length of the longest common subsequence of three strings
    (str, str, str, int, int, int) -> (int, 3D-array) """

    # Initializing the matrix
    Matrix = numpy.zeros((n1+1 , n2+1, n3+1))

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            for k in range(1, n3+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    Matrix[i][j][k] = Matrix[i-1][j-1][k-1] + 1
                else:
                    Matrix[i][j][k] = max(Matrix[i-1][j][k], Matrix[i][j-1][k], Matrix[i][j][k-1])
    
    return (int(Matrix[-1][-1][-1]), Matrix)

def printSubsequence(Matrix, s1, s2, s3, i, j, k, seq):
    """ Returns the longest common subsequence of three strings
    (3D-array, str, str, str, int, int, int, str) -> (str) """
    if i == 0 or j == 0 or k == 0:
        # If inputs for s1, s2 are strings uncomment below line
        if seq == []: return None
        else : return ''.join(seq[::-1])

        # If inputs for s1, s2 are numbers uncomment below line. 
        # return ' '.join([str(i) for i in seq][::-1])

    if s1[i-1] == s2[j-1] == s3[k-1]:
        seq.append(s1[i-1])
        return printSubsequence(Matrix, s1, s2, s3, i-1, j-1, k-1, seq)
    
    if Matrix[i-1][j][k] > Matrix[i][j-1][k]:
        if Matrix[i-1][j][k] > Matrix[i][j][k-1]:
            return printSubsequence(Matrix, s1, s2, s3, i-1, j, k, seq)
        else:
            return printSubsequence(Matrix, s1, s2, s3, i, j, k-1, seq)
    else:
        if Matrix[i][j-1][k]> Matrix[i][j][k-1]:
            return printSubsequence(Matrix, s1, s2, s3, i, j-1, k, seq)
        else:
            return printSubsequence(Matrix, s1, s2, s3, i, j, k-1, seq)

if __name__ == '__main__':
    n1, s1, n2, s2, n3, s3 = int(input()), input(), int(input()), input(), int(input()), input()

    # If inputs for s1, s2, s3 are numbers uncomment below line. 
    # s1, s2, s3 = [int(i) for i in s1.split()], [int(i) for i in s2.split()],  [int(i) for i in s3.split()]

    LCS_length, Matrix = LCS3(s1, s2, s3, n1, n2, n3)
    print('Length of LCS:', LCS_length)
    sequence = printSubsequence(Matrix, s1, s2, s3, n1, n2, n3, [])
    print('LCS:', sequence)
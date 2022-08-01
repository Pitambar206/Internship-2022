# You are given an integer,N . Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.) 


def print_rangoli(size):
    import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(L[:0:-1]+L))

if __name__ == '__main__':
    n = int(input())
    print_rango
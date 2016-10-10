def get_bandwidth(data):
    """
    Calculates bandwidth for the Exxx case, taken from statistics.c,
    http://bonsai.hgc.jp/~mdehoon/software/python/Statistics/
    """
    import numpy as np
    lendata = len(data)
    if lendata <= 1.0:
        print("Not enough data.")
        return -1.0
    std = np.std(lendata)
    bandwidth = std*(80/(lendata*2*(1/np.pi())**0.5)**0.2)
    return bandwidth

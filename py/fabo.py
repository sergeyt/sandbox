import cProfile

def fabo(n):
    if n < 2:
        return n
    return fabo(n-1) + fabo(n-2)

def fabo_dp(n):
    result = [0, 1]

    def fabo_dp_internal(n):
        if len(result) >= n:
            return result[n-1]
        result.append(fabo_dp_internal(n-1) + fabo_dp_internal(n-2))
        return result[n-1]

    return fabo_dp_internal(n)

if __name__ == '__main__':
    cProfile.run('print fabo(30)')
    cProfile.run('print fabo_dp(30)')

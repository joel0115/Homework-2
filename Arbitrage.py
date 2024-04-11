import deepcopy from copy

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

Bmax = -1
pathMax = ""

def getAmountOut(amountIn, reserveIn, reserveOut):
    amountOut = 997*amountIn*reserveOut / (1000*reserveIn + 997*amountIn)
    return amountOut

def dfs(liq, maxPathLen, curToken, curVal, endToken, path):
    if(curToken == endToken and len(path) != 1):
        if(Bmax < curVal):
            Bmax = curVal
            pathMax = path
            return
        if(len(path) > maxPathLen):
            return





if __name__ == '__main__':
    liq = deepcopy(liquidity)
    
    dfs(liq, 10, 'B', 5, 'B', "B")

    print()
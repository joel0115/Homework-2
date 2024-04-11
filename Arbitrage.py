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

def dfs(liq, curPathlen, maxPathLen, curToken, curVal, endToken, path):
    global Bmax
    global pathMax
    if(curToken == endToken and curPathlen != 1):
        if(Bmax < curVal):
            Bmax = curVal
            pathMax = path
            return
        if(curPathlen > maxPathLen):
            return

    for (token0, token1), (reserve0, reserve1) in liq.items():
        if(f"{token0}->{token1}" in path or f"{token1}->{token0}" in path):
                continue
        if token0 == curToken:
            amountOut = getAmountOut(curVal, reserve0, reserve1)
            liq[(token0,token1)] = (reserve0+curVal, reserve1-amountOut)
            dfs(liq, curPathlen+1, maxPathLen, token1, amountOut, endToken, path+"->"+token1)
            liq[(token0,token1)] = (reserve0, reserve1)
        elif token1 == curToken:
            amountOut = getAmountOut(curVal, reserve1, reserve0)
            liq[(token0,token1)] = (reserve0-amountOut, reserve1+curVal)
            dfs(liq, curPathlen+1, maxPathLen, token0, amountOut, endToken, path+"->"+token0)
            liq[(token0,token1)] = (reserve0, reserve1)




if __name__ == '__main__':
    dfs(liquidity, 1, 6, 'tokenB', 5, 'tokenB', "tokenB")

    print(f"path: {pathMax}, tokenB balance={Bmax}")
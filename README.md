# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

path: tokenB->tokenA->tokenC->tokenE->tokenD->tokenC->tokenB

ether: 5000000000000000000 -> 5655321988655321988 -> 2372138936383089007 -> 1530137136963616993 -> 3450741448619708083 -> 6684525579572586452 -> 22497221806974138089
 
Token B balance: 22.49722180697414
## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage: 由於 volatility 和 交易量 與 chain 的處理速度等原因，導致交易預計的價格與實際價格產生落差。

For example, Uniswap V2 provides a function _SwapExactTokensForTokens_:
```=
function swapExactTokensForTokens(
  uint amountIn,
  uint amountOutMin,
  address[] calldata path,
  address to,
  uint deadline
) external returns (uint[] memory amounts);
```

The argument _amountOutMin_ can be passed by user and indicate at least how many token should he/she gets.

And hence, we can control the slippage rate by this and the similar functions.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

According to [Uniswap v2 Core white paper](https://uniswap.org/whitepaper.pdf)

The value of a liquidity pool share to grow over time, either by accumulating trading fees or through “donations” to the liquidity pool.

In theory, this could result in a situation where the value of the minimum quantity of liquidity pool shares (1e-18 pool shares) is worth so much that it becomes infeasible for small liquidity providers to provide any liquidity. To mitigate this, Uniswap v2 burns the first 1e-15 (0.000000000000001) pool shares that are minted (1000 times the minimum quantity of pool shares), sending them to the zero address instead of to the minter.

This should be a negligible cost for almost any token pair.But it dramatically increases the cost of the above attack. In order to raise the value of a liquidity pool share to $100, the attacker would need to donate $100,000 to the pool, which would be permanently locked up as liquidity

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
The formula: liquidity = Math.min(amount0.mul(_totalSupply) / _reserve0, amount1.mul(_totalSupply) / _reserve1);

可以鼓勵 liquidity provider 提供相同比例的 token (因為能獲得的 liquidity 取決於提供比例較少之 token)，以維持 pool 內 token 的平衡

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

Sandwich attack: 

假設我今天要用 tokenX 換取 tokenY，這筆交易會導致 tokenY 的價格上升，

因此若有攻擊者搶先知道這筆交易的資訊，他就可以搶先 (透過提高 gas fee) 用原始價格購買 tokenY，使 tokenY 的價格上升。此時在我的交易被處理時，我就會以較高的價格購買 Y 產生損失。

更進一步，由於我的購買，導致 tokenY 又更進一步上升，此時攻擊者就可以再賣出他先前購得的 Y 來賺取價差。


# 당신은 주식투자자로서 많은 수익을 내고 싶다.
# 많은 수익을 내는 방법은 주식이 가장 쌀 때 주식을 사서
# 가장 비쌀 때 파는 것이다.
# 시간순으로 주식 가격들이 주어졌을 때 최대 수익을 내기 위해
# 주식을 살 시점과 주식을 팔 시점을 구하시오.
#
# input:  주식 가격을 나타내는 정수 리스트. 리스트의 순서는 시간을
#         나타낸다.
# output: 주식 가격을 살 시점과 팔 시점 (index)의 정수 쌍 (pair).
#         정수쌍의 첫번째 원소는 살 시점, 두번째 원소는 팔 시점을
#         나타낸다.

def find_trading_points(stock_prices):
    # TODO: implement this
    a = 0
    b = 0
    return (a, b)

def main():
    stock_prices = [8, 3, 7, 9, 2, 4, 7, 2, 7, 0, 5, 2, 1, 6, 8, 9, 4, 8]
    print(find_trading_points(stock_prices))

if __name__ == "__main__":
    main()

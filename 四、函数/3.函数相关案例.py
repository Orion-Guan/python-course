"""
一、计算!N的阶乘(递归: 从递推---->获取到结果----->递归，必须有结束条件。)
！10 = 10 * ！9
！9 = 9 * ！8
.。。
！2 = 2 * ！1
!1 = 1
"""

# def getJc(num):
#     if num == 1:
#         return 1
#     return num * getJc(num - 1)
#
#
# print(getJc(10))



"""
二、模拟计算购物车计算器
要求:
1、优惠券只能满200才能使用，优惠的金额不能超过商品总金额
2、使用门槛商品总金额必须满500元，兑换后的扣减钱数不能超过商品总金额; 每100个积分兑换1块钱，不足100积分的部分失效不会产生兑换的钱数。
"""


def getCartAmount(*args, coupon=0.0, score=0, express=0.0):
    """
    计算购物车结算总金额
    :param args: 各商品信息
    :param coupon: 优惠券
    :param score: 积分
    :param express: 邮费
    :return: 最终结算金额
    """
    # 计算商品总额
    good_amount = (good[1] * good[2] for good in args)
    total_amount = sum(good_amount)

    # 扣减优惠券
    if 200 <= total_amount >= coupon:
        total_amount -= coupon

    # 积分抵扣
    if total_amount >= 500 and score // 100 <= total_amount:
        total_amount -= score // 100

    # 计算运费
    total_amount += express

    # 返回结算后的总金额
    return round(total_amount, 2)


amount = getCartAmount(("电脑", 5999, 1), ("鼠标", 36, 1), ("显示器", 2344, 1), coupon=300, score=256, express=9.99)
print(amount)



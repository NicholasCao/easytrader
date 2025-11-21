# easytrader

修复聚宽跟单bug，增加了市价跟单的功能。

## DEMO
```python
# https://easytrader.readthedocs.io/zh-cn/master/miniqmt/
import easytrader

user = easytrader.use('miniqmt')

user.connect(
    miniqmt_path=r"D:\Apps\国金证券QMT交易端\userdata_mini",  # QMT 客户端下的 miniqmt 安装路径
    stock_account="xxx"  # 资金账号
)

print(user.balance)
# user.buy('600036', price=35.5, amount=10)

target = 'jq'  # joinquant
follower = easytrader.follower(target)
follower.login(user='***', password='***')

follower.follow(
    user,
    'https://www.joinquant.com/algorithm/live/index?backtestId=xxx', # 聚宽模拟盘url
    # trade_cmd_expire_seconds=100000000000, # 默认处理多少秒内的信号，用于调试
    # cmd_cache=False, # 是否读取已经执行过的命令缓存，以防止重复执行，用于调试
    entrust_prop="market" # market市价单, limit限价单
)
```

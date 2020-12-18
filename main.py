import json
import requests
from mov_sdk.key import xprv_my_sign, get_xpub
from mov_sdk.mov_api import MovApi

baseUrl = "https://supertx.movapi.com"
api = MovApi(secret_key="")
config = api.init_from_mnemonic("scatter afraid balcony pen exercise bulk sign skate category gloom clown wool")


# print(api.main_address)
# print(api.vapor_address)
# print(api.public_key)


# 获取所有交易对信息
def get_symbols():
    url = baseUrl + "/v1/symbols"
    res = requests.get(url)
    print(res.json())


# 获取兑换汇率
def get_exchange_rate(symbol, amount, side):
    url = baseUrl + "/v1/exchange-rate?symbol={}&amount={}&side={}".format(symbol, amount, side)
    res = requests.get(url)
    res = res.json()
    print(res)
    return res["data"]["exchange_rate"]


# 创建兑换请求
def bulid_exchange_request(address, symbol, amount, side):
    param = {
        "symbol": symbol,
        "amount": amount,
        "side": side,
        "exchange_rate": get_exchange_rate(symbol, amount, side)
    }

    url = baseUrl + "/v1/build-exchange-request?address={}".format(address)
    encoded_data = json.dumps(param).encode('utf-8')
    res = requests.post(url, encoded_data)
    res = res.json()
    print(res)

    return res["data"]


# 提交兑换请求
def submit_exchange_request(address, data):
    res = []
    url = baseUrl + "/v1/submit-exchange-request?address={}".format(address)

    for info in data:
        params = api.mov_sign(info)

        encoded_data = json.dumps(params).encode('utf-8')
        resp = requests.post(url, encoded_data)
        print(resp.json())
        res.append(resp)

    return res


# 查询兑换历史记录
def exchange_order_history(address, start="0", limit="20"):
    url = baseUrl + "/v1/exchange-order-history?address={}&start={}&limit={}".format(address, start, limit)
    res = requests.get(url)
    print(res.json())


# 储蓄池当前信息
def pool_info():
    url = baseUrl + "/v1/pool-info"
    res = requests.get(url)
    print(res.json())


# 获取某个流动性池的资产比例
def asset_proportion(symbol):
    url = baseUrl + "/v1/asset-proportion?symbol={}".format(symbol)
    res = requests.get(url)
    res = res.json()
    print(res)
    return res["data"]


# 构建双币转入
def build_multi_asset_deposit(address, symbol, quantity_proportion, amount):
    url = baseUrl + "/v1/build-multi-asset-deposit?address={}".format(address)
    param = {
        "symbol": symbol,
        "quantity_proportion": quantity_proportion,
        "amount": amount
    }
    encoded_data = json.dumps(param).encode('utf-8')
    res = requests.post(url, encoded_data)
    res = res.json()
    print(res)

    return res["data"]


# 构建单币转入
def build_single_asset_deposit(address, symbol, amount, currency):
    url = baseUrl + "/v1/build-single-asset-deposit?address={}".format(address)
    param = {
        "symbol": symbol,
        "amount": amount,
        "currency": currency
    }
    encoded_data = json.dumps(param).encode('utf-8')
    res = requests.post(url, encoded_data)
    res = res.json()
    print(res)

    return res["data"]


# 提交转入
def submit_deposit(address, data):
    res = []
    url = baseUrl + "/v1/submit-deposit?address={}".format(address)

    for info in data:
        params = api.mov_sign(info)
        encoded_data = json.dumps(params).encode('utf-8')
        resp = requests.post(url, encoded_data)
        print(resp.json())
        res.append(resp)

    return res


# 双资产移除流动性
def submit_multi_asset_withdrawal(address, symbol, amount):
    params = {
        "pubkey": get_xpub(api.secret_key),
        "symbol": symbol,
        "quantity_proportion": asset_proportion(symbol),
        "amount": amount,
        "time_stamp": api.generate_timestamp()
    }
    data = json.dumps(params).replace(' ', '').encode('utf-8')
    signature_data = xprv_my_sign(api.secret_key, data)
    url = baseUrl + "/v1/submit-multi-asset-withdrawal?signature={}&address={}".format(signature_data, address)
    encoded_data = json.dumps(params).encode('utf-8')

    res = requests.post(url, encoded_data)
    print(res.json())


# 单资产移除流动性
def submit_single_asset_withdrawal(address, symbol, amount, currency):
    params = {
        "pubkey": get_xpub(api.secret_key),
        "symbol": symbol,
        "amount": amount,
        "time_stamp": api.generate_timestamp(),
        "currency": currency,
    }
    data = json.dumps(params).replace(' ', '').encode('utf-8')
    signature_data = xprv_my_sign(api.secret_key, data)
    print(params)
    print(signature_data)
    url = baseUrl + "/v1/submit-single-asset-withdrawal?signature={}&address={}".format(signature_data, address)
    encoded_data = json.dumps(params).encode('utf-8')
    res = requests.post(url, encoded_data)
    print(res.json())


# 获取用户收益
def user_earning(address):
    url = baseUrl + "/v1/user-earning?address={}".format(address)
    res = requests.get(url)
    print(res.json())


# 获取年化收益率
def annual_rate():
    url = baseUrl + "/v1/annual-rate"
    res = requests.get(url)
    print(res.json())


# 获取多资产可用信息
def multi_asset_available(address):
    url = baseUrl + "/v1/multi-asset-available?address={}".format(address)
    res = requests.get(url)
    print(res.json())


# 获取单资产可用信息
def single_asset_available(address):
    url = baseUrl + "/v1/single-asset-available?address={}".format(address)
    res = requests.get(url)
    print(res.json())


# 获取同步状态信息
def chain_status():
    url = baseUrl + "/v1/chain-status"
    res = requests.get(url)
    print(res.json())


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 获取所有交易对信息
    get_symbols()

    # 获取指定交易对和方向的兑换汇率
    # symbol = "SUP/BTM"
    # amount = "12"
    # side = "buy"
    # get_exchange_rate(symbol, amount, side)

    # 创建并提交兑换订单
    # symbol = "SUP/BTM"
    # amount = "12"
    # side = "buy"
    # data = bulid_exchange_request(api.vapor_address, symbol, amount, side)
    # submit_exchange_request(api.vapor_address, data)

    # 查询历史兑换记录
    # exchange_order_history(api.vapor_address, start="0", limit="1")

    # 存储池当前信息
    # pool_info()

    # 双资产转入流动性池
    # symbol = "SUP/BTM"
    # amount = "0.003"
    # proportion = asset_proportion(symbol)
    # data = build_multi_asset_deposit(api.vapor_address, symbol, proportion, amount)
    # submit_deposit(api.vapor_address, data)

    # 单资产转入流动性池
    # symbol = "USDC/USDT"
    # amount = "0.15"
    # currency = "USDT"
    # data = build_single_asset_deposit(api.vapor_address, symbol, amount, currency)
    # submit_deposit(api.vapor_address, data)

    # 双资产移除流动性
    # symbol = "SUP/BTM"
    # amount = "0.003"
    # submit_multi_asset_withdrawal(api.vapor_address, symbol, amount)

    # 单资产移除流动性
    # symbol = "USDC/USDT"
    # amount = "0.1"
    # currency = "USDT"
    # submit_single_asset_withdrawal(api.vapor_address, symbol, amount, currency)

    # 查看收益
    # user_earning(api.vapor_address)

    # 获取年化收益率
    # annual_rate()

    # 获取多资产可用信息
    # multi_asset_available(api.vapor_address)

    # 获取单资产可用信息
    # single_asset_available(api.vapor_address)

    # 获取同步状态信息
    # chain_status()

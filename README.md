# SuperTxDemo

基于Python3编写的超导兑换API使用Demo

## 目录

1. [总览](#chapter-001)
2. [工具安装](#chapter-002)
3. [方法简述](#chapter-003)
4. [API文档](#chapter-004)

## 总览<a id="chapter-001"></a>

SuperTxDemo的目标是帮助用户更轻松的使用超导兑换API，封装了一些用户自己难以完成的工作，例如本地签名。用户可以轻松在Demo的基础上根据个人需求进行代码改造。

## 工具安装<a id="chapter-002"></a>

使用SuperTxDemo需要安装一些列工具。如果您还没有这些要求，则应通过安装以下方法解决此问题：

**Python**  MOV-MMDK是基于MOV Server的RESTful API开发的Python SDK，使用前请确保在你有 **Python 3 开发环境**。本教程所有过程使用的版本为 Python 3.9.0 

**MOV-MMDK**  MOV Market Maker Develo pment Kit，基于MOV Server的RESTful API开发的Python SDK。虽然本教程Demo演示的过程中采用requests包中的方法调用API，但仍然需要MMDK的部分方法完成本地签名。

```python
git clone https://github.com/Bytom/mov-mmdk 
cd mov-mmdk/ 
pip3 install -r requirements.txt 
python3 setup.py install
```

温馨提示：推荐在**macOS**或**Linux**环境下使用，Windows环境下安装依赖的过程比较繁琐。

## 方法简介<a id="chapter-003"></a>

- get_symbols()	获取所有交易对信息
- get_exchange_rate(symbol, amount, side)	获取兑换汇率
- bulid_exchange_request(address, symbol, amount, side)	创建兑换请求
- submit_exchange_request(address, data)	提交兑换请求
- exchange_order_history(address, start="0", limit="20")	查询兑换历史记录
- pool_info()	储蓄池当前信息
- asset_proportion(symbol)	获取某个流动性池的资产比例
- build_multi_asset_deposit(address, symbol, quantity_proportion, amount)	构建双币转入
- build_single_asset_deposit(address, symbol, amount, currency)构建单币转入	
- submit_deposit(address, data)	提交转入
- submit_multi_asset_withdrawal(address, symbol, amount)	双资产移除流动性
- submit_single_asset_withdrawal(address, symbol, amount, currency)	单资产移除流动性
- user_earning(address)	获取用户收益
- annual_rate()	获取年化收益率
- multi_asset_available(address)	获取多资产可用信息
- single_asset_available(address)	获取单资产可用信息
- chain_status()	获取同步状态信息

## API文档<a id="chapter-004"></a>

详细API文档请点击：[超导兑换API](https://developer.bymov.io/zh/guide/mmdk_super_con_api.html)
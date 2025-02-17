import sys
import types
from typing import Union, List, Optional, Any
from decimal import Decimal

if sys.version_info.minor > 7:
    from typing import TypedDict, Literal, Dict
else:
    from typing import Dict
    from typing_extensions import Literal
    TypedDict = Dict

OrderSide = Literal['buy', 'sell']
OrderType = Literal['limit', 'market']
PositionSide = Literal['long', 'short']


class Entry:
    def __init__(self, path, api, method, config):
        self.name = None
        self.path = path
        self.api = api
        self.method = method
        self.config = config

        def unbound_method(_self, params={}):
            return _self.request(self.path, self.api, self.method, params, config=self.config)

        self.unbound_method = unbound_method

    def __get__(self, instance, owner):
        if instance is None:
            return self.unbound_method
        else:
            return types.MethodType(self.unbound_method, instance)

    def __set_name__(self, owner, name):
        self.name = name


IndexType = Union[str, int]
Num = Union[None, str, float, int, Decimal]
Str = Optional[str]
Strings = Optional[List[str]]
Int = Optional[int]
Bool = Optional[bool]
Fee = Optional[Dict[str, Any]]


class Balance(TypedDict):
    free: Num
    used: Num
    total: Num


class Trade(TypedDict):
    info: Dict[str, Any]
    amount: Num
    datetime: Str
    id: Str
    order: Str
    price: Num
    timestamp: Int
    type: Str
    side: Str
    symbol: Str
    takerOrMaker: Str
    cost: Num
    fee: Fee


class Position(TypedDict):
    info: Dict[str, Any]
    symbol: Str
    id: Str
    timestamp: Int
    datetime: Str
    contracts: Num
    contractSize: Num
    side: Str
    notional: Num
    leverage: Num
    unrealizedPnl: Num
    realizedPnl: Num
    collateral: Num
    entryPrice: Num
    markPrice: Num
    liquidationPrice: Num
    hedged: bool
    maintenanceMargin: Num
    initialMargin: Num
    initialMarginPercentage: Num
    marginMode: Str
    marginRatio: Num
    lastUpdateTimestamp: Int
    lastPrice: Num
    percentage: Num
    stopLossPrice: Num
    takeProfitPrice: Num


class OrderRequest(TypedDict):
    symbol: Str
    type: Str
    side: Str
    amount: Union[None, float]
    price: Union[None, float]
    params: Dict[str, Any]


class Order(TypedDict):
    info: Dict[str, Any]
    id: Str
    clientOrderId: Str
    datetime: Str
    timestamp: Int
    lastTradeTimestamp: Int
    lastUpdateTimestamp: Int
    status: Str
    symbol: Str
    type: Str
    timeInForce: Str
    side: OrderSide
    price: Num
    average: Num
    amount: Num
    filled: Num
    remaining: Num
    stopPrice: Num
    takeProfitPrice: Num
    stopLossPrice: Num
    cost: Num
    trades: List[Trade]
    fee: Fee


class FundingHistory(TypedDict):
    info: Dict[str, Any]
    symbol: Str
    code: Str
    timestamp: Int
    datetime: Str
    id: Str
    amount: Num


class Balances(Dict[str, Balance]):
    datetime: Str
    timestamp: Int


class OrderBook(TypedDict):
    asks: List[Num]
    bids: List[Num]
    datetime: Str
    timestamp: Int
    nonce: Int


class Transaction(TypedDict):
    info: Dict[str, any]
    id: Str
    txid: Str
    timestamp: Int
    datetime: Str
    address: Str
    addressFrom: Str
    addressTo: Str
    tag: Str
    tagFrom: Str
    tagTo: Str
    type: Str
    amount: Num
    currency: Str
    status: Str
    updated: Int
    fee: Fee
    network: Str
    comment: Str
    internal: Bool


class Ticker(TypedDict):
    info: Dict[str, Any]
    symbol: Str
    timestamp: Int
    datetime: Str
    high: Num
    low: Num
    bid: Num
    bidVolume: Num
    ask: Num
    askVolume: Num
    vwap: Num
    open: Num
    close: Num
    last: Num
    previousClose: Num
    change: Num
    percentage: Num
    average: Num
    quoteVolume: Num
    baseVolume: Num


Tickers = Dict[str, Ticker]


class MarginMode(TypedDict):
    info: Dict[str, Any]
    symbol: Str
    marginMode: Str


class Greeks(TypedDict):
    symbol: Str
    timestamp: Int
    datetime: Str
    delta: Num
    gamma: Num
    theta: Num
    vega: Num
    rho: Num
    bidSize: Num
    askSize: Num
    bidImpliedVolatility: Num
    askImpliedVolatility: Num
    markImpliedVolatility: Num
    bidPrice: Num
    askPrice: Num
    markPrice: Num
    lastPrice: Num
    underlyingPrice: Num
    info: Dict[str, Any]


class MarketInterface(TypedDict):
    info: Dict[str, Any]
    id: Str
    symbol: Str
    base: Str
    quote: Str
    baseId: Str
    quoteId: Str
    active: Bool
    type: Str
    spot: bool
    margin: bool
    swap: bool
    future: bool
    option: bool
    contract: bool
    settle: Str
    settleId: Str
    contractSize: Num
    linear: bool
    inverse: bool
    expiry: Num
    expiryDatetime: Str
    strike: Num
    optionType: Str
    taker: Num
    maker: Num
    percentage: bool
    tierBased: bool
    feeSide: Str
    precision: Any
    limits: Any
    created: Int


class CurrencyInterface(TypedDict):
    id: Str
    code: Str
    precision: Num


Market = Optional[MarketInterface]
Currency = Optional[CurrencyInterface]

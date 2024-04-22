from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddRequest(_message.Message):
    __slots__ = ("tg_id", "qr_info")
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    QR_INFO_FIELD_NUMBER: _ClassVar[int]
    tg_id: int
    qr_info: str
    def __init__(self, tg_id: _Optional[int] = ..., qr_info: _Optional[str] = ...) -> None: ...

class AddResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("tg_id", "begin_time", "end_time")
    TG_ID_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    tg_id: int
    begin_time: str
    end_time: str
    def __init__(self, tg_id: _Optional[int] = ..., begin_time: _Optional[str] = ..., end_time: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("purchases",)
    PURCHASES_FIELD_NUMBER: _ClassVar[int]
    purchases: _containers.RepeatedCompositeFieldContainer[Purchase]
    def __init__(self, purchases: _Optional[_Iterable[_Union[Purchase, _Mapping]]] = ...) -> None: ...

class Purchase(_message.Message):
    __slots__ = ("id", "user_id", "name", "market", "price", "category", "quantity", "barcode")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MARKET_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    BARCODE_FIELD_NUMBER: _ClassVar[int]
    id: int
    user_id: int
    name: str
    market: str
    price: int
    category: str
    quantity: int
    barcode: str
    def __init__(self, id: _Optional[int] = ..., user_id: _Optional[int] = ..., name: _Optional[str] = ..., market: _Optional[str] = ..., price: _Optional[int] = ..., category: _Optional[str] = ..., quantity: _Optional[int] = ..., barcode: _Optional[str] = ...) -> None: ...

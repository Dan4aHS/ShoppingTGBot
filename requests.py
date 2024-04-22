import grpc
import pkg.proto.fnsdb_pb2_grpc
import config
import pkg.proto.fnsdb_pb2 as fnsdb_pb2


async def add_request(tg_id: int, qr_info: str) -> fnsdb_pb2.AddResponse:
    async with grpc.aio.insecure_channel(f'localhost:{config.GRPC_PORT}') as channel:
        stub = pkg.proto.fnsdb_pb2_grpc.ShoppingServiceStub(channel)
        req = fnsdb_pb2.AddRequest(tg_id=tg_id, qr_info=qr_info)
        res = await stub.Add(req)
    return res


async def list_request(tg_id, start, finish):
    return fnsdb_pb2.ListRequest(
        tg_id=tg_id,
        begin_time=start,
        end_time=finish
    )


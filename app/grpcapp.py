import grpc.aio

import config
import pkg.proto.fnsdb_pb2_grpc


# class ShoppingService(pkg.proto.fnsdb_pb2_grpc.ShoppingServiceServicer):
#     async def Add(
#             self,
#             req: pkg.proto.fnsdb_pb2.AddRequest,
#             context: grpc.aio.ServicerContext
#     ) -> pkg.proto.fnsdb_pb2.AddResponse:
#         return pkg.proto.fnsdb_pb2.AddResponse()
#
#     async def List(self, request, context):
#         return pkg.proto.fnsdb_pb2.ListResponse()
#
#
# async def serve() -> None:
#     server = grpc.aio.server()
#     pkg.proto.fnsdb_pb2_grpc.add_ShoppingServiceServicer_to_server(ShoppingService(), server)
#     listen_addr = '[::]:50051'
#     server.add_insecure_port(listen_addr)
#     await server.start()
#     await server.wait_for_termination()




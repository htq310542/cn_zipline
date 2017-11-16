import zerorpc
from cn_zipline.gens.tdx_broker import TdxBroker


def tdx_broker():
    client = zerorpc.Client()
    client.connect("tcp://127.0.0.1:4242")
    print(client.transactions())
    # print(client.orders())


tdx_broker()
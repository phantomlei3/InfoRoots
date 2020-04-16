import zmq


def test_URL(test_url):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:5555")

    socket.send(test_url)
    message = socket.recv()
    print(message)

    # socket.send(b"Article")
    # message = socket.recv()
    # print(message)

    socket.send(b"Author card")
    message = socket.recv()
    print(message)

    socket.send(b"Publisher card")
    message = socket.recv()
    print(message)

def test_NewYorkTime():
    url = b'URL https://www.nytimes.com/2020/04/06/world/europe/coronavirus-terrorism-threat-response.html?action=click&module=Spotlight&pgtype=Homepage'
    test_URL(url)


if __name__ == '__main__':
    test_NewYorkTime()
from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://qhbiivgl:m2I1MEBtDyATJpcjLLhqqtplksSZM6aj@donkey.rmq.cloudamqp.com/qhbiivgl"

TEST_QUEUE_NAME = 'test'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    sentMsg = {'test': 'demo'}
    client.sendMessage(sentMsg)
    client.sleep(10)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg
    print 'cloudAMQP connection is ok, test passed'
if __name__ == "__main__":
    test_basic()
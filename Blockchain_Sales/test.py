import Blockchain as bChain
import Block as b

blockchain = bChain.Blockchain()
b1 = b.Block("new")
b2 = b.Block("ddd")

blockchain.add(b1)
blockchain.add(b2)
print('2')
# for n in range(2):
#     blockchain.mine(b.Block("Block " + str(n+1)))

print('here')
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next

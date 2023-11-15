import hashlib as hasher
import datetime


class Data():
    def __init__(self, index, data, date):
        self.index = index
        self.data = data
        self.date = datetime.datetime.now()
        self.hex = self.hashing()

    def hashing(self):
        """This is the method which performs the hashing operation"""
        sha = hasher.sha256()
        strings = str(self.index) + str(self.data) + str(self.date)
        sha.update(strings.encode('utf-8'))
        return sha.hexdigest()

    def turncoats(self):
        return self.index, self.data, self, date, self.hex


def genesisBlock():
    firstBlock = Data(0,"This is first block",None)
    return firstBlock

listBlock = []
#listBlock.append(myBlock)


def nextBlocks(previous_block,data):
    index = int(previous_block.index) + 1
    timeStamp = None
    #data = "This is block number %r" % index
    new_block = Data(index, data, timeStamp)
    return new_block


def addingBlocks(dataset):
    listBlock.append(genesisBlock())
    previous_block = listBlock[0]
    for info in dataset:
        block_to_add = nextBlocks(previous_block,info)
        listBlock.append(block_to_add)
        previous_block = block_to_add
    theBlockChain()

def theBlockChain():
    for this_block in listBlock:
        print()
        print("Index:", this_block.index)
        print("Data:", this_block.data)
        print(str(this_block.date))
        print("SHA256:", this_block.hex)
        print("\n\n")




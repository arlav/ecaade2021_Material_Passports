

#refer to credentials.MD for public test ethereum addrsses
#double check that this is my infura.
#double check that all addresses are written with capitals so they CheckSum
#@dev:Note this setup is for Rinkeby-be careful with the infura nodes, chainID, and gas limits!

contract_address = "0x71603D1d4A341EfD6e7C8317d4a4Bfde0aaE3298" #contract owned by ArchChainONE on RinkeBy
wallet_address = "0x59DcC1e1B1F43BaD14DA3b8040995677d6fc923E"
address = "0x59DcC1e1B1F43BaD14DA3b8040995677d6fc923E"
wallet_private_key = "2366b847b1452a873139138443b88957f084e4add05f00d3074497ed404db0d0"
infura_url = "https://rinkeby.infura.io/v3/029c7ec526724b59b345469899f0dd9e" #Theo's infura Node

#infura_url = "https://ropsten.infura.io/v3/bc0151acb1204cacadd049ab3ac000eb" #Wassim's infura node

#@dev: entries to use with the anaconda python inside blender/dynamo/Grrasshopper
#@dev: testt initially without topologic, jusst send a strring to be minted,
#@dev:use double \\ in the windows path so that python does not throw an error in reading the string for the path
path = "C:\\Users\\calys\\anaconda3\\envs\\Dynamo383\\Lib\\site-packages" #enter your web3 location here
#['', '/opt/anaconda3/lib/python38.zip', '/opt/anaconda3/lib/python3.8', '/opt/anaconda3/lib/python3.8/lib-dynload', '/opt/anaconda3/lib/python3.8/site-packages', '/opt/anaconda3/lib/python3.8/site-packages/aeosa']

contract_abi =  ""



import time
import sys
sys.path.append(path)
from web3 import Web3, HTTPProvider


from topologic import Vertex, Topology
import cppyy

v = Vertex.ByCoordinates(10,20,30)
string = str('Hello_Mayur_it_is_Nice_to_meet_You')
w3 = Web3(HTTPProvider(infura_url))


smartContract = w3.eth.contract(address=contract_address, abi=contract_abi)

receipts = []

#the next function is the one to change according to the material passport function.
nonce = w3.eth.get_transaction_count(wallet_address)
tx_dict = smartContract.functions.mintNFT(address, string).buildTransaction({
    'chainId' : 4,
    'gas' : 2100000,  #some of this was throwing errors, double check gas amounts.
    'gasPrice' : w3.toWei('50', 'gwei'),
    'nonce' : nonce,
})



signed_tx = w3.eth.account.sign_transaction(tx_dict, wallet_private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash, timeout=120, poll_latency=0.1)
receipts.append(tx_receipt)



outputList = []
for tx_receipt in receipts:
    receipt = []
    receipt.append('blockHash: '+str(tx_receipt['blockHash']))
    receipt.append('blockNumber: '+str(tx_receipt['blockNumber']))
    receipt.append('contractAddress: '+str(tx_receipt['contractAddress']))
    receipt.append('cumulativeGasUsed: '+str(tx_receipt['cumulativeGasUsed']))
    receipt.append('from: '+str(tx_receipt['from']))
    receipt.append('gasUsed: '+str(tx_receipt['gasUsed']))
    receipt.append('logs: '+str(tx_receipt['logs']))
    receipt.append('to: '+str(tx_receipt['to']))
    receipt.append('transactionHash: '+str(tx_receipt['transactionHash']))
    receipt.append('tansactionIndex: '+str(tx_receipt['transactionIndex']))
    outputList.append(receipt)



print(outputList)

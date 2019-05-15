import json
from web3 import Web3, HTTPProvider, IPCProvider


my_provider = IPCProvider("/home/surge/Workspace/_studio/web3/mychain/data/geth.ipc")
web3 = Web3(my_provider)

abi = open('greeter_sol_Greeter.abi','r')
abi = json.load(abi) 
contract_address = "0x52Ad7161480E6C1329fA689F9105342b7bcbC6eb"

web3.eth.defaultAccount = web3.eth.accounts[0]
web3.personal.unlockAccount(web3.eth.defaultAccount, "qwe12345", 30000)

print('w3.eth.defaultAccount = ', web3.eth.defaultAccount)
print('contract_address = 0x52Ad7161480E6C1329fA689F9105342b7bcbC6eb')

user = web3.eth.contract(address=contract_address, abi=abi)
# tx_hash = user.functions.set(5).transact({'gas': 50000, 'from': web3.eth.defaultAccount})
# receipt = web3.eth.waitForTransactionReceipt(tx_hash)
# print(receipt)
user_data = user.functions.get().call()
print(user_data)

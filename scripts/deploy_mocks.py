from brownie import network, MockV3Aggregator
from scripts.helpful_scripts import get_account
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

def deploy_mocks():
    account = get_account()

    print(f"The active network is {network.show_active()}")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS,Web3.toWei(STARTING_PRICE,"ether"),{"from": account})
    print ("Mocks Deployed")

def main():
    deploy_mocks()
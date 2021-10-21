from brownie import network, accounts, config
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_BLOCKCHAIN_ENVIRONMENTS = ["mainnet-fork-dev"]

def get_account():
    if network.show_active() == LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() == FORKED_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


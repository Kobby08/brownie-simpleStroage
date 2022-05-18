from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    account = accounts[0]  # useful when testing on a local network like ganache.
    # account = accounts.load("quam-account") # encrypted way of storing accounts.
    # account = accounts.add(config["wallets"]["from_key"]) # using environment variables
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(50, {"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)


def main():
    deploy_simple_storage()

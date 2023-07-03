from brownie import OurToken,config
from scripts.helpful_scripts import get_account
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy
from web3 import Web3

inintial_supply = Web3.toWei(1000, "ether")

gas_strategy = LinearScalingStrategy("60 gwei", "90 gwei", 1.125)
gas_price = gas_strategy


def main():
    account = get_account()
    our_token = OurToken.deploy(
        inintial_supply, {"from": account, "gas_price": gas_strategy}
    )

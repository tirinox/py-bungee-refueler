import argparse
import sys
from sys import stderr

from loguru import logger
from web3 import Web3
from web3.middleware import geth_poa_middleware

from config import *

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white>"
                          " | <level>{level: <8}</level>"
                          " | <cyan>{line}</cyan>"
                          " - <white>{message}</white>")


def get_native_symbol(chain: str) -> str:
    symbol_mapping = {
        'ETH': 'ether',
        'OPT': 'ether',
        'ARB': 'ether',
        'AUR': 'ether',
        'ERA': 'ether',
        'MATIC': 'matic',
        'ZKEVM': 'matic',
        'BSC': 'bnb',
        'GNO': 'xdai',
        'AVAX': 'avax',
        'FTM': 'ftm'
    }

    return symbol_mapping.get(chain, '')


def calculate_gas_price(rpc, private_key, dest_chain_key, send_amount):
    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    address = Web3.to_checksum_address(w3.eth.account.from_key(private_key).address)
    gas_price = w3.to_wei(str(w3.eth.gas_price), 'wei')
    gas_limit = get_gas_limit(dest_chain_key)
    nonce = w3.eth.get_transaction_count(address)
    tx = {
        'nonce': nonce,
        'gas': gas_limit,
        'gasPrice': gas_price,
        'value': w3.to_wei(send_amount, 'ether')
    }
    estimated_gas = w3.eth.estimate_gas(tx)
    gas_limit = int(estimated_gas * 1.3)
    # update the gas-parameters of tx
    tx['gas'] = gas_limit
    return tx


def send_tx(w3,
            send_amount: float,
            private_key,
            source_chain: ChainConfig,
            dest_chain: ChainConfig):
    # Function: depositNativeToken(uint256 destinationChainId,address _to)

    address = None
    try:
        address = Web3.to_checksum_address(w3.eth.account.from_key(private_key).address)

        # recalculate gas
        tx_data = calculate_gas_price(source_chain.rpc, private_key, dest_chain.key, send_amount)
        if True:  # tx_type == 1:
            transaction = contract_refuel.functions \
                .depositNativeToken(dest_chain.chain_id, address) \
                .build_transaction(tx_data)

            # Sign the transaction with the receiver's private key
            signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

            # Send the transaction to the network
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            tx_hash = w3.to_hex(w3.keccak(signed_txn.rawTransaction))

            # Check if the transaction was successful
            if receipt['status'] == 1:
                logger.info(f'Refueling from {address} | {source_chain.tx_explorer}tx/{tx_hash}')
                logger.info(
                    f'Waiting txn for destination chain ({dest_chain.key}) '
                    f'{dest_chain.tx_explorer}address/{address}/#internaltx')
            else:
                raise ValueError(f"Refueling from {address} failed with receipt status {receipt['status']}")

    except Exception as error:
        logger.exception(f'{address} | {error}')


def main():
    print('-' * 108)
    print(f'{"BUNGEE BATCH REFUELER":^108}')
    print('-' * 108)

    download_chain_data()

    print('Select origin chain:')
    for i, chain in enumerate(CHAIN_CONFIG_MAP.values()):
        print(f'{i:3}. {chain.name:10} => {chain.key}')

    while True:
        source_key = input('Input short name of the source chain (ETH, ARB etc.): ').upper()
        source_chain_desc = CHAIN_CONFIG_MAP.get(source_key)
        if source_chain_desc:
            print(f'{source_chain_desc.name} selected like origin chain')
            break
        else:
            logger.error(f'Chain {source_key} not found')

    while True:
        dest_chain_name = input(f'Select target chain (ETH and {source_key} can not be selected): ').upper()
        dest_chain_desc = CHAIN_CONFIG_MAP.get(dest_chain_name)

        if dest_chain_desc:
            break
        if dest_chain_name == source_chain_desc.chain_id:
            print(f'origin chain {dest_chain_name} can not be select like destination chain')
        elif dest_chain_name == 'ETH':
            print(f'{dest_chain_name} can not be select like destination chain')
        else:
            logger.error(f'Chain {dest_chain_name} not found')

    gas_token = get_native_symbol(source_key)
    min_gas, max_gas = min_and_max_gas_amount(source_key, dest_chain_name)
    print(f"Minimum amount for send = {min_gas} {gas_token} + 10%")
    print(f"Maximum amount for send = {max_gas} {gas_token} - 10%")

    print(f"You can input value >= {min_gas} {gas_token} <= {max_gas} {gas_token}")
    print(f"You also can input 'min'/ 'max' for send minimum/maximum amounts {gas_token}")

    amount = ''
    send_amount = 0
    while (amount != 'MAX') or (amount != 'MIN') or (float(amount) < min_gas) or (float(amount) > max_gas):
        amount = input('Input amount to send: ')
        amount = amount.upper()

        # Setting gas amount for send
        if amount == 'MAX':
            amount = max_gas * 0.9
            send_amount = float(amount)
            break

        elif amount == 'MIN':
            amount = min_gas * 1.1
            send_amount = float(amount)
            break

        else:
            send_amount = float(amount)
            break

    private_keys = load_wallets()
    print(f"{amount} {gas_token} will be send from all your addresses")
    perform_actions(private_keys, send_amount, source_chain_desc, dest_chain_desc)


def load_wallets():
    # Loads private_keys
    with open('accounts.txt', encoding='utf-8-sig') as file:
        private_keys = [row.strip() for row in file]
    num_wallets = len(private_keys)
    logger.info(f'Loaded {num_wallets} wallets')
    return private_keys


def perform_actions(private_keys: list,
                    send_amount: float,
                    source_chain_desc: ChainConfig,
                    dest_chain_desc: ChainConfig):
    print(f'Starting send {send_amount:.5} Gas from {source_chain_desc.name} to {dest_chain_desc.name}')

    w3 = Web3(Web3.HTTPProvider(source_chain_desc.rpc))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    # Loads ABI for contracts
    with open('ABI/socket.json', 'r', encoding='utf-8-sig') as file:
        SOCKET_ABI = file.read().strip().replace('\n', '').replace(' ', '')
    global contract_refuel
    contract_refuel = w3.eth.contract(address=Web3.to_checksum_address(source_chain_desc.contract),
                                      abi=SOCKET_ABI)

    if isinstance(private_keys, str):
        private_keys = [private_keys]

    for private_key in private_keys:
        send_tx(w3, send_amount, private_key, source_chain_desc, dest_chain_desc)


def read_arguments():
    arg_parser = argparse.ArgumentParser(description=f'Bungee batch refueler. Supported chains are: {ALL_CHAINS}')
    arg_parser.add_argument('-k', '--private-key', type=str, help='private key in hex fromat without 0x prefix')
    arg_parser.add_argument('-a', '--amount', type=float, required=True, help='amount of coins to send')
    arg_parser.add_argument('-s', '--source-chain', '--src', '--source', type=str, required=True,
                            help='source chain code e.g. ARB, MATIC, OP etc.')
    arg_parser.add_argument('-d', '--destination-chain', '-dst', '--dest', type=str, required=True,
                            help='destination chain code')
    arg_parser.add_argument('-U', '--update-chain-data', action='store_true', help='update chain data')
    return arg_parser.parse_args()


def main_parametric(args):
    download_chain_data(bool(args.update_chain_data))

    source = args.source_chain.upper()
    assert source in ALL_CHAINS, f'Unknown source chain {source}'
    dest = args.destination_chain.upper()
    assert dest in ALL_CHAINS, f'Unknown destination chain {dest}'

    amount = float(args.amount)
    assert amount > 0, f'Amount must be positive, got {amount}'

    private_key = args.private_key
    assert private_key, 'Private key must be specified'
    if private_key.lower().startswith('0x'):
        private_key = private_key[2:]

    source_chain_desc = CHAIN_CONFIG_MAP[source]
    dest_chain_desc = CHAIN_CONFIG_MAP[dest]

    perform_actions([private_key], amount, source_chain_desc, dest_chain_desc)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = read_arguments()
        main_parametric(args)
    else:
        main()

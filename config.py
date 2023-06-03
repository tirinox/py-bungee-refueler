from pprint import pprint
from typing import NamedTuple

from dotenv import load_dotenv

from refuel import *

load_dotenv()


class ChainConfig(NamedTuple):
    key: str
    name: str
    chain_id: int
    rpc: str = ''
    contract: str = ''
    tx_explorer: str = ''


ALL_CHAINS = ('ETH', 'OPT', 'BSC', 'GNO', 'MATIC', 'ERA', 'ZKEVM', 'ARB', 'AVAX', 'AUR', 'FTM')

CHAIN_CONFIG_MAP = {
    'ETH': ChainConfig('ETH', 'Ethereum', chain_id=1, tx_explorer='https://etherscan.io/'),
    'OPT': ChainConfig('OPT', 'Optimism', chain_id=10, tx_explorer='https://optimistic.etherscan.io/'),
    'BSC': ChainConfig('BSC', 'BSC', chain_id=56, tx_explorer='https://bscscan.com/'),
    'GNO': ChainConfig('GNO', 'Gnosis', chain_id=100, tx_explorer='https://gnosisscan.io/'),
    'MATIC': ChainConfig('MATIC', 'Polygon', chain_id=137, tx_explorer='https://polygonscan.com/'),
    'ERA': ChainConfig('ERA', 'zkSync', chain_id=324, tx_explorer='https://explorer.zksync.io/'),
    'ZKEVM': ChainConfig('ZKEVM', 'zkEVM', chain_id=1101, tx_explorer='https://zkevm.polygonscan.com/'),
    'ARB': ChainConfig('ARB', 'Arbitrum', chain_id=42161, tx_explorer='https://arbiscan.io/'),
    'AVAX': ChainConfig('AVAX', 'Avalanche', chain_id=43114, tx_explorer='https://snowtrace.io/'),
    'AUR': ChainConfig('AUR', 'Aurora', chain_id=1313161554, tx_explorer='https://mainnet.aurora.dev/'),
    'FTM': ChainConfig('FTM', 'Fantom', chain_id=250, tx_explorer='https://ftmscan.com/')
}

for chain in ALL_CHAINS:
    router_key = f'BUNGEE_{chain}_ROUTER'
    router = os.getenv(router_key)
    rpc_key = f'RPC_{chain}'
    rpc = os.getenv(rpc_key)
    if not router:
        raise ValueError(f'Missing environment variable {router_key}')
    if not rpc:
        raise ValueError(f'Missing environment variable {rpc_key}')
    CHAIN_CONFIG_MAP[chain] = CHAIN_CONFIG_MAP[chain]._replace(rpc=rpc, contract=router)


def min_and_max_gas_amount(source_chain_key: str, dest_chain_key: str) -> Tuple[float, float]:
    """
    Returns the minimum gas amount for a given chain pair
    :param source_chain_key: The source chain key
    :param dest_chain_key: The destination chain key
    :return: The minimum and maximum gas amount
    """
    source = CHAIN_CONFIG_MAP.get(source_chain_key)
    destination = CHAIN_CONFIG_MAP.get(dest_chain_key)
    if not source or not destination:
        raise ValueError('Invalid chain key')

    return get_send_amounts(source.name, destination.chain_id)


pprint(CHAIN_CONFIG_MAP)

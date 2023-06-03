from typing import NamedTuple

from dotenv import load_dotenv

from refuel import *

load_dotenv()


class ChainConfig(NamedTuple):
    key: str
    name: str
    chain_id: int
    rpc: str
    contract: str
    tx_explorer: str


BUNGEE_ETH_ROUTER = os.getenv('BUNGEE_ETH_ROUTER')
BUNGEE_OPT_ROUTER = os.getenv('BUNGEE_OPT_ROUTER')
BUNGEE_BSC_ROUTER = os.getenv('BUNGEE_BSC_ROUTER')
BUNGEE_GNO_ROUTER = os.getenv('BUNGEE_GNO_ROUTER')
BUNGEE_MATIC_ROUTER = os.getenv('BUNGEE_MATIC_ROUTER')
BUNGEE_ERA_ROUTER = os.getenv('BUNGEE_ERA_ROUTER')
BUNGEE_ZKEVM_ROUTER = os.getenv('BUNGEE_ZKEVM_ROUTER')
BUNGEE_ARB_ROUTER = os.getenv('BUNGEE_ARB_ROUTER')
BUNGEE_AVAX_ROUTER = os.getenv('BUNGEE_AVAX_ROUTER')
BUNGEE_AUR_ROUTER = os.getenv('BUNGEE_AUR_ROUTER')
BUNGEE_FTM_ROUTER = os.getenv('BUNGEE_FTM_ROUTER')

RPC_ETH = os.getenv('RPC_ETH')
RPC_OPT = os.getenv('RPC_OPT')
RPC_BSC = os.getenv('RPC_BSC')
RPC_GNO = os.getenv('RPC_GNO')
RPC_MATIC = os.getenv('RPC_MATIC')
RPC_ERA = os.getenv('RPC_ERA')
RPC_ZKEVM = os.getenv('RPC_ZKEVM')
RPC_ARB = os.getenv('RPC_ARB')
RPC_AVAX = os.getenv('RPC_AVAX')
RPC_AUR = os.getenv('RPC_AUR')
RPC_FTM = os.getenv('RPC_FTM')

CHAIN_CONFIG_MAP = {
    'ETH': ChainConfig('ETH', 'Ethereum', chain_id=1, rpc=RPC_ETH, contract=BUNGEE_ETH_ROUTER,
                       tx_explorer='https://etherscan.io/'),
    'OPT': ChainConfig('OPT', 'Optimism', chain_id=10, rpc=RPC_OPT, contract=BUNGEE_OPT_ROUTER,
                       tx_explorer='https://optimistic.etherscan.io/'),
    'BSC': ChainConfig('BSC', 'BSC', chain_id=56, rpc=RPC_BSC, contract=BUNGEE_BSC_ROUTER,
                       tx_explorer='https://bscscan.com/'),
    'GNO': ChainConfig('GNO', 'Gnosis', chain_id=100, rpc=RPC_GNO, contract=BUNGEE_GNO_ROUTER,
                       tx_explorer='https://gnosisscan.io/'),
    'MATIC': ChainConfig('MATIC', 'Polygon', chain_id=137, rpc=RPC_MATIC, contract=BUNGEE_MATIC_ROUTER,
                         tx_explorer='https://polygonscan.com/'),
    'ERA': ChainConfig('ERA', 'zkSync', chain_id=324, rpc=RPC_ERA, contract=BUNGEE_ERA_ROUTER,
                       tx_explorer='https://explorer.zksync.io/'),
    'ZKEVM': ChainConfig('ZKEVM', 'zkEVM', chain_id=1101, rpc=RPC_ZKEVM, contract=BUNGEE_ZKEVM_ROUTER,
                         tx_explorer='https://zkevm.polygonscan.com/'),
    'ARB': ChainConfig('ARB', 'Arbitrum', chain_id=42161, rpc=RPC_ARB, contract=BUNGEE_ARB_ROUTER,
                       tx_explorer='https://arbiscan.io/'),
    'AVAX': ChainConfig('AVAX', 'Avalanche', chain_id=43114, rpc=RPC_AVAX, contract=BUNGEE_AVAX_ROUTER,
                        tx_explorer='https://snowtrace.io/'),
    'AUR': ChainConfig('AUR', 'Aurora', chain_id=1313161554, rpc=RPC_AUR, contract=BUNGEE_AUR_ROUTER,
                       tx_explorer='https://mainnet.aurora.dev/'),
    'FTM': ChainConfig('FTM', 'Fantom', chain_id=250, rpc=RPC_FTM, contract=BUNGEE_FTM_ROUTER,
                       tx_explorer='https://ftmscan.com/')
}


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

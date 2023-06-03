from dotenv import load_dotenv

from refuel import *

load_dotenv()
BUNGEE_ETH_ROUNER = os.getenv('BUNGEE_ETH_ROUNER')
BUNGEE_OPT_ROUTER = os.getenv('BUNGEE_OPT_ROUTER')
BUNGEE_BSC_ROUTER = os.getenv('BUNGEE_BSC_ROUTER')
BUNGEE_GNO_ROUTER = os.getenv('BUNGEE_GNO_ROUTER')
BUNGEE_MATIC_ROUNER = os.getenv('BUNGEE_MATIC_ROUNER')
BUNGEE_ERA_ROUNER = os.getenv('BUNGEE_ERA_ROUNER')
BUNGEE_ZKEVM_ROUNER = os.getenv('BUNGEE_ZKEVM_ROUNER')
BUNGEE_ARB_ROUNER = os.getenv('BUNGEE_ARB_ROUNER')
BUNGEE_AVAX_ROUNER = os.getenv('BUNGEE_AVAX_ROUNER')
BUNGEE_AUR_ROUNER = os.getenv('BUNGEE_AUR_ROUNER')
BUNGEE_FTM_ROUNER = os.getenv('BUNGEE_FTM_ROUNER')

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

EXP_ETH = 'https://etherscan.io/'
EXP_OPT = 'https://optimistic.etherscan.io/'
EXP_BSC = 'https://bscscan.com/'
EXP_GNO = 'https://gnosisscan.io/'
EXP_MATIC = 'https://polygonscan.com/'
EXP_ERA = 'https://explorer.zksync.io/'
EXP_ZKEVM = 'https://zkevm.polygonscan.com/'
EXP_ARB = 'https://arbiscan.io/'
EXP_AVAX = 'https://snowtrace.io/'
EXP_AUR = 'https://mainnet.aurora.dev/'
EXP_FTM = 'https://ftmscan.com/'

# Minimum amounts from ETH
min_eth_to_arb = get_min_send_amount('Ethereum', 42161)
min_eth_to_opt = get_min_send_amount('Ethereum', 10)
min_eth_to_bsc = get_min_send_amount('Ethereum', 56)
min_eth_to_matic = get_min_send_amount('Ethereum', 137)
min_eth_to_era = get_min_send_amount('Ethereum', 324)
min_eth_to_zkevm = get_min_send_amount('Ethereum', 1101)
min_eth_to_avax = get_min_send_amount('Ethereum', 43114)
min_eth_to_aur = get_min_send_amount('Ethereum', 1313161554)
min_eth_to_gno = get_min_send_amount('Ethereum', 100)

# Maximum amounts from ETH
max_eth_to_arb = get_max_send_amount('Ethereum', 42161)
max_eth_to_opt = get_max_send_amount('Ethereum', 10)
max_eth_to_bsc = get_max_send_amount('Ethereum', 56)
max_eth_to_matic = get_max_send_amount('Ethereum', 137)
max_eth_to_era = get_max_send_amount('Ethereum', 324)
max_eth_to_zkevm = get_max_send_amount('Ethereum', 1101)
max_eth_to_avax = get_max_send_amount('Ethereum', 43114)
max_eth_to_aur = get_max_send_amount('Ethereum', 1313161554)
max_eth_to_gno = get_max_send_amount('Ethereum', 100)

# Minimum amount from OPT
min_opt_to_arb = get_min_send_amount('Optimism', 42161)
min_opt_to_bsc = get_min_send_amount('Optimism', 56)
min_opt_to_gno = get_min_send_amount('Optimism', 100)
min_opt_to_matic = get_min_send_amount('Optimism', 137)
min_opt_to_era = get_min_send_amount('Optimism', 324)
min_opt_to_zkevm = get_min_send_amount('Optimism', 1101)
min_opt_to_avax = get_min_send_amount('Optimism', 43114)
min_opt_to_aur = get_min_send_amount('Optimism', 1313161554)

# Maximum amounts from OPT
max_opt_to_arb = get_max_send_amount('Optimism', 42161)
max_opt_to_bsc = get_max_send_amount('Optimism', 56)
max_opt_to_gno = get_max_send_amount('Optimism', 100)
max_opt_to_matic = get_max_send_amount('Optimism', 137)
max_opt_to_era = get_max_send_amount('Optimism', 324)
max_opt_to_zkevm = get_max_send_amount('Optimism', 1101)
max_opt_to_avax = get_max_send_amount('Optimism', 43114)
max_opt_to_aur = get_max_send_amount('Optimism', 1313161554)

# Minimum amounts from BSC
min_bsc_to_arb = get_min_send_amount('BSC', 42161)
min_bsc_to_opt = get_min_send_amount('BSC', 10)
min_bsc_to_gno = get_min_send_amount('BSC', 100)
min_bsc_to_matic = get_min_send_amount('BSC', 137)
min_bsc_to_era = get_min_send_amount('BSC', 324)
min_bsc_to_zkevm = get_min_send_amount('BSC', 1101)
min_bsc_to_avax = get_min_send_amount('BSC', 43114)
min_bsc_to_aur = get_min_send_amount('BSC', 1313161554)

# Minimum amounts from BSC
max_bsc_to_arb = get_max_send_amount('BSC', 42161)
max_bsc_to_opt = get_max_send_amount('BSC', 10)
max_bsc_to_gno = get_max_send_amount('BSC', 100)
max_bsc_to_matic = get_max_send_amount('BSC', 137)
max_bsc_to_era = get_max_send_amount('BSC', 324)
max_bsc_to_zkevm = get_max_send_amount('BSC', 1101)
max_bsc_to_avax = get_max_send_amount('BSC', 43114)
max_bsc_to_aur = get_max_send_amount('BSC', 1313161554)

# Min Amounts from Gnosis
min_gno_to_arb = get_min_send_amount('Gnosis', 42161)
min_gno_to_avax = get_min_send_amount('Gnosis', 43114)
min_gno_to_aur = get_min_send_amount('Gnosis', 1313161554)
min_gno_to_opt = get_min_send_amount('Gnosis', 10)
min_gno_to_bsc = get_min_send_amount('Gnosis', 56)
min_gno_to_matic = get_min_send_amount('Gnosis', 137)
min_gno_to_era = get_min_send_amount('Gnosis', 324)
min_gno_to_zkevm = get_min_send_amount('Gnosis', 1101)

# Max Amounts from Gnosis
max_gno_to_arb = get_min_send_amount('Gnosis', 42161)
max_gno_to_avax = get_min_send_amount('Gnosis', 43114)
max_gno_to_aur = get_min_send_amount('Gnosis', 1313161554)
max_gno_to_opt = get_min_send_amount('Gnosis', 10)
max_gno_to_bsc = get_min_send_amount('Gnosis', 56)
max_gno_to_matic = get_min_send_amount('Gnosis', 137)
max_gno_to_era = get_min_send_amount('Gnosis', 324)
max_gno_to_zkevm = get_min_send_amount('Gnosis', 1101)

# Min Amounts from MATIC
min_matic_to_arb = get_min_send_amount('Polygon', 42161)
min_matic_to_opt = get_min_send_amount('Polygon', 10)
min_matic_to_bsc = get_min_send_amount('Polygon', 56)
min_matic_to_gno = get_min_send_amount('Polygon', 100)
min_matic_to_era = get_min_send_amount('Polygon', 324)
min_matic_to_zkevm = get_min_send_amount('Polygon', 1101)
min_matic_to_avax = get_min_send_amount('Polygon', 43114)
min_matic_to_aur = get_min_send_amount('Polygon', 1313161554)

# Max Amounts from MATIC
max_matic_to_arb = get_max_send_amount('Polygon', 42161)
max_matic_to_opt = get_max_send_amount('Polygon', 10)
max_matic_to_bsc = get_max_send_amount('Polygon', 56)
max_matic_to_gno = get_max_send_amount('Polygon', 100)
max_matic_to_era = get_max_send_amount('Polygon', 324)
max_matic_to_zkevm = get_max_send_amount('Polygon', 1101)
max_matic_to_avax = get_max_send_amount('Polygon', 43114)
max_matic_to_aur = get_max_send_amount('Polygon', 1313161554)

# Min Amounts from Era
min_era_to_arb = get_min_send_amount('zkSync', 42161)
min_era_to_opt = get_min_send_amount('zkSync', 10)
min_era_to_bsc = get_min_send_amount('zkSync', 56)
min_era_to_gno = get_min_send_amount('zkSync', 100)
min_era_to_matic = get_min_send_amount('zkSync', 137)
min_era_to_zkevm = get_min_send_amount('zkSync', 1101)
min_era_to_avax = get_min_send_amount('zkSync', 43114)
min_era_to_aur = get_min_send_amount('zkSync', 1313161554)

# Max Amounts from Era
max_era_to_arb = get_max_send_amount('zkSync', 42161)
max_era_to_opt = get_max_send_amount('zkSync', 10)
max_era_to_bsc = get_max_send_amount('zkSync', 56)
max_era_to_gno = get_max_send_amount('zkSync', 100)
max_era_to_matic = get_max_send_amount('zkSync', 137)
max_era_to_zkevm = get_max_send_amount('zkSync', 1101)
max_era_to_avax = get_max_send_amount('zkSync', 43114)
max_era_to_aur = get_max_send_amount('zkSync', 1313161554)

# Min Amounts from zkEVM
min_zkevm_to_arb = get_min_send_amount('zkEVM', 42161)
min_zkevm_to_opt = get_min_send_amount('zkEVM', 10)
min_zkevm_to_bsc = get_min_send_amount('zkEVM', 56)
min_zkevm_to_gno = get_min_send_amount('zkEVM', 100)
min_zkevm_to_matic = get_min_send_amount('zkEVM', 137)
min_zkevm_to_era = get_min_send_amount('zkEVM', 324)
min_zkevm_to_avax = get_min_send_amount('zkEVM', 43114)
min_zkevm_to_aur = get_min_send_amount('zkEVM', 1313161554)

# Max Amounts from zkEVM
max_zkevm_to_arb = get_max_send_amount('zkEVM', 42161)
max_zkevm_to_opt = get_max_send_amount('zkEVM', 10)
max_zkevm_to_bsc = get_max_send_amount('zkEVM', 56)
max_zkevm_to_gno = get_max_send_amount('zkEVM', 100)
max_zkevm_to_matic = get_max_send_amount('zkEVM', 137)
max_zkevm_to_era = get_max_send_amount('zkEVM', 324)
max_zkevm_to_avax = get_max_send_amount('zkEVM', 43114)
max_zkevm_to_aur = get_max_send_amount('zkEVM', 1313161554)

# Min Amounts from Arbitrum
min_arb_to_zkevm = get_min_send_amount('Arbitrum', 1101)
min_arb_to_opt = get_min_send_amount('Arbitrum', 10)
min_arb_to_bsc = get_min_send_amount('Arbitrum', 56)
min_arb_to_gno = get_min_send_amount('Arbitrum', 100)
min_arb_to_matic = get_min_send_amount('Arbitrum', 137)
min_arb_to_era = get_min_send_amount('Arbitrum', 324)
min_arb_to_avax = get_min_send_amount('Arbitrum', 43114)
min_arb_to_aur = get_min_send_amount('Arbitrum', 1313161554)

# Max Amounts from Arbitrum
max_arb_to_zkevm = get_max_send_amount('Arbitrum', 1101)
max_arb_to_opt = get_max_send_amount('Arbitrum', 10)
max_arb_to_bsc = get_max_send_amount('Arbitrum', 56)
max_arb_to_gno = get_max_send_amount('Arbitrum', 100)
max_arb_to_matic = get_max_send_amount('Arbitrum', 137)
max_arb_to_era = get_max_send_amount('Arbitrum', 324)
max_arb_to_avax = get_max_send_amount('Arbitrum', 43114)
max_arb_to_aur = get_max_send_amount('Arbitrum', 1313161554)

# Min Amounts from Avalanche
min_avax_to_zkevm = get_min_send_amount('Avalanche', 1101)
min_avax_to_opt = get_min_send_amount('Avalanche', 10)
min_avax_to_bsc = get_min_send_amount('Avalanche', 56)
min_avax_to_gno = get_min_send_amount('Avalanche', 100)
min_avax_to_matic = get_min_send_amount('Avalanche', 137)
min_avax_to_era = get_min_send_amount('Avalanche', 324)
min_avax_to_arb = get_min_send_amount('Avalanche', 42161)
min_avax_to_aur = get_min_send_amount('Avalanche', 1313161554)

# Max Amounts from Avalanche
max_avax_to_zkevm = get_max_send_amount('Avalanche', 1101)
max_avax_to_opt = get_max_send_amount('Avalanche', 10)
max_avax_to_bsc = get_max_send_amount('Avalanche', 56)
max_avax_to_gno = get_max_send_amount('Avalanche', 100)
max_avax_to_matic = get_max_send_amount('Avalanche', 137)
max_avax_to_era = get_max_send_amount('Avalanche', 324)
max_avax_to_arb = get_max_send_amount('Avalanche', 42161)
max_avax_to_aur = get_max_send_amount('Avalanche', 1313161554)

# Min Amounts from Aurora
min_aur_to_zkevm = get_min_send_amount('Aurora', 1101)
min_aur_to_opt = get_min_send_amount('Aurora', 10)
min_aur_to_bsc = get_min_send_amount('Aurora', 56)
min_aur_to_gno = get_min_send_amount('Aurora', 100)
min_aur_to_matic = get_min_send_amount('Aurora', 137)
min_aur_to_era = get_min_send_amount('Aurora', 324)
min_aur_to_arb = get_min_send_amount('Aurora', 42161)
min_aur_to_avax = get_min_send_amount('Aurora', 43114)

# Max Amounts from Aurora
max_aur_to_zkevm = get_max_send_amount('Aurora', 1101)
max_aur_to_opt = get_max_send_amount('Aurora', 10)
max_aur_to_bsc = get_max_send_amount('Aurora', 56)
max_aur_to_gno = get_max_send_amount('Aurora', 100)
max_aur_to_matic = get_max_send_amount('Aurora', 137)
max_aur_to_era = get_max_send_amount('Aurora', 324)
max_aur_to_arb = get_max_send_amount('Aurora', 42161)
max_aur_to_avax = get_max_send_amount('Aurora', 43114)

# Min Amounts from Fantom
min_ftm_to_opt = get_min_send_amount('Fantom', 10)
min_ftm_to_bsc = get_min_send_amount('Fantom', 56)
min_ftm_to_gno = get_min_send_amount('Fantom', 100)
min_ftm_to_matic = get_min_send_amount('Fantom', 137)
min_ftm_to_era = get_min_send_amount('Fantom', 324)
min_ftm_to_zkevm = get_min_send_amount('Fantom', 1101)
min_ftm_to_arb = get_min_send_amount('Fantom', 42161)
min_ftm_to_avax = get_min_send_amount('Fantom', 43114)
min_ftm_to_aur = get_min_send_amount('Fantom', 1313161554)

# Max Amounts from Fantom
max_ftm_to_opt = get_max_send_amount('Fantom', 10)
max_ftm_to_bsc = get_max_send_amount('Fantom', 56)
max_ftm_to_gno = get_max_send_amount('Fantom', 100)
max_ftm_to_matic = get_max_send_amount('Fantom', 137)
max_ftm_to_era = get_max_send_amount('Fantom', 324)
max_ftm_to_zkevm = get_max_send_amount('Fantom', 1101)
max_ftm_to_arb = get_max_send_amount('Fantom', 42161)
max_ftm_to_avax = get_max_send_amount('Fantom', 43114)
max_ftm_to_aur = get_max_send_amount('Fantom', 1313161554)

# Min Amounts to Fantom
min_eth_to_ftm = get_min_send_amount('Ethereum', 250)
min_opt_to_ftm = get_min_send_amount('Optimism', 250)
min_bsc_to_ftm = get_min_send_amount('BSC', 250)
min_matic_to_ftm = get_min_send_amount('Polygon', 250)
min_era_to_ftm = get_min_send_amount('zkSync', 250)
min_zkevm_to_ftm = get_min_send_amount('zkEVM', 250)
min_arb_to_ftm = get_min_send_amount('Arbitrum', 250)
min_avax_to_ftm = get_min_send_amount('Avalanche', 250)
min_aur_to_ftm = get_min_send_amount('Aurora', 250)
min_gno_to_ftm = get_min_send_amount('Gnosis', 250)

# Max mounts to Fantom
max_eth_to_ftm = get_max_send_amount('Ethereum', 250)
max_opt_to_ftm = get_max_send_amount('Optimism', 250)
max_bsc_to_ftm = get_max_send_amount('BSC', 250)
max_matic_to_ftm = get_max_send_amount('Polygon', 250)
max_era_to_ftm = get_max_send_amount('zkSync', 250)
max_zkevm_to_ftm = get_max_send_amount('zkEVM', 250)
max_arb_to_ftm = get_max_send_amount('Arbitrum', 250)
max_avax_to_ftm = get_max_send_amount('Avalanche', 250)
max_aur_to_ftm = get_max_send_amount('Aurora', 250)
max_gno_to_ftm = get_max_send_amount('Gnosis', 250)

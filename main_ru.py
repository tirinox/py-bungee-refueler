from config import *

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white>"
                          " | <level>{level: <8}</level>"
                          " | <cyan>{line}</cyan>"
                          " - <white>{message}</white>")

def minGasAmount(parent_chain,destination_chain) -> float:
     # From Ethereum
     if (parent_chain == 'ETH') and (destination_chain == 'ARB'):
          return MIN_ETH_TO_ARB 
     
     if (parent_chain == 'ETH') and (destination_chain == 'OPT'):
          return MIN_ETH_TO_OPT 
        
     if (parent_chain == 'ETH') and (destination_chain == 'BSC'):
          return MIN_ETH_TO_BSC 
     
     if (parent_chain == 'ETH') and (destination_chain == 'MATIC'):
          return MIN_ETH_TO_MATIC
      
     if (parent_chain == 'ETH') and (destination_chain == 'FTM'):
          return MIN_ETH_TO_FTM 
     if (parent_chain == 'ETH') and (destination_chain == 'AVAX'):
          return MIN_ETH_TO_AVAX 
     
     # From Arbitrum    
     if (parent_chain == 'ARB') and (destination_chain == 'OPT'):
          return MIN_ARB_TO_OPT 
          
     if (parent_chain == 'ARB') and (destination_chain == 'BSC'):
          return MIN_ARB_TO_BSC 
          
     if (parent_chain == 'ARB') and (destination_chain == 'MATIC'):
          return MIN_ARB_TO_MATIC
      
     if (parent_chain == 'ARB') and (destination_chain == 'FTM'):
          return MIN_ARB_TO_FTM
     
     if (parent_chain == 'ARB') and (destination_chain == 'AVAX'):
          return MIN_ARB_TO_AVAX
     
     # From Optimism    
     if (parent_chain == 'OPT') and (destination_chain == 'ARB'):
          return MIN_OPT_TO_ARB 
          
     if (parent_chain == 'OPT') and (destination_chain == 'BSC'):
          return MIN_OPT_TO_BSC 
          
     if (parent_chain == 'OPT') and (destination_chain == 'MATIC'):
          return MIN_OPT_TO_MATIC
      
     if (parent_chain == 'OPT') and (destination_chain == 'FTM'):
          return MIN_OPT_TO_FTM
      
     if (parent_chain == 'OPT') and (destination_chain == 'AVAX'):
          return MIN_OPT_TO_AVAX 
     
     # From BNB Chain    
     if (parent_chain == 'BSC') and (destination_chain == 'ARB'):
          return MIN_BSC_TO_ARB 
          
     if (parent_chain == 'BSC') and (destination_chain == 'OPT'):
          return MIN_BSC_TO_OPT 
          
     if (parent_chain == 'BSC') and (destination_chain == 'MATIC'):
          return MIN_BSC_TO_MATIC
      
     if (parent_chain == 'BSC') and (destination_chain == 'FTM'):
          return MIN_BSC_TO_FTM
      
     if (parent_chain == 'BSC') and (destination_chain == 'AVAX'):
          return MIN_BSC_TO_AVAX 
     
     # From Polygon 
     if (parent_chain == 'MATIC') and (destination_chain == 'ARB'):
          return MIN_MATIC_TO_ARB 
          
     if (parent_chain == 'MATIC') and (destination_chain == 'OPT'):
          return MIN_MATIC_TO_OPT 
          
     if (parent_chain == 'MATIC') and (destination_chain == 'BSC'):
          return MIN_MATIC_TO_BSC 
     
     if (parent_chain == 'MATIC') and (destination_chain == 'FTM'):
          return MIN_MATIC_TO_FTM
      
     if (parent_chain == 'MATIC') and (destination_chain == 'AVAX'):
          return MIN_MATIC_AVAX
     
     # From Fantom
     if (parent_chain == 'FTM') and (destination_chain == 'ARB'):
          return MIN_FTM_TO_ARB
               
     if (parent_chain == 'FTM') and (destination_chain == 'OPT'):
          return MIN_FTM_TO_OPT
               
     if (parent_chain == 'FTM') and (destination_chain == 'BSC'):
          return MIN_FTM_TO_BSC
              
     if (parent_chain == 'FTM') and (destination_chain == 'MATIC'):
          return MIN_FTM_TO_MATIC
     
     if (parent_chain == 'FTM') and (destination_chain == 'AVAX'):
          return MIN_FTM_TO_AVAX

     # From AVAX
     if (parent_chain == 'AVAX') and (destination_chain == 'ARB'):
          return MIN_AVAX_TO_ARB
               
     if (parent_chain == 'AVAX') and (destination_chain == 'OPT'):
          return MIN_AVAX_TO_OPT
               
     if (parent_chain == 'AVAX') and (destination_chain == 'BSC'):
          return MIN_AVAX_TO_BSC
              
     if (parent_chain == 'AVAX') and (destination_chain == 'MATIC'):
          return MIN_AVAX_TO_MATIC
     
     if (parent_chain == 'AVAX') and (destination_chain == 'FTM'):
          return MIN_AVAX_TO_FTM
            
def calculateGasPrice(private_key,tx:dict):
        w3 = Web3(Web3.HTTPProvider(rpc))
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        address = Web3.to_checksum_address(w3.eth.account.from_key(private_key).address)
        gas_price = w3.to_wei(str(w3.eth.gas_price), 'wei')
        gas_limit = 900_000   
        nonce = w3.eth.get_transaction_count(address)
        tx = {
            'nonce': nonce,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'value': w3.to_wei((gas_amount *1.3),'ether')
        }              
        estimated_gas = w3.eth.estimate_gas(tx)
        gas_limit = int(estimated_gas * 1.3)
        # update the update the gas-parameters of tx
        tx['gas'] = gas_limit
        return tx

def send_tx(args):
    #Function: depositNativeToken(uint256 destinationChainId,address _to)
    private_key, recipient_address = args
    address = None
    try:
        address = Web3.to_checksum_address(w3.eth.account.from_key(private_key).address)
        gas_price = w3.to_wei(str(w3.eth.gas_price), 'wei')
        gas_limit = 300_000   
        nonce = w3.eth.get_transaction_count(address)
        # Prepare the transaction data
        tx_data = {
            #'from': address,
            'nonce': nonce,
            'gas': gas_limit,
            'gasPrice': gas_price,
            'value': w3.to_wei((gas_amount*1.25),'ether')
        }
        #recalculate gas
        tx_data = calculateGasPrice(private_key=private_key,tx=tx_data)
        if True:
            transaction = contract_refuel.functions.depositNativeToken(destinationChainId,address).build_transaction(tx_data)
            
            # Sign the transaction with the receiver's private key
            signed_txn = w3.eth.account.sign_transaction(transaction,private_key=private_key)
            
            # Send the transaction to the network
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

            tx_hash = w3.to_hex(w3.keccak(signed_txn.rawTransaction))

            # Check if the transaction was successful
            if receipt['status'] == 1:
                logger.info(f'Refueling from {address} | {tx_explorer}tx/{tx_hash}')
                logger.info(f'Waiting for destination chain ({destination_chain}) {dist_tx_explorer}address/{address}/#internaltx')
            
            else:
                raise ValueError(f"Refueling from {address} failed with receipt status {receipt['status']}")
        elif tx_type == 0:
            #pass
            print('Here need implementation sending from one address to recipients...')
    except Exception as error:
        logger.error(f'{address} | {error}')

if __name__ == '__main__':
    print('-' * 108)
    print((' '*32)+'BUNGEE BATCH REFUELER'+(' '*32))
    print('-' * 108)
    print('Выберите сеть отправки:')
    print('1. ETH')
    print('2. ARB')
    print('3. OPT')
    print('4. BSC')
    print('5. MATIC')
    print('6. FTM')
    print('7. AVAX')
    parent_chain = input('Введите короткое название сети: ')
    parent_chain = parent_chain.upper()
    if parent_chain == 'ETH':
         chainId = 1
         rpc = RPC_ETH
         contract = BUNGEE_ETH_ROUNER
         tx_explorer = EXP_ETH
    elif parent_chain == 'ARB':
         chainId = 42161
         rpc = RPC_ARB
         contract = BUNGEE_ARB_ROUNER
         tx_explorer = EXP_ARB
    elif parent_chain == 'OPT':
         chainId = 10
         rpc = RPC_OPT
         contract = BUNGEE_OPT_ROUTER
         tx_explorer = EXP_OPT
    elif parent_chain == 'BSC':
         chainId = 56
         rpc = RPC_BSC
         contract = BUNGEE_BSC_ROUTER
         tx_explorer = EXP_BSC
    elif parent_chain == 'MATIC':
         chainId = 137
         rpc = RPC_MATIC
         contract = BUNGEE_MATIC_ROUNER
         tx_explorer = EXP_MATIC
    elif parent_chain == 'FTM':
         chainId = 250
         rpc = RPC_FTM
         contract = BUNGEE_FTM_ROUNER
         tx_explorer = EXP_FTM
    elif parent_chain == 'AVAX':
         chainId = 43114
         rpc = RPC_AVAX
         contract = BUNGEE_AVAX_ROUNER
         tx_explorer = EXP_AVAX

    print(f'{parent_chain} выбрана в качестве исходной сети для отправки газа')

    destinationChainId = chainId
    while (destinationChainId ==  chainId):
        destination_chain = input(f'Выберите сеть назначения(ETH и {parent_chain} не могут быть выбраны): ')
        destination_chain = destination_chain.upper()

        if destination_chain == 'ETH':
            print(f'{destination_chain} не может быть выбрана в качестве сети назначения')
            
        elif destination_chain == 'ARB':
            destinationChainId = 42161
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_ARB

        elif destination_chain == 'OPT':
            destinationChainId = 10
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_OPT

        elif destination_chain == 'BSC':
            destinationChainId = 56
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_BSC

        elif destination_chain == 'MATIC':
            destinationChainId = 137
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_MATIC

        elif destination_chain == 'FTM':
            destinationChainId = 250
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_FTM

        elif destination_chain == 'AVAX':
            destinationChainId = 43114
            gas_amount = minGasAmount(parent_chain,destination_chain)
            dist_tx_explorer = EXP_AVAX
    #Select sending method     
    tx_type = 0
    print('Выберите метод рассылки газа:')
    print("'0' - Отправлять с одного адреса(default)")
    print("'1' - Отправлять с каждого адреса")
    tx_type = input('Введите требуемый метод: ')              
    print(f'Начинаю отправлять газ из {parent_chain} в {destination_chain}')
    print(f'Минимальное количество газа: {gas_amount} + 25%')
    
    w3 = Web3(Web3.HTTPProvider(rpc))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    #Loads recipient_addresses
    with open('recipient_addresses.txt', 'r', encoding='utf-8-sig') as file:
            recipient_addresses = file.read().strip().replace('\n', '').replace(' ', '')  
    #Loads ABI for contracts
    with open('ABI/socket.json', 'r', encoding='utf-8-sig') as file:
            SOCKET_ABI = file.read().strip().replace('\n', '').replace(' ', '')   
    contract_refuel = w3.eth.contract(address=Web3.to_checksum_address(contract),
                               abi=SOCKET_ABI)
    
    #Loads private_keys
    with open('accounts.txt', encoding='utf-8-sig') as file:
        private_keys = [row.strip() for row in file]
    num_wallets = len(private_keys)
    logger.info(f'Загружено {num_wallets} кошельков')

    processed_addresses = 0
    while processed_addresses < num_wallets:
        with Pool(processes=len(private_keys)) as executor:
            args = zip(private_keys[processed_addresses:], [recipient_addresses] * (num_wallets - processed_addresses))
            executor.map(send_tx, args)
        processed_addresses += num_wallets - processed_addresses

    input('Для выхода нажмите любую клавишу..')
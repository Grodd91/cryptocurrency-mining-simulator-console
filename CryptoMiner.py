import hashlib
import time
def proof_of_work(block, difficulty):
    target = '0' * difficulty
    bitcoin = 0
    max_iterations = 1000000
    while bitcoin < max_iterations:
        block_with_nonce = block + str(bitcoin)
        block_hash = hashlib.sha256(block_with_nonce.encode()).hexdigest()
        if block_hash[:difficulty] == target:
            return bitcoin
        bitcoin += 1
    raise Exception('Could not find bitcoin within the given number of iterations.')
difficulty = 4
previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
while True:
    transaction_list = [f"transaction{i}" for i in range(3)]
    block_data = previous_hash + "".join(transaction_list)
    start_time = time.time()
    new_bitcoin = proof_of_work(block_data, difficulty)
    end_time = time.time()
    block_with_new_bitcoin = block_data + str(new_bitcoin)
    new_hash = hashlib.sha256(block_with_new_bitcoin.encode()).hexdigest()
    print(f"New block mined with bitcoin: {new_bitcoin}, hash: {new_hash}, time: {end_time - start_time:.2f}s")
    previous_hash = new_hash

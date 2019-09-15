import os, binascii

def fetch():
    instruction = input("Next instruction: ")
    print("Received: " + instruction)
    print("Fetched: " + instruction)
    return instruction

def decode(instruction):
    decoded = binascii.b2a_hex(os.urandom(15))
    print("Decoded: " + instruction + " as " + decoded.decode('utf-8'))
    return decoded

def execute(decoded):
    print("Executed: " + decoded.decode('utf-8'))
    return decoded

def memory(decoded):
    print("Finished memory operation with: " + decoded.decode('utf-8'))
    return decoded

def writeback(decoded):
    print("Finished writeback operation with: " + decoded.decode('utf-8'))
    return decoded

def run():
    while True:
        instruction = fetch()
        decoded = decode(instruction)
        execution = execute(decoded)
        memoryOp = memory(execution)
        writeback(memoryOp)
        print("Finished cpu operation with: " + instruction)

def main():
    run()

if __name__ == '__main__':
    main()

# Version 1: Basic Subnet Counter

def calculate_basic():
    print("--- Subnet Calculator (First Try) ---")
    addr = input("Enter IP with CIDR (e.g. 192.168.1.0/24): ")
    
    try:
        # Split IP and Prefix
        ip, prefix = addr.split("/")
        prefix = int(prefix)
        
        if not (0 <= prefix <= 32):
            print("Invalid Prefix.")
            return

        # Math for usable hosts: 2^(32 - prefix) - 2
        host_bits = 32 - prefix
        number_of_hosts = (2 ** host_bits) - 2
        
        # If prefix is 32, hosts = 1 (Loopback), if 31, hosts = 0 (P2P)
        if number_of_hosts < 0: number_of_hosts = 0

        print(f"\nIP Address: {ip}")
        print(f"Prefix: /{prefix}")
        print(f"Usable Hosts: {number_of_hosts}")
        print("Note: This version doesn't calculate Network/Broadcast addresses yet.")

    except ValueError:
        print("Error: Use format IP/Prefix (e.g. 10.0.0.0/8)")

if __name__ == "__main__":
    calculate_basic()
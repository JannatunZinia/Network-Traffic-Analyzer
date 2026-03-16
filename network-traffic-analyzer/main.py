"""
Simple Network Traffic Analyzer using Scapy.

This script captures network packets and counts the number of TCP, UDP, ICMP, and other packets.
"""

from scapy.all import sniff, TCP, UDP, ICMP, get_if_list
from collections import Counter
import sys

# Dictionary to hold protocol counts
protocol_counts = Counter()

def packet_callback(packet):
    if packet.haslayer(TCP):
        protocol_counts['TCP'] += 1
    elif packet.haslayer(UDP):
        protocol_counts['UDP'] += 1
    elif packet.haslayer(ICMP):
        protocol_counts['ICMP'] += 1
    else:
        protocol_counts['Other'] += 1

def main():
    # List available interfaces
    interfaces = get_if_list()
    print("Available network interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")
    
    # Prompt user to select an interface (optional, defaults to None for auto-detection)
    try:
        iface_choice = int(input("Select interface number (or press Enter for default): ").strip() or -1)
        iface = interfaces[iface_choice] if 0 <= iface_choice < len(interfaces) else None
    except ValueError:
        iface = None
    
    print(f"Starting packet capture on interface '{iface}'... Press Ctrl+C to stop.")
    try:
        # Capture for a limited time or indefinitely; adjust timeout as needed
        sniff(iface=iface, prn=packet_callback, store=0, timeout=60)  # 60-second timeout for testing
    except KeyboardInterrupt:
        pass
    except PermissionError:
        print("Error: Permission denied. Run as administrator (on Windows) or with sudo (on Linux/Mac).")
        sys.exit(1)
    except Exception as e:
        print(f"Error during capture: {e}")
        sys.exit(1)
    
    print("\nCapture stopped.")
    print("Packet statistics:")
    for proto, count in protocol_counts.items():
        print(f"{proto}: {count} packets")

if __name__ == "__main__":
    main()
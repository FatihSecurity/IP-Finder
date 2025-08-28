import socket

def ip_finder():
    domain = input("Enter a domain (e.g. google.com): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is: {ip}")
    except socket.gaierror:
        print("Invalid domain!")

if __name__ == "__main__":
    ip_finder()

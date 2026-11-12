from commands.ip import lookup_ip

def main():
    ip_address = input("IP : ")
    data = lookup_ip(ip_address)
    
    if data:
        print(f"IP      : {data['query']}")
        print(f"Country : {data['country']}")
        print(f"City    : {data['city']}")
        print(f"ISP     : {data['isp']}")
    else:
        print("Lookup failed.")

if __name__ == "__main__":
    main()
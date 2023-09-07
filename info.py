import requests
import json

def get_ip_info(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    return response.json()

def main():
    option = input("Enter 'S' for single IP or 'B' for bulk IP lookup: ").strip().lower()

    if option == 's':
        ip = input("Enter the IP address you want to look up: ")
        ip_info = get_ip_info(ip)
        
        save_option = input("Save the IP data as JSON? (yes/no): ").strip().lower()
        if save_option == 'yes':
            filename = input("Enter the filename (leave empty for default 'ip_data.json'): ").strip()
            if not filename:
                filename = 'ip_data.json'
            with open(filename, 'w') as file:
                json.dump(ip_info, file, indent=4)
                print(f'IP data saved to {filename}')
        else:
            print("IP data not saved.")

    elif option == 'b':
        file_name = input("Enter the name of the text file containing a list of IP addresses (one per line): ").strip()
        
        with open(file_name, 'r') as file:
            bulk_ips = [line.strip() for line in file]

        bulk_data = {}
        
        for ip in bulk_ips:
            ip_info = get_ip_info(ip)
            bulk_data[ip] = ip_info

        save_option = input("Save the bulk IP data as JSON? (yes/no): ").strip().lower()
        if save_option == 'yes':
            filename = input("Enter the filename (leave empty for default 'bulk_ip_data.json'): ").strip()
            if not filename:
                filename = 'bulk_ip_data.json'
            with open(filename, 'w') as file:
                json.dump(bulk_data, file, indent=4)
                print(f'Bulk IP data saved to {filename}')
        else:
            print("Bulk IP data not saved.")

    else:
        print("Invalid option. Please enter 'S' or 'B'.")

if __name__ == "__main__":
    main()

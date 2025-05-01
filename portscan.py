import socket 

def port_scan(): 
    target = input("Enter IP Address you want to scan: ")

    ports = [21, 22, 25, 80, 443, 3389, 3306, 8080]

    print(f"Performing a port scan on: {target}")


    with open("scan_results.txt", "w") as file: 
        file.write(f"Port Scan results for {target}\n")
        file.write("-" *50 + "\n")
        file.write("PORT\tSTATUS\tBANNER\n")

    
        for port in ports: 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                status  = "OPEN"
                banner = "NO BANNER"

            try:
                s.send(b'HELLO\r\n')
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            except:
                status = "CLOSED"
                banner = "No INFO"
                pass

                print (f"Port {port}: Open")
                file.write(f"{port}\t{status}\t{banner}\n")
        else:
            print(f"Port {port} Closed")
            file.write(f"{port}\tCLOSED\t-\n")

        s.close()
        
        file.write("\nScan complete")

        print(f"Scan Complete, Resuslts saved to scan ResuLts.txt")

if __name__ == "__main__":
    port_scan()
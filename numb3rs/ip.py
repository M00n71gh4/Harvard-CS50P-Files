import ipaddress
import csv

# Define the IPv4 address range you want
start_ip = "0.0.0.0"
end_ip = "255.255.255.255"

# Convert the start and end IPs to IPv4 objects
start = ipaddress.IPv4Address(start_ip)
end = ipaddress.IPv4Address(end_ip)

# Create a list of IP addresses in the range
ip_range = [str(ip) for ip in range(int(start), int(end) + 1)]

# Specify the CSV file path
csv_file = "ipv4_ranges.csv"

# Write the IP addresses to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["IPv4 Address"])
    writer.writerows([[ip] for ip in ip_range])

print(f"CSV file '{csv_file}' with IPv4 ranges generated successfully.")
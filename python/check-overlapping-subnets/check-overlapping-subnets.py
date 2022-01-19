from ipaddress import IPv4Address, IPv4Network

lines = []
with open("routes.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

search_pattern = input("Enter a CIDR subnet to check: ")

for route in lines:
    IPv4Network(route).overlaps(IPv4Network(search_pattern))
    if IPv4Network(route).overlaps(IPv4Network(search_pattern)):
        print(search_pattern, "Overlaps with", route)

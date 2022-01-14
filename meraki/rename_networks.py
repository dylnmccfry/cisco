import meraki, json, operator

API_KEY = open('api-key.txt').read()
dashboard = meraki.DashboardAPI(API_KEY)
organization_id = 'XXXX'

response = dashboard.organizations.getOrganizationNetworks(
    organization_id, total_pages='all'
)

for network in response:
    network_id = network['id']
    network_name = network['name']
    network_name_split_list = network_name.split()
    list_length = len(network_name_split_list)
    if list_length > 2:
#Always take list item 2 and list item 1 and put it at the end
        network_item_to_move1 = network_name_split_list[2]
        network_item_to_move2 = network_name_split_list[1]
        network_name_split_list.append(network_name_split_list.pop(network_name_split_list.index(network_item_to_move2)))
        network_name_split_list.append(network_name_split_list.pop(network_name_split_list.index(network_item_to_move1)))
        reordered_network_name = " "
        reordered_network_name = reordered_network_name.join(network_name_split_list)
#Renaming section using Meraki Python Library
        response = dashboard.networks.updateNetwork(
            network_id,
            name=reordered_network_name)
        print(response)

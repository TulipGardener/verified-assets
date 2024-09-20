from copy import deepcopy
import json
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURRENT_DIR, '..', '..', 'assets.json'), 'r') as infile:
	assets = json.load(infile)

with open(os.path.join(CURRENT_DIR, '..', '..', 'chains.json'), 'r') as infile:
	chains = json.load(infile)

with open(os.path.join(CURRENT_DIR, '..', '..', 'cdn.json'), 'r') as infile:
	cdn = json.load(infile)

data = []

for asset in assets:
	final_asset = deepcopy(asset)

	# Update the icon to use the proper full cdn path
	final_asset['icon'] = cdn['icon'] + final_asset['icon']

	for network in final_asset["networks"]:

		# Convert chainPath to chainId
		major_network, chain = network['chainPath'].split('.')
		network["chainId"] = chains[major_network][chain]
		
		# And remove chainPath
		del network['chainPath']

	data.append(final_asset)

print(json.dumps(data, indent = 4))

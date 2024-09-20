from copy import deepcopy
import json
import os


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(CURRENT_DIR, 'assets.json'), 'r') as infile:
	assets = json.load(infile)

with open(os.path.join(CURRENT_DIR, 'chains.json'), 'r') as infile:
	chains = json.load(infile)

with open(os.path.join(CURRENT_DIR, 'cdn.json'), 'r') as infile:
	cdn = json.load(infile)

local_data = []
cdn_data = []

for asset in assets:
	final_asset = deepcopy(asset)

	for network in final_asset["networks"]:

		# Convert chainPath to chainId
		major_network, chain = network['chainPath'].split('.')
		network["chainId"] = chains[major_network][chain]
		
		# And remove chainPath
		del network['chainPath']

	# write out the local version
	local_data.append(deepcopy(final_asset))

	# Update the icon to use the proper full cdn path
	final_asset['icon'] = cdn['icon'] + final_asset['icon']
	cdn_data.append(final_asset)

with open('assets.local.gen.json', 'w') as f:
	# use separators to minify output
    json.dump(local_data, f, separators=(',', ':'))

with open('assets.cdn.gen.json', 'w') as f:
	# use separators to minify output
    json.dump(cdn_data, f, separators=(',', ':'))

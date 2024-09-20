import * as fs from 'fs';
import * as path from 'path';

// Get the current directory
const CURRENT_DIR = path.dirname(__filename);

// Load JSON files
const assets = JSON.parse(fs.readFileSync(path.join(CURRENT_DIR,  '..', '..', 'assets.json'), 'utf-8'));
const chains = JSON.parse(fs.readFileSync(path.join(CURRENT_DIR,  '..', '..', 'chains.json'), 'utf-8'));
const cdn = JSON.parse(fs.readFileSync(path.join(CURRENT_DIR,  '..', '..', 'cdn.json'), 'utf-8'));

let data: any[] = [];

for (const asset of assets) {
    // Deepcopy the asset
    const finalAsset = JSON.parse(JSON.stringify(asset));

    // Update the icon to use the proper full cdn path
    finalAsset['icon'] = cdn['icon'] + finalAsset['icon'];

    for (const network of finalAsset["networks"]) {
        // Convert chainPath to chainId
        const [majorNetwork, chain] = network['chainPath'].split('.');
        network["chainId"] = chains[majorNetwork][chain];

        // Remove chainPath
        delete network['chainPath'];
    }

    data.push(finalAsset);
}

// Log the resulting JSON to the console
console.log(JSON.stringify(data, null, 4));

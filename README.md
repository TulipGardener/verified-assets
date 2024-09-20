# Fuel Verified Assets

To keep our users safe and secure, Fuel has compiled this official list of verified assets that will be available at network launch.

Developers wishing to maintain a full list of on-chain assets should develop their own indexed solutions and be aware of the security risks that might exist by doing so.

## Included Files

### assets.json

This is the list of assets that have been verified by the Fuel team. It contains critical information such as asset ids, chain information, and so on.

There are also lists to icons. If you chose to use those icons, please host them yourselves to be polite to Fuel's CDN.

### chains.json

This is the list of chains associated with various assets.

The reference `chainPath` in the assets entries contains `'major_network.chain_name'` references that can be used to look up the proper chain id in this chains.json file.

### cdn.json

This is the cdn where icons are hosted. Please be polite when using this CDN and cache all images yourself to help with Fuel's bandwidth costs.

### Examples Folder

This folder contains examples of how to build fully composed JSON from each of the three files above that would be used in a project. Please feel free to adapt to your purposes.

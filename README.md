# Fuel Verified Assets

To keep our users safe and secure, Fuel has compiled this official list of verified assets that are available across our network.

Developers wishing to maintain a full list of on-chain assets should develop their own indexed solutions and be aware of the security risks that might exist by doing so.

## Using this repository

The information in this repository is published to a CDN maintained by Fuel. The current list of verified assets can be found at the following URL:

    https://verified-assets.fuel.network/assets.json

Any projects wishing to use this information are welcome to, however this is done at your own risk.



## Included Files

### assets.json

This is the list of assets that have been verified by the Fuel team. It contains critical information such as asset ids, chain information, and so on.

There are also lists to icons. If you chose to use those icons, please host them yourselves to be polite to Fuel's CDN.

### chains.json

This is the list of chains associated with various assets.

The reference `chainPath` in the assets entries contains `'major_network.chain_name'` references that can be used to look up the proper chain id in this chains.json file.

### cdn.json

This is the cdn where icons are hosted. Please be polite when using this CDN and cache all images yourself to help with Fuel's bandwidth costs.

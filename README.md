# Fuel Verified Assets

To keep our users safe and secure, Fuel has compiled this official list of verified assets that are available across our network.

Developers wishing to maintain a full list of on-chain assets should develop their own indexed solutions and be aware of the security risks that might exist by doing so.

## Using this repository

The information in this repository is published to a CDN maintained by Fuel. The current list of verified assets can be found at the following URL:

    https://verified-assets.fuel.network/assets.json

Any projects wishing to use this information are welcome to, however this is done at your own risk.

You can also download the latest asset information and icons in a single archive. This is great if you want to locally cache this list, or include it as part of a release pipeline in your own tools and libraries:

    https://verified-assets.fuel.network/latest.zip

## Submitting new assets

To submit new assets for inclusion in the verified assets list, [open a new Issue](https://github.com/FuelLabs/verified-assets/issues/new?assignees=&labels=update+info&projects=&template=submit_info.yml&title=Update+info+for+ASSET_NAME). Be sure to fill out all the fields on the issue form.

## Included Files

### assets.json

This is the list of assets that have been verified by the Fuel team. It contains critical information such as asset ids, chain information, and so on.

There are also lists to icons. If you chose to use those icons, please host them yourselves to be polite to Fuel's CDN.

### chains.json

This is the list of chains associated with various assets.

The reference `chainPath` in the assets entries contains `'major_network.chain_name'` references that can be used to look up the proper chain id in this chains.json file.

### cdn.json

This is the cdn where icons are hosted. Please be polite when using this CDN and cache all images yourself to help with Fuel's bandwidth costs.

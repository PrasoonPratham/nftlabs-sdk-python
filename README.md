# NFTLabs Python SDK

PyPi package found [here](https://pypi.org/project/thirdweb-sdk).

## Deprecation Notice

> The `nftlabs-sdk` pypi package will be deprecated on November 30th, 2021
>
> Please make sure you install the new `thirdweb-sdk` package found [here](https://pypi.org/project/thirdweb-sdk)
>
> In your code, update all imports to use the `thirdweb` package and switch to using the `ThirdwebSdk` package (instead of the `NftlabsSdk` package)


### Docs
https://docs.nftlabs.co

### API Reference
https://python-docs.nftlabs.co/



## Installing the SDK

```bash
$ pip install thirdweb-sdk
```



## Package Structure

```
nftlabs
├── abi       // contains autogenerated ABI contract wrappers 
├── errors    // commonly thrown errors
├── modules   // NFT, Currency, Marketplace, Pack, Collection, etc modules
├── options   // Options classes used throughout the SDK
├── sdk.py    // NftlabsSdk class, wrapper for the entire package
├── storage   // Distributed file storage helper classes
└── types     // Types consumed by some of the methods exposed in the modules
```

## Calling the modules

You can call the NFTLabs modules by instantiating an SDK object and fetching the module with your contract address
like this:

```python
import os
from nftlabs import NftlabsSdk, SdkOptions

sdk = NftlabsSdk(SdkOptions(), "https://rpc-mumbai.maticvigil.com") # polygon testnet as an example

# Assumes your private key is assigned to the `PKEY` environment variable
sdk.set_private_key(os.getenv("PKEY"))

# Put your NFT contract address here if you want to mint your own NFTs!
nft_module = sdk.get_nft_module("0xbDfF8fb43688fB4D2184DF8029A7238ac1413A24")
print(nft_module.total_supply())
```

## Development

### Generating ABI wrappers

The `abi` package contains autogenerated code compiled by the
0xchain `abi-gen` tool found [here](https://www.npmjs.com/package/@0x/abi-gen).

Our protocols are developer at [this repo](https://github.com/nftlabs/nftlabs-protocols).

Install the `abi-gen` cli tool and use it to compile abi wrappers like this:

```bash
$ # assumes you have the nftlabs-protocols repo cloned in the parent directory
$ abi-gen --language Python -o nftlabs/abi --abis ../nftlabs-protocols/abi/NFT.json
```

Anytime there are ABI contract changes, you should regenerate the abi wrappers.

require("@nomicfoundation/hardhat-toolbox");
require('hardhat-contract-sizer');
require('dotenv').config();

/** @type import('hardhat/config').HardhatUserConfig */

module.exports = {
  networks: {
    hardhat: {
      chainId: 1337
    },
    mainnet: {
      url: process.env.INFURA_NODE,
      accounts: [process.env.PRIVATE_KEY]
    },
    goerli: {
      url: process.env.INFURA_NODE_GOERLI,
      accounts: [process.env.PRIVATE_KEY_TEST]
    }
  },
  solidity: {
    version: "0.8.7",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  }
};

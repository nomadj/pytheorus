const hre = require("hardhat");

async function main() {
  const Pytheorus = await hre.ethers.getContractFactory("Pytheorus");
  const pytheorus = await Pytheorus.deploy();

  await pytheorus.deployed();

  console.log(
    `Pytheorus deployed to ${pytheorus.address}`
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

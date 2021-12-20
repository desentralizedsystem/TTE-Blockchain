const sign = artifacts.require("sign");

module.exports = function (deployer) {
  deployer.deploy(sign);
};

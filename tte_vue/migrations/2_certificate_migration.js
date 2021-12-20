const digitalCertificate = artifacts.require("digitalCertificate");

module.exports = function (deployer) {
  deployer.deploy(digitalCertificate);
};

pragma solidity 0.8.4;

contract digitalCertificate {
    
    mapping(string => Certificate) public certificates;
    
    struct Certificate{
        string email;
        string key_url;
        string cert_url;
    }

    function addCertificate (string memory email, string memory key_url, string memory cert_url) public {
        certificates[email]=Certificate(email,key_url,cert_url);
    }
}
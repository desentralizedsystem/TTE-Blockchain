pragma solidity 0.8.4;

contract sign {
    struct Signer{
        string email;
        string first_name;
        string last_name;
        string file_url;
        string hash;
    }
     
    mapping (uint => Signer[]) public document;
    mapping (string => Signer[]) public docValidate;

    function addSigner(uint _docId,string memory _email,string memory _fname,string memory _lname,string memory _url,string memory _hash)public{
        document[_docId].push(Signer(_email,_fname,_lname,_url,_hash));
        docValidate[_hash].push(Signer(_email,_fname,_lname,_url,_hash));
    }

    function countSigner(uint  _docId) public view returns (uint){
        return document[_docId].length;
    }
    
    function countSignerValidate(string memory _hash) public view returns (uint){
        return docValidate[_hash].length;
    }

}
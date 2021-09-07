//SPDX-License-Identifier: MIT

pragma solidity ^0.6.2;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v3.1.0/contracts/access/Ownable.sol";

// @dev: This creates a  simple struct to map three integers as ids of materials, processes, and outputs encapsulating material passports.
// @user: it takes into account ids passed on from Blender/Topologic as dictionaries belonging to lists.

contract Mat_passport is Ownable{
   struct MaterialID {
      uint inputID;
      uint processID;
      uint outputID;
   }
   MaterialID materialID;

   function setMaterialID(uint _inputID, uint _processID, uint _outputID ) public {
      materialID = MaterialID(_inputID, _processID, _outputID);
   }
   function getInputID() public view returns (uint) {
      return materialID.inputID;
   }

   function getOutputID() public view returns (uint) {
      return materialID.outputID;
   }

   function getProcessID() public view returns (uint) {
      return materialID.processID;
   }
}

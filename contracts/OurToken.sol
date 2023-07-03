// SPDX-License-Identifier: MIT 
// SPDX-Licence-Identifier: GPL-3.0

pragma solidity ^0.8.18;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OurToken is ERC20{
    
    constructor(uint256 initialSupply) ERC20("OurToken", "OT"){
        _mint(msg.sender, initialSupply);
    }
   

}
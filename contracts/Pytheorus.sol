// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Pytheorus is ERC721, Ownable {
	using Strings for uint256;

	uint256 private _tokenId;
	bool public _requestsEnabled;
	mapping (uint256 => Token) private _tokens;
	Student[] private _pending;
	Student[] private _students;
	mapping (address => bool) private _accepted;
	mapping (uint256 => string) private _tokenURIs;

	struct Student {
		string name;
		bool isApproved;
		address addr;
	}

	struct Token {
		string name;
		string composer;
		uint256 blockNumber;
		uint256 timeStamp;
 		string uri;
		uint256 tokenId;
	}

	constructor() ERC721("Pytheorus", "PYUS") {
		_tokenId = 0;
		_requestsEnabled = true;
	}

	function _setTokenURI(uint256 tokenId_, string memory tokenURI_) internal {
		require(_exists(tokenId_), "ERC721Metadata: URI set of nonexistent token");
		_tokenURIs[tokenId_] = tokenURI_;
	}

	function tokenURI(uint256 tokenId_) public view override returns (string memory) {
		require(_exists(tokenId_), "ERC721Metadata: URI query for nonexistent token");
		string memory _tokenURI = _tokenURIs[tokenId_];
		string memory base = _baseURI();

		if (bytes(base).length == 0) {
			return _tokenURI;
		}
		
		if (bytes(_tokenURI).length > 0) {
			return string(abi.encodePacked(base, _tokenURI));
		}
		return string(abi.encodePacked(base, tokenId_.toString()));
	}

	function toggleRequestsEnabled() public onlyOwner {
		_requestsEnabled = !_requestsEnabled;
	}

	function mint(address to_, string memory uri_, string memory name_, string memory composer_) public {
		require(_accepted[_msgSender()], "You are not authorized for this operation.");
		_mint(to_, _tokenId);
		_setTokenURI(_tokenId, uri_);
		Token memory token = Token({ name: name_, composer: composer_, blockNumber: block.number, timeStamp: block.timestamp, uri: uri_, tokenId: _tokenId});
		_tokens[_tokenId] = token;
		_tokenId++;
	}

	function _msgValue() internal view returns (uint256) {
		return msg.value;
	}
	
	function requestApproval(string memory name_) public {
		require(_requestsEnabled, "Requests are not being accepted at this time.");
		Student memory student = Student({ name: name_, isApproved: false, addr: _msgSender() });
		_pending.push(student);
	}

	function getPendingStudents() public view onlyOwner returns (Student[] memory) {
		return _pending;
	}

	function getStudents() public view returns (Student[] memory) {
		return _students;
	}

	function getToken(uint256 tokenId_) public view returns (Token memory) {
		return _tokens[tokenId_];
	}

	function approveOrDenyStudent(uint256 index, bool decision) public onlyOwner {
		Student storage student = _pending[index];
		if (decision) {
			student.isApproved = true;
			_accepted[student.addr] = true;
			_students.push(student);
		}
		_pending[index] = _pending[_pending.length - 1];
		_pending.pop();
	}
}

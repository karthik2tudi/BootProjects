package com.rt.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
/**
 * For NRI's we want to save/update/delete thru this controller
 * 
 */
@RestController
@RequestMapping(path = "/nri")
public class NRIPersonController {
	
	
	@GetMapping(path = "/getPersons")
	public ResponseEntity<String> getPersonDetails() {
		boolean flag = true;
		if (flag == true) {
			return new ResponseEntity<>("NRI Person details fetched successfully through Get Method ", HttpStatus.OK);
		} else {
			return new ResponseEntity<>("NRI Person details not present in DB ", HttpStatus.NOT_FOUND);
		}
	}

	@PostMapping(path = "/savePerson")
	public ResponseEntity<String> savePerson() {
		return new ResponseEntity<String>("NRI person details saved successfully thr POST method", HttpStatus.CREATED);
	}
	
	
	@PutMapping(path = "/updatePerson")
	public ResponseEntity<String> updatePerson() {
		boolean flag = false;
		if (flag == true) {
		return new ResponseEntity<String>("NRI person details updated successfully thr PUT method", HttpStatus.OK);
		} else {
			return new ResponseEntity<String>("NRI person details not found in DB with that ID ", HttpStatus.NOT_FOUND);
		}
	}
	
	@DeleteMapping(path = "/deletePerson")
	public ResponseEntity<String> deletePerson() {
		boolean flag = false;
		if (flag == true) {
		return new ResponseEntity<String>("NRI person details deleted successfully thr DELETE method", HttpStatus.OK);
		} else {
			return new ResponseEntity<String>("NRI person details not found in DB with that ID ", HttpStatus.NOT_FOUND);
		}
	}

}

package com.rt.controller;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.rt.Exception.DataNotFoundException;

/**
 * Indian persons want save/get/update/delete through this controller
 * 
 */
@RestController
@RequestMapping(path = "/indian")  //global path
public class PersonController {

	@GetMapping(path = "/persons")
	public ResponseEntity<?> getPersonDetails() {
		boolean flag = false;
		if (flag == true) {
			return new ResponseEntity<>("Indian Person details fetched successfully through Get Method ", HttpStatus.OK);
		} else {
			return new ResponseEntity<>(new DataNotFoundException("data not found thr custom Exception"), HttpStatus.NOT_FOUND);
		}
	}

	@PostMapping(path = "/persons")
	public ResponseEntity<String> savePerson() {
		return new ResponseEntity<String>("Indian Person details saved successfully thr POST method", HttpStatus.CREATED);
	}
	
	
	@PutMapping(path = "/persons")
	public ResponseEntity<String> updatePerson() {
		boolean flag = false;
		if (flag == true) {
		return new ResponseEntity<String>("Indian Person details updated successfully thr PUT method", HttpStatus.OK);
		} else {
			return new ResponseEntity<String>("Indian Person details not found in DB with that ID ", HttpStatus.NOT_FOUND);
		}
	}
	
	@DeleteMapping(path = "/persons")
	public ResponseEntity<String> deletePerson() {
		boolean flag = false;
		if (flag == true) {
		return new ResponseEntity<String>("Indian Person details deleted successfully thr DELETE method", HttpStatus.OK);
		} else {
			return new ResponseEntity<String>("Indian Person details not found in DB with that ID ", HttpStatus.NOT_FOUND);
		}
	}

}

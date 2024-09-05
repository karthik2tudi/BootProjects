package com.rt.Exception;

public class DataNotFoundException extends Exception{

	private String message;

	public DataNotFoundException(String message) {
		super();
		this.message = message;
	}
	
	
}

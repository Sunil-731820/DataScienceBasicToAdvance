package com.java.jsf.PrimeFaces;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;

@ManagedBean
@SessionScoped
public class UserBean {
	
	private String username;

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}
	
	
	public String getUser() {
		String response = "";
		if(username!=null) {
			response = "The User is "+ username;
		}
		return response;
	}

}

package com.java.jsf.Navigation;

import java.io.Serializable;
import javax.faces.bean.ManagedBean;
import javax.faces.bean.SessionScoped;

@ManagedBean
@SessionScoped
public class Mobile implements Serializable {
	private static final long serialVersionUID = 4672207931321758371L;
	private String mname;
	private String color;
	private String Id;
	private String model;
	private String regno;

	public Mobile() {
	}

	public Mobile(String mname, String color, String model) {
		this.mname = mname;
		this.color = color;
		this.model = model;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getMname() {
		System.out.println("Mobile name is" + mname);
		return mname;
	}

	public void setCname(String mname) {
		this.mname = mname;
	}

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public String add() {
		return "form";
	}

	public String view() {
		return "form";
	}
}

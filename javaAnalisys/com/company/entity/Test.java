package com.company.entity;

public class Test {
	 
	private int id;
	private String description;
	private String link;
	private int userId;
	
	public Test(int id, String description, String link, int userId) {
		super();
		this.id = id;
		this.description = description;
		this.link = link;
		this.userId = userId;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getLink() {
		return link;
	}

	public void setLink(String link) {
		this.link = link;
	}

	public int getUserId() {
		return userId;
	}

	public void setUserId(int userId) {
		this.userId = userId;
	}
	
}

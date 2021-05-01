package com.company.controllers;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.LinkedList;
import java.util.List;

import com.company.data.interfaces.IDB;
import com.company.entity.Test;

public class CompanyController {
	IDB db;
	public CompanyController(IDB db) {
		this.db = db;
	}
	
	
	public List<Test> getAllTests() {
		
		 Connection con = null;
	        try {
	            con = db.getConnection();
	            String sql = "SELECT * FROM tests";
	            Statement st = con.createStatement();

	            ResultSet rs = st.executeQuery(sql);
	            List<Test> tests = new LinkedList<>();
	          
	            while (rs.next()) {
	            	 Test test = new Test(rs.getInt("test_id"), rs.getString("test_description"), rs.getString("test_link"), rs.getInt("user_id"));
	            	 tests.add(test);
	            }

	            return tests;
	        } catch (SQLException throwables) {
	            throwables.printStackTrace();
	        } catch (ClassNotFoundException e) {
	            e.printStackTrace();
	        } finally {
	            try {
	                con.close();
	            } catch (SQLException throwables) {
	                throwables.printStackTrace();
	            }
	        }
	        return null;
	    }
	
}

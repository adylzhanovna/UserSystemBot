package com.company.controllers;

import java.io.File;
import java.sql.Date;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import com.company.entity.Test;




public class XmlCreater {
	 
	
	public void createXml(String file, List<Test> tests) {
		 try {
			 
	            DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance(); // documentfactory
	 
	            DocumentBuilder documentBuilder = documentFactory.newDocumentBuilder(); // documenybuilder
	 
	            Document document = documentBuilder.newDocument(); // create a new document xml
	 
	           	           
	            
	            Element root = document.createElement("information"); 
	            document.appendChild(root); 
	             System.out.println(tests);
	            for(Test test: tests) {  
	            System.out.println(test.getId());		
	            	Element first = document.createElement("test"); 
		            root.appendChild(first); 
	 
	           
	    
	            Element carnumber = document.createElement("testId"); 
	            carnumber.appendChild(document.createTextNode(test.getId() + "")); 
	            first.appendChild(carnumber); 
	            
	            Element carclass = document.createElement("testDescription"); 
	            carclass.appendChild(document.createTextNode(test.getDescription())); 
	            first.appendChild(carclass); 
	            
	            Element firstname = document.createElement("testLink"); 
	            firstname.appendChild(document.createTextNode(test.getLink())); 
	            first.appendChild(firstname); 
	 
	          
	            Element lastname = document.createElement("testUserId"); 
	            lastname.appendChild(document.createTextNode(test.getUserId() + "")); 
	            first.appendChild(lastname); 
	 
	        
	             
	            
	              
	            }  
	             
	            TransformerFactory transformerFactory = TransformerFactory.newInstance(); 
	            Transformer transformer = transformerFactory.newTransformer(); 
	            DOMSource domSource = new DOMSource(document); 
	            
	            	StreamResult streamResult = new StreamResult(new File(file)); 
	            	transformer.transform(domSource, streamResult);
	           
	        } catch (ParserConfigurationException pce) {
	            pce.printStackTrace();
	        } catch (TransformerException tfe) {
	            tfe.printStackTrace();
	        }
	    }
}

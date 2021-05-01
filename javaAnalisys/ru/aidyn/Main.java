package ru.aidyn;
import com.company.controllers.CompanyController;
import com.company.controllers.XmlCreater;
import com.company.data.PostgresDB;
import com.company.data.interfaces.IDB;

public class Main {
	
	public static void main(String[] args) {
		System.out.println("ëxample!");
		IDB db = new PostgresDB();
		CompanyController controller = new CompanyController(db);
		XmlCreater xml = new XmlCreater();
		xml.createXml("test.xml", controller.getAllTests());
	}
}

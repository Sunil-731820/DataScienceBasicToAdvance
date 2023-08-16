package com.java.jsf;

public class StrinBufferExample { 
	public static void main(String[] args) {
		StringBuffer str = new StringBuffer();
		System.out.println("String is : ="+str);
		if(str.isEmpty()) {
			System.out.println("EMoty ="+str);
		}else {
			System.out.println("Filled : =");
		}
//		if(str.equals("")) {
//			System.out.println("HIIIIIII");
//		}else {
//			System.out.println("HELLLOOOOOOO");
//		}
//		String str1 = ;
//		if(str.equals()) {
//			System.out.println("Fileddd");
//			
//		}else {
//			System.out.println("Empty String////////");
//		}
		
//		StringBuffer stringBuffer = new StringBuffer();
//        stringBuffer.append("Hello");
//
// 
//
//        String emptyString = "";
//
//        String stringBufferContents = stringBuffer.toString();
//        System.out.println(stringBufferContents);
//        if (emptyString.equals(stringBufferContents)) {
//            System.out.println("The StringBuffer is empty.");
//        } else {
//            System.out.println("The StringBuffer is not empty.");
//        }
//		
		String str21 = "Sunil:";
		if(str21==null) {
			System.out.println("NULL    :");
		}else {
			System.out.println("Hello : "+str21);
			
		}
	}

}

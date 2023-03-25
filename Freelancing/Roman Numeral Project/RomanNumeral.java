import java.util.*;  

// Base class to store roman and arabic values
public class RomanNumeral {
    private String roman;
    private int arabic;

    // Function to convert Roman to Arabic
    public static int RomanToArabic(String roman){
        Map<Character, Integer> mapper=new HashMap<Character, Integer>();  
        //Mapping the letter to their corresponding value
        mapper.put('M',1000);  
        mapper.put('D',500);  
        mapper.put('C',100);  
        mapper.put('L',50);  
        mapper.put('X',10);  
        mapper.put('V',5);  
        mapper.put('I',1);  
        // Replacing romans with a simpler format
        roman = roman.replace("IV","IIII");  
        roman = roman.replace("IX","VIIII");  
        roman = roman.replace("XL","XXXX");  
        roman = roman.replace("XC","LXXXX");  
        roman = roman.replace("CD","CCCC");  
        roman = roman.replace("CM","DCCCC");  
        int arabic = 0;  
        // iterating through the roman string and calculating the arabic value
        for (int i = 0; i < roman.length(); i++)  
        {  
            arabic = arabic + (mapper.get(roman.charAt(i)));  
        }  
        return arabic;
    }
    
    //Constructor
    RomanNumeral(String romanValue){
        this.roman = romanValue;        
        this.arabic = RomanToArabic(romanValue);
    }
    
    // getters & setters
    public String getRomanValue(){
        return this.roman;
    }

    public void setRomanValue(String value){
        this.roman = value;
    } 

    public int getArabicValue(){
        return this.arabic;
    }

    public void setArabicValue(int value){
        this.arabic = value;
    } 

    public boolean equals(int value){
        return value==this.arabic;
    }

    public String toString(){
        String output = "Arabic vaule: "+this.arabic+"\n Roman Value : "+this.roman;
        return output;
    }

    // Override the compareTo() method
    @Override public int compareTo(RomanNumeral rm)
    {
        if (this.arabic > rm.getArabicValue()) {
            return 1;
        }
        else if (this.arabic == rm.getArabicValue()) {
            return 0;
        }
        else {
            return -1;
        }
    }
}

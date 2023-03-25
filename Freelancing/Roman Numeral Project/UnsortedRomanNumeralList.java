import java.util.*;
// Class for the unsorted list of roman numerals
public class UnsortedRomanNumeralList extends RomanNumeralList{
    
    // method to add new roman numerals to the list
    public void append(RomanNumeral roman_numeral){
        this.listofRomanNumerals.addLast(roman_numeral);
    }

    //returns a string with the unsorted arabic values 
    public String displayArabicList(){
        String result = "";
        for(int i=0;i<this.listofRomanNumerals.size();i++){
            result = result + listofRomanNumerals.get(i).getArabicValue()+"\n";
        }
        return result;
    }

    //returns a string with the unsorted roman values 
    public String displayRomanList(){
        String result = "";
        for(int i=0;i<this.listofRomanNumerals.size();i++){
            result = result + listofRomanNumerals.get(i).getRomanValue()+"\n";
        }
        return result;
    }
}

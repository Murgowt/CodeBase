import java.util.Collections;
import java.util.Comparator;

// Class for the sorted list of roman numerals
public class SortedRomanNumeralList extends RomanNumeralList{
    public void add(RomanNumeral roman_numeral){
        this.listofRomanNumerals.add(roman_numeral);
        //Custom sorting
        Collections.sort(this.listofRomanNumerals,new Comparator<RomanNumeral>() {
            @Override
            public int compare(RomanNumeral o1, RomanNumeral o2) {
                return o1.getArabicValue() - o2.getArabicValue();
            }
        });
    }

    //returns a string with the sorted arabic values 
    public String displayArabicList(){
        String result = "";
        for(int i=0;i<this.listofRomanNumerals.size();i++){
            result = result + listofRomanNumerals.get(i).getArabicValue()+"\n";
        }
        return result;
    }
}

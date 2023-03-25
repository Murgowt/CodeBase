import java.util.Scanner;  

// Driver Class
public class project2 {
    public static void main(String args[]){
        //Taking the input of the number of romans
        int num_of_romans ;
        Scanner sc = new Scanner(System.in);  
        System.out.print("Enter the number of roman numericals: ");
        num_of_romans = sc.nextInt();

        // Creating objects for sorted & unsorted lists
        UnsortedRomanNumeralList unsorted_list = new UnsortedRomanNumeralList();
        SortedRomanNumeralList sorted_list = new SortedRomanNumeralList();
        
        //Taking the input from user
        for(int i=0;i<num_of_romans;i++){
            System.out.print("Enter the roman value: ");
            String roman_numerical = sc.next();
            //Creating a RomanNumerical object with the entered value
            RomanNumeral romanNumerical = new RomanNumeral(roman_numerical);
            //adding the object to the sorted and unsorted lists
            unsorted_list.append(romanNumerical);
            sorted_list.add(romanNumerical);
        } 
        // Formulating the outputs
        String unsorted_roman_list = unsorted_list.displayRomanList();
        String unsorted_arabic_list = unsorted_list.displayArabicList();
        String sorted_list_arabic = sorted_list.displayArabicList();
        
        // Displaying the output on a GUI grid
        RomanNumeralGUI.display(unsorted_roman_list,unsorted_arabic_list, sorted_list_arabic);

        // Closing the scanner 
        sc.close();
    }
}

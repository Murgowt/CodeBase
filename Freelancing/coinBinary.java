import java.util.Scanner;
class coinBinary{
    public static void main(String args[]){
        // Declaring variables
        int number;
        Scanner sc = new Scanner(System.in);

        // Taking the input from the user
        while(true){
            System.out.print("Enter an integer representing the state of the coins: ");
            number= sc.nextInt();
            // If the number entered is greater than 511 or less than 0; we prompt the user to enter a number again
            if(number<0 || number >511){
                System.out.println("Please enter a number between 0 to 511.");
            }
            else{
                break;
            }
        }
        //Converting the number to binary String
        String coins = Integer.toBinaryString(number);

        //Padding zeros to make the length equal to 9
        int length_value = coins.length();
        while(length_value<9){
            coins = "0"+coins;
            length_value=length_value+1;
        }

        //Displaying the output to the user
        String line="";
        for(int i=0;i<9;i++){
            //It is Tails if the bit is 1; else H
            if(coins.charAt(i)=='1'){
                line = line + "T";
            }
            else{
                line = line + "H";
            }

            // Change to new line after every 3 bits
            if(i%3==2){
                System.out.println(line);
                line = "";
            }
            else{
                line = line + " ";
            }
            
        }   
        //Closing the scanner
        sc.close();
    }   
}
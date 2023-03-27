import program1;
import javax.swing.JOptionPane;

public class program2 {

    public static int  getIntegerInput(boolean lowerLimitFlag, int lowerLimit, boolean upperLimitFlag,
    int upperLimit, String prompt, String errorMsg){
        while(true){
            boolean flag = true;
            try{
                String inputString = JOptionPane.showInputDialog(null, prompt);
                Integer input = Integer.parseInt(inputString);
                if(lowerLimitFlag && input<lowerLimit ){
                    flag = false;
                }
                if(upperLimitFlag && upperLimit<input){
                    flag = false;
                }
                if(flag){
                    JOptionPane.showMessageDialog(null, "You entered "+inputString);
                    return input;
                }
                else{
                    JOptionPane.showMessageDialog(null,errorMsg);
                }
                
            }
            catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(null, errorMsg);
            }
        }
        
    }

    public static double calculateTravelCharges(int route_num, int num_of_passengers){
        double amount=0;
        if(route_num == 1){
            if(num_of_passengers==1){
                amount = 35;
            }
            else if (num_of_passengers==2){
                amount = 60;
            }
            else{
                amount = 26.5 * num_of_passengers;
            }
        }
        else if (route_num == 2){
            if(num_of_passengers==1){
                amount = 32.89;
            }
            else if (num_of_passengers==2){
                amount = 53.12;
            }
            else{
                amount = 24.2 * num_of_passengers;
            }
        }
        else{
            if(num_of_passengers==1){
                amount = 38;
            }
            else if (num_of_passengers==2){
                amount = 63.78;
            }
            else{
                amount = 28.78 * num_of_passengers;
            }
        }
        return amount;
    }

    public static double  calculateTravelCharges(int route_num){
        double amount=0;
        if(route_num == 1){
            amount = 35;
        }
        else if (route_num == 2){
            amount = 32.89;
        }
        else{
            amount = 38;
        }
        return amount;
    }

    public static  double calculateMembershipDiscount(double travelCharges, double discountRate){
        double amount =travelCharges*(discountRate)/100;
        return amount;
    }

    public static double calculateCouponDiscount(double travelCharges, int numPassengers){
        return 5;
    }

    public static double calculateFirstTimeUserDiscount(double travelCharges, double discountRate){
        double amount =travelCharges*(discountRate)/100;
        return amount;
    }

    public static double calculateSalesTax(double travelCharges, double taxRate){
        return travelCharges * taxRate/100;
    }
    public static void main(String args[]){
        int route_num = getIntegerInput(true, 1, true, 3, "Which route would you like to travel (1-3)?", "Invalid option, please select a valid route (1-3)");
        int num_of_passengers = getIntegerInput(true, 1, false, 10, "How many passengers?", "Invalid input,please enter a valid passengers count.");
        int member = getIntegerInput(true, 0, true, 1, "Are you a member (0=no, 1=yes)?", "Invalid input, please enter 0 or 1.");
        int firstTimeUser = getIntegerInput(true, 0, true, 1, "Are you a first-time user (0=no, 1=yes)?", "Invalid input, please enter 0 or 1.");
        int coupon = getIntegerInput(true, 0, true, 1, "Do you have a coupon (0=no, 1=yes)?", "Invalid input, please enter 0 or 1.");
        double travelCharges,membershipDiscount,firstTimeUserDiscount,membership,firstTime;
        if(num_of_passengers==1){
             travelCharges = calculateTravelCharges( route_num);
        }
        else{
            travelCharges = calculateTravelCharges( route_num,  num_of_passengers);
        }

        if(num_of_passengers==1){
             membershipDiscount = calculateMembershipDiscount(travelCharges, member*5);
             membership=5;
             firstTime = 10;
             firstTimeUserDiscount = calculateFirstTimeUserDiscount(travelCharges, firstTimeUser*10);
        }
        else if (num_of_passengers==2){
             membershipDiscount = calculateMembershipDiscount(travelCharges, member*6.2);
             firstTimeUserDiscount = calculateFirstTimeUserDiscount(travelCharges, firstTimeUser*7);
             membership=6.2;
             firstTime = 7;
        }
        else{
             membershipDiscount = calculateMembershipDiscount(travelCharges, member*8);
             firstTimeUserDiscount = calculateFirstTimeUserDiscount(travelCharges, firstTimeUser*4);
             membership=8;
             firstTime = 4;
        }

        double couponDiscount = calculateCouponDiscount(travelCharges, num_of_passengers);
        
        double price = travelCharges-membershipDiscount-firstTimeUserDiscount-couponDiscount;
        double salesTax = calculateSalesTax(price, 7.5);
        double finalPrice = price + salesTax;

        String travelCoString = "Travel charges for "+num_of_passengers+" passengers on Route "+route_num+" : $"+String.format("%.2f", travelCharges);
        String membershipDiscountString = "Membership discount("+String.format("%.2f",membership)+"%): $"+String.format("%.2f", membershipDiscount);
        String firstTimeUserString = "First Time discount("+String.format("%.2f",firstTime)+"): $"+String.format("%.2f", firstTimeUserDiscount);
        String CouponDiscountString = "Coupon discount(5.00%): $"+String.format("%.2f", membershipDiscount);
        String SalesTaxString = "Sales Tax applied(7.5%): $"+String.format("%.2f", salesTax);
        String priceString = "Final charge: $"+String.format("%.2f",finalPrice);
        String finalString = travelCoString;
        if(member==1){
            finalString = finalString+"\n"+membershipDiscountString;
        }
        if(firstTimeUser==1){
            finalString = finalString +"\n"+firstTimeUserString;
        }
        if(coupon==1){
            finalString = finalString + "\n" + CouponDiscountString;
        }
        finalString = finalString + "\n" + "Charges after applying applicable discounts: $"+String.format("%.2f", price);
        finalString = finalString + "\n" + SalesTaxString;
        finalString =  finalString +"\n"+ priceString;
        System.out.println(finalString);
        JOptionPane.showMessageDialog(null, finalString);
    }
}

import javax.swing.JFrame;
import javax.swing.JOptionPane;
public class program1 {
    public static void getIntegerInput(boolean lowerLimitFlag, int lowerLimit, boolean upperLimitFlag,
    int upperLimit, String prompt, String errorMsg){
        JFrame frame = new JFrame();
        while(true){
            boolean flag = true;
            try{
                String inputString = JOptionPane.showInputDialog(frame, prompt);
                Integer input = Integer.parseInt(inputString);
                if(lowerLimitFlag && input<lowerLimit ){
                    flag = false;
                }
                if(upperLimitFlag && upperLimit<input){
                    flag = false;
                }
                if(flag){
                    JOptionPane.showMessageDialog(null, "You entered "+inputString);
                    return;
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
    public static void main(String args []){
        String prompt = "Please enter an integer between 1 to 100";
        String errorMsg = "Invalid input, Please enter an integer between 1 to 100";
        boolean lowerLimitFlag = true;
        boolean upperLimitFlag = true;
        int lowerLimit = 0;
        int upperLimit = 100;
        getIntegerInput(lowerLimitFlag, lowerLimit, upperLimitFlag, upperLimit, prompt, errorMsg);
    }
}

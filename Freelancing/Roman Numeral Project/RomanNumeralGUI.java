import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
//Class for displaying the information on GUI
public class RomanNumeralGUI {
    static JFrame f;
    static JTable j;
    public static void display(String unsortedListRomans, String unsortedArabics, String sortedArabics){
        f = new JFrame();
 
        f.setTitle("Roman Numerals");
        String[][] data = {
            { unsortedListRomans, unsortedArabics, sortedArabics }
        };
        String[] columnNames = { "Original Roman Values", "Unsorted Arabic values", "Sorted Arabic values" };
         j = new JTable(data, columnNames);
        j.setBounds(30, 40, 200, 300);
         JScrollPane sp = new JScrollPane(j);
        f.add(sp);
        f.setSize(500, 200);
        f.setVisible(true);
    }
}

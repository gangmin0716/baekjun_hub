import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String result = "";
        
        for (int i = 0; i < a.length(); i++){
            char a_ch = a.charAt(i); 
            if (Character.isUpperCase(a_ch)){
                result += Character.toLowerCase(a_ch);
            } else {
                result += Character.toUpperCase(a_ch);
            }
        }
        
        System.out.print(result);
    }
}
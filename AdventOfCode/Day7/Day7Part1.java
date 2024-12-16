import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day7Part1 {

    static boolean is_valid(long target, int value, List<Integer> values) {
        if (target == value && values.isEmpty()){
            return true;
        }
        if (value <= 0 || values.isEmpty()){
            return false;
        }
        else{
            if (target%value != 0){
                int newValue = values.getFirst();
                List<Integer> clone = new ArrayList<Integer>(values);
                clone.removeFirst();
                return is_valid(target-value, newValue, clone);
            }
            else{
                int newValue = values.getFirst();
                List<Integer> clone = new ArrayList<Integer>(values);
                clone.removeFirst();
                if (is_valid(target-value, newValue, clone)) {
                    return true;
                }
                return is_valid(Math.floorDiv(target, value), newValue, clone);
            }
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        File my_file = new File("file_path");
        Scanner my_scanner = new Scanner(my_file);

        List<Long> targets = new ArrayList<Long>();
        List<List<Integer>> nums = new ArrayList<>();

        while (my_scanner.hasNextLine()) {
            String line = my_scanner.nextLine();
            String[] my_string = line.split(": ");
            targets.add(Long.parseLong(my_string[0]));

            ArrayList<Integer> num = new ArrayList<>();
            String[] numbers = my_string[1].split(" ");
            for (String number : numbers) {
                num.add(Integer.parseInt(number));
            }
            nums.add(num.reversed());
        }
        my_scanner.close();

        long sol = 0;
        for (int i = 0; i < nums.size(); i++) {
            List<Integer> currentNums = new ArrayList<>(nums.get(i));
            int first = currentNums.removeFirst();
            if (is_valid(targets.get(i), first, currentNums)) {
                sol += targets.get(i);
            }
        }

        System.out.println(sol);
    }
}

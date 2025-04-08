package List;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        // Array
        String[] ninjasArray = new String[3];
        ninjasArray[0] = "Ninjas";
        ninjasArray[1] = "Bruno";
        ninjasArray[2] = "Louco";

        List<String> ninjasList = new ArrayList<>();
        ninjasList.add("Naruto Uzumaki");
        ninjasList.add("Naruto Uchiha");
        ninjasList.add("Naruto Hyuuga");

        System.out.println("Ninjas: " + ninjasList);

        ninjasList.remove("Naruto Uzumaki");
        System.out.println("Ninjas: " + ninjasList);

        // Trocar elementos

        System.out.println(ninjasList.get(3));
    }
}

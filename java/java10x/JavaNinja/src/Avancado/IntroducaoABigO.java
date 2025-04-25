package Avancado;

import java.util.ArrayList;

public class IntroducaoABigO {


    public static void main(String[] args) {
        ArrayList<Ninjas> ninjas = new ArrayList<Ninjas>();
        ninjas.add(new Ninjas("Naruto Uzumaki", 17));
        ninjas.add(new Ninjas("Sasuke Uchiha", 20));
        ninjas.add(new Ninjas("Kakashi Hatake", 37));

        System.out.println(ninjas);

        System.out.println("++++++++++++++++++++++++++++++");

        // Algoritimo - o(1) - complexidade constante
        System.out.println(ninjas.get(1));

        System.out.println("++++++++++++++++++++++++++++++");

        // Algoritmo - o(n) - complexidade linear
        for (int i = 0; i < ninjas.size(); i++) {
            System.out.println(ninjas.get(i));
                for (int j = 0; j < ninjas.size(); j++) {
                    System.out.println(ninjas.get(j) + " vs " + ninjas.get(i));
                }
        }
    }

}

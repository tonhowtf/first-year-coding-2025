package Basico;

public class Array {
    public static void main(String[] args) {

        /*String ninja1 = "Naruto Uzumaki";
        String ninja2 = "Sasuke Uchiha";
        String ninja3 = "Sakura Haruno";
        */

        String[] ninja = new String[6];
        ninja[0] = "Naruto Uzumaki";
        ninja[1] = "Sasuke Uchiha";
        ninja[2] = "Sakura Haruno";
        ninja[3] = "Hinata Hyuga";

        System.out.println(ninja[5]);

        // Redeclarar
        ninja = new String[7];
        ninja[0] = "Hashirama senju";
        ninja[1] = "Tobirama Senju";
        ninja[2] = "Hiruzen Sarutobi";
        ninja[3] = "Minato Namikaze";
        ninja[4] = "Tsunade senju";
        ninja[5] = "Kakashi Hatake";

        for(int i = 0; i < 7 ; i++){
            System.out.println(ninja[i]);
        }

        int[] idade = new int[2];

        double[] flutuante = new double[1];


        /*String nomeDoNinja1 = "Gaara do deserto";
        String nomeDoNinja2 = "Rock Lee";*/
    }
}

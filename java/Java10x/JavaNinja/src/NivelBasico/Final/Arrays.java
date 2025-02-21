package NivelBasico.Final;

public class Arrays {
    public static void main(String[] args) {

        String[][] ninjaEAldeias = new String[3][3];

        ninjaEAldeias[0][0] = "Konoha";
        ninjaEAldeias[0][1] = "Naruto Uzumaki";
        ninjaEAldeias[0][2] = "Sasuke Uchiha";

        ninjaEAldeias[1][0] = "Nevoa";
        ninjaEAldeias[1][1] = "Zabuza";
        ninjaEAldeias[1][2] = "Haku";

        ninjaEAldeias[2][0] = "Deserto";
        ninjaEAldeias[2][1] = "Gaara";
        ninjaEAldeias[2][2] = "Temari";

        for (int i = 0; i < ninjaEAldeias.length; i++) {
            System.out.println("Aldeias: " + ninjaEAldeias[i][0] + ", " + ninjaEAldeias[0][i]);
        }
    }
}

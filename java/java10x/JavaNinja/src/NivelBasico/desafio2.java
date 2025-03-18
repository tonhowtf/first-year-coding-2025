package NivelBasico;
import java.util.Scanner;

public class desafio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] ninjas = new String[6];
        int i = 0;
        while(true){
            System.out.println("Menu:");
            System.out.println("1 - Cadastrar Ninja");
            System.out.println("2 - Listar Ninjas");
            System.out.println("0 - Sair");
            int opcao = sc.nextInt();


            switch(opcao){
                case 1:
                    System.out.println("Digite o nome do ninja: ");
                    String ninja = sc.next();
                    ninjas[i] = ninja;
                    i++;
                    break;
                case 2:
                    for(String ninjaa : ninjas){
                        System.out.println(ninjaa);
                    }
                case 0:
                    break;

                default:
                    System.out.println("Opção inválida!");
                    continue;

            }

            if (opcao == 0) {
                break;
            }
        }

    }
    }


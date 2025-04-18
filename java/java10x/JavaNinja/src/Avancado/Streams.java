package Avancado;

import java.util.ArrayList;
import java.util.List;

public class Streams {
    public static void main(String[] args) {


        List<Ninja> ninjas = new ArrayList<>();
        ninjas.add(new Ninja("Naruto Uzumaki", "Konoha", 17));
        ninjas.add(new Ninja("Sakura Haruno", "Konoha", 17));
        ninjas.add(new Ninja("Sasuke Uchiha", "Konoha", 17));
        ninjas.add(new Ninja("Kakashi Hatake", "Konoha", 30));
        ninjas.add(new Ninja("Hinata Hyuga", "Konoha", 16));
        ninjas.add(new Ninja("Shikamaru Nara", "Konoha", 17));
        ninjas.add(new Ninja("Ino Yamanaka", "Konoha", 17));
        ninjas.add(new Ninja("Choji Akimichi", "Konoha", 17));
        ninjas.add(new Ninja("Neji Hyuga", "Konoha", 18));
        ninjas.add(new Ninja("Rock Lee", "Konoha", 17));
        ninjas.add(new Ninja("Tenten", "Konoha", 17));
        ninjas.add(new Ninja("Gaara", "Suna", 17));
        ninjas.add(new Ninja("Kankuro", "Suna", 19));
        ninjas.add(new Ninja("Temari", "Suna", 20));
        ninjas.add(new Ninja("Itachi Uchiha", "Akatsuki", 21));
        ninjas.add(new Ninja("Kisame Hoshigaki", "Akatsuki", 32));
        ninjas.add(new Ninja("Deidara", "Akatsuki", 19));
        ninjas.add(new Ninja("Sasori", "Akatsuki", 35));
        ninjas.add(new Ninja("Hidan", "Akatsuki", 22));
        ninjas.add(new Ninja("Kakuzu", "Akatsuki", 91));


        // Filter Filtragem dos ninja
        // .stream
        /*ninjas.stream().filter(ninja -> ninja.getVila()
                .equals("Suna"))
                .forEach(System.out::println);*/

        // Sorted Ordenação
      /*  ninjas.stream()
                .sorted((n1, n2) -> Integer.compare(n1.getIdade(), n2.getIdade()))
                .forEach(System.out::println);
    }*/
        /*ninjas.stream().sorted((n1, n2) -> n1.getNome().compareToIgnoreCase(n2.getNome()))
                .forEach(System.out::println);
    }*/
        // MAP
        /*ninjas.stream()
                .map(Ninja::getNome)
                .forEach(System.out::println);*/

       Ninja ninjaMaisvelho = ninjas.stream()
                .max((n1, n2) -> Integer.compare(n1.getIdade(), n2.getIdade()))
                .orElse(null);

       System.out.println(ninjaMaisvelho);
    }
}


import java.time.LocalDateTime

fun main(){

println(somar())

}

fun saudacao(hora: Int): Int {
    val horaDefault = LocalDateTime.now()

    when(hora){
        in 6..11 -> "Bom dia"
        in 12..17 -> "Boa tarde"
        in 18..23 -> "Boa noite"
        in 0..5 -> "Boa madrugada"
        else -> horaDefault
    }
}
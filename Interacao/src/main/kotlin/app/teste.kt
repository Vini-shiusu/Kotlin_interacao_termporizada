package app


import configuracao.Conexao
import dominio.Resposta
import repositorio.RespostaRepositorio
import javax.swing.JOptionPane.showInputDialog
import javax.swing.JOptionPane.showMessageDialog

fun main() {

    val jdbcTemplate = Conexao().getJdbcTemplate()
    val repositorio = RespostaRepositorio(jdbcTemplate)

    showMessageDialog(null, "alguem está usando este pc?")
    var resposta:Int = showInputDialog(null,"Se alguem estiver usando este pc, digite 1").toInt()

    if (resposta == 1) {
        showMessageDialog(null, "Obrigado pela confirmacao")
    }

    val RespostaAtual = Resposta(resposta)
    repositorio.inserir(RespostaAtual)

    println("Gravou amuain")

    val teste = repositorio.listar()
    teste.forEach {
        println(teste)
    }
}
package repositorio

import dominio.Resposta
import org.springframework.jdbc.core.BeanPropertyRowMapper
import org.springframework.jdbc.core.JdbcTemplate

class RespostaRepositorio(val jdbcTemplate: JdbcTemplate) {

    fun inserir(resposta: Resposta) {
        jdbcTemplate.update("""
            insert into respostaOcio (resposta, Data_hora) values
            (${resposta.resposta}, getDate())
        """)
    }

    fun listar():List<Resposta> {
        return jdbcTemplate.query("select resposta from respostaOcio",
            BeanPropertyRowMapper(Resposta::class.java)
        )
    }
}
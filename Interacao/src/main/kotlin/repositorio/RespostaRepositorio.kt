package repositorio

import dominio.Resposta
import org.springframework.jdbc.core.BeanPropertyRowMapper
import org.springframework.jdbc.core.JdbcTemplate

class RespostaRepositorio(val jdbcTemplate: JdbcTemplate) {

    fun inserir(resposta: Resposta) {
        jdbcTemplate.update("""
            insert into respostaTB (ID, resposta) values
            (3, ${resposta.resposta})
        """)
    }

    fun listar():List<Resposta> {
        return jdbcTemplate.query("select * from respostaTB",
            BeanPropertyRowMapper(Resposta::class.java)
        )
    }
}
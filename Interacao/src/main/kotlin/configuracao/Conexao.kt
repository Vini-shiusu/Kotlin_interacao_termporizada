package configuracao

import org.apache.commons.dbcp2.BasicDataSource
import org.springframework.jdbc.core.JdbcTemplate

class Conexao {
    val driverClassName = "org.h2.Driver"
    val url = "jdbc:h2:./banco-h2"
    val username = "teste"
    val password = "123"

    fun getJdbcTemplate(): JdbcTemplate {
        val dataSource = BasicDataSource()
        dataSource.driverClassName = driverClassName
        dataSource.url = url
        dataSource.username = username
        dataSource.password = password

        val jdbcTemplate = JdbcTemplate(dataSource)
        return jdbcTemplate
    }
}
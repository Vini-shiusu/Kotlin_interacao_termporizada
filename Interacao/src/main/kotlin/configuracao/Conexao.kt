package configuracao

import org.apache.commons.dbcp2.BasicDataSource
import org.springframework.jdbc.core.JdbcTemplate

class Conexao {
    val driverClassName = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    val url = "jdbc:sqlserver://Turi.database.windows.net;databaseName=Turi"
    val username = "adm-turi"
    val password = "Urubu1002"

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
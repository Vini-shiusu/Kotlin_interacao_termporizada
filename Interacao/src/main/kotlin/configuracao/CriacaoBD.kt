package configuracao

fun main() {

    val jdbcTemplate = Conexao().getJdbcTemplate()

/*
método execute() -> executa qualquer tipo de instrução SQL
OBS: O ";" ao final da instrução é opcional, porém, se houverem
     mais de 1 instrução SQL, deve ter o ";" ao final de cada uma
 */
    jdbcTemplate.execute("""
        create table IF NOT EXISTS respostaTB (
            ID int PRIMARY KEY,
            resposta Int not null
        );
    """)
}
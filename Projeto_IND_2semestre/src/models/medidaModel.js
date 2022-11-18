var database = require("../database/config");

function buscarUltimasMedidas(limite_linhas) {

    instrucaoSql = ''


    if (process.env.AMBIENTE_PROCESSO == "desenvolvimento") {
        instrucaoSql = `select percent_cpu from memoria;
        `;
        console.log("Executando a instrução SQL: \n" + instrucaoSql);
         
 }
        else {
            console.log("\nO AMBIENTE (produção OU desenvolvimento) NÃO FOI DEFINIDO EM app.js\n");
            return
        }
        console.log("Executando a instrução SQL: \n" + instrucaoSql);
        return database.executar(instrucaoSql);
}

function buscarMedidasEmTempoReal() {

    instrucaoSql = ''

    if (process.env.AMBIENTE_PROCESSO == "desenvolvimento") {
        instrucaoSql = `select percent_cpu from memoria where id = 1;`;
        console.log("Executando a instrução SQL: \n" + instrucaoSql);
         database.executar(instrucaoSql);
        //  instrucaoSql = `select count(FkVotacao) as QtdAcao from Usuario where fkVotacao = 101;`;

        //  instrucaoSql = `select count(FkVotacao) as QtdTerror from Usuario where fkVotacao = 102;`;
        // console.log("Executando a instrução SQL: \n" + instrucaoSql);
        //  database.executar(instrucaoSql);
        //  instrucaoSql = `select count(FkVotacao) as QtdEstrategia from Usuario where fkVotacao = 103;`;

        //  instrucaoSql = `select count(FkVotacao) as QtdEsporte from Usuario where fkVotacao = 104;`;
        // console.log("Executando a instrução SQL: \n" + instrucaoSql);
        //  database.executar(instrucaoSql);
        //  instrucaoSql = `select count(FkVotacao) as QtdDiversao from Usuario where fkVotacao = 105;`;

        //  instrucaoSql = `select count(FkVotacao) as QtdFPS from Usuario where fkVotacao = 106;`;
        // console.log("Executando a instrução SQL: \n" + instrucaoSql);
        //  database.executar(instrucaoSql);
        //  instrucaoSql = `select count(FkVotacao) as QtdRPG from Usuario where fkVotacao = 107;`;
    } else {
        console.log("\nO AMBIENTE (produção OU desenvolvimento) NÃO FOI DEFINIDO EM app.js\n");
        return
    }

    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}


module.exports = {
    buscarUltimasMedidas,
    buscarMedidasEmTempoReal
}
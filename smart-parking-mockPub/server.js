const http = require("http");
const express = require("express");
const fs = require("fs");
const app = express();
const cors = require("cors");

app.use(cors());

app.get("/dadosSobreVagas", function(req, res) {
  fs.readFile("../smart-parking-api/dadosVagas.json", "utf-8", (err, data) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: "Erro ao ler o arquivo de dados" });
    } else {
      const dadosVagas = JSON.parse(data);
      res.json(dadosVagas);
    }
  });
});

app.get("/dadosPorLocalizacao/:localizacao", function(req, res) {
  const localizacaoParam = req.params.localizacao;

  fs.readFile("../smart-parking-api/dadosVagasFiltradas.json", "utf-8", (err, data) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: "Erro ao ler o arquivo de dados" });
    } else {
      const dadosVagas = JSON.parse(data);

      // Filtra os dados com base na localizacaoParam
      const dadosFiltrados = dadosVagas.filter(
        (dados) => dados.localizacao === localizacaoParam
      );

      if (dadosFiltrados.length > 0) {
        res.json(dadosFiltrados);
      } else {
        res.status(404).json({ error: "Localização não encontrada" });
      }
    }
  });
});

http.createServer(app).listen(3000, () =>
  console.log("Servidor rodando local na porta 3000")
);

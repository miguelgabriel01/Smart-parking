const axios = require('axios');
const fs = require('fs');

const file = '../smart-parking-api/situacaoVagaDoDispositivo.json'; // Coloque o caminho do seu arquivo JSON aqui

// Função para buscar o status e atualizar o arquivo JSON
async function updateFile() {
  try {
    const response = await axios.get('http://192.168.137.117/status');
    const data = response.data;

    // Ler o arquivo JSON existente
    const fileContent = JSON.parse(fs.readFileSync(file, 'utf8'));

    // Atualizar apenas o valor da chave "livre"
    fileContent.livre = data.vagaLivre;

    // Escrever de volta no arquivo mantendo a estrutura original
    const updatedFileContent = JSON.stringify(fileContent, null, 2);
    fs.writeFileSync(file, updatedFileContent);

    console.log('Valor da chave "livre" atualizado para:', fileContent.livre);
  } catch (error) {
    console.error('Erro ao atualizar o valor da chave "livre":', error.message);
  }
}

// Chamar a função a cada 3 segundos
setInterval(updateFile, 3000);
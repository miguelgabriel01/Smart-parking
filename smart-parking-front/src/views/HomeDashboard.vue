<template>
  <div id="dashboard">
    <SearchInput />
    <div class="dashboard-number">
      <p class="dashboard-number-texts">TOTAL DE VAGAS</p>
      <div class="vacancies">
        <div class="vacancies-number">
          <div class="vacancies-dashboard" style="background-color: #198f6c">
            {{ situacaoDoEstacionamento.data.vagasLivres }}
          </div>
          <p class="dashboard-number-texts">Livres</p>
        </div>
        <div class="vacancies-number">
          <div class="vacancies-dashboard" style="background-color: #e90b0b">
            {{ situacaoDoEstacionamento.data.vagasOcupadas }}
          </div>
          <p class="dashboard-number-texts">Ocupadas</p>
        </div>
      </div>
    </div>
    <div class="text-info">
      <small
        >Data: {{ situacaoDoEstacionamento.data.ultimaAtualizacaoData }}</small
      ><br />
      <small
        >Última Atualização:
        {{ situacaoDoEstacionamento.data.ultimaAtualizacaoHora }}</small
      ><br />
      <small>Local: {{ situacaoDoEstacionamento.data.localizacao }}</small>
    </div>
    <ButtomReload />
  </div>
</template>

<script>
import ButtomReload from "../components/ButtomReload.vue";
import SearchInput from "../components/SearchInput.vue";
import { api } from "../services.js";

export default {
  name: "HomePage",
  components: {
    ButtomReload,
    SearchInput,
  },
  data() {
    return {
      situacaoDoEstacionamento: null,
    };
  },
  methods: {
    getVagas() {
      setInterval(() => {
        console.log("entrou nesta merda");
        const selectedLocation = localStorage.getItem("selectedLocation");

        if (selectedLocation) {
          // O valor foi encontrado no localStorage
          console.log("Seleção da Localização:", selectedLocation);
        } else {
          // O valor não foi encontrado no localStorage ou é null/vazio
          console.log("Nenhuma seleção de localização encontrada.");
        }
        api.get("/dadosSobreVagas").then((response) => {
          console.log("response da api");
          console.log(response.data);
          this.situacaoDoEstacionamento = response;
        });

        if (this.situacaoDoEstacionamento == null) {
          this.$router.push({ path: "/errorpage" });
        }
      }, 2000);
    },
  },
  created() {
    this.getVagas();
  },
};
</script>

<style scoped>
/*Configurações globais*/
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#dashboard {
  margin: 0;
  padding: 0;
  position: relative;
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-direction: column;
}

.search-parking {
  width: 306px;
  height: 41px;
  border-radius: 9px;
  background-color: #f3f3f3;
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
  align-content: center;
  margin-top: 20px;
}

.info-parking {
  color: #9f9f9f;
  font-size: 15px;
  font-style: Bold;
  font-family: "Secular One", sans-serif;
}

.icon-search {
  width: 20px;
  margin-left: 7px;
}

.icon-options-parking {
  width: 35px;
}

.dashboard-number {
  width: 100%;
  height: 250px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  justify-content: space-around;
  margin-top: 20px;
}

.text-info {
  width: 100%;
  height: 80px;
  padding: 10px;
  margin-bottom: 30px;
}

small {
  color: #9f9f9f;
  font-size: 15px;
  font-style: Bold;
  font-family: "Secular One", sans-serif;
  margin-left: 5px;
}

.reload-info {
  width: 100%;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 90px;
}

.button-reload {
  background-color: #6f9aee;
  width: 250px;
  height: 60px;
  border-radius: 9px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.vacancies {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}

.vacancies-number {
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.vacancies-dashboard {
  width: 150px;
  height: 145px;
  background-color: red;
  border-radius: 9px;
  color: white;
  font-size: 59px;
  font-style: Bold;
  font-family: "Secular One", sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
}

.dashboard-number-texts {
  color: #9f9f9f;
  font-size: 20px;
  font-style: Bold;
  font-family: "Secular One", sans-serif;
}
</style>
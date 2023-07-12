<template>
    <div id="dashboard">
        <SearchInput/>
        <div class="dashboard-number">
            <p class="dashboard-number-texts">ESTACIONAMENTO</p>
            <div class="vacancies">
                <div class="vacanciesLeft">
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                </div>
                <div class="vacanciesRig">
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoLeft"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                    <div class="vagaEspacoRig"><img src="../assets/icons/carroVistoPorCimaCinza.png" alt="iconeDeCarro" class="imgCarro"></div>
                </div>
            </div>
        </div>
        <ButtomReload/>
    </div>
    
</template>

<script>
import ButtomReload from '../components/ButtomReload.vue'
import SearchInput from '../components/SearchInput.vue'
//import {api} from '../services.js'

export default {
    name: 'HomeParking',
  components: {
    ButtomReload,
    SearchInput,
  },
  data(){
    return{
    situacaoDoEstacionamento: null,
    }},
    methods:{
       /* getVagas(){
            setInterval(()=>{
                api.get('/dadosSobreVagas')
            .then(response => {
                console.log("response da api");
                console.log(response.data);
                this.situacaoDoEstacionamento = response
            })

             if(this.situacaoDoEstacionamento == null){
                    this.$router.push({path: '/errorpage'});
            } 

            },2000)
        }*/
    },
    created(){
        //this.getVagas()
    }
}
</script>

<style scoped>
/*Configurações globais*/
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

#dashboard{
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

.dashboard-number{
    width: 100%;
    height: 250px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    justify-content: space-around;
    margin-top: 20px;
}

.dashboard-number-texts{
    color:#9F9F9F;
    font-size:20px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
    padding: 15px;
}

.vacancies{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 5px;
}

.vacanciesLeft{
    width: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    flex-wrap: wrap;
}

.vacanciesRig{
    width: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
    flex-wrap: wrap;
}
.vagaEspacoLeft{
    width: 80px;
    height: 50px;
    border-top: 1px solid #9F9F9F;
    border-right: 1px solid #9F9F9F;
    border-bottom: 1px solid #9F9F9F;
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
}

.vagaEspacoRig{
    width: 80px;
    height: 50px;
    border-top: 1px solid #9F9F9F;
    border-left: 1px solid #9F9F9F;
    border-bottom: 1px solid #9F9F9F;
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
}

.imgCarro{
    width: 47px;
    height: 47px;
}
</style>

<template>
  <select class="search-parking" v-model="selectedLocation" @change="handleSelectionChange">
    <img src="../assets/icons/Vector.png" alt="" class="icon-search">
    <option value="">Procurar Estacionamento</option>
    <option v-for="location in locations" :key="location.value" :value="location.value">{{ location.label }}</option>
  </select>
</template>

<script>
export default {
  name: 'SearchInput',
  computed: {
    selectedLocation: {
      get() {
        return this.$store.state.selectedLocation || ''; // Use o valor do store
      },
      set(value) {
        this.$store.commit('setSelectedLocation', value);
        this.$emit('location-change', value); // Emita um evento personalizado
      },
    },
    locations() {
      return this.$store.state.locations;
    },
  },
  methods: {
    handleSelectionChange() {
      // Este método é chamado quando a opção é alterada
      console.log('Opção selecionada:', this.selectedLocation);
    },
  },
};
</script>



<style scoped>
/*Configurações globais*/
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.search-parking{
    width: 306px;
    height: 41px;
    border-radius: 9px;
    background-color: #F3F3F3;
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-between;
    align-content: center;
    margin-top: 20px;
    outline: none;
    border: none;
    font-size:15px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
    text-align: center;
}

.info-parking{
    color:#9F9F9F;
    font-size:15px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
}

select option{
    color:#9F9F9F;
    font-size:15px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
    border: none;
    outline: none;
}

.icon-search{
    width: 20px;
    margin-left: 7px;
}

.icon-options-parking{
    width: 35px;
}
</style>
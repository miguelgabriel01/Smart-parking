<template>
    <div class="map-container">
      <l-map :zoom="zoom" :center="center">
        <l-tile-layer :url="tileLayerUrl"></l-tile-layer>
        <l-marker :lat-lng="currentLocation" v-if="currentLocation"></l-marker>
        <l-marker :lat-lng="destinationLocation" v-if="destinationLocation"></l-marker>
      </l-map>
    </div>
  </template>
  
  <script>
  import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
  import 'leaflet/dist/leaflet.css';
  
  export default {
    components: {
      LMap,
      LTileLayer,
      LMarker,
    },
    data() {
      return {
        zoom: 13,
        center: [0, 0], // Localização inicial
        tileLayerUrl: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', // URL do provedor de mapa
        currentLocation: null, // Localização atual do usuário
        destinationLocation: [-7.7323498, -34.9440206], // Latitude e longitude do destino desejado
      };
    },
    mounted() {
      // Obter a localização atual do usuário
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          (position) => {
            this.currentLocation = [position.coords.latitude, position.coords.longitude];
            this.center = this.currentLocation;
          },
          (error) => {
            console.error(error.message);
          }
        );
      } else {
        console.error('Geolocation is not supported by this browser.');
      }
    },
  };
  </script>
  
  <style scoped>
  .map-container {
    height: 400px;
  }
  </style>
  
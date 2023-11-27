import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store/store'; // Importe o store

const app = createApp(App);
app.use(router);
app.use(store); // Use o store
app.mount('#app');
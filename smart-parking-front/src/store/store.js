import { createStore } from 'vuex';

export default createStore({
  state: {
    selectedLocation: '',
    locations: [
      { value: 'Shopping north way', label: 'Shopping north way' },
      { value: 'Shopping de igarassu', label: 'Shopping de igarassu' },
      { value: 'Shopping Patteo Olinda', label: 'Shopping Patteo Olinda' },
    ],
  },
  mutations: {
    setSelectedLocation(state, value) {
      state.selectedLocation = value;
    },
  },
});

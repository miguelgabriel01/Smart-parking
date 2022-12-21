import axios from 'axios'

//criamos a url base do nosso projeto apos instanciar o axios
const axiosInstace = axios.create({
  baseURL:'https://anypoint.mulesoft.com/mocking/api/v1/sources/exchange/assets/c7f363aa-e0df-4aba-8bed-7d59f151344e/smarth-parking/1.0.1/m/v1/find-all'
})

export const api = {
  //metodos get
  get(endpoint){
    return axiosInstace.get(endpoint);
  },

  //metodos post
  post(endpoint,body){
    return axiosInstace.post(endpoint, body);
  },

  delete(endpoint){
    return axiosInstace.delete(endpoint)
  },

  put(endpoint,body){
    return axiosInstace.put(endpoint, body);
  }

}
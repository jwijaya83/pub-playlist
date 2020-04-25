import axios from 'axios'

export const HttpClient = axios.create({
  baseURL: 'http://localhost:3000',
})

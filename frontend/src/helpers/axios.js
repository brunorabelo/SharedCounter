
import axios from 'axios'

export default axios.create({
  //baseURL: process.env.API_BASE_URL,
  baseURL: "/api",
  withCredentials: false,
})
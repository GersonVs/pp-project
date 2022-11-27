import axios from 'axios';
import { 
    verifyToken, 
    refreshAccessToken, 
    isUserLoggedIn,
    getUserData } from '@/auth/jwtUtils';

const env = import.meta.env

const getAuthorization = async () => {
    const userData = getUserData()
    if (userData) {
        return 'Bearer ' + userData.access   
    }
    return 'Bearer'
}

const instance = axios.create({
    baseURL: env.VITE_BACKEND_HOST
})

instance.defaults.headers.common['Authorization'] = await getAuthorization()

export { instance as axiosInstance }
import axios from 'axios';

const env = import.meta.env

const instance = axios.create({
    baseURL: env.VITE_BACKEND_HOST
})

const getUserData = () => {
    let data = localStorage.getItem('userData')
    if (data && data != 'undefined') {
        return JSON.parse(localStorage.getItem('userData')) 
    }
    
    return false
}

const refreshAccessToken = async (refreshToken) => {
    const res = await instance.post('/authentication/api/token/refresh/', {
        refresh: refreshToken
    }).catch(e => e.response.status)

    if (res.status < 400) {
        let userData = getUserData()
        userData.access = res.data.access
        userData.refresh = res.data.refresh

        setUserData(userData)

        return true
    } 
    alert('An internal error has been occurred! Please, refresh the page and try again.')
    return false
}

const verifyToken = async (token) => {
    const res = await instance.post('/authentication/api/token/verify/', {
        token: token
    }).catch(e => e.response.status)

    return res.status === 200
}

const isUserLoggedIn = async () => {
    const userData = getUserData()
    if (userData) {
        return await verifyToken(userData.refresh)
    } 
    
    return false
}

const setUserData = (userData) => {
    localStorage.setItem('userData', JSON.stringify(userData))
}

export { 
    refreshAccessToken,
    isUserLoggedIn,
    getUserData,
    setUserData,
    verifyToken 
}
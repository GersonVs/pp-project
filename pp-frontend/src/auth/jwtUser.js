import { 
    refreshAccessToken, 
    getUserData, 
    setUserData, 
    isUserLoggedIn } from '@/auth/jwtUtils'

const jwt = async () => {
    if (!await isUserLoggedIn()) {
        let currentLocation = window.location.pathname
        if (currentLocation != '/login') window.location.href = '/login'
    } else {
        var userData = getUserData()
        let tokenData = await refreshAccessToken(userData.refresh)
        
        userData.access  = tokenData.access
        userData.refresh = tokenData.refresh
        
        setUserData(userData)    
    }
}

const { jwtUser } = jwt()

export default jwtUser
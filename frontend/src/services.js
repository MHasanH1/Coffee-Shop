import axios from "axios";
/* eslint-disable */
const checkAuthentication =async () => {
    if (localStorage.getItem('token') === null) {
        return false;
    }
    return await axios.get('http://localhost:8000/api/check-auth/',{
        headers:{
            Authorization : `Token ${localStorage.getItem('token')}`
        }
    })
    .then(res=>{
        return true;
    })
    .catch(err=>{
        console.log(err);
        return false;
    })

}

export default checkAuthentication;
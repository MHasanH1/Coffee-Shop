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

const checkAdministary =async () =>{
    if (await checkAuthentication()){
        return await axios.get('http://localhost:8000/api/profile/',{
            headers:{
                Authorization : `Token ${localStorage.getItem('token')}`
            }
        })
        .then(res=>{
            return res.data.is_admin;
        })
        .catch(err=>{
            console.log(err);
        })
    }
    return false;
}

export {checkAuthentication,checkAdministary};
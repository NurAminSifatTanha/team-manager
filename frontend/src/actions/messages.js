import {CREATE_MESSAGE,GET_ERROR} from './types'

//create message
export const createMessgae=(msg)=>{
    return {
        type:CREATE_MESSAGE,
        payload: msg
    }
};

//return errors
export const returnError=(msg,status)=>{
    return{
        type:GET_ERROR,
        payload: {msg,status}
    }
};
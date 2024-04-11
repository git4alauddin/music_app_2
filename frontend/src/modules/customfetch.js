export default async function customfetch(url, init_obj){
    let res=null
    let data=null
    
    try{
        res=await fetch(url,init_obj)

    }
    catch{
        throw new Error('Network connection failure')

    }
    try{
        data= await res.json()
    }catch
    {
        throw new Error('Body not json')
    }


if(res.ok){
return data
}
else{
    throw new Error(data.message)
}
}


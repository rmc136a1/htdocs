function textinner(adress,target){
    fetch(adress).then(function(response){
        response.text().then(function(text){
            document.querySelector(target).innerHTML=text;
        })
    })
}
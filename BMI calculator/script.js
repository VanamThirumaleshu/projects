function BMI(){
    var h=document.getElementById('h').value;
    var w=document.getElementById('w').value;
    
    
   
    var bmi=w/(h/100*h/100);
    var bmio=(bmi.toFixed(2));
    var res='Your BMI is '+bmio;
    if (bmio<18.5){
        res=res+' Sorry! to say that you are in UNDERWEIGHT range';

    }else if(bmio>=18.5 && bmio<=24.9){
        res=res+' Congratulations! You are in HEALTHY WEIGHT range';
    }else if(bmio>=25 && bmio<=29.9){
        res=res+' Sorry! to say that You are in OVER WEIGHT range';

    }else{
        res=res+' Sorry! to say that You are in OBESE range Take Care';
    }

    document.getElementById('result').innerHTML=res;
        

    
}
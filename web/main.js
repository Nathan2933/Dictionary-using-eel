function meaning(){
    meaning1.innerHTML="";
    var word1=document.getElementById("word").value;
    eel.meanin(word1);
}
function reset(){
    document.getElementById("word").value="";
    var meaning1=document.getElementById("meaning1");
    meaning1.innerHTML="";
    
}
function alerting(Text){
    
    if (confirm("Did you mean "+Text+" instead ?")) {
        eel.meaning2(Text);
    } 
   else{
       alert("Please type a correct word");
   }
    
}
eel.expose(alerting);
function addText(text){
    var meaning1=document.getElementById("meaning1");
    meaning1.innerHTML+=text;
}
eel.expose(addText);
function wde(Text){
    alert(Text);
}
eel.expose(wde);
var colors=generateRandomColors(6);
var square=document.querySelectorAll(".square");
var pickedColor= pickColor();
var colorDisplay=document.getElementById("colorDisplay");
var messageDisplay=document.querySelector("#message");
var h1=document.querySelector("h1");
var resetButton=document.querySelector("#reset");


resetButton.addEventListener("click",function () {
    colors= generateRandomColors(6);
    pickedColor=pickColor();
    colorDisplay.textContent=pickedColor;
    messageDisplay.textContent="";
    this.textContent="New Colors";
    for(var i=0;i<square.length;i++){
        square[i].style.background=colors[i];
    }
    h1.style.background="steelblue";
});

colorDisplay.textContent=pickedColor;

for(var i=0;i<square.length;i++){
    square[i].style.background=colors[i];

    square[i].addEventListener("click", function(){
        var clickedColor=this.style.background;
        if(clickedColor==pickedColor){
            messageDisplay.textContent="Correct";
            resetButton.textContent="Play Again?";
            changeColors(clickedColor);
            h1.style.background=clickedColor;
        }
        else{
            this.style.background="#232323";
             messageDisplay.textContent="Try Again";
        }
    })
}
function changeColors(color){
    for(var i=0;i<square.length;i++){
        square[i].style.background=color;
    }
}
function pickColor(){
    var random=Math.floor(Math.random() * colors.length);
    return colors[random];
}
function generateRandomColors(num){
     var arr=[]

for(var i=0;i<num;i++){
         arr.push(randomColor())

}

return arr;
}

function randomColor(){
    var r=Math.floor(Math.random()*256);
    var g=Math.floor(Math.random()*256);
    var b=Math.floor(Math.random()*256);

    "rgb(r, g, b"
   return "rgb(" + r + ", " + g + ", " + b +")";
}








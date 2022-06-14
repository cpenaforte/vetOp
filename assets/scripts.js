const input2 = document.getElementById("input2");
input2.style.display = "none";
const selector1 = document.createElement("select");
const op11 = document.createElement("option");
const button = document.getElementById("submit-button");
const form = document.getElementById("form");
const text = document.createTextNode("Vector Rotation");

op11.setAttribute("value","rotation");
op11.appendChild(text);

selector1.setAttribute("id","selector1")
selector1.appendChild(op11);

const selector2 = document.createElement("select");
const op21 = document.createElement("option");
const op22 = document.createElement("option");
const op23 = document.createElement("option");
const op24 = document.createElement("option");

op21.setAttribute("value","add");
const text1 = document.createTextNode("Vector Sum");
op21.appendChild(text1);

op22.setAttribute("value","sub");
const text2 = document.createTextNode("Vector Subtract");
op22.appendChild(text2);

op23.setAttribute("value","sca");
const text3 = document.createTextNode("Scalar Product");
op23.appendChild(text3);

op24.setAttribute("value","vec");
const text4 = document.createTextNode("Vector Product");
op24.appendChild(text4);

selector2.setAttribute("id","selector2")
selector2.appendChild(op21);
selector2.appendChild(op22);
selector2.appendChild(op23);
selector2.appendChild(op24);

const selector3 = document.createElement("select");
const op31 = document.createElement("option");
const op32 = document.createElement("option");
const op33 = document.createElement("option");

op31.setAttribute("value","x");
const text31 = document.createTextNode("Axle x");
op31.appendChild(text31);

op32.setAttribute("value","y");
const text32 = document.createTextNode("Axle y");
op32.appendChild(text32);

op33.setAttribute("value","z");
const text33 = document.createTextNode("Axle z");
op33.appendChild(text33);

selector3.setAttribute("id","selector3")
selector3.appendChild(op31);
selector3.appendChild(op32);
selector3.appendChild(op33);

const inputAngle = document.createElement("input");
inputAngle.setAttribute("type","text");
inputAngle.setAttribute("id","angle");
inputAngle.setAttribute("placeholder","Type the rotation angle in radians");
inputAngle.setAttribute("onfocus","this.value='';");


form.insertBefore(selector1,button);
form.insertBefore(selector3,button);
form.insertBefore(inputAngle,button);
  
function changeListener(){
  var value = this.value;
    
  if (value == "1 Vector Operations"){
    input2.style.display = "none";

    form.insertBefore(selector1,button);
    form.insertBefore(selector3,button);
    form.insertBefore(inputAngle,button);

    form.removeChild(selector2);

  }else if (value == "2 Vectors Operations"){
    input2.style.display = "flex";

    form.removeChild(selector1);
    form.removeChild(selector3);
    form.removeChild(inputAngle);

    form.insertBefore(selector2,button);
    }
    
  }

  document.getElementById("selector").onchange = changeListener;
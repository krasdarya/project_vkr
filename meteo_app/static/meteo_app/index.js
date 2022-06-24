function mouseOver() {
  document.getElementById("demo").className='display-4 fw-normal text-dan text-dan-title text-center';
}

function mouseOut() {
  document.getElementById("demo").className = 'display-4 fw-normal header-text text-dan-title text-center';
}
function mouseOver1() {
  document.getElementById("btn1").className='btn btn-main';
  document.getElementById("meteo").className='text-white';
}

function mouseOut1() {
  document.getElementById("btn1").className='btn btn-out';
  document.getElementById("meteo").className='header-text';
}

function mouseOver2() {
  document.getElementById("btn2").className='btn btn-main';
  document.getElementById("wind").className='text-white';
}

function mouseOut2() {
  document.getElementById("btn2").className='btn btn-out';
  document.getElementById("wind").className='header-text';
}

function mouseOver3() {
  document.getElementById("btn3").className='btn btn-main';
  document.getElementById("invertor").className='text-white';
}

function mouseOut3() {
  document.getElementById("btn3").className='btn btn-out';
  document.getElementById("invertor").className='header-text';
}
function meteoOver() {
    document.getElementById("meteo-data").className='display-4 fw-normal text-dan text-dan-title text-center my-5';
}
function meteoOut() {
    document.getElementById("meteo-data").className = 'display-4 fw-normal header-text text-dan-title text-center my-5';
}
function windOver() {
    document.getElementById("wind-data").className='display-4 fw-normal text-dan text-dan-title text-center my-5';
}
function windOut() {
    document.getElementById("wind-data").className = 'display-4 fw-normal header-text text-dan-title text-center my-5';
}
function invertorOver() {
    document.getElementById("invertor-data").className='display-4 fw-normal text-dan text-dan-title text-center my-5';
}
function invertorOut() {
    document.getElementById("invertor-data").className = 'display-4 fw-normal header-text text-dan-title text-center my-5';
}
function mgraphOver() {
    document.getElementById("meteo-graph").className='display-5 fw-normal text-dan text-dan-title text-center my-5';
}
function mgraphOut() {
    document.getElementById("meteo-graph").className = 'display-5 fw-normal header-text text-dan-title text-center my-5';
}
function wgraphOver() {
    document.getElementById("wind-graph").className='display-5 fw-normal text-dan text-dan-title text-center my-5';
}
function wgraphOut() {
    document.getElementById("wind-graph").className = 'display-5 fw-normal header-text text-dan-title text-center my-5';
}
function igraphOver() {
    document.getElementById("invertor-graph").className='display-5 fw-normal text-dan text-dan-title text-center my-5';
}
function igraphOut() {
    document.getElementById("invertor-graph").className = 'display-5 fw-normal header-text text-dan-title text-center my-5';
}
/*function hideFunc() {
  var x = document.getElementById("myUL");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}*/
// Get the button, and when the user clicks on it, execute myFunction
//document.getElementById("myBtn").onclick = function() {hideFunc()};

/* myFunction toggles between adding and removing the show class, which is used to hide and show the dropdown content */
/*function hideFunc() {
  document.getElementById("myDrop").classList.toggle("show");
}*/

function myFunctionbtn() {
  var x = document.getElementById("myDrop");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function myFunchidewind() {
  var x = document.getElementById("myDropwind");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function myFuncbtninv() {
  var x = document.getElementById("myDropinv");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
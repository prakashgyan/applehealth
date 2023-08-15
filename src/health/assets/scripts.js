window.onload = function() {
    var number = document.getElementById("number123");
    var finalValue = 1001; // Change this to the final value you want
  
    for (var i = 0; i <= finalValue; i++) {
      setTimeout(function() {
        number.innerHTML = i;
      }, i * 20);
    }
  }
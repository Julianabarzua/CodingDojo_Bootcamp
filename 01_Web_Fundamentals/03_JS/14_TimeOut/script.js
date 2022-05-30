function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() + 
      new Date().getMinutes() * 60 + 
      new Date().getHours() * 3600;
}

function getHourHandAngle(s){
    s %=43200;
    return(360*s/43200+180) % 360;
}

function getMinuteHandAngle(s){
    s %=3600;
    return(6*s/60+180) % 360;
}

function getSecondHandAngle(s){
    s %=60;
    return(6*s+180) % 360;
}

const hour = document.getElementById("hour");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");



setInterval( function() {
    var time = getSecondsSinceStartOfDay();
    console.log(time);

    hour.style.transform = `rotate(${getHourHandAngle(time)}deg)`;
    minutes.style.transform = `rotate(${getMinuteHandAngle(time)}deg)`;
    seconds.style.transform = `rotate(${getSecondHandAngle(time)}deg)`;




  }, 1000);
  
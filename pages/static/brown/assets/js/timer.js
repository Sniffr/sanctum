var count;
var now =Math.floor(Date.now() / 1000);
var datecreated =Math.round(JSON.parse($("#date-created").text()));
var time_expiry = datecreated +1800;

var counter=setInterval(timer, 1000);
console.log(time_expiry);
console.log(now);
count = time_expiry - now;

function fmtMSS(s){return(s-(s%=60))/60+(9<s?':':':0')+s}

function timer()
{
  count=count-1;
  if (count <= 0)
  {
     clearInterval(counter);
     document.getElementById("timer").innerHTML="0:00";
     return;
  }

 document.getElementById("timer").innerHTML=fmtMSS(count);
}




function showTime(){
    var date = new Date();
    var today = date.getDate();
    month = date.toLocaleString('default', {month: 'long'});
    var year = date.getFullYear();
    var h = date.getHours();
    var m = date.getMinutes(); 
    var s = date.getSeconds(); 
    var session = "AM";
    
    if(h == 0){
        h = 12;
    }
    
    if(h > 12){
        h = h - 12;
        session = "PM";
    }
    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    var time = h + ":" + m + ":" + s + " " + session;
    var day = `${today} ${month} ${year}.`;
    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("date").textContent = day;
    
    setTimeout(showTime, 1000);
    
}

showTime();



function putTime(){
    
    var date = new Date();
    var today = date.getDate();
    month = date.toLocaleString('default', {month: 'long'});
    var year = date.getFullYear();
    var h = date.getHours();
    var m = date.getMinutes(); 
    var s = date.getSeconds(); 
    var session = "AM";
    
    if(h == 0){
        h = 12;
    }
    
    if(h > 12){
        h = h - 12;
        session = "PM";
    }
    
    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    
    var time = h + ":" + m + ":" + s + " " + session;
    document.getElementById("time").value = time;

    console.log(time)
}

putTime();
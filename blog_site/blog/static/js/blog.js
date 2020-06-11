// Offsets UTC blog post times with client timezone
[...document.getElementsByClassName("post_time")].forEach(time => {
    var time_offset = new Date().getTimezoneOffset() / 60;
    var new_hour = parseInt(time.innerHTML.split(":")[0]) - time_offset;
    
    time.innerHTML = new_hour + ":" + time.innerHTML.split(":")[1];

});

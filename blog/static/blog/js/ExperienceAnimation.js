// var cadre = document.getElementById('cadre');
// var cadreL = parseFloat(getComputedStyle(cadre).width);
var jobElt = document.getElementById('job');
var maxJob = parseFloat(getComputedStyle(jobElt).width);
var d = 1;
var v = 5;
var jobLActuel = 0;
var cpt = 0;
var t = false;
liste = ['Web', 'Responsive', 'WordPress', 'Vim'];
liste2 = ['Application', 'Design', 'Developper', 'Developper']

function funtionAnimation(){
    jobLActuel = parseFloat(getComputedStyle(jobElt).width);

    if(jobLActuel + v > maxJob)
    {
        d *= -1;
        t = true;
    }

    if(jobLActuel <= 0)
    {
        d *= -1;
        // t = true;
        jobElt.innerHTML = liste[cpt]+"<span style='color: #424141'>i</span>"+liste2[cpt]
        cpt += 1;
        if (cpt===4) { cpt = 0;}
    }
    changeLargeur();

}

function changeLargeur(){
    jobElt.style.width = (jobLActuel + v*d) + 'px';
    // console.log('oui');
    if(t){
        clearInterval(intervalId);
        // setTimeout(function() {}, 10000);
        t = false;

        intervalIdStop = setInterval(stop, 2000);
    }

}

function stop(){
    clearInterval(intervalIdStop);
    intervalId = setInterval(funtionAnimation, 10);
}

// var l = ['j','k','o'];

// funtionAnimation();
intervalId = setInterval(funtionAnimation, 10);

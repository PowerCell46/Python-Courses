function skeleton(input) {

let controlMinutes = Number(input[0]);
let controlSeconds = Number(input[1]);
let controlTimeTotal = (controlMinutes * 60) + controlSeconds;

let distance = Number(input[2]);
let timeFor100meters = Number(input[3]);

let slowingDown = (distance / 120) * 2.5;
let totalSwimmingTime = (distance / 100) * timeFor100meters - slowingDown;



if(totalSwimmingTime <= controlTimeTotal) {
console.log("Marin Bangiev won an Olympic quota!");
console.log("His time is " + totalSwimmingTime.toFixed(3) + ".");
} else {
    let neededSec = totalSwimmingTime - controlTimeTotal;
    console.log("No, Marin failed! He was " + neededSec.toFixed(3) + " second slower.");
}
}

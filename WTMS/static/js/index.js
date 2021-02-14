
document.getElementById('b1').addEventListener('click', clickDiv);
document.getElementById('b2').addEventListener('click',clickDiv);
document.getElementById('b3').addEventListener('click',clickDiv);
document.getElementById('b4').addEventListener('click',clickDiv);
function clickDiv() {
   // document.getElementById('b1').innerHTML = "Clicked and Changed"; // Changes text inside div one time only when clicked
    alert("Clicked!")
    window.open("issue", '_self')
}
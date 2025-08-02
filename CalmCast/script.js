let timer;
let timeLeft = 25 * 60;
function startTimer() {
 if (timer) return;
 timer = setInterval(() => {
   if (timeLeft <= 0) {
     clearInterval(timer);
     alert("Time's up! Take a break or extend!");
     return;
   }
   timeLeft--;
   displayTime(); //fixed time display
 }, 1000);
}
function resetTimer() {
 clearInterval(timer);
 timer = null;
 timeLeft = 25 * 60; //provide options to set custom time
 displayTime();
}
function displayTime() {
 const minutes = Math.floor(timeLeft / 60);
 const seconds = timeLeft % 60;
 document.getElementById('timer').textContent =
   `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}
function addTask() {
 const input = document.getElementById("taskInput");
 const task = input.value.trim();
 if (task) {
   const li = document.createElement("li");
   li.textContent = task;
   document.getElementById("taskList").appendChild(li);
   input.value = "";
 }
}
displayTime();

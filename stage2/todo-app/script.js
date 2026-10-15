const input=document.getElementById("task-input")
const button=document.getElementById("add-button")
const list=document.getElementById("task-list")
let tasks = JSON.parse(localStorage.getItem("tasks")) || []
   
 function renderTasks() {
    list.innerHTML= ""
    tasks.forEach(function(tasktext , index ){
    const li = document.createElement("li")
    li.textContent = tasktext

    const deleteBtn = document.createElement("button")
    deleteBtn.textContent = "delete"
    deleteBtn.addEventListener("click", function() {
      tasks.splice(index, 1)
      localStorage.setItem("tasks" , JSON.stringify(tasks))
      renderTasks ()
    })
    li.appendChild(deleteBtn)
    list.appendChild(li)
    })
  }

button.addEventListener("click" , function(){
    const tasktext = input.value
    if (tasktext !==""){
      tasks.push(tasktext)
      localStorage.setItem("tasks" ,JSON.stringify(tasks))
      renderTasks()
      input.value = ""
    }
})

renderTasks()
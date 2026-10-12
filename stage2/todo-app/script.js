const input=document.getElementById("task-input")
const button=document.getElementById("add-button")
const list=document.getElementById("task-list")

button.addEventListener("click" , function(){
    const tasktext = input.value
    if (tasktext !==""){
     const li = document.createElement("li")
     li.textContent = tasktext
     list.appendChild(li)
     input.value = ""
    }
})


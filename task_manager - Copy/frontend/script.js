async function addTask() {
  let title = document.getElementById("task").value;

  await fetch("http://127.0.0.1:8000/tasks?title=" + title + "&owner=admin", {
    method: "POST"
  });

  loadTasks();
}

async function loadTasks() {
  let res = await fetch("http://127.0.0.1:8000/tasks?owner=admin");
  let tasks = await res.json();

  let list = document.getElementById("list");
  list.innerHTML = "";

  tasks.forEach(t => {
    let li = document.createElement("li");
    li.innerText = t.title;
    list.appendChild(li);
  });
}

loadTasks();

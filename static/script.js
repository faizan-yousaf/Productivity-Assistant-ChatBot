function createTask() {
    const taskName = document.getElementById('taskName').value;
    const taskDescription = document.getElementById('taskDescription').value;
    
    fetch('/create_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ taskName, taskDescription }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Task created successfully!');
            document.getElementById('taskName').value = '';
            document.getElementById('taskDescription').value = '';
            getTasks();
        } else {
            alert('Failed to create task.');
        }
    });
}

function getTasks() {
    fetch('/get_tasks')
    .then(response => response.json())
    .then(tasks => {
        const taskList = document.getElementById('taskList');
        
        taskList.innerHTML = '';
        tasks.forEach(task => {
            const li = document.createElement('li');
            li.textContent = task.name;
            taskList.appendChild(li);
        });
    });
}

function askAssistant() {
    const question = document.getElementById('question').value;
    
    fetch('/ask_assistant', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('assistantResponse').textContent = data.response;
    });
}

// Load tasks when the page loads
getTasks();
let token = "";

// ----------------------------
// LOGIN FUNCTION
// ----------------------------
function login() {
    token = document.getElementById("token").value.trim();

    if(token === "") {
        alert("Please enter a token");
        return;
    }

    document.getElementById("main").style.display = "block";

    loadRequests();
}

// ----------------------------
// CREATE NEW REQUEST
// ----------------------------
function createRequest() {
    let data = {
        title: document.getElementById("title").value,
        category: document.getElementById("category").value,
        description: document.getElementById("description").value,
        priority: document.getElementById("priority").value,
        name: document.getElementById("name").value,
        email: document.getElementById("email").value
    };

    fetch(`http://127.0.0.1:8000/request?token=${token}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        alert(result.message);
        loadRequests();
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to create request");
    });
}

// ----------------------------
// LOAD ALL REQUESTS
// ----------------------------
function loadRequests() {
    fetch(`http://127.0.0.1:8000/requests?token=${token}`)
    .then(response => response.json())
    .then(data => {
        let table = document.getElementById("table");
        table.innerHTML = "";

        data.forEach(req => {
            
            let row = `<tr>
    <td><a href="details.html?id=${req.id}&token=${token}">${req.id}</a></td>
    <td>${req.title}</td>
    <td>${req.status}</td>
</tr>`;
            table.innerHTML += row;
        });
    })
    .catch(error => {
        console.error("Error loading requests:", error);
    });
}
document.getElementById("qrForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    // Send data to Python server
    const response = await fetch("http://127.0.0.1:5000/generate_qr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email })
    });

    const data = await response.json();
    document.getElementById("qrImage").src = data.qr_code;
});

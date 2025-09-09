// js/main.js
document.getElementById("signupForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("http://127.0.0.1:5000/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: name,
        email: email,
        password: password
      })
    });

    const data = await res.json();

    // Show response on page
    const messageEl = document.getElementById("message");
    messageEl.textContent = data.message || data.error;
    messageEl.style.color = data.error ? "red" : "green";

    console.log("Server response:", data);

  } catch (error) {
    console.error("Error:", error);
    document.getElementById("message").textContent = "Something went wrong!";
  }
});

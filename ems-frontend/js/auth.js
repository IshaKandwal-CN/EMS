const API_URL = "http://127.0.0.1:5000/auth";  // Flask backend

// Handle Signup
document.getElementById("signupForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const username = document.getElementById("username").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${API_URL}/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password })
    });

    const data = await res.json();
    document.getElementById("signupMsg").textContent = data.message || data.error;

    if (res.ok) {
      // ✅ Successfully registered, now user must verify email
      setTimeout(() => {
        window.location.href = "login.html";
      }, 2000);
    }
  } catch (error) {
    console.error("Signup Error:", error);
    document.getElementById("signupMsg").textContent = "Something went wrong!";
  }
});

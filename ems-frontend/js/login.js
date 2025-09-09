// js/login.js
document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("http://127.0.0.1:5000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    const messageEl = document.getElementById("message");
    messageEl.textContent = data.message || data.error;
    messageEl.style.color = data.error ? "red" : "green";

    console.log("Login Response:", data);

    if (data.message === "OTP sent to your email.") {
      // Store email temporarily to verify OTP later
      localStorage.setItem("userEmail", email);
      window.location.href = "otp.html"; // redirect to OTP page
    }

  } catch (error) {
    console.error("Error:", error);
    document.getElementById("message").textContent = "Something went wrong!";
  }
});

// js/otp.js
document.getElementById("otpForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const otp = document.getElementById("otp").value;
  const email = localStorage.getItem("userEmail"); // from login

  try {
    const res = await fetch("http://127.0.0.1:5000/auth/verify-otp", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, otp })
    });

    const data = await res.json();

    const messageEl = document.getElementById("message");
    messageEl.textContent = data.message || data.error;
    messageEl.style.color = data.error ? "red" : "green";

    console.log("OTP Verify Response:", data);

    if (data.token) {
      // Save JWT token in localStorage for further API calls
      localStorage.setItem("token", data.token);
      window.location.href = "dashboard.html"; // go to dashboard
    }

  } catch (error) {
    console.error("Error:", error);
    document.getElementById("message").textContent = "Something went wrong!";
  }
});

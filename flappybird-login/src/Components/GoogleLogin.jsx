import React, { useState } from "react";
import axios from "axios";
import authimg from "F:/flappy/__maingame__/gulgulauth.png";
import { auth, provider, signInWithPopup } from "./firebase";

function GoogleLogin() {
  const [clicked, setClicked] = useState(false);

  const handleLogin = async () => {
    setClicked(true);
    setTimeout(() => setClicked(false), 200);

    try {
      const result = await signInWithPopup(auth, provider);
      const token = await result.user.getIdToken(); // Firebase ID token

      // Send this token to your backend
      const response = await axios.post(
        "http://localhost:5000/api/verify",
        { token },
        { headers: { "Content-Type": "application/json" } }
      );

      if (response.data.status === "success") {
        await fetch("http://127.0.0.1:5000/launch-game");
      }

      console.log("User logged in:", result.user.displayName);
    } catch (err) {
      console.error("Login failed:", err);
    }
  };

  return (
    <button
      onClick={handleLogin}
      className={
        clicked
          ? "transition transform scale-90 googleAuth"
          : "transition googleAuth"
      }
    >
      <img src={authimg} alt="auth_img" />
    </button>
  );
}

export default GoogleLogin;

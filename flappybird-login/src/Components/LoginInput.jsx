import React, { useState } from "react";
import axios from "axios";
import loginimg from "F:/flappy/__maingame__/loginimg.png";
import highscoreimg from "F:/flappy/__maingame__/highscoreimg.png";
import ppimg from "F:/flappy/__maingame__/pp.png";

const LoginInput = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:5000/login", {
        email,
        password,
      });
      setMessage(response.data.message);

      if (response.data.status === "success") {
        // Trigger Python Flappy Bird Game
        await axios.get("http://127.0.0.1:5000/launch-game"); // New endpoint to launch game
      }
    } catch (error) {
      setMessage("Login failed. Please try again.");
    }
  };

  return (
    <div className="login flex flex-col justify-center left bg-white/20 backdrop-blur-md rounded-lg p-4  shadow-md">
      <div className="login-img p-35 pt-0 pb-2">
        <img src={`${loginimg}`} alt="" />
      </div>
      <div className="login-form">
        <form onSubmit={handleSubmit} className="z-10">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit" className="mt-5 text-black">
            Login
          </button>
        </form>
      </div>
      <div className="player-card mt-5 flex flex-col">
        <div className="info flex flex-row">
          <div className="profile-photo ml-3 mt-3">
            <img src={`${ppimg}`} alt="profilepic" />
          </div>
          <div className="player-info pl-3 pt-3 flex flex-col gap-1">
            <p id="name" className="text-black">
              user singh khabardar
            </p>
            <p id="username" className="text-black">
              lunarboy256
            </p>
            <p id="rank" className="text-black">
              56
            </p>
          </div>
        </div>
        <div className="high-score pt-5 pl-3">
          <img
            src={`${highscoreimg}`}
            alt="highscoreimg"
            className="max-w-xs h-[40px]"
          />
        </div>
      </div>
      <p className="mt-5 text-black">
        New User ? <a href="#signup">SignUp</a>
      </p>
    </div>
  );
};

export default LoginInput;

import React, { useState } from "react";
import axios from "axios";
import bgImage from "F:/flappy/__maingame__/spring world.jpg";
import mainimg from "F:/flappy/Welcome screen/img_45.png";
import abtimg from "F:/flappy/__maingame__/aboutflappy.png";
import authimg from "F:/flappy/__maingame__/gulgulauth.png";
import charimg from "F:/flappy/__maingame__/char.png";
import harryimg from "F:/flappy/__maingame__/harry.png";
import rachelimg from "F:/flappy/__maingame__/rachel.png";
import mikeimg from "F:/flappy/__maingame__/mike.png";
import donnaimg from "F:/flappy/__maingame__/donna.png";
import loginimg from "F:/flappy/__maingame__/loginimg.png";
import highscoreimg from "F:/flappy/__maingame__/highscoreimg.png";
import ppimg from "F:/flappy/__maingame__/pp.png";

const LoginForm = () => {
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
    <section id="login">
      <div className="absolute top-0 left-0 z-10 background">
        <img src={`${bgImage}`} alt="background" />
      </div>
      {/* Login Form */}
      <div className="hero-layout">
        <div className="flex flex-row box">
          <div className="flex flex-col justify-center bc left space-y-4 p-10 pt-0 pb-0">
            <div className="mainimg object-contain">
              <img src={`${mainimg}`} alt="mainimg" />
            </div>
            <div className="about">
              <img src={`${abtimg}`} alt="about" />
            </div>
            <div className="google-auth p-20 pt-2 pb-2 mb-0">
              <img src={`${authimg}`} alt="auth_img" />
            </div>
            <div className="players">
              <img src={`${charimg}`} alt="characters_text" />
              <div className="grid-2-cols pt-4">
                <img src={`${harryimg}`} alt="" />
                <img src={`${rachelimg}`} alt="" />
                <img src={`${mikeimg}`} alt="" />
                <img src={`${donnaimg}`} alt="" />
              </div>
            </div>
          </div>
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
                  class="max-w-xs h-[40px]"
                />
              </div>
            </div>
            <p className="mt-5 text-black">
              New User ? <a href="">SignUp</a>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default LoginForm;

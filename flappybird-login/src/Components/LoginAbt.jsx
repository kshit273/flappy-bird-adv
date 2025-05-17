import mainimg from "F:/flappy/Welcome screen/img_45.png";
import abtimg from "F:/flappy/__maingame__/aboutflappy.png";
import charimg from "F:/flappy/__maingame__/char.png";
import { players } from "../constants/playerImages.js";
import GoogleLogin from "./GoogleLogin.jsx";
import { useState } from "react";

const LoginAbt = () => {
  const [selected, setSelected] = useState(false);
  const selectPlayer = async (player) => {
    try {
      await fetch("http://localhost:5000/select_bird", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bird: player.ogimagePath }),
      });
    } catch (error) {}
  };

  return (
    <div className="flex flex-col justify-center bc left space-y-4 p-10 pt-0 pb-0">
      <div className="mainimg object-contain">
        <img src={mainimg} alt="mainimg" />
      </div>
      <div className="about">
        <img src={abtimg} alt="about" />
      </div>
      <div className="google-auth p-20 pt-2 pb-2 mb-0">
        <GoogleLogin />
      </div>
      <div className="players">
        <img src={charimg} alt="characters_text" />
        <div className="grid-2-cols pt-4">
          {players.map((player) => (
            <div
              className={
                "player" + (selected === player.name ? "selected" : "")
              }
              key={player.name}
              onClick={() => {
                selectPlayer(player);
                setSelected(selected === player.name ? null : player.name);
              }}
            >
              <img src={player.path} alt={player.name} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default LoginAbt;

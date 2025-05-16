import mainimg from "F:/flappy/Welcome screen/img_45.png";
import abtimg from "F:/flappy/__maingame__/aboutflappy.png";
import authimg from "F:/flappy/__maingame__/gulgulauth.png";
import charimg from "F:/flappy/__maingame__/char.png";
import { players } from "../constants/playerImages.js";

const LoginAbt = () => {
  return (
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
          {players.map((player) => (
            <img src={player.path} alt={player.name} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default LoginAbt;

import LoginInput from "./LoginInput";
import LoginAbt from "./LoginAbt";

const LoginComp = () => {
  return (
    <div className="hero-layout">
      <div className="flex flex-row box">
        <LoginAbt />
        <LoginInput />
      </div>
    </div>
  );
};

export default LoginComp;

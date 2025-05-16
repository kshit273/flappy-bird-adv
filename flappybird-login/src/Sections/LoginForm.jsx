import bgImage from "F:/flappy/__maingame__/spring world.jpg";
import LoginComp from "../Components/LoginComp";

const LoginForm = () => {
  return (
    <section id="login">
      <div className="absolute top-0 left-0 z-10 background">
        <img src={`${bgImage}`} alt="background" />
      </div>
      <LoginComp />
    </section>
  );
};

export default LoginForm;

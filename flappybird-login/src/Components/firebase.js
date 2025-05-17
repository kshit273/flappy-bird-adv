import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyD5zq4i2eWcwlMYjYE7z39jMhlg5UnNoec",
  authDomain: "flappy-bird-cd89a.firebaseapp.com",
  projectId: "flappy-bird-cd89a",
  storageBucket: "flappy-bird-cd89a.firebasestorage.app",
  messagingSenderId: "592842595063",
  appId: "1:592842595063:web:46c96c1bbad716b9a551f2",
  measurementId: "G-148GWX07MR",
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export { auth, provider, signInWithPopup };

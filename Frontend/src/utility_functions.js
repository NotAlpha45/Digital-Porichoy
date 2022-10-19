import { writable } from "svelte/store";
import { auth } from "./firebase_conf";
import router from "page";
// import { writable } from "svelte-local-storage-store";

let initialToken = localStorage.getItem("userToken");
let defaultToken;

if (initialToken) {
  defaultToken = initialToken;
}

const userTokenStore = writable(initialToken);

userTokenStore.subscribe((token) => {
  localStorage.setItem("userToken", token);
});

const checkPassword = function (password, confirmPassword) {
  if (password != confirmPassword) {
    alert("আপনার পাসওয়ার্ড ম্যাচ করে না। আবার লিখুন!");
    return false;
  }
  if (password.length < 6) {
    alert("আপনার পাসওয়ার্ড অন্তত ৬ অক্ষর হতে হবে। আবার লিখুন!");
    return false;
  }

  return true;
};

const checkPhoneNumber = function (phoneNumber) {
  if (phoneNumber.length != 11 || !phoneNumber.startsWith("0")) {
    alert("আপনার ফোন নাম্বার ঠিক নেই। আবার লিখুন!");
    return false;
  }
  return true;
};

// userTokenStore.subscribe((token) => {
//   localStorage.content = token;
// });

const logOut = function () {
  if (auth.currentUser != null) {
    auth.signOut().then(() => {
      console.log("Logged Out");
    });
  }
  userTokenStore.set(null);
  localStorage.removeItem("userToken");
};

const isLoggedIn = () => {
  let flag = false;

  if (auth.currentUser != null) {
    flag = true;
  }
  return flag;
};

export { checkPassword, checkPhoneNumber, logOut, isLoggedIn, userTokenStore };

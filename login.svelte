<script>
  import axios from "axios";
  import router from "page";
  import { checkPhoneNumber } from "../utility_functions";

  //added:
  import API_HOST from "./api_config";
  import {
    getToken,
    deleteToken,
    setToken,
    getCsrfToken,
    deleteCsrfToken,
    setCsrfToken
  } from "./util";
  import {
    fetchUserData,
    fetchAuthToken,
    fetchCreateUser,
    fetchCsrfToken,
    validateInputs
  } from "./auth";
  export let isLoggedIn;
  let id, username, email;
  let wantsToSignUp = false;
  let usernameInput = "";
  let passwordInput = "";
  let isMessageError = false;
  let message = "";
  if (getToken()) {
    // if we have a token saved to local storage,
    // then log them in automatically
    fetchUserData_().then(fetchCsrfToken_());
    // Also get a new CSRF token always
  }
  function setUserData(json) {
    id = json.id;
    username = json.username;
    email = json.email;
    isLoggedIn = true;
    isMessageError = false;
    message = "Logged in as " + username;
  }
  function clearUserData() {
    id = null;
    username = null;
    email = null;
    isLoggedIn = false;
    isMessageError = false;
    message = "Logged out";
  }
  async function fetchUserData_() {
    let token = getToken();
    if (token) {
      try {
        fetchUserData(token)
          .then(res => res.json())
          .then(json => {
            if (json.username) {
              setUserData(json);
            } else {
              deleteToken();
            }
          })
          .catch(err => {
            console.log(err);
          });
      } catch (error) {
        console.log("threw error when fetching username: " + error);
        deleteToken();
      }
    } else {
      clearUserData();
      console.log("cannot get username because we have no token");
    }
  }
  function logOut() {
    deleteToken();
    deleteCsrfToken();
    clearUserData();
  }

  async function fetchAuthToken_() {
    if (validateInputs(usernameInput, passwordInput)) {
      fetchAuthToken(usernameInput, passwordInput)
        .then(res => res.json())
        .then(json => {
          if (json.token && json.user) {
            localStorage.setItem("token", json.token);
            setUserData(json.user);
          } else {
            isMessageError = true;
            message = "Error logging in";
          }
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
  function fetchCsrfToken_() {
    let token = getToken();
    if (token && !getCsrfToken()) {
      fetchCsrfToken(token)
        .then(res => res.json())
        .then(json => {
          if (json.csrf_token) {
            setCsrfToken(json.csrf_token);
          } else {
            isMessageError = true;
            message = "Error getting CSRF token";
          }
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
  function logIn() {
    fetchAuthToken_().then(fetchCsrfToken_());
  }
  function signUp() {
    if (validateInputs(usernameInput, passwordInput)) {
      fetchCreateUser(usernameInput, passwordInput)
        .then(res => res.json())
        .then(json => {
          if (json.token) {
            localStorage.setItem("token", json.token);
            setUserData(json);
          } else {
            isMessageError = true;
            message = json.username;
          }
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
  //done

  let password,
    phone = "",
    formatted_phone;

  async function formSubmit() {
    if (checkPhoneNumber(phone)) {
      formatted_phone = "+88" + phone;
      console.log(phone, password);

      let request_body = {
        phone: formatted_phone,
        password: password,
      };

      await axios({
        method: "post",
        url: "http://127.0.0.1:8000/auth/customer_auth/login",
        data: request_body,
      })
        .then(function (response) {
          console.log(response);

          if (response.data.userID === null) {
            alert("এই তথ্যে ইউজার নেই। সঠিক তথ্য দিয়ে চেষ্টা করুন।");
          } else {
            
            router.redirect("/");
          }
        })
        .catch(function (err) {
          console.log(err);
        });
    }
  }
</script>

<section id="contact" class="contact">
  <div class="container" data-aos="fade">
    <div class="section-header">
      <h2>Login</h2>
    </div>

    <div class="row gx-lg-0 gy-4">
      <div class="col-4" />

      <div class="col-4 align-self-center">
        <form role="form" class="php-email-form">
          <div class="form-group mt-3">
            <input
              type="text"
              name="phone"
              class="form-control"
              id="phone"
              placeholder="ফোন নাম্বার লিখুন"
              required
              bind:value={phone}
            />
          </div>
          <div class="form-group mt-3">
            <input
              type="password"
              class="form-control"
              name="password"
              id="password"
              placeholder="পাসওয়ার্ড লিখুন"
              required
              bind:value={password}
            />
          </div>
          <!--             
            <div class="my-3">
              <div class="loading">Loading</div>
              <div class="error-message"></div>
              <div class="sent-message">Your message has been sent. Thank you!</div>
            </div> -->
          <div class="text-center form-group mt-3">
            <button
              type="button"
              class="btn btn-success rounded-pill"
              on:click={formSubmit}>Login (লগ ইন করুন)</button
            >
          </div>
        </form>
      </div>
      <!-- End Contact Form -->
    </div>
  </div>
</section>

<!-- End Contact Section -->
<style>
</style>

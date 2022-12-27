<script>
  import axios from "axios";
  import router from "page";
  import { empty } from "svelte/internal";
  import { auth, signInWithCustomToken } from "../firebase_conf";
  import { userTokenStore } from "../utility_functions";
  import { checkPassword, checkPhoneNumber } from "../utility_functions";
  import FormData from "form-data";

  let userToken = $userTokenStore,
    name,
    role,
    username,
    phone,
    formattedPhone,
    userData,
    password = "",
    confirmPassword = "",
    imageUrl = "blank-profile-pic";

  let request_body = {
    token: userToken,
  };

  axios
    .post("http://127.0.0.1:8000/auth/get_user", request_body)
    .then((response) => {
      userData = response.data;
      name = userData.names.name;
      username = userData.names.username;
      phone = userData.credentials.phone.slice(3);
      role = userData.names.role;

      // console.log(userData.credentials.image_url);

      if (userData.credentials.image_url != "") {
        imageUrl = userData.credentials.image_url;
      }
    })
    .catch((error) => {
      console.log(error);
    });

  let filename;

  $: {
    filename = phone + String(Date.now());
    console.log(imageUrl);
  }

  function handleSubmit() {
    let request_body;

    if (password != "" && confirmPassword != "") {
      if (checkPassword(password, confirmPassword) && checkPhoneNumber(phone)) {
        formattedPhone = "+88" + phone;

        request_body = {
          token: userToken,
          name: name,
          phone: formattedPhone,
          username: username,
          password: password,
          confirm_password: confirmPassword,
          role: role,
        };

        axios
          .post("http://127.0.0.1:8000/auth/update_user", request_body)
          .then((response) => {
            console.log(response);
            router.redirect("/dashboard");
          })
          .catch((error) => {
            console.log(error);
          });
      }
    } else if (password == "" && confirmPassword == "") {
      if (checkPhoneNumber(phone)) {
        formattedPhone = "+88" + phone;

        request_body = {
          token: userToken,
          name: name,
          phone: formattedPhone,
          username: username,
          password: "",
          confirm_password: "",
          role: role,
        };

        axios
          .post("http://127.0.0.1:8000/auth/update_user", request_body)
          .then((response) => {
            console.log(response);
            router.redirect("/dashboard");
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
  }
</script>

<!-- <link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
  integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
  crossorigin="anonymous"
/> -->

<section id="contact" class="contact">
  <div class="container">
    <h1>Edit Profile</h1>
    <hr />
    <div class="row">
      <!-- left column -->
      <div class="col-md-4">
        <div class="text-center">
          <img
            src={`http://127.0.0.1:8000/images/get_image?filename=${imageUrl}`}
            class="avatar img-circle"
            alt="avatar"
            width="320px"
            height="320px"
          />
          <h6>অন্য ছবি আপলোড করুন</h6>

          <form
            class="php-email-form"
            method="post"
            action="http://127.0.0.1:8000/auth/update_user_image"
            enctype="multipart/form-data"
          >
            <input
              type="hidden"
              class="form-control"
              name="filename"
              value={filename}
            />
            <input
              type="hidden"
              class="form-control"
              name="role"
              value={role}
            />
            <input
              type="hidden"
              class="form-control"
              name="token"
              value={userToken}
            />
            <input type="file" class="form-control" name="content" />
            <div class="form-group mt-3">
              <button type="submit" class="btn btn-success rounded-pill"
                >নতুন ছবি দিন</button
              >
            </div>
          </form>

          <!-- <input type="file" class="form-control" /> -->
        </div>
      </div>

      <!-- edit form column -->
      <div class="col-md-8 personal-info">
        <h3>Personal info</h3>
        <div class="col-8 align-self-center">
          <form class="php-email-form">
            <div class="form-group mt-3">
              <label class="col-lg-5 control-label">নতুন নাম লিখুন:</label>
              <input
                type="text"
                class="form-control"
                placeholder="নিজের নাম লিখুন"
                bind:value={name}
              />
            </div>
            <div class="form-group mt-3">
              <label class="col-lg-5 control-label">নতুন ইউজার নাম লিখুন:</label
              >
              <input
                type="text"
                class="form-control"
                placeholder="নিজের ইউজার নাম লিখুন"
                bind:value={username}
              />
            </div>
            <div class="form-group mt-3">
              <label class="col-lg-3 control-label">নতুন নাম্বার লিখুন:</label>
              <input
                type="text"
                class="form-control"
                placeholder="নিজের ফোন নাম্বার লিখুন (পূর্বের নাম্বার: {phone})"
                bind:value={phone}
              />
            </div>
            <div class="form-group mt-3">
              <label class="col-lg-5 control-label">নতুন পাসওয়ার্ড লিখুন:</label
              >
              <input
                type="password"
                class="form-control"
                name="password"
                id="password"
                placeholder="নিজের নতুন পাসওয়ার্ড লিখুন"
                bind:value={password}
              />
            </div>
            <div class="form-group mt-3">
              <label class="col-lg-5 control-label"
                >নতুন পাসওয়ার্ড আবার লিখুন:</label
              >
              <input
                type="password"
                class="form-control"
                name="confirm-password"
                id="confirm-password"
                placeholder="নতুন পাসওয়ার্ড আবার লিখুন"
                bind:value={confirmPassword}
              />
            </div>

            <div class="text-center form-group mt-3">
              <button
                type="button"
                class="btn btn-success rounded-pill"
                on:click={handleSubmit}>পরিবর্তন করুন</button
              >
              <span />
              <input
                type="reset"
                class="btn btn-default rounded-pill"
                value="বাতিল করুন"
              />
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- End Contact Section -->
<style>
</style>

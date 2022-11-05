<script>
  import axios from "axios";
  import router from "page";
  import { empty } from "svelte/internal";
  import { auth, signInWithCustomToken } from "../firebase_conf";
  import { userTokenStore } from "../utility_functions";
  import { checkPassword } from "../utility_functions";

  let newName, newPhone, newUsername, newRole, newPass, newRetypePass;

  let request_body = {
    token: $userTokenStore,
  };

  const editProfile = () => {
    newName = document.forms["editProfileForm"]["newName"].value;
    newPass = document.forms["editProfileForm"]["newPass"].value;
    newUsername = document.forms["editProfileForm"]["newUsername"].value;
    newRetypePass = document.forms["editProfileForm"]["newRetypePass"].value;

    if (!newName) {
      newName = name;
    }

    if (!newUsername) {
      newUsername = username;
    }

    if (checkPassword(newPass, newRetypePass)) {
      console.log("New name: ", newName);
      console.log("old name:", name);
      console.log("New username: ", newUsername);
      console.log("old username:", username);
      console.log("New pass: ", newPass);
      console.log("old pass:", pass);

      router.redirect("/dashboard");
    }
  };
  let name, username, phone, role, userData, pass;
  let namePlaceholder, phonePlaceholder, usernamePlaceholder, passPlaceholder;
  let txt1 = "Currently: ";
  axios
    .post("http://127.0.0.1:8000/auth/get_user", request_body)
    .then((response) => {
      userData = response.data;
      name = userData.names.name;
      username = userData.names.username;
      phone = userData.credentials.phone;
      role = userData.names.role;
      pass = "Hidden Pass";

      namePlaceholder = txt1.concat(name);
      phonePlaceholder = txt1.concat(phone);
      usernamePlaceholder = txt1.concat(username);
      passPlaceholder = txt1.concat(pass);
    })
    .catch((error) => {
      console.log(error);
    });
</script>

<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
  integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
  crossorigin="anonymous"
/>

<div class="container">
  <h1>Edit Profile</h1>
  <hr />
  <div class="row">
    <!-- left column -->
    <div class="col-md-3">
      <div class="text-center">
        <img
          src="http://127.0.0.1:8000/images/get_image?filename=blank-profile-pic"
          class="avatar img-circle"
          alt="avatar"
          width="320px"
          height="320px"
        />
        <h6>Upload a different photo...</h6>

        <input type="file" class="form-control" />
      </div>
    </div>

    <!-- edit form column -->
    <div class="col-md-9 personal-info">
      <h3>Personal info</h3>

      <form class="form-horizontal" role="form">
        <div class="form-group">
          <label class="col-lg-3 control-label">First name:</label>
          <div class="col-lg-8">
            <input class="form-control" type="text" value="Jane" />
          </div>
        </div>
        <div class="form-group">
          <label class="col-lg-3 control-label">Last name:</label>
          <div class="col-lg-8">
            <input class="form-control" type="text" value="Bishop" />
          </div>
        </div>
        <div class="form-group">
          <label class="col-lg-3 control-label">Company:</label>
          <div class="col-lg-8">
            <input class="form-control" type="text" value="" />
          </div>
        </div>
        <div class="form-group">
          <label class="col-lg-3 control-label">Email:</label>
          <div class="col-lg-8">
            <input
              class="form-control"
              type="text"
              value="janesemail@gmail.com"
            />
          </div>
        </div>
        <div class="form-group">
          <label class="col-lg-3 control-label">Time Zone:</label>
          <div class="col-lg-8">
            <div class="ui-select">
              <select id="user_time_zone" class="form-control">
                <option value="Hawaii">(GMT-10:00) Hawaii</option>
                <option value="Alaska">(GMT-09:00) Alaska</option>
                <option value="Pacific Time (US &amp; Canada)"
                  >(GMT-08:00) Pacific Time (US &amp; Canada)</option
                >
                <option value="Arizona">(GMT-07:00) Arizona</option>
                <option value="Mountain Time (US &amp; Canada)"
                  >(GMT-07:00) Mountain Time (US &amp; Canada)</option
                >
                <option
                  value="Central Time (US &amp; Canada)"
                  selected="selected"
                  >(GMT-06:00) Central Time (US &amp; Canada)</option
                >
                <option value="Eastern Time (US &amp; Canada)"
                  >(GMT-05:00) Eastern Time (US &amp; Canada)</option
                >
                <option value="Indiana (East)"
                  >(GMT-05:00) Indiana (East)</option
                >
              </select>
            </div>
          </div>
        </div>
        <div class="form-group">
          <label class="col-md-3 control-label">Username:</label>
          <div class="col-md-8">
            <input class="form-control" type="text" value="janeuser" />
          </div>
        </div>
        <div class="form-group">
          <label class="col-md-3 control-label">Password:</label>
          <div class="col-md-8">
            <input class="form-control" type="password" value="11111122333" />
          </div>
        </div>
        <div class="form-group">
          <label class="col-md-3 control-label">Confirm password:</label>
          <div class="col-md-8">
            <input class="form-control" type="password" value="11111122333" />
          </div>
        </div>
        <div class="form-group">
          <label class="col-md-3 control-label" />
          <div class="col-md-8">
            <input type="button" class="btn btn-primary" value="Save Changes" />
            <span />
            <input type="reset" class="btn btn-default" value="Cancel" />
          </div>
        </div>
      </form>
    </div>
  </div>
</div>
<hr />

<!-- End Contact Section -->
<style>
</style>

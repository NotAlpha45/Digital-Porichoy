<script>
  import axios from "axios";
  import { auth, signInWithCustomToken } from "../firebase_conf";
  import { userTokenStore } from "../utility_functions";

  // if (auth.currentUser == null) {
  //   if ($userTokenStore) {
  //     signInWithCustomToken(auth, $userTokenStore)
  //       .then(function (userCredentials) {

  //       })
  //       .catch(function (error) {
  //         console.log(error);
  //       });
  //   }
  // }
  let request_body = {
    token: $userTokenStore,
  };

  let name,
    username,
    phone,
    role,
    userData,
    imageUrl = "blank-profile-pic";

  axios
    .post("http://127.0.0.1:8000/auth/get_user", request_body)
    .then((response) => {
      userData = response.data;
      name = userData.names.name;
      username = userData.names.username;
      phone = userData.credentials.phone;
      role = userData.names.role;
      imageUrl = userData.credentials.image_url;
      // console.log(userData);
    })
    .catch((error) => {
      console.log(error);
    });
</script>

<section id="contact" class="contact">
  <div class="container" data-aos="fade-up">
    <div class="section-title">
      <h2>Profile</h2>
    </div>

    <div class="row">
      <div class="col-lg-4">
        <img
          src={`http://127.0.0.1:8000/images/get_image?filename=${imageUrl}`}
          class="img-fluid"
          alt=""
          width="320px"
          height="320px"
        />
      </div>
      <div class="col-lg-8 pt-4 pt-lg-0 content">
        <h3>{name}</h3>
        <div>
          <br />
        </div>

        <div class="row">
          <div class="col-lg-6">
            <ul>
              
              <li>
                <i class="bi bi-rounded-right" />
                <strong>Username: </strong>{username}
              </li>
              <li>
                <i class="bi bi-rounded-right" />
                <strong>Phone: </strong>{phone}
              </li>
              <li>
                <i class="bi bi-rounded-right" />
                <strong>Role: </strong>{role}
              </li>
            </ul>
            <a href="/edit-profile" class="btn-about">Edit Profile</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- End About Section -->
<style></style>

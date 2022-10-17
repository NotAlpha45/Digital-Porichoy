<script>
  import axios from "axios";
  import router from "page";
  import { checkPhoneNumber } from "../utility_functions";

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

<<<<<<< HEAD
      <div class="row gx-lg-0 gy-4">

      <div class="col-4"></div>

        <div class="col-4 align-self-center">
          <form action="forms/contact.php" method="post" class="php-email-form">
            <div class="form-group mt-3">
                <input type="text" name="name" class="form-control" id="name" placeholder="Your Name" required>
              </div>
              <div class="form-group mt-3">
                <input type="email" class="form-control" name="email" id="email" placeholder="Your Email" required>
              </div>
            
=======
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
>>>>>>> main
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

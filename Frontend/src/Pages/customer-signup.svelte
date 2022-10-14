<script>
  import axios from "axios";
  import router from "page";

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
    if (phoneNumber.length != 11 && !phoneNumber.startsWith("0")) {
      alert("আপনার ফোন নাম্বার ঠিক নেই। আবার লিখুন!");
      return false;
    }
    return true;
  };

  let name,
    username,
    password,
    retype_password,
    email = "",
    phone = "",
    formatted_phone;

  async function formSubmit() {
    if (checkPassword(password, retype_password) && checkPhoneNumber(phone)) {
      formatted_phone = "+88" + phone;
      console.log(phone, password);

      let request_body = {
        userdata: {
          credentials: {
            email: email,
            phone: formatted_phone,
          },
          names: {
            name: name,
            username: username,
            role: "customer",
          },
          service_data: {
            favorite_provider: "",
            favorite_service: "",
            used_service_and_provider: [],
          },
        },
        password: password,
      };

      await axios({
        method: "post",
        url: "http://127.0.0.1:8000/auth/customer_auth/signup",
        data: request_body,
      })
        .then(function (response) {
          console.log(response);
          router.redirect("/home");
        })
        .catch(function (err) {
          console.log(err);
        });
    }
  }
</script>

<div>
  <section
    class="u-clearfix u-image u-shading u-section-1"
    id="sec-4164"
    data-image-width="1280"
    data-image-height="853"
  >
    <div class="u-clearfix u-sheet u-sheet-1">
      <h1
        class="u-align-center u-custom-font u-font-montserrat u-text u-text-default u-text-1"
      >
        Customer Regestration<br />
      </h1>
      <div class="u-form u-form-1">
        <form
          class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form"
          source="email"
          name="form"
          style="padding: 34px;"
        >
          <div class="u-form-group u-form-name">
            <label for="name-a66d" class="u-label">Name (নাম)</label>
            <input
              type="text"
              placeholder="নিজের নাম লিখুন"
              id="name-a66d"
              name="name"
              class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"
              required=""
              bind:value={name}
            />
          </div>
          <div class="u-form-group u-form-name u-form-group-2">
            <label for="name-e2ab" class="u-label">Username (ইউজার নাম)</label>
            <input
              type="text"
              placeholder="নিজের ইউজার নাম লিখুন"
              id="name-e2ab"
              name="username"
              class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"
              required=""
              bind:value={username}
            />
          </div>
          <div class="u-form-group u-form-phone u-form-group-4">
            <label for="phone-f0d1" class="u-label">Phone (ফোন নাম্বার)</label>
            <input
              type="tel"
              placeholder="নিজের ফোন নাম্বার লিখুন (যেমন: +8801778654767)"
              id="phone-f0d1"
              name="phone"
              class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"
              required=""
              bind:value={phone}
            />
          </div>
          <div class="u-form-group u-form-group-5">
            <label for="text-cbc5" class="u-label">Password</label>
            <input
              placeholder="নিজের পাসওয়ার্ড লিখুন"
              id="text-cbc5"
              name="password"
              class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"
              required="required"
              type="password"
              bind:value={password}
            />
          </div>
          <div class="u-form-group u-form-group-6">
            <label for="text-02bd" class="u-label">Retype Password</label>
            <input
              placeholder="আবার পাসওয়ার্ড লিখুন"
              id="text-02bd"
              name="retype_password"
              class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"
              required="required"
              type="password"
              bind:value={retype_password}
            />
          </div>
          <div class="u-align-center u-form-group u-form-submit">
            <button
              on:click={formSubmit}
              href=""
              class="u-border-none u-btn u-btn-round u-btn-submit u-button-style u-hover-palette-1-light-1 u-radius-29"
            >
              Submit (সাবমিট করুন)</button
            >
            <!-- <input type="submit" value="submit" class="u-form-control-hidden" /> -->
          </div>
        </form>
      </div>
    </div>
  </section>
</div>

<style>
  .u-section-1 {
    background-image: linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.6),
        rgba(0, 0, 0, 0.6)
      ),
      url("/images/4fd81a5519456a4e67515f4156f00f145cb103071a001cdce1cb61a4d6728ebf87634fe83768169f955836e0a0b2c939e3eff35a9d54485ad85fe7_1280.jpg");
    background-position: 50% 50%;
  }

  .u-section-1 .u-sheet-1 {
    min-height: 810px;
  }

  .u-section-1 .u-text-1 {
    margin: 67px auto 0;
  }

  .u-section-1 .u-form-1 {
    height: 644px;
    width: 570px;
    margin: 23px auto 24px;
  }

  .u-section-1 .u-form-group-2 {
    margin-left: 0;
  }

  .u-section-1 .u-form-group-4 {
    margin-left: 0;
  }

  .u-section-1 .u-form-group-5 {
    margin-left: 0;
  }

  .u-section-1 .u-form-group-6 {
    margin-left: 0;
  }

  @media (max-width: 1199px) {
    .u-section-1 .u-sheet-1 {
      min-height: 880px;
    }
  }

  @media (max-width: 991px) {
    .u-section-1 .u-sheet-1 {
      min-height: 869px;
    }

    .u-section-1 .u-form-1 {
      margin-bottom: 60px;
    }
  }

  @media (max-width: 767px) {
    .u-section-1 .u-form-1 {
      width: 540px;
      margin-bottom: 30px;
    }
  }

  @media (max-width: 575px) {
    .u-section-1 .u-sheet-1 {
      min-height: 874px;
    }

    .u-section-1 .u-form-1 {
      width: 340px;
    }
  }
</style>

<script>
  import { auth } from "../firebase_conf";
  import axios from "axios";
  import { userTokenStore } from "../utility_functions";

  console.log($userTokenStore);
  // console.log(auth.currentUser)
  // console.log(window.lcoalStorage.getItem("userToken"));

  // if (auth.currentUser !== null) {
  //   auth.currentUser
  //     .getIdToken(true)
  //     .then(function (token) {
  //       console.log("At home page, the user token:", token);
  //       axios({
  //         method: "post",
  //         url: "http://127.0.0.1:8000/auth/verify_token",
  //         data: { token: token },
  //       });
  //     })
  //     .catch(function (error) {
  //       console.log(error);
  //     });
  // }
</script>

<!-- ======= Hero Section ======= -->
<section id="hero" class="hero">
  <div class="container position-relative">
    <div class="row gy-5" data-aos="fade-in">
      <div
        class="col-lg-6 order-2 order-lg-1 d-flex flex-column justify-content-center text-center text-lg-start"
      >
        <h2>Welcome to <br /><span>Digital পরিচয়</span></h2>
        <p>
          Sed autem laudantium dolores. Voluptatem itaque ea consequatur
          eveniet. Eum quas beatae cumque eum quaerat.
        </p>
        <div class="d-flex justify-content-center justify-content-lg-start">
          <a href="#about" class="btn-get-started">Get Started</a>
          <a
            href="https://www.youtube.com/watch?v=LXb3EKWsInQ"
            class="glightbox btn-watch-video d-flex align-items-center"
            ><i class="bi bi-play-circle" /><span>Watch Video</span></a
          >
        </div>
      </div>
      <div class="col-lg-6 order-1 order-lg-2">
        <img
          src="assets/img/hero-img.svg"
          class="img-fluid"
          alt=""
          data-aos="zoom-out"
          data-aos-delay="100"
        />
      </div>
    </div>
  </div>

  <div class="icon-boxes position-relative">
    <div class="container position-relative">
      <div class="row gy-4 mt-5">
        <div class="col-xl-3 col-md-6" data-aos="fade-up" data-aos-delay="100">
          <div class="icon-box">
            <div class="icon"><i class="bi bi-easel" /></div>
            <h4 class="title">
              <a href="" class="stretched-link">Lorem Ipsum</a>
            </h4>
          </div>
        </div>
        <!--End Icon Box -->

        <div class="col-xl-3 col-md-6" data-aos="fade-up" data-aos-delay="200">
          <div class="icon-box">
            <div class="icon"><i class="bi bi-gem" /></div>
            <h4 class="title">
              <a href="" class="stretched-link">Sed ut perspiciatis</a>
            </h4>
          </div>
        </div>
        <!--End Icon Box -->

        <div class="col-xl-3 col-md-6" data-aos="fade-up" data-aos-delay="300">
          <div class="icon-box">
            <div class="icon"><i class="bi bi-geo-alt" /></div>
            <h4 class="title">
              <a href="" class="stretched-link">Magni Dolores</a>
            </h4>
          </div>
        </div>
        <!--End Icon Box -->

        <div class="col-xl-3 col-md-6" data-aos="fade-up" data-aos-delay="500">
          <div class="icon-box">
            <div class="icon"><i class="bi bi-command" /></div>
            <h4 class="title">
              <a href="" class="stretched-link">Nemo Enim</a>
            </h4>
          </div>
        </div>
        <!--End Icon Box -->
      </div>
    </div>
  </div>
</section>

<!-- End Hero Section -->
<style>
</style>

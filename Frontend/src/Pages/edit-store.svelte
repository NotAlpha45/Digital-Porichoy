<script>
  import axios from "axios";
  import Geolocation from "svelte-geolocation";
  import { onMount } from "svelte";
  import { serviceIdStore } from "../utility_functions";
  import { userTokenStore } from "../utility_functions";
  import router from "page";

  const placeHolderImage = "assets/img/blog/blog-1.jpg";
  let displayImage = placeHolderImage;

  let shops = [],
    shop = "",
    selectedShop = "",
    shopName = "",
    category = "",
    description = "",
    proprietor = "",
    openingTime = "",
    closingTime = "",
    closingDay = "",
    imageUrl = "",
    serviceId = "",
    shopPhone = "";

  let offerings = [];

  let imageName = "";

  function mockGetStore() {
    axios
      .get("http://127.0.0.1:8000/services/get_my_service", {
        params: {
          user_token: $userTokenStore,
        },
      })
      .then(function (response) {
        shops.push(response.data.result);
        shop = shops[0];
        shopName = shop.credentials.name;
        category = shop.credentials.category;
        description = shop.credentials.store_description;
        proprietor = shop.credentials.owner;
        openingTime = shop.credentials.opening_time;
        closingTime = shop.credentials.closing_time;
        closingDay = shop.credentials.closing_day;
        offerings = shop.offerings;
        serviceId = shop.credentials.provider_id;
        shopPhone = shop.credentials.phone;

        try {
          imageUrl = shop.credentials.image_url;
          displayImage = `http://127.0.0.1:8000/images/get_image?filename=${imageUrl}`;
        } catch (err) {
          console.error(err);
          displayImage = placeHolderImage;
        }
      });
  }
  $: {
    mockGetStore();

    imageName = "store" + $userTokenStore.slice(0, 5) + String(Date.now());
  }

  onMount(() => {
    const imageForm = document.getElementById("imageForm");
    const editProfileForm = document.getElementById("editProfileForm");

    editProfileForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const editProfileFormData = new FormData(editProfileForm);

      // Make an HTTP request to the server
      fetch("http://127.0.0.1:8000/services/edit_service", {
        method: "POST",
        body: editProfileFormData,
      })
        .then(function (response) {
          response.json().then(function (data) {
            let status = data.status;
            console.log(status);
            if (status == "ok") {
              alert("আপনার সার্ভিস আপডেট হয়েছে হয়েছে");
              router.redirect("/mystore");
            } else if (status == "unavailable") {
              alert("কোনো সমস্যা হয়েছে, আবার চেষ্টা করুন");
            }
          });
        })
        .catch((error) => {
          alert("কোনো একটি সমস্যা হয়েছে, আবার চেষ্টা করুন।");
        });
    });

    imageForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const imageFormData = new FormData(imageForm);

      // Make an HTTP request to the server
      fetch("http://127.0.0.1:8000/services/edit_service_image", {
        method: "POST",
        body: imageFormData,
      })
        .then(function (response) {
          response.json().then(function (data) {
            let status = data.status;
            console.log(status);
            if (status == "ok") {
              alert("আপনার ছবি যোগ হয়েছে");
              router.redirect("/mystore");
            } else if (status == "unavailable") {
              alert("আপনার কোনো স্টোর নেই");
            }
          });
        })
        .catch((error) => {
          alert("কোনো একটি সমস্যা হয়েছে, আবার চেষ্টা করুন।");
        });
    });
  });
  // mockGetStore();
</script>

<!-- <Geolocation getPosition let:coords>
      {console.log(coords)}
    </Geolocation> -->
<main id="main">
  <section id="blog" class="blog">
    <div class="container" data-aos="fade">
      <div class="row g-5">
        <div class="col-lg-8">
          <article class="blog-details">
            <div class="post-img">
              <img src={displayImage} alt="" class="img-fluid" />
            </div>
            <div>
              <form
                id="imageForm"
                class="php-email-form"
                enctype="multipart/form-data"
              >
                <input
                  type="hidden"
                  class="form-control"
                  name="filename"
                  value={imageName}
                />
                <input
                  type="hidden"
                  class="form-control"
                  name="service_id"
                  value={serviceId}
                />
                <input type="file" class="form-control" name="content" />
                <div class="form-group mt-3">
                  <button type="submit" class="btn btn-success rounded-pill"
                    >নতুন ছবি দিন</button
                  >
                </div>
              </form>
            </div>

            <h1 class="title">{shopName}</h1>

            <div class="meta-top">
              <ul>
                <li class="d-flex align-items-center">
                  <i class="bi bi-person" />
                  <a href="blog-details.html">{proprietor}</a>
                </li>
              </ul>
            </div>
            <!-- End meta top -->
          </article>
          <br />
          <article class="blog-details">
            <div class="container" data-aos="fade-up">
              <div class="section-header">
                <h2>নিজের স্টোর আপডেট করুন</h2>
              </div>

              <div class="row gx-lg-0 gy-4">
                <div class="col-4" />
                <div class="col-4">
                  <form class="php-email-form" id="editProfileForm">
                    <input
                      type="hidden"
                      class="form-control"
                      name="user_token"
                      value={$userTokenStore}
                    />
                    <div class="form-group mt-3">
                      দোকানের নাম পরিবর্তন করুন
                      <input
                        type="text"
                        name="new_name"
                        class="form-control"
                        required
                        bind:value={shopName}
                      />
                    </div>

                    <div class="form-group mt-3">
                      খোলার সময়, বন্ধ করার সময় এবং ছুটির দিন সিলেক্ট করুন
                      <input
                        type="time"
                        class="form-control"
                        name="new_opening_time"
                        placeholder="খোলার সময় সিলেক্ট করুন"
                        bind:value={openingTime}
                      />
                      <input
                        type="time"
                        class="form-control"
                        name="new_closing_time"
                        placeholder="বন্ধ করার সময় সিলেক্ট করুন"
                        bind:value={closingTime}
                      />
                      <select
                        class="form-select"
                        aria-label="select-holiday"
                        name="new_closing_day"
                        bind:value={closingDay}
                      >
                        <option value="Saturday-শনিবার">Saturday-শনিবার</option>
                        <option value="Sunday-রবিবার">Sunday-রবিবার</option>
                        <option value="Monday-সোমবার">Monday-সোমবার</option>
                        <option value="Tuesday-মঙ্গলবার"
                          >Tuesday-মঙ্গলবার</option
                        >
                        <option value="Wednesday-বুধবার"
                          >Wednesday-বুধবার</option
                        >
                        <option value="Thursday-বৃহষ্পতিবার"
                          >Thursday-বৃহষ্পতিবার</option
                        >
                        <option value="Friday-শুক্রবার">Friday-শুক্রবার</option>
                      </select>
                    </div>

                    <div class="form-group mt-3">
                      স্টোরের ফোন পরিবর্তন করুন
                      <input
                        type="text"
                        class="form-control"
                        name="new_phone"
                        id="phone"
                        bind:value={shopPhone}
                      />
                    </div>

                    <div class="form-group mt-3">
                      স্টোরের বর্ণনা লিখুন
                      <textarea
                        class="form-control"
                        name="new_store_description"
                        id="desciption"
                        bind:value={description}
                      />
                    </div>

                    <div class="text-center">
                      <button type="submit" class="btn btn-success rounded-pill"
                        >আপডেট করুন</button
                      >
                    </div>
                  </form>
                </div>
                <!-- End Contact Form -->
              </div>
            </div>
          </article>
          <!-- <div>
                <Map />
              </div> -->
        </div>

        <div class="col-lg-4">
          <div class="sidebar">
            <div class="sidebar-item categories">
              <h3 class="sidebar-title">Category</h3>
              <ul class="mt-3">
                <li>{category}</li>
              </ul>
            </div>

            <!-- End sidebar categories-->
          </div>
          <br />
          <div class="sidebar">
            <div class="sidebar-item categories">
              <h3 class="sidebar-title">About</h3>
              <ul class="mt-3">
                <li>{description}</li>
              </ul>
            </div>

            <!-- End sidebar categories-->
          </div>
          <br />
          <div class="sidebar">
            <div class="sidebar-item categories">
              <h3 class="sidebar-title">Service Hours</h3>
              <ul class="mt-3">
                <li><b>Opens:</b> {openingTime}</li>
                <li><b>Closes:</b> {closingTime}</li>
                <li><b>Off-day:</b> {closingDay}</li>
              </ul>
            </div>

            <!-- End sidebar categories-->
          </div>
          <br />

          <!-- End Blog Sidebar -->
        </div>
      </div>
    </div>
  </section>
  <!-- End Blog Details Section -->
</main>

<!-- End #main -->
<style>
</style>

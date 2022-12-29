<script>
  import axios from "axios";
  import Geolocation from "svelte-geolocation";
  import { onMount } from "svelte";
  import { serviceIdStore } from "../utility_functions";
  import Map from "./map.svelte";
  import { userTokenStore } from "../utility_functions";

  serviceIdStore.set(localStorage.getItem("selectedService"));

  console.log(localStorage.getItem("selectedService"));

  const placeHolderImage = "assets/img/blog/blog-1.jpg";
  let displayImage = placeHolderImage;

  let shops = [],
    shop = "",
    selectedShop,
    shopName = "",
    category = "",
    description = "",
    proprietor = "",
    openingTime = "",
    closingTime = "",
    closingDay = "",
    imageUrl = "";

  let offerings = [];

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
        console.log(offerings);

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
  }
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

            <h1 class="title">{shopName}</h1>

            <div class="meta-top">
              <ul>
                <li class="d-flex align-items-center">
                  <i class="bi bi-person" />
                  <a href="/dashboard"><h5>{proprietor}</h5></a>
                </li>
              </ul>
            </div>
            <!-- End meta top -->
          </article>
          <br />
          <article class="blog-details">
            <h1 class="title">Products/Services</h1>

            <div
              class="container h-100 d-flex justify-content-center align-items-center"
            >
              <div class="col-md-12">
                {#each offerings as offering}
                  <br />
                  <article class="blog-details">
                    <div class="row no-gutters">
                      <div class="col-md-4">
                        <img
                          src={`http://127.0.0.1:8000/images/get_image?filename=${offering.offering_image_url}`}
                          alt=""
                          class="card-img"
                        />
                      </div>

                      <div class="col-md-8">
                        <div class="card-body">
                          <h4 class="card-title">
                            <strong>{offering.offering_name}</strong>
                          </h4>
                          <h5 class="card-text">
                            দামঃ {offering.offering_price}৳
                          </h5>
                          <p class="card-text">
                            {offering.offering_description}
                          </p>
                        </div>
                      </div>
                    </div>
                  </article>
                {/each}
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
          <div class="sidebar">
            <div class="sidebar-item categories">
              <ul class="mt-3">
                <li>
                  <a href="/add-product" style="color: teal;"
                    ><i class="bi bi-plus-circle" /> Add Product</a
                  >
                </li>

                <li>
                  <a href="/editstore" style="color: teal;"
                    ><i class="bi bi-pencil-square" /> Edit Store</a
                  >
                </li>
              </ul>
            </div>

            <!-- End sidebar categories-->
          </div>
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

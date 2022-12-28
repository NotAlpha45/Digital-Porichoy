<script>
  import Map from "./map.svelte"
  import axios from "axios";
  import router, { show } from "page";
  import { serviceIdStore } from "../utility_functions";
  import Geolocation from "svelte-geolocation";

  let coords = [-1, -1];

  function getStore() {
    router.redirect("/store");
  }

  let shops = [],
    category = "Mechanic/মেকানিক",
    district = "Gazipur/গাজীপুর",
    showAll = false;

  async function mockGetStore(category, district) {
    await axios
      .get("http://127.0.0.1:8000/services/search_service", {
        params: {
          district: district,
          category: category,
          long: coords[0],
          lat: coords[1],
          distance: 10,
          search_limit: 50,
        },
      })
      .then(function (response) {
        shops = response.data.result;
        // console.log(shops);
      });
  }

  function submit() {
    // get the selected values of the dropdowns and checkbox
    category = document
      .getElementById("category")
      .value.split("/")[0]
      .toLowerCase();
    district = document
      .getElementById("district")
      .value.split("/")[0]
      .toLowerCase();
    showAll = document.getElementById("show-all").checked;

    // run the function using the selected values
    // runFunction(category, district, showAll);
    // console.log(category);
    // console.log(district);
  }

  // This section activates whenever an element (category is changed)
  $: {
    navigator.geolocation.getCurrentPosition(function (location) {
      coords[0] = location.coords.longitude;
      coords[1] = location.coords.latitude;
    });

    if (
      (coords[0] != -1 || coords[1] != -1) &&
      category !== null &&
      district !== null
    ) {
      let selectedCategory = category.split("/")[0].toLowerCase();
      let selectedDistrict = district.split("/")[0].toLowerCase();
      mockGetStore(selectedCategory, selectedDistrict);
    }
    console.log(category, district, coords, showAll, $serviceIdStore);
  }
</script>

  <!-- ======= Breadcrumbs ======= -->
  <div class="breadcrumbs">
    <div></div>
      <div class="page-header d-flex align-items-center" style="background-image: url('');">
        <div class="container position-relative">
          <div class="row d-flex justify-content-center">
            <div class="col-lg-6 text-center">
              <div class="form-container">
                  <form class="form-inline">
                    <div class="form-group mb-2">
                      <br>
                      <label for="category" style="color: rgba(255, 255, 255, 0.8); font-weight: 900 ">ধরণ পছন্দ করুন</label>
                      <select
                        class="form-control"
                        id="category"
                        bind:value={category}
                      >
                        <option>Mechanic/মেকানিক</option>
                        <option>Service/সার্ভিস</option>
                        <option>Business/ব্যবসা</option>
                      </select>
                    </div>
                    <div class="form-group mb-2">
                      <label for="district" class="sr-only" style="color: rgba(255, 255, 255, 0.8); font-weight: 900 ">জেলা পছন্দ করুন</label>
                      <select
                        class="form-control"
                        id="district"
                        bind:value={district}
                      >
                        <option>Gazipur/গাজীপুর</option>
                        <option>Dhaka/ঢাকা</option>
                        <option>Rajshahi/রাজশাহী</option>
                        <option>Rangpur/রংপুর</option>
                      </select>
                    </div>
                    <div class="form-check col-md-4">
                      <input
                        type="checkbox"
                        class="form-check-input"
                        id="show-all"
                        bind:checked={showAll}
                      />
                      <label class="form-check-label" for="show-all" style="color: rgba(255, 255, 255, 0.8); font-weight: 900 "
                        >সব দোকান/সেবা দেখান</label
                      >
                    </div>
                    <!-- <button
                      type="submit"
                      class="btn btn-success rounded-pill"
                      on:click={submit}>দোকান/সার্ভিস খুঁজুন</button
                    > -->
                  </form>
                </div>
      
            </div>
          </div>
        </div>
      </div>
      
    </div><!-- End Breadcrumbs -->

    <!-- ======= Blog Section ======= -->
    <section id="blog" class="blog">
      <div class="container" data-aos="fade-in">
        
    

        <div class="row gy-4 posts-list">
          {#each shops as shop}
          <div class="col-xl-4 col-md-6">
            <article>

              <div class="post-img">
                <img src="http://127.0.0.1:8000/images/get_image?filename=blank-mechanic-pic2" alt="" class="img-fluid">
              </div>

              <p class="post-category">{shop.credentials.category}</p>

              <h2 class="title">
                  <button
                  type="button"
                  class="storebutton"
                  on:click={getStore}
                  on:click={() => {
                    let serviceId = shop.credentials.provider_id;
                    // serviceIdStore.set(shopIndex);

                    localStorage.setItem("selectedService", serviceId);
                    serviceIdStore.set(
                      localStorage.getItem("selectedService")
                    );
                  }}
                >
                  {shop.credentials.name}
                </button>
              </h2>

              

            </article>
          </div>
          {/each}
          

        </div><!-- End blog posts list -->

        

      </div>
    </section><!-- End Blog Section -->

<style>
  .form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  
</style>



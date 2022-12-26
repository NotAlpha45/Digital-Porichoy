<script>
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

    if (coords !== [] && category !== null && district !== null) {
      let selectedCategory = category.split("/")[0].toLowerCase();
      let selectedDistrict = district.split("/")[0].toLowerCase();
      mockGetStore(selectedCategory, selectedDistrict);
    }
    console.log(category, district, coords, showAll, $serviceIdStore);
  }
</script>

<section id="portfolio" class="portfolio sections-bg">
  <div class="container" data-aos="fade-up">
    <div class="section-header">
      <h2>Search For Service</h2>
      <div class="row gx-lg-0 gy-4 justify-content-center">
        <div class="col-4">
          <div class="form-group mt-3 align-items-center">
            <h5>খোঁজার অপশন দিন</h5>
          </div>

          <div class="form-container">
            <form class="form-inline">
              <div class="form-group mb-2">
                <label for="category" class="sr-only">ধরণ পছন্দ করুন</label>
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
                <label for="district" class="sr-only">জেলা পছন্দ করুন</label>
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
              <div class="form-check mb-2">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="show-all"
                  bind:checked={showAll}
                />
                <label class="form-check-label" for="show-all"
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

          <!-- <div class="form-group mt-3">
            <select
              class="form-select"
              aria-label="select-store"
              bind:value={category}
              placeholder="Select"
            >
              <option value="mechanic">Mechanic-মেকানিক</option>
              <option value="business">Business-ব্যবসা</option>
              <option value="labour">Labour-শ্রমিক</option>
            </select>
          </div> -->
        </div>
      </div>
    </div>
  </div>
</section>

<section id="portfolio" class="portfolio sections-bg">
  <div class="container" data-aos="fade-up">
    <div class="section-header">
      <h2>Stores and Services</h2>
    </div>

    <div
      class="portfolio-isotope"
      data-portfolio-filter="*"
      data-portfolio-layout="masonry"
      data-portfolio-sort="original-order"
      data-aos="fade-up"
      data-aos-delay="10"
    >
      <div class="row gy-4 portfolio-container">
        {#each shops as shop}
          <div class="col-xl-4 col-md-6 portfolio-item filter-app">
            <div class="portfolio-wrap">
              <a
                href="http://127.0.0.1:8000/images/get_image?filename=blank-mechanic-pic2"
                data-gallery="portfolio-gallery-app"
                class="glightbox"
                ><img
                  src="http://127.0.0.1:8000/images/get_image?filename=blank-mechanic-pic2"
                  class="img-fluid"
                  alt=""
                  href="/store"
                /></a
              >
              <div class="portfolio-info">
                <h4>
                  <button
                    type="button"
                    class="btn btn-success rounded-pill"
                    on:click={getStore}
                    on:click={() => {
                      let shopIndex = shop.credentials.provider_id;
                      serviceIdStore.set(shopIndex);
                    }}
                  >
                    {shop.credentials.name}
                  </button>
                  <!-- <a href="/store" title="More Details"
                    >{shop.credentials.name}</a
                  > -->
                </h4>
                <p>{shop.credentials.store_description}</p>
              </div>
            </div>
          </div>
          <!-- End Portfolio Item -->
        {/each}
      </div>
      <!-- End Portfolio Container -->
    </div>
  </div>
</section>

<!-- End Portfolio Section -->
<style>
  .form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>

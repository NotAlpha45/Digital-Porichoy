<script>
  import axios from "axios";
  import router from "page";
  import { serviceIdStore } from "../utility_functions";

  let category = null,
    shopIndex = null;

  function getStore() {
    router.redirect("/store");
  }

  let shops = [];
  function mockGetStore() {
    axios
      .get("http://127.0.0.1:8000/services/search_service", {
        params: {
          district: "gazipur",
          category: category,
          long: 90.38090089366824,
          lat: 23.948577732828085,
          distance: 10,
          search_limit: 50,
        },
      })
      .then(function (response) {
        shops = response.data.result;
        // console.log(shops);
      });
  }

  // This section activates whenever an element (category is changed)
  $: {
    if (category !== null) {
      console.log(shopIndex);
      console.log(category);
      mockGetStore();
    }
  }
</script>

<section id="portfolio" class="portfolio sections-bg">
  <div class="container" data-aos="fade-up">
    <div class="section-header">
      <h2>Stores and Services</h2>
    </div>

    <div class="row gx-lg-0 gy-4 align-items-center">
      <div class="col-4">
        <div class="form-group mt-3">
          ধরণ পছন্দ করুন
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
        </div>
      </div>
    </div>

    <div
      class="portfolio-isotope"
      data-portfolio-filter="*"
      data-portfolio-layout="masonry"
      data-portfolio-sort="original-order"
      data-aos="fade-up"
      data-aos-delay="10"
    >
      <div>
        <ul class="portfolio-flters">
          <!-- <li data-filter="*" class="filter-active">All</li>
            <li data-filter=".filter-app">App</li>
            <li data-filter=".filter-product">Product</li>
            <li data-filter=".filter-branding">Branding</li>
            <li data-filter=".filter-books">Books</li> -->
        </ul>
        <!-- End Portfolio Filters -->
      </div>

      <div class="row gy-4 portfolio-container">
        {#each shops as shop}
          <div class="col-xl-4 col-md-6 portfolio-item filter-app">
            <div class="portfolio-wrap">
              <a
                href="assets/img/portfolio/app-1.jpg"
                data-gallery="portfolio-gallery-app"
                class="glightbox"
                ><img
                  src="assets/img/portfolio/app-1.jpg"
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
                      shopIndex = shop.credentials.provider_id;
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
        <!-- <div class="col-xl-4 col-md-6 portfolio-item filter-product">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/product-1.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/product-1.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Product 1</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item -->

        <!-- <div class="col-xl-4 col-md-6 portfolio-item filter-branding">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/branding-1.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/branding-1.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Branding 1</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-books">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/books-1.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/books-1.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Books 1</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-app">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/app-2.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/app-2.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">App 2</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-product">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/product-2.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/product-2.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Product 2</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-branding">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/branding-2.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/branding-2.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Branding 2</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-books">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/books-2.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/books-2.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Books 2</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-app">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/app-3.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/app-3.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">App 3</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-product">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/product-3.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/product-3.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Product 3</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-branding">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/branding-3.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/branding-3.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Branding 3</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div><!-- End Portfolio Item 

          <div class="col-xl-4 col-md-6 portfolio-item filter-books">
            <div class="portfolio-wrap">
              <a href="assets/img/portfolio/books-3.jpg" data-gallery="portfolio-gallery-app" class="glightbox"><img src="assets/img/portfolio/books-3.jpg" class="img-fluid" alt=""></a>
              <div class="portfolio-info">
                <h4><a href="portfolio-details.html" title="More Details">Books 3</a></h4>
                <p>Lorem ipsum, dolor sit amet consectetur</p>
              </div>
            </div>
          </div>End Portfolio Item -->
      </div>
      <!-- End Portfolio Container -->
    </div>
  </div>
</section>

<!-- End Portfolio Section -->
<style>
</style>

<script>
  //   import mapboxgl from "mapbox-gl/dist/mapbox-gl";
  import { onMount } from "svelte";
  import axios from "axios";
  import router from "page";

  let user_longitude = null,
    user_latitude = null;
  let coords = [-1, -1];
  let shops = [],
    category = "Mechanic/মেকানিক",
    district = "Gazipur/গাজীপুর";

  function getStore() {
    router.redirect("/store");
  }

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
        console.log(shops);
      });
  }

  let map, geoLocator;

  function renderMap() {
    mapboxgl.accessToken =
      "pk.eyJ1IjoibWFoZWVubWFzaHJ1ciIsImEiOiJjbDk5cnBxdW4xM2g3M3hsbWtwcnN6cHB2In0.38PIrzXSblk36C64gerW4w";
    map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/outdoors-v11",
      center: [90.38, 23.94], // starting position
      zoom: 14, // starting zoom
    });

    // // Fullscreen and navigation control
    map.addControl(new mapboxgl.NavigationControl());
    map.addControl(new mapboxgl.FullscreenControl());

    geoLocator = new mapboxgl.GeolocateControl({
      positionOptions: {
        enableHighAccuracy: true,
      },
      // When active the map will receive updates to the device's location as it changes.
      trackUserLocation: true,
      // Draw an arrow next to the location dot to indicate which direction the device is heading.
      showUserHeading: true,
    });

    // Add geolocate control to the map.
    map.addControl(geoLocator);

    geoLocator.on("geolocate", function (location) {
      user_longitude = location.coords.longitude;
      user_latitude = location.coords.latitude;

      console.log(user_longitude, user_latitude);
    });

    // Add mouse move control
    // map.on("click", (e) => {
    //   coords = {
    //     longitude: e.lngLat.wrap().lng,
    //     latitude: e.lngLat.wrap().lat,
    //   };
    //   console.log(coords);
    // });
  }
  function displayButton() {
    console.log("I was pressed again!");
  }

  function displayShopsOnMap(shops) {
    console.log(shops);
    // add markers to map
    for (const shop of shops) {
      // console.log(shop);
      // create a HTML element for each shop

      const marker = document.createElement("div");
      marker.className = "markerContainer";

      marker.style.backgroundImage = "url(images/placeholder.png)";
      marker.style.width = "18px";
      marker.style.height = "16px";
      marker.style.borderRadius = "50%";

      // make a marker for each shop and add to the map

      let popupObject = new mapboxgl.Popup({ offset: 25 }) // add popups
        .setHTML(
          `
          
            <div class="col-xl-4 col-md-6">
            <article>
              <p class="post-category">${shop.credentials.category}</p>

              <h6 class="title">
                  ${shop.credentials.name}
              </h6>
            </article>
          </div>`
        );

      // popupObject.getElementById().addEventListener("click", () => {
      //   // your logic here
      //   console.log("OK");
      // });
      popupObject.setLngLat([shop.location.long, shop.location.lat]).addTo(map);
      // new mapboxgl.Marker(marker)
      //   .setLngLat([shop.location.long, shop.location.lat])
      //   .setPopup(popupObject)
      //   .addTo(map);

      // document.getElementById("storeButton").addEventListener("click", () => {
      //   alert("OK");
      // });
    }
    // const btn = document.getElementsById("storeButton");
    // btn.addEventListener("click", () => {
    //   console.log("hello");
    // });
  }

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
      // console.log(shops);
    }
  }

  onMount(() => {
    const form = document.getElementById("searchForm");

    // Listen for the submit event on the form
    form.addEventListener("submit", function (event) {
      displayShopsOnMap(shops);
      // Prevent the default form submission behavior
      event.preventDefault();
    });

    renderMap();
  });
</script>

<!-- <div class="d-flex justify-content-center"> -->
<div id="map" />
<div class="breadcrumbs">
  <div />
  <div
    class="page-header d-flex align-items-center"
    style="background-image: url(''); background-color:transparent; max-width:110vh; max-height:50vh"
  >
    <div class="col-lg-6 text-center">
      <div class="row d-flex justify-content-center">
        <div class="col-lg-6 text-center">
          <div class="form-container">
            <form class="form-inline" id="searchForm">
              <div class="form-group mb-2">
                <br />
                <label for="category" style="color: black; font-weight: 900 "
                  >ধরণ পছন্দ করুন</label
                >
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
                <label
                  for="district"
                  class="sr-only"
                  style="color: black; font-weight: 900 ">জেলা পছন্দ করুন</label
                >
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

              <button type="submit" class="btn btn-success rounded-pill"
                >দোকান/সার্ভিস খুঁজুন</button
              >
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- End Breadcrumbs -->

<!-- </div> -->
<style>
  .mapboxgl-popup {
    max-width: 200px;
  }

  .mapboxgl-popup-content {
    text-align: left;
    font-family: "Open Sans", sans-serif;
  }
  #map {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
  }
</style>

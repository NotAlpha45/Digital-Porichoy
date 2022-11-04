<script>
  import axios from "axios";
  import router from "page";
  import { userTokenStore } from "../utility_functions";
  import Geolocation from "svelte-geolocation";
  import { auth } from "../firebase_conf";

  let mycoords = [],
    coords = [];
  let userID,
    name,
    username,
    trade_license,
    category = "",
    district,
    email = "",
    phone = "",
    formatted_phone,
    openingTime,
    closingTime,
    ownerName,
    description,
    closingDay;

  async function formSubmit() {
    formatted_phone = "+88" + phone;
    mycoords = coords;

    ownerName = auth.currentUser.displayName;
    userID = auth.currentUser.uid;

    let request_body = {
      credentials: {
        provider_id: userID,
        trade_license: trade_license,
        category: category,
        name: name,
        phone: formatted_phone,
        owner: ownerName,
        opening_time: openingTime,
        closing_time: closingTime,
        closing_day: closingDay,
        store_description: description,
      },
      location: {
        district: district,
        long: mycoords[0],
        lat: mycoords[1],
      },
      offerings: [],
      ratings: [],
    };

    await axios({
      method: "post",
      url: "http://127.0.0.1:8000/services/create_service",
      data: request_body,
    })
      .then(function (response) {
        console.log(response);

        if (response.data.provider_id == "exists") {
          alert("এই স্টোর তৈরি করাই আছে।");
        } else if (response.data.provider_id == null) {
          alert("আপনি কোনো সেবাদাতা নন!");
        } else {
          console.log(response.data.provider_id);
          router.redirect("/store");
        }
      })
      .catch(function (err) {
        console.log(err);
      });
  }
  //   onMount(() => {
  //   mapboxgl.accessToken =
  //       "pk.eyJ1IjoibWFoZWVubWFzaHJ1ciIsImEiOiJjbDk5cnBxdW4xM2g3M3hsbWtwcnN6cHB2In0.38PIrzXSblk36C64gerW4w";
  //     const map = new mapboxgl.Map({
  //       container: "map",
  //       style: "mapbox://styles/mapbox/outdoors-v11",
  //       center: [90.38, 23.94], // starting position
  //       zoom: 15, // starting zoom
  //     });

  //     // // Fullscreen and navigation control
  //     map.addControl(new mapboxgl.NavigationControl());
  //     map.addControl(new mapboxgl.FullscreenControl());

  //     let geoLocator = new mapboxgl.GeolocateControl({
  //       positionOptions: {
  //         enableHighAccuracy: true,
  //       },
  //       // When active the map will receive updates to the device's location as it changes.
  //       trackUserLocation: true,
  //       // Draw an arrow next to the location dot to indicate which direction the device is heading.
  //       showUserHeading: true,
  //     });

  //     // Add geolocate control to the map.
  //     map.addControl(geoLocator);

  //     geoLocator.on("geolocate", function (location) {
  //       user_longitude = location.coords.longitude;
  //       user_latitude = location.coords.latitude;

  //       console.log(user_longitude, user_latitude);
  //     });

  //     // Add mouse move control
  //     // map.on("click", (e) => {
  //     //   coords = {
  //     //     longitude: e.lngLat.wrap().lng,
  //     //     latitude: e.lngLat.wrap().lat,
  //     //   };
  //     //   console.log(coords);
  //     // });
  //   })
</script>

<!-- <Geolocation getPosition bind:mycoords /> -->

<Geolocation getPosition bind:coords>
  {console.log(coords)}
</Geolocation>
<section id="contact" class="contact">
  <div class="container" data-aos="fade-up">
    <div class="section-header">
      <h2>Store Registration - স্টোর রেজিস্ট্রেশন</h2>
    </div>

    <div class="row gx-lg-0 gy-4">
      <div class="col-4" />
      <div class="col-4">
        <form class="php-email-form">
          <div class="form-group mt-3">
            <input
              type="text"
              name="name"
              class="form-control"
              id="name"
              placeholder="স্টোরের নাম লিখুন"
              required
              bind:value={name}
            />
          </div>
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

          <div class="form-group mt-3">
            খোলার সময়, বন্ধ করার সময় এবং ছুটির দিন সিলেক্ট করুন
            <input
              type="time"
              name="openingTime"
              class="form-control"
              id="openingTime"
              placeholder="খোলার সময় সিলেক্ট করুন"
              required
              bind:value={openingTime}
            />
            <input
              type="time"
              name="closingTime"
              class="form-control"
              id="closingTime"
              placeholder="বন্ধ করার সময় সিলেক্ট করুন"
              required
              bind:value={closingTime}
            />
            <select
              class="form-select"
              aria-label="select-holiday"
              bind:value={closingDay}
              placeholder="Select"
            >
              <option value="Saturday-শনিবার">Saturday-শনিবার</option>
              <option value="Sunday-রবিবার">Sunday-রবিবার</option>
              <option value="Monday-সোমবার">Monday-সোমবার</option>
              <option value="Tuesday-মঙ্গলবার">Tuesday-মঙ্গলবার</option>
              <option value="Wednesday-বুধবার">Wednesday-বুধবার</option>
              <option value="Thursday-বৃহষ্পতিবার">Thursday-বৃহষ্পতিবার</option>
              <option value="Friday-শুক্রবার">Friday-শুক্রবার</option>
            </select>
          </div>

          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              name="phone"
              id="phone"
              placeholder="স্টোরের ফোন নাম্বার লিখুন (যেমন: 01778654707)"
              required
              bind:value={phone}
            />
          </div>
          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              name="password"
              id="text"
              placeholder="জেলার নাম লিখুন"
              required
              bind:value={district}
            />
          </div>
          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              name="trade-license"
              id="trade-license"
              placeholder="ট্রেড লাইসেন্স নাম্বার লিখুন"
              required
              bind:value={trade_license}
            />
          </div>

          <div class="form-group mt-3">
            <textarea
              class="form-control"
              name="description"
              id="desciption"
              placeholder="নিজের সেবা সম্পর্কে লিখুন"
              required
              bind:value={description}
            />
          </div>

          <div class="text-center form-group mt-3">
            <button
              type="button"
              class="btn btn-success rounded-pill"
              on:click={formSubmit}>Register - রেজিস্টার</button
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

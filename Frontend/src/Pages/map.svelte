<script>
    import mapboxgl from "mapbox-gl/dist/mapbox-gl";
    import { onMount } from "svelte";
  
    let user_longitude, user_latitude;
    console.log("Component Loaded");
  
    // onMount function renders something after the html containers has been mounted
    onMount(() => {
      console.log("Component mounted");
      // const location_data = {
      //   type: "FeatureCollection",
      //   features: [
      //     {
      //       type: "Feature",
      //       geometry: {
      //         type: "Point",
      //         coordinates: [90.38272198584104, 23.942261777079167],
      //       },
      //       properties: {
      //         title: "মানিক রিপেয়ার",
      //         description: "গাড়ির সার্ভিস",
      //       },
      //     },
      //     {
      //       type: "Feature",
      //       geometry: {
      //         type: "Point",
      //         coordinates: [90.37625317148104, 23.93432319934628],
      //       },
      //       properties: {
      //         title: "হাসান রিপেয়ার",
      //         description: "গাড়ির সার্ভিস",
      //       },
      //     },
      //   ],
      // };
  
      // mapboxgl.accessToken =
      //   "pk.eyJ1IjoibWFoZWVubWFzaHJ1ciIsImEiOiJjbDk5cnBxdW4xM2g3M3hsbWtwcnN6cHB2In0.38PIrzXSblk36C64gerW4w";
      // const map = new mapboxgl.Map({
      //   container: "map-container",
      //   style: "mapbox://styles/mapbox/outdoors-v11",
      //   center: [90.38, 23.94], // starting position
      //   zoom: 15, // starting zoom
      // });
  
      // // Fullscreen and navigation control
      // map.addControl(new mapboxgl.NavigationControl());
      // map.addControl(new mapboxgl.FullscreenControl());
  
      // // Add geolocate control to the map.
      // map.addControl(
      //   new mapboxgl.GeolocateControl({
      //     positionOptions: {
      //       enableHighAccuracy: true,
      //     },
      //     // When active the map will receive updates to the device's location as it changes.
      //     trackUserLocation: true,
      //     // Draw an arrow next to the location dot to indicate which direction the device is heading.
      //     showUserHeading: true,
      //   })
      // );
  
      // let coords;
      // // Add mouse move control
      // map.on("click", (e) => {
      //   coords = {
      //     longitude: e.lngLat.wrap().lng,
      //     latitude: e.lngLat.wrap().lat,
      //   };
      //   console.log(coords);
      // });
  
      // // add markers to map
      // for (const feature of location_data.features) {
      //   // create a HTML element for each feature
      //   const marker = document.createElement("div");
      //   marker.className = "marker";
  
      //   marker.style.backgroundImage = "url(images/placeholder.png)";
      //   marker.style.width = "18px";
      //   marker.style.height = "16px";
      //   //   marker.style.borderRadius = "50%";
  
      //   // make a marker for each feature and add to the map
      //   new mapboxgl.Marker(marker)
      //     .setLngLat(feature.geometry.coordinates)
      //     .setPopup(
      //       new mapboxgl.Popup({ offset: 25 }) // add popups
      //         .setHTML(
      //           `<h3>${feature.properties.title}</h3><p>${feature.properties.description}</p>`
      //         )
      //     )
      //     .addTo(map);
      // }
    });
  </script>
  
  <meta
    name="viewport"
    content="width=device-width, height=device-height, initial-scale=1"
  />
  
  <!-- <div class="main">
    <div>
      <h1>Map Page!</h1>
    </div>
  
    <div id="map-container" class="map" />
  </div> -->
  
  <h1>Map</h1>
  
  <style>
    .mapboxgl-popup {
      max-width: 200px;
    }
  
    .mapboxgl-popup-content {
      text-align: center;
      font-family: "Open Sans", sans-serif;
    }
    .main {
      width: 100%;
      height: 500px;
      align-items: center;
      text-align: center;
    }
    .map {
      width: 70%;
      height: 100%;
      margin-left: auto;
      margin-right: auto;
      align-items: center;
    }
  </style>
  
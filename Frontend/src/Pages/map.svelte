<script>
  import mapboxgl from "mapbox-gl/dist/mapbox-gl";
  import { onMount } from "svelte";

  // onMount function renders something after the html containers has been mounted
  onMount(() => {
    mapboxgl.accessToken =
      "pk.eyJ1IjoibWFoZWVubWFzaHJ1ciIsImEiOiJjbDk5cnBxdW4xM2g3M3hsbWtwcnN6cHB2In0.38PIrzXSblk36C64gerW4w";
    const map = new mapboxgl.Map({
      container: "map-container",
      style: "mapbox://styles/mapbox/outdoors-v11",
      center: [90.38, 23.94], // starting position
      zoom: 15, // starting zoom
    });

    map.addControl(new mapboxgl.NavigationControl());

    map.addControl(new mapboxgl.FullscreenControl());

    // Add geolocate control to the map.
    map.addControl(
      new mapboxgl.GeolocateControl({
        positionOptions: {
          enableHighAccuracy: true,
        },
        // When active the map will receive updates to the device's location as it changes.
        trackUserLocation: true,
        // Draw an arrow next to the location dot to indicate which direction the device is heading.
        showUserHeading: true,
      })
    );

    let coords;
    // Add mouse move control
    map.on("click", (e) => {
      coords = { lang: e.lngLat.wrap().lng, lat: e.lngLat.wrap().lat };
      console.log(coords);
    });
  });
</script>

<meta
  name="viewport"
  content="width=device-width, height=device-height, initial-scale=1"
/>
<div class="main">
  <div>
    <h1>Map Page!</h1>
  </div>
  <div id="map-container" class="map" />
</div>

<style>
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

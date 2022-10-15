<script>
  import Navbar from "./components/Navbar.svelte";
  import CustomerSignup from "./Pages/customer-signup.svelte";
  import CustomerLogin from "./Pages/customer-login.svelte";
  import Home from "./Pages/home.svelte";
  import Map from "./Pages/map.svelte";
  import router from "page";

  let page;

  router("/map", () => {
    page = Map;
  });

  router("/customer-signup", () => {
    page = CustomerSignup;
  });

  router("/customer-login", () => {
    page = CustomerLogin;
  });

  router("/", () => {
    page = Home;
  });

  router.start();
</script>

<main>
  <Navbar />
  <svelte:component this={page} />
  <!-- <h1>Hello {name}!</h1>
  <p>
    Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
    how to build Svelte apps.
  </p> -->
</main>

<style>
</style>

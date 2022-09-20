<script>
  import Navbar from "./components/Navbar.svelte";
  import CustomerLogin from "./Pages/customer-login.svelte";
  import router from "page";
  let page;

  router("/customer-signup", () => (page = CustomerLogin));
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

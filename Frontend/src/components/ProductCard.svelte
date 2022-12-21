<script>
  export let cardContent;
</script>

<div class="card mb-3" style="max-width: 700px;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <!-- svelte-ignore a11y-img-redundant-alt -->
      <img
        src={`http://127.0.0.1:8000/images/get_image?filename=${cardContent.offering_image_url}`}
        class="card-img"
        alt="Product image"
      />
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h4 class="card-title">{cardContent.offering_name}</h4>
        <h5 class="card-text">দামঃ {cardContent.offering_price}৳</h5>
        <p class="card-text">
          {cardContent.offering_description}
        </p>
        <p class="card-text">
          <small class="text-muted">Last updated 3 mins ago</small>
        </p>
      </div>
    </div>
  </div>
</div>

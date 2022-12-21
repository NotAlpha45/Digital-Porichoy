<script>
  import axios from "axios";
  import { userTokenStore } from "../utility_functions";

  function deleteOffering(offering) {
    axios
      .post("http://127.0.0.1:8000/services/remove_offering", {
        user_token: $userTokenStore,
        deleted_offering: offering,
      })
      .then((response) => {
        let confirmation = response.data.status;
        if (confirmation == "ok") {
          alert("আপনার পণ্য/সার্ভিস বাতিল করা হয়েছে");
        } else {
          alert("কোনো একটি সমস্যা হয়েছে, আবার চেষ্টা করুন");
        }
      })
      .catch((error) => {
        alert("কোনো একটি সমস্যা হয়েছে, আবার চেষ্টা করুন");
        console.log(error);
      });
  }
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
        <button
          type="submit"
          on:click={() => {
            deleteOffering(cardContent);
          }}
          class="btn btn-danger rounded-pill">পণ্য/সার্ভিস বাতিল করুন</button
        >
      </div>
    </div>
  </div>
</div>

<script>
  import { userTokenStore } from "../utility_functions";
  import axios from "axios";
  import { onMount } from "svelte";

  let imageUrl = "blank-product-pic",
    filename,
    role,
    userToken;

  // Image name for a service = store/user id + current time
  $: {
    userToken = $userTokenStore;
    filename = $userTokenStore.slice(0, 5) + String(Date.now());
  }

  onMount(() => {
    const form = document.getElementById("addProductForm");

    // Listen for the submit event on the form
    form.addEventListener("submit", function (event) {
      // Prevent the default form submission behavior
      event.preventDefault();

      // Get the form data
      const formData = new FormData(form);

      // Make an HTTP request to the server
      fetch("http://127.0.0.1:8000/services/add_offering", {
        method: "POST",
        body: formData,
      })
        .then(function (response) {
          response.json().then(function (data) {
            let status = data.status;
            if (status == "ok") {
              alert("আপনার পণ্য/সার্ভিস যোগ হয়েছে");
            } else if (status == "unavailable") {
              alert("আপনার কোনো স্টোর নেই");
            }
          });
        })
        .catch((error) => {
          alert("কোনো একটি সমস্যা হয়েছে, আবার চেষ্টা করুন।");
        });
    });
  });
</script>

<section>
  <div class="container h-100 d-flex justify-content-center align-items-center">
    <div class="col-md-6">
      <h1 class="text-center mb-4">Add Your Product</h1>
      <form id="addProductForm" enctype="multipart/form-data">
        <div class="form-group">
          <label for="productName">পণ্য/সার্ভিসের নাম লিখুনঃ</label>
          <input
            type="text"
            class="form-control"
            id="productName"
            name="offering_name"
            required
          />
        </div>
        <div class="form-group">
          <label for="productDescription">পণ্য/সার্ভিসের নাম বর্ণনা দিনঃ</label>
          <textarea
            class="form-control"
            id="productDescription"
            name="offering_description"
            rows="3"
            required
          />
        </div>

        <div class="form-group">
          <label for="productPrice">পণ্য ব সার্ভিসের দাম লিখুনঃ</label>
          <input
            type="number"
            class="form-control"
            id="productPrice"
            name="productPrice"
            min="0"
            required
          />
        </div>

        <div class="form-group">
          <label for="productImage">পণ্য বা সার্ভিসের ছবি দিনঃ</label>
          <input
            type="file"
            class="form-control-file"
            id="productImage"
            name="offering_image"
            required
          />
        </div>

        <div class="form-group">
          <input
            type="hidden"
            class="form-control-file"
            id="productImage"
            name="offering_image_url"
            value={filename}
          />
          <input
            type="hidden"
            class="form-control-file"
            id="productImage"
            name="user_token"
            value={userToken}
          />
        </div>

        <button type="submit" class="btn btn-success rounded-pill"
          >পণ্য যোগ করুন</button
        >
      </form>
    </div>
  </div>
</section>

<style>
  #addProductForm .form-group {
    margin-bottom: 20px;
  }

  #addProductForm .btn {
    margin-top: 40px;
    width: 100%;
  }

  .container {
    width: 100%;
    height: 100%;
  }
</style>

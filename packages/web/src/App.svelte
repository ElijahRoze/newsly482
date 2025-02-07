<script lang="ts">

  let txtUsername: HTMLInputElement = null;
  let txtPassword: HTMLInputElement = null;
  let errorMsg: string = '';
  let successMsg: string = '';

  function doSubmit(username: HTMLInputElement, password: HTMLInputElement) {
    console.log(username.value, password.value);
    const loginUri = "/api/users/login";
    fetch(loginUri, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        
      },
      body: JSON.stringify({
        username: txtUsername.value,
        password: txtPassword.value
      })
    }).then((resp) => {
      errorMsg = '';
      successMsg = '';

      if (resp.status === 200) {
        successMsg = "Logged in!";
      } else {
        resp.json().then((error) => {
          errorMsg = error.detail;
        })
      }
    });

    
  }

</script>

<main>
  <div>
    <div class="login-form">
      <h1>Newsly Login</h1>
      <p class="error">
        {errorMsg}
      </p>
      <p class="success">
        {successMsg}
      </p>
      <div class="form">
        <label for="username">
          <b>Username</b>
          <input type="text" bind:this={txtUsername} name="username" />
        </label>
      
        <label for="password">
          <b>Username</b>
          <input type="password" bind:this={txtPassword} name="password" />
        </label>
      
        <button on:click={doSubmit.bind(this, txtUsername, txtPassword)}>
          Login
        </button>
      </div>
    </div>
  </div>
</main>

<style>
  .login-form .form {
    display: flex;
    flex-direction: column;
  }

  .success {
    color: lime;
    font-size: 18px;
  }

  .error {
    font-size: 18px;
    color: red;
  }

  .form label {
    padding: 10px 0;
  }

  input {
    padding: 4px;
    font-size: 16px;
  }

  button {
    margin-top: 20px;
    padding: 10px;
  }
</style>

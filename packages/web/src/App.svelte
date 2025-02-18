<script lang="ts">
  import ArticleDashboard from "./components/ArticleDashboard.svelte";
  import Content from "./components/Content.svelte";
  import Header from "./components/Header.svelte";
  import { UserStore } from "./store";

  let loggedIn = false;
  let txtUsername: HTMLInputElement | null = null;
  let txtPassword: HTMLInputElement | null = null;
  let errorMsg: string = '';

  UserStore.subscribe((user) => {
    if (user) {
      loggedIn = user.loggedIn;
    } else {
      loggedIn = false;
    }
  })

  // This function will submit the username and password to the API so we can see
  // if they are a valid user.
  function doSubmit(username: HTMLInputElement, password: HTMLInputElement) {   

    // Call the API and pass in the username and password as parameters
    // Then handle the response accordingly.
    fetch("/api/users/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        
      },
      body: JSON.stringify({
        username: txtUsername?.value,
        password: txtPassword?.value
      })
    }).then((resp) => {
      errorMsg = '';

      // If the response is 200 (a success code) then 
      // update the cache to say this user is logged in and valid.
      // Updating the cache will redirect the page to the main experience.
      if (resp.status === 200) {
        const userContext = {
          "username": txtUsername?.value,
          "loggedIn": true,
        }
        UserStore.set(userContext);
        localStorage.setItem('context', JSON.stringify(userContext));
        loggedIn = true;
      } else {
        // If there was an error, show the error message to the user.
        resp.json().then((error) => {
          errorMsg = error.detail;
        })
      }
    });

    
  }

</script>

<main>
  {#if loggedIn}
    <Content>
      <Header />
      <ArticleDashboard />

    </Content>
  {:else}
    <div class="login-page">
      <div class="login-form">
        <h1>Newsly Login</h1>
        <p class="error">
          {errorMsg}
        </p>
        <div class="form">
          <label for="username">
            <b>Username</b>
            <input type="text" bind:this={txtUsername} name="username" />
          </label>
        
          <label for="password">
            <b>Password</b>
            <input type="password" bind:this={txtPassword} name="password" />
          </label>
        
          <button on:click={doSubmit.bind(this, txtUsername, txtPassword)}>
            Login
          </button>
        </div>
      </div>
    </div>
  {/if}
</main>

<style>
  .login-form .form {
    display: flex;
    flex-direction: column;
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
  .login-page {
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .login-page h1 {
    color: var(--uw);
    padding: 20px 0;
  }
</style>

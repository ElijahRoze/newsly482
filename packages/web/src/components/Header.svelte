<script lang="ts">
    import { UserStore, type UserStoreProps } from "../store";

    let activeUser: UserStoreProps | undefined = undefined;

    // Listen to changes to the User "Store". This happens when a user logs in.
    // And when the user store changes, update who is logged in.
    UserStore.subscribe((user) => {
        if (user) {
            activeUser = user;
        }
    });

    // The logout function will clear the cache and reload the page.
    function logout() {
        localStorage.clear();
        UserStore.set({
            loggedIn: false
        });
    }
</script>

<div class="header">
    <span class="header-sticky">
        Welcome, {activeUser?.username}!
    </span>
    <span class="log-out">
        <button on:click={logout}>Log Out</button>
    </span>
</div>

<style>
    .header {
        width: 100%;
        flex-grow: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: var(--uw);
        color: white;
        position: sticky;
        top: 0;
        font-weight: bold;
        font-size: 18px;
        padding: 8px 8px;
    }

    .header-sticky {
        flex-grow: 1;
    }

    .log-out {
        border: 2px solid black;
    }

</style>
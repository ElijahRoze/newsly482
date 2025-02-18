import { writable } from "svelte/store";

// This is what a logged in user looks like.
// And all the information we need about them.
export type UserStoreProps = {
  username?: string;
  loggedIn: boolean;
};

// This is the local cache of the user who is logged in.
export const UserStore = writable<UserStoreProps>({
  loggedIn: false,
});

try {
  // This will try to load the user from the browser cache, instead of making them login.
  // @ts-ignore because it is valid javascript
  UserStore.set(JSON.parse(localStorage.getItem("context")));
} catch (ex) {}

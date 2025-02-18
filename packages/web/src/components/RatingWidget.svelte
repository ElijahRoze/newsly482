<script lang="ts">
    import Fa from 'svelte-fa'
    import { faThumbsUp, faThumbsDown } from '@fortawesome/free-solid-svg-icons/index'
    export let onThumbsUp;
    export let onThumbsDown;
</script>

<div class="rating-container">
    <div class="rating-widget">
        <div on:click={onThumbsUp}>
            <Fa class="rating-element" icon={faThumbsUp} />
        </div>
        <div on:click={onThumbsDown}>
            <Fa class="rating-element" icon={faThumbsDown} />
        </div>
    </div>
</div>

<style>
    .rating-container {
        width: 100%;
        display: flex;
        justify-content: center;
        font-size: 28px;
        background-color: var(--uw);
        color: white;
        padding: 20px;
    }

    .rating-widget {
        width: 200px;
        display: flex;
        justify-content: space-between;
    }

    :global(.rating-element:hover) {
        color: var(--uw-dark);
        cursor: pointer;
    }
</style>
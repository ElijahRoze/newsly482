<script lang="ts">
    export let title;
    export let url;
    export let score;
</script>


<div class="article">
    <div class="title">
        <div>{title}</div>
        <div class="url">{url}</div>
    </div>
    <iframe src={url} />
</div>

<style>
    .article {
        height: 100%;
    }


    .title {
        background-color: var(--uw-dark);
        color: white;
        font-size: 24px;
        padding: 10px;
    }

    .url {
        font-size: 18px;
        color: #ccc;
    }

    iframe {
        width: 100%;
        height: 100%;
    }
</style>
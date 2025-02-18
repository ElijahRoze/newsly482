<script>
    export let title;
    export let url;
    export let score;
</script>

<a href={url} data-bad={score <= .8}>[{Math.round(score*100)/100}] {title}</a>
<style>
    a {
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        font-size: 20px;
        padding: 8px;
    }

    a[data-bad='true'] {
        opacity: .2;
    }
</style>
<script lang="ts">
    import ArticleViewer from "./ArticleViewer.svelte";
    import RatingWidget from "./RatingWidget.svelte";

    // Define the fields an RSS feed article has
    type Article = {
        title: string;
        url: string;
        score: number;
    }

    // Some initial variables
    let articles: Article[] = [];
    let activeArticle: Article;
    let articleIdx = 0;

    // Fetch all the articles we have generated for this user
    fetch("/api/articles").then((resp) => resp.json()).then((links) => {
        articles = [...links];
        activeArticle = articles[0];
        articleIdx = 0;
    });

    // Write a function to progress to the next article
    function next() {
        articleIdx++;
        if (articleIdx >= articles.length) {
            // Do nothing
        } else {
            activeArticle = articles[articleIdx];
        }
    }

    // TODO: Record that the user liked this article in the database
    // but for now, just go to the next article.
    function thumbsUp() {
        next();
    }

    // TODO: Record that the user disliked this article in the database
    // but for now, just go to the next article.
    function thumbsDown() {
        next();
    }

</script>

<div class="article-container">
    {#if activeArticle !== undefined}    
        <ArticleViewer title={activeArticle.title} url={activeArticle.url} score={activeArticle.score} />
    {/if}
    <RatingWidget onThumbsUp={thumbsUp} onThumbsDown={thumbsDown} />
</div>

<style>
    .article-container {
        display: flex;
        flex-direction: column;
        height: 100%;
        flex-grow: 1;
    }
</style>
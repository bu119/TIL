<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{ name: 'create' }">게시글 작성</router-link>
    <hr>
    <ArticleItem
      v-for = "article in articles"
      :key=article.div
      :article="article"
    />
  </div>
</template>

<script>
import ArticleItem from '@/components/ArticleItem'

export default {
  name: 'IndexView',
  computed: {
    articles(){
      return this.$store.state.articles
    }
  },
  components: {
    ArticleItem
  }
}
</script>

<style>

</style>
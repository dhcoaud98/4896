<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg sticky-top" style="background-color: #4C0070;">
      <div class="container-fluid">
        <a class="navbar-brand" href="http://localhost:8080/"><img src="@/assets/video.png" alt="logo" width="30" height="24"></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon mb-0 mt-2" style="color: #E9A6A6;">▼</span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-0 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'movies' }" style="color: #E9A6A6;" onclock="">Movies</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="color: #E9A6A6;">
                Recomend
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'popular' }" style="color: #E9A6A6;">popularMovies</router-link>
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'timeMovie' }" style="color: #E9A6A6;">nowTimeMovie</router-link>
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'shortMovie' }" style="color: #E9A6A6;">shortMovie</router-link>
                <router-link class="nav-link active" aria-current="page" :to="{ name: 'longMovie' }" style="color: #E9A6A6;">longMovie</router-link>
              </ul>
            </li>
            <li class="nav-item">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'information' }" style="color: #E9A6A6;">4896.info</router-link>
            </li>
          </ul>
          <ul class="navbar-nav">
            <li class="nav-item">
              <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-sm" type="submit" style="color: #E9A6A6;" >Search</button>
              </form>
            </li>
            <!-- 로그인이 안되어 있으면 -->
            <li v-if="!isLoggedIn">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'login' }" style="color: #E9A6A6;" onclock="">Login</router-link>
            </li>
            <li v-if="!isLoggedIn">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'signup' }" style="color: #E9A6A6;" onclock="">Signup</router-link>
            </li>

            <!-- 로그인 했다면? -->
            <li v-if="isLoggedIn">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'logout' }" style="color: #E9A6A6;" onclock="">Logout</router-link>
            </li>
            <li v-if="isLoggedIn">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'articles' }" style="color: #E9A6A6;" onclock="">article</router-link>
            </li>
            <li v-if="isLoggedIn">
              <router-link class="nav-link active" aria-current="page" :to="{ name: 'profile', params: { username } }" style="color: #E9A6A6;">profile</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style></style>

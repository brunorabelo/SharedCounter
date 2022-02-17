<template>
  <main>
    <div v-if="loading">
      <PageLoading />
    </div>
    <div v-else>
      <div></div>
    </div>
  </main>
</template>
<script>
import PageLoading from "@/components/PageLoading.vue";
import Room from "@/components/Room.vue";
import api from "@/components/api";

export default {
  components: {
    PageLoading,
    Room,
  },
  data() {
    return {
      modalActive: false,
      username: "",
      roomName: "",
      loading: false,
      wsLink: "",
    };
  },
  methods: {
    fetchRoomInfo() {
      api
        .getRoomInfo(this.roomName)
        .then((result) => {
          console.log(result);
          return result.data;
        })
        .then((data) => {
          this.wsLink = data.result.ws_link;
          this.loading = false;
          console.log(this.wsLink);
        })
        .catch();
    },
  },
  mounted() {
    this.loading = true;
    this.roomName = this.$route.params.roomName;
    this.username = localStorage.username;

    this.fetchRoomInfo();
  },
};
</script>

<style>
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid white;
  border-color: #000 transparent #fff transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>

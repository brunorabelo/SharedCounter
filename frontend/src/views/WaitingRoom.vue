<template>
  <div class="about">
    <div id="register" class="container mt-6 pt-6">
      <div class="columns is-centered">
        <div class="column is-half">
          <div class="card">
            <div class="card-content">
              <p class="title has-text-centered">SHARED COUNTER</p>
              <div class="box">
                <div class="field">
                  <label class="label">Room code</label>
                  <div class="control">
                    <input
                      class="input"
                      v-model="roomName"
                      type="name"
                      placeholder="ABC123"
                      @keyup.enter="enterRoomClick()"
                    />
                  </div>
                </div>
                <button class="button is-primary" v-on:click="enterRoomClick()">
                  Enter room
                </button>
                <br />
                <br />
                <button
                  class="button is-secondary"
                  v-on:click="createRoomClick()"
                >
                  Create room
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="modal"
      :class="{ 'is-active': modalActive }"
      id="username-modal"
    >
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">
            {{ action === 1 ? "Creating room" : "Entering in room " }}
            {{ roomName }}
          </p>
          <button
            class="delete"
            aria-label="close"
            v-on:click="closeModal()"
          ></button>
        </header>
        <section class="modal-card-body">
          <div class="box">
            <div class="field">
              <label class="label">Username</label>
              <div class="control">
                <input
                  class="input"
                  type="name"
                  placeholder="Joao"
                  v-model="username"
                  @keyup.enter="go"
                />
              </div>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button
            class="button is-success"
            :class="{ 'is-loading': loading }"
            id="save_btn"
            v-on:click="go()"
          >
            Save
          </button>
          <button class="button" v-on:click="closeModal()">Cancel</button>
        </footer>
      </div>
    </div>
  </div>
</template>


<script>
export const CREATE_ACTION = 1;
export const ENTER_ACTION = 2;

import api from "@/services/api";

export default {
  data() {
    return {
      modalActive: false,
      username: localStorage.username || "",
      action: -1,
      roomName: "",
      loading: false,
    };
  },
  mounted() {
    const paramsRoomName = this.$route.params.roomName;
    if (paramsRoomName) {
      this.roomName = paramsRoomName;
      this.enterRoomClick();
    }
  },
  methods: {
    showModal() {
      this.modalActive = true;
    },
    closeModal() {
      this.modalActive = false;
    },
    enterRoomClick() {
      this.action = ENTER_ACTION;
      this.showModal();
    },
    createRoomClick() {
      this.action = CREATE_ACTION;
      this.showModal();
    },
    enterRoom() {
      this.$router.push({
        name: "room",
        params: {
          roomName: this.roomName,
        },
      });
    },
    saveUsername() {
      localStorage.username = this.username;
    },
    async go() {
      this.loading = true;
      this.saveUsername();
      if (this.action === CREATE_ACTION) {
        //create new room and calls enterRoom
        api
          .createRoom()
          .then((result) => {
            return result.data;
          })
          .then((data) => {
            console.log(data);
            var result = data.result;
            this.roomName = result.room_name;
            this.enterRoom();
          })
          .catch((error) => {
            console.log("Erro");
          });
      } else {
        this.enterRoom();
      }
    },
  },
};
</script>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

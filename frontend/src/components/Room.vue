<template>
  <div>
    <div class="status" :class="{ connected: 'connected' }">
      {{ connected ? "Connected" : "Disconnected" }}
    </div>

    <div v-if="connected" id="register" class="container mt-6 pt-6">
      <div class="columns is-centered">
        <div class="column"></div>
        <div class="column is-half">
          <div class="card">
            <div class="card-content">
              <p class="title has-text-centered">Room: {{ roomName }}</p>
              <p class="subtitle">User: {{ username }}</p>
              <div class="box">
                <div class="field">
                  <log-viewer :messages="logMessage" />
                  <br />
                  <p class="title has-text-centered">
                    Counter: <span id="count-total">{{ count }}</span>
                  </p>
                </div>
                <br />
                <inc-counter :count="count" @inc-event="incCounter()" />
              </div>
            </div>
          </div>
        </div>
        <div class="column">
          <div class="content">
            <p class="title">User list</p>

            <ul>
              <li :key="idx" v-for="(user, idx) in activeUsers">
                {{ user[0] }}
              </li>
            </ul>
          </div>
          <hr />
          <div class="content">
            <p class="title">Sharing</p>
            <p class="subtitle">Link:</p>
            <button class="button" @click="share()">
              <i class="far fa-share-square"></i>
            </button>
          </div>

          <div class="content">
            <p class="subtitle">QR Code</p>
            <qrcode-vue :value="getUrlToShare()" level="H" size="200" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import IncCounter from "./IncCounter.vue";
import LogViewer from "./LogViewer.vue";
import QrcodeVue from "qrcode.vue";
export default {
  components: { LogViewer, IncCounter, QrcodeVue },
  props: {
    wsLink: { type: String, default: "" },
    username: { type: String, default: "" },
    roomName: { type: String, default: "" },
    initialCount: { type: Number, default: 0 },
  },
  data() {
    return {
      connection: null,
      logMessage: "",
      usersList: [],
      connected: false,
      count: this.initialCount,
    };
  },
  computed: {
    activeUsers() {
      return this.usersList.filter((x) => {
        return x[1];
      });
    },
  },
  created() {
    console.log(this.wsLink);
    if (this.wsLink) this.connectWs();
  },
  methods: {
    incCounter() {
      const data = {
        event: "count.inc",
        total: this.count,
      };
      console.log(data);
      this.connection.send(JSON.stringify(data));
    },

    connectWs() {
      console.log("Starting connection to WebSocket Server");
      console.log(this.wsLink);
      this.connection = new WebSocket(this.wsLink);

      this.connection.onopen = this.onOpen;
      this.connection.onmessage = this.onMessage;
      this.connection.onclose = this.onClose;
      this.connection.onerror = this.onError;
    },

    onOpen(e) {
      this.connected = true;
      console.log(e);
      const data = {
        event: "user.joined",
        username: this.username,
      };
      console.log(data);
      this.connection.send(JSON.stringify(data));
    },

    onMessage(e) {
      const data = JSON.parse(e.data);
      console.log(data);
      const event = data["event"];
      if (event === "count.inc") {
        const total = data.counter_total;
        this.log(total);
        this.count = total;
      } else if (event === "user.joined") {
        this.log(data.username + " entrou");
      } else if (event === "users.list") {
        this.usersList = data.users;
      }
    },
    onClose(e) {
      this.connected = false;
      console.log(
        "Socket is closed. Reconnect will be attempted in 1 second.",
        e.reason
      );
      setTimeout(function () {
        this.connectWs();
      }, 1000);
    },
    onError(err) {
      console.error(
        "Socket encountered error: ",
        err.message,
        "Closing socket"
      );
      this.connection.close();

      this.connected = false;
      setTimeout(function () {
        this.connect();
      }, 1000);
    },
    log(message) {
      this.logMessage += message + "\n";
    },
    getUrlToShare() {
      const urlShare = this.$router.resolve({
        name: "enter-room",
        params: { roomName: this.roomName },
      });
      const absoluteURL = new URL(urlShare.href, window.location.href).href;
      return absoluteURL;
    },
    share() {
      urlShare = this.getUrlToShare();
      console.log(absoluteURL);
      debugger;
      if (navigator.share) {
        navigator
          .share({
            title: "Shared Counter",
            text: "Help me to count",
            url: urlShare,
          })
          .then(() => console.log("Successful share"))
          .catch((error) => console.log("Error sharing", error));
      } else {
        console.log("Share not supported on this browser, do it the old way.");
      }
    },
    qrCode() {
      new QRCode(document.getElementById("qrcode"), this.getUrlToShare());
    },
  },
  unmounted() {
    this.connection && this.connection.close();
    this.connected = false;
  },
};
</script>

 <style>
* {
  /* Reset browser's padding and margin */
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.status {
  background-color: red;
  text-align: center;
  color: whitesmoke;
}
.connected {
  background-color: #00d1b2;
  text-align: center;
}

.my-button {
  touch-action: manipulation;
  width: 100px;
  height: 100px;
  border: none;
  border-radius: 100px;
  outline: none;
  background: #00d1b2;
  color: white;
  cursor: pointer;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.15);
}
.my-button:hover {
  background: darkblue;
}

/* Rules for using icons as black on a light background. */
.material-icons.md-dark {
  color: hsl(171, 100%, 41%);
}
.material-icons.md-dark.md-inactive {
  color: hsl(171, 100%, 41%);
}
</style>
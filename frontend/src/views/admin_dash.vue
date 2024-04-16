<template>
  <div>

    <!-- dashboard -->
    <div class="dashboard-container">
      <div class="user-info">
        <h2><p>Welcome, {{ email }} [{{ role }}]</p></h2>
      </div>
    </div><hr>



    <h2 id = "stats">Stats at a glance....</h2>

    <div class="admin-container">
  <!-- Admin Stats -->
  <div class="admin-stats-container">
    <div class="admin-stat-card">
      <div v-if="loading" class="loading-message">Loading...</div>
      <div v-else>
        <table class="admin-stat-table">
          <tr>
            <th>Category</th>
            <th>Total</th>
          </tr>
          <tr>
            <td>Total Users</td>
            <td>{{ adminStats.total_users }}</td>
          </tr>
          <tr>
            <td>Total Songs</td>
            <td>{{ adminStats.total_songs }}</td>
          </tr>
          <tr>
            <td>Total Playlists</td>
            <td>{{ adminStats.total_playlists }}</td>
          </tr>
          <tr>
            <td>Total Albums</td>
            <td>{{ adminStats.total_albums }}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>

  <!-- Admin Stats Visualization -->
  <div class="admin-stats-visualization-container">
    <div class="admin-stats-chart">
      <canvas id="admin-stats-chart"></canvas>
    </div>
  </div>
</div>
<br><hr>






<div class="section-container">
  <!-- Users Section -->
  <div class="section">
    <button class="func_button" @click="toggleUsers">Users</button>
    <div class="users" v-if="showUsers && users.length > 0">
      <table>
        <tr>
          <th>Email</th>
          <th>Username</th>
          <th>Active</th>
          <th>Action</th>
        </tr>
        <tr v-for="user in users" :key="user.id">
          <td>{{ user.email }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.active }}</td>
          <td>
            <button v-if="user.active" @click="blacklistUser(user.id)">Blacklist</button>
            <button v-else @click="whitelistUser(user.id)">Whitelist</button>
          </td>
        </tr>
      </table>
    </div>
  </div><hr>

  <!-- Albums Section -->
  <div class="section">
    <button class="func_button" @click="toggleAlbums">Albums</button>
    <div class="albums" v-if="showAlbums && albums.length > 0">
      <table>
        <tr>
          <th>Title</th>
          <th>Release Year</th>
          <th>Action</th>
        </tr>
        <tr v-for="album in albums" :key="album.id">
          <td>{{ album.title }}</td>
          <td>{{ album.release_year }}</td>
          <td>
            <button @click="deleteAlbum(album.id)">Delete</button>
          </td>
        </tr>
      </table>
    </div>
  </div><hr>

  <!-- Playlists Section -->
  <div class="section">
    <button class="func_button" @click="togglePlaylists">Playlists</button>
    <div class="playlists" v-if="showPlaylists && playlists.length > 0">
      <table>
        <tr>
          <th>Title</th>
          <th>Action</th>
        </tr>
        <tr v-for="playlist in playlists" :key="playlist.id">
          <td>{{ playlist.title }}</td>
          <td>
            <button @click="deletePlaylist(playlist.id)">Delete</button>
          </td>
        </tr>
      </table>
    </div>
  </div><hr>

  <!-- Songs Section -->
  <div class="section">
    <button class="func_button" @click="toggleSongs">Songs</button>
    <div class="songs" v-if="showSongs && songs.length > 0">
      <table>
        <tr>
          <th>Title</th>
          <th>Action</th>
        </tr>
        <tr v-for="song in songs" :key="song.id">
          <td>{{ song.title }}</td>
          <td>
            <button v-if="!song.is_flagged" @click="blacklistSong(song.id)">Blacklist</button>
            <button v-else @click="whitelistSong(song.id)">Whitelist</button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</div>




    </div>
  </template>
  
<script>
import axios from 'axios';
import chart from 'chart.js/auto';

export default {
  data() {
    return {
      // loading: true,
      email: '',
      role: '',
      users: [],
      albums: [],
      playlists: [],
      songs: [],
      showUsers: false,
      showAlbums: false,
      showPlaylists: false,
      showSongs: false,
      adminStats: {},
    };
  },

  created() {
    this.fetchAdminStats();
  },

  mounted() {
    this.email = localStorage.getItem('email') || '';
    this.role = localStorage.getItem('role') || '';
  },

  methods: {
    async fetchUsers() {
      try {
        const response = await axios.get('http://localhost:5000/users/users', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        });
        this.users = response.data;
        console.log('fetched all users:', this.users);
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },

    async fetchAlbums() {
      try {
        const response = await axios.get('http://localhost:5000/albums/albums', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        });
        this.albums = response.data;
        
      } catch (error) {
        console.error('Error fetching albums:', error);
      }
    },      

    async fetchPlaylists() {
      try {
        const response = await axios.get('http://localhost:5000/playlists/playlists', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        });
        this.playlists = response.data;
      } catch (error) {
        console.error('Error fetching playlists:', error);
      }
    },

    async fetchSongs() {
      try {
        const response = await axios.get('http://localhost:5000/songs/songs', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        });
        this.songs = response.data;
      } catch (error) {
        console.error('Error fetching songs:', error);
      }
    },

    async fetchAdminStats() {
      try {
        const response = await axios.get('http://localhost:5000/users/users/admin_stats', {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') },
        });
        this.adminStats = response.data;
        this.renderChart();
        console.log('Admin stats:', this.adminStats);
      } catch (error) {   
        console.error('Error fetching admin stats:', error);
      }
    },

    renderChart() {
      const ctx = document.getElementById('admin-stats-chart').getContext('2d');
      new chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Users', 'Songs', 'Playlists', 'Albums'],
          datasets: [{
            label: 'Count',
            data: [
              this.adminStats.total_users,
              this.adminStats.total_songs,
              this.adminStats.total_playlists,
              this.adminStats.total_albums
            ],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
            ],
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    },

    toggleUsers() {
      this.showUsers = !this.showUsers;
      if (this.showUsers && this.users.length === 0) {
        this.fetchUsers();
      }
    },

    toggleAlbums() {
      this.showAlbums = !this.showAlbums;
      if (this.showAlbums && this.albums.length === 0) {
        this.fetchAlbums();
      }
    },

    togglePlaylists() {
      this.showPlaylists = !this.showPlaylists;
      if (this.showPlaylists && this.playlists.length === 0) {
        this.fetchPlaylists();
      }
    },

    toggleSongs() {
      this.showSongs = !this.showSongs;
      if (this.showSongs && this.songs.length === 0) {
        this.fetchSongs();
      }
    },

    async blacklistSong(songId) {
      try {
        const response = await axios.get(`http://localhost:5000/songs/songs/flag_song/${songId}`, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('Song blacklisted successfully:', response.data);
        this.fetchSongs();

      } catch (error) {
        console.error('Error blacklisting song:', error);
      }
    },

    async whitelistSong(songId) {
      try {
        const response = await axios.get(`http://localhost:5000/songs/songs/unflag_song/${songId}`, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('Song whitelisted successfully:', response.data);
        this.fetchSongs();
      } catch (error) {
        console.error('Error whitelisting song:', error);
      }
    },

    async blacklistUser(userId) {
      try {
        const response = await axios.put(`http://localhost:5000/userfn/blacklist`, 
        {
          user_id : this.userId
        },

        {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('User blacklisted successfully:', response.data);
        this.fetchUsers();
      } catch (error) {
        console.error('Error blacklisting user:', error);
      }
    }, 

    async whitelistUser(userId) {
      try {
        const response = await axios.put(`http://localhost:5000/userfn/whitelist`, 
        {
          user_id : this.userId
        },
        {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
        });
        console.log('User whitelisted successfully:', response.data);
        this.fetchUsers();
      } catch (error) {
        console.error('Error whitelisting user:', error);
      }
    },  


    async deleteAlbum(albumId) {
      axios.delete(`http://localhost:5000/albums/albums/${albumId}`, {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the album from the yourAlbums array
        this.albums = this.albums.filter(album => album.id !== albumId);
        console.log('Album deleted successfully.');

        this.fetchAlbums();
        this.fetchAdminStats();
      })
      .catch(error => {
        console.error('Error deleting album:', error);
      });
    },

    async deletePlaylist(playlistId) {
      axios.delete(`http://localhost:5000/playlists/playlists/${playlistId}`, {
        headers: { Authorization: 'Bearer ' + localStorage.getItem('token') }, 
      })
      .then(response => {
        // If the deletion was successful, remove the playlist from the yourPlaylists array
        this.playlists = this.playlists.filter(playlist => playlist.id !== playlistId);
        console.log('Playlist deleted successfully.');
        
        this.fetchPlaylists();
        this.fetchAdminStats();
      })
      .catch(error => {
        console.error('Error deleting playlist:', error);
      });
    },



  },
};
</script>


<style scoped>
#stats[data-v-65deba6f] {
    text-align: center;
    border: 2px solid red;
    width: 60%;
    margin-left:20%;
}


/*--------------------------------------- stats and visuals--------------------------------*/
.admin-container {
  display: flex;
}
.admin-stats-container,
.admin-stats-visualization-container {
  flex: 1;
  margin-right: 20px;
}

.admin-stat-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.admin-stats-chart {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 20px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}



/* ---------------------------------------dashboard-------------------------------------------- */
.dashboard-container {
  text-align: center;
}

.user-info {
  margin-top: 20px;
}

.user-info p {
  font-size: 18px;
  color: #333;
}

/* -----------------------------------------tables ----------------------------------*/
.section {
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
}

th, td {
  padding: 12px;
  text-align: left;
}

th {
  background-color: #4CAF50;
  color: white;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

tr:hover {
  background-color: #ddd;
}

button {
  padding: 8px 12px;
  border: none;
  width:48%;
  border-radius: 4px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 23%;
  cursor: pointer;
  background-color: #555;
  color: white;
}

button:hover {
  background-color: #777;
}

/* Adjust styles for specific sections */
.users th:last-child,
.albums th:last-child,
.playlists th:last-child,
.songs th:last-child {
  text-align: center;
}

.users td:nth-child(3),
.songs td:nth-child(2) {
  text-align: center;
}

.users td:last-child,
.albums td:last-child,
.playlists td:last-child,
.songs td:last-child {
  text-align: center;
}



</style>
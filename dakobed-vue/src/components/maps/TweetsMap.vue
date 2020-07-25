<template>
<v-container>
  <div class="section-box map-search">
     <h4 class="section-box__heading">MAP</h4>

     <gmap-map
      ref="mapRef"
      :center="center"
      :zoom="4"
      style="width: 800px;  height: 500px;"
    >
    <gmap-marker
        :key="index"
        v-for="(marker, index) in markers"
        :position="marker.position"
      ></gmap-marker>
     </gmap-map>
<!-- 
     </gmap-map>
        <gmap-marker
        :key="index"
        v-for="(marker, index) in markers"
        :position="marker.position"
      ></gmap-marker> -->
      <!-- <gmap-marker
        :key="index"
        v-for="(shop, index) in shops"
        :position="shop.position"
      ></gmap-marker> --> 
  </div>
</v-container>
</template>


<script>
export default {
    data() {
      return {
        markers:[{position: { lat: 39, lng: -98 }}],
        center: { lat: 39, lng: -98 },
        boundMap: {},
        shops: [] 
      };
    }
}
</script>
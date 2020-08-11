import React, { Component } from 'react';
import  { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

import{
  GoogleMap,
  useLoadScript,
  Marker, 
  InfoWindow
} from "@react-google-maps/api"

import { formatRelative } from "date-fns"
import mapStyles from "../../mapStyles"
const center = {
  lat: 40,
  lng: -94
}

const options = {
  styles: mapStyles,
  disableDefaultUI:true
}

const mapContainerStyle = {
  width: "100%",
  height: "60vh"
}


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

export default function TweetsMap(){
  const [markers, setMarkers] = React.useState([]);
  const classes = useStyles();
  
  return (<div>
      <h2> Virus Tweets</h2>

      
      <GoogleMap
          mapContainerStyle={mapContainerStyle}
          zoom={4.2}
          center={center}
          options ={options}


          onClick={(event)=>{
            setMarkers(current => [...current, {
              lat: event.latLng.lat(),
              lng: event.latLng.lng(),
              time: new Date()
            }])
            console.log(event)
          }}
        >
        {markers.map(marker => (
          <Marker 
            key = {marker.time.toISOString()}
            position={{lat:marker.lat, lng:marker.lng}}
          />  
        ))}

      </GoogleMap>
  </div>
  );
}




// class TweetsMap extends Component {
//   constructor(){
//     super();
//     this.state = {};
//   }

  
//   render() {
//     return (
//       <div>
      
//         <h2>I am a {this.props.brand}!</h2>
//       </div>
//     );
//   }
// }
//export default TweetsMap; 
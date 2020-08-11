import React from 'react';
import{
  GoogleMap,
  useLoadScript,
  Marker, 
  InfoWindow
} from "@react-google-maps/api"

import { formatRelative } from "date-fns"
import TweetsMap from "./components/map/TweetsMap"
import TweetsList from "./components/TweetsList"
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import {makeStyles} from "@material-ui/core/styles"

import './App.css';

import mapStyles from "./mapStyles"

const useStyles = makeStyles((theme) =>({
  grid:{
    width: '100%',
    margin: '0px'
  },
  paper:{
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    background:  theme.palette.success.light
  }
}))


// const mapContainerStyle = {
//   width: "100vw",
//   height: "100vh"
// }


const options = {
  styles: mapStyles,
  disableDefaultUI:true
}


const libraries = ["places"]

export default function App(){
  const{ isLoaded, loadError} = useLoadScript({
    googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
    libraries: ["places"]
  }) ;


  const [markers, setMarkers] = React.useState([]);
  const classes = useStyles();
  if(loadError) return "Error loading maps";
    if(!isLoaded) return "Loading Maps";

  return( <div>
    <Grid container spacing={2} className={classes.grid}>
      <Grid item xs={12} md={8} style={{position: 'relative', height: '50vh'}}>
      <Paper className={classes.paper}  style={{position: 'relative', height: '70vh'}} >

          <TweetsMap brand="Ford"> </TweetsMap>
        </Paper>

      </Grid>
      <Grid item xs={12} md={4}>
        <Paper className={classes.paper}>

          <TweetsList></TweetsList>
        </Paper>
      </Grid>

    </Grid>

      {/* <Grid container spacing={3}>
        <Grid item sm={12} style={{position: 'relative', height: '50vh'}}>
          <TweetsMap> </TweetsMap>
        
        </Grid>
        <Grid item xs={12} sm={5}>
        </Grid>
      </Grid> */}

    {/* <TweetsMap> </TweetsMap> */}

    </div>);
}

import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Parent from './components/parentToChild/parent'
class App extends Component {
  state ={
    title: 'placeholder title'
  }
  changeTheWorld = (newTitle) => {
    this.setState({title:newTitle});
  }
  keepTheWorldTheSame = (newTitle) => {
    this.setState({title:newTitle})
  }
  render(){
    return (
      <div className="App">
        <Parent 
        keepWorldSameEvent={this.keepTheWorldTheSame.bind(this,'same world')}
        changeTheWorldEvent={this.changeTheWorld.bind(this, 'new world')}
        title={this.state.title} />
      </div>
    );
  }

}

export default App;

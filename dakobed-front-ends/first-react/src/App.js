import React, {Component} from 'react';
import Todos from "./components/Todos"
import Header from './components/layout/Header';
import AddTodo from './components/AddTodo'
import { BrowserRouter as Router, Route } from 'react-router-dom';
import About from './components/pages/About';
import { Button, Typography } from '@material-ui/core';


import './App.css';

class App extends Component {
  state ={
    todos:[
      {
        id:1,
        title: "Take out the trash",
        completed:false
      },
      {
        id:2,
        title: "Get a job",
        completed:false
      },
      {
        id:3,
        title: "Be successfull",
        completed:false
      }
    ]
  }
  
  
  render(){
    console.log(this.state.todos)
    return (
      <Router>
        <div className="App">
          <div className="container">
            <Header />
            <Route
              exact
              path="/"
              render={props => (
                <React.Fragment>
                  <AddTodo addTodo={this.addTodo} />
                  <Todos
                    todos={this.state.todos}
                    markComplete={this.markComplete}
                    delTodo={this.delTodo}
                  />
                </React.Fragment>
              )}
            />
            <Route path="/about" component={About} />
          </div>
        </div>
      
        <Button disabled> First Button</Button>
      </Router>

      

    );
  }
}

export default App;

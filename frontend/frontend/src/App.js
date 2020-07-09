import React from 'react';
import { Switch, Route, Redirect, withRouter, BrowserRouter } from 'react-router-dom'
import './app.css'
import Home from './components/HomeComponent'
import Header from './components/Header'
function App() {
  return (
    <div>
      <Header />
      <BrowserRouter>
        <Switch>
          <Route path='/home' component={() => <Home />} />
          <Redirect to="/home" />
        </Switch>
      </BrowserRouter>
      {/* <Footer/> */}
    </div>
  );
}

export default App;

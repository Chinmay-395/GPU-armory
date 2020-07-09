import React from 'react';
import { Switch, Route, Redirect, withRouter, BrowserRouter } from 'react-router-dom'

import Home from './components/HomeComponent'
function App() {
  return (
    <div>
      {/* <Header/> */}
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

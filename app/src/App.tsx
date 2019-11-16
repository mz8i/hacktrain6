import React from 'react';
import Route from 'react-router-dom/Route';
import Switch from 'react-router-dom/Switch';

// import 'bootstrap/dist/css/bootstrap.min.css';
import 'semantic-ui-css/semantic.min.css';
import './App.css';

import { MapPage } from './map/MapPage';
import Home from './pages/Home';

const App = () => (
  <Switch>
    <Route exact path="/" component={Home} />
    <Route exact path="/map" component={MapPage} />
  </Switch>
);

export default App;

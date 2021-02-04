import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from './Home';
function App() {
  return (
    <div className="App">
      <header>
        <p>header</p>
      </header>
      <Router>
          <Route exact path='/' component={Home}/>
          
      </Router>
      
    </div>
    
  );
}

export default App;

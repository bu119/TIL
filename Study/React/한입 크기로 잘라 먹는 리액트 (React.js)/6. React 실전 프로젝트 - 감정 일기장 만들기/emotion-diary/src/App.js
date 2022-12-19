import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './pages/Home'
import New from './pages/New'
import Edit from './pages/Edit'
import Diary from './pages/Diary'

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <h2>App.js</h2>
        {/* process.env.PUBLIC_URL : public 위치 */}
        {/* <img src={process.env.PUBLIC_URL + `/assets/emotion1.png`} /> */}
   

        <Routes>
          <Route path='/' element={<Home/>}/>
          <Route path='/new' element={<New/>}/>
          <Route path='/edit' element={<Edit/>}/>
          {/* <Route path='/diary/' element={<Diary/>}/> */}
          <Route path='/diary/:id' element={<Diary/>}/>
        </Routes>

      </div>
    </BrowserRouter>
  );
}

export default App;

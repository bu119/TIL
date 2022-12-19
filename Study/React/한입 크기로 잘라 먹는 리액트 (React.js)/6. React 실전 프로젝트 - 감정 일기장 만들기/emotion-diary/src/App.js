import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Home from './pages/Home'
import New from './pages/New'
import Edit from './pages/Edit'
import Diary from './pages/Diary'

// COMPONENTS
import MyButton from './components/MyButton';



function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <h2>App.js</h2>
        {/* process.env.PUBLIC_URL : public 위치 */}
        {/* <img src={process.env.PUBLIC_URL + `/assets/emotion1.png`} /> */}
        
        <MyButton
          text={"버튼"}
          onClick={()=> alert("버튼 클릭")}
          type={"positive"}
        />
        <MyButton
          text={"버튼"}
          onClick={()=> alert("버튼 클릭")}
          type={"negative"}
        />
        <MyButton
          text={"버튼"}
          onClick={()=> alert("버튼 클릭")}
        />

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

import React,{useState} from 'react';
import OddEvenResult from './OddEvenResult';


const Counter = ({initialValue}) => {
    const [count, setCount] = useState(initialValue);

    const onIncrease = () => {
        setCount(count + 1);
    }

    const onDecrease = () => {
        setCount(count - 1);
    }

    return (
        <div>
          <h2>{count}</h2>
          <button onClick={onIncrease}>+</button>
          <button onClick={onDecrease}>-</button>
          <OddEvenResult count={count}/>
      </div>
    );
};

// 만약 부모 컴포넌트에서 빈 값을 보내면? default 값으로 0을 설정
Counter.defaultProps = {
    initialValue: 0,
};

export default Counter;
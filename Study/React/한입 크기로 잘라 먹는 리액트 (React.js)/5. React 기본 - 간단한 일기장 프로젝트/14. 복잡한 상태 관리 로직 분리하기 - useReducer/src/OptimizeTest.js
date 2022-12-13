import React, { useEffect, useState } from "react";

// React.memo 를 이용하여 컴포넌트를 메모화해서 재사용
const CounterA = React.memo(({ count }) => {
  useEffect(() => {
    console.log(`CounterA Update - count : ${count}`);
  });
  return <div>{count}</div>;
});

const CounterB = React.memo(({ obj }) => {
  useEffect(() => {
    console.log(`CounterB Update - count : ${obj.count}`);
  });
  return <div>{obj.count}</div>;
});

const areEqual = (prevProps, nextProps) => {
  if (prevProps.obj.count === nextProps.obj.count) {
    return true;  // 이전 프롭스와 현재 프롭스가 같다. -> 리덴더링을 일으키지 않게된다.
  }
  return false;   // 이전 프롭스와 현재 프롭스가 다르다. -> 리덴더링을 일으킨다.
};

const MemoizedCounterB = React.memo(CounterB, areEqual);

const OptimizeTest = () => {
  const [count, setCount] = useState(1);
  const [obj, setObj] = useState({
    count: 1
  });

  return (
    <div style={{ padding: 50 }}>
      <div>
        <h2>Counter A</h2>
        <CounterA count={count} />
        <button onClick={() => setCount(count)}>A Button</button>
      </div>
      <div>
        <h2>Counter B</h2>
        <MemoizedCounterB obj={obj} />
        <button onClick={() => setObj({ count: 1 })}>B Button</button>
      </div>
    </div>
  );
};

export default OptimizeTest;

import React, { useEffect, useState } from "react";

// LifeCycle 제어 알아보기

const UnMountTest = () => {
  useEffect(() => {
    // Mount 시점에 실행된다.
    console.log("Sub Component Mount!");
    return () => {
      // Unmount 시점에 실행된다.
      console.log("Sub Component Unmount!");
    };
  }, []);
  return <div>Unmount Testing Component</div>;
};

const LifeCycle = () => {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");

  const [isVisible, setIsVisible] = useState(false);
  const toggle = () => setIsVisible(!isVisible);

  useEffect(() => {
    console.log("Mount!");
  }, []);

  useEffect(() => {
    console.log("Update!");
  });

  useEffect(() => {
    console.log(`count is update : ${count}`);
    if (count > 5) {
      alert("count가 5를 넘었습니다. 따라서 1로 초기화합니다.")
      setCount(1)
    }
  }, [count]);

  useEffect(() => {
    console.log(`text is update : ${text}`);
  }, [text]);

  return (
    <div>
      <div>
        {count}
        <button onClick={() => setCount(count + 1)}>count up</button>
      </div>
      <div>
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>
      <button onClick={toggle}>ON/OFF BUTTON</button>
      {isVisible && <UnMountTest />}
    </div>
    // 단락회로평가
    // isVisible 값이 true면 <UnMountTest /> 값에 따라 달라지므로 <UnMountTest /> 값이 반환되서 화면에 렌더링 된다.
    // isVisible 값이 false면 <UnMountTest /> 값과 관계없이 렌더링되지 않는다.
  );
};

export default LifeCycle;

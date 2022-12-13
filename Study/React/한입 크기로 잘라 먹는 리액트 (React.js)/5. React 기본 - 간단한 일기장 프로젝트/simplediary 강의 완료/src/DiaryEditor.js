import React, { useContext, useRef, useState } from "react";
import { DiaryDispatchContext } from "./App";

const DiaryEditor = () => {

  const { onCreate } = useContext(DiaryDispatchContext);

  const authorInput = useRef();
  const contentInput = useRef();

  // state에 author와 content의 state를 하나로 묶는다.
  const [state, setState] = useState({
    author: "",
    content: "",
    emotion: 1,
    
  });

  // author, content 이벤트핸들러 합치기
  const handleChangeState = (e) => {
    setState({
      // state의 객체가 길면 spread 연산자를 사용한다.
      // 변경하고자하는 값을 spread 연산자 밑에 쓴다.
      // 반대로하면 원래 값이 새로운 값을 덮어쓰게 된다.
      ...state,
      [e.target.name]: e.target.value
      // author : 바뀐값
      // content : 바뀐값
    });
  };

  const handleSubmit = () => {
    if (state.author.length < 1) {
      // alert("작성자는 최소 1글자 이상 입력해주세요.")
      // focus
      authorInput.current.focus();
      return;
    }

    if (state.content.length < 5) {
      // alert("일기 본문은 최소 5글자 이상 입력해주세요.")
      // focus
      contentInput.current.focus();
      return;
    }
    // 3. 일기가 저장될 때 onCreate 함수를 호출하여 작성된 폼을 App 컴포넌트의 onCreate에 전달한다.
    onCreate(state.author, state.content, state.emotion)
    // console.log(state);
    alert("저장 성공!");
    // 일기가 작성되면 일기 작성 폼의 데이터를 초기화
    setState({
      author: "",
      content: "",
      emotion: 1
    });
  };


  return (
    <div className="DiaryEditor">
      <h2>오늘의 일기</h2>
      <div>
        <input
          ref={authorInput}
          name="author"
          value={state.author}
          onChange={handleChangeState}
        />
      </div>
      <div>
        <textarea 
          ref={contentInput}
          name="content"
          value={state.content}
          onChange={handleChangeState}
        />
      </div>
      <div>
        <span>오늘의 감정점수 : </span>
          <select
            name="emotion"
            value={state.emotion}
            onChange={handleChangeState}
          >
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
          <option value={5}>5</option>
        </select>
      </div>
      <div>
        <button onClick={handleSubmit}>일기 저장하기</button>
      </div>
    </div>
  );
};
export default React.memo(DiaryEditor);

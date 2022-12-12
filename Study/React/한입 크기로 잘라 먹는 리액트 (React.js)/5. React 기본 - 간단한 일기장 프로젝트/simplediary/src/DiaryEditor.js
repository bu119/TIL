import { useRef, useState } from "react";

const DiaryEditor = () => {

  const authorInput = useRef();
  const contentInput = useRef();

  // state에 author와 content의 state를 하나로 묶는다.
  const [state, setState] = useState({
    author: "",
    content: "",
    emotion: 1,

  });
  // const [author, setAuthor] = useState("");
  // const [content, setContent] = useState("");

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

    // console.log(state);
    alert("저장 성공!");
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
          // onChange={(e)=>{
          //   // console.log(e.target.value)
          //   // setAuthor(e.target.value)
          //   // 객체를 바꾸려면 객체로 전달
          //   setState({
          //     // state의 객체가 길면 spread 연산자를 사용한다.
          //     // 변경하고자하는 값을 spread 연산자 밑에 쓴다.
          //     // 반대로하면 원래 값이 새로운 값을 덮어쓰게 된다.
          //     ...state,
          //     author: e.target.value,
          //     // content: state.content,
          //   })
          // }}
        />
      </div>
      <div>
        <textarea 
          ref={contentInput}
          name="content"
          value={state.content}
          onChange={handleChangeState}
          // onChange={(e)=>{
          //   // console.log(e.target.value)
          //   // setContent(e.target.value)
          //   setState({
          //     // author: state.author,
          //     ...state,
          //     content: e.target.value,
          //   })
          // }}
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
        <button button onClick={handleSubmit}>일기 저장하기</button>
      </div>
    </div>
  );
};
export default DiaryEditor;

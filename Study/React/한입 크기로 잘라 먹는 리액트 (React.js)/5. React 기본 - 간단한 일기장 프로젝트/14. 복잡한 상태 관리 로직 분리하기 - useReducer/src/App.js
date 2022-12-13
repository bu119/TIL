import React, { useMemo, useEffect, useRef, useCallback, useReducer } from 'react';
import './App.css';
import DiaryEditor from './DiaryEditor';
import DiaryList from './DiaryList';
// import OptimizeTest from './OptimizeTest';
// import LifeCycle from './LifeCycle';

// API 호출 Json 파일
// https://jsonplaceholder.typicode.com/comments

// 임시 더미 데이터
// const dummyList = [
//   {
//     id: 1,
//     author: "이정환",
//     content: "하이 1",
//     emotion: 5,
//     created_date: new Date().getTime()
//   },
//   {
//     id: 2,
//     author: "홍길동",
//     content: "하이 2",
//     emotion: 2,
//     created_date: new Date().getTime()
//   },
//   {
//     id: 3,
//     author: "아무개",
//     content: "하이 3",
//     emotion: 1,
//     created_date: new Date().getTime()
//   }
// ];


const reducer = (state, action) => {
  switch (action.type) {
    case "INIT": {
      return action.data;
      // 새로운 state
    }
    case "CREATE": {
      const created_date = new Date().getTime();
      const newItem = {
        ...action.data,
        created_date
      };
      return [newItem, ...state];
    }
    case "REMOVE": {
      return state.filter((it) => it.id !== action.targetId);
    }
    case "EDIT": {
      return state.map((it) =>
        it.id === action.targetId ?
        { ...it, content: action.newContent } : it
      );
    }
    default:
      return state;
  }
};


function App() {

  // 전체 일기 데이터 관리 State
  // 일기가 없는 상태로 시작 (빈 배열 [])
  // const [data, setData] = useState([])

  // useReducer
  const [data, dispatch] = useReducer(reducer, []);


  // id는 0번 부터 시작
  const dataId = useRef(0)

  // API 호출 (async - 비동기 함수로 바꿈)
  const getData = async() => {
    const res = await fetch(
      'https://jsonplaceholder.typicode.com/comments'
    ).then((res) => res.json())
    
    // console.log(res)
    const initData = res.slice(0, 20).map((it) => {
      return {
        author: it.email,
        content: it.body,
        // API 데이터에 없으므로 1~5 랜덤으로 넣기
        emotion: Math.floor(Math.random() * 5) + 1,
        created_date: new Date().getTime() + 1,
        id: dataId.current++
      };
    });

    dispatch({ type: "INIT", data: initData });

    // setData(initData);
  }

  // 마운트 되자마자 API 호출
  useEffect(() => {
    getData();
  }, []);


  // 4. 새로운 일기 데이터를 setData로 data에 추가
  // const onCreate = useCallback(
  //   (author, content, emotion) => {
  //     const created_date = new Date().getTime();
  //     const newItem = {
  //       author,
  //       content,
  //       emotion,
  //       created_date,
  //       id: dataId.current
  //     };
  //     // 현재 일기 데이터를 추가하고 다음 일기 데이터를 위해 id + 1 해주기
  //     dataId.current += 1;
  //     // ...data 원래 있던 데이터
  //     setData((data) => [newItem, ...data]);
  //   },

  //   [data]
  // );

  const onCreate = useCallback((author, content, emotion) => {
    dispatch({
      type: "CREATE",
      data: { author, content, emotion, id: dataId.current }
    });
    dataId.current += 1;
  }, []);

  // 일기 본문 삭제
  // const onRemove = useCallback((targetId) => {
  //   // console.log(`${targetId}가 삭제되었습니다.`)
  //   setData((data) => data.filter((it) => it.id !== targetId));
  // },[])

  const onRemove = useCallback((targetId) => {
    dispatch({ type: "REMOVE", targetId });
  }, []);

  // 일기 본문 수정
  // const onEdit = useCallback((targetId, newContent) => {
  //   setData((data) =>
  //     data.map((it) =>
  //       it.id === targetId ? { ...it, content: newContent } : it
  //     )
  //   );
  // }, []);

  const onEdit = useCallback((targetId, newContent) => {
    dispatch({
      type: "EDIT",
      targetId,
      newContent
    });
  }, []);

  // 기분 개수 표시
  // Memoization 하고 싶은 함수 useMemo로 감싸기
  // useMemo로 감싸면 getDiaryAnalysis 함수가 함수에서 값으로 변한다.
  // [data.length]가 변화할 때만 리렌더한다.
  const getDiaryAnalysis = useMemo(() => {
    // if (data.length === 0) {
    //   return { goodcount: 0, badCount: 0, goodRatio: 0 };
    // }

    // console.log("일기 분석 시작");

    const goodCount = data.filter((it) => it.emotion >= 3).length;
    const badCount = data.length - goodCount;
    const goodRatio = (goodCount / data.length) * 100;
    return { goodCount, badCount, goodRatio };
  }, [data.length]);

  const { goodCount, badCount, goodRatio } = getDiaryAnalysis;


  return (
    <div className="App">
      {/* <LifeCycle /> */}
      {/* <OptimizeTest /> */}
      <DiaryEditor onCreate={onCreate} />
      <div>전체 일기 : {data.length}</div>
      <div>기분 좋은 일기 개수 : {goodCount}</div>
      <div>기분 나쁜 일기 개수 : {badCount}</div>
      <div>기분 좋은 일기 비율 : {goodRatio}</div>
      <DiaryList onEdit={onEdit} onRemove={onRemove} diaryList={data} />
    </div>
    // DiaryList에는 현재 App 컴포넌트가 가진 일기 배열 데이터의 State를 넘겨준다. 
    // App컴포넌트의 data State가 바뀌면 DiaryList는 리렌더한다.
    // DiaryEditor에 작성한 내용을 저장해 DiaryList에 반영되게 만드려면
    // App 컴포넌트의 data의 상태를 변화시키면 된다.
    // 1. 새로운 일기를 추가하는 onCreate 함수를 생성한다.
    // 2. DiaryEditor에 함수를 props로 넘겨준다,
  );
}

export default App;

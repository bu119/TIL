import DiaryItem from "./DiaryItem";

const DiaryList = ({ onEdit, onRemove, diaryList }) => {
  // console.log(diaryList)
  return (
    <div className="DiaryList">
      <h2>일기 리스트</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {diaryList.map((it) => (
          <DiaryItem key={it.id} {...it} onEdit={onEdit} onRemove={onRemove} />
          // DiaryItem 컴포넌트로 대체
          // key={idx}를 사용할 경우 (배열의 인덱를 사용할 경우) 
          // 데이터를 수정, 추가, 삭제하여 인덱스들의 순서가 바뀔 때 리액트에서 문제가 발생할수있다.
          // 고유한 아이디를 가지고 있다면 고유한 아이디 사용
          // <div key={it.id}>
          //   <div>작성자 : {it.author}</div>
          //   <div>내용 : {it.contentr}</div>
          //   <div>작성자 : {it.emotion}</div>
          //   <div>작성 시간(ms): {it.created_date}</div>
          // </div>
        ))}
      </div>
    </div>
  );
};
// undefined 으로 넘어 오는 값의 기본값을 설정
DiaryList.defaultProps = {
  diaryList: []
};

export default DiaryList;

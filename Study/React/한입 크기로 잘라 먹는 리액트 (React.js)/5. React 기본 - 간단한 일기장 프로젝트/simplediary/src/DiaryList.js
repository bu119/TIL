// import DiaryItem from "./DiaryItem";

const DiaryList = ({ diaryList }) => {
  // console.log(diaryList)
  return (
    <div className="DiaryList">
      <h2>일기 리스트</h2>
      <h4>{diaryList.length}개의 일기가 있습니다.</h4>
      <div>
        {diaryList.map((it) => (
          // key={idx}를 사용할 경우 
          <div key={it.id}>
            <div>작성자 : {it.author}</div>
            <div>내용 : {it.contentr}</div>
            <div>작성자 : {it.emotion}</div>
            <div>작성 시간(ms): {it.created_date}</div>
          </div>
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

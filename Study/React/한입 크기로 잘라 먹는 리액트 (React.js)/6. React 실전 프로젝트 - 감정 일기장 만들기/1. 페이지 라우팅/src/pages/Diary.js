import { useParams } from "react-router-dom"

const Diary = () => {
  // use 키워드 react hooks 에서 많이 쓰임
  // react 가 제공하는 react hooks는 아니지만
  // 라이브러리의 기능을 더 편하게 해주는 사용자 정의 Hook을 커스텀 hooks라고 부른다.
  // useParams를 이용하면 전달받은 Path Variable들을 모아서 객체로 받을 수 있다.
  const {id} = useParams()
  console.log(id)

  return (
    <div>
      <h1>Diary</h1>
      <p>이곳은 일기 상세 페이지 입니다.</p>
    </div>
  )
}

export default Diary
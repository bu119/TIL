import { useNavigate, useSearchParams } from "react-router-dom"

const Edit = () => {
  
  // useNavigate는 페이지를 이동시킬 수 있는 함수를 반환해준다.
  // navigate의 인자로 경로를 작성한다. (ex. 로그인 안한 사람 강제로 로그인 페이지로 보내기)
  // link tag를 클릭안했을 때도 의도적으로 페이지를 바꿀 수 있다.
  const navigate = useNavigate()

  // useSearchParams는 Query String을 처리하는 커스텀 훅이다. 
  // useSearchParams은 배열을 반환한다.
  // setSearchParams는 searchParms를 변경시키는 역할을 한다.
  // Query String은 실시간으로 Query String을 변경시키는 setSearchParams라는 상태 변화 함수도 가진다.
  const [searchParms, setSearchParams] = useSearchParams()

  const id = searchParms.get("id")
  console.log("id : ", id)

  const mode = searchParms.get("mode")
  console.log("mode : ", mode)


  return <div>
    <h1>Edit</h1>
    <p>이곳은 일기 수정 페이지 입니다.</p>
    <button onClick={()=>setSearchParams({who:"bu"})}>
      QS 바꾸기
    </button>
    
    <button onClick={()=>{
      navigate("/home")
    }}>
      Home으로 가기
    </button>
    <button onClick={()=>{
      navigate(-1)
    }}>
      뒤로가기
    </button>
  </div>
}

export default Edit
import { useContext, useEffect, useState } from "react";
import { DiaryStateContext } from "../App";

import MyHeader from "../components/MyHeader";
import MyButton from "../components/MyButton";
import DiaryList from "../components/DiaryList";
import LineChart from "../components/LineChart";

const Home = () => {
  // 일기 리스트
  const diaryList = useContext(DiaryStateContext);

  const [data, setData] = useState([]);

  // 마지막날 저장 (날짜별 차트 보류...)
  // const [CurLastDate, setCurLastDate] = useState('');

  const [curDate, setCurDate] = useState(new Date());
  // console.log(curDate)
  const headText = `${curDate.getFullYear()}년 ${curDate.getMonth() + 1}월`;

  const monthData = curDate.getMonth() + 1

  useEffect(() => {
    // 일기가 없을 때는 할 필요없다.
    if (diaryList.length >= 1) {
      // 달의 첫날 (1일) (년, 월, 일)
      const firstDay = new Date(
        curDate.getFullYear(),
        curDate.getMonth(),
        1
      ).getTime();

      // 달의 마지막 날 (날, 시, 분, 초)
      const lastDay = new Date(
        curDate.getFullYear(),
        curDate.getMonth() + 1,
        0,
        23,
        59,
        59
      ).getTime();

      // 해당 달에 작성된 일기 데이터
      setData(
        diaryList.filter((it) => firstDay <= it.date && it.date <= lastDay)
      );

      // 마지막 월 추가 (날짜별 차트 보류...)
      // const lastDate = new Date(lastDay)
      // console.log(lastDate.getDate())
      // setCurLastDate(lastDate.getDate())

    }
  }, [diaryList, curDate]);

  useEffect(() => {
    // console.log(data);
  }, [data]);

  const increaseMonth = () => {
    setCurDate(
      new Date(curDate.getFullYear(), curDate.getMonth() + 1, curDate.getDate())
    );
  };

  const decreaseMonth = () => {
    setCurDate(
      new Date(curDate.getFullYear(), curDate.getMonth() - 1, curDate.getDate())
    );
  };

  // 달력 선택 추가
  const selectMonth = (date) => {
    const year = date.slice(0, 4)
    const month = date.slice(5, 7)
    setCurDate(new Date(parseInt(year), parseInt(month) - 1, 1))
  }

  return (
    <div>
      <MyHeader
        headText={headText}
        headSelectMonth={
          <input
            onChange={(e) => selectMonth(e.target.value)}
            className="input_month"
            type="month"
          />
        }
        leftChild={<MyButton text={"<"} onClick={decreaseMonth} />}
        rightChild={<MyButton text={">"} onClick={increaseMonth} />}
      />
      <LineChart diaryList={data} month={monthData} />
      <DiaryList diaryList={data} />
    </div>
  );
};

export default Home;

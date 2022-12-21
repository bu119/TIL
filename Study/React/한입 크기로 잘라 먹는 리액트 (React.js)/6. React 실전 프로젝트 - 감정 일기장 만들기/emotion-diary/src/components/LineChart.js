import React, { useContext, useMemo } from "react";

import Chart from 'chart.js/auto';
import { Line } from "react-chartjs-2";


const LineChart = ({ diaryList, month }) => {
  // console.log(diaryList)
  
  // 정렬
  const compare = (a, b) => {
    return parseInt(a.date) - parseInt(b.date);
  }
  const sortDiaryList = diaryList.sort(compare)
  
  // 1일부터 마지막 날까지 배열(날짜별 차트 보류...)
  // const dayList = [];
  // for (let i = 1; i <= parseInt(lastDay); ++i) {
  //   dayList.push(i);
  // }
  const emotionList = sortDiaryList.map((e) => {
    const day = new Date(e.date)
    return {'x':`${day.getDate()}일`,'y':5-e.emotion}
  })
  const dayList = sortDiaryList.map((e) => {
    const day = new Date(e.date)
    return `${day.getDate()}일`
  })
  // console.log(dayList)

  const setDayList = [...new Set(dayList)]

  let chartData = {
      labels: setDayList,
      datasets: [{
        type: 'line',
        data: emotionList,
        label: `${month}월의 기분 변화`,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
  };
    
	return (
    <div className="line_chart">
      <Line type="line" data={chartData}/>
    </div>
  );
}

export default React.memo(LineChart);
import React from "react";

import Chart from 'chart.js/auto';
import { Bar } from "react-chartjs-2";


const BarChart = ({ diaryList, lastDay }) => {
  // console.log(diaryList)
  
  // 1일부터 마지막 날까지 배열
  const alldayList = [];
  for (let i = 1; i <= parseInt(lastDay); ++i) {
    alldayList.push(`${i}일`);
  }

  // 감정별로 배열만들기
  const emotionBest = diaryList.filter((e)=>e.emotion === 1)
  const emotionGood = diaryList.filter((e)=>e.emotion === 2)
  const emotionSoso = diaryList.filter((e)=>e.emotion === 3)
  const emotionBad = diaryList.filter((e)=>e.emotion === 4)
  const emotionWorst = diaryList.filter((e)=>e.emotion === 5)

  // 감정별로 그래프에 적용할 x,y 배열 만들기
  const emotionBestList = emotionBest.map((e) => {
    const day = new Date(e.date)
    return {'x':`${day.getDate()}일`,'y':6-e.emotion}
  })
  const emotionGoodList = emotionGood.map((e) => {
    const day = new Date(e.date)
    return {'x':`${day.getDate()}일`,'y':6-e.emotion}
  })
  const emotionSosoList = emotionSoso.map((e) => {
    const day = new Date(e.date)
    return {'x':`${day.getDate()}일`,'y':6-e.emotion}
  })
  const emotionBadList = emotionBad.map((e) => {
    const day = new Date(e.date)
    return {'x':`${day.getDate()}일`,'y':6-e.emotion}
  })
  const emotionWorstList = emotionWorst.map((e) => {
    const day = new Date(e.date)
    return {'x':`${day.getDate()}일`,'y':6-e.emotion}
  })

  // const emotionList = diaryList.map((e) => {
  //   const day = new Date(e.date)
  //   return {'x':`${day.getDate()}일`,'y':6-e.emotion}
  // })
  
  // labels을 가지고 있는 값으로만 설정

  // 정렬
  // const compare = (a, b) => {
  //   return parseInt(a.date) - parseInt(b.date);
  // }
  // const sortDiaryList = diaryList.sort(compare)

  // 가지고 있는 값 저장
  // const dayList = sortDiaryList.map((e) => {
  //   const day = new Date(e.date)
  //   return `${day.getDate()}일`
  // })
  // console.log(dayList)

  // labels 중복 값 제거
  // const setDayList = [...new Set(dayList)]

  // let chartData = {
  //     labels: alldayList,
  //     datasets: [{
  //       type: 'line',
  //       data: emotionList,
  //       label: `${month}월의 기분 변화`,
  //       fill: false,
  //       borderColor: 'rgb(75, 192, 192)',
  //       tension: 0.1
  //     }]
  // };

  const options = {
    legend: {
        display: false, // label 숨기기
    },
    title: {
      display: true,		// 타이틀 
      text: "Total",
      fontSize: 25,
    },
    scales: {
      // x축값 누적
      x:{
        stacked:true
      },
      y: {
        suggestedMin: 0,
        suggestedMax: 5
    }
    },
    maintainAspectRatio: false // false로 설정 시 사용자 정의 크기에 따라 그래프 크기가 결정됨.
  }

  const emotioBackColor = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(255, 159, 64, 0.2)',
    'rgba(255, 205, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    // 'rgba(153, 102, 255, 0.2)',
    // 'rgba(201, 203, 207, 0.2)'
  ]
  const emotioBorderColor = [
    'rgb(255, 99, 132)',
    'rgb(255, 159, 64)',
    'rgb(255, 205, 86)',
    'rgb(75, 192, 192)',
    'rgb(54, 162, 235)',
    // 'rgb(153, 102, 255)',
    // 'rgb(201, 203, 207)'
  ]

  // const chartData = {
  //   labels: alldayList,
  //   datasets: [
  //     {
  //       label: `${month}월의 기분 변화`,
  //       backgroundColor: rankColor,
  //       borderColor: rankColor,
  //       borderWidth: 1,
  //       hoverBackgroundColor: rankColor,
  //       hoverBorderColor: rankColor,
  //       data: emotionList
  //     }
  //   ]
  // }; 

  const chartData = {
    labels: alldayList,
    datasets: [
      {
        label: '완전 좋음',
        backgroundColor: emotioBackColor[4],
        borderColor: emotioBorderColor[4],
        borderWidth: 1,
        hoverBackgroundColor: emotioBackColor[4],
        hoverBorderColor: emotioBorderColor[4],
        data: emotionBestList
      },
      {
        label: '좋음',
        backgroundColor: emotioBackColor[3],
        borderColor: emotioBorderColor[3],
        borderWidth: 1,
        hoverBackgroundColor: emotioBackColor[3],
        hoverBorderColor: emotioBorderColor[3],
        data: emotionGoodList
      },
      {
        label: '그럭저럭',
        backgroundColor: emotioBackColor[2],
        borderColor: emotioBorderColor[2],
        borderWidth: 1,
        hoverBackgroundColor: emotioBackColor[2],
        hoverBorderColor: emotioBorderColor[2],
        data: emotionSosoList
      },
      {
        label: '나쁨',
        backgroundColor: emotioBackColor[1],
        borderColor: emotioBorderColor[1],
        borderWidth: 1,
        hoverBackgroundColor: emotioBackColor[1],
        hoverBorderColor: emotioBorderColor[1],
        data: emotionBadList
      },
      {
        label: '끔찍함',
        backgroundColor: emotioBackColor[0],
        borderColor: emotioBorderColor[0],
        borderWidth: 1,
        hoverBackgroundColor: emotioBackColor[0],
        hoverBorderColor: emotioBorderColor[0],
        data: emotionWorstList
      },

    ]
  }; 

	return (
    <div className="bar_chart">
      <Bar 
        data={chartData}
        // width={300}
        height={200}
        options={options}
      />
    </div>
  );
}

export default React.memo(BarChart);
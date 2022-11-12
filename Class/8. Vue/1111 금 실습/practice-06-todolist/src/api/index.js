const getDueDateTime = () => {
  const nowDate = new Date()
  const fullYear = nowDate.getFullYear()
  const month = nowDate.getMonth() + 1
  const date = nowDate.getDate() 
  const hours = nowDate.getHours()
  const minutes = nowDate.getMinutes()
  return `${fullYear}-${month}-${date}T${hours}:${minutes}`
}

const mockCreateTodayTodo = data => {
  return {
    id: new Date().getTime(),
    dueDateTime: getDueDateTime(),
    isCompleted: false,
    isImportant: false,
    ...data,
  }
}

const mockCreateImportantTodo = data => {
  return {
    id: new Date().getTime(),
    dueDateTime: getDueDateTime(),
    isCompleted: false,
    isImportant: true,
    ...data,
  }
}

export {
  mockCreateTodayTodo,
  mockCreateImportantTodo,
}
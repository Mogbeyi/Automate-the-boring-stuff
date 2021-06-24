let parts = [
      {
        name: 'Fundamentals of React',
        exercises: 10,
        id: 1
      },
      {
        name: 'Using props to pass data',
        exercises: 7,
        id: 2
      },
      {
        name: 'State of a component',
        exercises: 14,
        id: 3
      }
]

const addLecturer = part => { 
    part.lecturer = 'Emmanuel'
    return part
}

let newParts = parts.map(addLecturer)
console.log(newParts)

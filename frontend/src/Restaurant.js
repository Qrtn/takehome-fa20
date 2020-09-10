import React, { Component } from 'react'
import Counter from './Counter'

class App extends Component {
  render() {
    const { name, rating } = this.props;

    return (
      <div>
        <span>{name}</span>
        
        <Counter count={parseInt(rating)} />
      </div>
    )
  }
}

export default App

import React, { Component } from 'react'

class Counter extends Component {
  state = {
    count: this.props.count
  }

  handleIncrement = () => {
    this.setState(({ count }) => ({count: count + 1}))
  }

  handleDecrement = () => {
    this.setState(({ count }) => ({count: count - 1}))
  }
  
  render() {
    return (
      <div>
        {this.state.count}
        <button onClick={this.handleIncrement}>+</button>
        <button onClick={this.handleDecrement}>-</button>
      </div>
    )
  }
}

export default Counter

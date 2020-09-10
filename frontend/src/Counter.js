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
      <div className="Counter">
        <button onClick={this.handleIncrement}>+</button>
        <span className="count">{this.state.count}</span>
        <button onClick={this.handleDecrement}>&minus;</button>
      </div>
    )
  }
}

export default Counter

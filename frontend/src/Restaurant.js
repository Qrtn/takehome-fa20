import React, { Component } from 'react'
import Counter from './Counter'

class Restaurant extends Component {
  render() {
    const { name, rating } = this.props;

    return (
      <div className="Restaurant">
        <Counter count={parseInt(rating)} />
        
        <span className="name">{name}</span>
      </div>
    )
  }
}

export default Restaurant

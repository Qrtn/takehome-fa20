import React, { Component } from 'react'
import Instructions from './Instructions'
import Restaurant from './Restaurant'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      restaurants: [
        {id: 1, name: "Golden Harbor", rating: 10},
        {id: 2, name: "Potbelly", rating: 6},
        {id: 3, name: "Noodles and Company", rating: 8},
      ],
      newestId: 3,
      newName: "",
    }
  }

  handleNameChange = ({ target: { value } }) => {
    this.setState({ newName: value })
  }

  handleNameSubmit = (event) => {
    this.setState(({ restaurants, newestId, newName }) => ({
      restaurants: [...restaurants, {
        id: newestId + 1,
        name: newName,
        rating: 0
      }],
      newestId: newestId + 1,
      newName: ""
    }))

    event.preventDefault()
    return false
  }

  render() {
    const { newName } = this.state;

    return (
      <div className="App">
        <Instructions complete={true} />
        <hr />

        <h2>Parts 2&ndash;5</h2>
        
        <h3>Yelp4Impact</h3>
        {this.state.restaurants.map(x => (
          <Restaurant id={x.id} name={x.name} rating={x.rating} />
        ))}

        <form className="addRestaurant" onSubmit={this.handleNameSubmit}>
          <button type="submit">Add</button>
          <input value={newName} onChange={this.handleNameChange} placeholder="Restaurant name" />
        </form>
      </div>
    )
  }
}

export default App

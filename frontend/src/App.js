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

  handleNameSubmit = () => {
    this.setState(({ restaurants, newestId, newName }) => ({
      restaurants: [...restaurants, {
        id: newestId + 1,
        name: newName,
        rating: 0
      }],
      newestId: newestId + 1,
      newName: ""
    }))
  }

  render() {
    const { newName } = this.state;

    return (
      <div className="App">
        <Instructions complete={true} />
        {this.state.restaurants.map(x => (
          <Restaurant id={x.id} name={x.name} rating={x.rating} />
        ))}

        <input value={newName} onChange={this.handleNameChange} />
        <button type="button" onClick={this.handleNameSubmit}>Add Restaurant</button>
      </div>
    )
  }
}

export default App

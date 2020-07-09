import React, { Component } from 'react'
import axios from 'axios'

let getData = async () =>
    await axios.get(`http://127.0.0.1:8000/gpuApi/`)
        .then(response => console.log(response.data))
        .catch(error => console.log(error))


class Home extends Component {

    handleClick = () => {
        console.log("Clicked")

        getData()
    }
    render() {
        return (
            <div>
                <h1>Home Page</h1>
                <button onClick={this.handleClick}>Click me</button>
            </div>
        )
    }
}
export default Home;

// let getData = async () =>
//     await axios.get(`http://127.0.0.1:8000/gpuApi/`)
//         .then(response => console.log(response.data))
//         .catch(error => console.log(error))

// getData()
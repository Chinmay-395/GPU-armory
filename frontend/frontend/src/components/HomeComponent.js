import React, { Component } from 'react'
import axios from 'axios'
import img1 from '../shared/img11.jpg'
import img2 from '../shared/img13.jpg'
import img3 from '../shared/img15.jpg'

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
            <>
                <CarouselFuncComponent />
                <div className="container">
                    <div className="row">
                        <h1>Home Page</h1>
                        <br />
                        <button onClick={this.handleClick}>Click me</button>
                    </div>
                </div>
            </>
        )
    }
}
export default Home;

export const CarouselFuncComponent = () => {
    return (
        <div id="demo" className="carousel slide" data-ride="carousel">
            <ul className="carousel-indicators">
                <li data-target="#demo" data-slide-to="0" className="active"></li>
                <li data-target="#demo" data-slide-to="1"></li>
                <li data-target="#demo" data-slide-to="2"></li>
            </ul>
            <div className="carousel-inner">
                <div className="carousel-item active">
                    <img src={img1} alt="Los Angeles" width="1100" height="500" />
                    <div className="carousel-caption">
                        <h3>Los Angeles</h3>
                        <p>We had such a great time in LA!</p>
                    </div>
                </div>
                <div className="carousel-item">
                    <img src={img3} alt="Chicago" width="1100" height="500" />
                    <div className="carousel-caption">
                        <h3>Chicago</h3>
                        <p>Thank you, Chicago!</p>
                    </div>
                </div>
                <div className="carousel-item">
                    <img src={img2} alt="New York" width="1100" height="500" />
                    <div className="carousel-caption">
                        <h3>New York</h3>
                        <p>We love the Big Apple!</p>
                    </div>
                </div>
            </div>
            <a className="carousel-control-prev" href="#demo" data-slide="prev">
                <span className="carousel-control-prev-icon"></span>
            </a>
            <a className="carousel-control-next" href="#demo" data-slide="next">
                <span className="carousel-control-next-icon"></span>
            </a>
        </div>
    )
}
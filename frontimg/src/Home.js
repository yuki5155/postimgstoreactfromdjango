import { findAllByTitle } from '@testing-library/react';
import axios from 'axios';
import React, { useState, useEffect, useRef } from 'react';

function Home() {

    const [imagelist, setimagelist] = useState([])

    const [upimage, setupimage] = useState()

    
    useEffect(() => {
        axios.get(`http://localhost:8000/`,{
          
          headers: {
              'Content-Type': 'application/json',
              
              
              
          }
        },
        )
        .then(
            //response =>console.log(response.data.tasks),
            //response => setUsers(response.data.tasks),
            response =>{
                //console.log(response.data)
                setimagelist(response.data);
                
              
            
            
            },)
    }
    ,[])

    const handleImageChange = (e) => {
        //this.setState({
          //image: e.target.files[0]
        //})
        //console.log(e.target.files[0])
        setupimage(e.target.files[0])
      };

    
      const handleSubmit = async (e) => {
        e.preventDefault();
        
        let form_data = new FormData();
        form_data.append('img', upimage);

        console.log(form_data)
        //form_data.append('title', this.state.title);
        //form_data.append('content', this.state.content);
        let url = 'http://localhost:8000/';
        axios.post(url, form_data, {
          headers: {
            'content-type': 'multipart/form-data'
          }
        })
            .then(res => {
                setimagelist(res.data);
            })
            .catch(err => console.log(err))
      };





 
    return (
      
        <>
            <p>sssaas</p>

            {imagelist.map((image) => (
                <img src={image.img}  />
               
            ))}
            <form　onSubmit={handleSubmit}>
            <input type="file"
                   id="image"
                   accept="image/png, image/jpeg" onChange={handleImageChange} required/>

            <input type="submit"/>

            </form>


        </>

        
        
        
    );
  }
  
  export default Home;
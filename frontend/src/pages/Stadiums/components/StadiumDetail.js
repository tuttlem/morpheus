import React, {useEffect, useState} from 'react';
import {
  Button,
  Card,
  CardBody,
  CardGroup,
  CardImg,
  CardText,
  CardTitle,
  Col,
  Container, Dropdown, DropdownItem, DropdownMenu, DropdownToggle,
  Form, FormGroup, Input, Label,
  Row,
  Table
} from "reactstrap";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCirclePlus, faDeleteLeft, faHome} from "@fortawesome/free-solid-svg-icons";
import axios from "axios";
import {faEdit} from "@fortawesome/free-solid-svg-icons/faEdit";
import {Link} from "react-router-dom";
import {toast} from "react-toastify";


const StadiumDetail = ({ id, onUpdateSuccess }) => {
  const [data, setData] = useState([]);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const images = [...Array(17).keys()].map(k => (`${k+1}.png`));

  useEffect(() => {
    if (id === 'new') {
      // create a new stadium data object to use
      setData({
        name: '',
        location: '',
        image: '',
      });
    } else {
      // get the stadium data and fill the data object
      axios.get(`http://localhost:5000/stadiums/${id}`)
        .then(response => {
          setData(response.data);
          handleImageSelect(response.data.image);
        })
        .catch(error => {
          toast.error('Unable to retrieve');
          console.error(error);
        });
    }

  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleImageSelect = (image) => {
    setData((prevData) => ({ ...prevData, image: image }));
    setDropdownOpen(false);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // prune the data object
    const { name, location, image } = data;
    const pruned = { name, location, image };

    if (id === 'new') {
      // perform an add action against the api
      axios.post(`http://localhost:5000/stadiums`, pruned)
        .then(response => {
          onUpdateSuccess();
        })
        .catch(error => {
          toast.error('Unable to save');
          console.error(error);
        });
    } else {
      // perform an update action against the api
      axios.put(`http://localhost:5000/stadiums/${id}`, pruned)
        .then(response => {
          onUpdateSuccess();
        })
        .catch(error => {
          toast.error('Unable to save');
          console.error(error);
        });
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Row>
        <Col md={6}>
          <FormGroup>
            <Label for="name">Name</Label>
            <Input
              type="text"
              name="name"
              id="name"
              value={data.name}
              onChange={handleChange}
              placeholder="Enter your name"
            />
          </FormGroup>

          <FormGroup>
            <Label for="location">Location</Label>
            <Input
              type="text"
              name="location"
              id="location"
              value={data.location}
              onChange={handleChange}
              placeholder="Enter your location"
            />
          </FormGroup>

          <FormGroup>
            <Label for="image">Select an Image</Label>
            <Dropdown isOpen={dropdownOpen} toggle={() => setDropdownOpen(!dropdownOpen)}>
              <DropdownToggle caret>
                {data.image}
              </DropdownToggle>
              <DropdownMenu>
                {images.map((image) => (
                  <DropdownItem key={image} onClick={() => handleImageSelect(image)}>
                    {image}
                  </DropdownItem>
                ))}
              </DropdownMenu>
            </Dropdown>
          </FormGroup>

          <Button color="primary" type="submit">
            Submit
          </Button>
        </Col>
        <Col md={6}>
          <div>
            <h3>Image Preview</h3>
            <img src={`/assets/images/stadiums/${data.image}`} alt="Preview" style={{ width: '100%', height: 'auto' }} />
          </div>
        </Col>
      </Row>
    </Form>
  );
};

export default StadiumDetail;
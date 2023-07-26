import React, {useEffect, useState} from 'react';
import {Button, Card, CardBody, CardGroup, CardImg, CardText, CardTitle, Col, Container, Row, Table} from "reactstrap";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCirclePlus, faDeleteLeft, faHome} from "@fortawesome/free-solid-svg-icons";
import axios from "axios";
import {faEdit} from "@fortawesome/free-solid-svg-icons/faEdit";
import {Link} from "react-router-dom";
import {toast} from "react-toastify";

const CardRow = ({ data }) => {
  return (
    <CardGroup >
      {data.map(item => (
        <Card key={item.id} className="data-card m-2" outline>
          <CardImg top style={{objectFit: "cover"}} height="120vh" src={`/assets/images/stadiums/${item.image}`}></CardImg>
          <CardBody>
            <CardTitle>{item.name}</CardTitle>
            <CardText>{item.location}</CardText>

            <Link to={`/stadiums/${item.id}`}>
              <Button color="primary" size="sm">
                <FontAwesomeIcon icon={faEdit}></FontAwesomeIcon>&nbsp;
              </Button>
            </Link>

            <Link to={`/stadiums/${item.id}/delete`}>
              <Button color="danger" size="sm">
                <FontAwesomeIcon icon={faDeleteLeft}></FontAwesomeIcon>&nbsp;
              </Button>
            </Link>

          </CardBody>
        </Card>
      ))}
    </CardGroup>
  );
};

const StadiumList = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/stadiums')
      .then(response => {
        const groupedData = [];
        for (let i = 0; i < response.data.length; i += 3) {
          groupedData.push(response.data.slice(i, i + 3));
        }

        setData(groupedData);
      })
      .catch(error => {
        toast.error('Unable to retrieve');
        console.error(error);
      });
  }, []);

  return (
    <Container>
      {data.map((group, index) => (
        <Row>
          <Col>
            <CardRow key={index} data={group} />
          </Col>
        </Row>

      ))}
    </Container>
  );
};

export default StadiumList;
import React, {useEffect, useState} from 'react';
import {Button, Col, Container, Row, Table} from "reactstrap";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCirclePlus, faDeleteLeft, faHome} from "@fortawesome/free-solid-svg-icons";
import axios from "axios";
import {faEdit} from "@fortawesome/free-solid-svg-icons/faEdit";

const CompetitionList = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/competitions')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <Container>
      <Row>
        <Col>
          <Table>
            <thead>
              <tr>
                <th>#</th>
                <th>Name</th>
                <th>Sport</th>
                <th>Structure</th>
                <td align="right">
                  <Button color="success" size="sm">
                    <FontAwesomeIcon icon={faCirclePlus}></FontAwesomeIcon>&nbsp;
                  </Button>
                </td>
              </tr>
            </thead>
            <tbody>
            {data.map(item => (
              <tr key={item.id}>
                <td>{item.id}</td>
                <td>{item.name}</td>
                <td>{item.sport}</td>
                <td>{item.structure}</td>
                <td>
                  <Button color="primary" size="sm">
                    <FontAwesomeIcon icon={faEdit}></FontAwesomeIcon>&nbsp;
                  </Button>

                  <Button color="error" size="sm">
                    <FontAwesomeIcon icon={faDeleteLeft}></FontAwesomeIcon>&nbsp;
                  </Button>
                </td>
              </tr>
            ))}
            </tbody>
          </Table>
        </Col>
      </Row>
    </Container>
  );
};

export default CompetitionList;
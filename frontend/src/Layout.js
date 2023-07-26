import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import {Outlet} from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import { ToastContainer } from 'react-toastify';

const App = () => {
  return (

    <Container fluid>
      <Row>
        <Col>
          <Header />
          <ToastContainer />
        </Col>
      </Row>
      <Row>
        <Col md="3">
          <Sidebar />
        </Col>
        <Col md="9">
          <Outlet />
        </Col>
      </Row>
    </Container>

  );
};

export default App;
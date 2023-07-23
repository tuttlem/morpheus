import React from 'react';
import { Container, Row, Col } from 'reactstrap';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';

const App = () => {
  return (
    <Router>
      <Container fluid>
        <Row>
          <Col>
            <Header />
          </Col>
        </Row>
        <Row>
          <Col md="3">
            <Sidebar />
          </Col>
          <Col md="9">
            <Switch>
              <Route exact path="/" component={Dashboard} />
              {/* Add more routes for other pages */}
              {/* For example: */}
              {/* <Route path="/users" component={Users} /> */}
              {/* <Route path="/settings" component={Settings} /> */}
            </Switch>
          </Col>
        </Row>
      </Container>
    </Router>
  );
};

export default App;
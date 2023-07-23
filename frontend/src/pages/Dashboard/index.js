import React from 'react';
import {Col, Container, Row} from "reactstrap";

const Dashboard = () => {
  return (
    <Container>
      <Row>
        <Col>
          <h1>Morpheus</h1>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Step into the world of exhilarating tackles, mesmerizing tries, and tactical brilliance.
            Our Fantasy Rugby Dashboard is your gateway to an immersive rugby experience like never before.
            Assemble your dream team of rugby superstars, strategize your moves, and compete with fellow fans from across the globe.
          </p>
          <p>
            Stay up-to-date with real-time player stats, injury updates, and match highlights.
            Unleash your managerial prowess, make shrewd transfers, and lead your team to victory in the ultimate test of rugby knowledge and foresight.
          </p>
          <p>
            Whether you're a seasoned rugby aficionado or a newcomer to the sport, the Fantasy Rugby Dashboard promises
            endless excitement and adrenaline-pumping moments. Prepare to embark on a thrilling journey as you rise through
            the ranks, claim bragging rights, and make your mark in the world of fantasy rugby.
          </p>
          <p>
            Get ready to embrace the passion, embrace the intensity, and embrace the fantasy!
          </p>
          <p>
            Let the games begin!
          </p>
        </Col>
      </Row>
    </Container>
  );
};

export default Dashboard;
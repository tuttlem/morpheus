import React from 'react';
import {Col, Container, Row} from "reactstrap";
import CompetitionList from "./components/CompetitionList";

const Competitions = () => {
  return (
    <Container>
      <Row>
        <Col>
          <h1>Competitions</h1>
        </Col>
      </Row>
      <Row>
        <Col>
          <p>
            Enter the adrenaline-charged realm of Rugby League and Rugby Union showdowns,
            where teams battle for supremacy. Witness lightning-fast action in Rugby League
            tournaments and the strategic brilliance of Rugby Union epics.
          </p>
          <p>
            Each competition features its own championship trophy, a shining symbol of victory
            and determination. With diverse formats like league battles, knockout showdowns,
            and electrifying international clashes, this is where unforgettable rugby moments
            are made.
          </p>
          <p>
            Choose your favorites, cheer passionately, and immerse yourself in the ultimate
            rugby experience!
          </p>
        </Col>
      </Row>
      <Row>
        <Col>
          <CompetitionList></CompetitionList>
        </Col>
      </Row>
    </Container>
  );
};

export default Competitions;
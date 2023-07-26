import React from 'react';
import {Button, Col, Container, Row} from "reactstrap";
import StadiumList from "./components/StadiumList";
import {Link, useParams, useNavigate} from "react-router-dom";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {faCirclePlus} from "@fortawesome/free-solid-svg-icons";
import StadiumDetail from "./components/StadiumDetail";
import {toast} from "react-toastify";

const Stadiums = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const handleUpdateSuccess = () => {
    toast.success('Save successful');
    navigate('/stadiums');
  };

  return (
    <Container>

      {id && (
        <>
        <Row>
          <Col>
            <h1>Stadium Details</h1>
          </Col>
        </Row>
          <Row>
            <Col>
              <p>
                Here, you can add or edit essential information about your stadium. Fill in the
                stadium's name and location, and select an image that represents your venue perfectly.
                Whether you're creating a new stadium profile or updating existing details, this
                simple and user-friendly form ensures all the necessary data is captured accurately.
              </p>
              <p>
                Enjoy the ease of managing your stadium's information and showcase its unique features
                with an eye-catching image. Let's ensure your stadium stands out among the rest!
              </p>
            </Col>
          </Row>
        <Row>
          <Col>
            <StadiumDetail id={id} onUpdateSuccess={handleUpdateSuccess} />
          </Col>
        </Row>
        </>
      )}

      {!id && (
        <>
          <Row>
            <Col>
              <h1>Stadiums</h1>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>
                Welcome to our exclusive Stadium List, a gateway to the hallowed grounds where
                rugby history was written. Embark on a journey through the most revered stadiums
                across the globe, where the roars of passionate fans echo and the spirit of the
                game soars to new heights.
              </p>
              <p>
                Discover the legendary venues that have witnessed epic clashes, historic victories,
                and heart-stopping moments. From the iconic stadiums of Twickenham and Eden Park to
                the electric atmosphere of Suncorp Stadium and Ellis Park, each venue holds a unique
                charm and a captivating story.
              </p>
              <p>
                Whether you're a seasoned rugby enthusiast or a newcomer to the sport, our Stadium List
                promises an exhilarating experience for all. So, gear up for an unforgettable adventure
                through the meccas of rugby, where the essence of the game comes alive, and the
                memories of champions are etched in time.
              </p>
            </Col>
          </Row>
          <Row>
            <Col>
              <Link to="new">
                <Button type="button" color="success" size="sm">
                  <FontAwesomeIcon icon={faCirclePlus}></FontAwesomeIcon>&nbsp;
                  Create new
                </Button>
              </Link>
            </Col>
          </Row>
          <Row>
            <Col>
              <StadiumList></StadiumList>
            </Col>
          </Row>
        </>
    )}
    </Container>
  );
};

export default Stadiums;
import React from 'react';
import {
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {
  faCirclePlay,
  faHome,
  faTrophy,
  faPeopleGroup,
  faPersonRunning,
  faHockeyPuck,
  faTable,
} from "@fortawesome/free-solid-svg-icons";
import {Link} from "react-router-dom";

const Sidebar = () => {
  return (
    <Nav vertical className="list-unstyled pb-3">
      <NavItem>

        <NavLink tag={Link} to={"/"}>
          <FontAwesomeIcon icon={faHome}></FontAwesomeIcon>&nbsp;
          Home
        </NavLink>

        <NavLink tag={Link} to={"/competitions"}>
          <FontAwesomeIcon icon={faTrophy}></FontAwesomeIcon>&nbsp;
          Competitions
        </NavLink>

        <NavLink tag={Link} to={"/"}>
          <FontAwesomeIcon icon={faPeopleGroup}></FontAwesomeIcon>&nbsp;
          Teams
        </NavLink>

        <NavLink tag={Link} to={"/"}>
          <FontAwesomeIcon icon={faPersonRunning}></FontAwesomeIcon>&nbsp;
          Players
        </NavLink>

        <NavLink tag={Link} to={"/stadiums"}>
          <FontAwesomeIcon icon={faHockeyPuck}></FontAwesomeIcon>&nbsp;
          Stadiums
        </NavLink>

        <NavLink tag={Link} to={"/"}>
          <FontAwesomeIcon icon={faTable}></FontAwesomeIcon>&nbsp;
          Results
        </NavLink>


      </NavItem>
    </Nav>
  );
};

export default Sidebar;
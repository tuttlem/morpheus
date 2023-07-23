import React, { useState } from 'react';
import { Collapse, Navbar, NavbarBrand, Nav, NavItem, NavLink, Input } from 'reactstrap';

const Header = () => {
  const [searchOpen, setSearchOpen] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSearch = () => {
    setSearchOpen(!searchOpen);
  };

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <Navbar className="navbar sticky-top bg-dark flex-md-nowrap p-0 shadow" color="dark" expand="md">
      <NavbarBrand className="col-md-3 col-lg-2 me-0 px-3 fs-6 text-white" href="#">Morpheus</NavbarBrand>

    </Navbar>
  );
};

export default Header;
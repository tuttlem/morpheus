
import {useEffect, useState} from "react";

// @mui material components
import Card from "@mui/material/Card";
import Icon from "@mui/material/Icon";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";

// Material Dashboard 2 React components
import MDBox from "components/MDBox";
import MDTypography from "components/MDTypography";

// Material Dashboard 2 React examples
import DataTable from "examples/Tables/DataTable";

import MDProgress from "../../../../components/MDProgress";
import MDButton from "../../../../components/MDButton";

function StadiumList() {
  const [columns, setColumns] = useState([
    { Header: "name", accessor: "name", width: "40%", align: "left" },
    { Header: "location", accessor: "location", width: "40%", align: "left" },
    { Header: "", accessor: "actions", width: "20%", align: "right" },
    ]);

  const [rows, setRows] = useState([]);

  const [menu, setMenu] = useState(null);

  const openMenu = ({ currentTarget }) => setMenu(currentTarget);
  const closeMenu = () => setMenu(null);

  const renderMenu = (
    <Menu
      id="simple-menu"
      anchorEl={menu}
      anchorOrigin={{
        vertical: "top",
        horizontal: "left",
      }}
      transformOrigin={{
        vertical: "top",
        horizontal: "right",
      }}
      open={Boolean(menu)}
      onClose={closeMenu}
    >
      <MenuItem onClick={closeMenu}>Action</MenuItem>
      <MenuItem onClick={closeMenu}>Another action</MenuItem>
      <MenuItem onClick={closeMenu}>Something else</MenuItem>
    </Menu>
  );

  const makeRow = (row) => (
    {
      name: (
        <MDTypography component="a" href={`/stadiums/${row.id}`} variant="caption" color="text" fontWeight="medium">
          {row.name}
        </MDTypography>
      ),
      location: row.location,
      actions: (
        <MDTypography component="a" href="#" variant="caption" color="text" fontWeight="medium">
          Delete
        </MDTypography>
      ),
    }
  )

  useEffect(() => {
    fetch('http://localhost:5000/stadiums')
      .then(response => response.json())
      .then(json => setRows(json.map(makeRow)))
      .catch(error => console.error(error));
  }, []);

  return (
    <Card>
      <MDBox display="flex" justifyContent="space-between" alignItems="center" p={3}>
        <MDBox>
          <MDTypography variant="h6" gutterBottom>
            Stadiums
          </MDTypography>
        </MDBox>
        <MDBox color="text" px={2}>
          <Icon sx={{ cursor: "pointer", fontWeight: "bold" }} fontSize="small" onClick={openMenu}>
            more_vert
          </Icon>
        </MDBox>
        {renderMenu}
      </MDBox>
      <MDBox>
        <DataTable
          table={{ columns, rows }}
          showTotalEntries={false}
          isSorted={false}
          noEndBorder
          entriesPerPage={false}
        />
      </MDBox>
    </Card>
  );
}

export default StadiumList;

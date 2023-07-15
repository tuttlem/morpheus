import Dashboard from "layouts/dashboard";
import Home from "layouts/home";
import Tables from "layouts/tables";
import Billing from "layouts/billing";
import RTL from "layouts/rtl";
import Notifications from "layouts/notifications";
import Profile from "layouts/profile";
import SignIn from "layouts/authentication/sign-in";
import SignUp from "layouts/authentication/sign-up";
import Icon from "@mui/material/Icon";

const routes = [
  {
    type: "collapse",
    name: "Home",
    key: "home",
    icon: <Icon fontSize="small">home</Icon>,
    route: "/home",
    component: <Home />,
  },
  {
    type: "collapse",
    name: "Competitions",
    key: "competitions",
    icon: <Icon fontSize="small">emoji_events</Icon>,
    route: "/competitions",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Games",
    key: "games",
    icon: <Icon fontSize="small">sports</Icon>,
    route: "/games",
    component: <Dashboard />,
  },

  {
    type: "collapse",
    name: "Teams",
    key: "teams",
    icon: <Icon fontSize="small">groups</Icon>,
    route: "/teams",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Players",
    key: "players",
    icon: <Icon fontSize="small">people</Icon>,
    route: "/people",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Stadiums",
    key: "stadium",
    icon: <Icon fontSize="small">stadium</Icon>,
    route: "/stadiums",
    component: <Dashboard />,
  },
/*
  {
    type: "collapse",
    name: "Dashboard",
    key: "dashboard",
    icon: <Icon fontSize="small">dashboard</Icon>,
    route: "/dashboard",
    component: <Dashboard />,
  },
  {
    type: "collapse",
    name: "Tables",
    key: "tables",
    icon: <Icon fontSize="small">table_view</Icon>,
    route: "/tables",
    component: <Tables />,
  },
  {
    type: "collapse",
    name: "Billing",
    key: "billing",
    icon: <Icon fontSize="small">receipt_long</Icon>,
    route: "/billing",
    component: <Billing />,
  },
  {
    type: "collapse",
    name: "RTL",
    key: "rtl",
    icon: <Icon fontSize="small">format_textdirection_r_to_l</Icon>,
    route: "/rtl",
    component: <RTL />,
  },
  {
    type: "collapse",
    name: "Notifications",
    key: "notifications",
    icon: <Icon fontSize="small">notifications</Icon>,
    route: "/notifications",
    component: <Notifications />,
  },
  {
    type: "collapse",
    name: "Profile",
    key: "profile",
    icon: <Icon fontSize="small">person</Icon>,
    route: "/profile",
    component: <Profile />,
  },
  {
    type: "collapse",
    name: "Sign In",
    key: "sign-in",
    icon: <Icon fontSize="small">login</Icon>,
    route: "/authentication/sign-in",
    component: <SignIn />,
  },
  {
    type: "collapse",
    name: "Sign Up",
    key: "sign-up",
    icon: <Icon fontSize="small">assignment</Icon>,
    route: "/authentication/sign-up",
    component: <SignUp />,
  },
 */
];

export default routes;

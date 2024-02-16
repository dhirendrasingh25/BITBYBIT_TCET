// assets
import { LoginOutlined, ProfileOutlined } from "@ant-design/icons";

// icons
const icons = {
  LoginOutlined,
  ProfileOutlined,
};

// ==============================|| MENU ITEMS - EXTRA PAGES ||============================== //

const User = {
  id: "User Management",
  title: "User Management",
  type: "group",
  children: [
    {
      id: "profile",
      title: "Profile",
      type: "item",
      url: "/profile",
      icon: icons.LoginOutlined,
      target: true,
    },
    {
      id: "",
      title: "Register",
      type: "item",
      url: "/register",
      icon: icons.ProfileOutlined,
      target: true,
    },
  ],
};

export default User;

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
      title: "View Profile",
      type: "item",
      url: "/profile",
      icon: icons.LoginOutlined,
      target: true,
    },
    {
      id: "edit-profile",
      title: "Edit Profile",
      type: "item",
      url: "/edit-profile",
      icon: icons.LoginOutlined,
      target: true,
    },

    {
      id: "Users",
      title: "User  List",
      type: "item",
      url: "/users",
      icon: icons.ProfileOutlined,
      target: true,
    },
    {
      id: "AddTransaction",
      title: "Add Transaction",
      type: "item",
      url: "/add-transaction",
      icon: icons.ProfileOutlined,
      target: true,
    },
    {
      id: "calander",
      title: "Calander",
      type: "item",
      url: "/calander",
      icon: icons.ProfileOutlined,
      target: true,
    },
  ],
};

export default User;

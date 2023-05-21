import React from 'react'
import HomeIcon from '@mui/icons-material/Home';
import DashboardIcon from '@mui/icons-material/Dashboard';
import InfoIcon from '@mui/icons-material/Info';
import ContactPhoneIcon from '@mui/icons-material/ContactPhone';
import Person2Icon from '@mui/icons-material/Person2';
import LoginIcon from '@mui/icons-material/Login';
import LogoutIcon from '@mui/icons-material/Logout';

export const SidebarData= [
    {
        title:"Home",
        icon: <HomeIcon />,
        link:"/home"
    },
    {
        title:"Dash Board",
        icon: <DashboardIcon />,
        link:"/dashboard"
    },
    {
        title:"Information",
        icon: <InfoIcon />,
        link:"/information"
    },
    {
        title:"Contact",
        icon: <ContactPhoneIcon />,
        link:"/contact"
    },
    {
        title:"Profile",
        icon: <Person2Icon />,
        link:"/profile"
    },
    {
        title:"Log In",
        icon: <LoginIcon />,
        link:"/login"
    },

    {
        title:"Log Out",
        icon: <LogoutIcon />,
        link:"/logout"
    }


   

  
]


 
import React from 'react'

import { SidebarData } from './SidebarData'

function Sidebar() {
  return (
    <div className='sidebar'>
        <ul className='SidebarList'>
        {SidebarData.map((val,key)=>{
            return <li key={key} onClick={()=>{window.location.pathname = val.link}} className='row' id={window.location.pathname == val.link ? "active" : ""}>
                {" "}
                <div id='icon'>{val.icon}</div>{" "}
                <div id='title'>
                    {val.title}
                </div>
            </li>
        })}
        </ul>
    </div>
  )
}

export default Sidebar

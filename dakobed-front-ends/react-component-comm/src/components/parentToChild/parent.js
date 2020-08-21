import React from 'react'
import Child from './child'


const parent = (props) => {
    return (
        <div className ="App">
            <Child doWhatever ={props.keepWorldSameEvent} title={props.title}/>
            <Child doWhatever ={props.changeTheWorldEvent} title={props.title}/>
        </div>
    )
}
export default parent

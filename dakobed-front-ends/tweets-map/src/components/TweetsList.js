import React from 'react';

class TweetsList extends React.Component{
    constructor(props){
        super(props)
    }

    render(){
        const data =[{"name":"test1"},{"name":"test2"}];
        const listItems = data.map((d) => <li key={d.name}>{d.name}</li>);
        return(
            <div>
                {listItems }
            </div>
        )
    }
}

export default TweetsList; 

// export default function TweetsList(){
    
//     return( <div>
//         <h1>What are people tweeting about</h1>
//     </div>);

// }
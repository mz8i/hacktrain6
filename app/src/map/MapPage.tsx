import moment from 'moment';
import React from 'react';
import { Dropdown } from 'semantic-ui-react';

import 'leaflet/dist/leaflet.css';
import './MapPage.css';

import { stations } from '../data';

import { DelayMap } from './DelayMap';

interface MapPageState {
    location?: string;
    day?: Date;
    otherDay?: Date;
}

class MapPage extends React.Component<{}, MapPageState> {

    constructor(props) {
        super(props);
        this.state = {
            location: undefined,
            day: undefined,
            otherDay: undefined
        };
    }

    render() {
        return (
            <div className='map-page'>
                <div className="menu">
                    <Dropdown
                        className='menu-input'
                        placeholder='Station'
                        fluid
                        clearable
                        options={
                            stations
                            .map(s=>({
                                text: s.name,
                                value: s.code
                            }))
                            .sort((a,b) => a.text.localeCompare(b.text))
                        }
                        onChange={(e, data) => {
                            const val = data.value === '' ? undefined : data.value;
                            this.setState({
                                location: val as string
                            });
                        }}
                    />
                </div>
                {
                    this.state.location != undefined &&
                    <DelayMap
                        center={[52.476515,
                            -1.899737]}
                        stations={[]}
                        metrics={[]}
                        styleFunction={() => ({ color: 'red' })}
                    />    
                }
                          
            </div>
        );
    }
}

export {
    MapPage
};

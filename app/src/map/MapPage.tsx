import moment from 'moment';
import React from 'react';
import { Dropdown } from 'semantic-ui-react';

import './MapPage.css';

import { stations, stationsLookup } from '../../data';

interface MapPageState {
    location?: string;
    day?: Date;
    otherDay?: Date;
}

function stationToOption(station) {
    return {

    };
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
            <div>
                <div className="menu">
                    Menu
                    <div>
                        <Dropdown
                            className='menu-input'
                            placeholder='Station'
                            fluid
                            options={
                                stations
                                .map(s=>({
                                    text: s.name,
                                    value: s.code
                                }))
                                .sort((a,b) => a.text.localeCompare(b.text))
                            }
                            onChange={(e, data) => {
                                this.setState({
                                    location: data.value as string
                                });
                            }}
                        />
                    </div>
                    {
                        this.state.location != undefined &&
                            <div>
                                You have chosen {this.state.location}
                            </div>
            }
                </div>
                <div>
                    Visualisation
                </div>
            </div>
        );
    }
}

export {
    MapPage
};

import moment, { Moment } from 'moment';
import React from 'react';
import DatePicker from 'react-datepicker';
import { Dropdown } from 'semantic-ui-react';

import 'leaflet/dist/leaflet.css';
import 'react-datepicker/dist/react-datepicker.css';
import './MapPage.css';

import { connectionsLookup } from '../data/stationConnections';
import { stations, stationsLookup } from '../data/stations';
import { Station } from '../models/station';

import { DelayMap } from './DelayMap';

interface MapPageState {
    location?: string;
    day?: Date;
    otherDay?: Date;
}

function optionsFromStations(stations) {
    return stations
        .map(s => ({
            text: s.name,
            value: s.code
        }))
        .sort((a, b) => a.text.localeCompare(b.text));
}

class MapPage extends React.Component<{}, MapPageState> {

    constructor(props) {
        super(props);
        this.state = {
            location: 'BHAMNWS',
            day: undefined,
            otherDay: undefined
        };

        this.updateStation = this.updateStation.bind(this);
        this.updateIncidentDate = this.updateIncidentDate.bind(this);
        this.updateOtherIncidentDate = this.updateOtherIncidentDate.bind(this);
    }

    basicStyleFunction = (s: Station) => ({
        radius: s.code === this.state.location ? 12 : 8,
        fillColor: "white",
        color: "#000",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.8
    })

    updateStation(e, data) {
        const val = data.value === '' ? undefined : data.value;
        this.setState({
            location: val as string
        });
    }

    updateIncidentDate(date: Date) {
        this.setState({
            day: date
        });
    }

    updateOtherIncidentDate(date: Date) {
        this.setState({
            otherDay: date
        });
    }

    getSelectedStations(stationCode): Station[] {
        if(stationCode == undefined) return undefined;

        const selectedStationConnections = connectionsLookup[stationCode];

        if(selectedStationConnections == undefined) return undefined;

        const selectedStations = Object
                .entries(selectedStationConnections)
                .map(([sCode, connections]: [string, string[]]) => {
                    const station = stationsLookup[sCode];
                    station.connections = connections;
                    return station;
                });

        return selectedStations;
    }

    render() {

        let selectedStations, mainStation;
        if(this.state.location != undefined) {
            selectedStations = this.getSelectedStations(this.state.location);
            mainStation = stationsLookup[this.state.location];
        }

        return (
            <div className='map-page'>
                <div className="menu">
                    <div>
                        <label htmlFor='station-picker'>
                            Station:
                        </label>
                        <Dropdown clearable
                            search={true}
                            id='station-picker'
                            className='menu-input'
                            options={optionsFromStations(stations)}
                            onChange={this.updateStation}
                            style={{border:'1px solid grey'}}
                        />
                    </div>
                    {
                        this.state.location != undefined &&
                        <>
                            <div>
                                <label htmlFor='incident-date-picker'>
                                    Incident date:
                                </label>
                                <DatePicker
                                    id='incident-date-picker'
                                    className='menu-input'
                                    selected={this.state.day}
                                    onChange={this.updateIncidentDate}
                                />
                            </div>
                            {
                                this.state.day != undefined &&
                                <div>
                                    <label htmlFor='other-incident-date-picker'>
                                        Other incident date:
                                    </label>
                                    <DatePicker
                                        id='other-incident-date-picker'
                                        className='menu-input'
                                        selected={this.state.otherDay}
                                        onChange={this.updateOtherIncidentDate}
                                    />
                                </div>
                            }
                        </>
                    }
                </div>
                <div className='visualisation-container'>
                {
                    this.state.location != undefined &&
                    <>
                        <DelayMap
                            center={[mainStation.lat, mainStation.lng]}
                            stations={selectedStations}
                            connections={[]}
                            selectionCode={this.state.location}
                            timestamp={this.state.day}
                            metrics={[]}
                            styleFunction={this.basicStyleFunction}
                            />
                        {
                            this.state.otherDay != undefined &&
                            <DelayMap
                            center={[mainStation.lat, mainStation.lng]}
                            stations={selectedStations}
                            connections={[]}
                            selectionCode={this.state.location}
                            timestamp={this.state.otherDay}
                            metrics={[]}
                            styleFunction={this.basicStyleFunction}
                            />
                        }
                    </>
                }
                </div>
                          
            </div>
        );
    }
}

export {
    MapPage
};

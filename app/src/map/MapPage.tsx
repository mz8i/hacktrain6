import * as d3 from 'd3-scale-chromatic';
import * as _ from 'lodash';
import moment, { Moment } from 'moment';
import React from 'react';
import { Handles, Slider, Tracks} from 'react-compound-slider';
import DatePicker from 'react-datepicker';
import { Dropdown } from 'semantic-ui-react';

import 'leaflet/dist/leaflet.css';
import 'react-datepicker/dist/react-datepicker.css';
import './MapPage.css';

import { delays, delayTimes } from '../data/delays';
import { connectionsLookup } from '../data/stationConnections';
import { stations, stationsLookup } from '../data/stations';
import { withMemoize } from '../memoize';
import { Metric } from '../models/metric';
import { Station } from '../models/station';

import { DelayMap } from './DelayMap';

interface MapPageState {
    location?: string;
    day?: Date;
    otherDay?: Date;
    relativeTime: number;
}

function optionsFromStations(stations: Station[]) {
    if (stations == undefined) return [];
    return stations
        .map(s => ({
            text: s.name,
            value: s.code
        }))
        .sort((a, b) => a.text.localeCompare(b.text));
}

function getMetricsForDay(stationCode: string, date: Date) {
    if(date == undefined) return [];
    let dayData;
    if(date.getDate() == 17 && date.getMonth() == 8 && date.getFullYear() == 2019) {
        dayData = delays["2019-09-17"];
    } else if (date.getDate() == 29 && date.getMonth() == 5 && date.getFullYear() == 2019) {
        dayData = delays["2019-06-29"];
    } else {
        return [];
    }

    return dayData;
}

function getMetricsForTime(metricsForDay: {[code: string]: number[]}, offset: number): Metric[] {
    return Object.entries(metricsForDay).map(([code, metrics]) => ({
        stationCode: code,
        metric: metrics[offset]
    }));
}

function getIncidentTime(stationCode: string, date: Date): {hour: number, minute: number} {
    if (stationCode == undefined || date == undefined) return undefined;
    return delayTimes[formatLocalDate(date)];
}

function formatLocalDate(date: Date): string {
    let yearPart = date.getFullYear() + '';
    let monthPart = (date.getMonth() + 1).toString().padStart(2, '0');
    let dayPart = date.getDate().toString().padStart(2, '0');
    return `${yearPart}-${monthPart}-${dayPart}`;
}

function getSelectedStations(stationCode): Station[] {
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

/** Prepare data */

const stationOptions = optionsFromStations(stations);
const birminghamStationOptionValue = (stationOptions
    .filter(x => x.text === 'Birmingham New Street Rail Station'))[0].value;

class MapPage extends React.Component<{}, MapPageState> {

    memoizedGetSelectedStations = withMemoize(getSelectedStations);
    memoizedGetMetricsForLocationDateTime = withMemoize((location, date, time) => 
        getMetricsForTime(
            getMetricsForDay(location, date),
            time
        )
    );

    constructor(props) {
        super(props);
        this.state = {
            location: birminghamStationOptionValue,
            day: undefined,
            otherDay: undefined,
            relativeTime: 0
        };

        this.updateStation = this.updateStation.bind(this);
        this.updateIncidentDate = this.updateIncidentDate.bind(this);
        this.updateOtherIncidentDate = this.updateOtherIncidentDate.bind(this);
        this.updateOffset = this.updateOffset.bind(this);
    }

    basicStyleFunction = (s: Station & {metric: number}) => {
        // let color = s.metric == undefined ? 'gray' :
        //     d3.interpolateReds(s.metric / 2.0);
        let color;
        if (s.metric == undefined) color = 'gray';
        else if (s.metric > 1) color = '#E31A1C';
        else if (s.metric > 0.5) color = '#FF7F00';
        else color = '#33A02C';

        return {
            radius: s.code === this.state.location ? 12 : 8,
            fillColor: color,
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 1
        };
    }

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

    updateOffset(event) {
        this.setState({
            relativeTime: event.target.value
        });
    }

    render() {

        let selectedStations, mainStation;
        if(this.state.location != undefined) {
            selectedStations = this.memoizedGetSelectedStations(this.state.location);
            mainStation = stationsLookup[this.state.location];
        }

        const showFirstDatePicker =  this.state.location != undefined;
        const showFirstMap = showFirstDatePicker;
        const showSecondDatePicker = showFirstDatePicker && this.state.day != undefined;
        const showSlider = showSecondDatePicker;
        const showSecondMap = showSecondDatePicker && this.state.otherDay != undefined;

        


        return (
            <div className='map-page'>
                <div className="menu">
                    <div className='menu-input-group'>
                        <label htmlFor='station-picker'>
                            Station:
                        </label>
                        <Dropdown clearable
                            search={true}
                            id='station-picker'
                            className='menu-input'
                            options={stationOptions}
                            onChange={this.updateStation}
                            style={{border:'1px solid grey'}}
                            defaultValue={birminghamStationOptionValue}
                        />
                    </div>
                    {
                        showFirstMap &&
                        <div className='menu-input-group'>
                            <label htmlFor='incident-date-picker'>
                                Incident date:
                            </label>
                            <DatePicker
                                id='incident-date-picker'
                                className='menu-input'
                                selected={this.state.day}
                                onChange={this.updateIncidentDate}
                                openToDate={new Date("2019-09-17")}
                            />
                        </div>
                    }
                    {
                        showSecondDatePicker &&
                            <div className='menu-input-group'>
                                <label htmlFor='other-incident-date-picker'>
                                    Other incident date:
                                </label>
                                <DatePicker
                                    id='other-incident-date-picker'
                                    className='menu-input'
                                    selected={this.state.otherDay}
                                    onChange={this.updateOtherIncidentDate}
                                    openToDate={new Date("2019-06-29")}
                                />
                            </div>
                    }
                    {
                        showSlider &&
                        <div className='menu-input-group'>
                            <label htmlFor="slider">
                                Time from incident:
                            </label>
                            <input id="slider" className='menu-input' type='range' min={0} max={3} defaultValue={0} onChange={this.updateOffset}>

                            </input>
                        </div>
                    }
                </div>
                <div className='visualisation-container'>
                {
                    showFirstMap &&
                        <DelayMap
                            center={[mainStation.lat, mainStation.lng]}
                            stations={selectedStations}
                            connections={[]}
                            selectionCode={this.state.location}
                            timestamp={this.state.day}
                            metrics={
                                this.memoizedGetMetricsForLocationDateTime(
                                    this.state.location,
                                    this.state.day,
                                    this.state.relativeTime
                                )
                            }
                            incidentTime={getIncidentTime(this.state.location, this.state.day)}
                            relativeTime={this.state.relativeTime}
                            styleFunction={this.basicStyleFunction}
                        />
                }
                {
                    showSecondMap &&
                        <DelayMap
                            center={[mainStation.lat, mainStation.lng]}
                            stations={selectedStations}
                            connections={[]}
                            selectionCode={this.state.location}
                            timestamp={this.state.otherDay}
                            metrics={
                                this.memoizedGetMetricsForLocationDateTime(
                                    this.state.location,
                                    this.state.otherDay,
                                    this.state.relativeTime
                                )
                            }

                            incidentTime={getIncidentTime(this.state.location, this.state.otherDay)}
                            relativeTime={this.state.relativeTime}
                            styleFunction={this.basicStyleFunction}
                        />
                }
                </div>
                          
            </div>
        );
    }
}

export {
    MapPage
};

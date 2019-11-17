import { Feature } from 'geojson';
import L from 'leaflet';
import * as _ from 'lodash';
import React from 'react';
import { CircleMarker, LayerGroup, Map, TileLayer, Tooltip, Viewport } from 'react-leaflet-universal';

import './DelayMap.css';

import { stationsLookup } from '../data/stations';
import { Connection } from '../models/connection';
import { Metric } from '../models/metric';
import { Station } from '../models/station';

const mapboxToken = 'pk.eyJ1IjoibXo4aSIsImEiOiJjazMyOHhjcG8wZzBwM21xampxeDkyYmFnIn0.pU85lKhvn-Sx4ctxGKxS8w';

interface DelayMapProps {
    center?: [number, number];
    stations: Station[];
    connections: Connection[];
    selectionCode: string;
    timestamp: Date;
    metrics: Metric[];
    styleFunction?: (stationMetric: Station & { metric: number}) => any;
    viewport?: Viewport;
    onViewportChange?: (viewport: Viewport) => void;
}

function mergeStationsAndMetric(stations: Station[], metrics: Metric[]): (Station & {metric: number})[] {
    const metricsByCode = _.chain(metrics)
        .keyBy('stationCode')
        .value();

    console.log(metricsByCode);
    return stations.map(s => {
        let stationWithMetric: any = {...s};
        let metricByCode = metricsByCode[s.code];

        stationWithMetric.metric = metricByCode != undefined ? metricByCode.metric : undefined;
        return stationWithMetric;
    });
}

class DelayMap extends React.Component<DelayMapProps> {
    render() {
        const selectionName = stationsLookup[this.props.selectionCode].name;
        const markerKey = this.props.selectionCode + (this.props.timestamp == undefined ? 'undefined' : this.props.timestamp.toISOString());
        const mergedData = mergeStationsAndMetric(this.props.stations, this.props.metrics); 
        console.log(mergedData);
        return (
            <div className="map-container">
                <h2>
                    {selectionName}
                    {this.props.timestamp && 
                        <>
                            &nbsp;-&nbsp;
                            {
                                this.props.timestamp.toLocaleDateString([], {
                                    weekday: 'short',
                                    day: 'numeric',
                                    year: 'numeric',
                                    month: 'short',
                                    // hour:'numeric',
                                    // minute: 'numeric'
                                })
                            }
                        </>
                }
                </h2>
                <Map
                    center={this.props.center}
                    zoom={10}
                    minZoom={9}
                    maxZoom={19}
                >
                    <TileLayer url={`https://api.mapbox.com/styles/v1/mapbox/dark-v8/tiles/{z}/{x}/{y}?access_token=${mapboxToken}`} />
                    <LayerGroup key={'markers'+markerKey}>
                    {
                        mergedData &&
                            mergedData.map(s => (
                            <CircleMarker 
                                center ={[s.lat, s.lng]}
                                {...this.props.styleFunction(s)}
                            >
                                <Tooltip>{s.name}</Tooltip>
                            </CircleMarker>
                        ))
                    }
                    </LayerGroup>
                    <LayerGroup key={'lines'+markerKey}>

                    </LayerGroup>
                </Map>
            </div>
        );
    }
}

export {
    DelayMap
};

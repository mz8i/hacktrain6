import { Feature } from 'geojson';
import L from 'leaflet';
import React from 'react';
import { CircleMarker, LayerGroup, Map, TileLayer, Tooltip } from 'react-leaflet-universal';

import './DelayMap.css';

import { Connection } from '../models/connection';
import { Metric } from '../models/metric';
import { Station } from '../models/station';

import { stationsToGeojson } from './generateGeoJson';

const mapboxToken = 'pk.eyJ1IjoibXo4aSIsImEiOiJjazMyOHhjcG8wZzBwM21xampxeDkyYmFnIn0.pU85lKhvn-Sx4ctxGKxS8w';

interface DelayMapProps {
    center?: [number, number];
    stations: Station[];
    connections: Connection[];
    selectionCode: string;
    timestamp: Date;
    metrics: Metric[];
    styleFunction?: (stationMetric: Station) => any;
}

class DelayMap extends React.Component<DelayMapProps> {
    render() {
        // const data = stationsToGeojson(this.props.stations, this.props.metrics);

        const markerKey = this.props.selectionCode + (this.props.timestamp == undefined ? 'undefined' : this.props.timestamp.toISOString());
        return (
            <div className="map-container">
                <Map
                    center={this.props.center}
                    zoom={10}
                    minZoom={9}
                    maxZoom={19}
                >
                    <TileLayer url={`https://api.mapbox.com/styles/v1/mapbox/dark-v8/tiles/{z}/{x}/{y}?access_token=${mapboxToken}`} />
                    <LayerGroup key={'markers'+markerKey}>
                    {
                        this.props.stations &&
                        this.props.stations.map(s => (
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

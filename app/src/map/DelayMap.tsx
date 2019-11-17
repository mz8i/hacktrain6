import { Feature } from 'geojson';
import React from 'react';
import { GeoJSON, Map, TileLayer } from 'react-leaflet-universal';

import './DelayMap.css';

import { Metric } from '../models/metric';
import { Station } from '../models/station';

import { stationsToGeojson } from './generateGeoJson';

const mapboxToken = 'pk.eyJ1IjoibXo4aSIsImEiOiJjazMyOHhjcG8wZzBwM21xampxeDkyYmFnIn0.pU85lKhvn-Sx4ctxGKxS8w';

interface DelayMapProps {
    center?: [number, number];
    stations: Station[];
    metrics: Metric[];
    styleFunction?: (feature: Feature) => any;
}

class DelayMap extends React.Component<DelayMapProps> {
    render() {
        const data = stationsToGeojson(this.props.stations, this.props.metrics);
        return (
            <div className="map-container">
                <Map
                    center={this.props.center}
                    zoom={10}
                    minZoom={9}
                    maxZoom={19}
                >
                    <TileLayer url={`https://api.mapbox.com/styles/v1/mapbox/dark-v8/tiles/{z}/{x}/{y}?access_token=${mapboxToken}`} />
                    <GeoJSON data={data} style={this.props.styleFunction}/>
                </Map>
            </div>
        );
    }
}

export {
    DelayMap
};

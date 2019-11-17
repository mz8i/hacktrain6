import { GeoJSON } from "geojson";

import { Metric } from "../models/metric";
import { Station } from "../models/station";

export function stationsToGeojson(stations: Station[], metrics: Metric[]): GeoJSON {
    return {
        type: 'FeatureCollection',
        features: stations.map(s => ({
            type: 'Feature',
            geometry: {
                type: 'Point',
                coordinates: [s.lng, s.lat]
            },
            properties: {

            }

        }))
    };
}

// import * as _ from 'lodash';

import { Station } from './models/station';

export const stations: Station[] = [
    {
        code: 'BRMGHM',
        name: 'Birmingham New Street',
        lat: 52.476515,
        lng: -1.899737,
        connections: []
    }
];

// const stationsLookup = _.chain(stations)
//     .keyBy('code')
//     .value();

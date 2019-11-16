import * as _ from 'lodash';

const stations = [
    {
        code: 'WCHAPEL',
        name: 'Whitechapel'
    }
];

const stationsLookup = _.chain(stations)
    .keyBy('code')
    .value();



export {
    stations,
    stationsLookup
};

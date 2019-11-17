export interface Station {
    code: string;
    name: string;
    lat: number;
    lng: number;
    connections?: string[];
}

export interface Image {
    sopinstanc: string;
    sopclassui: string;
    imagenumbe: string;
    imagedate: string;
    imagetime: string;
    echonumber: string;
    numberoffr: string;
    acqdate: string;
    acqtime: string;
    receivingc: string;
    acqnumber: string;
    slicelocat: string;
    samplesper: string;
    photometri: string;
    rows: string;
    colums: string;
    bitsstored: string;
    imagetype: string;
    imageid: string;
    imagepat: string;
    seriesinst: string;
    accesstime: number;
    qtimestamp: number;
    qflags: number;
    qspare: string;
    objectfile: string;
    devicename: string;
}

export interface Patient {
    patientid: string;
    patientnam: string;
    patientbir: string;
    patientsex: string;
    accesstime: number;
    qtimestamp: number;
    qflags: number;
    qspare: string;
}

export interface Roi {
    roiid: number;
    name: string;
    priority: number;
}

export interface RClass {
    classid: number;
    parentclassid: number;
    name: string;
}

export interface Feature {
    radiomicfeatureid: number;
    radiomicclassid: number;
    name: string;
}

export interface FeatureValue {
    id: number;
    radiomicsid: number;
    roiid: number;
    filterid: number;
    classid: number;
    featureid: number;
    value: string;
}

export interface RFilter {
    filterid: number;
    name: string;
}

export interface Radiomics {
    radiomicsid: number;
    radiomicpat: string;
    radiomicseriesofimageslicesmodality: string;
    radiomicseriesofimageslices: string;
    radiomicrtstructseries: string;
    timeofcalculation: Date;
}

export interface Series {
    seriesinst: string;
    seriesnumb: string;
    seriesdate: string;
    seriestime: string;
    seriesdesc: string;
    modality: string;
    patientpos: string;
    contrastbo: string;
    manufactur: string;
    modelname: string;
    bodypartex: string;
    protocolna: string;
    stationnam: string;
    institutio: string;
    frameofref: string;
    seriespat: string;
    studyinsta: string;
    accesstime: number;
    qtimestamp: number;
    qflags: number;
    qspare: string;
}

export interface SeriesRoi {
    id: number;
    roiid: number;
    seriesinst: string;
    number: number;
    dicomsegfile: string;
}

export interface Study {
    studyinsta: string;
    studydate: string;
    studytime: string;
    studyid: string;
    studydescr: string;
    accessionn: string;
    referphysi: string;
    patientsag: string;
    patientswe: string;
    studymodal: string;
    patientnam: string;
    patientbir: string;
    patientsex: string;
    patientid: string;
    accesstime: number;
    qtimestamp: number;
    qflags: number;
    qspare: string;
}

import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, Subscriber } from 'rxjs';
import { Dicom } from '../models/DicomSelection';


@Injectable({
  providedIn: 'root'
})
export class DataService {

  private baseUrl = 'http://localhost:8000';
  public headers = new Headers({ 'Content-Type': 'application/json' });

  constructor(private httpClient: HttpClient) { }

// data retrieval from backend

  getDicomTable(dicom: Dicom): Observable<any> {
    return this.httpClient.get(`${(this.baseUrl)}${dicom.url}`);
  }

  getCalculationList() {
    return this.httpClient.get<any[]>(`${(this.baseUrl)}` + '/calc-list/');
  }

  getOverview(): Observable<any> {
    return this.httpClient.get(`${(this.baseUrl)}` + '/overview/');
  }

// file handling

  openRequestFile(name: string) {
    return this.httpClient.get(`${(this.baseUrl)}${name}`, {responseType: 'text'});
  }

  writeToFile(method: string, fileType: string, data: string) {
    return this.httpClient.put(`${(this.baseUrl)}${method}${fileType}`, data);
  }

// currently not in use - request script be run in the backend
  runScript(option: string) {
    return this.httpClient.get(`${(this.baseUrl)}${option}`);
  }

// download zip file
  downloadZip(filetype: string) {
    return this.httpClient.get(`${(this.baseUrl)}${filetype}`, {
            responseType: 'arraybuffer'}
    );
  }

// delete calculation
  deleteCalc(name: string, toDelete: any[]) {
    return this.httpClient.post(`${(this.baseUrl)}${name}`, toDelete);
  }

// feature calculation - sends specific commands to the backend
  sendCommand(command: string): Observable<any> {
    return this.httpClient.get(`${(this.baseUrl)}/${command}/`);
  }

// Region of Interest priority requests

  getPriority(name: string) {
    return this.httpClient.get(`${(this.baseUrl)}${name}`);
  }

  changePriority(name: string, roiList: any[]) {
    return this.httpClient.post(`${(this.baseUrl)}${name}`, roiList);
  }

}

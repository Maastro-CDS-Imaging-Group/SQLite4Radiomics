import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, Subscriber } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class PingService {
  private baseUrl = 'http://localhost:8000';
  public headers = new Headers({ 'Content-Type': 'application/json' });

  constructor(private httpClient: HttpClient) { }

  ping(route: string): Observable<any> {
    return this.httpClient.get(`${(this.baseUrl)}${route}/`);
  }

}

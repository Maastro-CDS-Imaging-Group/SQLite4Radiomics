import { Injectable, OnDestroy } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { Observable, of } from 'rxjs';
import { map, switchMap, retryWhen, delay} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class WebsocketService implements OnDestroy {
  connection$: WebSocketSubject<any>;
  RETRY_SECONDS = 10;

  constructor() { }

  ngOnDestroy() {
    this.closeConnection();
  }



  connect(text: string): Observable<any> {
    return of('http://localhost:8000').pipe(
      // https becomes wws, http becomes ws
      map(apiUrl => apiUrl.replace(/^http/, 'ws') + `${text}`),
      switchMap(wsUrl => {
        if (this.connection$) {
          return this.connection$;
        } else {
          this.connection$ = webSocket(wsUrl);
          return this.connection$;
        }
      }),
      retryWhen((errors) => errors.pipe(delay(this.RETRY_SECONDS)))
    );
  }

  send(data: any) {
    if (this.connection$) {
      this.connection$.next(data);
    } else {
      console.error('Did not send data, open a connection first');
    }
  }

  closeConnection() {
    if (this.connection$) {
      this.connection$.complete();
      this.connection$ = null;
    }
  }


}

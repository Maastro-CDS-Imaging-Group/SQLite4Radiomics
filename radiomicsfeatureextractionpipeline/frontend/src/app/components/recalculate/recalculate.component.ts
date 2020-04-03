import { Message } from './../../models/Message';
import { Component, OnInit,/*, OnDestroy,*/ 
Inject} from '@angular/core';
//import { WebsocketService } from '../../services/websocket.service';
import {MatSnackBarRef,/*, MAT_SNACK_BAR_DATA*/
MAT_SNACK_BAR_DATA} from '@angular/material';//
//import { Message } from '@angular/compiler/src/i18n/i18n_ast';
//import { Subject } from 'rxjs';
//import { takeUntil, map } from 'rxjs/operators';
import { DataService } from "../../services/data.service";
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-recalculate',
  templateUrl: './recalculate.component.html',
  styleUrls: ['./recalculate.component.css']
})



export class RecalculateComponent implements OnInit/*, OnDestroy*/ {
  // messages: Message[] = [];
  // destroyed$ = new Subject();
  //private text: string;
  public message: Message = null;
  public messages: Message[] = [];
  private command: string;
  constructor(/*private webSocket: WebsocketService,*/ private dataService: DataService,
                                                       public snackbarRef: MatSnackBarRef<RecalculateComponent>,
                                                       @Inject(MAT_SNACK_BAR_DATA) public data: any) {
                                                         this.command = data;
                                                       }

  ngOnInit() {
    // this.webSocket.connect('/progress-message/').pipe(
    //   takeUntil(this.destroyed$)
    // ).subscribe(messages => this.messages.push(messages));
    // this.sendMessage(this.text);

    // send command to start the calculation process, and push the message
    this.dataService.sendCommand(this.command).pipe(map(result => {
      Object.keys(result).forEach((element) => {
        this.message = new Message(result[element]);
      });
    })).subscribe((result) => {
      this.messages.push(this.message);
    });

    this.requestProgress('progress');

  }

  // Request progress on the calculation process periodically
  requestProgress(value: string) {
    // this.text = value;
    // this.webSocket.send({ message: this.text });
    // this.text = '';

    this.dataService.sendCommand(value).pipe(map(result => {
      Object.keys(result).forEach((element) => {
        this.message = new Message(result[element]);
      });
    })).subscribe((result) => {
      this.messages.push(this.message);
      if ( this.message.text === 'No process running or the process has finished') {
          setTimeout(() => this.snackbarRef.dismiss(), 5000);
        } else {
          setTimeout(() => this.requestProgress(value), 7000);
        }
      });
  }

  // send a cancel command and push the returned message
  onCancel(): void {
    this.dataService.sendCommand('cancel').pipe(map(result => {
      Object.keys(result).forEach((element) => {
        this.message = new Message(result[element]);
      });
    })).subscribe((result) => {
      this.messages.push(this.message);
    });
  }

  // ngOnDestroy() {
  //   this.destroyed$.next();
  // }

}

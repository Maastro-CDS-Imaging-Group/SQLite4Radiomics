import { Component, AfterViewInit, Input, Output, ViewChild } from '@angular/core';
import { OpenfileDialogComponent } from '../openfile-dialog/openfile-dialog.component';
import { HelpDialogComponent } from '../help-dialog/help-dialog.component';
import { RecalculateComponent } from '../recalculate/recalculate.component';
import { EventEmitter } from 'events';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { DataService } from '../../services/data.service';
import { MatSnackBar, MatSnackBarConfig } from '@angular/material/snack-bar';
import { PrioritySetterComponent } from '../priority-setter/priority-setter.component';
import { DeleteCsvComponent } from '../delete-csv/delete-csv.component';


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements AfterViewInit {

  @ViewChild(OpenfileDialogComponent, {static: false})
  @ViewChild(HelpDialogComponent, {static: false})
  @ViewChild(RecalculateComponent, {static: false})
  @Output() openFileEvent = new EventEmitter();
  private text: string;
  private fileType: string;
  private activated = false;

  constructor(public dialog: MatDialog, private dataService: DataService, public snackbar: MatSnackBar ) { }

  ngAfterViewInit() {
    // checks if there is any uncalculated data that needs to be processed
    this.checkForUpdatedData('start-calculate');
  }

  // Gets the file's content and passes it to the openfile component, opening it as a dialog and subscribes to the result
  openFile(name: string): void {
    this.dataService.openRequestFile(name).subscribe((result) => {
      this.text = result.toString();
      const dialogConfig = new MatDialogConfig();
      dialogConfig.data = this.text;
      const openFileDialogRef = this.dialog.open(OpenfileDialogComponent, dialogConfig);
      openFileDialogRef.afterClosed().subscribe(result => {
        if (result === undefined) {
          console.log('i am undefined');
        } else if (result.toString() === '/restore-old') {
          this.dataService.writeToFile(result, this.fileType, '').subscribe();
        } else if (result.toString() === '/restore-default') {
          this.dataService.writeToFile(result, this.fileType, '').subscribe();
        } else {
          this.dataService.writeToFile('/write', this.fileType, result).subscribe();
        }
      });
    });
  }

  //  get the file type, parameter file or configuration file
  getType(fileType: string): void {
    this.fileType = fileType;
  }

  // open the help component as a dialog
  openHelp() {
    this.dialog.open(HelpDialogComponent);
  }

  // run a script from the backend, not currently used
  callScript(option: string) {
    this.dataService.runScript(option).subscribe();
  }


  // download from the backend the files specified
  downloadZipFile(typeofFile: string) {
    this.dataService.downloadZip(typeofFile).subscribe(response => {
        this.downloadFile(response, 'application/zip');
      },
      (error) => {
        alert('Something went wrong! No files found.');
    });
  }

  // execute the download of the file withoutopening a new tab
  downloadFile(data: any, type: string) {
    const blob = new Blob([data], { type: type});
    const url = window.URL.createObjectURL(blob);
    window.location.href = url;
  }

  // issue recalculation on all data currently stored
  recalculate(name: string): void {
    //this.dataService.runScript(name).subscribe();
    //this.text = name.toString();

    // if there is no snackbar currently active, open the recalculate component as a snackbar and subscribe to the result
    if (!this.activated) {
      this.activated = true;
      const recalculateConfig = new MatSnackBarConfig();
      recalculateConfig.data = name;
      const recalculateRef = this.snackbar.openFromComponent(RecalculateComponent, recalculateConfig);
      recalculateRef.afterDismissed().subscribe(() => {
        // reset boolean
        this.activated = false;
      });
    } else if (this.activated) {
      alert('A calculation is already running!');
    }
  }

  // function to check if there is any uncalculated data
  checkForUpdatedData(name: string): void {
    this.activated = true;
    const recalculateConfig = new MatSnackBarConfig();
    recalculateConfig.data = name;
    const recalculateRef = this.snackbar.openFromComponent(RecalculateComponent, recalculateConfig);
    recalculateRef.afterDismissed().subscribe(() => {
      this.activated = false;
    });
  }

  // delete csv files int he backend
  // open reinitialize component (dialog) and subscribe o result
  deleteCSV(): void {
    const deletecsvDialogRef = this.dialog.open(DeleteCsvComponent);
    deletecsvDialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if (result === undefined) {
      } else if (result.toString() === 'yes') {
        this.dataService.runScript('/delete-csv/').subscribe((response) => {
          alert( 'All csv files deleted!');
          },
          (error) => {
              alert('Something went wrong! No files found.');
        });
      }
    });
  }
}

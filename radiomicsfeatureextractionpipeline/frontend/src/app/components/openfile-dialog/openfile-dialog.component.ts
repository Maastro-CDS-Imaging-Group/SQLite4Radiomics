import { Component, OnInit, Input, Output, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';


@Component({
  selector: 'app-openfile-dialog',
  templateUrl: './openfile-dialog.component.html',
  styleUrls: ['./openfile-dialog.component.css']
})
export class OpenfileDialogComponent implements OnInit {
  private text: string;

  constructor(public dialogRef: MatDialogRef<OpenfileDialogComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) {
                this.text = data;
              }


  ngOnInit() {
  }

  onCancelClick(): void {
    this.dialogRef.close();
  }

  onRestore(option: string): void {
    this.dialogRef.close(option);

  }

}

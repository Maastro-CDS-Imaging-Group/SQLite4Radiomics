import { Component, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';

@Component({
  selector: 'app-re-initialize',
  templateUrl: './re-initialize.component.html',
  styleUrls: ['./re-initialize.component.css']
})
export class ReInitializeComponent implements OnInit {

  constructor(public dialogRef: MatDialogRef<ReInitializeComponent>) { }

  ngOnInit() {
  }

  onCancelClick(): void {
    this.dialogRef.close();
  }

  onYes(choice: string): void {
    this.dialogRef.close(choice);
  }
}

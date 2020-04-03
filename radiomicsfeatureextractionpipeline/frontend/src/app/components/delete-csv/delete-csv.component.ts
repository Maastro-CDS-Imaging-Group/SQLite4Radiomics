import { Component, OnInit } from '@angular/core';
import { MatDialogRef } from '@angular/material';

@Component({
  selector: 'app-delete-csv',
  templateUrl: './delete-csv.component.html',
  styleUrls: ['./delete-csv.component.css']
})
export class DeleteCsvComponent implements OnInit {

  constructor(public dialogRef: MatDialogRef<DeleteCsvComponent>) { }

  ngOnInit() {
  }

  onCancelClick(): void {
    this.dialogRef.close();
  }

  onYes(choice: string): void {
    this.dialogRef.close(choice);
  }

}

import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { FormBuilder, FormGroup, Validators, FormControl } from '@angular/forms';

@Component({
  selector: 'app-priority-setter',
  templateUrl: './priority-setter.component.html',
  styleUrls: ['./priority-setter.component.css']
})
export class PrioritySetterComponent implements OnInit {
  private roiList: Array<any>;
  constructor(fb: FormBuilder, public dialogRef: MatDialogRef<PrioritySetterComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) {
      this.roiList = data;
    }

  ngOnInit() {
  }

  onCancel(): void {
    this.dialogRef.close();
  }

  onSubmit(): void {
    if (this.roiList.find(element => element.priority === -1) !== undefined) {
      alert('Invalid input! Only values between 1 and 10 are accepted.');
    } else {
      this.dialogRef.close(this.roiList);
    }
  }

}

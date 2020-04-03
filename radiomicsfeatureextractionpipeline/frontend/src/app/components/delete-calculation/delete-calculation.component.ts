import { Component, Output, EventEmitter, ViewChild, AfterViewInit, Inject, ViewEncapsulation } from '@angular/core';
import { Moment } from 'moment';
import * as moment from 'moment';
import { MatCalendar, MatCalendarCellCssClasses } from '@angular/material';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { Calculation } from 'src/app/models/Calculation';


@Component({
  selector: 'app-delete-calculation',
  templateUrl: './delete-calculation.component.html',
  styleUrls: ['./delete-calculation.component.css'],
  encapsulation: ViewEncapsulation.None
})
export class DeleteCalculationComponent implements AfterViewInit {
  @Output()
  dateSelected: EventEmitter<Moment> = new EventEmitter();
  calculations: Calculation[];

  @Output()
  selectedDate = moment();

  @ViewChild('calendar', {static: false})
  calendar: MatCalendar<Moment>;
  private dateList: Moment[] = [];
  private temp: Calculation[] = [];


  constructor(public dialogRef: MatDialogRef<DeleteCalculationComponent>,
              @Inject(MAT_DIALOG_DATA) public data: any) {
      // take injected data a map it to the calendar
      this.calculations = data;
      this.calculations.map(a => {
        const date =  moment(a.calculation_date);
        this.dateList.push(date);
      });
    }

  ngAfterViewInit() {

  }

  // When a user clicks on a different date, load the calculations for that date
  dateChanged() {
    this.temp = [];
    this.calendar.activeDate = this.selectedDate;
    this.dateSelected.emit(this.selectedDate);
    this.dateList.forEach(element => {
      if (element.isSame(this.selectedDate, 'day')) {
        this.calculations.forEach(calc => {
          if ( moment(calc.calculation_date).isSame(element)) {
            this.temp.push(calc);
          }
        });
      }
    });
  }

  // go back to current date
  today() {
    this.selectedDate = moment();
    this.dateChanged();
  }

  // class for making special dates highlighted in the calendar
  dateClass() {
    return (date: Moment): MatCalendarCellCssClasses => {
      const highlightDate = this.dateList
        .some(d => d.isSame(date, 'day'));

      return highlightDate ? 'special-date' : '';
    };
  }

  // gets the selected dates and pushes them to a list, which is returned when closing the dialog
  delete(selected: Array<any>) {
    const toDelete: Calculation[] = [];
    this.calculations.forEach(calculation => {
      selected.forEach(element => {
        if (calculation.calculation_date === element.value.calculation_date && calculation.Value === element.value.Value) {
          toDelete.push(calculation);
        }
      });
    });
    this.dialogRef.close(toDelete);
  }

  // closes the dialog
  onCancelClick(): void {
    this.dialogRef.close();
  }

}

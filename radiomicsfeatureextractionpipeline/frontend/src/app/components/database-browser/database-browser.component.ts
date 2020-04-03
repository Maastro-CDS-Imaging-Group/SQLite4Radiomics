import { Component, AfterViewInit, Output, EventEmitter } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTable } from '@angular/material';
import { MatDialog, MatDialogConfig } from "@angular/material/dialog";
import { ReInitializeComponent } from "../re-initialize/re-initialize.component";
import { DeleteCalculationComponent } from "../delete-calculation/delete-calculation.component";

/** Data service and models */
import { DataService } from '../../services/data.service';
import { Dicom } from '../../models/DicomSelection';
import { Calculation } from '../../models/Calculation';
import { map } from 'rxjs/operators';
import { PrioritySetterComponent } from '../priority-setter/priority-setter.component';

@Component({
  selector: 'app-database-browser',
  templateUrl: './database-browser.component.html',
  styleUrls: ['./database-browser.component.css']
})


export class DatabaseBrowserComponent implements AfterViewInit {

  private dataSource: MatTableDataSource<any>;
  private calculations: Calculation[] = [];
  private toDelete: any[] = [];

  displayedColumns = [];

  @ViewChild(MatTable, { static: false }) table: MatTable<any>;
  @ViewChild(MatPaginator, { static: false }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: false }) sort: MatSort;
  @ViewChild(PrioritySetterComponent, {static: false})
  @Output() openFileEvent = new EventEmitter();

  private dicom: Dicom;

  constructor(private dataService: DataService, public dialog: MatDialog) {
    // Assign the data to the data source for the table to render
    this.dataSource = new MatTableDataSource();
  }


  dicomControl = new FormControl('', [Validators.required]);
  selectFormControl = new FormControl('', Validators.required);
  // Dicom table names and respective URLs to send GET reques
  dicoms: Dicom[] = [
    { name: 'DICOMPatients', url: '/patients/' },
    { name: 'DICOMImages', url: '/images/' },
    { name: 'DICOMROI', url: '/roi/' },
    { name: 'DICOMRadiomicClass', url: '/radiomic-class/' },
    { name: 'DICOMRadiomicFeature', url: '/feature/' },
    { name: 'DICOMRadiomicFeatureValue', url: '/feature-value/' },
    { name: 'DICOMRadiomicFilter', url: '/radiomic-filter/' },
    { name: 'DICOMRadiomics', url: '/radiomics/' },
    { name: 'DICOMSeries', url: '/series/' },
    { name: 'DICOMSeriesROI', url: '/series-roi/' },
    { name: 'DICOMStudies', url: '/study/' },
  ];

  ngAfterViewInit() {
  }

  // filter data in the table based on a stirng value provided
  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  // everytime a different table name is selected, refresh table
  dataChange(dicom: Dicom): void {
    this.dicom = dicom;
    this.dataService.getDicomTable(dicom).subscribe((result) => {
      this.dataSource.data = result;
      this.addColumns();
      this.refreshTableRender();
    });
  }

  // add data to table columns
  addColumns(): void {
    this.displayedColumns = Object.keys(this.dataSource.data[0]);
    console.log(Object.keys(this.dataSource.data[0]));
    console.log(this.displayedColumns);
  }

  // reload paginator, sorting and the rendered rows
  refreshTableRender(): void {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
    this.table.renderRows();
  }

  // reload data
  refresh(): void {
    this.dataChange(this.dicom);
  }

  // open reinitialize component (dialog) and subscribe o result
  reInitialize(): void {
    const reinitializeDialogRef = this.dialog.open(ReInitializeComponent);
    reinitializeDialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if (result === undefined) {
      } else if (result.toString() === 'yes') {
        this.dataService.runScript('/recreate-radiomic-tables/').subscribe(); // perhaps exception handling here
        alert( 'The tables have been re-initialized!');
      }
    });
  }

  // Opens the delete-calculation component as a dialog and subscribes to the result
  onDeleteCalc(): void {
    // Get calculations and create calculaion object, push said object to a list
    this.dataService.getCalculationList().pipe(map(calc => {
      calc.forEach(element => {
        this.calculations.push(new Calculation(element.Value, element.calculation_date));
      });
    }))
    .subscribe((response) => {
      // open the dialog with the data from the request
      const dialogConfig = new MatDialogConfig();
      console.log(this.calculations);
      dialogConfig.data = this.calculations;
      const deleteCalcRef = this.dialog.open(DeleteCalculationComponent, dialogConfig);
      deleteCalcRef.afterClosed().subscribe(result => {
        console.log(result);
        if (result !== undefined && (result as Array<Calculation>).length > 0) {
          result.forEach(element => {
            // if there is an array of calculation returned from the closed dialog, push them to a list
            this.calculations.forEach(calculation => {
              if (calculation === element) {
                this.toDelete.push(calculation);
              }
            });
          });
          // delete calculations
          this.dataService.deleteCalc('/delete-calc/', this.toDelete).subscribe(); // perhaps exception handling here
          alert( 'Calculation(s) deleted!');
        }
      });
    });

    // reset variables
    this.calculations = [];
    this.toDelete = [];
  }

  // gets the priority data from the backend, passes it to the priority-setter component (opened as a dialog) and subscribes to the result
  prioritySet(name: string) {
    this.dataService.getPriority(name).subscribe((response) => {
      const dialogConfig = new MatDialogConfig();
      dialogConfig.data = response;
      const prioritySetterRef = this.dialog.open(PrioritySetterComponent, dialogConfig);
      prioritySetterRef.afterClosed().subscribe(result => {
        console.log(result);
        if (result !== undefined) {
          this.dataService.changePriority('/change-priority/', result).subscribe();
          alert('Successfully saved!');
        }
      });
    });
  }
}

